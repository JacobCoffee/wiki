# KirbyBase

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

## Masthead 

URL

:   [http://www.netpromi.com/kirbybase_python.html](http://www.netpromi.com/kirbybase_python.html)

licence
:   python or bsd style

platforms
:   anywhere python runs

## Pros 

kirbybase is a pure-python, flat-file, plain-text database management system. It can be used either embedded in a python application or in a client/server, multi-user mode. You can use python expressions/regular expressions in your query statement rather than having to use another language in your code such as sql. It is small and very easy to install (1 file). It understands python field types and lets you store your data in: strings, integers, floats, booleans, and datetime.date/datetime.datetime formats.

## Cons 

It does not support joins, referential integrity, indexes, triggers, transactions, and some of the other things you will find in other databases. Performance on very large tables will suffer. Python 2.6 breaks the \"select\" function, and further development appears to have ceased in 2006.
