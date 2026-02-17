# PyDo

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

[http://skunkweb.sourceforge.net/PyDO/](http://skunkweb.sourceforge.net/PyDO/)

## Is this tool similar to JavaDataObjects? 

PyDO is similar to [JavaDataObjects](JavaDataObjects) except that you do not need to create a Persist class, nor do you have to deal all that much with the persistence manager. All of the information needed to persist the data is held in the instances themselves (actually the class). In PyDO, you also specify the database types that will be used, so that PyDO can use the best appropriate native (native being Python) type. The current downfall is that PyDO is hard to use in a multithreaded environment, or any environment where more than one connection is desired to be to the \*same\* database.

They kinda come from two different ways of looking at the persistence problem. [JavaDataObjects](JavaDataObjects) looks to come from the aspect of \"I\'ve got this object and want to stuff it in a database\" whereby PyDO comes from the aspect of \"I\'ve got a database, make it easy for me to use it\".

PyDO\'s predecessor (unreleased) was written from the same aspect of [JavaDataObjects](JavaDataObjects), and suffered when the DBAs (rightfully) decided that DDL was their domain (they\'re the ones whose pagers go off when things go south), and didn\'t want it dictated to them. PyDO\'s design was written from the hard experience of having to conform to existing schemas.

The DDL generated for [JavaDataObjects](JavaDataObjects) also (from one of the tutorials I saw anyway \-- [http://www.onjava.com/pub/a/onjava/2002/02/06/jdo1.html](http://www.onjava.com/pub/a/onjava/2002/02/06/jdo1.html)) seems to be a bit much given what is being persisted (one object yields three tables and two \"opaque\" rows), whereby PyDO will work pretty much with any existing schema you can throw at it. I\'ve seen a few middleware packages that come from the same aspect as [JavaDataObjects](JavaDataObjects), and they all (including PyDO\'s predecessor) seem to have this same problem to a lesser or greater extent.

Also, PyDO has tools for reverse engineering an existing database schema. This way, you don\'t often need to write the PyDO classes, at all, but use the generated code. Of course you can edit it to taste :). The reverse engineering tools can even figure out many relations ([Oracle](Oracle), [PostgreSQL](PostgreSQL) and [SAP DB](SAP DB)), assuming that the associated referential integrity constraints are in place.

In short, PyDO aims to not to dictate your schema, as client code comes and goes, but schemas seem to live forever.

I will have to put in a caveat that I\'ve not read much on [JavaDataObjects](JavaDataObjects) enough to know whether or not there is a way to map an existing schema to a class, and that some of my argument may be somewhat invalid.

See also [PyDO](PyDO)

[DrewCsillag](DrewCsillag)
