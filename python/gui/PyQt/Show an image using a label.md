# PyQt/Show an image using a label

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# Show an image using a label 

On the `#pyqt`{.backtick} IRC channel on Freenode, `elhobab`{.backtick} asked how to show an image.

:::: 
::: 
``` 
   1 import sys
   2 from PyQt4.QtGui import *
   3 
   4 app = QApplication(sys.argv)
   5 
   6 label = QLabel()
   7 pixmap = QPixmap(sys.argv[1])
   8 label.setPixmap(pixmap)
   9 label.show()
  10 
  11 sys.exit(app.exec_())
```
:::
::::
