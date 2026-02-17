# PythonCdCore

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

The [PythonCd](PythonCd) includes the Python distribution in several forms:

# Installable Python packages 

In the top level directory of the CD is a directory `python/`{.backtick}, containing several packages of Python:

- Python for Linux - most Linux distributions include Python, so we don\'t provide it for them
- Python for Mac OS X
- Python for Windows, win32all extension
- Python for DOS - no maintainer yet, so we only provide an URL
- Python source code, if you want to compile it yourself

# Ready-to-Use Python 

On the bootable Linux system, Python is already installed and ready to run:

- Python 2.3.4 (latest and greatest, use this!)
- Python 2.2.3
- Python 2.1.3

The older versions are provided for satisfying dependencies of other stuff and to be able to try compatibility of your source code.
