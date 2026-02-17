# PyQt/Undo and redo with line edits

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# Undo and redo with line edits 

On `comp.lang.python`{.backtick}, Zabin asked for some help with undo/redo and a form interface.

:::: 
::: 
``` 
   1 import sys
   2 
   3 from PyQt4.QtGui import *
   4 
   5 class Form(QWidget):
   6 
   7     def __init__(self, parent = None):
   8     
   9         QWidget.__init__(self, parent)
  10         
  11         self.undoStack = QUndoStack()
  12         
  13         undoAction = self.undoStack.createUndoAction(self, self.tr("&Undo"))
  14         undoAction.setShortcuts(QKeySequence.Undo)
  15         redoAction = self.undoStack.createRedoAction(self, self.tr("&Redo"))
  16         redoAction.setShortcuts(QKeySequence.Redo)
  17         
  18         nameEdit = QLineEdit()
  19         addressEdit = QLineEdit()
  20         
  21         undoButton = QToolButton()
  22         undoButton.setDefaultAction(undoAction)
  23         redoButton = QToolButton()
  24         redoButton.setDefaultAction(redoAction)
  25         
  26         nameEdit.editingFinished.connect(self.storeFieldText)
  27         addressEdit.editingFinished.connect(self.storeFieldText)
  28         
  29         formLayout = QFormLayout()
  30         formLayout.addRow(self.tr("&Name"), nameEdit)
  31         formLayout.addRow(self.tr("&Address"), addressEdit)
  32         
  33         buttonLayout = QVBoxLayout()
  34         buttonLayout.addWidget(undoButton)
  35         buttonLayout.addWidget(redoButton)
  36         
  37         layout = QHBoxLayout(self)
  38         layout.addLayout(formLayout)
  39         layout.addLayout(buttonLayout)
  40         
  41         self.setWindowTitle(self.tr("Undo Example"))
  42     
  43     def storeFieldText(self):
  44     
  45         command = StoreCommand(self.sender())
  46         self.undoStack.push(command)
  47 
  48 
  49 class StoreCommand(QUndoCommand):
  50 
  51     def __init__(self, field):
  52     
  53         QUndoCommand.__init__(self)
  54         
  55         # Record the field that has changed.
  56         self.field = field
  57         
  58         # Record the text at the time the command was created.
  59         self.text = field.text()
  60 
  61     def undo(self):
  62     
  63         # Remove the text from the file and set it in the field.
  64         # ...
  65         self.field.setText(self.text)
  66     
  67     def redo(self):
  68     
  69         # Store the text in the file and set it in the field.
  70         # ...
  71         self.field.setText(self.text)
  72 
  73 
  74 if __name__ == "__main__":
  75 
  76     app = QApplication(sys.argv)
  77     form = Form()
  78     form.show()
  79     sys.exit(app.exec_())
```
:::
::::
