# PyQt/A full widget waiting indicator

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# A full widget waiting indicator 

In [this message](http://lists.trolltech.com/pipermail/qt-interest/2009-September/012678.html) on the [qt-interest mailing list](http://lists.trolltech.com/mailman/listinfo/qt-interest), Fabio Dago asked how to create a \"waiting widget\".

This example is adapted from the [Widget Overlay](http://wiki.qtcentre.org/index.php?title=Widget_Overlay) example on the [Qt Centre Wiki](http://wiki.qtcentre.org), adding timer code to animate the indicator.

![wait.png](attachments/PyQt(2f)A(20)full(20)widget(20)waiting(20)indicator/wait.png "wait.png")

:::: 
::: 
``` 
   1 import math, sys
   2 from PyQt4.QtCore import Qt, QTimer
   3 from PyQt4.QtGui import *
   4 
   5 class Overlay(QWidget):
   6 
   7     def __init__(self, parent = None):
   8     
   9         QWidget.__init__(self, parent)
  10         palette = QPalette(self.palette())
  11         palette.setColor(palette.Background, Qt.transparent)
  12         self.setPalette(palette)
  13     
  14     def paintEvent(self, event):
  15     
  16         painter = QPainter()
  17         painter.begin(self)
  18         painter.setRenderHint(QPainter.Antialiasing)
  19         painter.fillRect(event.rect(), QBrush(QColor(255, 255, 255, 127)))
  20         painter.setPen(QPen(Qt.NoPen))
  21         
  22         for i in range(6):
  23             if (self.counter / 5) % 6 == i:
  24                 painter.setBrush(QBrush(QColor(127 + (self.counter % 5)*32, 127, 127)))
  25             else:
  26                 painter.setBrush(QBrush(QColor(127, 127, 127)))
  27             painter.drawEllipse(
  28                 self.width()/2 + 30 * math.cos(2 * math.pi * i / 6.0) - 10,
  29                 self.height()/2 + 30 * math.sin(2 * math.pi * i / 6.0) - 10,
  30                 20, 20)
  31         
  32         painter.end()
  33     
  34     def showEvent(self, event):
  35     
  36         self.timer = self.startTimer(50)
  37         self.counter = 0
  38     
  39     def timerEvent(self, event):
  40     
  41         self.counter += 1
  42         self.update()
  43         if self.counter == 60:
  44             self.killTimer(self.timer)
  45             self.hide()
  46 
  47 
  48 class MainWindow(QMainWindow):
  49 
  50     def __init__(self, parent = None):
  51     
  52         QMainWindow.__init__(self, parent)
  53         
  54         widget = QWidget(self)
  55         self.editor = QTextEdit()
  56         self.editor.setPlainText("0123456789"*100)
  57         layout = QGridLayout(widget)
  58         layout.addWidget(self.editor, 0, 0, 1, 3)
  59         button = QPushButton("Wait")
  60         layout.addWidget(button, 1, 1, 1, 1)
  61         
  62         self.setCentralWidget(widget)
  63         self.overlay = Overlay(self.centralWidget())
  64         self.overlay.hide()
  65         button.clicked.connect(self.overlay.show)
  66     
  67     def resizeEvent(self, event):
  68     
  69         self.overlay.resize(event.size())
  70         event.accept()
  71 
  72 
  73 if __name__ == "__main__":
  74 
  75     app = QApplication(sys.argv)
  76     window = MainWindow()
  77     window.show()
  78     sys.exit(app.exec_())
```
:::
::::
