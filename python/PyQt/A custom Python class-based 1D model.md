# PyQt/A custom Python class-based 1D model

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# A custom Python class-based 1D model 

On 2010-04-12, on the `#pyqt`{.backtick} channel on Freenode, `rowinggolfer`{.backtick} [pasted](http://paste.debian.net/68590/) the following model with these remarks:

    [18:20] <rowinggolfer> I played with a custom python class based 1d model, attached to a listview, and accessed via drag/drop.
    [18:20] <rowinggolfer> I put the code up here for anyone to play with / fine tune.
    [18:20] <rowinggolfer> http://paste.debian.net/68590/
    [18:21] <rowinggolfer> there's a couple of standard (?) tricks in there... using QUserRole to get the actual python object passed to the QDrag as an argument
    [18:21] <rowinggolfer> and converting to a bytestream using pickle
    [18:22] <rowinggolfer> I also played with generating a nice pixmap for the drag, but decided that the grabwidget method is easiest.

:::: 
::: 
``` 
   1 import datetime
   2 import cPickle
   3 import pickle
   4 import sys
   5 
   6 from PyQt4 import QtGui, QtCore
   7 
   8 class person(object):
   9     '''
  10     a custom data structure, for example purposes
  11     '''
  12     def __init__(self, name, dob, house_no):
  13         self.name = name
  14         self.dob = dob
  15         self.addr = "%d Rue de la Soleil"% house_no
  16     def __repr__(self):
  17         return "%s\n%s\n%s"% (self.name, self.dob, self.addr)
  18 
  19 class simple_model(QtCore.QAbstractListModel):
  20     def __init__(self, parent=None):
  21         super(simple_model, self).__init__(parent)
  22         self.list = []
  23         for name, dob, house_no in (
  24         ("Neil", datetime.date(1969,12,9), 23),
  25         ("John", datetime.date(1952,5,3), 2543),
  26         ("Ilona", datetime.date(1975,4,6), 1)):
  27             self.list.append(person(name, dob, house_no))
  28         self.setSupportedDragActions(QtCore.Qt.MoveAction)
  29 
  30     def rowCount(self, parent=QtCore.QModelIndex()):
  31         return len(self.list)
  32 
  33     def data(self, index, role):
  34         if role == QtCore.Qt.DisplayRole: #show just the name
  35             person = self.list[index.row()]
  36             return QtCore.QVariant(person.name)
  37         elif role == QtCore.Qt.UserRole:  #return the whole python object
  38             person = self.list[index.row()]
  39             return person
  40         return QtCore.QVariant()
  41 
  42     def removeRow(self, position):
  43         self.list = self.list[:position] + self.list[position+1:]
  44         self.reset()
  45 
  46 class dropZone(QtGui.QLabel):
  47     def __init__(self, parent=None):
  48         super(dropZone, self).__init__(parent)
  49         self.setMinimumSize(200,200)
  50         self.set_bg()
  51         self.setText("Drop Here")
  52         self.setAlignment(QtCore.Qt.AlignCenter)
  53         self.setAcceptDrops(True)
  54 
  55     def dragEnterEvent(self, event):
  56         if event.mimeData().hasFormat("application/x-person"):
  57             self.set_bg(True)
  58             event.accept()
  59         else:
  60             event.ignore()
  61 
  62     def dragMoveEvent(self, event):
  63         if event.mimeData().hasFormat("application/x-person"):
  64             event.setDropAction(QtCore.Qt.MoveAction)
  65             event.accept()
  66         else:
  67             event.ignore()
  68 
  69     def dragLeaveEvent(self, event):
  70         self.set_bg()
  71 
  72     def dropEvent(self, event):
  73         data = event.mimeData()
  74         bstream = data.retrieveData("application/x-person",
  75             QtCore.QVariant.ByteArray)
  76         selected = pickle.loads(bstream.toByteArray())
  77         self.setText(str(selected))
  78         self.set_bg()
  79         event.accept()
  80 
  81     def set_bg(self, active=False):
  82         if active:
  83             val = "background:yellow;"
  84         else:
  85             val = "background:green;"
  86         self.setStyleSheet(val)
  87 
  88 
  89 class draggableList(QtGui.QListView):
  90     '''
  91     a listView whose items can be moved
  92     '''
  93     def ___init__(self, parent=None):
  94         super(draggableList, self).__init__(parent)
  95         self.setDragEnabled(True)
  96 
  97     def dragEnterEvent(self, event):
  98         if event.mimeData().hasFormat("application/x-person"):
  99             event.setDropAction(QtCore.Qt.QMoveAction)
 100             event.accept()
 101         else:
 102             event.ignore()
 103 
 104     def startDrag(self, event):
 105         index = self.indexAt(event.pos())
 106         if not index.isValid():
 107             return
 108 
 109         ## selected is the relevant person object
 110         selected = self.model().data(index,QtCore.Qt.UserRole)
 111 
 112         ## convert to  a bytestream
 113         bstream = cPickle.dumps(selected)
 114         mimeData = QtCore.QMimeData()
 115         mimeData.setData("application/x-person", bstream)
 116 
 117         drag = QtGui.QDrag(self)
 118         drag.setMimeData(mimeData)
 119 
 120         # example 1 - the object itself
 121 
 122         pixmap = QtGui.QPixmap()
 123         pixmap = pixmap.grabWidget(self, self.rectForIndex(index))
 124 
 125         # example 2 -  a plain pixmap
 126         #pixmap = QtGui.QPixmap(100, self.height()/2)
 127         #pixmap.fill(QtGui.QColor("orange"))
 128         drag.setPixmap(pixmap)
 129 
 130         drag.setHotSpot(QtCore.QPoint(pixmap.width()/2, pixmap.height()/2))
 131         drag.setPixmap(pixmap)
 132         result = drag.start(QtCore.Qt.MoveAction)
 133         if result: # == QtCore.Qt.MoveAction:
 134             self.model().removeRow(index.row())
 135 
 136     def mouseMoveEvent(self, event):
 137         self.startDrag(event)
 138 
 139 class testDialog(QtGui.QDialog):
 140     def __init__(self, parent=None):
 141         super(testDialog, self).__init__(parent)
 142         self.setWindowTitle("Drag Drop Test")
 143         layout = QtGui.QGridLayout(self)
 144 
 145         label = QtGui.QLabel("Drag Name From This List")
 146 
 147         self.model = simple_model()
 148         self.listView = draggableList()
 149         self.listView.setModel(self.model)
 150         self.dz = dropZone()
 151 
 152         layout.addWidget(label,0,0)
 153         layout.addWidget(self.listView,1,0)
 154         layout.addWidget(self.dz,0,1,2,2)
 155 
 156 if __name__ == "__main__":
 157     '''
 158     the try catch here is to ensure that the app exits cleanly no matter what
 159     makes life better for SPE
 160     '''
 161     try:
 162         app = QtGui.QApplication([])
 163         dl = testDialog()
 164         dl.exec_()
 165     except Exception, e:  #could use as e for python 2.6...
 166         print e
 167     sys.exit(app.closeAllWindows())
```
:::
::::
