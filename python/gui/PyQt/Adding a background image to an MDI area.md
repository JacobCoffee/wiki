# PyQt/Adding a background image to an MDI area

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# Adding a background image to an MDI area 

On [TheMailingList](TheMailingList), Sarah Mount asked [whether it was possible to display a non-tiled image](http://www.riverbankcomputing.com/pipermail/pyqt/2011-April/029653.html) in the background of an MDI area widget.

The following code uses the same technique that the `qtconfig`{.backtick} tool uses to place a message in the background of its preview widget. In this example, setting the `centered`{.backtick} attribute causes the image to be displayed in the centre of the background area; if unset, the image is scaled to fill the background area.

[mdiarea_pixmap.py](attachments/PyQt(2f)Adding(20)a(20)background(20)image(20)to(20)an(20)MDI(20)area/mdiarea_pixmap.py)

:::: 
::: 
``` 
   1 import sys
   2 from PyQt4.QtCore import Qt
   3 from PyQt4.QtGui import *
   4 
   5 class MDIArea(QMdiArea):
   6 
   7     def __init__(self, background_pixmap, parent = None):
   8     
   9         QMdiArea.__init__(self, parent)
  10         self.background_pixmap = background_pixmap
  11         self.centered = False
  12     
  13     def paintEvent(self, event):
  14     
  15         painter = QPainter()
  16         painter.begin(self.viewport())
  17         
  18         if not self.centered:
  19             painter.drawPixmap(0, 0, self.width(), self.height(), self.background_pixmap)
  20         else:
  21             painter.fillRect(event.rect(), self.palette().color(QPalette.Window))
  22             x = (self.width() - self.display_pixmap.width())/2
  23             y = (self.height() - self.display_pixmap.height())/2
  24             painter.drawPixmap(x, y, self.display_pixmap)
  25         
  26         painter.end()
  27     
  28     def resizeEvent(self, event):
  29     
  30         self.display_pixmap = self.background_pixmap.scaled(event.size(), Qt.KeepAspectRatio)
  31 
  32 
  33 if __name__ == "__main__":
  34 
  35     app = QApplication(sys.argv)
  36     
  37     if len(app.arguments()) != 2:
  38     
  39         sys.stderr.write("Usage: %s <image path>\n" % sys.argv[0])
  40         sys.exit(1)
  41     
  42     m = MDIArea(QPixmap(sys.argv[1]))
  43     m.centered = True
  44     m.show()
  45     sys.exit(app.exec_())
```
:::
::::
