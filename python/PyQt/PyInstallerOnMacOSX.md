# PyQt/PyInstallerOnMacOSX

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# Using PyInstaller with PyQt on Mac OS-X 

PyInstaller has only preliminary support for Mac OS-X and currently (Feb. 2010) needs some workarounds and modifications to work properly with PyQt. Therefore this short how-to will show the steps to make the QtWebKit based \'Minibrowser\' sample app from [here](http://eric-ide.python-projects.org/tutorials/MiniBrowser/index.html) into an OS-X application bundle.

## Prerequisites 

- Recent versions of Qt and PyQt need to be installed.

I installed PyQt and Eric4 according to [this](http://works13.com/blog/mac/installing-eric4-on-mac-os-x-leopard.htm) guide. The following versions were used: OS-X 10.6.2, Python 2.6.1, Qt 4.6.2., PyQt 4.7, sip 4.10, QScintilla 2.4.2. Eric4 is obviously optional for the purpose of this how-to.

## Installing and patching PyInstaller 

- Create a working folder, for example:
  - /Users/username/pywork
  - Open a Terminal window and
    -       $ mkdir pywork
                $ cd pywork
- Download the current pyinstaller source:
  -       $ svn co http://svn.pyinstaller.org/trunk pyinstaller

    \> Checked out revision 771
- Modify pyinstaller/source/linux/main.c by commenting out the following \'wait()\' section at the end of the file:
  -         wait(&rc);
                rc = WEXITSTATUS(rc);

                VS("Back to parent...\n");
                if (strcmp(workpath, homepath) != 0)
                    clear(workpath);

    This deals with the problem \"Icon and Menu is missing from PyQt apps, when running an OS-X App Bundle\". The patch is described and can be downloaded [here](http://www.pyinstaller.org/ticket/156).

           $ cd pyinstaller/source/linux
           $ patch --verbose main.c main.patch
- Setup pyinstaller:
  -       $ cd pyinstaller/source/linux
              $ python ./Make.py
              $ make
              $ cd ../..
              $ python Configure.py
- Patch Build.py, otherwise we get a \'Python image not found error\'
  - Browse to Ticket #152 [\"pyinstaller onefile fails to bundle Python framework shared lib on osx\"](http://www.pyinstaller.org/ticket/152)

  - Download [pyinstaller.patch](http://www.pyinstaller.org/raw-attachment/ticket/152/pyinstaller.patch) and copy it into pywork/pyinstaller

    -     $ patch --verbose Build.py pyinstaller.patch

## Making the Application into an App Bundle 

- Download a the Minibrowser sample project:
  - From [here](http://eric-ide.python-projects.org/tutorials/MiniBrowser/resources/minibrowser.zip) into the pywork directory and unzip

- In the main loop add window.raise\_():
  - this deals with the PyQt specific problem in OS-X, that an application window is not automatically brought to the front on launch as expected. [link](http://www.pyinstaller.org/ticket/158)

  - for example in pywork/minibrowser/minibrowser.py modify as follows

  <!-- -->

  - :::: 
    ::: 
    ``` 
       1     ui = MainWindow()
       2     ui.show()
       3     ui.raise_()
    ```
    :::
    ::::

- Change to the pywork directory & make the spec file:

  -    $ cd ..
           $ python pyinstaller/Makespec.py --out=MinibrowserTmp minibrowser/minibrowser.py

- Add the following to the bottom of your spec file:
  -     import sys 
            if sys.platform.startswith("darwin"): 
                app = BUNDLE(exe, 
                          appname='Minibrowser', 
                          version='1.0')

- Build the Application Bundle:
  -    $ python pyinstaller/Build.py MinibrowserTmp/minibrowser.spec

- Fix the Bundle:
  - Change the key in pywork/Minibrowser.app/Contents/Info.plist to
    -          <key>LSBackgroundOnly</key>
                   <false/>

- To deal with the issue \'OS-X App Bundle is missing most files\' described [here](http://www.pyinstaller.org/ticket/155)

  - Copy the missing app files into pywork/Minibrowser.app/Contents/MacOS:
    -       $ cp -rv MinibrowserTmp/dist/minibrowser/* Minibrowser.app/Contents/MacOS

- To prevent the Error: \'qt_menu.nib could not be loaded\' described [here](http://www.pyinstaller.org/ticket/157)

  - Into the pywork/Minibrowser.app/Contents/Resources folder copy qt_menu.nib from /Library/Frameworks/QtGui.framework/Versions/4/Resources/qt_menu.nib
    -       $ cp -rv /Library/Frameworks/QtGui.framework/Versions/4/Resources/qt_menu.nib Minibrowser.app/Contents/Resources

## Test and Compress the App 

- You should now be able to run the application bundle just like any native OS-X application by double clicking on it.

- Minibrowser usage: Enter a url and *click* the Navigate button

- Package the app in a compressed dmg for distribution, this reduces the size to about one third.

Check the linked issue tickets and PyInstaller [tracker](http://www.pyinstaller.org/report/1) and release notes, as these issues will be resolved sometime and the steps with workarounds will hopefully not be needed any more.
