# PyQt/Exporting a file to other applications

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# Exporting a file to other applications 

On the [mailing list](TheMailingList), Hugo Léveillé asked how to drag data from an application into another that accepts a file drop.

The following example shows one way to do this. Improvements to this code are welcome.

:::: 
::: 
``` 
   1 import sys
   2 from PyQt4.QtCore import QDir, QMimeData, Qt, QTemporaryFile, QUrl
   3 from PyQt4.QtGui import *
   4 
   5 class Window(QLabel):
   6 
   7     def __init__(self, parent = None):
   8 
   9         QLabel.__init__(self, parent)
  10 
  11     def mousePressEvent(self, event):
  12 
  13         if event.button() == Qt.LeftButton:
  14 
  15             drag = QDrag(self)
  16             data = QMimeData()
  17             data.setData("text/plain", str(self.text()))
  18 
  19             path = QDir.tempPath() + "hello.txt"
  20             f = open(path, "w")
  21             f.write("Hello world!")
  22             f.close()
  23             data.setUrls([QUrl.fromLocalFile(path)])
  24             drag.setMimeData(data)
  25             drag.exec_()
  26 
  27 
  28 if __name__ == "__main__":
  29 
  30     app = QApplication(sys.argv)
  31     window = Window()
  32     window.setText("Drag me...")
  33     window.show()
  34 
  35     sys.exit(app.exec_())
```
:::
::::
