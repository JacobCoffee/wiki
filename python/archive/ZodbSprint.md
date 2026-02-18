# ZodbSprint

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

Let\'s work on making ZODB better!

Leader: Tim Peters

Jim Fulton will present the ZODB architecture as a basis for work. This will be a good opportunity to learn about many of the nitty-gritty details of ZODB.

There are many things we could work on, including:

- Adding interfaces (what exactly are the public APIs? it\'s become muddy) PROGRESS: Christian Theune made a good start at this; more is needed.

- Database iteration (e.g., iterate over all the objects of class Foo; there\'s no efficient way to do this now, especially when using ZEO). PROGRESS: A FileStorage iterator was implemented. Still needed: other storages; ZEO; more usable API on Connections.

- Multi-database support, [http://zope.org/Wikis/ZODB/MultiDatabases](http://zope.org/Wikis/ZODB/MultiDatabases). PROGRESS: A simpler of version of this proposal was implemented. Still needed: work on Zope to use this, and to stop monkey-patching ZODB internals.

- Deprecate get_transaction() officially. PROGRESS: done for ZODB 3.4, and all ZODB code using it (test suites and tools) changed to stop using it. Zope trunks (2.8 and 3) have been cleaned up to match.

- Blob support. PROGRESS: Enormous progress on this was made, primarily by Christian Theune and Chris [McDonough](./McDonough.html). See the zodb-dev mail list for some detailed status reports and timings. The code is in ZODB/branches/ctheune-blobsupport/.

- Documentation

- Bug fixes

- Code cleanup

- Saner tests

- Savepoints

- Getting rid of versions

- Conflict resolution redesign. Possiblities: make it optional, make it pluggable, use a registry of class-\>resolution code instead of methods, get it off the ZEO server?

Note that to be able to make code contributions, you must be a Zope contributor: [http://dev.zope.org/Subversion](http://dev.zope.org/Subversion) Note that you don\'t have to be a Zope user to be a Zope contributor. ![:)](/wiki/europython/img/smile.png ":)") You don\'t have to be a Zope contributor either to participate in working out (and writing up) proposals for things ZODB could/should be doing better.

If you plan to participate, please put your name below, and, if you won\'t be there all 4 days, indicate which days you plan to be there.

Participants:

- Tim Peters (Sat, Sun, Mon, Tue)

- Christian Theune (All days)

- Jim Fulton (perhaps intermittently)

- Cameron Laird: will likely arrive late Saturday afternoon; is willing to work on documentation; and has lots of interest both in Zope and in OODBMSs generally.

- Chris [McDonough](./McDonough.html) (Sat, Sun)

If you don\'t sign up, you can still come and participate. The sign up is to give us an idea who will be there.

[ChrisMcDonough](../archive/ChrisMcDonough) says

------------------------------------------------------------------------

We seem to have a nascent idea about working on ZODB \"blob\" suppport for at least some period of time during this sprint\... for details, see [http://www.plope.com/Members/chrism/zodb_blob_proposal](http://www.plope.com/Members/chrism/zodb_blob_proposal)

Other minor things:

- \- Make ZEO server write a pidfile so we can rotate its logs by sending an appropriate
  - signal.

  \- Come up with a Wiki page somewhere that details how to check stuff into ZODB without
  - making Tim\'s life a nightmare. But Tim thinks this is

    pretty hopeless ![;-)](/wiki/europython/img/smile4.png ";-)")

  \- Allow ZEO clients to query the active ZEO server for its system clock value
  - (useful for synchronization).

------------------------------------------------------------------------

[CategoryPyCon2005](CategoryPyCon2005)
