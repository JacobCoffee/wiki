# Database Programming

Python talks to databases through the DB-API, a standard interface defined in PEP 249. This section has everything from getting-started guides to cheat sheets to opinionated critiques of the API itself. You will also find pages for specific database engines and ORMs. Some of the version information here is dated, but the conceptual material on DB-API usage holds up well.

## Getting Started

- [DatabaseProgramming](DatabaseProgramming) -- starting point for learning about databases in Python, covering relational databases, the DB-API, and ORMs
- [DatabaseInterfaces](DatabaseInterfaces) -- list of available Python database interface modules, organized by database engine
- [DatabaseBooks](DatabaseBooks) -- recommended books on database concepts and Python database programming
- [DatabaseBof](DatabaseBof) -- notes from a birds-of-a-feather meeting on Python database capabilities
- [DatabaseTemplate](DatabaseTemplate) -- blank template for documenting a database interface

## The DB-API

- [DbApi3](DbApi3) -- discussion topics for a possible DB-API 3.0 specification
- [DbApi3 subpages](DbApi3/index) -- related discussions and proposals for DB-API 3
- [DbApiCheatSheet](DbApiCheatSheet) -- quick syntax reference comparing DB-API usage across PostgreSQL, SQLite, MySQL, Oracle, and ODBC
- [DbApiFaq](DbApiFaq) -- frequently asked questions from the DB-SIG mailing list, including parameter passing and cursor usage
- [DbApiModuleComparison](DbApiModuleComparison) -- side-by-side feature comparison table of DB-API modules
- [DbApiSucks](DbApiSucks) -- frank criticism of DB-API design decisions, particularly around cursor semantics

## Database Engines

- [SQLite](SQLite) -- the embedded database bundled with Python's standard library
- [PostgreSQL](PostgreSQL) -- PostgreSQL interface information
- [MySQL](MySQL) -- MySQL interface information
- [Oracle](Oracle) -- Oracle database interface information
- [SQL Server](SQL%20Server) -- Microsoft SQL Server connectivity
- [ADO](ADO) -- Microsoft's ActiveX Data Objects, a high-level database interface on Windows

## ORMs and Tools

- [SQLAlchemy](SQLAlchemy) -- the Python SQL toolkit and ORM
- [SQL](SQL) -- overview of Python's SQL database support and pointers to interface modules
- [SQLPython](SQLPython) -- a Python-based alternative to Oracle's SQL*Plus command-line tool

```{toctree}
:hidden:
:maxdepth: 1

DbApi3/index
ADO
DatabaseBof
DatabaseBooks
DatabaseInterfaces
DatabaseProgramming
DatabaseTemplate
DbApi3
DbApiCheatSheet
DbApiFaq
DbApiModuleComparison
DbApiSucks
MySQL
Oracle
PostgreSQL
SQL
SQL Server
SQLAlchemy
SQLPython
SQLite
```
