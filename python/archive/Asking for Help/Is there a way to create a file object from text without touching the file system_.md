# Asking for Help/Is there a way to create a file object from text without touching the file system?

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# Asking for Help: Is there a way to create a file object from text without touching the file system? 

I want to use [ElementTree](ElementTree) to parse a text object, but the [ElementTree](ElementTree).parse function looks like it only takes file objects. I\'m doing this all from within Blender, and don\'t want to touch the filesystem - so is there a way to create a file object from text (to pass to parse) without touching the file system? I\'d also like to go the other way, create a text object from an [ElementTree](ElementTree) object.

## Answer 

The `StringIO`{.backtick} module provides support for treating strings like file objects. Since there\'s a faster version of the module, the idiom to use to access the all-important `StringIO`{.backtick} class (yes, it has the same name) is as follows:

:::: 
::: 
``` 
   1 try:
   2     from cStringIO import StringIO
   3 except ImportError:
   4     from StringIO import StringIO
```
:::
::::

In fact, for the exact problem you\'re having, the example \"21 lines: XML/HTML parsing (using Python 2.5 or third-party library)\" from the [SimplePrograms](SimplePrograms) page should at least help you with the parsing problem. For serialising (\"going the other way\"), you probably want to create a `StringIO`{.backtick} object and then pass it to the appropriate [ElementTree](ElementTree) node method.

------------------------------------------------------------------------

[CategoryAskingForHelp](CategoryAskingForHelp) [CategoryAskingForHelpAnswered](CategoryAskingForHelpAnswered)
