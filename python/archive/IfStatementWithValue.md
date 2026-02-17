# IfStatementWithValue

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# The Problem 

Python is sorely missing an if statement that:

- computes and takes the value of A if and only if the predicate is true
- computes and takes the value of B if and only if the predicate is false

In C and its derivitives,

    predicate ? A : B 

This is extremely useful in programming and helps avoid copy and paste assignments. This is an example of poor code, because the assignment logic \"x=\" is copied and pasted, violating the software maintainbility and readability principle of [OnceAndOnlyOnce](./OnceAndOnlyOnce.html):

    if test:
       x=sin(cos(x))
    else:
       x=cos(sin(x))

# Accepted Solution 

This is now part of Python 2.5:

    A if predicate else B

which would convert the above snippet to:

    x = sin(cos(x)) if test else cos(sin(x))

# Discussion 

Please see [http://python.org/peps/pep-0308.html](http://python.org/peps/pep-0308.html) and google for discussions about the ternary operator (if you haven\'t yet).
