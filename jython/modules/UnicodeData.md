# UnicodeData

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

This is out of date, we have an implementation of unicodedata currently in Jython and soon in Java. Some of these issues are still relevant, so retaining this page for now.

===================================

Initially, I am just going to dump stuff out so that I don\'t forget it. Later on, I hope to savagely re-edit it into a more coherent structure.

## Overview 

unicodedata is essentially a lookup table of the [Unicode Character Database](http://www.unicode.org/ucd/) that is published as part of the Unicode specification. There seem to be effectively two types of lookup:

1.  Given a unicode character, retrieve a property of that character.
2.  Given a unicode character name, retrieve the unicode character (the unicodedata.lookup function).

It\'s probably worthwhile trying to compile a list of known clients of this module, so that we have a clear idea of the usages that should be optimized.

Breaking it down further, the obvious implementation is to have two lookup tables.

1.  The first one will take an integer (or unichr - a Unicode character is effectively an integer in this context) and return an O(1) index into a table which defines the properties of the character.
2.  The second one will be a dictionary lookup or similar, to find a codepoint given a name.

TODO better analysis of CPython version, describing the table encoding and space-time trade-offs.

TODO testing notes. Existing tests, why java.lang.Character and ICU aren\'t considered suitable (the latter without OSGi / classloader shenanigans anyway), more tests around surrogate characters (c.f. Sam Ruby on the subject, which is always entertaining).

TODO understand whether the OpenJDK stuff can be re-used (the stuff that generates the java.lang.Character stuff, and just point it at whichever versions of the Unicode Character Database we wish to support.

## Bibliography 

- [The Unicode Consortium](http://www.unicode.org/)

- [Wikipedia article](http://en.wikipedia.org/wiki/Unicode)

- A [discussion](http://java.sun.com/developer/technicalArticles/Intl/Supplementary/) of Unicode support in the Java platform.

- [Unicode Ate My Brain](http://home.ccil.org/~cowan/uamb.pdf) Nice discussion about the different table lookups, for people like myself without a classical CS background or strong knowledge about data structures and algorithms.
