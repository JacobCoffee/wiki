# BuildPyQt4Windows

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# The No-fuss Guide to Building PyQt on Windows XP

  --------- ------------------------------------------------------------------------------------------
  Date:     2007-07-11
  Author:   Martin Blais \<[blais@furius.ca](mailto:blais@furius.ca)\>
  --------- ------------------------------------------------------------------------------------------

::: 
Abstract

This document contains instructions on building PyQt under Windows, using the pre-built binary version of Qt installed via its installer.
:::

:::: 
### Introduction

Typically, you want to built the PyQt snapshots when it is lagging a little bit behind the Qt release. When I wrote this document, I wanted to build PyQt for Qt-4.3.3 and there was no binary at that time.

See this thread for more details: [http://www.mail-archive.com/pyqt%40riverbankcomputing.com/index.html#11081](http://www.mail-archive.com/pyqt%40riverbankcomputing.com/index.html#11081)

Note: follow these instructions to-the-letter. This is Windows. Any slight variation might throw you off.

::: 
#### Versions

This document is up-to-date for the following versions:

- Qt-4.3.3
- Python-2.5
- MinGW-5.1.3
- SIP snapshot as of 2007-07-11
- PyQt4 snapshot as of 2007-07-11
:::
::::

::::::::: 
### Detailed Instructions

::: 
#### Installing Qt

- Grab the binary installer (.exe) for the latest Qt release on TrollTech\'s webpage.
- Execute the installation, with or without MinGW depending on if you already have it.

This will place Qt in `C:\Qt\<version>` by default.
:::

::: 
#### Installing Python

- Download the Python MSI binary from the python.org website and run it, and install it (typically in `C:\Python25\python.exe`).
:::

::: 
#### Installing MinGW

You will need an install of MinGW that contains `mingw32-make.exe`. Install MinGW using the binaries from the MinGW website. I placed mine in `C:\MinGW`.

- Make sure you have:

      C:\MinGW\bin/mingw32-make.exe
      C:\MinGW\bin/g++.exe
:::

::: 
#### Setting up for Build

You MUST use the `cmd.exe` shell, and not Cygwin\'s bash nor MinGW nor MKS not anything else.

Start `cmd.exe` and set your PATH to something clean that contains both MinGW and Qt:

    set PATH=C:\WINDOWS\system32;C:\WINDOWS;C:\WINDOWS\System32\Wbem;C:\Qt\4.3.3\bin;C:\MinGW\bin

Verify your PATH configuration by running these two commands:

    g++ -v
    qmake -v
:::

::: 
#### Building and Installing SIP

- Download and unpack the SIP snapshot source for Windows.

- Configure it, making sure to use the `-p` option (otherwise the build runs in an infinite loop):

      C:\tmp\sip-snapshot-20070704> C:/Python25/python configure.py -p win32-g++
      C:\tmp\sip-snapshot-20070704> mingw32-make
      C:\tmp\sip-snapshot-20070704> mingw32-make install

This should install the following files in your Python library:

    C:\Python25\include\sip.h
    C:\Python25\Lib\site-packages\sip.pyd
    C:\Python25\Lib\site-packages\sipconfig.py
    C:\Python25\Lib\site-packages\sipconfig.pyc
    C:\Python25\Lib\site-packages\sipdistutils.py
    C:\Python25\sip.exe
:::

::: 
#### Building and Installing PyQt

Using the same shell setup as above,

- Download and unpack the PyQt4 snapshot source for Windows.

- Configure it:

      C:\tmp\PyQt-win-gpl-4-snapshot-20070710> C:/Python25/python configure.py -w
      Determining the layout of your Qt installation...
      C:\Qt\4.3.3\bin\qmake.exe -o qtdirs.mk qtdirs.pro
      mingw32-make -f qtdirs.mk release
      mingw32-make -f qtdirs.mk.Release
      mingw32-make[1]: Entering directory `C:/tmp/PyQt-win-gpl-4-snapshot-20070710'
      g++ -c -O2 -frtti -fexceptions -mthreads -Wall -DUNICODE [...]
      g++ -enable-stdcall-fixup -Wl,-enable-auto-import [...]
      lqtmain -lQtCore4
      mingw32-make[1]: Leaving directory `C:/tmp/PyQt-win-gpl-4-snapshot-20070710'
      release\qtdirs.exe
      This is the GPL version of PyQt 4-snapshot-20070710 (licensed under the GNU
      General Public License) for Python 2.5 on win32.

      Type 'L' to view the license.
      Type 'yes' to accept the terms of the license.
      Type 'no' to decline the terms of the license.

      Do you accept the terms of the license? yes
      Checking to see if the QtGui module should be built...
      g++ -DUNICODE -DQT_LARGEFILE_SUPPORT -DQT_DLL -DQT_NO_DEBUG -DQT_GUI_LIB -I. -IC:\Qt\4.3.3\mkspecs\default [...]
      [...]

  This should complete succesfully.

  Note: you should not have to set any variable. QTDIR is now obsolete. QMAKESPEC should be found automatically, but if it is not, you can probably safely use the `-p win32-g++` option.

- Compile it:

      C:\tmp\PyQt-win-gpl-4-snapshot-20070710> mingw32-make

- Install it:

      C:\tmp\PyQt-win-gpl-4-snapshot-20070710> mingw32-make install

This should install the following files:

    C:/Python25
    C:/Python25/Lib/site-packages
    C:/Python25/Lib/site-packages/PyQt4
    C:/Python25/Lib/site-packages/PyQt4/pyqtconfig.py
    C:/Python25/Lib/site-packages/PyQt4/Qt.pyd
    C:/Python25/Lib/site-packages/PyQt4/QtAssistant.pyd
    C:/Python25/Lib/site-packages/PyQt4/QtCore.pyd
    C:/Python25/Lib/site-packages/PyQt4/QtDesigner.pyd
    C:/Python25/Lib/site-packages/PyQt4/QtGui.pyd
    C:/Python25/Lib/site-packages/PyQt4/QtNetwork.pyd
    C:/Python25/Lib/site-packages/PyQt4/QtOpenGL.pyd
    C:/Python25/Lib/site-packages/PyQt4/QtScript.pyd
    C:/Python25/Lib/site-packages/PyQt4/QtSql.pyd
    C:/Python25/Lib/site-packages/PyQt4/QtSvg.pyd
    C:/Python25/Lib/site-packages/PyQt4/QtTest.pyd
    C:/Python25/Lib/site-packages/PyQt4/QtXml.pyd
    C:/Python25/Lib/site-packages/PyQt4/uic
    C:/Python25/Lib/site-packages/PyQt4/uic/Compiler
    C:/Python25/Lib/site-packages/PyQt4/uic/Loader
    C:/Python25/Lib/site-packages/PyQt4/uic/widget-plugins
    C:/Python25/Lib/site-packages/sip.pyd
    C:/Python25/Lib/site-packages/sipconfig.py
    C:/Python25/Lib/site-packages/sipconfig.pyc
    C:/Python25/pylupdate4.exe
    C:/Python25/pyrcc4.exe
    C:/Python25/pyuic4.bat
    C:/Python25/sip
    C:/Python25/sip/PyQt4
    C:/Python25/sip/PyQt4/Qt
    C:/Python25/sip/PyQt4/Qt/Qtmod.sip
    C:/Python25/sip/PyQt4/QtAssistant
    C:/Python25/sip/PyQt4/QtCore
    C:/Python25/sip/PyQt4/QtDesigner
    C:/Python25/sip/PyQt4/QtGui
    C:/Python25/sip/PyQt4/QtNetwork
    C:/Python25/sip/PyQt4/QtOpenGL
    C:/Python25/sip/PyQt4/QtScript
    C:/Python25/sip/PyQt4/QtSql
    C:/Python25/sip/PyQt4/QtSvg
    C:/Python25/sip/PyQt4/QtTest
    C:/Python25/sip/PyQt4/QtXml
:::
:::::::::

::: 
### Test It

Run Python and import PyQt4 to test it:

    C:\tmp\PyQt-win-gpl-4-snapshot-20070710>C:/Python25/python
    Python 2.5 (r25:51908, Sep 19 2006, 09:52:17) [MSC v.1310 32 bit (Intel)] on win32
    Type "help", "copyright", "credits" or "license" for more information.
    >>> from PyQt4.Qt import *
    >>> from sip import *
    >>> print SIP_VERSION_STR, QT_VERSION_STR, PYQT_VERSION_STR
:::
