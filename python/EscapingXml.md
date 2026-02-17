# EscapingXml

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# Escaping XML 

The Python standard library contains a couple of simple functions for escaping strings of text as XML character data. These routines are not actually very powerful, but are sufficient for many applications. They should generally be applied to Unicode text that will later be encoded appropriately, or to already-encoded text using an ASCII-superset encoding, since most characters are left alone.

The `xml.sax.saxutils` module contains the functions `escape()` and `quoteattr()`. The `escape()` function is used to convert the `<`, `&`, and `>` characters to the corresponding entity references:

:::: 
::: 
``` 
   1 >>> from xml.sax.saxutils import escape
   2 >>>
   3 >>> escape("< & >")
   4 '&lt; &amp; &gt;'
```
:::
::::

This function does not generate either the `&apos;` or `&quot;` entity references; these are not needed in parsed character data in an XML document. They may be needed in character data in attribute values, however. For attribute values, `quoteattr()` function provides a more useful service than `escape()`. `quoteattr()` will determine whether single or double quotation marks are more appropriate for an attribute value and quote the value appropriately; values which include both kinds of quotation marks in the value cause `&quot;` to be used as needed. The return value includes the quotation marks which are needed to ensure the value is properly quoted:

:::: 
::: 
``` 
   1 >>> from xml.sax.saxutils import quoteattr
   2 >>>
   3 >>> quoteattr("some value ' containing an apostrophe")
   4 '"some value \' containing an apostrophe"'
   5 >>> quoteattr('some value containing " a double-quote')
   6 '\'some value containing " a double-quote\''
   7 >>> quoteattr('value containing " a double-quote \' and an apostrophe')
   8 '"value containing &quot; a double-quote \' and an apostrophe"'
```
:::
::::

Both of these functions can be provided with a mapping of additional replacements that should be made; the same mapping can generally be used for both. This can be used to add additional entities specific to the DTD of the document being generated, or to cause particular characters to be encoded as character references:

:::: 
::: 
``` 
   1 >>> escape("abc", {"b": "&#98;"})
   2 'a&#98;c'
   3 >>> escape("My product, PyThingaMaJiggie, is really cool.",
   4 ...        {"PyThingaMaJiggie": "&productName;"})
   5 'My product, &productName;, is really cool.'
```
:::
::::

## Unescaping XML 

The `xml.sax.saxutils` module provides an `unescape()` function as well. This function converts the `&amp;`, `&gt;`, and `&lt;` entity references back to the corresponding characters:

:::: 
::: 
``` 
   1 >>> from xml.sax.saxutils import unescape
   2 >>>
   3 >>> unescape("&lt; &amp; &gt;")
   4 '< & >'
```
:::
::::

Note that the predefined entities `&apos;` and `&quot;` are not supported by default. Like the `escape()` and `quoteattr()` functions, `unescape()` can be provided with an additional mapping of replacements that should be performed. This can be used to add support for the additional predefined entities:

:::: 
::: 
``` 
   1 >>> unescape("&apos; &quot;", {"&apos;": "'", "&quot;": '"'})
   2 '\' "'
```
:::
::::

This can also be used to perform replacements for longer strings.

Note that the `unescape()` function does not deal with arbitrary character references. This could be accomplished by passing in a really large mapping as the second argument, but that\'s pretty silly given the size of the mapping that\'s required to support both decimal and hexadecimal character references (and the hexadecimal references containing A-F would need to be accounted for in all permutations of upper and lower case, and leading zeros would need to be considered). If we want character references to be considered, we can use the Expat XML parser included with all recent versions of Python. This function will do the trick:

:::: 
::: 
``` 
   1 import xml.parsers.expat
   2 
   3 def unescape(s):
   4     want_unicode = False
   5     if isinstance(s, unicode):
   6         s = s.encode("utf-8")
   7         want_unicode = True
   8 
   9     # the rest of this assumes that `s` is UTF-8
  10     list = []
  11 
  12     # create and initialize a parser object
  13     p = xml.parsers.expat.ParserCreate("utf-8")
  14     p.buffer_text = True
  15     p.returns_unicode = want_unicode
  16     p.CharacterDataHandler = list.append
  17 
  18     # parse the data wrapped in a dummy element
  19     # (needed so the "document" is well-formed)
  20     p.Parse("<e>", 0)
  21     p.Parse(s, 0)
  22     p.Parse("</e>", 1)
  23 
  24     # join the extracted strings and return
  25     es = ""
  26     if want_unicode:
  27         es = u""
  28     return es.join(list)
```
:::
::::

Note the extra work we have to go to so that the result has the same type as the input; this came for free with the `.replace()`-based approaches.

Using this `unescape()` function provides support for character references and the predefined entities, but does not let us extend the mapping with additional entity definitions (a more elaborate function could make that possible, though). Assuming we\'ve imported this from whatever module we stored it in, we get:

:::: 
::: 
``` 
   1 >>> unescape("abc")
   2 'abc'
   3 >>> unescape(u"abc")
   4 u'abc'
   5 >>> unescape("&#x61;&#98;&#x63;")
   6 'abc'
```
:::
::::

We also get support for constructs that we might not want in some contexts, though these are probably acceptable since we\'re looking at XML data:

:::: 
::: 
``` 
   1 >>> unescape("a<![CDATA[b]]>c")
   2 'abc'
   3 >>> unescape("a<!--wow!-->bc<!--this is really long-->")
   4 'abc'
```
:::
::::

## See Also 

- [EscapingHtml](EscapingHtml)
