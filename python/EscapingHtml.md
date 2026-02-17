# EscapingHtml

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# Escaping HTML 

The `cgi` module that comes with Python has an `escape()` function:

:::: 
::: 
``` 
   1 import cgi
   2 
   3 s = cgi.escape( """& < >""" )   # s = "&amp; &lt; &gt;"
```
:::
::::

However, it doesn\'t escape characters beyond `&`, `<`, and `>`. If it is used as `cgi.escape(string_to_escape, quote=True)`, it also escapes `"`.

Recent Python 3.2 have [html module](https://docs.python.org/3/library/html.html) with `html.escape()` and `html.unescape()` functions. `html.escape()` differs from `cgi.escape()` by its defaults to `quote=True`:

:::: 
::: 
``` 
   1 import html
   2 
   3 s = html.escape( """& < " ' >""" )   # s = '&amp; &lt; &quot; &#x27; &gt;'
```
:::
::::

Here\'s a small snippet that will let you escape quotes and apostrophes as well:

:::: 
::: 
``` 
   1 html_escape_table = {
   2     "&": "&amp;",
   3     '"': "&quot;",
   4     "'": "&apos;",
   5     ">": "&gt;",
   6     "<": "&lt;",
   7     }
   8 
   9 def html_escape(text):
  10     """Produce entities within text."""
  11     return "".join(html_escape_table.get(c,c) for c in text)
```
:::
::::

You can also use `escape()` from `xml.sax.saxutils` to escape html. This function should execute faster. The `unescape()` function of the same module can be passed the same arguments to decode a string.

:::: 
::: 
``` 
   1 from xml.sax.saxutils import escape, unescape
   2 # escape() and unescape() takes care of &, < and >.
   3 html_escape_table = {
   4     '"': "&quot;",
   5     "'": "&apos;"
   6 }
   7 html_unescape_table = {v:k for k, v in html_escape_table.items()}
   8 
   9 def html_escape(text):
  10     return escape(text, html_escape_table)
  11 
  12 def html_unescape(text):
  13     return unescape(text, html_unescape_table)
```
:::
::::

## Unescaping HTML 

Undoing the escaping performed by `cgi.escape()` isn\'t directly supported by the library. This can be accomplished using a fairly simple function, however:

:::: 
::: 
``` 
   1 def unescape(s):
   2     s = s.replace("&lt;", "<")
   3     s = s.replace("&gt;", ">")
   4     # this has to be last:
   5     s = s.replace("&amp;", "&")
   6     return s
```
:::
::::

or alternatively (before [issue2927](http://bugs.python.org/issue2927)):

    >>> from HTMLParser import HTMLParser
    >>> HTMLParser.unescape.__func__(HTMLParser, 'ss&copy;')
    u'ss\xa9'

Note that this will undo exactly what `cgi.escape()` does; it\'s easy to extend this to undo what the `html_escape()` function above does. Note the comment that converting the `&amp;` must be last; this avoids getting strings like `"&amp;lt;"` wrong.

This approach is simple and fairly efficient, but is limited to supporting the entities given in the list. A more thorough approach would be to perform the same processing as an HTML parser. Using the HTML parser from the standard library is a little more expensive, but many more entity replacements are supported \"out of the box.\" The table of entities which are supported can be found in the `htmlentitydefs` module from the library; this is not normally used directly, but the `htmllib` module uses it to support most common entities. It can be used very easily:

:::: 
::: 
``` 
   1 import htmllib
   2 
   3 def unescape(s):
   4     p = htmllib.HTMLParser(None)
   5     p.save_bgn()
   6     p.feed(s)
   7     return p.save_end()
```
:::
::::

This version has the additional advantage that it supports character references (things like `&#65;`) as well as entity references.

A more efficient implementation would simply parse the string for entity and character references directly (and would be a good candidate for the library, if there\'s really a need for it outside of HTML data).

## Formal htmlentitydefs 

Yet another approach available with recent Python takes advantage of htmlentitydefs:

    import re
    from htmlentitydefs import name2codepoint
    def htmlentitydecode(s):
        return re.sub('&(%s);' % '|'.join(name2codepoint),
                lambda m: unichr(name2codepoint[m.group(1)]), s)

## Builtin HTML/XML escaping via ASCII encoding 

A very easy way to transform non-ASCII characters like German umlauts or letters with accents into their HTML equivalents is simply encoding them from unicode to ASCII and use the `xmlcharrefreplace` encoding error handling:

    >>> a = u"äöüßáà"
    >>> a.encode('ascii', 'xmlcharrefreplace')
    '&#228;&#246;&#252;&#223;&#225;&#224;'

Note, that this does only transform *non*-ASCII characters and therefore leaves `<`, `>`, `?` as they are. However, you can combine this technique with the `cgi.escape`.

## See Also 

XML entities are different from, if related to, HTML entities. This page hints at the details:

- [EscapingXml](EscapingXml)

John J. Lee discusses still more refinements in implementation in [this comp.lang.python follow-up](http://groups.google.com/group/comp.lang.python/msg/ce3fc3330cbbac0a).
