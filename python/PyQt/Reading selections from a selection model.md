# PyQt/Reading selections from a selection model

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# Reading selections from a selection model 

On the `#pyqt`{.backtick} channel on freenode, `GHellings`{.backtick} asked for a way to get all selected items in a QListWidget.

The following example, adapted from a code snippet in Qt, shows how to access the selected items in a table via its QItemSelectionModel and update them.

:::: 
::: 
``` 
   1 import sys
   2 from PyQt4.QtCore import QModelIndex
   3 from PyQt4.QtGui import *
   4 
   5 class Window(QMainWindow):
   6 
   7     def __init__(self, parent = None):
   8     
   9         QMainWindow.__init__(self, parent)
  10         
  11         self.model = QStandardItemModel(8, 4)
  12         table = QTableView()
  13         table.setModel(self.model)
  14         
  15         actionMenu = QMenu(self.tr("&Actions"), self)
  16         fillAction = actionMenu.addAction(self.tr("&Fill Selection"))
  17         clearAction = actionMenu.addAction(self.tr("&Clear Selection"))
  18         selectAllAction = actionMenu.addAction(self.tr("&Select All"))
  19         self.menuBar().addMenu(actionMenu)
  20 
  21         fillAction.triggered.connect(self.fillSelection)
  22         clearAction.triggered.connect(self.clearSelection)
  23         selectAllAction.triggered.connect(self.selectAll)
  24         
  25         self.selectionModel = table.selectionModel()
  26 
  27         self.statusBar()
  28         self.setCentralWidget(table)
  29         
  30         self.setWindowTitle(self.tr("Selected Items in a Table Model"))
  31 
  32     def fillSelection(self):
  33     
  34         indexes = self.selectionModel.selectedIndexes()
  35         
  36         for index in indexes:
  37         
  38             text = u"(%i,%i)" % (index.row(), index.column())
  39             self.model.setData(index, text)
  40     
  41     def clearSelection(self):
  42     
  43         indexes = self.selectionModel.selectedIndexes()
  44 
  45         for index in indexes:
  46             self.model.setData(index, "")
  47 
  48     def selectAll(self):
  49     
  50         parent = QModelIndex()
  51         
  52         topLeft = self.model.index(0, 0, parent)
  53         bottomRight = self.model.index(
  54                           self.model.rowCount(parent) - 1,
  55                           self.model.columnCount(parent) - 1, parent)
  56         
  57         selection = QItemSelection(topLeft, bottomRight)
  58         self.selectionModel.select(selection, QItemSelectionModel.Select)
  59 
  60 
  61 if __name__ == "__main__":
  62 
  63     app = QApplication(sys.argv)
  64     window = Window()
  65     window.show()
  66     sys.exit(app.exec_())
```
:::
::::
