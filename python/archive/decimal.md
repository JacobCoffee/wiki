# decimal

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

------------------------------------------------------------------------

    r""" bsce.py

    Show that the Python decimal module understands computer engineering notation,
    in contrast with the Python math module that understands scientific notation.

    Thus help Python newbies unfamiliar with __future__, with, decimal 0 +, etc.

    >>> est(0)
    '0'
    >>> est(100)
    '100'
    >>> est(12300)
    '12.3e+3'
    >>> est(12345)
    '~12.3e+3'
    >>> est(987654321)
    '~988e+6'
    >>> est(987654321, 6)
    '~987.654e+6'
    >>> est(2 ** 40)
    '~1.10e+12'
    >>>

    >>> estsci(12300)
    '1.23e+4'
    >>> estsci(987654321)
    '~9.88e+8'
    >>> estsci(987654321, 6)
    '~9.87654e+8'
    >>>

    See also: http://www.google.com/search?q=python+notation+engineering+scientific
    See also: http://www.etsimo.uniovi.es/python/pycon/2005/papers/24/
    See also: http://docs.python.org/lib/module-decimal.html
    """

    from __future__ import with_statement

    import decimal
    import math

    def est(count, prec = 3):

            """ Return the count or an approximately equal value in engr. notation. """

            with decimal.localcontext(decimal.Context(prec = prec)):
                    eng = (0 + decimal.Decimal(count)).to_eng_string().lower()
                    est = eng if count == int(float(eng)) else '~' + eng
                    return est

    def estsci(count, prec = 3):

            """ Return the count or an approximately equal value in sci. notation. """

            exp = int(math.log(count, 10))
            sci = ('%.' + str(prec - 1) + 'fe+%d') % (count / (10.0 ** exp), exp)
            est = sci if count == int(float(sci)) else '~' + sci
            return est

    if __name__ == '__main__':

            import doctest

            (failings, testings) = doctest.testmod(optionflags = doctest.ELLIPSIS)

------------------------------------------------------------------------

[CategoryFaq](CategoryFaq)
