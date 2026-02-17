# JythonFaq/JythonModules

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# Jython modules 

[JythonFaq](JythonFaq)

------------------------------------------------------------------------

## What parts of the Python library are supported? 

The good news is that Jython now supports almost all of the standard Python library.

If there is some standard Python module that you have a real need for that doesn\'t work with Jython yet, please file a bug.

------------------------------------------------------------------------

## Can I use the python DB API from Jython? 

Use zxJDBC which gives data database connectivity from Jython using the Python DB API 2.0 interface. For more information about using zxJDBC see:

\- [http://www.jython.org/docs/zxjdbc.html](http://www.jython.org/docs/zxjdbc.html)

Note: the use of zxJDBC is now discouraged in favour of JyJDBC. One reason for that is the lack of testing in zxJDBC, which makes non trivial to change it.

\- [https://code.google.com/p/jyjdbc/](https://code.google.com/p/jyjdbc/)

------------------------------------------------------------------------

## Can I use the Numeric package from Jython? 

Take a look at at Tim Hochberg\'s Java implementation of Numeric, JNumeric.

\- [http://jnumerical.sourceforge.net/index.html](http://jnumerical.sourceforge.net/index.html)
