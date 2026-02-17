# PyQt/Widgets in a layout

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# Widgets in a layout 

This page contains the source code shown in the [Creating widgets and a layout](http://www.youtube.com/watch?v=YbqwW3p7tSA) video on YouTube.

This shows basic widget creation, though most programs will tend to create and instantiate subclasses of QWidget or other widget classes for their main user interfaces.

The code below uses version 4 of [PyQt](PyQt). For version 5, see for instance the [PyQt Widgets example on GitHub](https://github.com/pyqt/examples/tree/_/src/02%20PyQt%20Widgets).

:::: 
::: 
``` 
   1 # [Create a window]
   2 
   3 import sys
   4 from PyQt4.QtGui import *
   5 
   6 app = QApplication(sys.argv) #ignore()
   7 window = QWidget()
   8 window.setWindowTitle("Hello World")
   9 window.show()
  10 
  11 # [Add widgets to the widget]
  12 
  13 # Create some widgets (these won't appear immediately):
  14 nameLabel = QLabel("Name:")
  15 nameEdit = QLineEdit()
  16 addressLabel = QLabel("Address:")
  17 addressEdit = QTextEdit()
  18 
  19 # Put the widgets in a layout (now they start to appear):
  20 layout = QGridLayout(window)
  21 layout.addWidget(nameLabel, 0, 0)
  22 layout.addWidget(nameEdit, 0, 1)
  23 layout.addWidget(addressLabel, 1, 0)
  24 layout.addWidget(addressEdit, 1, 1)
  25 layout.setRowStretch(2, 1)
  26 
  27 # [Resizing the window]
  28 
  29 # Let's resize the window:
  30 window.resize(480, 160)
  31 
  32 # The widgets are managed by the layout...
  33 window.resize(320, 180)
  34 
  35 # [Run the application]
  36 
  37 # Start the event loop...
  38 sys.exit(app.exec_())
```
:::
::::
