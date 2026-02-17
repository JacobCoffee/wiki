# UsingEnumerate

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

**`enumerate`** is easy to use:

:::: 
::: 
``` 
   1 for index, character in enumerate("hello"):
   2   print "#%d: %s" % (index, character)
```
:::
::::

\...which prints out:

    #0: h
    #1: e
    #2: l
    #3: l
    #4: o

You can use it on just about any iterable sequence.
