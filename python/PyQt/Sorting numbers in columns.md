# PyQt/Sorting numbers in columns

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# Sorting numbers in columns 

On the [PyQt mailing list](./PyQt(2f)TheMailingList.html), Bernard Van Der Stichele asked if it was possible to sort a column of numbers in a QTableWidget by their real numeric values instead of treating them as strings.

The following example shows how to do this for a QTableView with a model. I don\'t think it\'s possible to apply this to a QTableWidget because its model is private.

:::: 
::: 
``` 
   1 import random, sys
   2 from PyQt4.QtCore import Qt, QVariant
   3 from PyQt4.QtGui import *
   4 
   5 class NumberSortModel(QSortFilterProxyModel):
   6 
   7     def lessThan(self, left, right):
   8     
   9         lvalue = left.data().toDouble()[0]
  10         rvalue = right.data().toDouble()[0]
  11         return lvalue < rvalue
  12 
  13 
  14 if __name__ == "__main__":
  15 
  16     app = QApplication(sys.argv)
  17     model = QStandardItemModel(5, 5)
  18     random.seed()
  19     for i in range(5):
  20         for j in range(5):
  21             item = QStandardItem()
  22             item.setData(QVariant(str(random.randint(-500, 500)/10.0)), Qt.DisplayRole)
  23             model.setItem(i, j, item)
  24     
  25     proxy = NumberSortModel()
  26     proxy.setSourceModel(model)
  27     
  28     view = QTableView()
  29     view.setModel(proxy)
  30     view.setSortingEnabled(True)
  31     view.show()
  32     sys.exit(app.exec_())
```
:::
::::
