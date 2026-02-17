# PyQt/Animated items using delegates and movies

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# Animated items using delegates and movies 

This example shows how to use a custom delegate with an animation to indicate that an item is busy, or perhaps waiting for additional data.

Example code: [movie_delegate.py](attachments/PyQt(2f)Animated(20)items(20)using(20)delegates(20)and(20)movies/movie_delegate.py)

## Outline 

For convenience, we re-use QStandardItemModel and QStandardItem. Real world models may be completely implemented from scratch by subclassing QAbstractItemModel or one of its subclasses.

To produce busy items, we create QStandardItem instances, some of which we modify by setting their UserRole roles to True, indicating that they are waiting for something.

We subclass QStandardItemModel so that we can examine items as they are added to the model. We create timers for waiting items to simulate some delay in obtaining data, and we keep track of the associated items so that we can change their states when the timers elapse.

:::: 
::: 
``` 
   1 import random, sys
   2 from PyQt4.QtCore import pyqtSignal, QObject, Qt, QTimer, QVariant
   3 from PyQt4.QtGui import *
```
:::
::::

The delegate class uses a QMovie instance to generate images to display for waiting items. We create a custom signal, `needsRedraw`{.backtick}, that we emit every time the movie changes its current frame.

:::: 
::: 
``` 
   1 class Delegate(QItemDelegate):
   2 
   3     needsRedraw = pyqtSignal()
   4     
   5     def __init__(self, movie, parent = None):
   6     
   7         QItemDelegate.__init__(self, parent)
   8         self.movie = movie
   9         self.movie.frameChanged.connect(self.needsRedraw)
  10         self.playing = False
  11     
  12     def startMovie(self):
  13         self.movie.start()
  14         self.playing = True
  15     
  16     def stopMovie(self):
  17         self.movie.stop()
  18         self.playing = False
  19     
  20     def paint(self, painter, option, index):
  21     
  22         waiting = index.data(Qt.UserRole).toBool()
  23         if waiting:
  24             option = option.__class__(option)
  25             pixmap = self.movie.currentPixmap()
  26             painter.drawPixmap(option.rect.topLeft(), pixmap)
  27             option.rect = option.rect.translated(pixmap.width(), 0)
  28         
  29         QItemDelegate.paint(self, painter, option, index)
```
:::
::::

We reimplement the `paint()`{.backtick} method of the delegate, adjusting the region in which the delegate draws its normal contents, and we draw a pixmap at the left-hand end of the item. We finish by calling the base class\'s implementation of the `paint()`{.backtick} method so that the rest of the item is painted normally.

The customisations to the model class are minimal. We provide a custom signal, `finished`{.backtick}, so that we can inform other components when all waiting items have finished, and we keep a dictionary that maps timers to pending items.

:::: 
::: 
``` 
   1 class Model(QStandardItemModel):
   2 
   3     finished = pyqtSignal()
   4     
   5     def __init__(self, parent = None):
   6     
   7         QStandardItemModel.__init__(self, parent)
   8         self.pendingItems = {}
   9     
  10     def appendRow(self, item):
  11     
  12         if item.data(Qt.UserRole).toBool():
  13         
  14             timer = QTimer()
  15             timer.timeout.connect(self.checkPending)
  16             timer.setSingleShot(True)
  17             self.pendingItems[timer] = item
  18             timer.start(2000 + random.randrange(0, 2000))
  19         
  20         QStandardItemModel.appendRow(self, item)
```
:::
::::

Reimplementing the `appendRow()`{.backtick} method, we create timers for items that are waiting (they have their [UserRole](./UserRole.html) set to True), and store them in the `pendingItems`{.backtick} dictionary. Each timer\'s `timeout`{.backtick} signal is connected to the `checkPending()`{.backtick} slot.

This method simply retrieves the corresponding item for each timer and updates its state so that the delegate no longer shows it as a waiting item. It then deletes the dictionary entry (and the timer, since it is the dictionary key). If no items remain in the dictionary, we emit the `finished`{.backtick} signal.

:::: 
::: 
``` 
   1     def checkPending(self):
   2     
   3         # Check when items are updated so that we can emit the finished()
   4         # signal when the list is cleared.
   5         item = self.pendingItems[self.sender()]
   6         del self.pendingItems[self.sender()]
   7         item.setData(QVariant(False), Qt.UserRole)
   8         if not self.pendingItems:
   9             self.finished.emit()
```
:::
::::

We might want to be more careful with items here. For example, we may need to deal with them differently if they have been removed from the model.

The creation of the model and items is as we described in the outline. We create a standard view and an instance of our custom model, which we populate with standard items, making sure to mark some of them as waiting items.

:::: 
::: 
``` 
   1 if __name__ == "__main__":
   2 
   3     random.seed()
   4     
   5     app = QApplication(sys.argv)
   6     view = QListView()
   7     model = Model()
   8     waiting = True
   9     
  10     for i in range(5):
  11     
  12         item = QStandardItem("Test %i" % i)
  13         item.setData(QVariant(waiting), Qt.UserRole)
  14         waiting = not waiting
  15         model.appendRow(item)
  16     
  17     view.setModel(model)
```
:::
::::

The delegate is set up with an animation (see [animation.mng](attachments/PyQt(2f)Animated(20)items(20)using(20)delegates(20)and(20)movies/animation.mng)) and its `needsRedraw`{.backtick} signal is connected to the `update()`{.backtick} slot of the view\'s viewport - using the view\'s `update()`{.backtick} slot is not sufficient, it seems. We start the movie.

:::: 
::: 
``` 
   1     delegate = Delegate(QMovie("animation.mng"))
   2     view.setItemDelegate(delegate)
   3     delegate.needsRedraw.connect(view.viewport().update)
   4     delegate.startMovie()
   5     
   6     model.finished.connect(delegate.stopMovie)
   7     model.finished.connect(view.viewport().update)
```
:::
::::

We connect the model\'s `finished`{.backtick} slot to the delegate\'s `stopMovie()`{.backtick} slot - there is no point in running the movie if no items are waiting - and to the appropriate `update()`{.backtick} slot.

Now we can show the view and start the event loop.

:::: 
::: 
``` 
   1     view.show()
   2     sys.exit(app.exec_())
```
:::
::::

## Conclusions 

This appears to work quite well, and it should be possible to write more abstract models that actually need to wait for data, but I\'m not satisfied with having lots of low-level connections between the components. Perhaps I\'ll apply the technique to a real world model and create a new example based on my experience.
