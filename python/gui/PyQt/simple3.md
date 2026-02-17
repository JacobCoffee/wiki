# PyQt/simple3

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

## \"Simple\" Stage 3 

Here is listing of the next stage, namely **Stage 3**:

:::: 
::: 
``` 
   1 #!/usr/bin/env python
   2 # .../simple_1/simple.py
   3 '''A really simple editor program in PyQt4 - simple.py'''
   4 
   5 import sys
   6 
   7 from PyQt4.QtGui import (QMainWindow, QApplication, QFileDialog)
   8 from PyQt4.QtCore import SIGNAL
   9 
  10 from ui_simple import Ui_MainWindow
  11 __version__ = "0.0.04"
  12 class MainWindow(QMainWindow, Ui_MainWindow):
  13     def __init__(self, parent=None):
  14         super(MainWindow, self).__init__(parent)                                         
  15         self.setupUi(self)
  16         self.action_New.triggered.connect(self.fileNew)
  17         self.action_Open.triggered.connect(self.fileOpen)
  18         self.action_Save.triggered.connect(self.fileSave)
  19         self.actionSave_As.triggered.connect(self.fileSaveAs)
  20         self.fileName = None
  21         
  22     def fileNew(self):
  23         '''Clear the editor window for a new file with name
  24         specified in fileSaveAs method.'''
  25         self.textEdit.setText('')
  26         self.statusBar().showMessage('File menu: New selected', 8000)
  27 
  28     def fileOpen(self):
  29         '''Open file'''
  30         fname = unicode(QFileDialog.getOpenFileName(self,
  31                         "Open File", '.', "Files (*.*)"))
  32         if not (fname == ""):
  33             self.textEdit.setText(open(fname).read())
  34             self.fileName = fname
  35         else:
  36             return
  37         self.statusBar().showMessage('File opened ', 8000)
  38   
  39     def fileSave(self):
  40         if self.fileName is None:
  41             return self.fileSaveAs()
  42         else:
  43             fname = self.fileName
  44             fl = open(fname, 'w')
  45             tempText = self.textEdit.toPlainText()
  46             if tempText:                
  47                 fl.write(tempText)
  48                 fl.close()
  49                 self.statusBar().showMessage('Saved file ' + fname, 8000)
  50                 return True
  51             else:
  52                 self.statusBar().showMessage('Failed to save ...', 5000)
  53                 return False
  54         
  55     def fileSaveAs(self):
  56         dir = self.fileName if self.fileName is not None else "."
  57         fname = unicode(QFileDialog.getSaveFileName(self,
  58                         "Simple Editor, SaveAs ", dir, "Any File (*.*)"))
  59         if fname:
  60             if "." not in fname:
  61                 fname += ".txt"
  62             self.fileName = fname
  63             self.fileSave()        
  64             self.statusBar().showMessage('SaveAs file' + fname, 8000)
  65        
  66 if __name__ == '__main__':
  67     app = QApplication(sys.argv)
  68     frame = MainWindow()
  69     frame.show()
  70     app.exec_()
```
:::
::::

We will put this snipped of a code again to [http://akabaila.pcug.org.au/data_sample/](http://akabaila.pcug.org.au/data_sample/) directory and will name it **simple0.0.04.tar.gz.** Please download it and save it for testing the program. This version is a bit longer than that of **Stage 2,** but it is already a fully working program - you start a new document, type the text and save it as **some_file_name;** open a file and edit it and save it with the same name; you can exit the program. Of course, right from the **Stage 0,** the edit window can be resized, the window can be moved to any desired location. The typed part of program is still only some 70 lines long.

So why don\'t we stop here, pat ourselves on the shoulder for a job well done and retire? Well, to begin with, it is unusual for modern GUIs to only have menus to invoke various actions, so we need some tool bars and populate them with icons that have the same effect as the menu items. Icons will need images and we may as well append those images to the menu items. We also should help the user avoid shooting himself or herself in the foot and warn about destructive actions. So if there is a text in the window that has been altered from the originally loaded source of it and the user requests to open a new file, we should issue a **warning** about it. There probably are other situations that we should draw user attention to.

One small item really bugged me when I started to use this partially complete program - I sorely missed the lack of **title of opened file.** That needs to be also attended too.

It would be useful to issue tips at the end of the mouse arrow when it is hovering over representation of an action (an icon that invokes action). It would be nice to also have the status bar at the bottom of the edit window, to display the status information.

From **Stage 2** to **Stage 3** was a small step. After all, in **Stage 3** we did with all actions that which we in **Stage 2** did with **file_New** action. Though the program text is about 3 times bigger, there is nothing new or unfamiliar. So it may come as a surprise that the completed program in the **finished** Stage is some 3 times longer than **Stage 3**, though it is still small as programs go.

One thing that needs to be stressed - we are using the results of **Qt Designer**, which produced file **simple.ui,** which we compiled to python source, named **ui_simple.py.** We did not invent the action names - we took them from **ui_simple.py!** We do want to make as much use of the information from **Qt Designer** as possible. No need to reinvent the wheel!

Yes, **ui_simple.py** is full of useful information, but the code should not be edited. Of course, we can get a new **simple.ui** with different setup from the Qt Designer any time we want to. That allows substantial alterations to the form that we have designed in the first place. However its compilation would wipe out any editing of the ui_simple.py file. That\'s why it is best not to edit it.

A plea to you all - if you visit this tutorial, please drop a line to me at the following address: **akabaila\[at\]pcug\[dot\]org\[dot\]au.** It would be great if you would kindly report any glitches that you encounter - that\'s what open source software is all about! Thank you.

[Return Home](simple)
