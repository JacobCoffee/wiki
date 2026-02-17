# PyQt/Making non-clickable widgets clickable

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# Making non-clickable widgets clickable 

On the `#pyqt`{.backtick} channel on Freenode, `xh`{.backtick} asked if it was possible to make QLabel objects clickable without subclassing.

There are two ways to do this:

1.  Use event filters.
2.  Assign new methods to the labels.

These are shown below.

## Event filters 

The following example code shows how to use event filters to do this. It uses one filter object per label, which is created when the `clickable()`{.backtick} function is called with the widget that is to be click-enabled. The function returns a `clicked()`{.backtick} signal that actually belongs to the filter object. The caller can connect this signal to a suitable callable object.

:::: 
::: 
``` 
   1 import sys
   2 from PyQt4.QtCore import *
   3 from PyQt4.QtGui import *
   4 
   5 def clickable(widget):
   6 
   7     class Filter(QObject):
   8     
   9         clicked = pyqtSignal()
  10         
  11         def eventFilter(self, obj, event):
  12         
  13             if obj == widget:
  14                 if event.type() == QEvent.MouseButtonRelease:
  15                     if obj.rect().contains(event.pos()):
  16                         self.clicked.emit()
  17                         # The developer can opt for .emit(obj) to get the object within the slot.
  18                         return True
  19             
  20             return False
  21     
  22     filter = Filter(widget)
  23     widget.installEventFilter(filter)
  24     return filter.clicked
  25 
  26 
  27 class Window(QWidget):
  28 
  29     def __init__(self, parent = None):
  30     
  31         QWidget.__init__(self, parent)
  32         
  33         label1 = QLabel(self.tr("Hello world!"))
  34         label2 = QLabel(self.tr("ABC DEF GHI"))
  35         label3 = QLabel(self.tr("Hello PyQt!"))
  36         
  37         clickable(label1).connect(self.showText1)
  38         clickable(label2).connect(self.showText2)
  39         clickable(label3).connect(self.showText3)
  40         
  41         layout = QHBoxLayout(self)
  42         layout.addWidget(label1)
  43         layout.addWidget(label2)
  44         layout.addWidget(label3)
  45     
  46     def showText1(self):
  47         print "Label 1 clicked"
  48     
  49     def showText2(self):
  50         print "Label 2 clicked"
  51     
  52     def showText3(self):
  53         print "Label 3 clicked"
  54 
  55 
  56 if __name__ == "__main__":
  57 
  58     app = QApplication(sys.argv)
  59     window = Window()
  60     window.show()
  61     sys.exit(app.exec_())
```
:::
::::

## Assigning new methods 

As `xh`{.backtick} pointed out, it should be possible to assign new event handler methods to instances of QLabel, and this should work as long as the labels were created in Python:

:::: 
::: 
``` 
   1 import sys
   2 from PyQt4.QtGui import *
   3 
   4 class Window(QWidget):
   5 
   6     def __init__(self, parent = None):
   7     
   8         QWidget.__init__(self, parent)
   9         
  10         label1 = QLabel(self.tr("Hello world!"))
  11         label2 = QLabel(self.tr("ABC DEF GHI"))
  12         label3 = QLabel(self.tr("Hello PyQt!"))
  13         
  14         label1.mouseReleaseEvent = self.showText1
  15         label2.mouseReleaseEvent = self.showText2
  16         label3.mouseReleaseEvent = self.showText3
  17         
  18         layout = QHBoxLayout(self)
  19         layout.addWidget(label1)
  20         layout.addWidget(label2)
  21         layout.addWidget(label3)
  22     
  23     def showText1(self, event):
  24         print "Label 1 clicked"
  25     
  26     def showText2(self, event):
  27         print "Label 2 clicked"
  28     
  29     def showText3(self, event):
  30         print "Label 3 clicked"
  31 
  32 
  33 if __name__ == "__main__":
  34 
  35     app = QApplication(sys.argv)
  36     window = Window()
  37     window.show()
  38     sys.exit(app.exec_())
```
:::
::::
