# Asking for Help/How can I add or substract two to the last digit of a float?

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# Asking for Help: How can I add or substract two to the last digit of a float? 

How can I add or substract two to the last digit of a float? Like 4.9999 should be 5.0001 or 4.9997. The problem is

    >>> 4.9999
    4.9999000000000002
    would yield 4.9999000000000000 or 4.9999000000000004 which is not right.
    I could make a str(4.9999), convert each character to an int and work on each character from right   
    to left, but there must be a better way.
    this is not what I want as well:
    >>> ( 4.9999 * 10000 + 2 ) / 10000.0
    5.0000999999999998 -> this should be 5.0001
    this makes it somehow :))
    >>> str(( 4.9999 * 10000 + 2 ) / 10000)
    '5.0001'

Answer: [http://www.python.org/doc/current/library/decimal.html?highlight=round#decimal-faq](http://www.python.org/doc/current/library/decimal.html?highlight=round#decimal-faq)

------------------------------------------------------------------------

[CategoryAskingForHelp](CategoryAskingForHelp) [CategoryAskingForHelpAnswered](CategoryAskingForHelpAnswered)
