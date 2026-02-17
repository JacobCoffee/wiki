# Oracle

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# Oracle 

URL

:   [http://www.oracle.com/index.html](http://www.oracle.com/index.html)

FAQ

:   [http://www.orafaq.com/](http://www.orafaq.com/)

Wiki

:   [http://www.orawiki.com/](http://www.orawiki.com/)

Wikipedia

:   [http://en.wikipedia.org/wiki/Oracle_database](http://en.wikipedia.org/wiki/Oracle_database)

license

:   commercial/proprietary; free for development from [Oracle Technology Network](http://www.oracle.com/technology//index.html); [Oracle XE](http://www.oracle.com/technology/software/products/database/xe/index.html) is free for production and development (and an excellent option all-around)

platforms
:   Unix, Linux, win32, win64

## Pros 

- Reputation for being capable of handling large scale databases
- Typically the database system others compare themselves to

## Cons 

- Usually requires bloated Oracle client installation on any machine that the app will run on
- Frequently the subject of migration discussions (to alternatives), usually for reasons of cost

------------------------------------------------------------------------

## DB API 2.0 Drivers 

### cx_Oracle 

URL

:   [http://cx-oracle.sourceforge.net/](http://cx-oracle.sourceforge.net/)

licence

:   [BSD like](http://cx-oracle.sourceforge.net/LICENSE.txt)

platforms
:   Unix, win32

Python versions
:   2.5 - 3.2

Oracle versions
:   10i - 11g

Last release
:   5.1 (March 19, 2011)

### DCOracle2 

URL

:   [http://www.zope.org/Members/matt/dco2](http://www.zope.org/Members/matt/dco2)

licence
:   ZPL

platforms
:   Unix, win32

Python versions

:   

Last release
:   1.3beta (Feb 10, 2003)

DCOracle2 targets Oracle 8i and up.

There also is DCOracle ([http://www.zope.org/Products/DCOracle/](http://www.zope.org/Products/DCOracle/)) for the older Oracle 7 and 8 versions, but this is unmaintained.

### mxODBC 

URL

:   [http://www.egenix.com/products/python/mxODBC/](http://www.egenix.com/products/python/mxODBC/)

Licence
:   eGenix Commercial License

Platforms
:   Windows, Linux, MacOS X, FreeBSD, Solaris, AIX

Python versions
:   2.4 - 2.7

mxODBC is compatible with the Oracle ODBC drivers on Windows and Unix, such as the ones included in the [Oracle Instant Client](http://www.oracle.com/technology/tech/oci/instantclient/index.html).

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

### OJDBC and JayDeBeApi 

URL

:   [http://pypi.python.org/pypi/JayDeBeApi](http://pypi.python.org/pypi/JayDeBeApi)

licence
:   LGPL

platforms
:   Any (requires Java)

Python versions
:   Tested on CPython 2.6.6 and Jython 2.5.2

Oracle versions
:   Any supported by Oracle\'s JDBC drivers (currently 8.1.7 to 11.2.0.2.0)

Last release
:   0.1 (2010-08-16)

No [InstantClient](./InstantClient.html) required. Download an Oracle JDBC driver (the filename will be something like ojdbc6.jar) from the [Oracle website](http://www.oracle.com/technetwork/database/features/jdbc/index-091264.html), and set the classpath to include the driver. Note that if not running under Jython, JPype is required. Use code like the following:

:::: 
::: 
``` 
   1 environ['JAVA_HOME'] = '/usr/lib/jvm/java-6-openjdk/jre'
   2 jpype.startJVM(jpype.getDefaultJVMPath(), '-Djava.class.path=ojdbc6.jar')
   3 conn = jaydebeapi.connect('oracle.jdbc.driver.OracleDriver', 'jdbc:oracle:thin:user/pass@server:1521:dbname')
```
:::
::::

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

mxODBC Connect Server is compatible with the [Oracle Instant Client](http://www.oracle.com/technology/tech/oci/instantclient/index.html) ODBC drivers.

------------------------------------------------------------------------

## Supported Python Applications 

- [Zope](Zope)

- an Oracle (DCOracle and DCOracle2) driver exists for [PyDO](PyDO) (Python Data Objects)

## Web Links 

[Oracle Forum](http://www.orafaq.com/forum)

Oracle Wiki\'s: [English](http://www.orafaq.com/wiki) [German](http://www.oracle-10g.de/oracle-wiki)

Oracle Documentation: [10g](http://www.oracle-doku.de/oracle_10g_documentation/index.htm) [9i](http://www.oracle-doku.de/oracle_9i_documentation/index.htm) [8i](http://www.oracle-doku.de/oracle_8i_documentation/index.htm) [7](http://www.oracle-doku.de/oracle_7_documentation/index.htm)
