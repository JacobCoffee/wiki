# PyQt/Handling Qt's internal item MIME type

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# Handling Qt\'s internal item MIME type 

Normally, to perform drag and drop between two item views, the developer would create their own model, reimplementing the `mimeData()`{.backtick} method to return a custom MIME type and the `dropMimeData()`{.backtick} method to accept data with this MIME type. However, this seems like a lot of work, especially when the data comes from a standard model.

The following code implements a model that you can use for the view that accepts dropped data. The `decode_data()`{.backtick} method decodes `application/x-qabstractitemmodeldatalist`{.backtick} MIME type data supplied by a standard model. The reimplementation of the `dropMimeData()`{.backtick} method takes the decoded data and either adds a new item to the top level of a tree structure or increments a counter associated with each item.

Qt\'s item views pass around items using the internal `application/x-qabstractitemmodeldatalist`{.backtick} MIME type (see the [Model Subclassing Reference](http://doc.trolltech.com/4.5/model-view-model-subclassing.html#mime-data) for more information about this type). For practical purposes, it may be useful to be able to unpack data sent in this format when implementing a drop handler for a custom model. The example shown in this document shows how this can be done in Python.

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
```
:::
::::

The start of the `dropMimeData()`{.backtick} method queries the MIME data for the format we recognise. If it can supply data in the internal MIME type used by Qt, we call a helper method to unpack it. The helper method will return a list of dictionaries corresponding to each of the items dropped onto the view. Each dictionary maps a role number to corresponding data for that role. We are interested in the text supplied in the display role.

:::: 
::: 
``` 
   1     def dropMimeData(self, data, action, row, column, parent):
   2     
   3         if data.hasFormat('application/x-qabstractitemmodeldatalist'):
   4             bytearray = data.data('application/x-qabstractitemmodeldatalist')
   5             data_items = self.decode_data(bytearray)
   6             
   7             # Assuming that we get at least one item, and that it defines
   8             # text that we can display.
   9             text = data_items[0][Qt.DisplayRole].toString()
  10             
  11             for row in range(self.rowCount()):
  12                 name = self.item(row, 0).text()
  13                 if name == text:
  14                     number_item = self.item(row, 1)
  15                     number = int(number_item.text())
  16                     number_item.setText(str(number + 1))
  17                     break
  18             else:
  19                 name_item = QStandardItem(text)
  20                 number_item = QStandardItem("1")
  21                 self.appendRow([name_item, number_item])
  22             
  23             return True
  24         else:
  25             return QStandardItemModel.dropMimeData(self, data, action, row, column, parent)
```
:::
::::

The rest of this method just does what the requester wanted: it puts the names into the model with an associated number, starting at 1, or increments the number associated with existing items if they are already present in the model. Data not handled by us is passed to the base class\'s implementation of `dropMimeData()`{.backtick}.

The `decode_data()`{.backtick} method relies on the internal format used by Qt when sending items as MIME data. The byte array is opened using a data stream and unpacked using the information that it contains a sequence of items, each stored as a pair of row and column integers followed by a map of role integers to `QVariant`{.backtick} values. (See [Format of the QDataStream Operators](http://doc.trolltech.com/4.5/datastreamformat.html) for more information about how these are serialised by Qt.)

:::: 
::: 
``` 
   1     def decode_data(self, bytearray):
   2     
   3         data = []
   4         item = {}
   5         
   6         ds = QDataStream(bytearray)
   7         while not ds.atEnd():
   8         
   9             row = ds.readInt32()
  10             column = ds.readInt32()
  11             
  12             map_items = ds.readInt32()
  13             for i in range(map_items):
  14             
  15                 key = ds.readInt32()
  16                 
  17                 value = QVariant()
  18                 ds >> value
  19                 item[Qt.ItemDataRole(key)] = value
  20             
  21             data.append(item)
  22         
  23         return data
  24 
  25 app = QApplication(sys.argv)
  26 
  27 window = QWidget()
  28 
  29 listModel = QStringListModel(["John", "Jane", "Frank", "Henry"])
  30 listView = QListView()
  31 listView.setModel(listModel)
  32 listView.setDragEnabled(True)
  33 
  34 treeModel = TreeModel()
  35 treeView = QTreeView()
  36 treeView.setHeaderHidden(True)
  37 treeView.setRootIsDecorated(False)
  38 treeView.setAcceptDrops(True)
  39 treeView.setModel(treeModel)
  40 
  41 layout = QHBoxLayout(window)
  42 layout.addWidget(listView)
  43 layout.addWidget(treeView)
  44 
  45 window.show()
  46 sys.exit(app.exec_())
```
:::
::::
