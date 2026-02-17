# PyQt/GraphicsView_-_SimpleAnimation

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# Graphics View - Simple Animation 

The example below presents how to use QGraphicsView along with QGraphicsItem, QGraphicsItemAnimation and QTimeLine to construct a very simple animation. If you have any questions please do not hesitate to ask me directly.

:::: 
::: 
``` 
   1 # simple code by Krystian Samp - krychu (samp[dot]krystian[monkey]gmail.com), November 2006
   2 
   3 import sys
   4 from PyQt4 import QtGui, QtCore
   5 
   6 class MyView(QtGui.QGraphicsView):
   7     def __init__(self):
   8         QtGui.QGraphicsView.__init__(self)
   9 
  10         self.scene = QtGui.QGraphicsScene(self)
  11         self.item = QtGui.QGraphicsEllipseItem(-20, -10, 40, 20)
  12         self.scene.addItem(self.item)
  13         self.setScene(self.scene)
  14 
  15         # Remember to hold the references to QTimeLine and QGraphicsItemAnimation instances.
  16         # They are not kept anywhere, even if you invoke QTimeLine.start().
  17         self.tl = QtCore.QTimeLine(1000)
  18         self.tl.setFrameRange(0, 100)
  19         self.a = QtGui.QGraphicsItemAnimation()
  20         self.a.setItem(self.item)
  21         self.a.setTimeLine(self.tl)
  22 
  23         # Each method determining an animation state (e.g. setPosAt, setRotationAt etc.)
  24         # takes as a first argument a step which is a value between 0 (the beginning of the
  25         # animation) and 1 (the end of the animation)
  26         self.a.setPosAt(0, QtCore.QPointF(0, -10))
  27         self.a.setRotationAt(1, 360)
  28 
  29         self.tl.start()
  30 
  31 if __name__ == '__main__':
  32     app = QtGui.QApplication(sys.argv)
  33     view = MyView()
  34     view.show()
  35     sys.exit(app.exec_())
```
:::
::::

![ani.gif](attachments/PyQt(2f)GraphicsView_(2d)_SimpleAnimation/ani.gif "ani.gif") (WinXP, Py2.6, [PyQt4](PyQt4).4.4)
