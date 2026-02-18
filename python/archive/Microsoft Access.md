# Microsoft Access

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# Microsoft Access mdb and accdb Database 

URL

:   [http://office.microsoft.com/en-us/access/](http://office.microsoft.com/en-us/access/)

Licence
:   Commercial/Proprietary software

Platforms
:   Windows

## Pros 

- Widely used by end users.
- It comes with the GUI tools,and very user friendly.

## Cons 

- Windows only.

------------------------------------------------------------------------

## DB API 2.0 Drivers 

### PyPyODBC （Pure Python) 

URL

:   [http://code.google.com/p/pypyodbc](http://code.google.com/p/pypyodbc)

License
:   MIT

Platforms
:   Windows, Linux

Python versions
:   2.4 - 3.4

PyPyODBC is a pure Python script module providing ODBC interfacing functions, it runs on CPython / [IronPython](../implementations/IronPython) / [PyPy](../implementations/PyPy) , Version 2.4 / 2.5 / 2.6 / 2.7 , Win / Linux , 32 / 64 bit.

However, ***on Windows Platform***, PyPyODBC also provides a set of methods bringing [PyPyODBC\'s extra support for Access on Windows Platform](https://code.google.com/p/pypyodbc/wiki/pypyodbc_for_access_mdb_file)

### mxODBC 

URL

:   [http://www.egenix.com/](http://www.egenix.com/)

License
:   eGenix.com Commercial License

Platforms
:   Windows, Unix

Python versions
:   2.4 - 2.7

On Windows, you can use mxODBC with the ODBC driver that comes with MS Access, or use the ODBC driver that comes with the [MDAC 2.8 SP1 database access package](http://www.microsoft.com/downloads/details.aspx?familyid=78CAC895-EFC2-4F8E-A9E0-3A1AFBD5922E&displaylang=en), if you don\'t have MS Access installed on the machine.

On Unix platforms, you can use one of the ODBC drivers available from commercial ODBC vendors. If you only need to query data from MS Access files, you can also have a look at the very limited ODBC driver that comes with the [MDBTools](http://mdbtools.sourceforge.net/). This works reasonably well to extract data from the MS Access files.

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

mxODBC Connect Server is compatible with the MS Access ODBC driver on Windows and allows both reading and writing to MDB/ACCDB Access files. Provided you have a Windows server available to run those drivers, you can then work with MS Access database files from any Python platform using the mxODBC Connect Client.
