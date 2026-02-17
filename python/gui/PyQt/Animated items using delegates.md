# PyQt/Animated items using delegates

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# Animated items using delegates 

A nasty hack involving a custom delegate, timer events and a signal to inform a view that it needs to repaint itself. It is just a proof of concept.

Perhaps a better example might be [Animated items using delegates and movies](Animated items using delegates and movies).

Things that are wrong with this code:

- It starts a timer and never stops it.
- The signal in the delegate is connected to the viewport of the view instead of the view itself (it doesn\'t work otherwise).
- The delegate simply shifts the normal content of the waiting items and paints a pixmap - it doesn\'t try to replace or add an icon to existing items.

:::: 
::: 
``` 
   1 import sys
   2 from PyQt4.QtCore import pyqtSignal, Qt, QVariant
   3 from PyQt4.QtGui import *
   4 
   5 # Icons used for animation:
   6 _icon0_xpm = [
   7     "16 16 4 1",
   8     ".  c None",
   9     "s  c #cccc00",
  10     "x  c #ffffff",
  11     "   c #000000",
  12     "................",
  13     ".              .",
  14     ". xxxxxxxxxxxx .",
  15     ". x          x .",
  16     ".. x ssssss x ..",
  17     "... x ssss x ...",
  18     ".... x ss x ....",
  19     "..... x  x .....",
  20     "..... x  x .....",
  21     ".... x    x ....",
  22     "... x      x ...",
  23     ".. x        x ..",
  24     ". x          x .",
  25     ". xxxxxxxxxxxx .",
  26     ".              .",
  27     "................"]
  28 
  29 _icon1_xpm = [
  30     "16 16 4 1",
  31     ".  c None",
  32     "s  c #cccc00",
  33     "x  c #ffffff",
  34     "   c #000000",
  35     "................",
  36     ".              .",
  37     ". xxxxxxxxxxxx .",
  38     ". x          x .",
  39     ".. x s    s x ..",
  40     "... x ssss x ...",
  41     ".... x ss x ....",
  42     "..... x  x .....",
  43     "..... x  x .....",
  44     ".... x ss x ....",
  45     "... x  ss  x ...",
  46     ".. x        x ..",
  47     ". x          x .",
  48     ". xxxxxxxxxxxx .",
  49     ".              .",
  50     "................"]
  51 
  52 _icon2_xpm = [
  53     "16 16 4 1",
  54     ".  c None",
  55     "s  c #cccc00",
  56     "x  c #ffffff",
  57     "   c #000000",
  58     "................",
  59     ".              .",
  60     ". xxxxxxxxxxxx .",
  61     ". x          x .",
  62     ".. x        x ..",
  63     "... x ssss x ...",
  64     ".... x ss x ....",
  65     "..... x  x .....",
  66     "..... x  x .....",
  67     ".... x ss x ....",
  68     "... x  ss  x ...",
  69     ".. x   ss   x ..",
  70     ". x          x .",
  71     ". xxxxxxxxxxxx .",
  72     ".              .",
  73     "................"]
  74 
  75 _icon3_xpm = [
  76     "16 16 4 1",
  77     ".  c None",
  78     "s  c #cccc00",
  79     "x  c #ffffff",
  80     "   c #000000",
  81     "................",
  82     ".              .",
  83     ". xxxxxxxxxxxx .",
  84     ". x          x .",
  85     ".. x        x ..",
  86     "... x      x ...",
  87     ".... x    x ....",
  88     "..... x  x .....",
  89     "..... x  x .....",
  90     ".... x ss x ....",
  91     "... x ssss x ...",
  92     ".. x ssssss x ..",
  93     ". x          x .",
  94     ". xxxxxxxxxxxx .",
  95     ".              .",
  96     "................"]
  97 
  98 
  99 class Delegate(QItemDelegate):
 100 
 101     needsRedraw = pyqtSignal()
 102     
 103     def __init__(self, parent = None):
 104     
 105         QItemDelegate.__init__(self, parent)
 106         self.current = 0
 107         self.timerId = self.startTimer(250)
 108         self.model = QStandardItemModel()
 109         self.pixmaps = (QPixmap(_icon0_xpm),
 110                         QPixmap(_icon1_xpm),
 111                         QPixmap(_icon2_xpm),
 112                         QPixmap(_icon3_xpm))
 113     
 114     def timerEvent(self, event):
 115     
 116         if event.timerId() == self.timerId:
 117             self.current = (self.current + 1) % 4
 118             self.needsRedraw.emit()
 119     
 120     def paint(self, painter, option, index):
 121     
 122         waiting = index.data(Qt.UserRole).toBool()
 123         if waiting:
 124             option = option.__class__(option)
 125             painter.drawPixmap(option.rect.topLeft(), self.pixmaps[self.current])
 126             option.rect = option.rect.translated(20, 0)
 127         
 128         QItemDelegate.paint(self, painter, option, index)
 129 
 130 
 131 app = QApplication(sys.argv)
 132 view = QListView()
 133 model = QStandardItemModel()
 134 waiting = True
 135 
 136 for i in range(5):
 137 
 138     item = QStandardItem("Test %i" % i)
 139     item.setData(QVariant(waiting), Qt.UserRole)
 140     waiting = not waiting
 141     model.appendRow(item)
 142 
 143 view.setModel(model)
 144 
 145 delegate = Delegate()
 146 view.setItemDelegate(delegate)
 147 delegate.needsRedraw.connect(view.viewport().update)
 148 
 149 view.show()
 150 sys.exit(app.exec_())
```
:::
::::
