# DefaultEncoding

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

Python users who are new to Unicode sometimes are attracted by default encoding returned by sys.getdefaultencoding(). The first thing you should know about default encoding is that you don\'t need to care about it. Its value should be \'ascii\' and it is used when converting byte strings [StrIsNotAString](../archive/StrIsNotAString) to unicode strings. As in this example:

:::: 
::: 
``` 
   1 a = "abc" + u"bcd"
```
:::
::::

When you concatenate byte string \"abc\" with unicode string u\"bcd\" Python will first convert \"abc\" into u\"abc\" by calling \"abc\".decode(sys.getdefaultencoding()). If you put non-ascii characters into byte string then .decode(sys.getdefaultencoding()) method will fail with `UnicodeDecodeError`, therefore byte strings should not contain non-ascii characters. In [Python3.0](../py3/Python3.0) sys.getdefaultencoding will be removed.

------------------------------------------------------------------------

[CategoryUnicode](CategoryUnicode)
