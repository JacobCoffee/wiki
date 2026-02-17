# PyQt/Using a translation of Qt

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# Using a translation of Qt 

On the `#pyqt`{.backtick} channel on [freenode](http://freenode.net), `Fisiu`{.backtick} asked about getting localized versions of the Qt dialogs.

:::: 
::: 
``` 
   1 import sys
   2 from PyQt4.QtCore import *
   3 from PyQt4.QtGui import *
   4 
   5 if __name__ == "__main__":
   6 
   7     app = QApplication(sys.argv)
   8     
   9     qt_translator = QTranslator()
  10     qt_translator.load("qt_" + QLocale.system().name(),
  11                        QLibraryInfo.location(QLibraryInfo.TranslationsPath))
  12     app.installTranslator(qt_translator)
  13     
  14     QMessageBox.aboutQt(None)
  15     sys.exit()
```
:::
::::
