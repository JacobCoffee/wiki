# CPythonVmInternals

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# Some Pointers 

The most [relevant files](http://svn.python.org/view/python/trunk/Python/) are:

- ceval.\[ch\] (VM engine)

- compile.\[ch\] (Bytecode compiler)

- frameobject.\[ch\] (execution frames)

- opcode.h (bytecodes)

- code.h (PyCodeObject)

- pystate.\[ch\] (interpreter state)

- pythonrun.\[ch\] (entry point)

Particularly useful pieces of documentation:

- [Execution Model](http://docs.python.org/ref/execmodel.html)

- [GIL](http://docs.python.org/api/threads.html)

- [Bytecodes](http://docs.python.org/lib/bytecodes.html)

- [Disassembler](http://docs.python.org/lib/module-dis.html)

# Notes on the implementation 

Unless otherwise noted, the source file in question is Python/ceval.c.

## Control Flow 

The calling sequence is: main() (in python.c) -\> Py_Main() (main.c) -\> PyRun_FooFlags() (pythonrun.c) -\> run_bar() (pythonrun.c) -\> PyEval_EvalCode() (ceval.c) -\> PyEval_EvalCodeEx() (ceval.c) -\> PyEval_EvalFrameEx() (ceval.c).

PyRun_FooFlags() also calls PyParser_ASTFromQuux() to obtain an AST which run_bar() then passes to PyAST_Compile() (in compile.c) to get a PyCodeObject for PyEval_EvalCode().

EvalCodeEx() does some initialization (creating a new execution frame, argument processing, and some generator-specific stuff) before calling EvalFrameEx() which contains the main interpreter loop.

## Threads 

PyEval_InitThreads() initializes the GIL (interpreter_lock) and sets main_thread to the (threading package dependent) ID of the current thread. Thread state switching is done using PyThreadState_Swap(), which sets \_PyThreadState_Current (both defined in pystate.c) and PyThreadState_GET() (an alias for \_PyThreadState_Current) (pystate.h).

The actual thread switching occurs by releasing the GIL (Python doesn\'t dispatch threads at all; it just releases the GIL, giving the operating system permission to wake up a different thread - which the operating system may or may not chose to do. After some time, the original thread will try to reacquire the GIL. Assuming the OS applies fairness, it will not get it back if a different thread was also waiting for it, so our thread will block - and **then** the OS will dispatch (at latest)). See *Periodic Tasks* below.

## Async Callbacks 

Asynchronous callbacks can be registered by adding the function to be called to pendingcalls\[\] (see Py_AddPendingCall()). The state of this queue is communicated to the main loop via things_to_do.

## State 

The global state is recorded in a (per-process) PyInterpreterState struct and a per-thread PyThreadState struct. In principle, multiple interpreter states are supported per process (and the current interpreter is identified by thread). However, there are many limitations and quirks in the multiple-interpreter code.

Each execution frame\'s state is contained in that frame\'s PyFrameObject (which includes the instruction stream, the environment (globals, locals, builtins, etc.), the value stack and so forth). EvalFrameEx()\'s local variables are initialized from this frame object. A lot of stuff also lives on the regular C stack, which exists in parallel to the frame object stack.

## Instruction Stream 

The instruction stream looks as follows (c.f. assemble_emit() in compile.c and dis.py for the inverse operation): A byte stream where each instruction consists of either

- a single byte opcode: OP
- a single byte opcode plus a two-byte immediate argument: OP LO HI
- a special opcode followed by the first two bytes of the argument, followed by the real opcode and the remaining two bytes of the argument: EXTENDED_ARG ARG ARG OP ARG ARG

## Opcode Prediction 

One neat trick used to speed up opcode dispatch is the following: Using the macros PREDICT() and PREDICTED() it is sometimes possible to jump directly to the code implementing the next instruction rather than having to go through the whole loop preamble, e.g.

    case FOO:
          // ...
          PREDICT(BAR);
          continue;

    PREDICTED(BAR);
    case BAR:
         // ...

    expands to

    case FOO:
          // ...
          if (*next_instr == BAR) goto PRED_BAR;
          continue;

    PRED_BAR: next_instr++;
    case BAR:
          // ...

## Main Loop 

### Variables and macros used in EvalFrameEx() 

The value stack:

      PyObject **stack_pointer;

The instruction stream:

      unsigned char *next_instr;

NEXTOP(), NEXTARG(), PEEKARG(), JUMPTO(), and JUMPBY() simply fiddle with next_instr. Likewise for TOP(), SET_SECOND(), PUSH(), POP(), etc. and stack_pointer.

Current opcode plus argument:

      int opcode;
      int oparg;

Error status:

      enum why_code why; // no, exn, exn re-raised, return, break, continue, yield
      int err;           // non-zero is error

The environment:

      PyObject *names;
      PyObject *consts;

and

      PyObject **fastlocals;

which is accessed via GETLOCAL() and SETLOCAL().

Finally, there are some more PyObject \*\'s (v, w, u, and so forth, used as temporary variables) as well as

      PyObject *retval;

### Basic structure 

    EvalFrameEx() {
        why = WHY_NOT;
        err = 0;

        for (;;) {    <------------------+---+
            // do periodic tasks         |   |
                                         |   |
        fast_next_opcode:                |   |
            opcode = NEXTOP();           |   |
            if (HAS_ARG(opcode))         |   |
                oparg = NEXTARG();       |   |
                                         |   |
        dispatch_opcode:                 |   |
            switch(opcode) {             |   |
                                         |   |
            continue; -------------------+   |
                                             |
            break; ----------------------+   |
                                         |   |
            // Also, opcode prediction   |   |
            // jumps around inside the   |   |
            // switch statement          |   |
                                         |   |
            }    <-----------------------+   |
                                             |
        on_error:                            |
            // no error: continue -----------+
            // otherwise why == WHY_EXCEPTION after this

        fast_block_end:
            // unwind stacks if there was an error
        }

        // more unwinding

    fast_yield:
        // reset current thread's exception info
    exit_eval_frame:
        // set thread's execution frame to previous execution frame
        return retval;
    }

### Periodic Tasks 

By checking and decrementing \_Py_Ticker, the main loop executes certain tasks once every \_Py_CheckInterval iterations (in fact Py_AddPendingCall() sets \_Py_Ticker to zero, ensuring that pending calls are executed right after the next instruction which doesn\'t jump to fast_next_opcode):

- If there are things_to_do, Py_MakePendingCalls() is called.

- The GIL is releases and re-acquired, giving other threads a chance to run.

### Instruction implementation 

Some general notes:

- Successful instructions either goto fast_next_opcode or continue.

- Unsuccessful instructions break out of the switch.

- The value stack holds only PyObject \*\'s.

- Instructions must take care to Py_INCREF() and Py_DECREF() the reference counts of PyObject\'s whose addresses have been pushed onto/popped off the value stack.

- \"New\" objects are transferred onto the value stack by GETITEM()ing them from consts or names, or by GETLOCAL()ing them using oparg as an offset into fastlocals (c.f. LOAD\_\* instructions).

- err is used as a general \"error occurred\" flag, both inside the code implementing an opcode and \"globally\" for the entire loop.

### Nested blocks 

Nested loop and try blocks are handled as follows: Each frame maintains a block stack; when entering a nested block, a SETUP\_\* instruction adds a PyTryBlock to the PyFrameObject\'s f_blockstack and registers that block\'s type (instruction which created the block), handler (offset into the instruction stream) and level (value stack level before the nested block was entered).

When such blocks are exited normally (e.g. last iteration of a loop), the final POP_BLOCK instruction restores the value stack to the state it was in before the block.

If a block is exited abnormally (e.g. a break instruction), the code following fast_block_end unwinds the value stack and jumps to the block\'s handler. Certain instructions, e.g. RETURN_VALUE, cause the entire block stack to be unwound (leading to multiple unwinds of the value stack).

See also the comments in compile.c (compiler_try_finally()) which include nice ASCII art diagrams.

### Error handling 

Internal errors (bad oparg, say) generally result in why being set to WHY_EXCEPTION and breaking out of the switch (if the code implementing the instruction doesn\'t set why, the code after on_error will).

The code following fast_block_end will jump to the correct exception handler and set the global exception related variables (exception information is stored in the current execution frame and the thread state. See set_exc_info() and reset_exc_info()).
