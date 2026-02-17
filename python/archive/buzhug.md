# buzhug

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

## General Information 

URL

:   [http://buzhug.sourceforge.net](http://buzhug.sourceforge.net)

licence
:   BSD

platforms
:   all platforms supporting Python 2.3+

## Programming Model 

buzhug is a fast, portable, pure-Python database engine, using a pythonic non-SQL syntax for all operations

A database is an iterator, yielding objects with attributes matching the fields defined for the base . Requests can be expressed as list comprehensions or generator expressions, instead of SQL.

The data is stored and accessed on disk (it is not an in-memory database). The implementation has been designed to make all operations, and especially selection, as fast as possible with an interpreted language.

A limited benchmark using the same use cases as SQLite\'s author shows that buzhug is much faster than other pure-Python modules ([KirbyBase](KirbyBase), gadfly). SQLite, which is implemented in C, is faster, but only less than 3 times on the average.

## Pros 

- most operations are faster than on other pure-Python databases
- concurrency control by versioning of records
- simple system to link databases dynamically (a record of a base can be a field of another base)
- complete documentation

## Cons 

- still beta : bug reports needed
- no thread-safe feature : should be used behind an asynchronous server for multiple users
