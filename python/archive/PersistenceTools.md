# PersistenceTools

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# Other Persistent Storage Modules 

The modules listed on this page provide mechanisms for storing data on disk. Some modules are simply the disk-based equivalent of dictionaries; others provide for persistent storage of arbitrary Python objects.

## Disk-based Dictionaries 

[anydbm](http://docs.python.org/lib/module-anydbm.html) Included with the standard Python distribution. The `anydbm` module is a generic interface to all the DBM-like modules listed in the next two lines, selecting from whichever modules are installed.

[DBM](http://docs.python.org/lib/module-dbm.html),\
[GDBM](http://docs.python.org/lib/module-gdbm.html),\
[dbhash](http://docs.python.org/lib/module-dbhash.html) Included with the standard Python distribution. Each of these modules is an interface to a specific library.

[BSDDB](http://docs.python.org/lib/module-bsddb.html) Included with the standard Python distribution. In addition to dictionary-like behaviour, this module also supports B-trees, which allows traversing the keys in sorted order.

[Metakit](http://www.equi4.com/metakit/) [MetaKit](MetaKit) is a C++ library for storage, transport, and manipulation of structured objects and collections. A Python interface is available.

[mxBeeBase](http://www.lemburg.com/files/python/mxBeeBase.html) mxBeeBase is a high performance construction kit for disk based indexed databases. It offers components which you can plug together to easily build your own custom mid-sized databases, up to around 2Gb on 32-bit platforms).

## Data Writing and Parsing 

[PyTables](PyTables) reads and writes large amounts of numeric data.

[Python-DSV](http://python-dsv.sourceforge.net/) parses comma-separated value (CSV) files or similar delimiter-separated files (see also [0305](http://www.python.org/dev/peps/pep-0305 "PEP")).

The xBase .dbf file format used by several old systems such as dBase(II,III,IV), Fox(Base,Pro)

- xBase ([http://linux.techass.com/projects/xdb/](http://linux.techass.com/projects/xdb/)) - Python interface in plans

- [http://www.fiby.at/dbfpy/index.html](http://www.fiby.at/dbfpy/index.html)

- [http://cbbrowne.com/info/xbase.html](http://cbbrowne.com/info/xbase.html)

- [http://www.clicketyclick.dk/databases/xbase/format/](http://www.clicketyclick.dk/databases/xbase/format/)

## Persistent Objects 

[pickle.py](http://docs.python.org/lib/module-pickle.html) Included with the standard Python distribution. The `pickle` module can convert Python objects to and from a string representation.

[shelve.py](http://docs.python.org/lib/module-shelve.html) Included with the standard Python distribution. Built on top of the `pickle` and `anydbm` modules, the `shelve` module behaves like a persistent dictionary whose values can be arbitrary Python objects.

[PyPerSyst](http://sourceforge.net/projects/pypersyst/) A portable object database management system (ODBMS) as well as a database application framework. [PyPerSyst](./PyPerSyst.html) works well with Pyro and Twisted.

[PyVersant](http://starship.python.net/crew/jmenzel/) A wrapper for the [Versant commercial OODBMS](http://www.versant.com).

[http://wiki.zope.org/ZODB](http://wiki.zope.org/ZODB) The Zope Object Database is a persistent-object system that provides transparent transactional object persistence to Python applications.

- [DirectoryStorage](./DirectoryStorage.html): [http://dirstorage.sourceforge.net/](http://dirstorage.sourceforge.net/)

- [RelStorage](./RelStorage.html): [http://pypi.python.org/pypi/RelStorage](http://pypi.python.org/pypi/RelStorage)

[Durus](http://www.mems-exchange.org/software/durus/)

Durus is a persistent object system that offers an easy way to use and maintain a consistent collection of object instances used by one or more processes. Changes to persistent instances are managed through a cached Connection instance that includes `commit()` and `abort() ` methods so that changes are transactional.
