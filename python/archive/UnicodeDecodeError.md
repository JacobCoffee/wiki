# UnicodeDecodeError

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

The `UnicodeDecodeError` normally happens when decoding an `str` string from a certain coding. Since codings map only a limited number of `str` strings to `unicode` characters, an illegal sequence of `str` characters will cause the coding-specific `decode()` to fail.

    Decoding from str to unicode.

    >>> "a".decode("utf-8")
    u'a'
    >>> "\x81".decode("utf-8")
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
      File "encodings/utf_8.py", line 16, in decode
    UnicodeDecodeError: 'utf8' codec can't decode byte 0x81 in position 0: unexpected code byte

    >>> "a\x81b".decode("utf-8", "replace")
    u'a\ufffdb'

Paradoxically, a `UnicodeDecodeError` may happen when \_encoding\_. The cause of it seems to be the coding-specific `encode()` functions that normally expect a parameter of type `unicode`. It appears that on seeing an `str` parameter, the `encode()` functions \"up-convert\" it into `unicode` before converting to their own coding. It also appears that such \"up-conversion\" makes no assumption of `str` parameter\'s coding, choosing a default `ascii` decoder. Hence a decoding failure inside an encoder.

Unlike a similar case with [UnicodeEncodeError](UnicodeEncodeError), such a failure cannot be always avoided. This is because the `str` result of `encode()` must be a legal coding-specific sequence. However, a more flexible treatment of the unexpected `str` argument type might first validate the `str` argument by decoding it, then return it unmodified if the validation was successful. As of Python2.5, this is not implemented.

Alternatively, a [TypeError](TypeError) exception could always be thrown on receiving an `str` argument in `encode()` functions. (This would require [StreamWriter](StreamWriter)`.write()` to accept only `unicode`. The underlying stream\'s `.write()` will receive only `str`\'s).

    Encoding from unicode to str.

    >>> u"a".encode("utf-8")
    'a'
    >>> u"\u0411".encode("utf-8")
    '\xd0\x91'
    >>> "a".encode("utf-8")         # Unexpected argument type.
    'a'
    >>> "\xd0\x91".encode("utf-8")  # Unexpected argument type.
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    UnicodeDecodeError: 'ascii' codec can't decode byte 0xd0 in position 0: ordinal not in range(128)

Python 3000 will prohibit encoding of bytes, according to PEP [3137](http://www.python.org/dev/peps/pep-3137 "PEP"): *\"encoding always takes a Unicode string and returns a bytes sequence, and decoding always takes a bytes sequence and returns a Unicode string\"*.

------------------------------------------------------------------------

[CategoryUnicode](CategoryUnicode)
