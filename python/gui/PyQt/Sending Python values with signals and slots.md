# PyQt/Sending Python values with signals and slots

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# Sending Python values with signals and slots 

On the `#pyqt`{.backtick} channel on Freenode, `Khertan`{.backtick} asked about sending Python values via Qt\'s signals and slots mechanism.

The following example uses the `PyQt_PyObject`{.backtick} value declaration with an old-style signal-slot connection, and again when the signal is emitted, to communicate a Python dictionary.

**Note:** The comments about new style connections in the code are incorrect.

:::: 
::: 
``` 
   1 import sys
   2 from PyQt4.QtCore import *
   3 from PyQt4.QtGui import *
   4 
   5 class Window(QWidget):
   6 
   7     def __init__(self, parent = None):
   8     
   9         QWidget.__init__(self, parent)
  10         
  11         button = QPushButton(self.tr("Click me"))
  12         self.resultLabel = QLabel(self.tr("..."))
  13         
  14         # New style: uses the connect method of a pyqtSignal object.
  15         self.connect(button, SIGNAL("clicked()"), self.handleClick)
  16         
  17         # Old style: uses the SIGNAL function to describe the signal.
  18         self.connect(self, SIGNAL("sendValue(PyQt_PyObject)"), self.handleValue)
  19         
  20         layout = QVBoxLayout(self)
  21         layout.addWidget(button)
  22         layout.addWidget(self.resultLabel)
  23     
  24     def handleClick(self):
  25     
  26         # Old style: emits the signal using the SIGNAL function.
  27         self.emit(SIGNAL("sendValue(PyQt_PyObject)"), {"abc": 123})
  28     
  29     def handleValue(self, value):
  30     
  31         self.resultLabel.setText(repr(value))
  32 
  33 
  34 if __name__ == "__main__":
  35 
  36     app = QApplication(sys.argv)
  37     window = Window()
  38     window.show()
  39     sys.exit(app.exec_())
```
:::
::::
