# Aug2001DbApi3Strawman

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

*The original posting of this document can be found at [http://mail.python.org/pipermail/db-sig/2001-August/001877.html](http://mail.python.org/pipermail/db-sig/2001-August/001877.html)*

    PEP: TBA
    Title: DB API 3.0
    Version: $Revision: 1.9 $
    Author: zen@shangri-la.dropbear.id.au (Stuart Bishop)
    Discussions-To: db-sig@python.org
    Status: strawman
    Type: Standards Track
    Requires: 234,248,249, Date PEP
    Created: 18-May-2001
    Post-History: Never

# Abstract 

- Python has had a solid Database API for SQL databases since 1996 \[1\]. This revision introduces iterator support and attempts to fix known issues with the interface. This version provides a module to be integrated into the core Python distribution, which provides the interface to 3rd party RDBMS drivers. This module can use DB API 1.0 and 2.0 compliant modules as the drivers, although it it expected that these drivers will be updated to support this API more fully.

# Copyright 

- This document has been placed in the public domain, except for those sections attributed to other sources.

# Specification 

- Use of this wrapper requires a DB API v2.0 compliant driver to be installed in sys.path. The wrapper may support DB API v1.0 drivers (to be determined). == Module Interface (sql.py) ==

  - connect(driver,dsn,user,password,host,database)
    - driver \-- The name of the DB API compliant driver module. dsn \-- Datasource Name user \-- username (optional) password - password (optional) host \-- hostname or network address (optional) database \-- database name (optional) Returns a Connection object. This will be a wrapper object for DB API 1.0 or DB API 2.0 compliant drivers. DB API 3.0 compliant drivers will have a Connection instance returned unmodified. Does the connect function need to accept arbitrary keyword arguments?

    Exceptions (unchanged from DB API 2.0)
    - Exceptions thrown need to be subclasses of those defined in the sql module, to allow calling code to catch them without knowning which driver module they were thrown from. This is particularly of use for code that is connecting to multiple databases using different drivers.

  == Connection Object ==

  - close() commit() cursor()
    - As per DB API 2.0.

    rollback(savepoint=None)
    - Rollback the current transaction entirely, or to the given savepoint if a savepoint is passed. The savepoint object must have been returned by the savepoint method during the current tranaction.

      The rollback method will raise a `NotSupportedError` exception if the driver doesn\'t support transactions.

    quote(object)
    - Returns a ANSI SQL quoted version of the given value as a

      string. For example:

                          >>> print con.quote(42)
                          42
                          >>> print con.quote("Don't do that!")
                          'Don''t do that!'

      Note that quoted dates often have a RDBMS dependant syntax (eg. \"TO_DATE(\'01-Jan-2001 12:01\',\'DD-MMM-YYYY H24:MI\')\" for Oracle). I need to track down the official ANSI SQL 1992 or 1999 compliant syntax for specifying date/time/and datetime datatype as strings (if it exists). The quote method is invaluable for generating logs of SQL commands or for dynamically generating SQL queries. This method may be made a module level function as opposed to a Connection method if it can be show that string quoting will always be RDBMS independant.

    driver_connection()
    - Returns the unwrapped connection object if the driver is a DB API 1.0 or DB API 2.0 compliant driver. This iis required for accessing RDBMS specific features. Returns self if the connection object is unwrapped.

    capabilities
    - A dictionary describing the capabilities of the driver. Currently defined values are:
      - apilevel
        - String constant stating the supported DB API level of the driver. Currently only the strings \'1.0\', \'2.0\' and \'3.0\' are allowed.

        threadsafety
        - As per DB API 2.0.

        rollback
        - 1 if the driver supports the rollback() method 0 if the driver does not support the rollback() method

        nextset
        - 1 if the driver\'s cursors supports the nextset() method 0 if the nextset() method is not supported.

        default_transaction_level
        - The default transaction isolation level for this driver.

    set_transaction_level(level)
    - Set the transaction isolation level to the given level,

      or a more restrictive isolation level. A [NotSupported](./NotSupported.html) exception is raised if the given or more restrictive isolation level cannot be set. Returns the transaction isolation level actually set.

    autocommit(flag)
    - Do we want an autocommit method? It would need to default to false for backwards compatibility, and remembering to turn autocommit on is as easy as explicitly calling commit().

    savepoint()
    - Sets a savepoint in the current transaction, or throws a

      [NotSupportedError](./NotSupportedError.html) exception. Returns an object which may be passed to the rollback method to rollback the transaction to this point.

  == Cursor Object ==

  - The cursor object becomes an iterator after its execute method has been called. Rows are retrieved using the drivers fetchmany(arraysize) method. execute(operation,sequence_of_parameters)

    - As per the executemany method in the DB API 2.0 spec. Is there any need for both execute and executemany in this API? Setting arraysize to 1 will call the drivers fetch() method rather than fetchmany(). Returns self, so the following code is valid {{{ for row in mycursor.execute(\'select actor,year from sketches\'):
      - \[ \... \] }}}

      What should the default format be for bind variables?

    callproc(procedure,\[parameters\]) arraysize description rowcount close() setinputsizes(size) setoutputsizes(size\[,column\]

    - As per DB API 2.0

    driver_cursor()

    - Return the unwrapped cursor object as produced by the driver. This may be required to access driver specific features.

    next()

    - Return the Row object for the next row from the currently executing SQL statement. As per DB API 2.0 spec, except

      a [StopIteration](./StopIteration.html) exception is raised when the result set is exhausted.

    [iter]()

    - Returns self.

    nextset()

    - I guess as per DB API 2.0 spec.

    warnings

    - List of Warning exceptions generated so far by the currently executing statement. This list is cleared automatically by the execute and callproc methods.

    clear_warnings()

    - Erase the list of warnings. Same as \'del cursor.warnings\[:\]\' Is this method required?

    raise_warnings

    - If set to 0, Warning exceptions are not raised and instead only appended to the warnings list. If set to 1, Warning excepions are raised as they occur. Defaults to 1

  == Row Object ==

  - When a Cursor is iterated over, it returns Row objects.

    dtuple.py ([http://www.lyra.org/greg/python/](http://www.lyra.org/greg/python/)) provides such an implementation already. \[index_or_key\]

    - Retrieve a field from the Row. If index_or_key is an integer, the column of the field is referenced by number (with the first column index 0). If index_or_key is a string, the column is referenced by its lowercased name (lowercased to avoid problems with the differing methods vendors use to capitalize their column names).

  == Type Objects and Constructors ==

  - As per DB API 2.0 spec.

    Do we need Date, Time and [DateTime](./DateTime.html) classes, or just [DateTime](./DateTime.html)? Need to author the \'Date PEP\'. It would be nice if there was a more intelligent standard Date class in the Python core that we could leverage. If we don\'t, people will start using the

    sql module for the more intelligent [DateTime](./DateTime.html) object it would need to provide even if they arn\'t using databases.

  == [ConnectionPool](./ConnectionPool.html) Object ==

  - A connection pool, to be documented.

  == Transaction Isolation Levels ==

  - Insert description of dirty reads, non repeatable reads and phantom reads, probably stolen from JDBC 3.0 documentation. The following symbolic constants are defined to describe the four transaction isolation levels defined by SQL99. Note that they are in numeric order so comparison operators can be safely used to test for restrictivness. Note that these definitions are taken from the JDBC API 3.0 documentation by Sun. TRANSACTION_NONE
    - No transaction isolation is guarenteed.

    TRANSACTION_READ_UNCOMMITTED
    - Allows transactions to see uncommitted changes to the data. This means that dirty reads, nonrepeatable reads, and phantom reads are possible.

    TRANSACTION_READ_COMMITTED
    - Means that any changes made inside a transaction are not visible outside the transaction until the transaction is committed. This prevents dirty reads, but nonrepeatable reads and phantom reads are still possible.

    TRANSACTION_REPEATABLE_READ
    - Disallows dirty reads and nonrepeatable reads. Phantom read are still possible.

    TRANSACTION_SERIALIZABLE
    - Specifies that dirty reads, nonrepeatable reads, and phantom reads are prevented.

  == Test Suite ==

  - A common test suite will be part of the implementation, to allow driver authors and driver evaluators to test and excercise the systems. Two possbilities to start with are the test suites in psycopg by Federico Di Gregorio and mxODBC by eGenix.com Software. Example DDL for various systems will need to be provided.

# Rationale 

- The module is called sql.py, to avoid any ambiguity with non-realational or non-SQL compliant database interfaces. This also nicely limits the scope of the project. Other suggestions are \'sqlutil\' and \'rdbms\', since \'sql\' may refer to the language itself. Previous versions of the DB API have been intentially kept lean to make it simpler to develop and maintain drivers, as a richer feature set could be implemented by a higher level wrapper and maintained in a single place rather than in every API compliant driver. As this revision provides a single place to maintain code, these features can now be provided without placing a burden to the driver authors. Existing DB API 1.0 and 2.0 drivers can be used to power the backend of this module. This means that there will be a full compliment of drivers available from day 1 of this modules release without placing a burden on driver developers and maintainers. The core of the API is identical to the Python Database API v2.0 (PEP-249). This API is already familiar to Python programers and is a proven solid foundation. Python previously defined a common relational database API that was implemented by all drivers, and application programmers accessed the drivers directly. This caused the following issues:
  - It was difficult to write code that connected to multiple database vendor\'s databases. Each seperate driver used defined its own heirarchy of exceptions that needed to be handled, their own datetime class and their own set of datatype constants. Platform independant code could not be written simply, due to the differing paramater styles used by bind variables. This also caused problems with publishing example code and tutorials. The API remained minimal, as any new features would need to be implemented by all driver maintainers. The DB-SIG felt most feature suggestions would be better implemented by higher level wrappers, such as that defined by this PEP.

# Language Comparison 

- The design proposed in this PEP is the same as that used by Java, where a relational database API is shipped as part of the core language, but requires the installation of 3rd party drivers to be used. Perl has a similar arrangement of API and driver separation. Perl does not ship with PerlDBI or drivers as part of the core language, but it is well documented and trivial to add using the CPAN tools. PHP has a seperate API for each database vendor, although work is underway (completed?) to define a common abstraction layer similar to Java, Perl and Python. All of the drivers ship as part of the core language.

# References 

- \[1\] PEPs: [0248](http://www.python.org/dev/peps/pep-0248 "PEP") and [0249](http://www.python.org/dev/peps/pep-0249 "PEP")
