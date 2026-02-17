# BytesStr

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# Text handling in Python 3 

Python 3 uses two very different types:

- `bytes`: intended to represent raw byte data. For more information on this type, please consult [PEP 358](http://www.python.org/dev/peps/pep-0358/).

- `str`: a unicode character string

## Choosing Between \"bytes\" and \"str\" 

When choosing the type you want to use to work with text you have to ask yourself: do I manipulate characters or bytes (integers)? \"A\" is a character and 65 is an integer. Examples:

- a network socket manipulates bytes
- a text parser manipulates characters (uses lower, strip, etc. methods)

## Iterating over \"bytes\" 

It\'s important to note that the `bytes` iterator generates integers and not characters:

    >>> for item in b'abc':
    ...   print item
    97
    98
    99

## Comparing \"bytes\" 

Comparing one `bytes` object to another works as expected:

    >>> b'xyz' == b'xyz'
    True
    >>> b'xyz' == b'abc'
    False

However, it is important to note that the `bytes` type is completely distinct from the `str` type in Python 3, and comparisons between them do *not* work:

    >>> b'xyz' == 'xyz'
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    TypeError: can't compare bytes and str

This should make clearly evident some incomplete transitions. But it also means that you really can\'t mix then very well:

    >>> L = ["1", b"1"]
    >>> "1" in L
    True
    >>> "2" in L
    Traceback (most recent call last):
     File "<stdin>", line 1, in <module>
    TypeError: can't compare str and bytes

As mentioned earlier, getting an item of a bytes returns an integer, not a bytes object:

    >>> b'xyz'[0] == b'x'
    False
    >>> b'xyz'[0]
    120

### Hashing \"bytes\" 

`bytes` is mutable, and as a result, it\'s not hashable. Among other things, this means that `bytes` objects can\'t be used as keys in dictionaries.

Hacks and workarounds for this include:

- use `buffer(value)`

Other solutions include:

- create an immutable `frozenbytes` type

- avoid using hash

# Historical information 

For historical information that may be useful in porting or maintaining remaining Python 2 systems, please see [previous page revisions](https://wiki.python.org/moin/BytesStr?action=recall&rev=12).
