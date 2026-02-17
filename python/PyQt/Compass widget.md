# PyQt/Compass widget

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# Compass widget 

On the `#pyqt`{.backtick} channel on [Freenode](http://freenode.net), `epifanio`{.backtick} was creating a compass widget. Although he eventually decided to use Graphics View for this, the following code could be used as the starting point for a simple custom widget with a custom signal and a property for controlling the angle.

![compasswidget.png](attachments/PyQt(2f)Compass(20)widget/compasswidget.png "compasswidget.png")

:::: 
::: 
``` 
   1 import sys
   2 from PyQt4.QtCore import *
   3 from PyQt4.QtGui import *
   4 
   5 class CompassWidget(QWidget):
   6 
   7     angleChanged = pyqtSignal(float)
   8     
   9     def __init__(self, parent = None):
  10     
  11         QWidget.__init__(self, parent)
  12         
  13         self._angle = 0.0
  14         self._margins = 10
  15         self._pointText = {0: "N", 45: "NE", 90: "E", 135: "SE", 180: "S",
  16                            225: "SW", 270: "W", 315: "NW"}
  17     
  18     def paintEvent(self, event):
  19     
  20         painter = QPainter()
  21         painter.begin(self)
  22         painter.setRenderHint(QPainter.Antialiasing)
  23         
  24         painter.fillRect(event.rect(), self.palette().brush(QPalette.Window))
  25         self.drawMarkings(painter)
  26         self.drawNeedle(painter)
  27         
  28         painter.end()
  29     
  30     def drawMarkings(self, painter):
  31     
  32         painter.save()
  33         painter.translate(self.width()/2, self.height()/2)
  34         scale = min((self.width() - self._margins)/120.0,
  35                     (self.height() - self._margins)/120.0)
  36         painter.scale(scale, scale)
  37         
  38         font = QFont(self.font())
  39         font.setPixelSize(10)
  40         metrics = QFontMetricsF(font)
  41         
  42         painter.setFont(font)
  43         painter.setPen(self.palette().color(QPalette.Shadow))
  44         
  45         i = 0
  46         while i < 360:
  47         
  48             if i % 45 == 0:
  49                 painter.drawLine(0, -40, 0, -50)
  50                 painter.drawText(-metrics.width(self._pointText[i])/2.0, -52,
  51                                  self._pointText[i])
  52             else:
  53                 painter.drawLine(0, -45, 0, -50)
  54             
  55             painter.rotate(15)
  56             i += 15
  57         
  58         painter.restore()
  59     
  60     def drawNeedle(self, painter):
  61     
  62         painter.save()
  63         painter.translate(self.width()/2, self.height()/2)
  64         painter.rotate(self._angle)
  65         scale = min((self.width() - self._margins)/120.0,
  66                     (self.height() - self._margins)/120.0)
  67         painter.scale(scale, scale)
  68         
  69         painter.setPen(QPen(Qt.NoPen))
  70         painter.setBrush(self.palette().brush(QPalette.Shadow))
  71         
  72         painter.drawPolygon(
  73             QPolygon([QPoint(-10, 0), QPoint(0, -45), QPoint(10, 0),
  74                       QPoint(0, 45), QPoint(-10, 0)])
  75             )
  76         
  77         painter.setBrush(self.palette().brush(QPalette.Highlight))
  78         
  79         painter.drawPolygon(
  80             QPolygon([QPoint(-5, -25), QPoint(0, -45), QPoint(5, -25),
  81                       QPoint(0, -30), QPoint(-5, -25)])
  82             )
  83         
  84         painter.restore()
  85     
  86     def sizeHint(self):
  87     
  88         return QSize(150, 150)
  89     
  90     def angle(self):
  91         return self._angle
  92     
  93     @pyqtSlot(float)
  94     def setAngle(self, angle):
  95     
  96         if angle != self._angle:
  97             self._angle = angle
  98             self.angleChanged.emit(angle)
  99             self.update()
 100     
 101     angle = pyqtProperty(float, angle, setAngle)
 102 
 103 
 104 if __name__ == "__main__":
 105 
 106     app = QApplication(sys.argv)
 107     
 108     window = QWidget()
 109     compass = CompassWidget()
 110     spinBox = QSpinBox()
 111     spinBox.setRange(0, 359)
 112     spinBox.valueChanged.connect(compass.setAngle)
 113     
 114     layout = QVBoxLayout()
 115     layout.addWidget(compass)
 116     layout.addWidget(spinBox)
 117     window.setLayout(layout)
 118     
 119     window.show()
 120     sys.exit(app.exec_())
```
:::
::::
