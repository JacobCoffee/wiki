# PyQt/Creating a widget with a fixed aspect ratio

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# Creating a widget with a fixed aspect ratio 

On the `#pyqt`{.backtick} channel on [Freenode](http://freenode.net), `magicblaze007`{.backtick} asked for an example of a custom widget with a fixed aspect ratio.

One place to look for information is the Qt Quarterly article, [Trading Height for Width](http://doc.qt.digia.com/qq/qq04-height-for-width.html) which shows how this is done using C++ and Qt 3.

Another example is shown here.

:::: 
::: 
``` 
   1 import sys
   2 from PyQt4.QtCore import pyqtSignal, QSize, Qt
   3 from PyQt4.QtGui import *
   4 
   5 class MyWidget(QWidget):
   6 
   7     clicked = pyqtSignal()
   8     keyPressed = pyqtSignal(unicode)
   9     
  10     def __init__(self, parent = None):
  11     
  12         QWidget.__init__(self, parent)
  13         self.color = QColor(0, 0, 0)
  14         sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
  15         sizePolicy.setHeightForWidth(True)
  16         self.setSizePolicy(sizePolicy)
  17     
  18     def paintEvent(self, event):
  19     
  20         painter = QPainter()
  21         painter.begin(self)
  22         painter.fillRect(event.rect(), QBrush(self.color))
  23         painter.end()
  24     
  25     def keyPressEvent(self, event):
  26     
  27         self.keyPressed.emit(event.text())
  28         event.accept()
  29     
  30     def mousePressEvent(self, event):
  31     
  32         self.setFocus(Qt.OtherFocusReason)
  33         event.accept()
  34     
  35     def mouseReleaseEvent(self, event):
  36     
  37         if event.button() == Qt.LeftButton:
  38         
  39             self.color = QColor(self.color.green(), self.color.blue(),
  40                                 127 - self.color.red())
  41             self.update()
  42             self.clicked.emit()
  43             event.accept()
  44     
  45     def sizeHint(self):
  46     
  47         return QSize(400, 600)
  48     
  49     def heightForWidth(self, width):
  50     
  51         return width * 1.5
  52 
  53 
  54 if __name__ == "__main__":
  55 
  56     app = QApplication(sys.argv)
  57     window = QWidget()
  58     
  59     mywidget = MyWidget()
  60     label = QLabel()
  61     
  62     mywidget.clicked.connect(label.clear)
  63     mywidget.keyPressed.connect(label.setText)
  64     
  65     layout = QVBoxLayout()
  66     layout.addWidget(mywidget, 0, Qt.AlignCenter)
  67     layout.addWidget(label)
  68     window.setLayout(layout)
  69     
  70     window.show()
  71     sys.exit(app.exec_())
```
:::
::::
