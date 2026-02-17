# PyQt/Extend Two QPixmap

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# Extend Two QPixmap 

On the `#pyqt`{.backtick} channel on freenode, iTayb asked if it was possible to merge two QPixmaps into a one QPixmap, side by side. rowinggolfer has answered him:

:::: 
::: 
``` 
   1 '''
   2 combine 2 pixmaps into one.
   3 '''
   4 
   5 from PyQt4 import QtCore, QtGui
   6 
   7 IMAGE1 = "/home/neil/www/openmolar.com/images/om_screenies/client.png"
   8 IMAGE2 = "/home/neil/www/openmolar.com/images/om_screenies/admin_welcome.png"
   9 
  10 app = QtGui.QApplication([])
  11 
  12 pm1 = QtGui.QPixmap(IMAGE1)
  13 pm2 = QtGui.QPixmap(IMAGE2)
  14 
  15 pm = QtGui.QPixmap(400,200)
  16 
  17 label = QtGui.QLabel()
  18 
  19 left_rectF = QtCore.QRectF(0,0,200,200)    #the left half
  20 right_rectF = QtCore.QRectF(200,0,400,200) #the right half
  21 
  22 painter = QtGui.QPainter(pm)
  23 painter.drawPixmap(left_rectF, pm1, QtCore.QRectF(pm1.rect()))
  24 painter.drawPixmap(right_rectF, pm2, QtCore.QRectF(pm2.rect()))
  25 
  26 label.setPixmap(pm)
  27 label.show()
  28 
  29 app.exec_()
```
:::
::::
