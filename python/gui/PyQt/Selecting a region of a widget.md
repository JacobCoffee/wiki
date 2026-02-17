# PyQt/Selecting a region of a widget

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# Selecting a region of a widget 

On [TheMailingList](./PyQt(2f)TheMailingList.html), Brickle Macho asked for some advice on writing a widget that allows part of the image it is displaying to be selected.

The following code shows how the QRubberBand class is used to perform a selection. The key parts of the code involve the mousePressEvent(), mouseMoveEvent() and mouseReleaseEvent() handlers. These initialise and show, update, and hide the rubber band respectively. Obtaining the geometry of the rubber band and reading the corresponding part of the image are left as exercises for the reader.

:::: 
::: 
``` 
   1 import random, sys
   2 from PyQt4.QtCore import QPoint, QRect, QSize, Qt
   3 from PyQt4.QtGui import *
   4 
   5 class Window(QLabel):
   6 
   7     def __init__(self, parent = None):
   8     
   9         QLabel.__init__(self, parent)
  10         self.rubberBand = QRubberBand(QRubberBand.Rectangle, self)
  11         self.origin = QPoint()
  12     
  13     def mousePressEvent(self, event):
  14     
  15         if event.button() == Qt.LeftButton:
  16         
  17             self.origin = QPoint(event.pos())
  18             self.rubberBand.setGeometry(QRect(self.origin, QSize()))
  19             self.rubberBand.show()
  20     
  21     def mouseMoveEvent(self, event):
  22     
  23         if not self.origin.isNull():
  24             self.rubberBand.setGeometry(QRect(self.origin, event.pos()).normalized())
  25     
  26     def mouseReleaseEvent(self, event):
  27     
  28         if event.button() == Qt.LeftButton:
  29             self.rubberBand.hide()
  30 
  31 
  32 def create_pixmap():
  33 
  34     def color():
  35         r = random.randrange(0, 255)
  36         g = random.randrange(0, 255)
  37         b = random.randrange(0, 255)
  38         return QColor(r, g, b)
  39     
  40     def point():
  41         return QPoint(random.randrange(0, 400), random.randrange(0, 300))
  42     
  43     pixmap = QPixmap(400, 300)
  44     pixmap.fill(color())
  45     painter = QPainter()
  46     painter.begin(pixmap)
  47     i = 0
  48     while i < 1000:
  49         painter.setBrush(color())
  50         painter.drawPolygon(QPolygon([point(), point(), point()]))
  51         i += 1
  52     
  53     painter.end()
  54     return pixmap
  55 
  56 
  57 if __name__ == "__main__":
  58 
  59     app = QApplication(sys.argv)
  60     random.seed()
  61     
  62     window = Window()
  63     window.setPixmap(create_pixmap())
  64     window.resize(400, 300)
  65     window.show()
  66     
  67     sys.exit(app.exec_())
```
:::
::::
