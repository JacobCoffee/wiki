# DatabaseInterfaces

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

This page lists database interfaces available for Python. It may also help in finding a suitable database engine for you to use in your Python database applications.

# Generic Database Interfaces and APIs 

- The Python standard for database interfaces is the [Python DB-API (PEP 249)](http://www.python.org/dev/peps/pep-0249/) Most Python database interfaces adhere to this standard.

- Most databases have ODBC support; see the section below on ODBC modules.

- Java databases usually support JDBC, and can be used from Jython.

- See also [DbApiModuleComparison](DbApiModuleComparison)

## ODBC Support 

- See [ODBC](ODBC)

## ADO Support 

- See [ADO](ADO)

# Database Interfaces for Relational Database Systems 

Database systems employing a relational model, with support for SQL.

## General Purpose Database Systems 

- IBM [DB2](DB2)

- [Firebird](Firebird) (and Interbase)

- [Informix](Informix)

- [Ingres](Ingres)

- [MySQL](MySQL)

- [Oracle](Oracle)

- [PostgreSQL](PostgreSQL)

- [SAP DB](../archive/SAP DB) (also known as \"MaxDB\")

- Microsoft [SQL Server](SQL Server)

- Microsoft [Access](../people/Microsoft Access)

- [Sybase](Sybase)

- [InterSystems IRIS](../archive/InterSystems IRIS)

(To add new entries, please choose [DatabaseTemplate](DatabaseTemplate) when creating the page.)

## Data Warehouse Database Systems 

- [Teradata](Teradata)

- IBM [Netezza](Netezza)

(To add new entries, please choose [DatabaseTemplate](DatabaseTemplate) when creating the page.)

## Database Systems for Embedding Into Applications 

The following database systems are more oriented towards embedded applications:

- [asql](asql)

- [GadFly](./GadFly.html)

- [SQLite](SQLite)

- [ThinkSQL](ThinkSQL)

(To add new entries, please choose [DatabaseTemplate](DatabaseTemplate) when creating the page.)

# Non-Relational Databases 

## Record-based Databases 

Databases working on flat files or fixed records.

- [MetaKit](MetaKit)

- [ZODB](ZODB)

- [BerkeleyDB](BerkeleyDB)

- [KirbyBase](KirbyBase)

- [Durus](Durus)

- [atop](./atop.html)

- [buzhug](buzhug)

(To add new entries, please choose [DatabaseTemplate](DatabaseTemplate) when creating the page.)

## XML Databases 

- 4Suite server

- Oracle/Sleepycat DB XML ([howto](http://jimmyg.org/blog/2008/oracle-db-xml-was-sleepycat.html))

## Graph Databases 

- [Neo4j](./Neo4j.html)

(To add new entries, please choose [DatabaseTemplate](DatabaseTemplate) when creating the page.)

# Native Python Databases 

- [buzhug](buzhug)

- [SnakeSQL](SnakeSQL)
