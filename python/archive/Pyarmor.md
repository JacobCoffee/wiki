# Pyarmor

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# Pyarmor 

Pyarmor is a command line tool used to obfuscate python scripts, bind obfuscated scripts to fixed machine or expire obfuscated scripts. It protects Python scripts by the following ways:

- Obfuscate code object to protect constants and literal strings.
- Obfuscate byte code of each code object.
- Clear f_locals of frame as soon as code object completed execution.
- Expired obfuscated scripts, or bind to fixed machine.

Look at what happened after `foo.py`{.backtick} is obfuscated by Pyarmor. Here are the files list in the output path `dist`{.backtick}

        foo.py

        pytransform.py
        _pytransform.so, or _pytransform.dll in Windows, _pytransform.dylib in MacOS

        pyshield.key
        pyshield.lic
        product.key
        license.lic

`dist/foo.py`{.backtick} is obfuscated script, the content is

:::: 
::: 
``` 
   1     from pytransfrom import pyarmor_runtime
   2     pyarmor_runtime()
   3 
   4     __pyarmor__(__name__, __file__, b'\x06\x0f...')
```
:::
::::

All the other extra files called `Runtime Files`{.backtick}, which are required to run or import obfuscated scripts. So long as runtime files are in any Python path, obfuscated script `dist/foo.py`{.backtick} can be used as normal Python script. That is to say, `the original python scripts can be replaced with obfuscated scripts seamlessly.`{.backtick}

## Obfuscate Scripts 

How to obfuscate python scripts by Pyarmor?

First compile Python script to code object

        char *filename = "foo.py";
        char *source = read_file( filename );
        PyCodeObject *co = Py_CompileString( source, "<frozen foo>", Py_file_input );

Next change this code object as the following ways

- Wrap byte code `co_code`{.backtick} within a `try...finally`{.backtick} block

          wrap header:

                  LOAD_GLOBALS    N (__armor_enter__)     N = length of co_consts
                  CALL_FUNCTION   0
                  POP_TOP
                  SETUP_FINALLY   X (jump to wrap footer) X = size of original byte code

          changed original byte code:

                  Increase oparg of each absolute jump instruction by the size of wrap header

                  Obfuscate original byte code

                  ...

          wrap footer:

                  LOAD_GLOBALS    N + 1 (__armor_exit__)
                  CALL_FUNCTION   0
                  POP_TOP
                  END_FINALLY

- Append function names `__armor_enter`{.backtick}, `__armor_exit__`{.backtick} to `co_consts`{.backtick}

- Increase `co_stacksize`{.backtick} to 4 if it\'s less than 4

- Set CO_OBFUSCAED (0x80000000) flag in `co_flags`{.backtick}

- Change all code objects in the `co_consts`{.backtick} recursively

Then serialize this reformed code object, obfuscate it to protect constants and literal strings

        char *string_code = marshal.dumps( co );
        char *obfuscated_code = obfuscate_algorithm( string_code );

Finally generate obfuscated script

        sprintf( buf, "__pyarmor__(__name__, __file__, b'%s')", obfuscated_code );
        save_file( "dist/foo.py", buf );

The obfuscated script is a normal Python script, it looks like this

:::: 
::: 
``` 
   1     __pyarmor__(__name__, __file__, b'\x01\x0a...')
```
:::
::::

## Run Obfuscated Scripts 

What happens to run obfuscated script `dist/foo.py`{.backtick} by Python Interpreter?

The first 2 lines, which called `Bootstrap Code`{.backtick}

:::: 
::: 
``` 
   1     from pytransfrom import pyarmor_runtime
   2     pyarmor_runtime()
```
:::
::::

It will fulfil the following tasks

- Validate `dist/license.lic`{.backtick}, check whether it\'s expired or not etc.

- Add 3 functions to module `builtins`{.backtick}:

  - `__pyarmor__`{.backtick}

  - `__armor_enter__`{.backtick}

  - `__armor_exit__`{.backtick}

