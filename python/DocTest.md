# doctest

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

------------------------------------------------------------------------

    r""" halt-at-nth-failure.py

    See here a concise way to harness doctest to HALT_AT_NTH_FAILURE,
    even though that's not yet a doc'ed option like REPORT_ONLY_FIRST_FAILURE.

    See also: http://docs.python.org/lib/module-doctest.html

    Sorry you'll have to work harder if you need to doctest code
    that uses more than the write method of sys.stdout.

    An example of an illuminating result:

    $ python ./halt-at-nth-failure.py
    1
    **********************************************************************
    File "./halt-at-nth-failure.py", line 47, in __main__
    Failed example:
        0 + 1
    Expected:
        111
    Got:
        1
    2
    3
    **********************************************************************
    File "./halt-at-nth-failure.py", line 57, in __main__
    Failed example:
        2 + 1
    Expected:
        333
    Got:
        3
    **********************************************************************
    1 item interrupted
    ***Test Failed***
    $

    appears when this source file contains such input as:

    >>> import sys

    >>> print 'Hello, doctest world.'
    Hello, doctest world.
    >>>

    >>> print >>sys.stderr, 1
    >>> 0 + 1
    111
    >>>

    >>> print >>sys.stderr, 2
    >>> 1 + 1
    2
    >>>

    >>> print >>sys.stderr, 3
    >>> 2 + 1
    333
    >>>

    >>> print >>sys.stderr, 4
    >>> 3 + 1
    444
    >>>

    """

    import sys

    class DocTestExit(KeyboardInterrupt):

            """
            Write out the bytes passed to self.write.
            Raise self after self.write called to write the trigger the nth time.
            Derive self from KeyboardInterrupt to exit doctest when raised.
            Count each call containing the trigger, not all exact matches.
            """

            def __init__(self,
                    out,
                    nth = 1,
                    trigger = '\nFailed example:\n'
            ):

                    self.triggerings = nth # -1 == don't halt
                    self.out = out
                    self.trigger = trigger

                    self.write = self.writeOut

            def writeOut(self, bytes):

                    self.out.write(bytes)

                    if 0 <= bytes.find(self.trigger):
                            self.triggerings -= 1
                            if self.triggerings == 0:
                                    raise self

    if __name__ == '__main__':

            import doctest

            (failings, testings) = (1, None)
            try:

                    sys.stdout = DocTestExit(sys.stdout, 2)
                    (failings, testings) = doctest.testmod(
                            optionflags = doctest.ELLIPSIS)
            except DocTestExit:
                    print '*' * 70
                    print '1 item interrupted'
                    print '***Test Failed***'
            finally:
                    sys.stdout = sys.stdout.out

------------------------------------------------------------------------

[CategoryFaq](CategoryFaq)
