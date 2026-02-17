# CPythonInterpreterInitialization

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

The initialisation process for the CPython interpreter is complicated and while some parts of it are well documented, there\'s no cohesive overview of the whole process, and the quality of the documentation of the individual steps is quite uneven. This can lead to difficulties for developers of other applications that want to embed CPython, application authors that want to more strictly control the execution environment of their Python software (or just debug their software when it misbehaves) and CPython core developers considering proposals that further change the initialisation sequence.

This page is primarily aimed at collecting links to the existing documentation resources, proposals that affect the startup sequence, and some possible ideas for cleaning up and rationalising the startup process.

## Phases of Initialisation 

(These phases are neither comprehensive nor in sequence - yet)

- memory allocator initialisation
- builtin type initialisation
- builtins module creation
- sys module creation
- main module creation
- import system initialisation
- locating the standard library
- site.py execution (including system and user site packages)
- virtual environment processing
- warnings module import and configuration
- environment variable processing
- command line processing
- creation of standard streams
- figure out locale and filesystem encoding
- main execution

The following sketch highlights some of the C level functions and global variables involved in the initialisation sequence (based on an initial version contributed by a poster to the core mentorship list):

          +main()
            +-Copies argv from char array to wchar_t array (with LC_ALL locale set as the empty string)
            |  +-_Py_char2wchar()
            +-Py_Main()
            |  +-Use _PyOS_GetOpt to scan argc/argv to set Py_IgnoreEnvironmentFlag
            |  +-Force Py_HashRandomizationFlag to 1 by default
            |  +-_PyRandom_Init()
            |  |  +-Check (and set) Py_HashSecretInitialized
            |  |  +-Check for PYTHONHASHSEED (via Py_GETENV, which checks Py_IgnoreEnvironmentFlag)
            |  |  +-Create a process global hash seed (shared by all interpreters in the process)
            |  +-PySys_ResetWarnOptions()
            |  |  +-This usually does nothing since the "warnoptions" static will almost always be NULL...
            |  |  +-It does call PyList_Check() though (even though the interpreter may not be initialised)
            |  |  +-In any embedded case where this does something, we may get spurious lingering X options
            |  +-Use _PyOS_GetOpt to scan argc/argv to set
            |  |  +-command (controls CLI behaviour)
            |  |  +-module (controls CLI behaviour)
            |  |  +-Py_BytesWarningFlag
            |  |  +-Py_DebugFlag
            |  |  +-Py_InspectFlag
            |  |  +-Py_InteractiveFlag
            |  |  +-Py_OptimizeFlag
            |  |  +-Py_DontWriteBytecodeFlag
            |  |  +-Py_NoUserSiteDirectory
            |  |  +-Py_NoSiteFlag
            |  |  +-Py_UnbufferedStdioFlag (and saw_unbuffered_flag)
            |  |  +-Py_VerboseFlag
            |  |  +-skipfirstline (applies only to direct execution)
            |  |  +-help (controls CLI behaviour)
            |  |  +-version (controls CLI behaviour)
            |  |  +-PySys_AddWarnOption() (Remember, we haven't initialised the interpreter yet!)
            |  |  |  +-PySys_AddWarnOptionUnicode()
            |  |  |    +-PyUnicode_FromWideChar()
            |  |  |    +-PyList_Check(), PyList_New(), PyList_Append()
            |  |  +-PySys_AddXOption() (Again, interpreter not initialised!)
            |  |  |  +-get_xoptions()
            |  |  |  | +-PyDict_Check(), PyDict_New()
            |  |  |  +-Py_INCREF(Py_True)
            |  |  |  +-PyUnicode_FromWideChar()
            |  |  |  +-PyDict_SetItem()
            |  |  +-Py_QuietFlag
            |  +-If "help" requested, display it and bail out here
            |  +-If "version" requested, display it and bail out here
            |  +-Process the following environment variables (via Py_GETENV, which checks Py_IgnoreEnvironmentFlag)
            |  |  +-PYTHONINSPECT -> Py_InspectFlag
            |  |  +-PYTHONUNBUFFERED -> Py_UnbufferedStdioFlag
            |  |  +-PYTHONNOUSERSITE -> Py_NoUserSiteDirectory
            |  |  +-PYTHONWARNINGS -> PySys_AddWarnOption (if !Py_IgnoreEnvironmentFlag)
            |  +-If neither "command" nor "module" set, set "filename"
            |  +-PyFd_IsInteractive() (check if stdin is a tty)
            |  +-Tweak buffering of std streams based on unbuffered and interactive flags
            |  +-call Py_SetProgramName appropriately for platform
            |  | +-May look at PYTHONEXECUTABLE (via Py_GETENV) and __PYVENV_LAUNCHER__ (unconditional getenv) on OS X
            |  +-Py_Initialize[Ex]()
            |  |  +-_Py_InitializeEx_Private()
            |  |  |  +-Check (and set) "initialized" flag
            |  |  |  +-_Py_Finalizing flag set to NULL
            |  |  |  +-setlocale(LC_CTYPE, "")
            |  |  |  +-Process the following environment variables (via Py_GETENV, which checks Py_IgnoreEnvironmentFlag)
            |  |  |  |  +-PYTHONDEBUG -> Py_DebugFlag
            |  |  |  |  +-PYTHONVERBOSE -> Py_VerboseFlag
            |  |  |  |  +-PYTHONOPTIMIZE -> Py_OptimizeFlag
            |  |  |  |  +-PYTHONDONTWRITEBYTECODE -> Py_DontWriteBytecodeFlag
            |  |  |  |  +-PYTHONHASHSEED -> Py_HashRandomizationFlag
            |  |  |  +-_PyRandom_Init()
            |  |  |  +-PyInterpreterState_New()
            |  |  |  |    +-HEAD_INIT()
            |  |  |  |    +-HEAD_LOCK()
            |  |  |  |    +-HEAD_UNLOCK()
            |  |  |  +-PyThreadState_New()
            |  |  |  +-PyThreadState_Swap()
            |  |  |  +-_PyEval_FiniThreads() (clean up after previous Init/Fini pair)
            |  |  |  +-PyGILState_Init() (auto thread-state API)
            |  |  |  +-_Py_ReadyTypes()
            |  |  |  +-_PyFrame_Init()
            |  |  |  +-_PyLong_Init()
            |  |  |  +-_PyByteArray_Init()
            |  |  |  +-_PyFloat_Init()
            |  |  |  +-Create interpreter module cache with PyDict_New()
            |  |  |  +-_PyUnicode_Init() (Even though -W and -X may have already created Unicode objects...)
            |  |  |  +-_PyBuiltin_Init() (and record ref in interpreter state)
            |  |  |  +-_PyImport_FixupBuiltin() (prerecord builtin module in import state???)
            |  |  |  +-_PyExc_Init() (initialize exceptions)
            |  |  |  +-_PySys_Init() (and record ref in interpreter state)
            |  |  |  +-_PyImport_FixupBuiltin() (prerecord sys module in import state???)
            |  |  |  +-PySys_SetPath(Py_GetPath())
            |  |  |  +-Expose module cache as sys.modules
            |  |  |  +-Add interim stderr via PyFile_NewStdPrinter
            |  |  |  +-_PyImport_Init()
            |  |  |  +-_PyImportHooks_Init()
            |  |  |  +-_PyWarnings_Init()
            |  |  |  +-install_importlib()
            |  |  |  +-import_init()
            |  |  |  +-_PyFaulthandler_Init()
            |  |  |  +-_PyTime_Init()
            |  |  |  +-initfsencoding()
            |  |  |  +-initsigs()
            |  |  |  +-initmain()
            |  |  |  +-initstdio()
            |  |  |  +-if -W was used, import "warnings"
            |  |  |  +-if Py_NoSiteFlag not set, initsite()
            |  +-Print banner if running in interactive mode
            |  +-PySys_SetArgv() (sys.argv[0] may still be inaccurate)
            |  +-Attempt to import readline if in interactive mode
            |  +-if "command" is set: invoke sts = run_command()
            |  |  +-More detail needed
            |  +-if "module" is set: invoke sts = run_module()
            |  |  +-More detail needed
            |  +-otherwise running from file or stdin
            |  |  +-if running from interactive stdin: RunStartupFile
            |  |  +-if running from named file: try sts = RunMainFromImporter()
            |  |  |  +-More detail needed
            |  |  +-if that didn't work, open the file as an ordinary file
            |  |  +-if running from stdin or an ordinary file: sts = run_file()
            |  |     +-PyRun_AnyFileExFlags()
            |  |        +-PyRun_SimpleFileExFlags()
            |  |           +- PyRun_FileExFlags()
            |  +-Check late for PYTHONINSPECT (via Py_GETENV, which checks Py_IgnoreEnvironmentFlag) to allow os.environ["PYTHONINSPECT"] = 1
            |  +-If stdin is interactive and we were running from command/module/filename
            |  |  +-sts=(PyRun_AnyFileFlags() != 0);
            |  +-Py_Finalize()
            |  |  +-More detail needed
            |  +-"sts" is the return code for the interpreter invocation
            +

## Existing Related Documentation 

As the heading says, this section is for links to any documentation that currently exists

- [Import system specification](http://docs.python.org/3/reference/import.html)

- [C API initialization/finalization documentation](http://docs.python.org/3/c-api/init.html)

- [Command line usage guide](http://docs.python.org/3/using/cmdline.html)

- python -h

- [site module documentation](http://docs.python.org/3/library/site)

- [venv module documentation](http://docs.python.org/3/library/venv)

- [Virtual environments proposal (PEP 405)](http://www.python.org/dev/peps/pep-0405/)

## Relevant code areas 

This section is for direct links into relevant parts of the CPython source (where there\'s no good existing docs)

- [pythonrun.c, home of Py_Initialize and friends](http://hg.python.org/cpython/file/default/Python/pythonrun.c)

- [Direct link to \_PyInitializeEx_Private](http://hg.python.org/cpython/file/default/Python/pythonrun.c#l243)

- [main.c, home of the CLI definition in Py_Main](http://hg.python.org/cpython/file/default/Modules/main.c)

- [python.c, source for the actual binary that calls Py_Main from the Python library](http://hg.python.org/cpython/file/default/Modules/python.c)

- [sysmodule.c, where \_Py_SysInit does a lot of work](http://hg.python.org/cpython/file/default/Python/sysmodule.c#l1549)

- [Hash seed randomisation](http://hg.python.org/cpython/file/default/Python/random.c)

- [Global flag declarations (most of them, anyway)](http://hg.python.org/cpython/file/default/Python/pythonrun.c#l82)

- [Figuring out various filesystem related details](http://hg.python.org/cpython/file/default/Modules/getpath.c)

I know it makes no sense that main.c and python.c are in the Modules directory and sysmodule.c is in the Python directory, but that\'s a 20+ year old code base for you\...

## Proposed Additions/Enhancements 

This section is primarily for links to CPython tracker issues that propose changes for 3.4+ that mean adding even \*more\* flexibility to the initialisation process.

- [Override first sys.path entry](http://bugs.python.org/issue13475)

- [Run code prior to \_\_main\_\_ execution](http://bugs.python.org/issue14803)

- [Add to sys.path via command line](http://bugs.python.org/issue15716)

- [Run in an isolated mode](http://bugs.python.org/issue16499)

- [Detecting when sys.path\[0\] may be inside a package (part of PEP 395, rendered more challenging by PEP 420)](http://www.python.org/dev/peps/pep-0395/)

- [Setting IO encoding in embedded Python](http://bugs.python.org/issue16129)

- Generally making CPython more embedding friendly

## Preliminary Ideas 

This part is a scratchpad for half-baked ideas that may or may not end up being useful/viable

- Perhaps Py_Initialize could be split into multiple steps?:
  - Py\_[PreConfigure](./PreConfigure.html) (sets up the basic data types and the core eval loop, but no IO or OS interfaces except the memory allocator)

  - Py\_[GetStandardConfig](./GetStandardConfig.html) (pass in a dict requesting standard population of configuration settings - with a way to say not to bother working out some things when an embedding application plans to override them completely, e.g. by prepopulating them with \"None\")

  - Py_Configure (pass in a dict specifying the configuration settings to use, completes the initialisation process)

  - embedding applications could then just decide which settings they wanted to blacklist when calling Py\_[GetStandardConfig](./GetStandardConfig.html). They would also have the option to tweak the standard config before passing it to Py_Configure
- Concrete use case: \"System Python\"
  - create an \"spython\" alternate executable
  - doesn\'t set sys.path\[0\] based on the current directory or executable location
  - ignores environment variables
  - ignores user site directory
  - this \*should\* be easy, but is currently hard

------------------------------------------------------------------------

[CategoryInternals](CategoryInternals)
