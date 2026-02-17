# MacPython/Microsoft Word

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

Powerpoint and Word have extensive Applescript dictionaries.

Here\'s how to get the path of the folder of the current document in Word, and the name of the file:

      from appscript import *
      a = app("Microsoft Word")
      path = a.active_document.path()
      file = a.active_document.name()
      print path, file
