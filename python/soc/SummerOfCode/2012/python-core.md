# SummerOfCode/2012/python-core

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# Project ideas for Python Core in GSoC 2012 

1\. Implement [PEP 3154](http://www.python.org/dev/peps/pep-3154/)

2\. Use [PEP 3121](http://www.python.org/dev/peps/pep-3121/)

- PEP 3121 is already implemented since Python 3.0, yet few modules use it. The objective would be to port all extension modules to using this API, getting rid of global variables, to allow proper module cleanup and multiple interpreters.

3\. pprint rewrite. Currently prettyprint is not extensible, an alternative but backward compatible implementation would be desirable. There is an existing issue: [http://bugs.python.org/issue7434](http://bugs.python.org/issue7434).

4\. Implement Unicode algorithms for Python 3.3 such as grapheme clustering and collation.
