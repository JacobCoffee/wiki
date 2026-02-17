# UnicodeEncodeError

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

The `UnicodeEncodeError` normally happens when encoding a `unicode` string into a certain coding. Since codings map only a limited number of `unicode` characters to `str` strings, a non-presented character will cause the coding-specific `encode()` to fail.

    Encoding from unicode to str.

    >>> u"a".encode("iso-8859-15")
    'a'
    >>> u"\u0411".encode("iso-8859-15")
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
      File "encodings/iso8859_15.py", line 12, in encode
    UnicodeEncodeError: 'charmap' codec can't encode character u'\u0411' in position 0: character maps to <undefined>

    >>> u"a\u0411b".encode("iso-8859-15", "replace")
    'a?b'
    >>> u"a\u0411b".encode("iso-8859-15", "backslashreplace")
    'a\\u0411b'
    >>> u"a\u0411b".encode("iso-8859-15", "xmlcharrefreplace")
    'a&#1041;b'

Paradoxically, a `UnicodeEncodeError` may happen when \_decoding\_. The cause of it seems to be the coding-specific `decode()` functions that normally expect a parameter of type `str`. It appears that on seeing a `unicode` parameter, the `decode()` functions \"down-convert\" it into `str`, then decode the result assuming it to be of their own coding. It also appears that the \"down-conversion\" is performed using the `ASCII` encoder. Hence an encoding failure inside a decoder.

The choice of the `ASCII` encoder for \"down-conversion\" might be considered wise because it is an intersection of all codings. The subsequent decoding may only accept a coding-specific `str`.

However, unlike a similar issue with [UnicodeDecodeError](UnicodeDecodeError) while encoding, there would be not ambiguity if `decode()` simply returned the `unicode` argument unmodified. There seems to be not such a shortcut in `decode()` functions as of Python2.5.

Alternatively, a [TypeError](TypeError) exception could always be thrown on receiving a `unicode` argument in `decode()` functions. (This would require `stream.read()` to produce only `str` for [StreamReader](StreamReader)`.read()`. The latter would only produce `unicode`).

    Decoding from str to unicode.

    >>> "a".decode("utf-8")
    u'a'
    >>> "\xd0\x91".decode("utf-8")
    u'\u0411'
    >>> u"a".decode("utf-8")      # Unexpected argument type.
    u'a'
    >>> u"\u0411".decode("utf-8") # Unexpected argument type.
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
      File "encodings/utf_8.py", line 16, in decode
    UnicodeEncodeError: 'ascii' codec can't encode character u'\u0411' in position 0: ordinal not in range(128)

Python 3000 will prohibit decoding of Unicode strings, according to PEP [3137](http://www.python.org/dev/peps/pep-3137 "PEP"): *\"encoding always takes a Unicode string and returns a bytes sequence, and decoding always takes a bytes sequence and returns a Unicode string\"*.

------------------------------------------------------------------------

[CategoryUnicode](CategoryUnicode)
