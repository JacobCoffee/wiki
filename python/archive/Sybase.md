# Sybase

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

Sybase was acquired by SAP in 2010. The products below are now available as SAP products.

Note that there are *Sybase ASE* and *Sybase SQL Anywhere* systems. Those two are completely different database engines.

------------------------------------------------------------------------

# SAP Sybase ASE (Adaptive Server Enterprise) 

URL

:   [http://www.sap.com/pc/tech/database/software/adaptive-server-enterprise/index.html](http://www.sap.com/pc/tech/database/software/adaptive-server-enterprise/index.html)

licence
:   Commercial

platforms
:   Unix, Linux, Windows

# SAP Sybase ODBC drivers for Python 

URL

:   [https://www.devart.com/odbc/ase/download.html](https://www.devart.com/odbc/ase/download.html)

licence
:   Commercial

platforms
:   Mac OS X, Linux, Windows

Python versions
:   from 2.4 till the latest

[Sybase ODBC driver](https://www.devart.com/odbc/ase/) for Python is a connectivity solution which connects Python with SAP Adaptive Server Enterprise databases.

## DB API 2.0 Drivers 

### python-sybase

URL

:   [http://python-sybase.sourceforge.net/](http://python-sybase.sourceforge.net/)

Licence

:   

Platforms

:   

Python versions

:   

The older versions of this driver are available at [http://www.object-craft.com.au/projects/sybase/](http://www.object-craft.com.au/projects/sybase/).

### mxODBC 

URL

:   [http://www.egenix.com/products/python/mxODBC/](http://www.egenix.com/products/python/mxODBC/)

Licence
:   eGenix Commercial License

Platforms
:   Windows, Linux, MacOS X, FreeBSD, Solaris, AIX

Python versions
:   2.4 - 2.7

mxODBC is compatible with the Sybase ASE ODBC drivers on Windows and Unix.

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

mxODBC Connect Server is compatible with the Sybase ASE ODBC drivers.

------------------------------------------------------------------------

# SAP Sybase SQL Anywhere 

URL

:   [http://www.sap.com/pc/tech/database/software/sybase-sql-anywhere/index.html](http://www.sap.com/pc/tech/database/software/sybase-sql-anywhere/index.html)

licence
:   Commercial

platforms
:   Unix, Linux, Windows, MacOS X

## DB API 2.0 Drivers 

### mxODBC 

URL

:   [http://www.egenix.com/products/python/mxODBC/](http://www.egenix.com/products/python/mxODBC/)

Licence
:   eGenix Commercial License

Platforms
:   Windows, Linux, MacOS X, FreeBSD, Solaris, AIX

Python versions
:   2.4 - 2.7

mxODBC is compatible with the Sybase ASE ODBC drivers on Windows and Unix.

### sqlanydb

URL

:   [https://github.com/sqlanywhere/sqlanydb](https://github.com/sqlanywhere/sqlanydb)

Licence
:   Apache License 2.0

Platforms
:   Unix, Linux, Windows, MacOS X

Python versions
:   2.4 or newer with ctypes module

This a Google Code project providing a python interface to the SQL Anywhere Database.

## Supported Python Applications 

### Django 

URL

:   [https://github.com/sqlanywhere/sqlany-django](https://github.com/sqlanywhere/sqlany-django)

Licence
:   New BSD

Platforms
:   SQL Anywhere 11.0.1, Django 1.0.2 or 1.1

Python versions
:   2.4 - 2.6

This is a Google Code project allowing SQL Anywhere to be used as a backend database for the Django web framework.

## Pros 

## Cons 
