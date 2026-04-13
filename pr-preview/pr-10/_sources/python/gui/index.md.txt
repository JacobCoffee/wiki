# GUI Programming

Python has bindings for just about every GUI toolkit out there -- Qt, GTK, wxWidgets, Tk, and more. This section collects pages about desktop GUI development, from framework overviews and comparisons to specific toolkit documentation. Some of these pages are well-maintained; others reflect the state of GUI development circa 2010. Take version numbers with a grain of salt.

## Overviews and Comparisons

- [GuiProgramming](GuiProgramming) -- the main overview of GUI toolkits available for Python, with tables covering cross-platform, platform-specific, and web-based options
- [GuiBooks](GuiBooks) -- books about GUI programming with Python (PyQt, wxPython, Tkinter, etc.)
- [GuiProgrammingShootout](GuiProgrammingShootout) -- comparing GUI toolkits by implementing the same tasks in each

## Qt Bindings

- [PyQt](PyQt) -- Python bindings for Qt, covering both Qt 4 and Qt 5, with 620+ classes
- [PyQt4](PyQt4) -- PyQt4-specific page (mostly duplicates the PyQt page)
- [PyQt subpages](PyQt/index) -- extensive collection of PyQt snippets, tutorials, and examples
- [PyQt5 subpages](PyQt5/index) -- PyQt5-specific content including threading and signals/slots
- [Porting PyQt4 to Python 3](PortingPythonToPy3k/index) -- notes on porting PyQt4 code to Python 3

## wxWidgets

- [WxPython](WxPython) -- Python bindings for the wxWidgets C++ library, with installation notes and tutorial links
- [WxWidgets](WxWidgets) -- the underlying C++ toolkit (formerly wxWindows)
- [WxWindows](WxWindows) -- redirect noting the rename from wxWindows to wxWidgets

## GTK

- [PyWebkitGtk](PyWebkitGtk) -- Python bindings for WebKit on GTK, enabling web-based desktop UIs

```{toctree}
:hidden:
:maxdepth: 1

PortingPythonToPy3k/index
PyQt/index
PyQt5/index
GuiBooks
GuiProgramming
GuiProgrammingShootout
PyQt
PyQt4
PyWebkitGtk
WxPython
WxWidgets
WxWindows
```
