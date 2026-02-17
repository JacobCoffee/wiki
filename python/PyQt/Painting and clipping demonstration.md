# PyQt/Painting and clipping demonstration

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# Painting and clipping demonstration 

This example was created to explore issues with clipping mentioned in [this message](http://lists.trolltech.com/pipermail/qt-interest/2009-September/012599.html) to the [qt-interest mailing list](http://lists.trolltech.com/mailman/listinfo/qt-interest).

![clipper.png](attachments/PyQt(2f)Painting(20)and(20)clipping(20)demonstration/clipper.png "clipper.png")

The first version ([clipper.py](attachments/PyQt(2f)Painting(20)and(20)clipping(20)demonstration/clipper.py)) uses QPainter\'s `setClipRect()`{.backtick} method to clip painting outside a given rectangle.

:::: 
::: 
``` 
   1 import sys
   2 from PyQt4.QtCore import *
   3 from PyQt4.QtGui import *
   4 
   5 class Window(QWidget):
   6 
   7     def __init__(self):
   8     
   9         QWidget.__init__(self)
  10         self.largest_rect = QRect(50, 50, 400, 400)
  11         
  12         self.clip_rect = QRect(50, 50, 400, 400)
  13         self.dragging = None
  14         self.drag_offset = QPoint()
  15         self.handle_offsets = (
  16             QPoint(8, 8), QPoint(-1, 8), QPoint(8, -1), QPoint(-1, -1)
  17             )
  18         
  19         self.path = QPainterPath()
  20         self.path.moveTo(100, 250)
  21         font = QFont()
  22         font.setPixelSize(80)
  23         self.path.addText(100, 300, font, "Clipping")
  24         
  25         self.polygon = QPolygon([QPoint(250, 100), QPoint(400, 250),
  26                                  QPoint(250, 400), QPoint(100, 250),
  27                                  QPoint(250, 100)])
  28     
  29     def paintEvent(self, event):
  30     
  31         painter = QPainter()
  32         painter.begin(self)
  33         painter.fillRect(event.rect(), QBrush(Qt.white))
  34         painter.setRenderHint(QPainter.Antialiasing)
  35         painter.setPen(QPen(QBrush(Qt.red), 1, Qt.DashLine))
  36         painter.drawRect(self.largest_rect)
  37         painter.setPen(QPen(Qt.black))
  38         painter.drawRect(self.clip_rect)
  39         for i in range(4):
  40             painter.drawRect(self.corner(i))
  41         
  42         painter.setClipRect(self.clip_rect)
  43         painter.drawPolyline(self.polygon)
  44         painter.setBrush(QBrush(Qt.blue))
  45         painter.drawPath(self.path)
  46         painter.end()
  47     
  48     def corner(self, number):
  49     
  50         if number == 0:
  51             return QRect(self.clip_rect.topLeft() - self.handle_offsets[0], QSize(8, 8))
  52         elif number == 1:
  53             return QRect(self.clip_rect.topRight() - self.handle_offsets[1], QSize(8, 8))
  54         elif number == 2:
  55             return QRect(self.clip_rect.bottomLeft() - self.handle_offsets[2], QSize(8, 8))
  56         elif number == 3:
  57             return QRect(self.clip_rect.bottomRight() - self.handle_offsets[3], QSize(8, 8))
  58     
  59     def mousePressEvent(self, event):
  60     
  61         for i in range(4):
  62             rect = self.corner(i)
  63             if rect.contains(event.pos()):
  64                 self.dragging = i
  65                 self.drag_offset = rect.topLeft() - event.pos()
  66                 break
  67         else:
  68             self.dragging = None
  69     
  70     def mouseMoveEvent(self, event):
  71     
  72         if self.dragging is None:
  73             return
  74         
  75         left = self.largest_rect.left()
  76         right = self.largest_rect.right()
  77         top = self.largest_rect.top()
  78         bottom = self.largest_rect.bottom()
  79         
  80         point = event.pos() + self.drag_offset + self.handle_offsets[self.dragging]
  81         point.setX(max(left, min(point.x(), right)))
  82         point.setY(max(top, min(point.y(), bottom)))
  83         
  84         if self.dragging == 0:
  85             self.clip_rect.setTopLeft(point)
  86         elif self.dragging == 1:
  87             self.clip_rect.setTopRight(point)
  88         elif self.dragging == 2:
  89             self.clip_rect.setBottomLeft(point)
  90         elif self.dragging == 3:
  91             self.clip_rect.setBottomRight(point)
  92         
  93         self.update()
  94     
  95     def mouseReleaseEvent(self, event):
  96     
  97         self.dragging = None
  98     
  99     def sizeHint(self):
 100         return QSize(500, 500)
 101 
 102 
 103 if __name__ == "__main__":
 104 
 105     app = QApplication(sys.argv)
 106     window = Window()
 107     window.show()
 108     sys.exit(app.exec_())
```
:::
::::

The second version ([clipper_path.py](attachments/PyQt(2f)Painting(20)and(20)clipping(20)demonstration/clipper_path.py)) shows how the same effect can be achieved by using QPainterPath\'s `intersected()`{.backtick} method. Here, we show how the `paintEvent()`{.backtick} method of the example has been modified:

:::: 
::: 
``` 
   1     def paintEvent(self, event):
   2     
   3         painter = QPainter()
   4         painter.begin(self)
   5         painter.fillRect(event.rect(), QBrush(Qt.white))
   6         painter.setRenderHint(QPainter.Antialiasing)
   7         painter.setPen(QPen(QBrush(Qt.red), 1, Qt.DashLine))
   8         painter.drawRect(self.largest_rect)
   9         painter.setPen(QPen(Qt.black))
  10         painter.drawRect(self.clip_rect)
  11         for i in range(4):
  12             painter.drawRect(self.corner(i))
  13         
  14         path = QPainterPath()
  15         path.addRect(QRectF(self.clip_rect))
  16         polygon_path = QPainterPath()
  17         polygon_path.addPolygon(QPolygonF(self.polygon))
  18         painter.drawPath(path.intersected(polygon_path))
  19         painter.setBrush(QBrush(Qt.blue))
  20         painter.drawPath(path.intersected(self.path))
  21         painter.end()
```
:::
::::
