# PyQt/Adding items to a list widget

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# Adding items to a list widget 

On the `#pyqt`{.backtick} channel at Freenode, `afief`{.backtick} asked for an example that showed how to add items to a list widget using QListWidgetItem rather than just plain strings.

:::: 
::: 
``` 
   1 import sys
   2 from PyQt4.QtGui import *
   3 
   4 app = QApplication(sys.argv)
   5 
   6 listWidget = QListWidget()
   7 
   8 for i in range(10):
   9     item = QListWidgetItem("Item %i" % i)
  10     listWidget.addItem(item)
  11 
  12 listWidget.show()
  13 sys.exit(app.exec_())
```
:::
::::

Although this example seems easy, there is one subtle point worth noting: the list widget takes ownership of each of the items added to it. This means that you cannot add an item to more than one list widget.
