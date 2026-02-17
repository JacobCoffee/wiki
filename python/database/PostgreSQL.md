# PostgreSQL

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# PostgreSQL 

URL

:   [http://www.postgresql.org/](http://www.postgresql.org/)

licence
:   BSD

platforms

:   Unix, win32 ([NT-based Microsoft operating system](http://www.postgresql.org/docs/faqs.FAQ_MINGW.html))

## Pros 

From the [features page](http://www.postgresql.org/about/):

- Good compliance with SQL standards
- Supports many SQL features
  - Foreign keys
  - Implements all SQL99 join types: inner join, left, right, full outer join, natural join
  - Subqueries
  - UNION and UNION ALL, INTERSECT and EXCEPT
  - Views
  - Triggers
- Support for international character sets, multibyte character encodings, Unicode
- Supports many languages for writing server-side functions/procedures and aggregates: Python, C, Perl, Tcl, PL/PgSQL, \...
- ACID compliant
- Support for rollback
- Serializable transaction isolation
- Multi-Version Concurrency Control (MVCC) for highly scalable concurrent applications

## Cons 

- \[To be written\]

## DB API 2.0 Drivers 

### psycopg2

URL

:   [http://initd.org/psycopg/](http://initd.org/psycopg/)

Licence
:   LGPL

Platforms
:   Unix, win32

Python versions
:   2.4, 2.5, 2.6, 2.7, 3.1, 3.2

Maintenance
:   Active development

Psycopg is the most popular PostgreSQL adapter for the Python programming language. At its core it fully implements the Python DB API 2.0 specifications. Several extensions allow access to many of the features offered by PostgreSQL.

Extended documentation available on [http://initd.org/psycopg/docs/](http://initd.org/psycopg/docs/)

### PyGreSQL 

URL

:   [http://www.pygresql.org/](http://www.pygresql.org/)

licence
:   BSD-like

platforms
:   Unix, win32

Python versions
:   2.6 thru 3.5

Maintenance
:   Last version released is 5.0 (2016-03-20)

### pyPgSQL 

URL

:   [http://pypgsql.sourceforge.net](http://pypgsql.sourceforge.net)

Licence
:   BSD-like (depends on mxDateTime, which may be GPL-incompatible)

Platforms
:   Unix, win32

Python versions
:   2.1 thru 2.3

Maintenance
:   Active, sporatic (as of 10/2003)

#### Extensions to DB API 

- The fetch methods on cursors return an instances of [PgResultSet](./PgResultSet.html), which you can use to access rows by index (like in DB-API), dictionary-like or with attributes. This feature can be turned off for a slight performance boost.

- Support for PostgreSQL notifications in the low-level API.

### mxODBC 

URL

:   [http://www.egenix.com/products/python/mxODBC/](http://www.egenix.com/products/python/mxODBC/)

Licence
:   eGenix Commercial License

Platforms
:   Windows, Linux, MacOS X, FreeBSD, Solaris, AIX

Python versions
:   2.4 - 2.7

mxODBC is compatible with the [PostgreSQL ODBC driver](http://www.postgresql.org/ftp/odbc/versions/) on Windows and Unix.

Note that you have to enable the advanced option \"Use bytea for lo\" in case you want to work with BLOBs.

### pyodbc

URL

:   [https://github.com/mkleehammer/pyodbc](https://github.com/mkleehammer/pyodbc)

License
:   MIT

Platforms
:   Windows, Linux, MacOS X, FreeBSD, Solaris, Any (source provided)

Python versions
:   2.4 - 2.6

Actively maintained Open Source project.

Precompiled binaries are available for Windows. RedHat Enterprise Linux, Centos, and Fedora have precompiled RPMs available in their Extras repositories.

### py-postgresql

URL

:   [http://python.projects.postgresql.org](http://python.projects.postgresql.org)

License
:   BSD/MIT/PSF

Platforms
:   Any (windows installers available)

Python version
:   3.x

Maintenance
:   Active development

#### Comments 

Python 3 port of pg_proboscis and friends. Pure Python with C optimizations. Prepared statement driven APIs, PG-API.(DB-API is there as well).

Written with efficiency and flexibility in mind. Data is streamed in when requested to do so, and always is streamed in under DB-API.

### txpostgres

URL

:   [https://launchpad.net/txpostgres/](https://launchpad.net/txpostgres/)

License
:   MIT/X/Expat

Platforms
:   Any

A Twisted wrapper for asynchronous PostgreSQL connections.

Uses psycopg2, which exposes the async interfaces of the native PostgreSQL library, libpq.

Can be used as a drop-in replacement for Twisted\'s adbapi module when working with PostgreSQL. The only part that does not provide 100% compatibility is connection pooling, although pooling provided by txpostgres is very similar to the one Twisted adbapi offers.

### pg8000

URL

:   [https://github.com/tlocke/pg8000](https://github.com/tlocke/pg8000)

License
:   BSD

Platforms
:   Any

Python version
:   3.6+

pg8000 is somewhat distinctive in that it is written entirely in Python.

### PyPyODBC (Pure Python ODBC) 

URL

:   [https://github.com/jiangwen365/pypyodbc](https://github.com/jiangwen365/pypyodbc)

License
:   MIT

Platforms
:   Windows, Linux

Python versions
:   2.4 - 3.3

One pure Python script, runs on CPython / [IronPython](IronPython) / [PyPy](PyPy) , Version 3.3 / 3.2 / 3.1 / 2.4 / 2.5 / 2.6 / 2.7 , Win / Linux , 32 / 64 bit.

Almost totally same usage as pyodbc ( can be seen as a re-implementation of pyodbc in pure Python ).

Simple - the whole module is implemented in a single python script with less than 3000 lines.

### mxODBC Connect 

URL

:   [http://www.egenix.com/products/python/mxODBCConnect/](http://www.egenix.com/products/python/mxODBCConnect/)

License
:   eGenix Commercial License 1.3.0

Platforms
:   Client: all Python platforms; Server: Windows, Linux

Python versions
:   2.5 - 2.7

mxODBC Connect is a commercial client-server product that allows connecting Python to ODBC compatible databases running on remote servers without requiring an ODBC driver on the client side. The product uses mxODBC on the server side and provides a highly portable Python library for the client side. As such it supports all database backend that mxODBC supports, but allows connecting to these from many different Python-supported platforms.

mxODBC Connect supports asynchronous query execution via the popular [gevent package](http://www.gevent.org/), provides secure certificate based authentication, SSL encrypted database connections, comes with full support for stored procedures, multiple result sets, Unicode, a common interface on all platforms and implements [many other useful features](http://www.egenix.com/products/python/mxODBCConnect/#Features).

mxODBC Connect Server is compatible with the [PostgreSQL ODBC drivers](http://www.postgresql.org/ftp/odbc/versions/).

### Other Python Interfaces for PostgreSQL 

These entries still need to be updated to the standard format (see above):

- [PoPy](./PoPy.html): [http://sourceforge.net/projects/popy](http://sourceforge.net/projects/popy)

  - No activity since 2003

- pgasync: [http://jamwt.com/pgasync/](http://jamwt.com/pgasync/)

  - Asynchronous and pure Python. Speed comparable to C bindings. Special support for Twisted.

- bpgsql: [http://barryp.org/software/bpgsql/](http://barryp.org/software/bpgsql/)

  - Barebones pure-Python PostgreSQL client

- [sipPQ](sipPQ)

------------------------------------------------------------------------

## Supported Python Applications 

- [Zope](Zope)

- [DbDoc](./DbDoc.html)

- three PostgreSQL drivers (using pgdb, included with the PostgreSQL distro, pypgsql, and psycopg) exist for [PyDO](PyDO) (Python Data Objects)
