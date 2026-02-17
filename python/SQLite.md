# SQLite

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# SQLite 

URL

:   [http://sqlite.org/](http://sqlite.org/)

licence
:   Sources are uncopyrighted. Use for any purpose.

platforms
:   Built and tested under Linux and Win2K.

## Pros 

I think SQLite may be a good replacement for gadfly, because:

- The main engine is written in C, so it should be faster than the gadfly implementation in Python
- It\'s extensible in a very easy way via Python
- It doesn\'t put all data in memory like gadfly does (yet you can do that if you want, just use \':memory:\' as filename
- It\'s very cool for small databased application, because you do not have to start an external DBMS
- Implements almost all of SQL92

## Cons 

- SQLite only supports the basic types NULL, INTEGER, FLOAT, TEXT and BLOB
- If you want to use other types like DATE and TIME in pysqlite, you need to use its \"pysqlite types mode\", where things can get a little nastier.

------------------------------------------------------------------------

## DB API 2.0 Drivers 

### pysqlite

URL

:   [http://code.google.com/p/pysqlite/](http://code.google.com/p/pysqlite/)

SourceForge

:   [http://sourceforge.net/projects/pysqlite](http://sourceforge.net/projects/pysqlite)

licence
:   zlib/libpng License

platforms
:   Windows 95/98/2000/XP, POSIX, MacOS X

Python versions
:   2.1 or later (1.x branch)/2.3 or later (2.0 branch). Included in Python 2.5.

#### Extensions to DB API 

- Extensible type conversion
- Factories for connection and cursor objects
- row converter factory to easily and efficiently switch to a nonstandard type for rows (e. g. dicts)
- User-defined functions and aggregates

## Other Drivers 

### APSW 

URL

:   [http://code.google.com/p/apsw/](http://code.google.com/p/apsw/)

licence
:   zlib/libpng license (or any OSI approved license of your choice)

platforms
:   Windows, POSIX

Python versions
:   2.3 onwards, 3.1 onwards

#### Programming Model 

APSW is a Python wrapper for the [SQLite](http://sqlite.org/) embedded relational database engine. In contrast to other wrappers such as [pysqlite](http://code.google.com/p/pysqlite/) it focuses on being a minimal layer over SQLite attempting just to translate the complete SQLite API into Python. The [documentation](http://apidoc.apsw.googlecode.com/hg/pysqlite.html) has a section on the differences between APSW and pysqlite.

------------------------------------------------------------------------

## Supported Python Applications 

- Thuban (GIS application)

- Roundup (issue tracker)

- PyPI (Python Package Index)

- Trac (issue tracker, wiki, Subversion web frontend)

- Cloud Wiki (wiki)

- Supybot (IRC bot framework)

- [PyAddbook](./PyAddbook.html) (Address Book)

## Usage Notes 

The following solution was difficult to discover with the available documentation ([http://pysqlite.org/](http://pysqlite.org/) was unavailable). If this page can be found by others searching for answers, it may save many hours of frustration.

### Id of Most Recent Row 

After creating a new row in a table that uses AUTOINCREMENT to create the PRIMARY KEY, one may wish to determine the value of the new row-id, for example if the value is need for a new row in a related table that will be inserted next. The answer is to use the *lastrowid* property of the *cursor* class as in `newId=c.lastrowid ` shown below in a demo context. Tested in Python2.5.1 with the sqlite3 module:

               import sqlite3 

    # for py24 use from pysqlite2 import dbapi2 as sqlite

               con = sqlite3.connect('demo.db')
               con.execute("""CREATE TABLE tbl (
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   grp INTEGER)""")
               c = con.cursor()
               c.execute("""INSERT INTO tbl (grp) VALUES (0);""")

               newId = c.lastrowid

               print "New rowid =", newId
               c.close()
               con.close()

The result is printed:` New rowid = 1`
