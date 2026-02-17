# Pyrex

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

Pyrex is a Python-like language for rapidly and easily writing python extension modules. It can be described as python with C data types. With Pyrex, one can produce Python-like code that runs as fast as in C, with easy access to C libraries and functions.

The Pyrex homepage is at [http://www.cosc.canterbury.ac.nz/\~greg/python/Pyrex/](http://www.cosc.canterbury.ac.nz/~greg/python/Pyrex/)

The two main uses of Pyrex are:

- To speed up the execution of Python code
- To provide a Python interface to existing C modules/libraries

For **examples** of the speedup that Pyrex provides, see [this message](http://www.eby-sarna.com/pipermail/source-changes/2002q4/000749.html). or [this page](http://www.prescod.net/python/pyrexopt/optimization.html).

There is an enhanced fork of Pyrex, called [Cython](http://www.cython.org). It features substantial performance optimisations and improved support for newer Python language features.

[PyrexOnWindows](PyrexOnWindows) provides a step-by-step guide to **Pyrex installation on Windows**.

[pyrexdoc](http://www.freenet.org.nz/python/pyrexdoc) is a tool for **generating HTML documentation** from a compiled Pyrex module, by [DavidMcNab](./DavidMcNab.html). See other [DocumentationTools](DocumentationTools).

If you are looking for speed improvement, you may also want to consider **other Python speedup solutions** such as [PyPy](PyPy) and [weave](weave). [PyPy](PyPy)\'s spiritual predecessor, [psyco](http://psyco.sf.net), has been deprecated and is no longer actively maintained.

For accessing existing C libraries, the **ctypes** module is also available in Python 2.5 and above.
