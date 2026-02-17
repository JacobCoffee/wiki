# PyQt/Deploying_PyQt_Applications

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# Deploying PyQt Applications 

This page contains information about some of the tools that could be used to deploy [PyQt](PyQt) applications on various platforms, typically in binary form.

The idea is that each solution should be listed along with a brief description and a link to its home page. The description should probably come from the solution\'s home page or documentation, so that it is described \"in its own words\". Further comments and links for each can be given after these fields.

## Cross-Platform Solutions 

The following tools are cross-platform, working on Windows and some flavours of Unix.

### fman build system 

[https://build-system.fman.io](https://build-system.fman.io)

Creates stand-alone executables and installers for [PyQt](PyQt) applications. Supports Windows, macOS and Linux.

### PyInstaller 

[http://pyinstaller.python-hosting.com/](http://pyinstaller.python-hosting.com/)

- *\"[PyInstaller](PyInstaller) is a program that converts (packages) Python programs into stand-alone executables, under Windows, Linux and Irix.\"*

A short How-To for using PyInstaller with PyQt on Mac OS-X:

- [PyInstaller On Mac OS X](PyInstallerOnMacOSX)

### cx_Freeze 

[http://starship.python.net/crew/atuining/cx_Freeze/index.html](http://starship.python.net/crew/atuining/cx_Freeze/index.html)

- *\"cx_Freeze is a set of utilities for freezing Python scripts into executables using many of the techniques found in Thomas Heller\'s py2exe, Gordon [McMillan](./McMillan.html)\'s Installer and the Freeze utility that ships with Python itself.\"*

## bbfreeze

(Windows, Unix, but not Mac OS X)

[http://cheeseshop.python.org/pypi/bbfreeze/](http://cheeseshop.python.org/pypi/bbfreeze/)

- *\"bbfreeze creates stand-alone executables from python scripts. It\'s*

similar in purpose to the well known py2exe\_ for windows, py2app\_ for OS X, [PyInstaller](PyInstaller)\_ and cx_Freeze\_ (in fact ancient versions were based on cx_Freeze. And it uses the modulegraph\_ package, which is also used by py2app).\"

Mercurial repository: [http://systemexit.de/repo/bbfreeze](http://systemexit.de/repo/bbfreeze)

### Freeze 

The original freeze tool that embeds Python bytecode into executables is supplied with Python - look in the examples/Tools directory.

### qmake

For applications that don\'t depend too much on many shared library modules other than the ones shipped with [PyQt](PyQt), it may be possible to take advantage of qmake\'s features and a simple launcher application to create binaries for different platforms.

## Tools for Windows 

The following tools are designed to produce executables for Windows.

### py2exe

[http://www.py2exe.org/](http://www.py2exe.org/)

- *\"py2exe is a Python Distutils extension which converts Python scripts into executable Windows programs, able to run without requiring a Python installation.\"*

**Comments:** I highly recommend py2exe which can produce nice executables. Combined with [InnoSetup](./InnoSetup.html), you get a full standard windows application and the user has no idea that the stuff was actually developed on Linux with Open Source technologies. \-- Philippe Fremy

See the following links for more information about deploying PyQt applications with py2exe:

- [http://www.py2exe.org/index.cgi/Py2exeAndPyQt](http://www.py2exe.org/index.cgi/Py2exeAndPyQt)

- [http://mail.python.org/pipermail/python-list/2007-September/458364.html](http://mail.python.org/pipermail/python-list/2007-September/458364.html)

### ExeMaker 

[http://effbot.org/zone/exemaker.htm](http://effbot.org/zone/exemaker.htm)

- *\"[ExeMaker](./ExeMaker.html) is a small tool that takes a Python script, copies it to a program directory, and creates a Windows EXE file in the same directory.\"*

## Tools for Mac OS X 

The following tools are designed to produce executables for Mac OS X.

### py2app

[http://undefined.org/python/#py2app](http://undefined.org/python/#py2app)

- *\"A distutils extension which converts python scripts into executable Mac OS X applications, able to run without requiring an existing Python installation.\"*

## Other Resources 

[How can I create a stand-alone binary from a Python script?](http://effbot.org/pyfaq/how-can-i-create-a-stand-alone-binary-from-a-python-script.htm) from the [pyfaq](http://effbot.org/pyfaq/)
