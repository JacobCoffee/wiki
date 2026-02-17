# MySQL

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# MySQL 

URL

:   [http://www.mysql.com/](http://www.mysql.com/)

license
:   GPLv2

platforms
:   Unix, win32, win64, MacOS X, i5/OS

## Pros 

- Easy to install and administer
- Support for many SQL Features (v5.0 and up):
  - Good compliance with SQL standards
  - Foreign Keys (using InnoDB)
  - Stored Routines
  - Views
  - Triggers
- Subqueries (as of v4.1)
- Partitioning (as of v5.1)
- ACID compliant (InnoDB and NDB storage engines)
- Character set support
- Built-in Replication
- Many administration tools from third parties
- Widely deployed
- Regarded as being fast
- Modular storage engines and interesting clustering features

## Cons 

- Early versions (v4.1 and earlier) have the reputation for only basic SQL support (entry-level SQL 92) and deviations from the standards. Many interesting features (views, triggers,..) are included in the latest version (5 and above), but are missing in prior versions. Check [SQL Modes](http://dev.mysql.com/doc/refman/5.1/en/server-sql-mode.html) for making MySQL more strict.

- Some [gotchas](http://sql-info.de/mysql/gotchas.html) for MySQL v4.1 and earlier.

------------------------------------------------------------------------

## DB API 2.0 Drivers 

### MySQL for Python 

URL

:   [http://sourceforge.net/projects/mysql-python](http://sourceforge.net/projects/mysql-python)

License
:   GNU General Public License (GPL), Python License (CNRI Python License), Zope Public License

Platforms
:   OS Independent

Python versions
:   2.3 - 2.6

PyPI

:   [https://pypi.org/project/MySQL-python/](https://pypi.org/project/MySQL-python/)

[MySQL on-line documentation, additional forums](http://dev.mysql.com/downloads/python.html) (maintainer does not currently read these)

### mysqlclient

URL

:   [https://github.com/PyMySQL/mysqlclient-python](https://github.com/PyMySQL/mysqlclient-python)

License
:   GPL

Platforms
:   OS Independent

Python versions
:   Python 2.7 and 3.4+

PyPI

:   [https://pypi.org/project/mysqlclient/](https://pypi.org/project/mysqlclient/)

mysqlclient is a fork of MySQL-python. It adds Python 3 support and fixed many bugs. It is the MySQL library that is recommended by the Django documentation.

### PyMySQL 

URL

:   [http://www.pymysql.org/](http://www.pymysql.org/)

License
:   MIT

Platforms

:   OS Independent, CPython 2.x and 3.x, [PyPy](PyPy), Jython, [IronPython](IronPython)

Python versions
:   2.4 - 3.2

PyPI

:   [https://pypi.org/project/PyMySQL/](https://pypi.org/project/PyMySQL/)

- Pure-Python focused on simplicity and compatibility
- Virtually 100% compatible with MySQLdb
- Good performance

### mxODBC 

URL

:   [http://www.egenix.com/products/python/mxODBC/](http://www.egenix.com/products/python/mxODBC/)

License
:   eGenix Commercial License

Platforms
:   Windows, Linux, MacOS X, FreeBSD, Solaris, AIX

Python versions
:   2.4 - 2.7

PyPI

:   [https://pypi.org/project/egenix-mxodbc/](https://pypi.org/project/egenix-mxodbc/)

mxODBC is compatible with the MySQL ODBC driver on Windows and Unix.

### pyodbc

URL

:   [https://github.com/mkleehammer/pyodbc](https://github.com/mkleehammer/pyodbc)

License
:   MIT

Platforms
:   Windows, Linux, MacOS X, FreeBSD, Solaris, Any (source provided)

Python versions
:   2.4+

PyPI

:   [https://pypi.org/project/pyodbc/](https://pypi.org/project/pyodbc/)

Actively maintained Open Source project.

Precompiled binaries are available for Windows. Red Hat Enterprise Linux, Centos, and Fedora have precompiled RPMs available in their Extras repositories.

### MySQL Connector/Python 

URL

:   [https://dev.mysql.com/downloads/connector/python/](https://dev.mysql.com/downloads/connector/python/)

License

:   GNU GPL v2 with [FOSS License Exception](http://www.mysql.com/about/legal/licensing/foss-exception.html)

Platforms
:   Any (presumably)

Python versions

:   v2.6, v2.7 and Python v3.1 to 3.3 (See [version overview](http://dev.mysql.com/doc/connector-python/en/connector-python-versions.html))

PyPI
:   ??

- Implements the Python DB API 2.0 (PEP 249).
- Pure Python implementation of the MySQL protocol.
- Actively developed and maintained by Oracle.
- Includes Django database backend.

### mypysql

URL

:   [http://sourceforge.net/projects/mypysql/](http://sourceforge.net/projects/mypysql/)

License
:   GNU GPL v3+

Platforms
:   Any (presumably)

Python versions
:   3

PyPI
:   ??

- This module provides (yet) incomplete PEP 249 functionality
- C implementation of MySQL database connector
- A majority of the commands are implemented
- Still experimental but actively developed

### PyPyODBC (Pure Python ODBC) 

URL

:   [https://github.com/jiangwen365/pypyodbc](https://github.com/jiangwen365/pypyodbc)

License
:   MIT

Platforms
:   Windows, Linux

Python versions
:   2.4 - 3.3

PyPI

:   [https://pypi.org/project/pypyodbc/](https://pypi.org/project/pypyodbc/)

[Run SQLAlchemy on PyPy](https://code.google.com/p/pypyodbc/wiki/Enable_SQLAlchemy_on_PyPy)

One pure Python script, runs on CPython / [IronPython](IronPython) / [PyPy](PyPy) , Version 3.3 / 3.2 / 3.1 / 2.4 / 2.5 / 2.6 / 2.7 , Win / Linux , 32 / 64 bit.

Similar usage as pyodbc ( can be seen as a re-implementation of pyodbc in pure Python ).

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

PyPI

:   [https://pypi.org/project/egenix-mxodbc-connect-client/](https://pypi.org/project/egenix-mxodbc-connect-client/)

mxODBC Connect is a commercial client-server product that allows connecting Python to ODBC compatible databases running on remote servers without requiring an ODBC driver on the client side. The product uses mxODBC on the server side and provides a highly portable Python library for the client side. As such it supports all database backend that mxODBC supports, but allows connecting to these from many different Python-supported platforms.

mxODBC Connect supports asynchronous query execution via the popular [gevent package](http://www.gevent.org/), provides secure certificate based authentication, SSL encrypted database connections, comes with full support for stored procedures, multiple result sets, Unicode, a common interface on all platforms and implements [many other useful features](http://www.egenix.com/products/python/mxODBCConnect/#Features).

mxODBC Connect Server is compatible with the MySQL ODBC drivers.

------------------------------------------------------------------------

## Supported Python Applications 

- [Zope](Zope)

- A MySQL driver exists for [PyDO](PyDO) (Python Data Objects)