The next code line in `dist/foo.py`{.backtick} is

:::: 
::: 
``` 
   1     ...
   2 
   3     __pyarmor__(__name__, __file__, b'\x01\x0a...')
```
:::
::::

`__pyarmor__`{.backtick} is called, it will import original module from obfuscated code

        static PyObject *
        __pyarmor__(char *name, char *pathname, unsigned char *obfuscated_code)
        {
            char *string_code = restore_obfuscated_code( obfuscated_code );
            PyCodeObject *co = marshal.loads( string_code );
            return PyImport_ExecCodeModuleEx( name, co, pathname );
        }

After that, in the runtime of this python process

- `__armor_enter__`{.backtick} is called as soon as any code object is executed, it will restore byte-code of this code object

          static PyObject *
          __armor_enter__(PyObject *self, PyObject *args)
          {
              // Got code object
              PyFrameObject *frame = PyEval_GetFrame();
              PyCodeObject *f_code = frame->f_code;

              // Increase refcalls of this code object
              // Borrow co_names->ob_refcnt as call counter
              // Generally it will not increased  by Python Interpreter
              PyObject *refcalls = f_code->co_names;
              refcalls->ob_refcnt ++;

              // Restore byte code if it's obfuscated
              if (IS_OBFUSCATED(f_code->co_flags)) {
                  restore_byte_code(f_code->co_code);
                  clear_obfuscated_flag(f_code);
              }

              Py_RETURN_NONE;
          }

- `__armor_exit__`{.backtick} is called so long as code object completed execution, it will obfuscate byte-code again

          static PyObject *
          __armor_exit__(PyObject *self, PyObject *args)
          {
              // Got code object
              PyFrameObject *frame = PyEval_GetFrame();
              PyCodeObject *f_code = frame->f_code;

              // Decrease refcalls of this code object
              PyObject *refcalls = f_code->co_names;
              refcalls->ob_refcnt --;

              // Obfuscate byte code only if this code object isn't used by any function
              // In multi-threads or recursive call, one code object may be referenced
              // by many functions at the same time
              if (refcalls->ob_refcnt == 1) {
                  obfuscate_byte_code(f_code->co_code);
                  set_obfuscated_flag(f_code);
              }

              // Clear f_locals in this frame
              clear_frame_locals(frame);

              Py_RETURN_NONE;
          }

## Usage 

Install

        pip install pyarmor

Obfuscate Scripts

        cd /path/to/pyarmor
        python pyarmor.py obfuscate --src=examples/simple --entry=queens.py

Run Obfuscated Scripts

        cd dist
        python queens.py

Bind obfuscated scripts to fixed machine and expire it on some day. By default the obfuscated scripts can run in any machine and never expired, this behavior can be changed by replacing runtime file `dist/license.lic`{.backtick}

        cd /path/to/pyarmor
        python pyarmor.py licenses --expired "2018-12-31" --bind-mac "70:f1:a1:23:f0:94" Jondy
        cp licenses/Jondy/license.lic dist/

        cd dist
        python queens.py

## Support Platforms 

- Python 2.5, 2.6, 2.7 and Python3
- win32, win_amd64, linux_i386, linux_x86_64, macosx_intel
- Embedded Platform: Raspberry Pi, Banana Pi, TS-4600 / TS-7600

Besides, pyarmor works well with [py2exe](./py2exe.html) and [PyInstaller](PyInstaller). Here are some [examples](https://github.com/dashingsoft/pyarmor/blob/master/src/examples/README.md).

## Other Links 

- [Homepage](http://pyarmor.dashingsoft.com)

- [Source Code](https://github.com/dashingsoft/pyarmor)

- [pypi](https://pypi.org/project/pyarmor/)

- [User Guide](https://github.com/dashingsoft/pyarmor/blob/master/src/user-guide.md)

------------------------------------------------------------------------

[CategoryDistutilsCookbook](CategoryDistutilsCookbook)
