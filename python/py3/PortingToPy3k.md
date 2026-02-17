# PortingToPy3k

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

::: caution
**Python 2.x will no longer be supported after 1 Jan 2020.**

Python 2 reaches end of life in January 2020, and will no longer receive security updates. This page has resources to help with porting applications still running Python 2 to Python 3.
:::

# General questions 

- [Python 3 Frequently Asked Questions](./Python3000(2f)FAQ.html)

# Porting code to Python 3 

Since Python 3 introduces some incompatibilities, a porting strategy is needed to be able to run code on Python 3, and to have a single codebase that can be made to work under Python 2 and Python 3 using automatic conversion.

There are two separate issues here:

- [Porting Python code](PortingPythonToPy3k)

- [Porting C code (extension modules)](PortingExtensionModulesToPy3k)

When finished, these two documents are meant to be a comprehensive guide to porting and maintaining Python 2/3 code. They are authored here in the Wiki and will be included in the official Python documentation when in a good shape.

We also have a [Quick Reference](./PortingToPy3k(2f)BilingualQuickRef.html) to porting code to run on both python2 and python3. At some point, this should be folded into the above pages but currently it contains a quick reference for both Python code and extension modules so it needs some restructuring to fit in.

# Porting between Python 3 versions 

While Python 2 development has ceased at Python 2.7, new Python 3 versions are released at regular intervals. While all efforts are made to maintain backward compatibility between Python 3 versions, through the application of bug fixes and other changes, some small incompatibilities do creep in. Here are some collections of resources that may help you in porting your code between Python 3 major versions.

- From [Python 3.4 to 3.5](./PortingToPy3k(2f)34to35.html)

# Contact 

Help with and discussion of porting is available on the [python-porting mailing list](http://mail.python.org/mailman/listinfo/python-porting).
