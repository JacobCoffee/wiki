# JythonDeveloperGuide/PleaseAdoptMe

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

## Getting to a 2.2 release 

- **proper `__del__`{.backtick} support for user-defined new style classes** [Notes as I bootstrap into Jython](http://sourceforge.net/mailarchive/forum.php?thread_id=30988615&forum_id=5587)

- **metaclasses, super and others are still broken** [Re: bugs 1603312 and 1603315](http://sourceforge.net/mailarchive/message.php?msg_id=37533518)

- variety of bugs in tracker [status on new style classes](http://sourceforge.net/mailarchive/forum.php?thread_id=31129765&forum_id=5587)

- Update the README.

- Update the copyright date in LICENSE.txt to 2006.

## What\'s needed for 2.3 

Samuele: The next big things that we can foresee are indeed **finding a solution for jythonc** and **improving our overloaded java methods resolution** so that it can behave properly once we introduce bools.

(extracted from [Re: Notes as I bootstrap into Jython](http://sourceforge.net/mailarchive/forum.php?thread_id=30988616&forum_id=5587))

## Componentizing JAR Indexing 

[Componentizing JAR Indexing](http://sourceforge.net/mailarchive/forum.php?thread_id=30988620&forum_id=5587)

Charles asked: How much effort would it take to **componentize the whole jar-indexing** subsystem? We\'d be interested in using it for \"import\" purposes in JRuby

Charlie replied: the indexing code could use a significant cleanup. It\'s mostly contained in the [PackageManager](./PackageManager.html) class hierarchy. [SysPackageManager](SysPackageManager) extends [PathPackageManager](./PathPackageManager.html) which extends [CachedJarsPackageManager](./CachedJarsPackageManager.html) which extends [PackageManager](./PackageManager.html). Disentangling the interactions between that mess of inheritance makes working on the caching system harder than it should be.

Charles added: **making the dynlangs be able to call across each other** without some awful marshalling layer to/from java. In other words, we should be able to pass an object from JRuby to Jython to Rhino and read fields and invoke methods without difficulty. That\'s where a common underlying runtime or set of interfaces will be an absolute necessity.

## Compelling Goals 

(extracted from [Setting a compelling goal](http://sourceforge.net/mailarchive/forum.php?thread_id=30988621&forum_id=5587)) Charles: Just supporting Python is not enough of a goal to compel folks to contribute precious off-hours to the project. Working toward support for apps like Django would do a lot more for publicity and project interest.

- django

- [TurboGears](./TurboGears.html)

  - SQLObject and/or SQLAlchemy

  - [CherryPy](./CherryPy.html) see [cherrypy 2.0.0](http://sourceforge.net/mailarchive/message.php?msg_id=37496554) and [generators](http://sourceforge.net/mailarchive/forum.php?thread_id=31099865&forum_id=5587)

  - Kid and/or Genshi

- Twisted (using [Alan Kennedy\'s select implementation](http://www.xhaus.com/alan/python/jynio/select.html))

- WSGI (using [modjy](http://www.xhaus.com/modjy/index.html))

- Trac
