# MacPython/UniversalPython

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

Differences between [MacPython](MacPython) 2.4.1 and Universal Python 2.4.2:

- `/ApplicationsMacPython-2.4` is now `/Applications/Python 2.4`

- PythonIDE, [/PackageManager](./MacPython(2f)UniversalPython(2f)PackageManager.html) are gone. These applications have been deprecated for quite a long time, and depend on [WASTE](http://www.merzwaren.com/waste/), which is somewhat non-free and is not available for x86.

- select.poll and related constants exist on systems that have a correct poll implementation (definitely 10.4.4).

- pythonw is now an executable that does an execv (instead of a script), so it may be used in #!scripts

- All extensions and the framework are built universal for ppc and i386

- The MACOSX_DEPLOYMENT_TARGET defaults to 10.3, and extensions are built such that they will probably be compatible with 10.3.9+

- Versions of Mac OS X prior to 10.3.9 are not supported with this build

Unfinished differences between [MacPython](MacPython) 2.4.1 and Universal Python 2.4.2:

- The Python HTML documentation is now in Python.framework/Versions/2.4/Doc/html, which IDLE knows about.

- The python in the bin directory is now also pythonw, so pythonw is only necessary for legacy purposes.

- The installer places the framework\'s bin directory on the PATH for normal shells

Patches in Universal Python 2.4.2 vs Python 2.4.2 source trees:

- select.poll brokenness detection is moved from configure time to runtime

- CONFIGURE_MACOSX_DEPLOYMENT_TARGET is now MACOSX_DEPLOYMENT_TARGET

- distribution scripts have been rewritten in python rather than a hodgepodge of makefiles

- [/PythonLauncher](./MacPython(2f)UniversalPython(2f)PythonLauncher.html) is built without xcode/pbxbuild
