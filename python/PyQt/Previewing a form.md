# PyQt/Previewing a form

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# Previewing a form 

On the `#pyqt`{.backtick} channel on [Freenode](http://freenode.net), `a_l_e`{.backtick} asked for a way to preview a main window form created in Qt Designer.

:::: 
::: 
``` 
   1 import sys
   2 
   3 from PyQt4.QtGui import QApplication
   4 from PyQt4.uic import loadUi
   5 
   6 if __name__ == "__main__":
   7 
   8     app = QApplication(sys.argv)
   9     
  10     if len(app.arguments()) != 2:
  11     
  12         sys.stderr.write("Usage: %s <ui file>\n" % app.arguments()[0])
  13         sys.exit()
  14     
  15     window = loadUi(app.arguments()[1])
  16     window.show()
  17     sys.exit(app.exec_())
```
:::
::::
