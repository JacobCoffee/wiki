# SliceOverNegatives

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

How slice works:

    >>> a = list(range(10))
    >>> a[1:3]
    [1, 2]
    >>> a[1:-1]
    [1, 2, 3, 4, 5, 6, 7, 8]

    How slice works with negative numbers when nice:
    >>> a[-5:-2]
    [5, 6, 7]
    >>> a[2:-4]
    [2, 3, 4, 5]

    How slice fails with negative numbers
    >>> a[-5:2]
    []

In fact, any attempt to slice from a negative to a positive returns nothing. My expectation as a user is that it would move through the list, going over if need be. It would go from 8 to 9 to 0 to 1 to 2.

It isn\'t a problem that you run into very often. However, it counters user expectations and doesn\'t seem to provide a significant benefit. It probably wouldn\'t work as well in Python 4000 when lists start at 1, but for Python 3.4 or 3.5 it could make things simpler to understand.

\.... [SkipMontanaro](SkipMontanaro) writes \....

I believe slicing with negative indices works as expected:

    >>> x = range(10)
    >>> x[-9:9]
    [1, 2, 3, 4, 5, 6, 7, 8]

You just need to remember that a negative index means offset from the end while a positive index means offset from the start. Thus above, `-9` references offset `10-9 == 1`.
