# PyQt/simplefinis

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

## \"Simple Finished\" 

#### Preamble 

If you want **just to run** the example, you are advised to:

- Read at lest the **prerequisites** section of **Stage 0**

- Download and expand the tar ball **\"simple0.1.00.tar.gz\"** from [http://akabaila.pcug.org.au/data_sample/](http://akabaila.pcug.org.au/data_sample/) It has the required resource files.

#### Introduction 

It is usual to present tutorials with part of the project and only then the whole. It seems to me that it is not the best way. I feel that it is better to first state the objective and show what the finished project will look like and only then take it in small steps, showing at each step what has been achieved.

The aim of this tutorial is to show how a simple, yet reasonably complete, plain text editor can be created using the PyQt. We shall call that simple editor, rather appropriately, \"Simple\". As we are first presenting the finished project, some readers will want to see how it was done and try it out themselves. They are urged to look at each Stage 0 first, then Stage 1 and so on. Please try to code each stage yourselves, as you will gain most out of doing, rather than reading.

Other readers my find that the example is too simple for them and they are looking for some specific, advanced technique. By making discovering this in early reading of this tutorial they will be saved unnecessary looking through this presentation that is too simple and pace that is too slow. The motto for this tutorial is \"from a newbie to other newbies\" and we apologise up front if it does not apply to you.

### \"Simple\" Finished 

**Finished** is a relative term - there are features which could usefully be added to this GUI program, but they may well be contrary to the aim of keeping the example as simple as possible.

The main item in that category is saving the program state at the time of closing it and remembering the state when next opening the program. The technique to do that is well described in chapter 6 of the book \"Rapid GUI Programming with Python and Qt\" by Mark Summerfield. It is a fine book well worth a place on every PyQt programmers desk. The omission of this feature is partly prompted by similar omissions from some \"standard\" programs, notably \"Dolphin\" file manager. Personally when I use \"Dolphin\", I wish that it did \"remember\" where we were at in the previous session\... But it it is good enough for systems programmers to forget about it, it may be good enough for a tutorial example that aims at simplicity!

One other feature requires qualification: the \"help\" files are installed in the \"qrc\" resources. That is convenient, but also doubtful in view of its lack of economy of RAM. It seems that the resource file is automatically loaded in memory at the start of the program. That my be fine today when the memory is measured in Giga Bytes. Fine, provided that the program does not require large memory for, say, equations solving, a feature of programs for Structural Analysis of Engineering Structure, my area of interest. So personally, I would prefer to save resources of RAM and leave the help system in html format, particularly since help system, IMHO, is never too extensive.

#### Image of \"Simple\" 

![editor0.1.00.png](attachments/PyQt(2f)simplefinis/editor0.1.00.png "editor0.1.00.png")

