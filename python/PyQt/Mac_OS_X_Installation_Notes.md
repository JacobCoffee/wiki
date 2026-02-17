# PyQt/Mac_OS_X_Installation_Notes

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# Mac OS X Installation Notes 

This page contains a list of problems that people have encountered with Python and [PyQt](PyQt) on Mac OS X.

## Fatal Python error: Interpreter not initialized (version mismatch?) 

[Kevin Cureton writes](http://mats.imk.fraunhofer.de/pipermail/pykde/2006-July/013722.html):

    Once I rebuilt Python as a framework, along with rebuilding the various extensions, SIP, and PyQt, things worked fine.

    Here are the commands to build Python as a framework from the source.

         configure --enable-framework
         make
         sudo make frameworkinstall
