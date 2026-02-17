# PyQt/Windows with gradient backgrounds

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# Windows with gradient backgrounds 

On the #pyqt channel on Freenode, `felipe__`{.backtick} asked if it was possible to change the background colour of a window.

This code shows how it can be done with a fixed gradient. If you are subclassing QWidget or another widget class, it may be worth reimplementing its `resizeEvent()`{.backtick} method to modify the gradient so that it changes when the window is resized.

:::: 
::: 
``` 
   1 import sys
   2 from PyQt4.QtGui import *
   3 
   4 if __name__ == "__main__":
   5 
   6     app = QApplication([])
   7     
   8     w = QWidget()
   9     
  10     p = QPalette()
  11     gradient = QLinearGradient(0, 0, 0, 400)
  12     gradient.setColorAt(0.0, QColor(240, 240, 240))
  13     gradient.setColorAt(1.0, QColor(240, 160, 160))
  14     p.setBrush(QPalette.Window, QBrush(gradient))
  15     w.setPalette(p)
  16     
  17     w.show()
  18     app.exec_()
```
:::
::::
