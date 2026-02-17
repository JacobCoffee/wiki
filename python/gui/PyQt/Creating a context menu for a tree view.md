# PyQt/Creating a context menu for a tree view

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# Creating a context menu for a tree view 

On the `pyqt`{.backtick} channel on [freenode](http://www.freenode.net), `virousa`{.backtick} and `frankRojas`{.backtick} both asked for a way to create a menu for a tree view that showed different entries for items at different depths in the tree.

:::: 
::: 
``` 
   1 import sys
   2 from PyQt4.QtCore import *
   3 from PyQt4.QtGui import *
   4 
   5 data = [
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
  27         self.treeView.setContextMenuPolicy(Qt.CustomContextMenu)
  28         self.treeView.customContextMenuRequested.connect(self.openMenu)
  29         
  30         self.model = QStandardItemModel()
  31         self.addItems(self.model, data)
  32         self.treeView.setModel(self.model)
  33         
  34         self.model.setHorizontalHeaderLabels([self.tr("Object")])
  35         
  36         layout = QVBoxLayout()
  37         layout.addWidget(self.treeView)
  38         self.setLayout(layout)
  39     
  40     def addItems(self, parent, elements):
  41     
  42         for text, children in elements:
  43             item = QStandardItem(text)
  44             parent.appendRow(item)
  45             if children:
  46                 self.addItems(item, children)
  47     
  48     def openMenu(self, position):
  49     
  50         indexes = self.treeView.selectedIndexes()
  51         if len(indexes) > 0:
  52         
  53             level = 0
  54             index = indexes[0]
  55             while index.parent().isValid():
  56                 index = index.parent()
  57                 level += 1
  58         
  59         menu = QMenu()
  60         if level == 0:
  61             menu.addAction(self.tr("Edit person"))
  62         elif level == 1:
  63             menu.addAction(self.tr("Edit object/container"))
  64         elif level == 2:
  65             menu.addAction(self.tr("Edit object"))
  66         
  67         menu.exec_(self.treeView.viewport().mapToGlobal(position))
  68 
  69 
  70 if __name__ == "__main__":
  71 
  72     app = QApplication(sys.argv)
  73     window = Window()
  74     window.show()
  75     sys.exit(app.exec_())
```
:::
::::
