# PyQt/Adding auto-completion to a QLineEdit

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# Adding auto-completion to a QLineEdit 

On the `#pyqt`{.backtick} IRC channel on [Freenode](http://www.freenode.net), `filip`{.backtick} asked how to add auto-completion in a QLineEdit widget.

The following code shows how to use a QStringListModel to supply data to a QCompleter, itself used by a QLineEdit.

:::: 
::: 
``` 
   1 import sys
   2 from PyQt4.QtCore import Qt
   3 from PyQt4.QtGui import QApplication, QCompleter, QLineEdit, QStringListModel
   4 
   5 def get_data(model):
   6     model.setStringList(["completion", "data", "goes", "here"])
   7 
   8 if __name__ == "__main__":
   9 
  10     app = QApplication(sys.argv)
  11     edit = QLineEdit()
  12     completer = QCompleter()
  13     edit.setCompleter(completer)
  14 
  15     model = QStringListModel()
  16     completer.setModel(model)
  17     get_data(model)
  18 
  19     edit.show()
  20     sys.exit(app.exec_())
```
:::
::::

Note that, in a real application, you either need to keep a reference to the model or give it a QObject parent. Keeping a reference to the model enables you to update it with new data as required.
