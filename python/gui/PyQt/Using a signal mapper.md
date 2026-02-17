# PyQt/Using a signal mapper

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# Using a signal mapper 

On the `#pyqt`{.backtick} channel on Freenode, `lauri`{.backtick} asked about connecting identically-named signals with different parameters from QSignalMapper to slots.

The following example uses old-style signals and slots connections to explicitly specify the signals to be connected to slots in a Python subclass of QWidget.

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
  11         layout = QVBoxLayout(self)
  12         mapper = QSignalMapper(self)
  13         
  14         for i in range(5):
  15         
  16             button = QPushButton()
  17             button.setText("Button " + str(i))
  18             self.connect(button, SIGNAL("clicked()"), mapper, SLOT("map()"))
  19             if i % 2 == 0:
  20                 mapper.setMapping(button, str(i))
  21             else:
  22                 mapper.setMapping(button, i)
  23             layout.addWidget(button)
  24         
  25         self.connect(mapper, SIGNAL("mapped(const QString &)"), self.stringMapped)
  26         self.connect(mapper, SIGNAL("mapped(int)"), self.intMapped)
  27     
  28     def stringMapped(self, value):
  29     
  30         print "stringMapped", value
  31     
  32     def intMapped(self, value):
  33     
  34         print "intMapped", value
  35     
  36 
  37 if __name__ == "__main__":
  38 
  39     app = QApplication(sys.argv)
  40     window = Window()
  41     window.show()
  42     sys.exit(app.exec_())
```
:::
::::
