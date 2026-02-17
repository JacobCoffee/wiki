# PyQt/Fading and unfading a widget with a delay

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# Fading and unfading a widget with a delay 

On the PyQt mailing list, [Tim and Alison Bentley](http://www.riverbankcomputing.com/pipermail/pyqt/2009-November/025007.html) asked for a way to produce a fade-unfade animation.

The following example code uses a single-shot QTimer to schedule the unfade step of the animation for one second after the fade occurs.

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
  11         button = QPushButton(self.tr("Click me!"))
  12         
  13         button.clicked.connect(self.fade)
  14         
  15         layout = QVBoxLayout(self)
  16         layout.addWidget(button)
  17     
  18     def fade(self):
  19     
  20         self.setWindowOpacity(0.5)
  21         QTimer.singleShot(1000, self.unfade)
  22     
  23     def unfade(self):
  24     
  25         self.setWindowOpacity(1)
  26 
  27 
  28 if __name__ == "__main__":
  29 
  30     app = QApplication(sys.argv)
  31     window = Window()
  32     window.show()
  33     sys.exit(app.exec_())
```
:::
::::
