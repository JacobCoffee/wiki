# PyQt/simple4

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

## \"Simple\" Stage 4 

The program has now progressed and the GUI begins to look like GUIs usually look. Visually, the most noticeable change is the presence of several icons on the tool bar - basically, these icons have the same functionality as the menu items and are provided for the most frequently used operations. So we will need to talk some more about the **actions** and about generation and storage of **resources**. Once you download the program listing and start using it, other changes will be noticed: at the end of the mouse pointer, a **tool tip hint** pops up showing the purpose of the icon that the pointer is hovering over. Also, an informative note, often the same as the tool tip hint, is shown on the **status bar**.

In connection with the above, we will need to discuss how **icon images** are provided for icons.

One item that I missed in earlier versions is showing of the **title of document** opened in the edit window. The title is functional and it shows when the document has been altered. Not only that, there is a program bug that PyQt (or Qt) reports. I found the chasing after this bug as frustrating as it was instructive. It was not easy to find, yet I think that a programmer with experience in PyQt would spot it in no time at all! See if you can spot it easily.

![Simple0.0.06.png](attachments/PyQt(2f)simple4/Simple0.0.06.png "Simple0.0.06.png")

Below is the code listing for this stage of development. It is very often difficult to copy the code from a wiki. This is particularly so with Python programs, because Python relies on **indentation** for specification of code blocks (and it is such a **nice feature,** once you get used to it!). To make it simpler to test this stage of program, we provide a tar ball of program for downloading: see [http://akabaila.pcug.org.au/data_sample](http://akabaila.pcug.org.au/data_sample) and select the tar ball named **simple0.0.06.tar.gz.**

:::: 
::: 
``` 
   1 #!/usr/bin/env python
   2 # .../simple.py - developing of a simple text editor.
   3 '''A really simple editor program in PyQt4 - simple.py
   4 '''
   5 
   6 import sys
   7 import os
   8 
   9 from PyQt4.QtGui import (QMainWindow, QApplication, QFileDialog,
  10                          QKeySequence, QAction, QIcon)
  11 from PyQt4.QtCore import SIGNAL
  12 
  13 from ui_simple import Ui_MainWindow
  14 import qrc_simple
  15 
  16 __version__ = "0.0.06"
  17 
  18 class MainWindow(QMainWindow, Ui_MainWindow):
  19     def __init__(self, parent=None):
  20         super(MainWindow, self).__init__(parent)
  21         self.setupUi(self)        
  22         self.action_New = self.editAction(self.action_New, self.fileNew,
  23                 QKeySequence.New, "filenew", 
  24                 'Clear the textEdit window for a new file.')
  25         self.action_Open = self.editAction(self.action_Open, self.fileOpen, 
  26                         QKeySequence.Open, "fileopen", "Open an existing file")
  27         self.action_Save = self.editAction(self.action_Save, self.fileSave, 
  28                                 QKeySequence.Save, "filesave", "Save file")
  29         self.actionSave_As = self.editAction(self.actionSave_As, self.fileSaveAs, 
  30                             "Ctrl+A", "filesaveas", "Save file with a new name")
  31         self.fileName = None
  32 #-------------------------------------------------------------------------------------
  33         fileToolbar = self.addToolBar("File")
  34         self.addActions(fileToolbar, (self.action_New, self.action_Open,
  35                                       self.action_Save, self.actionSave_As))
  36 #--------------------------------------------------------------------------------------       
  37         self.resize(600, 400)
  38         self.dirty = False
  39         self.textEdit.textChanged.connect(self.setDirty)
  40 #--------------------------------------------------------------------------------------
  41     def setDirty(self):
  42         '''On change of text in textEdit window, set the flag
  43         "dirty" to True'''
  44         if self.dirty:
  45             return True        
  46         self.dirty = True
  47         self.updateStatus('self.dirty set to True')
  48        
  49     def clearDirty(self):
  50         '''Clear the dirty flag and update status'''
  51         self.dirty = False
  52 
  53     def updateStatus(self, message):
  54         if self.fileName is not None:
  55             flbase = os.path.basename(self.fileName)
  56             self.setWindowTitle(unicode("Simple Editor - " + flbase + "[*]") )
  57             self.statusBar().showMessage(message, 3000)
  58         self.setWindowModified(self.dirty)
  59         
  60     def okToContinue(self):
  61         if self.dirty:
  62             reply = QMessageBox.question(self,
  63                     "Simple Editor - Unsaved Changes",
  64                     "Save unsaved changes?",
  65                     QMessageBox.Yes|QMessageBox.No|QMessageBox.Cancel)
  66             if reply == QMessageBox.Cancel:
  67                 return False
  68             elif reply == QMessageBox.Yes:
  69                 return self.fileSave()
  70         return True
  71         
  72     def addActions(self, target, actions):
  73         for action in actions:
  74             if action is None:
  75                 target.addSeparator()
  76             else:
  77                 target.addAction(action)
  78 
  79     def editAction(self, action, slot=None, shortcut=None, icon=None,
  80                      tip=None, checkable=False, signal="triggered()"):
  81         if icon is not None:
  82             action.setIcon(QIcon(":/{0}.png".format(icon)))
  83         if shortcut is not None:
  84             action.setShortcut(shortcut)
  85         if tip is not None:
  86             action.setToolTip(tip)
  87             action.setStatusTip(tip)
  88         if slot is not None:
  89 #            self.connect(action, SIGNAL(signal), slot)            
  90             action.triggered.connect(slot)                        
  91         if checkable:
  92             action.setCheckable(True)
  93         return action
  94 
  95     def fileNew(self):
  96         '''Clear the editor window for a new file with name
  97         specified in fileSaveAs method.'''
  98         self.textEdit.setText('')
  99         self.statusBar().showMessage('File menu: New selected', 8000)
 100 
 101     def fileOpen(self):
 102         '''Open file'''
 103         fname = unicode(QFileDialog.getOpenFileName(self,
 104                         "Open File", '.', "Files (*.*)"))
 105         if not (fname == ""):
 106             self.textEdit.setText(open(fname).read())
 107             self.fileName = fname
 108         else:
 109             return
 110         self.clearDirty()
 111         self.updateStatus('File opened.')
 112        
 113     def fileSave(self):
 114         if self.fileName is None:
 115             return self.fileSaveAs()
 116         else:
 117             fname = self.fileName
 118             fl = open(fname, 'w')
 119             tempText = self.textEdit.toPlainText()
 120             if tempText:                
 121                 fl.write(tempText)
 122                 fl.close()
 123                 self.clearDirty()
 124                 self.updateStatus('Saved file') 
 125                 return True
 126             else:
 127                 self.statusBar().showMessage('Failed to save ...', 5000)
 128                 return False
 129         
 130     def fileSaveAs(self):
 131         path = self.fileName if self.fileName is not None else "."
 132         fname = unicode(QFileDialog.getSaveFileName(self,
 133                         "Simple Editor, SaveAs ", path, "Any File (*.*)"))
 134         if fname:
 135             if "." not in fname:
 136                 fname += ".txt"
 137             self.fileName = fname
 138             self.fileSave()        
 139             self.statusBar().showMessage('SaveAs file' + fname, 8000)
 140             self.clearDirty()
 141             
 142 if __name__ == '__main__':
 143     app = QApplication(sys.argv)
 144     frame = MainWindow()
 145     frame.show()
 146     app.exec_()
```
:::
::::

The listing is more extensive - the number of lines has about doubled from the previous section. On the other hand, the simple editor now looks like a \"real\" program and is able to do what we expect of a simple, tutorial type, plain text editor!

[Return Home](simple)
