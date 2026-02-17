# PyQt/Handling context menus

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# Handling context menus 

On the #pyqt channel on Freenode, `jams`{.backtick} asked about adding a context menu to a table widget.

The context menu policy described by [Qt.ContextMenuPolicy](http://www.riverbankcomputing.com/static/Docs/PyQt4/html/qt.html#ContextMenuPolicy-enum) determines how context menus are handled by each widget. To choose a policy, we call its [setContextMenuPolicy()](http://www.riverbankcomputing.com/static/Docs/PyQt4/html/qwidget.html#setContextMenuPolicy) method with one of the policy values. The useful policies are `DefaultContextMenu`{.backtick}, `ActionsContextMenu`{.backtick} and `CustomContextMenu`{.backtick}.

This means that there are basically three ways to add a context menu to a widget:

1.  Subclass the widget and reimplement its [contextMenuEvent()](http://www.riverbankcomputing.com/static/Docs/PyQt4/html/qwidget.html#contextMenuEvent) handler method, using the default context menu policy.

2.  Add actions to the widget and set the context menu policy to `ActionsContextMenu`{.backtick}.

3.  Set the context menu policy to `CustomContextMenu`{.backtick} and connect the widget\'s [customContextMenuRequested()](http://www.riverbankcomputing.com/static/Docs/PyQt4/html/qwidget.html#customContextMenuRequested) signal to a slot or method where a menu can be opened.

The code for the examples shown here can be found as attachments to this page:

- [custommenu_subclass.py](attachments/PyQt(2f)Handling(20)context(20)menus/custommenu_subclass.py)

- [custommenu_actions.py](attachments/PyQt(2f)Handling(20)context(20)menus/custommenu_actions.py)

- [custommenu_actions_standard.py](attachments/PyQt(2f)Handling(20)context(20)menus/custommenu_actions_standard.py)

- [custommenu_signal.py](attachments/PyQt(2f)Handling(20)context(20)menus/custommenu_signal.py)

## Subclassing 

If you are writing a custom widget or are subclassing a standard widget, the default subclassing approach is quite convenient.

We reimplement the context menu event and create our own menu, making sure that we convert the position passed in the `event`{.backtick} object from local widget coordinates to global screen coordinates.

:::: 
::: 
``` 
   1 import sys
   2 from PyQt4.QtCore import Qt
   3 from PyQt4.QtGui import *
   4 
   5 class TableWidget(QTableWidget):
   6 
   7     def __init__(self, parent = None):
   8     
   9         QTableWidget.__init__(self, parent)
  10     
  11     def contextMenuEvent(self, event):
  12     
  13         menu = QMenu(self)
  14         quitAction = menu.addAction("Quit")
  15         action = menu.exec_(self.mapToGlobal(event.pos()))
  16         if action == quitAction:
  17             qApp.quit()
  18 
  19 app = QApplication([])
  20 tableWidget = TableWidget()
  21 tableWidget.show()
  22 sys.exit(app.exec_())
```
:::
::::

## Actions 

For widgets with built-in actions, we can change the policy to `ActionsContextMenu`{.backtick} and the widget will automatically obtain its own context menu. For widgets without built-in actions, we can add new ones.

:::: 
::: 
``` 
   1 import sys
   2 from PyQt4.QtCore import Qt
   3 from PyQt4.QtGui import *
   4 
   5 class TableWidget(QTableWidget):
   6 
   7     def __init__(self, parent = None):
   8     
   9         QTableWidget.__init__(self, parent)
  10         self.setContextMenuPolicy(Qt.ActionsContextMenu)
  11         
  12         quitAction = QAction("Quit", self)
  13         quitAction.triggered.connect(qApp.quit)
  14         self.addAction(quitAction)
  15 
  16 app = QApplication([])
  17 tableWidget = TableWidget()
  18 tableWidget.show()
  19 sys.exit(app.exec_())
```
:::
::::

We can even add actions to standard widgets without having to subclass them:

:::: 
::: 
``` 
   1 import sys
   2 from PyQt4.QtCore import Qt
   3 from PyQt4.QtGui import *
   4 
   5 app = QApplication([])
   6 tableWidget = QTableWidget()
   7 tableWidget.setContextMenuPolicy(Qt.ActionsContextMenu)
   8 
   9 quitAction = QAction("Quit", None)
  10 quitAction.triggered.connect(qApp.quit)
  11 tableWidget.addAction(quitAction)
  12 
  13 tableWidget.show()
  14 sys.exit(app.exec_())
```
:::
::::

## Signal and Slot 

Sometimes, when we do not want to subclass a standard widget or use actions, it is easier to handle the context menu in a separate component, so we need a way for the widget to notify us when a context menu has been requested. We can do this by changing the policy to `CustomContextMenu`{.backtick} and connecting the widget\'s `customContextMenuRequested()`{.backtick} signal to a slot, method or function.

:::: 
::: 
``` 
   1 import sys
   2 from PyQt4.QtCore import Qt
   3 from PyQt4.QtGui import *
   4 
   5 app = QApplication([])
   6 tableWidget = QTableWidget()
   7 tableWidget.setContextMenuPolicy(Qt.CustomContextMenu)
   8 
   9 def openMenu(position):
  10 
  11     menu = QMenu()
  12     quitAction = menu.addAction("Quit")
  13     action = menu.exec_(tableWidget.mapToGlobal(position))
  14     if action == quitAction:
  15         qApp.quit()
  16 
  17 tableWidget.customContextMenuRequested.connect(openMenu)
  18 tableWidget.show()
  19 sys.exit(app.exec_())
```
:::
::::

The signal delivers a [QPoint](http://www.riverbankcomputing.com/static/Docs/PyQt4/html/qpoint.html) value, representing the position of the menu request in local widget coordinates. As before, we convert the position to a global screen position before showing the menu.
