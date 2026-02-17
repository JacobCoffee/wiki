# PdbRcIdea

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

**Note: this recipe uses `execfile`{.backtick}, which was removed in Python 3. Page needs an update!!!**

------------------------------------------------------------------------

# Problem 

You\'d like to include Python scripts into my .pdbrc, but only pdb commands are allowed there.

# Solution 

Use execfile() to run a file containing your Python code.

**.pdbrc** may look like this:

    # .pdbrc only allows for debugger commands; you cannot insert Python
    # scripts.

    # To overcome this restriction, this .pdbrc executes ~/.pdbrc.py,
    # which can contain arbitrary Python commands (including a call to a
    # local pdbrc.py (no leading dot!) in your working directory if it
    # exists).

    # If ~/.pdbrc.py is missing, you get an error message (which doesn't
    # hurt).

    execfile(os.path.expanduser("~/.pdbrc.py"))

and this is an example **\~/.pdbrc.py**:

    print ".pdbrc.py started"

    # Command line history:
    import readline
    histfile = ".pdb-pyhist"
    try:
        readline.read_history_file(histfile)
    except IOError:
        pass
    import atexit
    atexit.register(readline.write_history_file, histfile)
    del histfile
    readline.set_history_length(200)

    # return to debugger after fatal exception (Python cookbook 14.5):
    def info(type, value, tb):
        if hasattr(sys, 'ps1') or not sys.stderr.isatty():
            sys.__excepthook__(type, value, tb)
        import traceback, pdb
        traceback.print_exception(type, value, tb)
        print
        pdb.pm()

    sys.excepthook = info

    # From (on my machine) /usr/local/lib/python2.3/less user.py:
    import os
    home = os.curdir                        # Default
    if 'HOME' in os.environ:
        home = os.environ['HOME']
    elif os.name == 'posix':
        home = os.path.expanduser("~/")
    elif os.name == 'nt':                   # Contributed by Jeff Bauer
        if 'HOMEPATH' in os.environ:
            if 'HOMEDRIVE' in os.environ:
                home = os.environ['HOMEDRIVE'] + os.environ['HOMEPATH']
            else:
                home = os.environ['HOMEPATH']
    # Make sure home always ends with a directory separator:
    home = os.path.realpath(home) + os.sep

    # Try to execute local file (if any) unless we are in the home dir.
    if home != os.path.realpath(os.curdir) + os.sep:
        # Avoid recursively loading this file.
        try:
            _already_loaded += 1
        except NameError:
            _already_loaded = 1
        if _already_loaded < 3:
            try:
                execfile("pdbrc.py")
            except IOError:
                pass

    # Cleanup any variables that could otherwise clutter up the namespace.
    try:
        del atexit
        del home
        del info
        del os
        del pdb
        del readline
        del rlcompleter
        # careful here:
        del _already_loaded
    except NameError:
        # Probably this is a second pdbrc that has been loaded.
        pass

    print ".pdbrc.py finished"

------------------------------------------------------------------------

[PythonDebuggers](PythonDebuggers)
