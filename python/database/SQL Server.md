# SQL Server

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# Microsoft SQL Server 

URL

:   [http://www.microsoft.com/sql/default.mspx](http://www.microsoft.com/sql/default.mspx)

licence
:   commercial/proprietary software, although a free (gratis) edition \"SQL Server 2008 R2 Express\" is available

platforms
:   Windows 2000 and later

## Pros 

- SQL Server is a robust and fully-featured database, and it performs very well. Moreover, I have not had any problems using this database with Python.
- The SQL Server Express versions are free to download, use and can even be redistributed with products.

## Cons 

- Windows only.
- SQL Server comes in various flavours. The latest free version has a 10GB database size limit. It comes with the GUI tools and Reporting Services. The standard and other versions include many extra features.

------------------------------------------------------------------------

## DB API 2.0 Drivers 

### adodbapi

URL

:   [http://adodbapi.sourceforge.net/](http://adodbapi.sourceforge.net/)

SourceForge

:   [http://sourceforge.net/projects/adodbapi](http://sourceforge.net/projects/adodbapi)

licence
:   LGPL

platforms
:   Windows only

### pymssql

URL

:   [http://pymssql.org](http://pymssql.org)

licence
:   LGPL

platforms
:   Windows and Unix

### mssql

URL

:   [http://www.object-craft.com.au/projects/mssql/](http://www.object-craft.com.au/projects/mssql/)

licence
:   BSD

platforms
:   Windows

### mxODBC 

URL

:   [http://www.egenix.com/](http://www.egenix.com/)

License
:   eGenix.com Commercial License

Platforms
:   Windows, Unix, Mac OS X, FreeBSD, Solaris, AIX, other platforms on request

Python versions
:   2.4 - 2.7

mxODBC requires an ODBC driver to talk to SQL Server. On Windows, you can use the [MS SQL Server Native Client ODBC driver for Windows](http://msdn.microsoft.com/en-us/library/jj991993.aspx), on the other platforms, there are several commercial ODBC high quality drivers available, an open-source [http://www.freetds.org/ FreeTDS ODBC driver](http://www.freetds.org/%20FreeTDS%20ODBC%20driver) for Unix platforms and the free [MS SQL Server Native Client ODBC driver for Linux x64](http://msdn.microsoft.com/en-us/library/hh568451%28v=sql.110%29.aspx).

mxODBC comes with full support for stored procedures, multiple result sets, Unicode, a common interface on all platforms and [many other useful features](http://www.egenix.com/products/python/mxODBC/#Features).

### pyodbc

URL

:   [https://github.com/mkleehammer/pyodbc](https://github.com/mkleehammer/pyodbc)

License
:   MIT

Platforms
:   Windows, Linux, MacOS X, FreeBSD, Solaris, Any (source provided)

Python versions
:   2.4 - 3.2

Actively maintained Open Source project.

Precompiled binaries are available for Windows. RedHat Enterprise Linux, Centos, and Fedora have precompiled RPMs available in their Extras repositories.

Supports ANSI and Unicode data and SQL statements and includes an extensive set of unit tests for SQL Server. pyODBC require ODBC driver to work correctly with SQL Server. You may [download latest SQL Server ODBC driver](https://www.devart.com/odbc/sqlserver/download.html) and use it freely. Or you may choose Microsoft ODBC driver for that needs which is posted above in mxODBC driver description.

### pypyodbc （Pure Python) 

URL

:   [https://github.com/jiangwen365/pypyodbc](https://github.com/jiangwen365/pypyodbc)

License
:   MIT

Platforms
:   Windows, Linux

Python versions
:   2.4 - 3.3

[A Hello World script of pypyodbc database programing](http://code.google.com/p/pypyodbc/wiki/A_HelloWorld_sample_to_access_mssql_with_python)

[Connect SQL Server in 3 steps with pypyodbc on Linux](http://code.google.com/p/pypyodbc/wiki/Linux_ODBC_in_3_steps)

[Run SQLAlchemy on PyPy with pypyodbc driver](https://code.google.com/p/pypyodbc/wiki/Enable_SQLAlchemy_on_PyPy)

PyPyODBC is a pure Python script, it runs on CPython / [IronPython](IronPython) / [PyPy](PyPy) , Version 2.4 / 2.5 / 2.6 / 2.7 , Win / Linux , 32 / 64 bit.

Almost totally same usage as pyodbc ( can be seen as a re-implementation of pyodbc in pure Python ).

Simple - the whole module is implemented in a single python script with less than 3000 lines.

Built-in Access MDB file creation and compression functions on Windows.

### ODBC 

It is possible to connect to an SQL Server database using ODBC, either the mxODBC driver or the one included with Win32all. However, this is not recommended - adodbapi is a better solution, in part because it supports unicode.

*Comment:* This is actually not true at all: ODBC is the native API used for SQL Server and does support Unicode all the way. In fact, ODBC is the preferred way of accessing SQL Server if you care for performance. Microsoft has just released the [SQL Server Native Client](http://msdn2.microsoft.com/en-us/data/aa937733.aspx) which is an extended ODBC driver for SQL Server. ADO is just a layer on top of the ODBC interface and a lot slower as a result. See e.g. [MS TechNet](http://www.microsoft.com/technet/prodtechnol/windows2000serv/technologies/iis/reskit/iischp7.mspx) for a comparison of ODBC, OLE DB and ADO, or [this cookbook entry](http://aspn.activestate.com/ASPN/Cookbook/Python/Recipe/389535).

*Comment:* Note about the comment above \-- just because it should be pointed out, mxODBC is not a free product from what I can see, and the \'cookbook entry\' from 2005 referenced above indicates that it is.

------------------------------------------------------------------------

[CategoryPythonWebsite](CategoryPythonWebsite)
