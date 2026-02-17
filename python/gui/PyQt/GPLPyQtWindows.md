# PyQt/GPLPyQtWindows

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# Getting GPLed Qt/PyQt Running on Windows 

### Note: This page has become somewhat obsolete with the release of Qt 4.x under the GPL. 

There is a new page that describes how to build [PyQt4](PyQt4) at [BuildPyQt4Windows](BuildPyQt4Windows).

## Background 

One of the frustrations I\'ve always had with Qt is that current versions could not be used on Windows without paying a substantial developer fee for the license. I balked at this because

- I really couldn\'t afford it, and
- I wasn\'t writing commercial software anyways.

However, this has changed. The people over at the kde-cygwin project have taken the GPLed version of Qt and ported it to native Windows (i.e. it does not require Cygwin). As soon as I saw this, I immediately started to try and get [PyQt](PyQt) to compile against this version. Amazingly, it didn\'t take nearly as much work as I thought it would.

## Requirements 

- Python (version 2.3 or later)
- A Windows compiler suite. Either Borland, MinGW, MS VC++ 6.0, or MS VS.NET

## The process 

- **\* 1) Install Qt from the [qt-win](http://qtwin.sourceforge.net/qt3-win32/index.php) (formally kde-cygwin) project**

  - I was able to follow [these compile instructions](http://qtwin.sourceforge.net/qt3-win32/compile-net.php) in order to get my copy to build with MS Visual Studio.NET. There are also compile instructions for [Borland](http://qtwin.sourceforge.net/qt3-win32/compile-borland.php), [MinGW](http://qtwin.sourceforge.net/qt3-win32/compile-mingw.php) and [MS Visual C++ 6.0](http://qtwin.sourceforge.net/qt3-win32/compile-msvc.php).

    Configure notes:\
    I usually configure Qt with threading and GIF support, so I run configure.bat as the following:\
    `C:\qt-3> configure.bat -thread -gif -fast`\
    If you want to install the libraries and such in different places you can use the standard UNIX configure argument of `-prefix [path]` After a little while of compiling, you should have a full Qt-3.3.3 installation. You can check this by looking at QTDIR/lib (or if you set -prefix, whereever that is) and making sure qt-mt3.dll (multithreaded) or qt3.dll (single-threaded) is there. Things to be aware of:

    - Make sure you set the appropriate QTDIR, PATH, and QMAKESPEC environment variables (as it mentions in the compile instructions). Failure to do so will just make your build stop with not so explanatory error messages.

    - I\'ve noticed (and so have others), that the source does not like to be unpacked into a directory that includes spaces. I usually unpack it into C:\\qt-3 to be safe. Putting quotes around the directory when setting the QTDIR environment variable (e.g. set QTDIR=\"C:\\path with spaces\") seems to give the build process fits also.

    - On my MS VS.NET install instead of running\

      - `vcvars32.bat`\
        I needed to run\
        `\Microsoft Visual Studio.NET\Common7\Tools\vsvars32.bat` I suspect most people will not have this problem because at some point my .NET install became horribly broken.

  **\* 2) Get and install SIP**

  - SIP is available at [Riverbank Computing](http://www.riverbankcomputing.co.uk/) [here](http://www.riverbankcomputing.co.uk/sip/download.php). I have been using sip-4.1.1 for Windows. If you choose to directly download from Riverbank, your copy of SIP will need to be patched with [this patch](http://prdownloads.sourceforge.net/kscraft/sip-4.1.1.diff?download) before installation. The reason for the patch (or hack, really) is that the Qt install and SIP disagree on the format of the Qt DLL name (SIP looks for qt-mt333.dll whereas the Qt install generates qt-mt3.dll)

    To configure and install SIP, you can follow [these instructions](http://www.river-bank.demon.co.uk/docs/sip/sipref.html#configuring-sip). I usually run the following (for MSVC or MSVC.NET, multithreaded Qt and Python 2.4):

               C:\sip-4.1.1> C:\python24\python configure.py -l qt-mt
               C:\sip-4.1.1> nmake
               C:\sip-4.1.1> nmake install

<!-- -->

- **\* 3a) Get and install QScintilla (optional)**

  - If you want to be able to run the Eric3 IDE (or anything else that uses QScintilla), now is the time to install it.

    QScintilla is available at [Riverbank Computing](http://www.riverbankcomputing.co.uk/) [here](http://www.riverbankcomputing.co.uk/qscintilla/download.php). The installation is fairly easy. You can follow the directions from the README exactly. Just make sure you still have your QTDIR and PATH environment variables set up properly from the previous step or else it won\'t be able to find qmake, etc\...

  <!-- -->

  - For those who are lazy, the install instructions from the README are as follows:

    To build QScintilla on Windows, run:

              C:\qscintilla-1.4> cd qt
              C:\qscintilla-1.4\qt> qmake qscintilla.pro
              C:\qscintilla-1.4\qt> nmake 
              C:\qscintilla-1.4\qt> copy qextscintilla*.h %QTDIR%\include
              C:\qscintilla-1.4\qt> copy qscintilla*.qm %QTDIR%\translations
              C:\qscintilla-1.4\qt> copy %QTDIR%\lib\qscintilla.dll %QTDIR%\bin

    **Note:** If you read the README, you\'ll notice that it has the following statement:\
    *Please do not try to build the GPL version of QScintilla under Windows. It will not work and you would be contravening the GPL.*\
    You do not have to worry about this anymore since the version of Qt that you installed is GPLed. This is referring to installing QScintilla against one of the commerically licensed Qt-Windows versions which are not released under the GPL.

  <!-- -->

  - **\* 3) Get and install [PyQt](PyQt)**

    - PyQt is available at [Riverbank Computing](http://www.riverbankcomputing.co.uk/) [here](http://www.riverbankcomputing.co.uk/pyqt/download.php).

    <!-- -->

    - I have been using version [PyQt](PyQt)-x11-gpl-3.13.

      Like SIP, PyQt also needs to be patched. If you downloaded the source from Riverbank, you need to apply this [patch](http://prdownloads.sourceforge.net/kscraft/PyQt-x11-3.13.diff?download). I have also made an already patched .zip archive available [here](http://prdownloads.sourceforge.net/kscraft/PyQt-x11-gpl-3.13-patched.zip?download). The patch is for some types that the Windows port of Qt needs that aren\'t included in PyQt by default.

      To configure and install PyQt, I usually use these commands (for MSVC.NET and Python 2.4):

                C:\PyQt-x11-gpl-3.13> C:\python24\python configure.py
                C:\PyQt-x11-gpl-3.13> nmake
                C:\PyQt-x11-gpl-3.13> nmake install

      And that\'s it! You should now have a fully functional port of PyQt on Windows.

      As a first pass of testing to see if all went well, you can fire up the Python interpreter and try

                >>> import qt

      and hopefully it succeeds. If you do get an ImportError, check that you followed all the instructions correctly.

  **\* 4) Get and install Eric3 (optional)**

  - Note: In order to install Eric3, you must have installed QScintilla above

    Eric3 is available [here](http://www.die-offenbachs.de/detlev/eric3.html).

    Just unpack it and run the install script:

              C:\eric-3.5.1> python install.py

    You can change the default install paths, run with \--help for details.

Questions or comments? Email me at: jlamanna AT gmail DOT com

Page by James Lamanna - Copyright 2005
