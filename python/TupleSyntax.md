# TupleSyntax

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

Python newbies often have some confusion about how to make one-element tuples. [VenkataSubramanian](VenkataSubramanian) provided a nice summary of Python\'s tuple syntax [\[1](TupleSyntax#A1)\].

### Zero Element Tuples 

In Python, zero-element tuples look like:

    ()

In this form, unlike the other tuple forms, parentheses are the essential elements, not commas.

### One Element Tuples 

One-element tuples look like:

    1,

The essential element here is the trailing comma. As for any expression, parentheses are optional, so you may also write one-element tuples like

    (1,)

but it is the comma, not the parentheses, that define the tuple.

### Multiple Element Tuples 

In Python, multiple-element tuples look like:

    1,2,3

The essential elements are the commas between each element of the tuple. Multiple-element tuples may be written with a trailing comma, e.g.

    1,2,3,

but the trailing comma is completely optional. Just like all other expressions in Python, multiple-element tuples may be enclosed in parentheses, e.g.

    (1,2,3)
    or
    (1,2,3,)

but again, it is the commas, not the parentheses, that define the tuple.

\[1\] [http://mail.python.org/pipermail/python-list/2005-June/284208.html](http://mail.python.org/pipermail/python-list/2005-June/284208.html)
