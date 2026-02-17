# PyQt/Customising tab bars

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# Customising tab bars 

On the `#pyqt`{.backtick} channel on Freenode, `felipe__`{.backtick} asked if it was possible to make the tabs in a QTabBar widget fill the available space.

There is a property to do this in Qt 4.5 ([http://doc.trolltech.com/4.5/qtabbar.html#expanding-prop](http://doc.trolltech.com/4.5/qtabbar.html#expanding-prop)), but earlier versions require some trickery.

In the following example, we subclass QTabBar and reimplement `tabSizeHint()`{.backtick} to treat the last tab differently to the others, calculating the available space left by the other tabs and returning this value instead of the tab\'s normal size.

:::: 
::: 
``` 
   1 from PyQt4.QtCore import QSize
   2 from PyQt4.QtGui import *
   3 
   4 class TabBar(QTabBar):
   5 
   6     def tabSizeHint(self, index):
   7         if index == self.count() - 1:
   8             size = QSize(0, 0)
   9             for i in range(self.count() - 1):
  10                 size += QTabBar.tabSizeHint(self, i)
  11             return QSize(self.width() - size.width(), size.height())
  12         else:
  13             return QTabBar.tabSizeHint(self, index)
  14         
  15 
  16 app = QApplication([])
  17 
  18 w = QWidget()
  19 layout = QHBoxLayout()
  20 
  21 leftLayout = QVBoxLayout()
  22 rightLayout = QVBoxLayout()
  23 
  24 leftLayout.addWidget(QTextEdit())
  25 
  26 tabBar = TabBar()
  27 tabBar.addTab("Hippo")
  28 tabBar.addTab("Giraffe")
  29 
  30 tempLayout = QHBoxLayout()
  31 tempLayout.addWidget(tabBar)
  32 
  33 rightLayout.addLayout(tempLayout)
  34 rightLayout.addWidget(QListView())
  35 
  36 layout.addLayout(leftLayout)
  37 layout.addLayout(rightLayout)
  38 w.setLayout(layout)
  39 
  40 w.show()
  41 app.exec_()
```
:::
::::

`felipe__`{.backtick} also asked if it was possible to just split the available space equally between all tabs.

The following code does this, but does not take into account the space required to display the label of each tab. As a result, the tabs may not appear quite as you might wish.

:::: 
::: 
``` 
   1 class TabBar(QTabBar):
   2 
   3     def tabSizeHint(self, index):
   4         return QSize(self.width() / self.count(), QTabBar.tabSizeHint(self, 0).height())
```
:::
::::
