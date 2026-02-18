# PythagoreanTheorem

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

    from math import hypot

    print "Pythagorean Theorem - Version 1.0"

    print

    print "What is the value of x?"

    x = float(raw_input())

    print

    print "What is the value of y?"

    y = float(raw_input())

    print

    print "The value of z is":

    print hypot(x, y)

    print

    print "Press Enter to quit."

    raw_input()
