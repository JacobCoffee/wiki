# PyTable

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

[MikeFletcher](./MikeFletcher.html):

[PyTable\'s](http://pypi.python.org/pypi/pytable/) primary strength is its schema-driven nature. A database plan (schema) is created which maps the structure of the database into a run-time introspectable data structure.

Normally the schema is created in Python code, and used to drive the creation of the database, (though facilities are available for extracting a basic schema from the database). The schema can include information regarding what classes to instantiate when retrieving records for a given table (with suitable defaults provided). The schema is used internally by DBRow objects to implement update and insert queries, for instance. In other words, the DBRow objects can look at themselves to decide what actually needs to be done to accomplish a given task (such as specifying their row uniquely in the table).

PyTable sits halfway between the raw [DbApi](./DbApi.html) (where you know only approximate data-type, name, and a few other minimal pieces of information) and a system such as [PyDO](PyDO) (where the database interactions are done through an object-oriented API). PyTable is still very much about generating and running SQL code, you are not forced into the *everything is an object* mould, you can still run raw SQL (with some helper mechanisms to make creating complex queries easier) and integrate those queries into your row classes. The PyTable DBRow objects are simply very rich introspectable wrappers around the DB-API records (you can use non-DBRow records too).

As to BasicProperty, its purpose is to allow for defining rich *attribute descriptors*, similar to the property objects built in to Python 2.2 and above. Distinction being that the BasicProperty descriptors are far more involved, including default values/functions, two levels of storage hooks for customizing behaviour, the ability to auto-coerce values to/from data-types on save/restore, support for list-of types etceteras. BasicProperty is an extremely general mechanism, so it\'s a little hard to say what particular benefit it has without looking at particular applications.

- In PyTable, the field descriptors are actually BasicProperty objects linked to the field schema for the table from which they were created, so they can, for instance, be used to lookup foreign keys (and their tables)

- In PyTable\'s internal machinery, just about everything is a propertied object. This allows for defining objects as a collection of properties with documentation, default-values, data-typing and coercion. There are very few \"\_init\_\" methods, as just about everything uses the same base class which provides simple property-aware initialisation. Adding/removing properties generally doesn\'t require any change to the code other than the actual property declaration.

Back to the subject at hand; In effect, PyTable is about trying to make the nitty-gritty details of dealing with an SQL-driven application easier by providing introspection facilities that let your code reason about the structure of the database (as embodied in the schema objects).

**What PyTable is not**:

- Lightweight: compared to db_row or the like, it\'s very heavyweight, focused on creating interactive apps, not huge back-end processing apps that need to realise millions of rows simultaneously

- An SQL abstraction mechanism: unlike [PyDO](PyDO) no attempt is made to define a common SQL sub-set, i.e. it\'s not like ADO from Microsoft

- An object-relational mapper: though it may seem like it, PyTable doesn\'t convert references to records automatically (unless you explicitly code a property to do so), it doesn\'t map pivot tables to pseudo-dictionaries, in general, it only executes the SQL you tell it to execute

- Finished: there\'s still a lot of work to do to get to 1.0 beta 1 for PyTable
