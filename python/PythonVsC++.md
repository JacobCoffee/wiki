# PythonVsC++

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

No Dangling Else Trap

One additional benefit of using indentation is that the "dangling else ambiguity" is impossible in Python. For example, here is some C++ code:

- - if (x \> 0)

    - o
      - if (y \> 0)

        - \+ z = 1;

    else

    - o z = 5;

The code sets z to 1 if both x and y are greater than 0, and it looks like it will set z to 5 if x is less than or equal to 0. But in fact, it sets z to 5 only if x is greater than 0 and if y is less than or equal to 0. Here is what it means in Python:

- - if x \> 0:

    - o
      - if y \> 0:

        - \+ z = 1

        else:

        - \+ z = 5

And if we really want z set to 5 if x is less than or equal to 0, we would write this:

- - if x \> 0:

    - o
      - if y \> 0:

        - \+ z = 1

    else:

    - o z = 5

Thanks to Python's indentation-based block structure, we avoid the "dangling else" trap.
