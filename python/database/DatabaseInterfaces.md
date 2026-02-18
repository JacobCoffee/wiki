# DatabaseInterfaces

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

This page lists database interfaces available for Python. It may also help in finding a suitable database engine for you to use in your Python database applications.

## Generic Database Interfaces and APIs 

- The Python standard for database interfaces is the [Python DB-API (PEP 249)](http://www.python.org/dev/peps/pep-0249/) Most Python database interfaces adhere to this standard.

- Most databases have ODBC support; see the section below on ODBC modules.

- Java databases usually support JDBC, and can be used from Jython.

- See also [DbApiModuleComparison](DbApiModuleComparison)

### ODBC Support 

- See [ODBC](../archive/ODBC)

### ADO Support 

- See [ADO](ADO)

## Database Interfaces for Relational Database Systems 

Database systems employing a relational model, with support for SQL.

### General Purpose Database Systems 

- IBM [DB2](../archive/DB2)

- [Firebird](../archive/Firebird) (and Interbase)

- [Informix](../archive/Informix)

- [Ingres](../archive/Ingres)

- [MySQL](MySQL)

- [Oracle](Oracle)

- [PostgreSQL](PostgreSQL)

- [SAP DB](../archive/SAP%20DB) (also known as \"MaxDB\")

- Microsoft [SQL Server](SQL%20Server)

- Microsoft [Access](../people/Microsoft%20Access)

- [Sybase](../archive/Sybase)

- [InterSystems IRIS](../archive/InterSystems%20IRIS)

(To add new entries, please choose [DatabaseTemplate](DatabaseTemplate) when creating the page.)

### Data Warehouse Database Systems 

- [Teradata](../archive/Teradata)

- IBM [Netezza](../archive/Netezza)

(To add new entries, please choose [DatabaseTemplate](DatabaseTemplate) when creating the page.)

### Database Systems for Embedding Into Applications 

The following database systems are more oriented towards embedded applications:

- [asql](../archive/asql)

- [GadFly](./GadFly.html)

- [SQLite](SQLite)

- [ThinkSQL](../archive/ThinkSQL)

(To add new entries, please choose [DatabaseTemplate](DatabaseTemplate) when creating the page.)

## Non-Relational Databases 

### Record-based Databases 

Databases working on flat files or fixed records.

- [MetaKit](../people/MetaKit)

- [ZODB](../archive/ZODB)

- [BerkeleyDB](../archive/BerkeleyDB)

- [KirbyBase](../people/KirbyBase)

- [Durus](../archive/Durus)

- [atop](./atop.html)

- [buzhug](../archive/buzhug)

(To add new entries, please choose [DatabaseTemplate](DatabaseTemplate) when creating the page.)

### XML Databases 

- 4Suite server

- Oracle/Sleepycat DB XML ([howto](http://jimmyg.org/blog/2008/oracle-db-xml-was-sleepycat.html))

### Graph Databases 

- [Neo4j](./Neo4j.html)

(To add new entries, please choose [DatabaseTemplate](DatabaseTemplate) when creating the page.)

## Native Python Databases 

- [buzhug](../archive/buzhug)

- [SnakeSQL](../archive/SnakeSQL)
