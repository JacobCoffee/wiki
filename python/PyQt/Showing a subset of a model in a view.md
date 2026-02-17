# PyQt/Showing a subset of a model in a view

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# Showing a subset of a model in a view 

On the `pyqt`{.backtick} channel on [freenode](http://www.freenode.net), `frankRojas`{.backtick} asked for a way to show child items from a tree view in a table view.

This code uses the selection model of a tree view to discover when items are selected, then it creates a new model to contain the data for the children of the top-level item and displays it in the table view.

Another way to do this would be to use a proxy model.

:::: 
::: 
``` 
   1 import sys
   2 from PyQt4.QtCore import *
   3 from PyQt4.QtGui import *
   4 
   5 tree_data = [
   6     ("Alice", [
   7         ("Keys", []),
   8         ("Purse", [
   9             ("Cellphone", [])
  10             ])
  11         ]),
  12     ("Bob", [
  13         ("Wallet", [
  14             ("Credit card", []),
  15             ("Money", [])
  16             ])
  17         ])
  18     ]
  19 
  20 class Window(QWidget):
  21 
  22     def __init__(self):
  23     
  24         QWidget.__init__(self)
  25         
  26         self.treeView = QTreeView()
  27         self.tableView = QTableView()
  28         self.tableView.horizontalHeader().setStretchLastSection(True)
  29         
  30         self.model = QStandardItemModel()
  31         self.addTreeItems(self.model, tree_data)
  32         self.treeView.setModel(self.model)
  33         
  34         treeSelectionModel = self.treeView.selectionModel()
  35         treeSelectionModel.selectionChanged.connect(self.addTableItems)
  36         
  37         layout = QHBoxLayout(self)
  38         layout.addWidget(self.treeView)
  39         layout.addWidget(self.tableView)
  40     
  41     def addTreeItems(self, parent, elements):
  42     
  43         for text, children in elements:
  44             item = QStandardItem(text)
  45             parent.appendRow(item)
  46             if children:
  47                 self.addTreeItems(item, children)
  48     
  49     def addTableItems(self, selected, deselected):
  50     
  51         # Find the top-level item in the tree.
  52         treeIndex = selected.indexes()[0]
  53         
  54         parent = treeIndex.parent()
  55         while parent.isValid():
  56             treeIndex = parent
  57             parent = parent.parent()
  58         
  59         # treeIndex is now a model index corresponding to a top-level item
  60         
  61         self.tableModel = QStandardItemModel()
  62         
  63         for row in range(self.model.rowCount(treeIndex)):
  64             items = []
  65             for column in range(self.model.columnCount(treeIndex)):
  66                 text = self.model.index(row, column, treeIndex).data().toString()
  67                 items.append(QStandardItem(text))
  68             
  69             self.tableModel.appendRow(items)
  70         
  71         self.tableView.setModel(self.tableModel)
  72 
  73 
  74 if __name__ == "__main__":
  75 
  76     app = QApplication(sys.argv)
  77     window = Window()
  78     window.show()
  79     sys.exit(app.exec_())
```
:::
::::
