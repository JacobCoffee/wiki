# RepresentationError

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

(Note: this information is now part of the Python tutorial for Python 2.2a0, as appendix B. A preview is here: [http://python.sourceforge.net/devel-docs/tut/node14.html](http://python.sourceforge.net/devel-docs/tut/node14.html) )

\"Representation error\" refers to that some (most, actually) decimal fractions cannot be represented exactly as binary (base 2) fractions. This is the chief reason why Python (or Perl, C, C++, Java, Fortran, \...) often won\'t display the exact decimal number you expect:

    >>> 0.1
    0.10000000000000001
    >>>

Why is that? 1/10 is not exactly representable as a binary fraction. Almost all machines today (November 2000) use IEEE-754 floating point arithmetic, and almost all platforms map Python floats to IEEE-754 \"double precision\". 754 doubles contain 53 bits of precision, so on input the computer strives to convert 0.1 to the closest fraction it can of the form `J/2**N` where `J` is an integer containing exactly 53 bits. Rewriting

        1        J
       ---  ~= ----
       10      2**N

as

             2**N
        J ~= ----
              10   

and recalling that `J` has exactly 53 bits (is \>= 2\*\*52 but \< 2\*\*53), the best value for `N` is 56:

    >>> 2L**52
    4503599627370496L
    >>> 2L**53
    9007199254740992L
    >>> 2L**56/10
    7205759403792793L
    >>> 

That is, 56 is the only value for `N` that leaves `J` with exactly 53 bits. The best possible value for J is then that quotient rounded:

    >>> q, r = divmod(2L**56, 10)
    >>> r
    6L
    >>>

Since the remainder is more than half of 10, the best approximation is obtained by rounding up:

    >>> q+1
    7205759403792794L
    >>> 

Therefore the best possible approximation to 1/10 in 754 double precision is that over 2\*\*56, or

     7205759403792794L
    ------------------
    72057594037927936L

Note that since we rounded up, this is actually a little bit larger than 1/10; if we had not rounded up, the quotient would have been a little bit smaller than 1/10. But in no case can it be *exactly* 1/10!

So the computer never \"sees\" 1/10: what it sees is the exact fraction given above, the best 754 double approximation it can get:

    >>> .1 * 2L**56
    7205759403792794.0
    >>>

If we multiply that fraction by 10L\*\*30, we can see the (truncated) value of its 30 most significant decimal digits:

    >>> 7205759403792794L * 10L**30 / 2L**56
    100000000000000005551115123125L
    >>>

meaning that the exact number stored in the computer is approximately equal to the decimal value 0.100000000000000005551115123125. Rounding that to 17 significant digits gives the 0.10000000000000001 that Python displays (well, will display on any 754-conforming platform that does best-possible input and output conversions in its C library \-- yours may not!).
