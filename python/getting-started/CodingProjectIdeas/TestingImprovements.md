# CodingProjectIdeas/TestingImprovements

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

- Update all old tests to use unittest or doctest; see the [output](http://svn.python.org/view/python/trunk/Lib/test/output/) directory in svn to see what old tests still exist (minus any conversions already in Python\'s issue tracker). \[Done at [PyCon](PyCon) 2008\]

- Develop toolchain to make testing better and more helpful to non-CPython implementations.
  - Function to specify what module is being tested. This allows [ImportErrors](./ImportErrors.html) for modules required for testing to cause the test to fail, not skip the testing.

  - Function to specify what OSs the module being tested is expected to work on.

  - Function to specify if the module being tested is \"optional\" (i.e., reasonable to not have built).

  - Decorators (method and class) to classify tests; OS, known failure, implementation detail or not, etc. Helpful for [PyPy](PyPy) et. al. so they know they don\'t need to test something (e.g., refcount specifics).

  - Make unittest not print the docstring of a test instead of the method name when running a test.

- Create effective and stable tests for server/client bits of the standard library.
