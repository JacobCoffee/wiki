# PyQt/Adding custom signals to a simple painted widget

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# Adding custom signals to a simple painted widget 

On the `#pyqt`{.backtick} channel on [freenode](http://freenode.net), `magicblaze007`{.backtick} asked for an example that showed how to declare and use custom signals.

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
  14     
  15     def paintEvent(self, event):
  16     
  17         painter = QPainter()
  18         painter.begin(self)
  19         painter.fillRect(event.rect(), QBrush(self.color))
  20         painter.end()
  21     
  22     def keyPressEvent(self, event):
  23     
  24         self.keyPressed.emit(event.text())
  25         event.accept()
  26     
  27     def mousePressEvent(self, event):
  28     
  29         self.setFocus(Qt.OtherFocusReason)
  30         event.accept()
  31     
  32     def mouseReleaseEvent(self, event):
  33     
  34         if event.button() == Qt.LeftButton:
  35         
  36             self.color = QColor(self.color.green(), self.color.blue(),
  37                                 127 - self.color.red())
  38             self.update()
  39             self.clicked.emit()
  40             event.accept()
  41     
  42     def sizeHint(self):
  43     
  44         return QSize(100, 100)
  45 
  46 
  47 if __name__ == "__main__":
  48 
  49     app = QApplication(sys.argv)
  50     window = QWidget()
  51     
  52     mywidget = MyWidget()
  53     label = QLabel()
  54     
  55     mywidget.clicked.connect(label.clear)
  56     mywidget.keyPressed.connect(label.setText)
  57     
  58     layout = QVBoxLayout()
  59     layout.addWidget(mywidget)
  60     layout.addWidget(label)
  61     window.setLayout(layout)
  62     
  63     window.show()
  64     sys.exit(app.exec_())
```
:::
::::
