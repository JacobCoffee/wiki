# PyQt/Distinguishing between click and double click

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# Distinguishing between click and double click 

In a [PyQt QCalendarWidget events question](http://mail.python.org/pipermail/python-list/2012-July/626779.html) thread on the python-list mailing list, *tinnews* asked for a way to distinguish between single and double clicks on a calendar widget. This problem is more generally handled for a widget using timers in the following code:

:::: 
::: 
``` 
   1 import sys
   2 
   3 from PyQt4.QtCore import *
   4 from PyQt4.QtGui import *
   5 
   6 class Widget(QWidget):
   7 
   8     def __init__(self, parent = None):
   9     
  10         QWidget.__init__(self, parent)
  11         self.message = ""
  12     
  13     def paintEvent(self, event):
  14     
  15         painter = QPainter()
  16         painter.begin(self)
  17         painter.fillRect(event.rect(), QBrush(Qt.white))
  18         painter.drawText(self.rect(), Qt.AlignCenter, self.message)
  19         painter.end()
  20     
  21     def mousePressEvent(self, event):
  22     
  23         self.last = "Click"
  24     
  25     def mouseReleaseEvent(self, event):
  26     
  27         if self.last == "Click":
  28             QTimer.singleShot(QApplication.instance().doubleClickInterval(),
  29                               self.performSingleClickAction)
  30         else:
  31             # Perform double click action.
  32             self.message = "Double Click"
  33             self.update()
  34     
  35     def mouseDoubleClickEvent(self, event):
  36     
  37         self.last = "Double Click"
  38     
  39     def performSingleClickAction(self):
  40     
  41         if self.last == "Click":
  42             self.message = "Click"
  43             self.update()
  44 
  45 
  46 if __name__ == "__main__":
  47 
  48     app = QApplication(sys.argv)
  49     window = Widget()
  50     window.resize(400, 400)
  51     window.show()
  52     sys.exit(app.exec_())
```
:::
::::

The trick is to realise that Qt delivers MousePress, MouseRelease, MouseDoubleClick and MouseRelease events in that order to the widget. A click is typically recognised as occurring on the first MouseRelease, but we need to wait until a possible MouseDoubleClick event occurs before acting on it. If no second MousePress occurs, we can act on the single click.

However, if a second mouse press occurs, the mouseDoubleClickEvent() handler will be called. The application author can choose to perform an action immediately or wait for the next MouseRelease event. In any case, the mouseReleaseEvent() handler will need to know whether a single or double click has occurred.

To handle this, we set an attribute in the mousePressEvent() handler to indicate that a click has occurred. In the mouseReleaseEvent() handler we start a timer that will time out after the system-determined delay for a second mouse press has elapsed. If no second press occurs within that time, the performSingleClickAction() method will be called and we can check that only a single click occurred.

However, if a second press occurs within that time, the mouseDoubleClickEvent() handler will be called first, and we can set an attribute to indicate that a double click is in progress. The performSingleClickAction() method will be called anyway, so there is a check in that method to ensure that we only perform the single click action if the last mouse press was for a single click. Note that we only start a timer in the mouseReleaseEvent() handler after the first click since we handle the double click case directly in the handler method itself.
