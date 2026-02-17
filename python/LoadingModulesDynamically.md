# LoadingModulesDynamically

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

You can load a module dynamically like so:

:::: 
::: 
``` 
   1 __import__("os")
```
:::
::::

If you do that, though, \"os\" isn\'t bound to anything.

:::: 
::: 
``` 
   1 >>> __import__("os")
   2 <module 'os' from '/usr/lib/python2.3/os.pyc'>
   3 >>> os
   4 Traceback (most recent call last):
   5   File "<stdin>", line 1, in ?
   6 NameError: name 'os' is not defined
   7 >>>
```
:::
::::

Once you have the module, you probably want to find classes and functions and data inside of it.

Use `getattr`:

:::: 
::: 
``` 
   1 >>> m=__import__("mine")
   2 >>> m
   3 <module 'mine' from 'mine.pyc'>
   4 >>> getattr(m, "eggs")
   5 4654
   6 >>> getattr(m, "ham")
   7 'Monty Python'
```
:::
::::
