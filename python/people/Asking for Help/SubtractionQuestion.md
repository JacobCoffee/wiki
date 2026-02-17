# Asking for Help/SubtractionQuestion

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

I discovered this when my students were creating a fraction class. 7/4 = 1 however -7/4 = -2 It seems to me the second result should be -1 It appears it is using the floor function but it isn\'t what my students wanted nor can I think of when anyone would want this result. Anyone know why? Thanks for any help Terry S - [tscott@fisher.unco.edu](mailto:tscott@fisher.unco.edu)

------------------------------------------------------------------------

That is what floor division does, it reduces the value to the next lowest whole number. If you want to separate the whole number and fractional part, use math.modf:

    from __future__ import division
    import math
    print math.modf(25/12)
    --> (0.08333, 2.0)
    print math.modf(-25/12)
    --> (-0.08333, -2.0)

    #to just print the whole number as an int:
    print int(math.modf(25/12)[1])

------------------------------------------------------------------------

Please see the Python Programming FAQ, [question 1.3.2](http://www.python.org/doc/faq/programming.html#why-does-22-10-return-3), for an explanation.

------------------------------------------------------------------------

[CategoryAskingForHelp](CategoryAskingForHelp) [CategoryAskingForHelpAnswered](CategoryAskingForHelpAnswered)
