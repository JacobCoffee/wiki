# PyQt/Binding widget properties to Python variables

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# Binding widget properties to Python variables 

On the Freenode `#pyqt`{.backtick} channel, \'xh\' asked if there was a way to bind widget properties to Python variables.

The following code ([bindable.py](attachments/PyQt(2f)Binding(20)widget(20)properties(20)to(20)Python(20)variables/bindable.py)) is a quick hack to demonstrate one way of doing this:

:::: 
::: 
``` 
   1 import sys
   2 from PyQt4.QtCore import *
   3 from PyQt4.QtGui import *
   4 
   5 def bind(objectName, propertyName, type):
   6 
   7     def getter(self):
   8         return type(self.findChild(QObject, objectName).property(propertyName).toPyObject())
   9     
  10     def setter(self, value):
  11         self.findChild(QObject, objectName).setProperty(propertyName, QVariant(value))
  12     
  13     return property(getter, setter)
```
:::
::::

The `bind()`{.backtick} function performs the work of creating a Python property and associated getter and setter methods that queries an instance for the object with the specified name. The getter and setter methods retrieve the object\'s named property. The getter method reads its value and performs the appropriate type conversion; the setter method sets a new value for the property.

We could bind the variable using a PyQt property instead (with the `QtCore.pyqtProperty`{.backtick} object). This would also expose the property to other Qt objects.

:::: 
::: 
``` 
   1 class Window(QWidget):
   2 
   3     def __init__(self, parent = None):
   4     
   5         QWidget.__init__(self, parent)
   6         nameEdit = QLineEdit()
   7         nameEdit.setObjectName("nameEdit")
   8         addressEdit = QTextEdit()
   9         addressEdit.setObjectName("addressEdit")
  10         contactCheckBox = QCheckBox()
  11         contactCheckBox.setObjectName("contactCheckBox")
```
:::
::::

These three widgets are the ones whose properties we want to bind variables to. We give them unique names so that the Python property methods can find them.

:::: 
::: 
``` 
   1         layout = QFormLayout(self)
   2         layout.addRow(self.tr("Name:"), nameEdit)
   3         layout.addRow(self.tr("Address:"), addressEdit)
   4         layout.addRow(self.tr("Receive extra information:"), contactCheckBox)
```
:::
::::

:::: 
::: 
``` 
   1     name = bind("nameEdit", "text", str)
   2     address = bind("addressEdit", "plainText", str)
   3     contact = bind("contactCheckBox", "checked", bool)
```
:::
::::

We create three Python properties at the class level and bind them to specific properties of the named widgets, indicating the type that each of them should have in Python.

:::: 
::: 
``` 
   1 if __name__ == "__main__":
   2 
   3     app = QApplication(sys.argv)
   4     window = Window()
   5     window.show()
   6     sys.exit(app.exec_())
```
:::
::::
