# PythonWebKit

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

[PythonWebKit](http://www.gnu.org/software/pythonwebkit) provides direct python DOM bindings to the Webkit Web Browser engine. It places python as a peer of javascript, allowing developers to call functions such as getElementsByTagName, appendChild and even add python event callbacks onto XMLHttpRequest, Window and HTML Elements (onclick, onreadystatechange, onresize etc.)

The difference between PythonWebKit and [PyWebkitGtk](PyWebkitGtk) and [PyWebkitQt4](./PyWebkitQt4.html) is that PythonWebKit adds the entire range of W3C DOM bindings functions - including HTML5 features - whereas [PyWebkitGtk](PyWebkitGtk) and [PyWebkitQt4](./PyWebkitQt4.html) provide very little, inadequate, incomplete and more CPU-intensive DOM bindings.
