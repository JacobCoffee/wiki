# PyCon2006/Tutorials/UsingDatabaseWithPython

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# Audience 

Python programmers with a desire to understand how to build cross-platform database applications.

# Summary 

This tutorial will introduce the student to the relational model and SQL. It will present the DB API and show how it can be used in a relatively platform-independent way to maintain source portablility of Python database applications.

Pre-registered students will receive access to electronic copies of the course notes and example materials to allow them to run the examples presented in the tutorial.

To undertake the practical examples they should have a database installed on their laptop with a DB API-compliant Python interface, and should be able to create a database for use in class. The examples should work on MySQL, PostgreSQL and Microsoft Access at the very least, and the materials will contain programs to create the necessary database to support the examples.

Before class students should verify their ability to connect to the newly-created database from Python.

# Outline 

1\. A Super-Fast Introduction to the Relational Model

- Everything is in tables The role of the primary key SQL in a Nutshell

2\. The DB API

- Connections Cursors Exceptions Some API-compliant modules

3\. Connecting to the Database

- Creating connections Transactions Connection pooling Executing Queries

4\. Executing Queries

- Some representations of queries Building the query string Processing the results Representing results for convenient processing

5\. Handling Updates

- Inserting new data Deleting old data Updating existing data

6\. Object-Relational Mappers

- Purpose of mapping the object model Mapping characteristics PyDO SQLObject

7\. Putting it All Together

- Some real applications code
