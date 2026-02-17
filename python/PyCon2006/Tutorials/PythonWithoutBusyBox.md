# PyCon2006/Tutorials/PythonWithoutBusyBox

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

*This talk has been cancelled. Anyone with questions about this topic is welcome to contact \[Mailto:alex[.perry@ieee.org](mailto:.perry@ieee.org)\].*

# Python without a Busybox - Building small embedded devices quickly 

*This talk has been cancelled. Anyone with questions about this topic is welcome to contact \[Mailto:alex[.perry@ieee.org](mailto:.perry@ieee.org)\].*

The software of a future product can be quickly implemented using portable Python, whether on Linux, Mac, Windows, or another platform. Once tested to ensure that it meets all requirements, one can just merge those directories of Python code with a board support package, directly generating the download image for the device\'s Flash.

Small embedded devices, using Linux or a similar kernel, have often used Busybox to provide a basic posix like command line environment. Since this is similar, but not identical to a workstation\'s tools, there is effort involved in adapting scripts and configurations. Similarly, once the primary application purpose is loaded and running, that SysV boot environment unnecessarily costs several megabytes of RAM (since INIT remains) as well as additional megabytes of Flash.

This talk explains how to omit all non-Python software components and demonstrates the procedure with a simple Twisted Python program.

*Audience: Beginning programmers with an embedded need or background*
