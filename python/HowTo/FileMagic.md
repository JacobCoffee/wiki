# HowTo/FileMagic

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# General Information 

**Today** == Saturday, October 25, 2008

With special thanks for many of **The Keys** to **frank** and [his blog](http://boodebr.org/main/python/build-windows-extensions). Also, an [IBM article on setuptools](http://www.ibm.com/developerworks/linux/library/l-cppeak3.html?ca=dgr-lnxw03PythonEggWithSetuptools) had the info that helped me (at least) \"install\" setuptools without easy_install. (Necessary **Today** for Py v2.6; see below.)

I *tried* with Python v2.6, but could not get it to work; I\'m still not familiar with the magic of eggs, distutils, setuptools, etc. If anyone has the fix(es), let me know and I\'ll retest, revise, and update this info! (FYI: The problem is it\'s acting as if it can\'t find magic1.dll; if v2.6 is uninstalled, v2.5\[.2\] is \[re-\]installed, all works A-OK.)

This is my NON-PRISTINE copy of SWIG-able python-magic, unless/until Mr. Hupp re-posts it to his site (see below): [LARZ-python-magic-v0.1-c112ac064b7f.zip](attachments/HowTo(2f)FileMagic/LARZ-python-magic-v0.1-c112ac064b7f.zip)

**NOTE:** Mr. Hupp is working on a newer version; thus, all of this may become depreciated\...

This is what I did. It works on (32-bit) Windows XP Pro, SP3, on an old Athlon system with \<=512MB.

As they say: Your Mileage May Vary\... ![:)](/wiki/europython/img/smile.png ":)")

-Larry Hale (pythonlarry ta gmail)

# Software Used/Needed 

## CygWin 

version 2.573.2.3

