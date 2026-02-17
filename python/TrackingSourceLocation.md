# TrackingSourceLocation

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

The CPython interpreter currently tracks the source location of a code object in the co_filename attribute. In certain cases, this is a relative file name, which may break if the current directory changes. The objective of this project is to make sure that co_filename is always an absolute path, or to allow otherwise to infer the original location of the source file. In addition, if the module was imported from a byte code file, a mechanism should be provided to also find out what that byte code file was.

label:[NeedsTest](./NeedsTest.html)

------------------------------------------------------------------------

[CategoryIdeas](CategoryIdeas)
