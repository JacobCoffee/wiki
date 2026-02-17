# Teradata

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# Teradata 

## General Information 

URL

:   [http://www.teradata.com/products-and-services/Teradata-Database/](http://www.teradata.com/products-and-services/Teradata-Database/)

licence
:   proprietary

platforms
:   Linux (servers, VMs, mainframes)

## Pros 

- Big Data compatible
- Data Warehouse

## Cons 

------------------------------------------------------------------------

## DB API 2.0 Drivers 

### mxODBC 

URL

:   [http://www.egenix.com/products/python/mxODBC/](http://www.egenix.com/products/python/mxODBC/)

Licence
:   commercial

Platforms
:   Windows, Linux, Mac OS X, FreeBSD, Solaris, AIX, other platforms on request

Python versions
:   2.4 - 2.7

Commercially supported fully DB-API 2.0 compliant ODBC database interface from eGenix.com; actively maintained since 1997.

mxODBC comes with full support for stored procedures, multiple result sets, Unicode, a common interface on all platforms and [many other useful features](http://www.egenix.com/products/python/mxODBC/#Features).

mxODBC has been successfully tested with the Teradata ODBC drivers.

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

mxODBC Connect Server is compatible with the Teradata ODBC drivers.

## Other Drivers 

- N/A

------------------------------------------------------------------------

## Supported Python Applications 

- N/A
