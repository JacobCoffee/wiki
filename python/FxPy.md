# FxPy

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

::: caution
**Warning**

FXPy is unmaintained and it doesn\'t work on Python 3.
:::

[FXPy](http://fxpy.sourceforge.net) is a Python extension module that provides an interface to the [FOX](http://www.fox-toolkit.org) GUI toolkit.

FOX is a C++ based toolkit for developing graphical user interfaces easily and effectively. It offers a wide, and growing, collection of controls, and provides state of the art facilities such as drag and drop, selection, as well as OpenGL widgets for 3D graphical manipulation. FOX also implements icons, images, and user-convenience features such as status line help and tooltips.

Considerable importance has been placed on making FOX one of the fastest toolkits around, and to minimize memory use:- FOX uses a number of techniques to speed up drawing and spatial layout of the GUI. Memory is conserved by allowing programmers to create and destroy GUI elements on the fly.

Even though FOX offers a large collection of controls already, FOX leverages C++ to allow programmers to easily build additional controls and GUI elements, simply by taking existing controls, and creating a derived class which simply adds or redefines the desired behavior.

One of the prime design goals of FOX is the ease of programming; thus, most controls can be created using a single line of C++ code; most parameters have sensible default values, so that they may be omitted, and layout managers ensure that designers of GUI\'s do not have to worry about precise alignments.

Another nice feature of FOX which significantly reduces the number of lines of code which have to be written is FOX\'s ability to have widgets connect to each other, and passing certain commands between them; for example, a menu entry *Hide Toolbar* can be directly connected to the toolbar, and cause it to hide.

Finally, FOX makes it easy to maintain the state of the GUI in an application by having the GUI elements automatically updating themselves by interrogating the application\'s state. This feature eliminates the large amount of effort that may go into sensitizing, graying out, checking/unchecking etc. depending on the application state.

## FOX and FXPy Documentation 

- [FOX Documentation Index](http://www.fox-toolkit.org/doc.html)

- [Developing Graphical User Interfaces with FXPy](http://fxpy.sourceforge.net/doc/book.html)

- [FXPy source archived on github for \"historical purposes\"](https://github.com/lylejohnson/FXPy)
