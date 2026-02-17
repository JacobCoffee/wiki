# CommandlineTools

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

## Creating Command Line Tools With Python 

### Standard library support for parsing command lines 

- [optparse](https://docs.python.org/library/optparse.html) and [argparse](https://docs.python.org/library/argparse.html) (optparse is marked as deprecated since the introduction of argparse with Python 2.7 and Python 3.2, use argparse unless you have to support older Python versions)

- [getopt](https://docs.python.org/2/library/getopt.html) C-style command line parser

The [Argparse Tutorial](https://docs.python.org/howto/argparse.html) is an excellent read for getting you started with creating command line tools. See also [OptionParsing](OptionParsing).

------------------------------------------------------------------------

### Other articles on Python command line tools 

**For sysadmins familiar with Bash scripting**: Beginner Level, circa 02/2008

- [Python for Bash scripters: A well-kept secret](http://magazine.redhat.com/2008/02/07/python-for-bash-scripters-a-well-kept-secret/)

**Using Python To Create Unix Commandline Tools:** Beginning/Intermediate Level

- Summary: An introductory article on how to create command line tools with Python. A beginner should learn how to create command line tool after finishing.

- [Introduction To Creating CLI Tools with Python](http://www.ibm.com/developerworks/aix/library/au-pythocli/?ca=dgr-lnxw82pythonunixtool&S_TACT=105AGX59&S_CMP=GR)

**Command line tool with optparse, subprocess, and logging**: Beginning/Intermediate level

- Summary: This script provides shortcuts for using a Git repository but the script could be used as a template for other shell tools.

- [A Clean Python Shell Script](http://www.jperla.com/blog/2008/11/17/a-clean-python-shell-script/).

**[PyCon2008](PyCon2008) Presentation on Command Line Tools:** Intermediate Level

- Summary: Presentation goes into detail on using threads, subprocess, optparse, configparser, and ORM\'s to create sophisticated tools.

- [Slides: Creating Command Line Tools with Python](http://code.noahgift.com/pycon2008/pycon2008_cli_noahgift.pdf)

- [Source: Code](http://code.noahgift.com/pycon2008/pycon2008_cli_noahgift.zip)