#### Program Listing of \"Simple\" 

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
   8 import platform
   9 
  10 from PyQt4.QtGui import (QMainWindow, QApplication, QFileDialog,
  11                          QKeySequence, QAction, QIcon, QMessageBox)
  12 from PyQt4.QtCore import (SIGNAL, PYQT_VERSION_STR, QT_VERSION,
  13                           QT_VERSION_STR)
  14 
  15 from ui_simple import Ui_MainWindow
  16 import qrc_simple
  17 import helpform
  18 
  19 __version__ = "0.1.00"
  20 
  21 class MainWindow(QMainWindow, Ui_MainWindow):
  22     def __init__(self, parent=None):
  23         super(MainWindow, self).__init__(parent)
  24         self.setupUi(self)        
  25         self.action_New = self.editAction(self.action_New, self.fileNew,
  26                 QKeySequence.New, "filenew", 
  27                 'Clear the textEdit window for a new file.')
  28         self.action_Open = self.editAction(self.action_Open, self.fileOpen, 
  29                         QKeySequence.Open, "fileopen", "Open an existing file")
  30         self.action_Save = self.editAction(self.action_Save, self.fileSave, 
  31                                 QKeySequence.Save, "filesave", "Save file")
  32         self.actionSave_As = self.editAction(self.actionSave_As, self.fileSaveAs, 
  33                             "Ctrl+A", "filesaveas", "Save file with a new name")
  34         self.action_Quit = self.editAction(self.action_Quit, self.fileQuit, 
  35                             "Ctrl+Q", "filequit", "Close main window and application")
  36         self.fileName = None
  37         fileToolbar = self.addToolBar("File")
  38         self.addActions(fileToolbar, (self.action_New, self.action_Open,\
  39                                        self.action_Save, self.actionSave_As))
  40         self.resize(800, 600)
  41         self.dirty = False
  42         self.textEdit.textChanged.connect(self.setDirty)
  43 #=================================================================================
  44 # Supplementary stuff for Help/aTutorialNoteAbout and Help/Help menu items.
  45         self.actionA_bout = self.editAction(self.actionA_bout, self.about, 
  46                                             "Ctrl+B", "about", "Popup About dialog")
  47         self.action_Help = self.editAction(self.action_Help, self.help, 
  48                                            "Ctrl+H", "help", "Show Help pages")
  49         helpToolBar = self.addToolBar("Help")
  50         self.addActions(helpToolBar, (self.actionA_bout, self.action_Help))
  51 #=================================================================================
  52 # Add quit tool bar. It would be nice to have it at the right side of MainWindow...
  53         quitToolBar = self.addToolBar("Quit")
  54         self.addActions(quitToolBar, (self.action_Quit, ))
  55 #=================================================================================
  56 
  57     def fileQuit(self):
  58         pass
  59         
  60     def about(self):
  61         '''Popup a box with about message.'''
  62         QMessageBox.about(self, "About Simple Editor",
  63                 """<b>Simple</b> v %s
  64                 <p>Copyright &copy; 2010 A. Kabaila. 
  65                 All rights reserved in accordance with
  66                 GPL v2 or later.
  67                 <p>This application can be used for 
  68                 simple plain text editing.
  69                 <p>Python %s - Qt %s - PyQt %s on %s""" % (
  70                 __version__, platform.python_version(),
  71                 QT_VERSION_STR, PYQT_VERSION_STR, platform.system()))
  72 
  73     def help(self):
  74         '''Display index.html file.'''
  75         form = helpform.HelpForm("index.html", self)
  76         form.show()        
  77 
  78     def setDirty(self):
  79         '''On change of text in textEdit window, set the flag
  80         "dirty" to True'''
  81         if self.dirty:
  82             return True        
  83         self.dirty = True
  84         self.updateStatus('self.dirty set to True')
  85         
  86     def clearDirty(self):
  87         '''Clear the dirty.'''
  88         self.dirty = False
  89 
  90     def updateStatus(self, message):
  91         '''Keep status current.'''
  92         if self.fileName is not None:
  93             flbase = os.path.basename(self.fileName)
  94             self.setWindowTitle(unicode("Simple Editor - " + flbase + "[*]") )
  95             self.statusBar().showMessage(message, 5000)
  96             self.setWindowModified(self.dirty)
  97         
  98     def okToContinue(self):
  99         '''Boolean result invocation method.'''
 100         if self.dirty:
 101             reply = QMessageBox.question(self,
 102                     "Simple Editor - Unsaved Changes",
 103                     "Save unsaved changes?",
 104                     QMessageBox.Yes|QMessageBox.No|QMessageBox.Cancel)
 105             if reply == QMessageBox.Cancel:
 106                 return False
 107             elif reply == QMessageBox.Yes:
 108                 return self.fileSave()
 109         return True
 110         
 111     def addActions(self, target, actions):
 112         '''Add actions to tool bars or menus'''
 113         for action in actions:
 114             if action is None:
 115                 target.addSeparator()
 116             else:
 117                 target.addAction(action)
 118 
 119     def editAction(self, action, slot=None, shortcut=None, icon=None,
 120                      tip=None, checkable=False, signal="triggered()"):
 121         '''Add attributes to Action that have not been generated by
 122         the Qt Designer.'''
 123         if icon is not None:
 124             action.setIcon(QIcon(":/{0}.png".format(icon)))
 125         if shortcut is not None:
 126             action.setShortcut(shortcut)
 127         if tip is not None:
 128             action.setToolTip(tip)
 129             action.setStatusTip(tip)
 130         if slot is not None:
 131 #            self.connect(action, SIGNAL(signal), slot)            
 132             action.triggered.connect(slot)                        
 133         if checkable:
 134             action.setCheckable(True)
 135         return action
 136 
 137     def fileNew(self):
 138         '''Clear the editor window for a new file with name
 139         specified in fileSaveAs method.'''
 140         if not self.okToContinue():
 141             return
 142         self.textEdit.setText('')
 143         self.statusBar().showMessage('File menu: New selected', 5000)
 144 
 145     def fileOpen(self):
 146         '''Open file'''
 147         if not self.okToContinue():
 148             return
 149         fname = unicode(QFileDialog.getOpenFileName(self,
 150                         "Open File", '.', "Files (*.*)"))
 151         if not (fname == ""):
 152             self.textEdit.setText(open(fname).read())
 153             self.fileName = fname
 154         else:
 155             return
 156         self.clearDirty()
 157         self.updateStatus('File opened.')
 158         
 159     def fileSave(self):
 160         '''Save file with current name.'''
 161         if self.fileName is None:
 162             return self.fileSaveAs()
 163         else:
 164             if not self.dirty:
 165                 return
 166             fname = self.fileName
 167             fl = open(fname, 'w')
 168             tempText = self.textEdit.toPlainText()
 169             if tempText:                
 170                 fl.write(tempText)
 171                 fl.close()
 172                 self.clearDirty()
 173                 self.updateStatus('Saved file') 
 174                 return True
 175             else:
 176                 self.statusBar().showMessage('Failed to save ...', 5000)
 177                 return False
 178 
 179     def fileSaveAs(self):
 180         '''Save file with a different name and maybe different directory.'''
 181         path = self.fileName if self.fileName is not None else "."
 182         fname = unicode(QFileDialog.getSaveFileName(self,
 183                         "Simple Editor, SaveAs ", path, "Any File (*.*)"))
 184         if fname:
 185             if "." not in fname:
 186                 fname += ".txt"
 187             self.fileName = fname
 188             self.fileSave()        
 189             self.statusBar().showMessage('SaveAs file' + fname, 8000)
 190             self.clearDirty()
 191             
 192 if __name__ == '__main__':
 193     '''Execute this part of program if it is run as mainline.'''
 194     app = QApplication(sys.argv)
 195     frame = MainWindow()
 196     frame.show()
 197     app.exec_()
```
:::
::::

Let me reiterate the recommendation to download the full listing of program from a the tar ball, named \"simple0.1.00.tar.gz\", which is available from [http://akabaila.pcug.org.au/data_sample/](http://akabaila.pcug.org.au/data_sample/) directory. It would be greatly appreciated if you let me know if that worked for you: email akabaila\[at\]pcug\[dot\]org\[dot\]au

The tar ball is meant to have all the required files - the original **simple.ui** file, generated by the **Qt Designer** and saved by us; the **simple.qrc** file, an XML file with list of icons and other resources used by the program, as well as the resources themselves. Also, the automatically generated **ui_simple.py** and **qrc_simple.py** files which are python program files, importable to the project.

As programs go, the above listing is small - less than 200 lines. If you understand it all and could now program it all yourself, then just go and do it - congratulations, you are done with this tutorial! If you feel a little doubtful or curious how it all developed, then let us go to the beginning of it - **Stage 0**, followed by **Stage 1** and so on. I enjoy your company, stay with it!

[Return Home](./PyQt(2f)simple.html)
