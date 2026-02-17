# CodingProjectIdeas/PythonCore/UnicodeIdentifiers

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

Python should support arbitrary letters in identifiers, not just ASCII letters. The implementation should allow Unicode strings as class, function, and attribute names (possibly module names); it should specify what precise characters are allowed for identifiers (following recommendations from the Unicode Consortium). It is likely to appear only in Python 3, but should be able to run on 2.x already.

This is now implemented as [PEP 3131](http://www.python.org/dev/peps/pep-3131/).
