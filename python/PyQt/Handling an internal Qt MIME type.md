# PyQt/Handling an internal Qt MIME type

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# Handling an internal Qt MIME type 

On the `#pyqt`{.backtick} channel on Freenode, `reenen`{.backtick} asked if it was possible to handle the internal MIME type Qt uses for drag and drop between item views.

See [Handling Qt\'s internal item MIME type](./PyQt(2f)Handling(20)Qt(27)s(20)internal(20)item(20)MIME(20)type.html) for the details.

:::: 
::: 
``` 
   1 import sys
   2 from PyQt4.QtCore import QDataStream, Qt, QVariant
   3 from PyQt4.QtGui import *
   4 
   5 class TreeModel(QStandardItemModel):
   6 
   7     def __init__(self, parent = None):
   8     
   9         QStandardItemModel.__init__(self, parent)
  10     
  11     def dropMimeData(self, data, action, row, column, parent):
  12     
  13         if data.hasFormat('application/x-qabstractitemmodeldatalist'):
  14             bytearray = data.data('application/x-qabstractitemmodeldatalist')
  15             data_items = self.decode_data(bytearray)
  16             
  17             # Decode the data, assuming that we get 6 32-bit integers to
  18             # start with, then a count byte followed by a string.
  19             text = data_items[Qt.DisplayRole].toString()
  20             for row in range(self.rowCount()):
  21                 name = self.item(row, 0).text()
  22                 if name == text:
  23                     number_item = self.item(row, 1)
  24                     number = int(number_item.text())
  25                     number_item.setText(str(number + 1))
  26                     break
  27             else:
  28                 name_item = QStandardItem(text)
  29                 number_item = QStandardItem("1")
  30                 self.appendRow([name_item, number_item])
  31             
  32             return True
  33         else:
  34             return QStandardItemModel.dropMimeData(self, data, action, row, column, parent)
  35     
  36     def decode_data(self, bytearray):
  37     
  38         data = {}
  39         
  40         ds = QDataStream(bytearray)
  41         while not ds.atEnd():
  42         
  43             row = ds.readInt32()
  44             column = ds.readInt32()
  45             
  46             map_items = ds.readInt32()
  47             for i in range(map_items):
  48             
  49                 key = ds.readInt32()
  50                 
  51                 value = QVariant()
  52                 ds >> value
  53                 data[Qt.ItemDataRole(key)] = value
  54         
  55         return data
  56 
  57 app = QApplication(sys.argv)
  58 
  59 window = QWidget()
  60 
  61 listModel = QStringListModel(["John", "Jane", "Frank", "Henry"])
  62 listView = QListView()
  63 listView.setModel(listModel)
  64 listView.setDragEnabled(True)
  65 
  66 treeModel = TreeModel()
  67 treeView = QTreeView()
  68 treeView.setHeaderHidden(True)
  69 treeView.setRootIsDecorated(False)
  70 treeView.setAcceptDrops(True)
  71 treeView.setModel(treeModel)
  72 
  73 layout = QHBoxLayout(window)
  74 layout.addWidget(listView)
  75 layout.addWidget(treeView)
  76 
  77 window.show()
  78 sys.exit(app.exec_())
```
:::
::::
