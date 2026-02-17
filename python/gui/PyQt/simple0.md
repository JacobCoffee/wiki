# PyQt/simple0

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

## Simple Stage 0 

**Prerequisites:** In order to reproduce this tutorial, please install sip4 and PyQt4 from

- [http://riverbankcomputing.com](http://riverbankcomputing.com)

Windows users can get away by installing one of the binary packages from

- [http://www.riverbankcomputing.com/software/pyqt/download](http://www.riverbankcomputing.com/software/pyqt/download)

after installing the corresponding Python 2.\* package from

- [http://python.org](http://python.org)

Mac users might want to follow

- [http://works13.com/blog/mac/installing-eric4-on-mac-os-x-leopard.htm](http://works13.com/blog/mac/installing-eric4-on-mac-os-x-leopard.htm)

to get a working [PyQt](PyQt) development environment. (Note: the Qt link is broken at the time of writing, try to use: [http://qt.nokia.com/downloads/qt-for-open-source-cpp-development-on-mac-os-x](http://qt.nokia.com/downloads/qt-for-open-source-cpp-development-on-mac-os-x))

Linux users should install the packages provided by the distribution, which are usually called python-sip, python-qt4, python-qscintilla. Watch out for related -devel packages also. They\'re needed as well, if the packager has split them off. (Many thanks to **Hans-Peter Jansen** for this section of the tutorial and many other valuable suggestions.)

**We start this project** in the Qt Designer in which we shall design the main form. Qt Designer is a graphical tool that is well explained with superior gui. The image of the application can be easily created and here is a result of a little more than 5 minutes work with it:

- ![in_designer_window.png](attachments/PyQt(2f)simple0/in_designer_window.png "in_designer_window.png")

Start with the Main Window form. Main Window includes a Title Bar at the top of the form and a Status Bar at the bottom. It also includes a menu bar. We start with one main menu, \"File\". Whilst in the Qt Designer, click on it and enter the items \"New\", \"Open\", \"Save\", \"Save As\". In the titles of menu items, one letter should be underlined to indicate an accelerator key. So, for instance, for \"New\" we type \"&New\" and for \"Save As\", we type \"Save &As\". with the result that N in New is underlined. Similarly, in Save As \"A\" is underlined.

Whilst typing, Designer shows the key pressed. The underlining only appears when the application is displayed. Conveniently, whilst in Qt Designer ctrl+R shows the form in its \"live\", working format. Please try to resize it after you added the textEdit widget. When you resize the Main Window, the textEdit widget should also resize automatically. If it does not, it shows that you forgot to add to the Main Window the \"Layout in a Grid\". The layout kind of \"glues\" the textEdit widget to the Main Window. A good set of tutorials and other material for learning are supplied with the Qt Designer and there is no real need to \"reinvent the wheel\" - please take advantage of that material to learn a little about the Qt Designer.

In live format, the form can be resized, moved around and eventually closed in the usual manner of GUI windows.

The information from the Designer is saved in a file with an extension \"ui\", so name it simple.ui and is placed in the same directory as the PyQt (and possibly Python) program. It needs to be converted to Python. This conversion can be achieved simply by using a pyuic4 script as follows:

     pyuic4 simple.ui > ui_simple.py

The program at this stage is very minimal. Here is the listing:

:::: 
::: 
``` 
   1 #!/usr/bin/env python
   2 # .../simple_0/simple.py
   3 '''A really simple editor program in PyQt4 - simple.py'''
   4 
   5 import sys
   6 
   7 from PyQt4.QtGui import (QMainWindow, QApplication)
   8 #from PyQt4.QtCore import *
   9 
  10 from ui_simple import Ui_MainWindow
  11 __version__ = "0.0.00"
  12 class MainWindow(QMainWindow, Ui_MainWindow):
  13     def __init__(self, parent=None):
  14         super(MainWindow, self).__init__(parent)                                         
  15         self.setupUi(self)
  16 
  17 if __name__ == '__main__':
  18     app = QApplication(sys.argv)
  19     frame = MainWindow()
  20     frame.show()
  21     app.exec_()
```
:::
::::

The \"program\" at this stage does not do anything, though it uses the **ui_simple.py** which is generated (\"compiled\") from the **simple.ui** file. To run it only needs QMainWindow and QApplication from the QtGui module. It turns out, we need nothing from the QtCore module at this stage.

This kind of program stub occurs in many applications. We have chosen to use Python\'s special feature of **multiple inheritance**, so that the methods of Ui_MainWindow becomes readily accessible without referring explicitly to Ui_MainWindow. The convenience of this will become more apparent after we add to this stub some means to better control the program.

[Return Home](./PyQt(2f)simple.html)
