# SpeedUpInterpreterStartup

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

At [PyCon](PyCon) 2004 the startup time of the interpreter was analyzed and it was realized that no simple solution existed. Part of the reason was some older code, such as the \'site\' module which could stand a rewrite, was not optimized for modern Python. Another issue was other modules that were written in Python that might do better written in C (\'warnings\'?). It seemed importation of code was the major cause of a slow startup.

So, to make this work, one might need to consider:

- what modules are imported automatically
- whether modules that are always imported could be improved/modernized with an eye on efficiency
- lowering importation dependencies

## Notes 

The thing I keep running into is the time it takes the \'re\' module to load. Python doesn\'t load that initially by default but it\'s widely used so its slowness does in practice slow down startup. *- Stephan Deibel*
