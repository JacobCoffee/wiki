# Py3kConversionTools

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

Converting Python 2.x code to Python 3.x code

------------------------------------------------------------------------

Since Python 2.6, Python has include a standard tool 2to3 to assist in the conversion. [http://docs.python.org/library/2to3.html](http://docs.python.org/library/2to3.html)

Program features that need to be changed

- has_key changed to x in dict
- apply() removed
- reduce() changed to functools.reduce()

Infrastructure for automatic refactoring

- tokenize module
- Python 2.5 compile() return ast objects
