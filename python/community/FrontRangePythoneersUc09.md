# FrontRangePythoneersUc09

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# FRUncon 09: Front Range Pythoneers Unconference 2009 

We\'re planning a Python Unconference. Date: October 10, 2009, all day Saturday. We will be following up with code sprints on Sunday the 11th.

To learn more about unconferences, click [here](http://en.wikipedia.org/wiki/Unconference).

Note that an unconference assumes participation by a majority of the attendees. The more you put into it, the more you\'ll get out. Please feel free to edit this page if you\'d like to contribute.

## Dates & Locations 

Day 1 Unconference Sat Oct 10

- Google Boulder office, 2590 Pearl Street. Google will be sponsoring the event.

Day 2 [CodeJam](./CodeJam.html) Sun Oct 11

- Bivio Software, 2701 Iris, Suite S, Boulder.

## Social networking 

Proposed Twitter hashtag: #fruncon09

(Registered: [http://tagal.us/tag/fruncon09](http://tagal.us/tag/fruncon09) )

## Day 1 (The Unconference) 

The unconference will be an event where everyone is welcome be part of the actual conference other then just be an attendee. All are welcome to give a speech and/or presentation about Python or the tools that you use with your Python. If you\'re not sure what to talk about, there are a few ideas below, or if you would like to hear someone talk about something, please feel free to add to the list.

### Bios 

- Greg Holling, unconference unorganizer, is an independent consultant, mentor, and trainer based in Lakewood CO. You can reach him at 303-274-9001, or greg (at) holling-co.com.

- Matt Boersma helps organize Front Range Pythoneers and writes Python code at Array BioPharma in Boulder, CO. You can contact him at 303-249-7004, or matt (at) sprout (dot) org.

- Casey Duncan, coder/architect for Pandora.com, likes to experiment with games and graphics using python in his spare time. You can contact him at casey (dot) duncan (at) gmail (dot) com.

- Zooko Wilcox-O\'Hearn, developer and community organizer for the Tahoe-LAFS project. zooko (at) zooko (dot) com . Located in Boulder, CO.

- Chris Perkins, TG developer, evangelist. Employed by www.nrel.gov and www.getmvp.com (and others). Based out of Arvada, CO.

- Uche Ogbuji lives in Superior, CO and works for zepheira.com. Fuller bio: [http://wiki.python.org/moin/UcheOgbuji](http://wiki.python.org/moin/UcheOgbuji) . I\'ll be back from 2 weeks in Europe Oct 8th and am not sure to what extent I can help, but I will try to do what I can. Can\'t make it till about 12:30 :/

- Jim Baker, core committer on Jython and leader of the Front Range Pythoneers, [jbaker@zyasoft.com](mailto:jbaker@zyasoft.com).

- Steve Rogers lives in Lyons and works for Seagate. He\'s a language junkie, but finds that Python hits a sweat spot for many projects.

### What would you like to talk about? 

- (Note that many topics will come up \*at\* the conference)

- Intro to Python or ctypes intro - *Greg Holling*

- Intro to Python or Using [WxPython](WxPython) - *Matt Boersma*

- Matplotlib, unittesting, and/or some performance - *Nick Verbeck*

- pyglet/pygame, OpenGL, C extensions, particle effects - *Casey Duncan*

- Intro to Akara---*Uche Ogbuji*

- \* Slides here: [http://gonzaga.akara.info/\~uogbuji/etc/2009/akara-frpycon09.pdf](http://gonzaga.akara.info/~uogbuji/etc/2009/akara-frpycon09.pdf) (Note: includes promised simplification in last code slide)

- \* *Didn\'t happen. No time to prep*: Understanding strings versus Unicode---*Uche Ogbuji*

- SQLAlchemy, TG, Testing

- Agent Based Modeling in Python \-- *Steve Rogers*

- Foolscap Remote Objects (Actors) for Python \-- *Zooko Wilcox-O\'Hearn*

- Flappserver \-- the Foolscap Application Server: a convenient, secure \"remote button\" [http://foolscap.lothar.com/docs/flappserver.html](http://foolscap.lothar.com/docs/flappserver.html)

### What would you like to learn about? 

- Introduction to Python

- Code Katas

- Python performance

- Packaging for windows

- scientific computing with python
  - matplotlib
  - ipython

- sqlalchemy

- unittesting

- Concurrent Programming in Python
  - Threads/Locks
  - GIL
  - Processes/Messages
  - Immutable Data
  - Software Transaction Memory

- Scappy

- [PyEmu](./PyEmu.html)

- Vtrace

### What would you like to do to help out with the conference? 

- Greg Holling: Conference organizer
- Nick Verbeck: Got us into Google\'s Offices, whatever else needs to be done
- Casey Duncan: Setup/teardown
- Uche Ogbuji: is willing but the schedule seems bleak. If there are examples of something I could bring along or try to accomplish at very short notice, please let me know

*I think this section could use a list of needed tasks/help/contributions. Not everyone knows what sort of help is needed.*

### RSVP 

If you are wishing to attend the unconfrence. We do ask that if you would please RSVP on the Meetup site @ [http://www.meetup.com/frpythoneers/calendar/11167624/](http://www.meetup.com/frpythoneers/calendar/11167624/)

This will help use in getting started the day of the event as well as planning for everything. Including food and drink.

## Day 2 (CodeJaming) 

### TurboGears 

In the morning I\'d like to run this:

#### Relational Database Applications NOW! with TurboGears 

This tutorial is intended to be an un-tutorial. The idea is simple. Bring me a public database, (or 4) and share with the class as we explore the new admin-level RESTful features that [TurboGears2](./TurboGears2.html) employs.

At the end of the class, the goal is for everyone to have a working TG2 application, with a working admin, at least one customized form or table, based on a database they, or another student brought to class.

I will ask the students to do some prep-work. For those who would like to share a database, or a database schema, they should bring with them a database dump, be it a sqlite file on a memory stick, or a pgdump file, or a mysqldump file. If the students would like to share with the class, that\'d be the best way to run the tutorial, and if people provide me with dumps of reasonable sizes ahead of time, I will distribute them with the class material.

We will then split up into teams of people working on similar database systems.

##### Intro Talk 

A 10 minute talk to introduce myself and describe what SA and TG2 aim to do for relational databases. I will also discuss goals for the tutorial.

##### Part I 

The goal of part one is to break the ice with everyone, getting them into groups and getting the first database interactions happening.

- Student Database descriptions (10 mins)
- Splitting into groups (5 mins)
- Copying/Loading databases all around (10 mins)
- Install SQLAlchemy and SQLAutocode (5 mins)
- Run sqlautocode on your loaded database. (30 mins)
  - We will discuss the different options sqlautocode provides, and take a look at the output it produces.
- Set up TG2 and Quickstart a new App. (20 mins)

##### Part II 

The goal of part 2 is to integrate the work done in Part I and explore the ways we can put the turbogears admin and sprox to good use.

- Integrate sqlautocode with the quickstarted TG app. (10 mins)

- Fire up the admin, see how it works with the existing schema. (5 mins)

- Modify the TG code to replace the default TG [AdminConfig](./AdminConfig.html) with A customizable one. (10 mins)

- See where the class would like to customize their admin, following necessary parts of:
  - [http://turbogears.org/2.0/docs/main/Extensions/Admin/index.html](http://turbogears.org/2.0/docs/main/Extensions/Admin/index.html)

  - [http://www.sprox.org/tutorials/table.html](http://www.sprox.org/tutorials/table.html)

  - [http://www.sprox.org/tutorials/form.html](http://www.sprox.org/tutorials/form.html)

  <!-- -->

  - as needed (60 minutes)

##### Bonus 

If we need extra filler at the end (not likely), or, if people want to meet after the afternoon session, I will have a mini-tutorial for [BootAlchemy](./BootAlchemy.html). [BootAlchemy](./BootAlchemy.html) allows people to load Yaml files directly into a relational database.

##### Requirements 

Laptop with Python 2.5 or 2.6 installed. Database system of your choice (Postgres, Sqlite, MySQL) Python drivers for your desired database system installed. (psychopg2, pg8000, pysqlite, mysql-python)

And after some lunch, we can see where the TG discussion goes.