[http://www.cygwin.com/](http://www.cygwin.com/)

May setup with all default settings, except ***MUST ADD***

- **Devel** (group)

  - gcc (3.4.4-3)
  - gcc-core (3.4.4-3) (should auto-select)
  - gcc-g++ (3.4.4-3) (should auto-select)
  - gcc-mingw (20040810-1)
  - gcc-mingw-core (20050522-1) (should auto-select)
  - gcc-mingw-g++ (20080522-1) (should auto-select)
  - make (3.81-2)
  - SWIG (1.3.36-1)

## GnuWin32 - (Magic) \"File\" Utility 

version 4.26 (more recent than what was available via [CygWin](./CygWin.html) **Today**)

[http://gnuwin32.sourceforge.net/packages/file.htm](http://gnuwin32.sourceforge.net/packages/file.htm)

[http://downloads.sourceforge.net/gnuwin32/file-4.26-setup.exe](http://downloads.sourceforge.net/gnuwin32/file-4.26-setup.exe)

May setup with defaults, except (*I recommend*) change install directory from

- [GnuWin32](./GnuWin32.html)\\File

to simply

- File

**NOTE:** It\'s already set to install below \"Program Files\"

## Python 

version 2.5.2

[http://python.org/ftp/python/2.5.2/python-2.5.2.msi](http://python.org/ftp/python/2.5.2/python-2.5.2.msi)

Installed with all default settings EXCEPT install-to path

- C:\\Program Files\\Python25

## (Python) setuptools 

version 0.6c9

[http://pypi.python.org/pypi/setuptools](http://pypi.python.org/pypi/setuptools)

As of **Today** there wasn\'t a pre-built .EXE installer for Python 2.6 (which I\'d TRIED to test with first, to no avail), SO had to \"hack\" a bit - see IBM article link, above, for some info\... simply grab

- [http://peak.telecommunity.com/dist/ez_setup.py](http://peak.telecommunity.com/dist/ez_setup.py)

and run

- python ez_setup.py

Otherwise, if an installer is avail for your ver of Py, use it! ![:)](/wiki/europython/img/smile.png ":)")

## python-magic

version \'0.1\' (c112ac064b7f) with/for SWIG

[http://hupp.org/adam/hg/python-magic](http://hupp.org/adam/hg/python-magic)

**NOTE:** Adam (Hupp) doesn\'t have the SWIG version posted any longer; my copy isn\'t \"pristine\"; anybody have one lying around to send me? ![:)](/wiki/europython/img/smile.png ":)")

# Configuration & Changes 

## C:\\Program Files\\Python25\\Lib\\distutils 

### distutils.cfg

must have thiw file, with at least

{{{\[build\] compiler = mingw32}}}

### version.py

Due to newer [CygWin](./CygWin.html), change line 100 from

- {{{version_re = re.compile(r\'\^(\\d+) \\. (\\d+) (\\. (\\d+))? (\[ab\](\\d+))?\$\',

}}} to

- {{{version_re = re.compile(r\'\^(\\d+) \\. (\\d+) (\\. (\\d+))? (\\. (\\d+))?\$\',

}}}

# Do The Installation Shuffle 

Go to where you\'ve put the python-magic source files, then:

{{{path=%PATH%;C:\\Program Files\\Python25;C:\\cygwin\\bin;C:\\Program Files\\File\\bin

python setup.py install}}}

# Examples of Output You Might See 

### No setuptools 

{{{Traceback (most recent call last):

- File \"setup.py\", line 1, in \<module\>

  - from setuptools import setup, Extension

[ImportError](./ImportError.html): No module named setuptools}}}

### UNSUCCESSFUL build, due to no distutils.cfg compiler=mingw32 \"fix\" 

{{{running install running bdist_egg running egg_info creating magic.egg-info writing magic.egg-info\\PKG-INFO writing top-level names to magic.egg-info\\top_level.txt writing dependency_links to magic.egg-info\\dependency_links.txt writing manifest file \'magic.egg-info\\SOURCES.txt\' reading manifest file \'magic.egg-info\\SOURCES.txt\' writing manifest file \'magic.egg-info\\SOURCES.txt\' installing library code to build\\bdist.win32\\egg running install_lib running build_py copying magic.py -\> build\\lib.win32-2.5 copying cmagic.py -\> build\\lib.win32-2.5 running build_ext error: Python was built with Visual Studio 2003; extensions must be built with a compiler than can generate compatible binaries. Visual Studio 2003 was not found on this system. If you have Cygwin installed, you can try compiling with [MingW32](./MingW32.html), by passing \"-c mingw32\" to setup.py.}}}

### UNSUCCESSFUL build, due to the new CygWin meets the OLD/default distutils\\version.py regex (line 100) 

{{{running install running bdist_egg running egg_info writing magic.egg-info\\PKG-INFO writing top-level names to magic.egg-info\\top_level.txt writing dependency_links to magic.egg-info\\dependency_links.txt reading manifest file \'magic.egg-info\\SOURCES.txt\' writing manifest file \'magic.egg-info\\SOURCES.txt\' installing library code to build\\bdist.win32\\egg running install_lib running build_py running build_ext Traceback (most recent call last):

- File \"setup.py\", line 12, in \<module\>

  - libraries=\[\'magic\'\])\],

  File \"C:\\Program Files\\Python25\\lib\\distutils\\core.py\", line 151, in setup

  - dist.run_commands()

  File \"C:\\Program Files\\Python25\\lib\\distutils\\dist.py\", line 974, in run_commands

  - self.run_command(cmd)

  File \"C:\\Program Files\\Python25\\lib\\distutils\\dist.py\", line 994, in run_command

  - cmd_obj.run()

  File \"C:\\Program Files\\Python25\\lib\\site-packages\\setuptools-0.6c9-py2.5.egg\\setuptools\\command\\install.py\", line 76, in run File \"C:\\Program Files\\Python25\\lib\\site-packages\\setuptools-0.6c9-py2.5.egg\\setuptools\\command\\install.py\", line 96, in do_egg_install

etc., etc., etc. \...

- File \"C:\\Program Files\\Python25\\lib\\distutils\\version.py\", line 107, in parse
  - raise [ValueError](./ValueError.html), \"invalid version number \'%s\'\" % vstring

[ValueError](./ValueError.html): invalid version number \'2.18.50.20080625\'}}}

### Successful Build 

{{{running install running bdist_egg running egg_info writing magic.egg-info\\PKG-INFO writing top-level names to magic.egg-info\\top_level.txt writing dependency_links to magic.egg-info\\dependency_links.txt reading manifest file \'magic.egg-info\\SOURCES.txt\' writing manifest file \'magic.egg-info\\SOURCES.txt\' installing library code to build\\bdist.win32\\egg running install_lib running build_py running build_ext creating build\\bdist.win32 creating build\\bdist.win32\\egg copying build\\lib.win32-2.5\\cmagic.py -\> build\\bdist.win32\\egg copying build\\lib.win32-2.5\\magic.py -\> build\\bdist.win32\\egg copying build\\lib.win32-2.5\\\_cmagic.pyd -\> build\\bdist.win32\\egg byte-compiling build\\bdist.win32\\egg\\cmagic.py to cmagic.pyc byte-compiling build\\bdist.win32\\egg\\magic.py to magic.pyc creating stub loader for \_cmagic.pyd byte-compiling build\\bdist.win32\\egg\\\_cmagic.py to \_cmagic.pyc creating build\\bdist.win32\\egg\\EGG-INFO copying magic.egg-info\\PKG-INFO -\> build\\bdist.win32\\egg\\EGG-INFO copying magic.egg-info\\SOURCES.txt -\> build\\bdist.win32\\egg\\EGG-INFO copying magic.egg-info\\dependency_links.txt -\> build\\bdist.win32\\egg\\EGG-INFO copying magic.egg-info\\top_level.txt -\> build\\bdist.win32\\egg\\EGG-INFO writing build\\bdist.win32\\egg\\EGG-INFO\\native_libs.txt zip_safe flag not set; analyzing archive contents\... creating dist creating \'dist\\magic-0.1-py2.5-win32.egg\' and adding \'build\\bdist.win32\\egg\' to it removing \'build\\bdist.win32\\egg\' (and everything under it) Processing magic-0.1-py2.5-win32.egg Removing c:\\program files\\python25\\lib\\site-packages\\magic-0.1-py2.5-win32.egg Copying magic-0.1-py2.5-win32.egg to c:\\program files\\python25\\lib\\site-packages magic 0.1 is already the active version in easy-install.pth

Installed c:\\program files\\python25\\lib\\site-packages\\magic-0.1-py2.5-win32.egg Processing dependencies for magic==0.1 Finished processing dependencies for magic==0.1}}}

**NOTE:** Actually, this is what you\'ll see if you\'ve successfully RE-compiled\... but I digress\...

# Usage Notes 

{{{Python 2.5.2 (r252:60911, Feb 21 2008, 13:11:45) \[MSC v.1310 32 bit (Intel)\] on win32 Type \"help\", \"copyright\", \"credits\" or \"license\" for more information. \>\>\> import magic}}}

## magic1.dll Not in Path 

FIRST: Windows msgbox with red-X icon and \[OK\] button:

      TITLE: python.exe - Unable To Locate Component

      TEXT: This application has failed to start because magic1.dll was not found. Re-installing the application may fix this problem.

THEN (back in interpreter): {{{Traceback (most recent call last):

- File \"\<stdin\>\", line 1, in \<module\> File \"build\\bdist.win32\\egg\\magic.py\", line 2, in \<module\> File \"build\\bdist.win32\\egg\\cmagic.py\", line 5, in \<module\> File \"build\\bdist.win32\\egg\\\_cmagic.py\", line 7, in \<module\> File \"build\\bdist.win32\\egg\\\_cmagic.py\", line 6, in [bootstrap]

[ImportError](./ImportError.html): DLL load failed: The specified module could not be found.}}}

- **NOTE:** This is the same exact message (inside interpreter, NOT a Windows msgbox) that shows when I tried to use Py v2.6.

## Successful Import/Use 

{{{\>\>\> import magic \>\>\> test = magic.Magic() \>\>\> test.from_file( \'\\\\cygwin\\\\bin\\\\which.exe\' ) \'PE32 executable for MS Windows (console) Intel 80386 32-bit\'}}}

## Magic (Compiled) Files Not in Path/Elsewhere 

{{{\>\>\> import magic \>\>\> test = magic.Magic( magic_file = \'C:\\\\magic\' ) \# NOTE: This is the full path+filename of the magic db file \>\>\> test.from_file( \'\\\\startrek.exe\' ) \'MS-DOS executable, MZ for MS-DOS\'}}}

# File Location Information 

**DEFAULT/ASSUMED LOCATION FOR MAGIC DATABASE FILES IS** `C:\Program Files\File\share\file`

**NOTE:** magic1.dll file ***MUST BE FINDABLE IN THE PATH!!!***
