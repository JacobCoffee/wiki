# Asking for Help/How to have a mutable buffer with python 2.3?

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# Asking for Help: How to have a mutable buffer with python 2.3? 

Use the MutableString class in the UserString module:

:::: 
::: 
``` 
   1 >>> from UserString import MutableString
   2 >>> s = MutableString('python')
   3 >>> s[2:4] = 'l'
   4 >>> print s
   5 pylon
```
:::
::::

------------------------------------------------------------------------

[CategoryAskingForHelp](CategoryAskingForHelp) [CategoryAskingForHelpAnswered](CategoryAskingForHelpAnswered)
