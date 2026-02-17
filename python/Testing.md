# Testing

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

Testing is matching output produced by your Python code with your expectations.

Testing strategy is what you test and how you do it. There are multiple strategies that can be combined:

- unit tests - your Python code is limited by specific function and methods
- performance - measure performance over the time
- fuzz testing - overload your inputs with garbage to see the response
- web testing - code is server-side and expected output is web stuff
- acceptance - write testing logic once, and run it over a set of desired output

See [PythonTestingToolsTaxonomy](PythonTestingToolsTaxonomy) for more details.
