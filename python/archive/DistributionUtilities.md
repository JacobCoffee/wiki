# DistributionUtilities

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# Distribution Utilities 

General distribution of Python code is typically done using the [Distutils](../packaging/Distutils) package from the standard library which can produce source and binary distributions which depend on end-users having Python already installed on their computer (with Python Eggs being a form of software distribution provided by the [Distutils](../packaging/Distutils) derivative, [setuptools](../archive/setuptools)). Such source and binary software distributions are frequently available as operating system packages (a more general form of the term \"package\" referring not just to code but also to documentation, resources and other things) and can be installed using the package management infrastructure employed by various operating systems - see \"System Package Distribution\" below.

## Executable Applications 

The following projects support the production of executable application from Python scripts.

::: {}
  ----------------------------------------------------------------------------------------------------------------------------------------- ------------------------------------------------------------------------ -------------------------- -------------------------- -------------------------------------------------------------------------------------------------------------
  **Package**                                                                                                                               **Target**                                                               Latest update date         Latest version             **Notes**
  [bbfreeze](http://pypi.python.org/pypi/bbfreeze/)                                                                                  Python 2                                                                 2014-01-20                 1.1.3                      Create standalone executables from python scripts
  [esky](http://pypi.python.org/pypi/esky/)                                                                                          Python 2 & 3                                                             2013-03-27                 0.9.8                      An auto-update framework built on top of bbfreeze
  [cx Freeze](http://www.python.net/crew/atuining/cx_Freeze/)                                                                        Python 2                                                                 2006-07-21                 3.0.3                      a set of utilities for freezing Python scripts
  [ExeMaker](http://effbot.org/zone/exemaker.htm)                                                                                    Python 2                                                                 2004-10-12                 1.2                        Creates EXE loaders for Python scripts (for Windows)
  [Freeze](../archive/Freeze)                                                                                                                   Python 2 & ( [3 when fixed](http://bugs.python.org/issue16047))   Varies by python version   Varies by python version   Bundled with Python in the \"Tools\" Directory as **freeze.py** allows building executables (Unix-only?)
  [py2exe](http://www.py2exe.org/)                                                                                                   Python 2                                                                 2008-11-16                 0.6.9                      Transform Python scripts into standalone Windows executable. See [py2exe](../platforms/Py2Exe)
  [py2app](http://undefined.org/python/#py2app)                                                                                      Python 2 & 3                                                             2014-02-06                 0.8                        Converts Python scripts into executable Mac OS X applications
  [McMillan\'s Installer](https://web.archive.org/web/20130804055507/http://davidf.sjsoft.com/mirrors/mcmillan-inc/install1.html)   Python 2                                                                 2003-06-04                 5b5_4                      Includes notes about (other) distributing solutions
  [PyInstaller](http://www.pyinstaller.org/)                                                                                         Python 2                                                                 2013-09-18                 2.1                        Derived from McMillan\'s installer
  [Signet](http://jamercee.github.io/signet/)                                                                                        Python 2                                                                 2014-07-28                 1.0.10                     Signet is a distutils extension for creating tamper resistant python, while still distributing python code.
  [pyarmor](https://pypi.python.org/pypi/pyarmor/)                                                                                  Python 2 & 3                                                             2018-10-29                 4.1.4                      Obfuscate python scripts, bind obfuscated scripts to fixed machine or expire obfuscated scripts
  ----------------------------------------------------------------------------------------------------------------------------------------- ------------------------------------------------------------------------ -------------------------- -------------------------- -------------------------------------------------------------------------------------------------------------
:::

## Installers 

Installers are sometimes needed to wrap up the output of freeze tools into packages:

- [Inno Setup](http://www.jrsoftware.org/isinfo.php) (Windows)

- [NSIS](http://nsis.sourceforge.net/Main_Page) (Windows)

- [MacPython](../platforms/MacPython) [BundleBuilder](BundleBuilder) (Mac OS X)

## See also 

- [buildout](../packaging/buildout)

- [deployment](../archive/deployment) (an answer to the frequently asked question on the topic)

## System Package Distribution 

Although [Distutils](../packaging/Distutils) supports the production of some system packages, other tools exist to make such packages:

- There are videos explaining how to create a Debian package (.deb) from a python program (.py). This is useful if you want to distribute to Debian based Linux Systems like [Debian](http://www.debian.org) or [Ubuntu](http://www.ubuntu.com/).

## Distribution Using Virtualisation 

It is possible to distribute entire systems which can then be run under virtualisation or as \"live CD\" environments. Some solutions attempt to incorporate such approaches in a way which is transparent to the user:

- [LINA](http://en.wikipedia.org/wiki/LINA_%28software%29) - running Linux-based applications on other systems (Inactive 2009)

------------------------------------------------------------------------

[CategoryDistutilsCookbook](CategoryDistutilsCookbook)
