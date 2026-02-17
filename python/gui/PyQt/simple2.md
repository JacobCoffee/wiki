# PyQt/simple2

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

## \"Simple\" Stage 2 

The fully functional, but not very useful Main Window now looks as follows:

- ![simple_1.png](attachments/PyQt(2f)simple2/simple_1.png "simple_1.png")

As you can see, we can type text in the editor window and edit it, but we can not save it or open an existing file. Enabling the Editor to save and/or open a file is the subject of our talk now. As a first step, we shall provide a method for starting a new file.

To start let us discuss the PyQt\'s signals and slots. Our code has been slightly extended as shown in the following table.

:::: 
::: 
``` 
   1 #!/usr/bin/env python
   2 # .../simple_1/simple.py
   3 #'''A really simple editor program in PyQt4 - simple.py'''
   4 
   5 import sys
   6 
   7 from PyQt4.QtGui import (QMainWindow, QApplication)
   8 from PyQt4.QtCore import SIGNAL
   9 
  10 from ui_simple import Ui_MainWindow
  11 __version__ = "0.0.01"
  12 class MainWindow(QMainWindow, Ui_MainWindow):
  13     def __init__(self, parent=None):
  14         super(MainWindow, self).__init__(parent)                                         
  15         self.setupUi(self)
  16 #        self.connect(self.action_New, SIGNAL("triggered()"), self.fileNew)
  17         self.action_New.triggered.connect(self.fileNew)
  18 
  19     def fileNew(self):
  20         '''Clear the editor window for a new file with name
  21         specified in fileSaveAs method.'''
  22         self.textEdit.setText('')
  23 #        self.textEdit.append('fileNew pressed')
  24         self.statusBar().showMessage('File menu: New selected', 8000)
  25                 
  26 if __name__ == '__main__':
  27     app = QApplication(sys.argv)
  28     frame = MainWindow()
  29     frame.show()
  30     app.exec_()
```
:::
::::

Whilst the application is running in its loop (app.exec\_()), the program performs various tasks in response to user interaction, viz. clicking of a button, selecting and clicking a menu item. The message to the program is via a SIGNAL SLOT mechanism in C++ language. Qt is written in C++. PyQt is a wrapper that enables us not to be concerned with the complexities of C++ and instead use a friendly Python language for the GUI programming based on Qt. PyQt is undergoing developing rather rapidly. Whilst the earlier version of PyQt required the Python program to closely follow the C++ syntax, the later PyQt versions are less demanding.

The SIGNAL SLOT mechanism is a good example of this. Earlier versions of PyQt required at least the keyword SIGNAL, which needed to be imported from the QtCore module. So the action to start the **fileNew** method looked like this:

    self.connect(self.action_New, SIGNAL("triggered()"), self.fileNew)

The effect of the above statement is that the click (called here \"trigger\") of the menu item \"New\" causes the method **\"fileNew\"** to be executed. The naming of this **\"action_New\"** and its connection to the menu item \"File/New\" are all done automagically for us by the Qt Designer - see the \"ui_simple.py\" file for details. The \"slot\" is the executable method \"self.fileNew\" and the keyword SLOT no longer appears in the older style SIGNAL SLOT connection of the PyQt. The syntax of PyQt has been further simplified and the new style of SIGNAL SLOT connection can now be written as follows:

     self.action_New.triggered.connect(self.fileNew)

Thus, we simply **\"connect\"** the event (trigger, click etc) and the resulting \"action\" (fileNew). In this tutorial we shall use the new style syntax for the SIGNAL SLOT connection. So in the listing the older style connection is left, but commented out.

#### Afterthoughts and Summary 

The program listing is only some 20 lines long. Hopefully, you typed it and tried out. The editor is barely functional - we can type the text in the window and the File \> New option will clear it, so one button reacts to keypress and does something useful! If you tried to copy via clipboard the listing, the result was probably less than very satisfying. We are lucky to be on a moinmoin wiki, as not all wikis render Python code so well as moinmoin.

For you convenience, program listing and other project files are stored in

    http://akabaila.pcug.org.au/data_sample/

in a file named **simple0.0.01.tar.gz,** which you can download, expand and use. The simple.py file is a result of typing with an editor. \"Eric\" is a great editor, written in Python and PyQt - very appropriate for programming in Python and PyQt! The file simple.ui is the result of using the \"Qt Designer\". It is converted to ui_simple.py by the program **makepyqt.pyw.**

Have I mentioned that all that I know about PyQt I have learned from an excellent text \"Rapid GUI Programming with Python and Qt\" by Mark Summerfield? Well, I mention it now - it is a great text book. This tutorial is meant to be a \"gentle\" introduction to the PyQt world and it would be a disservice to the reader not to point out the direction to a more thorough treatment of the subject.

[Return Home](simple)
