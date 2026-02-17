# DbApi3

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

This page should summarize topics for the DB API 3.0. It is meant to provide

- clarifications of the DB API 2.0
- new optional features
- new recommendations

A related page is [ExtendingTheDbApi](ExtendingTheDbApi), which lists features that aren\'t general enough to make it into the spec.

Discussions should be held at [db-sig@python.org](mailto:db-sig@python.org), with summaries (even preliminary ones) entered here. This is also the place where limits imposed by the underlying database/library implementation should be entered for further reference. It could also be used as a place for technical voting by the driver authors (with tags like \'personal preference\', \'trivial to implement\', \'difficult to implement\', \'implementable only with loss of performance\' etc.)

# Prior Art 

- Stuart Bishop posted a DB-API 3.0 strawman in 2001, which can be found on the [Aug2001DbApi3Strawman](Aug2001DbApi3Strawman) page.

# Unified Parameter Style 

Possibilities

- currently: one parameter style per driver
- one parameter style for all drivers
- multiple parameter styles per driver, switchable per Connection, Cursor or .execute ()

## Pros 

- Programs can be written more portable as they don\'t have to distinguish between
  - different placeholders
  - different calling conventions (sequence vs. mapping)
- A well-chosen placeholder symbol would eliminate confusion between SQL parameter passing and Python string substitution

## Cons 

- possible loss of functionality (qmark, numeric, format can\'t support call with mapping)
- loss of performance, because the SQL would have to be tokenized unless the driver/database supports the style natively
- subtle errors, because tokenizing SQL is hard and error prone

## Possible Compromises 

- multiple parameter styles per driver
  - the native style: fast and secure
  - the standard style: possible slow, possible tokenizing bugs

- a standard module for SQL tokenizing
  - see [sqlliterals](http://www.python.org/pypi/sqlliterals) for some tokenisers

- using pyformat, with strings of the form %(identifier)s explicitly forbidden in SQL literals. *Easy to implement and the error situations are clearly defined, in contrast to a real tokenizer, where the error situations are more subtle*

- adoption of a slightly restricted SQL dialect for the standard style: this would involve ? (or another acceptable symbol) being used unconditionally as a placeholder, literal values would be discouraged in the SQL text (which may be the only part of SQL where ? would appear, at least)

## Ease of Implementation 

Driver authors should list with each style how easy they could be implemented. \'Native\' means that the SQL can be passed directly to the database, \'tokenize\' means that the driver would have to tokenize the SQL. \'tokenize, already implemented\' if the current driver tokenizes the SQL already in the current implementation.

Because it\'s mostly a feature of the database where some style is native, this should list the database name. If it a driver specic decision, then the driver name should be listed.

### qmark: WHERE a = ? 

native
:   mxODBC, JDBC, SAP DB, SQLite

tokenize

:   

### numeric: WHERE a = :1 

Is this useful at all? If Oracle uses them simply as an indicator of \'pass by position\' without regard to the actual numbers, then this style is confusing at best.

native
:   SAP DB

tokenize
:   mxODBC, JDBC

### named: WHERE a = :value 

native
:   Oracle, SAP DB (positional args, support for mappings could be implemented in the kernel), SQLite

tokenize
:   mxODBC, JDBC Remark: On M\$ SQL Server they use \@value, so there should be a way to know which character is used as prefix to value ( \'@\' instead of \':\' ).

### format: WHERE a = %s 

native

:   

tokenize
:   mxODBC, JDBC, SAP DB

### pyformat: WHERE a = %(value)s 

native
:   psycopg, psycopg2

tokenize
:   mxODBC, JDBC, SAP DB

## Preliminary Consensus 

- Every module implements at least \'qmark\' and \'named\' parameter styles. Additional parameter styles are allowed for backwards compatibility.

- Connection and cursor objects gain a writable \'paramstyle\' attribute for selecting the active parameter style. The default parameter style for a connection is implementation-defined. The default parameter style for a cursor is inherited from the connection at the time the cursor is created.

- Possible settings for the writable paramstyle are implementation-defined but must include at least \'qmark\' and \'named\'. Attempting to set an illegal paramstyle will raise a [ValueError](./ValueError.html).

# Additional Driver Objects 

Prepared statements in addition to Connection and Cursor. Related is the idea of statement caching:

- Cursor object as a prepapared statement
- Cursor object accesses a pool of cached prepared statements

# Parameter Passing 

`cursor.execute ("SELECT where size = :size", {'size': localvar})` vs.`cursor.execute ("SELECT where size = :size", size = localvar)`

`cursor.execute ("SELECT where size = ?", [localvar])` vs. `cursor.execute ("SELECT where size = ?", localvar)`

- Should the argument passing be driver dependent, should there be additional methods, should only one be allowed?

# Refined transaction model 

Currently, DB-API 2.0 loosely defines transactions at the level of a connection. However, many drivers provide extensions that allow multiple (distinct, nested, or both) transactions to exist on a given connection. Maybe it is time for a next generation DB-API to better formalize the transactional scope of a connection. Backends and drivers that wish to allow multiple concurrent transactions will have to implement a simple connection pool so that the same physical connection can be shared by multiple logical DB-API connection objects. Of course, this alters the concept of a connection and may require even more infrastructure to support. i.e., a developer could request an unshared connection so that global (physical) connection variables can be changed in isolation.

Also, some thought should be directed towards properly handling the semantics of nested transactions, as more and more backends are now supporting them.

# Schema Information 

# Role of the DB API spec 

- programs should be completely portable, including the SQL
- programs should be portable at the API level
- it should be possible to write portable programs, but extensions are allowed
- why bother, real apps write their own higher level API

# Common Modules 

- unit tests

------------------------------------------------------------------------

[CategoryDatabase](./CategoryDatabase.html)
