# SAP DB

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# SAP DB (MaxDB) 

URL for 7.6 and later

:   [http://www.sdn.sap.com/irj/sdn/maxdb](http://www.sdn.sap.com/irj/sdn/maxdb)

URL for 7.5

:   (was [http://www.mysql.org/products/maxdb/](http://www.mysql.org/products/maxdb/), but is no longer available)

URL for 7.3 and 7.4

:   [http://www.sapdb.org/](http://www.sapdb.org/)

licence
:   7.3 and 7.4 (GPL + LGPL), 7.5 (GPL), 7.6 and later (Commercial and free community edition)

platforms
:   Linux/i386, Solaris, HP-UX, AIX, Dec, Windows

------------------------------------------------------------------------

## DB API 2.0 Drivers 

### sdb.dbapi

URL

:   [http://maxdb.sap.com/doc/7_7/46/71b2a516ae0284e10000000a1553f6/frameset.htm](http://maxdb.sap.com/doc/7_7/46/71b2a516ae0284e10000000a1553f6/frameset.htm)

licence
:   (?) SAP now releases MaxDB for free, but no longer as open-source software

platforms
:   see SAP DB

Python versions

:   

### sapdbapi

URL

:   [http://www.sapdb.org/sap_db_program.htm](http://www.sapdb.org/sap_db_program.htm)

licence
:   LGPL

platforms
:   see SAP DB

Python versions
:   1.5.2 - 2.2

This is for the older SAP DB releases 7.3 and 7.4.

### mxODBC 

URL

:   [http://www.egenix.com/products/python/mxODBC/](http://www.egenix.com/products/python/mxODBC/)

Licence
:   eGenix.com Commercial License

Platforms
:   Windows, Linux, MacOS X, FreeBSD, Solaris, AIX

Python versions
:   2.4 - 2.7

SAP DB\'s native CLI is ODBC compatible and mxODBC can link directly against these libraries on Unix. It also supports the SAPDB ODBC driver on Windows.

Supports all SAP DB versions.

## Other Drivers 

### sdb.sql

URL

:   [http://maxdb.sap.com/doc/7_7/46/71b2a516ae0284e10000000a1553f6/frameset.htm](http://maxdb.sap.com/doc/7_7/46/71b2a516ae0284e10000000a1553f6/frameset.htm)

licence
:   (?) SAP now releases MaxDB for free, but no longer as open-source software

platforms
:   see SAP DB

Python versions

:   

### sapdb

URL

:   [http://www.sapdb.org/sap_db_program.htm](http://www.sapdb.org/sap_db_program.htm)

licence
:   LGPL

platforms
:   see SAP DB

Python versions
:   1.5.2 - 2.2

This is for the older SAP DB releases 7.3 and 7.4.

#### Programming Model 

    cursor = session.sql ("select * from messages")
    for msgno, lang, text in cursor:
        print msgno, text

    insert = session.prepare ("insert into sometable values (?, ?)")
    print insert.getDescription ()
    insert.execute (["string", 1])

    select = session.prepare ("select * from messages where msgno < :msgno")
    cursor = select.execute ([200])
    print cursor.next ()
    print cursor.relative (100)
    print cursor.absolute (4)
    print cursor.absolute (-4)

------------------------------------------------------------------------

## Supported Python Applications 

- a sapdb driver exists for [PyDO](PyDO) (Python Data Objects)
