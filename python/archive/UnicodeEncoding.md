# UnicodeEncoding

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

Python supports several [Unicode](../archive/Unicode) encodings.

Two of the most common encodings are:

- utf-8
- utf-16

It is critical to note that **a unicode encoding is not Python unicode!**

That is, there is a critical difference between a Python \"byte string\" (or \"normal string\" or \"regular string\") that stores utf-8 / utf-16 encoded unicode, and a Python unicode string.

- `u"foo"` \-- this is a Python unicode string

- `"foo"` \-- this is a Python bytes string \-- it is 3 bytes long

- `u"foo".encode('utf-8')` \-- this *starts* as a Python unicode string, and then encodes it into utf-8, stored in a normal Python bytes string.

When you see a \"u\" in front of quotation marks, that means \"this is a Python unicode string.\" You should not ask yourself: \"How is it represented?\" Don\'t even think about that. Just know: \"This is pure, platonic, Unicode. Python understands the mystery of the encoding of the character.\"

How many bytes is `"foo"`? **3.** How many bytes is `u"foo"`? You do not know, you do not wonder. Only the angels in heaven know how many bytes it takes to represent platonic characters.

But if you\'re writing to a file, then you need to turn that pure platonic Unicode character into something material and chunked into bytes. Now you encode it into bytes.

:::: 
::: 
``` 
   1 pure_platonic_string = u"blah blah blah"  # This is a Unicode string
   2 byte_string = pure_platonic_string.encode("utf-8")  # Now we make it utf-8
   3 f.write(byte_string)  # We write it to a file
```
:::
::::

## See Also 

[CategoryUnicode](CategoryUnicode)

- [Wikipedia:UTF-8](http://en.wikipedia.org/wiki/UTF-8) \-- for general information

- [Wikipedia:UTF-16](http://en.wikipedia.org/wiki/UTF-16) \-- for general information
