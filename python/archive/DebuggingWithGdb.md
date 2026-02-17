# DebuggingWithGdb

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

There are types of bugs that are difficult to debug from within Python:

- segfaults (not uncaught Python exceptions)

- hung processes (in cases where you can\'t get a Python traceback or debug with `pdb`)

- out of control daemon processes

In these cases, you can try `gdb`.

## Prerequisites 

You need to have `gdb`{.backtick} on your system and Python debugging extensions. Extensions package includes debugging symbols and adds Python-specific commands into `gdb`{.backtick}. On a modern Linux system, you can easily install these with:

Fedora:

- `sudo yum install gdb python-debuginfo`

Ubuntu:

- `sudo apt-get install gdb python2.7-dbg`

Centos\*:

- `sudo yum install yum-utils`

- `sudo debuginfo-install glibc`

- `sudo yum install gdb python-debuginfo`

##### \* tested on Centos 7. python-debuginfo is installable after the first two commands. 

For `gdb`{.backtick} support on legacy systems, look at the end of this page.

## Running with \`gdb\` 

There are two possible ways:

1.  run python under `gdb`{.backtick} from the start. Note: the python executable needs to have debug symbols in it which may be another exe python2.7-dbg depending on your system

2.  attach to already running python process

To run python under `gdb` there are also two ways.

Interactive:

- $ gdb python
      ...
      (gdb) run <programname>.py <arguments>

Automatic:

- $ gdb -ex r --args python <programname>.py <arguments>

This will run the program til it exits, segfaults or you manually stop execution (using Ctrl+C).

If the process is already running, you can attach to it provided you know the process ID.

- $ gdb python <pid of running process>

Attaching to a running process like this will cause it to stop. You can tell it to continue running with `c`{.backtick} command.

## Debugging process 

If your program segfaulted, `gdb`{.backtick} will automatically pause the program, so you can switch into `gdb`{.backtick} console to inspect its state. You can also manually interrupt program execution by pressing Ctrl+C in the console.

See the page [EasierPythonDebugging](https://fedoraproject.org/wiki/Features/EasierPythonDebugging) for the list of Python helper commands for `gdb`{.backtick}.

### Getting a C Stack Trace 

If you are debugging a segfault, this is probably the first thing you want to do.

At the `(gdb)` prompt, just run the following command:

- (gdb) bt
      #0  0x0000002a95b3b705 in raise () from /lib/libc.so.6
      #1  0x0000002a95b3ce8e in abort () from /lib/libc.so.6
      #2  0x00000000004c164f in posix_abort (self=0x0, noargs=0x0)
          at ../Modules/posixmodule.c:7158
      #3  0x0000000000489fac in call_function (pp_stack=0x7fbffff110, oparg=0)
          at ../Python/ceval.c:3531
      #4  0x0000000000485fc2 in PyEval_EvalFrame (f=0x66ccd8)
          at ../Python/ceval.c:2163
      ...

With luck, this will give some idea of where the problem is occurring and if it doesn\'t help you fix the problem, it can help someone else track down the problem.

The quality of the results will depend greatly on the amount of debug information available.

### Getting a Python Stack Trace 

If you have Python extensions installed, you can enter:

- (gdb) py-bt

to get stack trace with familiar Python source code.

### Working With Hung Processes 

If a process appears hung, it will either be waiting on something (a lock, IO, etc), or be in a busy loop somewhere. In either case, attaching to the process and getting a back trace can help.

If the process is in a busy loop, you may want to continue execution for a bit (using the `cont` command), then break (Ctrl+C) again and bring up a stack trace.

If the hang occurs in some thread, the following commands may be handy:

- (gdb) info threads
        Id   Target Id         Frame
        37   Thread 0xa29feb40 (LWP 17914) "NotificationThr" 0xb7fdd424 in __kernel_vsyscall ()
        36   Thread 0xa03fcb40 (LWP 17913) "python2.7" 0xb7fdd424 in __kernel_vsyscall ()
        35   Thread 0xa0bfdb40 (LWP 17911) "QProcessManager" 0xb7fdd424 in __kernel_vsyscall ()
        34   Thread 0xa13feb40 (LWP 17910) "python2.7" 0xb7fdd424 in __kernel_vsyscall ()
        33   Thread 0xa1bffb40 (LWP 17909) "python2.7" 0xb7fdd424 in __kernel_vsyscall ()
        31   Thread 0xa31ffb40 (LWP 17907) "QFileInfoGather" 0xb7fdd424 in __kernel_vsyscall ()
        30   Thread 0xa3fdfb40 (LWP 17906) "QInotifyFileSys" 0xb7fdd424 in __kernel_vsyscall ()
        29   Thread 0xa481cb40 (LWP 17905) "QFileInfoGather" 0xb7fdd424 in __kernel_vsyscall ()
        7    Thread 0xa508db40 (LWP 17883) "QThread" 0xb7fdd424 in __kernel_vsyscall ()
        6    Thread 0xa5cebb40 (LWP 17882) "python2.7" 0xb7fdd424 in __kernel_vsyscall ()
        5    Thread 0xa660cb40 (LWP 17881) "python2.7" 0xb7fdd424 in __kernel_vsyscall ()
        3    Thread 0xabdffb40 (LWP 17876) "gdbus" 0xb7fdd424 in __kernel_vsyscall ()
        2    Thread 0xac7b7b40 (LWP 17875) "dconf worker" 0xb7fdd424 in __kernel_vsyscall ()
      * 1    Thread 0xb7d876c0 (LWP 17863) "python2.7" 0xb7fdd424 in __kernel_vsyscall ()

Current thread is marked with `*`{.backtick}. To see where it is in Python code, use `py-list`{.backtick}:

- (gdb) py-list
      2025        # Open external files with our Mac app
      2026        if sys.platform == "darwin" and 'Spyder.app' in __file__:
      2027            main.connect(app, SIGNAL('open_external_file(QString)'),
      2028                         lambda fname: main.open_external_file(fname))
      2029
      >2030        app.exec_()
      2031        return main
      2032
      2033
      2034    def __remove_temp_session():
      2035        if osp.isfile(TEMP_SESSION_PATH):

To see Python code positions for all threads, use:

- (gdb) thread apply all py-list
      ...
       200
       201        def accept(self):
      >202            sock, addr = self._sock.accept()
       203            return _socketobject(_sock=sock), addr
       204        accept.__doc__ = _realsocket.accept.__doc__
       205
       206        def dup(self):
       207            """dup() -> socket object

      Thread 35 (Thread 0xa0bfdb40 (LWP 17911)):
      Unable to locate python frame

      Thread 34 (Thread 0xa13feb40 (LWP 17910)):
       197            for method in _delegate_methods:
       198                setattr(self, method, dummy)
       199        close.__doc__ = _realsocket.close.__doc__
       200
       201        def accept(self):
      >202            sock, addr = self._sock.accept()
       203            return _socketobject(_sock=sock), addr
      ...

## References 

- [http://fedoraproject.org/wiki/Features/EasierPythonDebugging](http://fedoraproject.org/wiki/Features/EasierPythonDebugging)

- [https://github.com/spyder-ide/spyder/wiki/How-to-debug-Spyder-deadlock-freeze-hang](https://github.com/spyder-ide/spyder/wiki/How-to-debug-Spyder-deadlock-freeze-hang)

## GDB on Legacy systems 

It may happen that you need to use `gdb`{.backtick} on a legacy system without advanced Python support. In this case you may find the following information useful.

#### GDB Macros 

A set of GDB macros are distributed with Python that aid in debugging the Python process. You can install them by adding the contents of `Misc/gdbinit`{.backtick} in the Python sources to `~/.gdbinit`{.backtick} \-- or copy it [from Subversion](http://svn.python.org/view/python/branches/release27-maint/Misc/gdbinit?view=log). Be sure to use the correct version for your version of Python or some features will not work.

Note that the new GDB commands this file adds will only work correctly if debugging symbols are available.

Depending on how you\'ve compiled Python, some calls may have had their frame pointers (i.e. `$fp` in GDB) optimised away, which means GDB won\'t have access to local variables like `co` that can be inspected for Python callstack information. For example, if you compile using `-g -O3` using GCC 4.1, then this occurs. Similarly, with gcc 4.5.2 on Ubuntu (at least) the macros fail for the same reason. The usual symptom is that you\'ll see the **call_function** routine appearing to be between **[PyEval](./PyEval.html)\_[EvalFrameEx](./EvalFrameEx.html)** and **[PyEval](./PyEval.html)\_[EvalCodeEx](./EvalCodeEx.html)**, and the macro failing with **No symbol \"co\" in current context.**. There are two work-arounds for the issue:

- Recompiling python with **make \"CFLAGS=-g -fno-inline -fno-strict-aliasing\"** solves this problem.

- Patching the conditionals for Python frames in the pystack and pystackv routines to ignore frames with where `$fp` is 0, like so:

  -     <<<<         if $pc > PyEval_EvalFrameEx && $pc < PyEval_EvalCodeEx
            >>>>         if $pc > PyEval_EvalFrameEx && $pc < PyEval_EvalCodeEx && $fp != 0

Also note that the stop condition for the while-loops in the `pystack` and `pystackv` routines were originally designed for the case where you\'re running the Python interpreter directly, and not running the interpreter withing another program (by loading the shared library and manually bootstrapping the interpreter). So you may need to tweak the while-loops depending on the program you\'re intending to debug. See, for example, [this StackOverflow post](http://stackoverflow.com/questions/22856807/stop-condition-for-stack-tracing-in-legacy-gdb-script) for another (putative) stop condition.

#### Getting Python Stack Traces With GDB Macros 

At the gdb prompt, you can get a Python stack trace:

- (gdb) pystack

Alternatively, you can get a list of the Python locals along with each stack frame:

- (gdb) pystackv

#### More useful macros not in python\'s gdbinit file 

See [http://web.archive.org/web/20070915134837/http://www.mashebali.com/?Python_GDB_macros:The_Macros](http://web.archive.org/web/20070915134837/http://www.mashebali.com/?Python_GDB_macros:The_Macros) for some more handy python gdb macros.
