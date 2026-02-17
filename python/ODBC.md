# ODBC

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# ODBC 

[ODBC](http://www.wikipedia.com/wiki/ODBC "WikiPedia") stands for *Open Database Connectivity*, the industry standard for database C APIs.

Most databases ship with ODBC drivers, so chances are high that you can use one of these drivers together with a Python ODBC interface to connect your Python application with any database on the market.

Since all ODBC Python interfaces need ODBC drivers to connect to the databases, we\'re hosting a [list of ODBC drivers](ODBCDrivers) on a separate page.

------------------------------------------------------------------------

## DB API 2.0 Drivers 

### mxODBC 

URL

:   [http://www.egenix.com/products/python/mxODBC/](http://www.egenix.com/products/python/mxODBC/)

License
:   eGenix Commercial License 1.3.0

Platforms
:   Windows, Unix, Mac OS X, FreeBSD, Solaris, AIX, other platforms on request

Python versions
:   2.4 - 2.7

Commercially supported fully DB-API 2.0 compliant ODBC database interface from eGenix.com; actively maintained since 1997.

mxODBC comes with full support for stored procedures, multiple result sets, Unicode, a common interface on all platforms and [many other useful features](http://www.egenix.com/products/python/mxODBC/#Features).

Supports Windows, Mac OS X, iODBC, unixODBC and DataDirect ODBC driver managers. Is known to work with these ODBC drivers: MS SQL Server Native Client, MS SQL Server ODBC Driver, FreeTDS ODBC Driver, Oracle Instant Client ODBC Driver, IBM DB2 ODBC Driver, Sybase ASE ODBC Driver, Netezza ODBC Driver, Teradata ODBC Driver, PostgreSQL ODBC Driver, MySQL ODBC Driver, .MaxDB ODBC Driver as well as the ODBC driver sets of EasySoft, DataDirect, OpenLink, Actual Technologies.

### pyodbc

URL

:   [https://github.com/mkleehammer/pyodbc](https://github.com/mkleehammer/pyodbc)

Documentation

:   [https://github.com/mkleehammer/pyodbc/wiki](https://github.com/mkleehammer/pyodbc/wiki)

License
:   MIT

Platforms
:   Windows, Linux, MacOS X, FreeBSD, Solaris, Any (source provided)

Python versions
:   2.7 - 3.6

Actively maintained Open Source project.

Precompiled binary wheels are available for Windows and macOS for Python 2.7 and 3.4+, installable using `pip install pyodbc`{.backtick}. [RedHat](RedHat) Enterprise Linux, Centos, and Fedora have precompiled RPMs available in their Extras repositories.

### turbodbc

URL

:   [https://github.com/blue-yonder/turbodbc](https://github.com/blue-yonder/turbodbc)

License
:   MIT

Platforms
:   Linux, OSX (Mac OS), Windows; all platforms 64-bit

Python versions
:   2.7, 3.4, 3.5, 3.6 (tested versions, other versions may work as well)

Actively maintained Open Source project.

Turbodbc offers turbocharged database access for data scientists. It heavily relies on buffered I/O for maximum performance, and comes with built-in (optional) [NumPy](NumPy) support.

### ceODBC 

URL

:   [http://ceodbc.sourceforge.net](http://ceodbc.sourceforge.net)

License

:   

Platforms
:   Windows

Python versions

:   

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

For ODBC drivers supported on the server side, please see the mxODBC entry.

### ODBTPAPI 

URL

:   [http://benjiyork.com/odbtp.html](http://benjiyork.com/odbtp.html)

License

:   

Platforms

:   

Python versions

:   

### PyPyODBC (Pure Python) 

URL

:   [https://github.com/jiangwen365/pypyodbc](https://github.com/jiangwen365/pypyodbc)

License
:   MIT

Platforms
:   Windows, Linux

Python versions
:   2.4 - 3.3

[A Hello World script of pypyodbc database programing](http://code.google.com/p/pypyodbc/wiki/A_HelloWorld_sample_to_access_mssql_with_python)

[Built-in Access MDB file creation and compression functions on Windows.](http://code.google.com/p/pypyodbc/wiki/pypyodbc_for_access_mdb_file)

[A DBI 2.0 SQLAlchemy enabler driver for IronPython](http://code.google.com/p/pypyodbc/wiki/Enable_SQLAlchemy_on_IronPython) [And PyPy](https://code.google.com/p/pypyodbc/wiki/Enable_SQLAlchemy_on_PyPy)

One pure Python script, runs on CPython / [IronPython](IronPython) / [PyPy](PyPy) , Version 2.4 / 2.5 / 2.6 / 2.7 / 3.2 / 3.3, Win / Linux , 32 / 64 bit.

Almost totally same usage as pyodbc ( can be seen as a re-implementation of pyodbc in pure Python ).

Simple - the whole module is implemented in a single python script with less than 3000 lines.

------------------------------------------------------------------------

## DB API 1.0 Drivers 

### win32 odbc module (part of pywin32 package) 

URL

:   [http://python.net/crew/mhammond/win32/](http://python.net/crew/mhammond/win32/)

License
:   PSF and others

platforms
:   Windows

Python versions
:   2.3 - 3.2

This interface is rather old, mostly unmaintained and only provides an DB-API 1.0 interface, but listed here since it started the Python DB-API specification development back in 1996.
