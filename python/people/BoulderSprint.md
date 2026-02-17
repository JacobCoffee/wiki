# BoulderSprint

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# Sprinting 

The BoulderSprint is a regular activity of the [FrontRangePythoneers](FrontRangePythoneers). We held six sprints in 2007, and we hope to do this or better in 2008. If you are interested in holding a sprint with us, please contact FRP leader Jim Baker (jbaker AT zyasoft DOT com).

For more information about sprints in general, read the [SprintIntroduction](SprintIntroduction) page. [SteveHolden](SteveHolden) has a useful [article](http://www.onlamp.com/pub/a/python/2006/10/19/running-a-sprint.html) in the [OnLamp Python DevCenter](http://www.onlamp.com/python/) on how to run a sprint.

Sprints have both short-term and long-term value. If you attend a sprint, you are going to get an immediate and immersive introduction to an opensource codebase. It\'s quite possible that code you write that day will get accepted immediately into the project, via its trunk or a branch. And then there is the long-term payoff, where the sprint leads into a longer journey. The newcompiler project for Jython 2.5 (sprints Jan 6, Feb 3, Aug 4) was merged into trunk on Jan 7, 2008, and is part of two students\' master and dissertation research respectively. The modern branch (expected to be merged in soon) generated some interest for Django on Jython, and soon perhaps ipython on Jython too (also due to another local Pythoneer) (sprints Sept 14-15; Dec 1); the Boulder-Oracle branch was merged April 19 into the Django trunk for its Oracle support (sprint Nov 4, 2006). (Fill in more long-term stories.)

# Previous Sprints 

(Fill in details for the last 3 sprints.)

## TurboGears World-Wide Sprint: Jan 12-13, 2007 

## Django World-Wide Sprint: Dec 1, 2007 

## Django World-Wide Sprint: Sept 14-15, 2007 

## Jython Sprint: Aug 4, 2007 

- Date/time: August 4, 2007 (Saturday), 9 AM - 5:30 PM. Time Zone: Americas/Denver (MDT)

- Food/beverages: provided! Just show up, we will keep you going and as caffeinated as you need to be.

- Location: [bivio Software, Inc.](http://www.bivio.biz/), 28th and Iris. Above Hair Elite in Suite S. [Google Maps link](http://maps.google.com/maps?f=q&hl=en&q=2701+Iris+Ave.,+Boulder+CO&ie=UTF8&z=15&om=1&iwloc=A)

- Topics: IPython on Jython and Jython 2.5 compiler work.

- People planning to participate, either in person or via IRC on #jython (irc.freenode.net):
  1.  Charlie Groves

  2.  Damien Lejeune

  3.  Eric Dobbs

  4.  Fernando Perez

  5.  Frank Wierzbicki

  6.  Ian Kelly

  7.  Jim Baker

  8.  Kip Lehman

  9.  Matt Boersma

  10. Tobias Ivarsson

  11. Neal McBurnett

  12. Philip Jenvey

### IPython on Jython 

For the Jython sprint on Aug 4, there\'s strong interest in getting IPython working on jython. Jython\'s ability to explore the large and complex ecosystem that is Java is one reason it\'s such a great tool. In particular, I (Jim Baker) like using Jython on Jython, as well as to explore functionality we are in the process of adding. It\'s much better to use an object shell than the alternatives (mostly painful).

But IPython is a much better object shell, as we know in using it to explore Django and other projects. Hence the sprint. x IPython support: Getting IPython to run on Jython (ideally the upcoming 2.2 release). Fernando Perez will be attending as a domain expert we can tap, although he plans to squash bugs in the CPython version.

- Homework
  1.  Install Jython 2.2, including source. Will this be RC3?
  2.  Get source code for IPython, and otherwise familiarize yourself with the shell.
- Late-breaking Homework
  1.  Grab the source for the sprint branch through svn: svn co [https://jython.svn.sourceforge.net/svnroot/jython/branches/august-boulder-sprint](https://jython.svn.sourceforge.net/svnroot/jython/branches/august-boulder-sprint) jython

### Jython 2.5 

The upcoming Jython 2.2 release represents a huge milestone for the Jython community, but in the next step we want to catch up on 2.5 (or even 2.6) features. The principal reason is to enlarge the community: as long as there\'s such a lagging between CPython and Jython, it means that supporting even core packages is shouldered by Jython implementers instead of being shared across the Python community. In addition, certain 2.5 functionality addresses portability concerns. Resource Allocation is Initialization (RAII), as enabled by the with-statement, makes it much easier to do the right thing and have deterministic resource destruction instead of relying on reference counting doing this implicitly, but creating an incompatibility with non-refcounting GC as is the case with Java/Jython. 2.6\'s Class decorators and function annotations, in addition to 2.5\'s function decorators and 2.2\'s import hooking, make it possible for Jython to consume and produce annotation metadata and type signatures.

Two of our Google Summer of Code students have confirmed their participation, Damien Lejeune and Tobias Ivarsson. Damien has been working on the new AST parser based on Antlr, and Tobias has been working on a new bytecode compiler based on ASM. In this sprint, we would like to help them out and especially help with their integration of the compilation pipeline. In addition one of us (Jim Baker) is planning on finally getting to work on support for Java annotation metadata.

- Homework. To be filled in shortly.

## IPython1 Sprint 

- Date/time: April 28, 2007 (Saturday), 9 AM - 6 PM

- Location: [bivio Software, Inc.](http://www.bivio.biz/), 28th and Iris. Above Hair Elite in Suite S. [Google Maps link](http://maps.google.com/maps?f=q&hl=en&q=2701+Iris+Ave.,+Boulder+CO&ie=UTF8&z=15&om=1&iwloc=A)

Summary: IPython1 is a beefed-up version of the python interactive interpreter that enables parallel computing. It\'s the next generation of the indispensible IPython shell.

We\'re going to caffeinate and code and get this amazing codebase to beta status.

Your homework:

- Visit [http://ipython.scipy.org/moin/IPython1](http://ipython.scipy.org/moin/IPython1)

- Thoroughly read the wiki pages relating to IPython1

- Check out the \"saw\" branch (not \"chainsaw\") as described at [http://ipython.scipy.org/moin/Developer_Zone](http://ipython.scipy.org/moin/Developer_Zone)

- Run the test suite against the saw branch

This shouldn\'t take more than an hour or two, and will ensure we all have a base level of familiarity with the project that will help us hit the ground running.

In addition, Fernando plans to use Mercurial for distributed version control during the sprint, so you should install and familiarize yourself with that software if time permits.

## Jython Sprints 

- January 6, 2007 (Saturday), 9 AM - 6 PM
- February 3, 2007 (Saturday), 9 AM - 6 PM

Update Jython. [Brian Zimmer\'s proposal](http://wiki.python.org/jython/MovingJythonForward) is an useful outline of what needs to be done technically. Perhaps even more importantly, there are some key engineering challenges to be addressed to ensure overall project success. Because of the scope of the work, we are looking at this as preliminary to [a 4-day sprint at PyCon](http://us.pycon.org/TX2007/Sprints). More here at [JythonSprint](JythonSprint).

## Participants 

1.  Eric Dobbs
2.  Bill Simons
3.  Matt Boersma
4.  Kip Lehman
5.  Jim Baker

## Django-Oracle Project 

November 4, 2006 (Saturday), 9 AM - 6 PM

Complete support for Oracle in Django in time for 1.0. Suggested by Matt Boersma.

UPDATE: Thanks to the hard work of Ian Kelly, this code is basically complete. We\'re submitting a patch for Oracle support back to the trunk today (April 19, 2007). Lots of people had a hand in these changes, so congratulations are in order for everyone!

Specifically, we would like to build on the good work already done by the Django community to produce a single patch that can be applied to current subversion sources, enabling Django\'s ORM to pass basic tests against an Oracle database. The current patches available have Oracle-specific conditional tests in many locations; we will try to confine such code to the django.db.backends.oracle package.

## References 

The bug report stipulating Oracle support by Django version 1.0 is here: [http://code.djangoproject.com/ticket/1990](http://code.djangoproject.com/ticket/1990)

## Preliminary Tasks 

(Many of these are refinements and performance improvements that we won\'t get to, since we\'re focused only on correct behavior right now. But several of us reviewed the code and didn\'t want to lose any feedback. After the sprint, we will enter the outstanding issues in [the Django project Trac](http://code.djangoproject.com/newticket).)

- Use ROWNUM, not LIMIT 1. Oracle guru Tom Kyte addresses this in a recent [article](http://www.oracle.com/technology/oramag/oracle/06-sep/o56asktom.html) in Oracle magazine. It boils down to using a doubly nested subquery.

- Create LOB columns out-of-line

- Need a way to explicitly specify TABLESPACE for table creation

- (Done) CREATE \[SEQUENCE\|CONSTRAINTS\] gets logged twice

- (Done) backend creates LONG columns, should use CLOBs instead

- (Done) backend may create two LONG columns, but Oracle allows one per table (don\'t use LONG columns\... solved by using CLOBs)

- In \"syncdb\", foreign keys should be created as a second pass after table creation, using ALTER statements. Otherwise the DDL will reference tables not yet created, and Oracle throws errors.

- (Done) Primary key \"id\" column ([AutoField](./AutoField.html)) is NUMBER(38) in creation.py. Does it need to be that large? No it doesn\'t.

- \"syncdb\" should always create indexes for foreign key columns, or Oracle will optimize poorly

- \"syncdb\" doesn\'t check for table existence before running table creation SQL?

- (Done\--as is) [FormatStylePlaceholderCursor](./FormatStylePlaceholderCursor.html) object: is it needed? We thought cx_Oracle already did named params\...

- fulltext search isn\'t supported

- Use INSTR instead of costly LIKE for the endswith construct (LIKE %s) ?

- (Partially done) get_indexes() and get_relations() unimplemented. Use USER_CONSTRAINTS and USER_INDEXES from Oracle.

- (Done) [SlugField](./SlugField.html), [PhoneNumberField](./PhoneNumberField.html), etc., use VARCHAR and CHAR, but all should use VARCHAR2 consistently.

- [TimeField](./TimeField.html) should use \"INTERVAL DAY TO SECOND\" datatype

- (Done) [NullBooleanField](./NullBooleanField.html) should be NUMBER(1) like [BooleanField](./BooleanField.html), not NUMBER(38)

- (Done) Don\'t use Oracle\'s non-native Integer and [SmallInteger](./SmallInteger.html) types, which result in a NUMBER(38).

- [XmlField](./XmlField.html) unimplemented, although Oracle now has native support for this.

- In db/models/base.py, should use COUNT(\*) instead of Oracle LIMIT 1 conditional test

- Create a function-based index on lower() columns, or else check if DB is Oracle 10g

- move query.py oracle tests out to the db module

- Which versions of Oracle do we need to support? (9i and 10g, hopefully, although old versions of cx_Oracle still support 8i)

- Good comment from Winston Lee: \"I think the biggest issue is the restriction of only one LONG field type on a table. This means that NCLOB will need to be used for [TextField](./TextField.html)? in creation.py. cx_Oracle will then return NCLOB field as a cx_Oracle.LOB. I thought that it would be possible to use cx_Oracle.Connection.register to hook into the return and read the LOB object but it should really be a lazy fetch.\"

- Add more Monty Python references to the code.

## Participants 

1.  Jim Baker
2.  Matt Boersma, Aries, the man with the plan
3.  Eric Dobbs
4.  Ian Kelly, Pisces, he who shall do all the work
5.  Matt Drew, Capricorn, master pizza orderer
6.  Michelle Cyr, Cancer, senior ice cream fetcher
7.  Jacob Kaplan-Moss, lead Django developer!
8.  Malcolm Tredinnick (working remotely from Sydney \-- with the flu, no less!)
9.  Mitchell W. Smith, Virgo, schwag coordinator

## Post Sprint Party 

Some of us are planning to go to the [Cuban Connection fundraiser](http://www.bouldercuba.org/), 6 PM - 1 AM, St. Julien Hotel (our favorite meeting place for [FrontRangePythoneers](FrontRangePythoneers)). In addition to raising money for a good cause, this will be a chance to stretch our weary coding muscles while dancing salsa to Quemando and Havana NRG.

## Photo Stream 

- Nov 4, 2006 [Photos](http://www.flickr.com/search/?w=all&q=bouldersprint)
