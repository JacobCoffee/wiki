# PyQt/Removing a database

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# Removing a database 

On the `#pyqt`{.backtick} channel on [Freenode](http://freenode.net), `munny`{.backtick} asked about removing a database without getting the warning: \"QSqlDatabasePrivate::removeDatabase: connection \'\...\' is still in use, all queries will cease to work.\" or similar.

The following code tries to do this by ensuring that everything that uses the database connection is deleted or set to use different data sources before the connection is removed.

:::: 
::: 
``` 
   1 import sys
   2 from PyQt4.QtGui import *
   3 from PyQt4.QtSql import *
   4 
   5 class Window(QMainWindow):
   6 
   7     def __init__(self, path, parent = None):
   8     
   9         QMainWindow.__init__(self, parent)
  10         
  11         self.path = path
  12         self.db = None
  13         
  14         databaseMenu = self.menuBar().addMenu(self.tr("&Database"))
  15         reloadAction = databaseMenu.addAction(self.tr("&Reload"))
  16         reloadAction.triggered.connect(self.openDatabase)
  17         
  18         self.view = QTableView()
  19         self.openDatabase()
  20         
  21         self.setCentralWidget(self.view)
  22     
  23     def openDatabase(self):
  24     
  25         if self.db:
  26             self.closeDatabase()
  27         
  28         self.db = QSqlDatabase.addDatabase("QSQLITE", "db1")
  29         self.db.setDatabaseName(self.path)
  30         if not self.db.open("", ""):
  31             sys.exit()
  32         
  33         self.model = QSqlTableModel(None, self.db)
  34         self.model.setTable(self.db.tables()[-1])
  35         self.model.select()
  36         
  37         self.view.setModel(self.model)
  38         self.statusBar().showMessage(self.tr("Reloaded"), 1000)
  39     
  40     def closeDatabase(self):
  41 
  42         self.view.setModel(None)
  43         del self.model
  44         self.db.close()
  45         del self.db
  46         QSqlDatabase.removeDatabase("db1")
  47     
  48     def closeEvent(self, event):
  49     
  50         self.closeDatabase()
  51 
  52 
  53 if __name__ == "__main__":
  54 
  55     app = QApplication(sys.argv)
  56     
  57     if len(app.arguments()) != 2:
  58     
  59         sys.stderr.write("Usage: %s <path to SQLITE database\n" % app.arguments()[0])
  60         sys.exit(1)
  61     
  62     window = Window(app.arguments()[1])
  63     window.show()
  64     sys.exit(app.exec_())
```
:::
::::

The `closeDatabase()`{.backtick} method sets a null model on the view, clearing it momentarily, deletes the model, closes the database and deletes the connection. Finally, the database connection can be removed by name using the QSqlDatabase\'s static `removeDatabase()`{.backtick} function.
