# PyCon2006/Sprints

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

For more information about [PyCon](../PyCon) 2006, see the main conference site at [http://us.pycon.org/](http://us.pycon.org/).

The following sprints are planned for the four days after the conference.

To register a new sprint, just edit this page and add your sprint, listing yourself as the sprint coach. If you won\'t be around for all four days, please specify the days you\'ll be present.

If you have any questions about sprinting at [PyCon](../PyCon), please send email to the Sprint Coordinator, [David Goodger](mailto:goodger@python.org).

## Logistics 

- Rooms: To be decided. Time: Starting 8 am Monday (intro session from 3:30 pm Sunday) Date: Monday February 27 through Thursday March 2 inclusive. Cost to attend: Free! Bring: Your laptop and a wireless card. IRC: #pycon-sprints on irc.freenode.net, or as listed below

## Preparations 

Because the sprints are after the formal conference, all the sprint attendees will likely be present at the start of the sprints. Sprint coaches should plan for an introductory session on Sunday afternoon or Monday morning, where you can help attendees get started. This might involve helping them to get SVN or CVS installed, find the development tree, talk about the software\'s architecture, or planning what the four-day sprint will try to accomplish.

If the introductory session is on Sunday, you should plan to begin around 3:30PM.

### Free Wing IDE licenses 

For sprinters that would like a free license for Wing IDE Professional, please see Stephan Deibel or John Ehresman either at the sprint plenary Sunday 3:35 PM in Preston Trail or during the sprinting days.

## Sprints 

### Django 

- Goal: Same thing we do every night, Pinky Coach: Jacob Kaplan-Moss

  Details: [/DjangoSprint](Sprints/DjangoSprint)

### Zope 

- Goals: Integrate more of Zope 3 into Zope 2, improved through-the-web management, \... Coach: Jim Fulton (jim at zope.com)

  Details: [http://dev.zope.org/Zope3/PyCon2006Sprint](http://dev.zope.org/Zope3/PyCon2006Sprint) IRC: #zope3-dev

### Stackless 

- Goal: to port Stackless to Python 2.4.2 Coach: Christian Tismer

  Details: [/StacklessSprint](Sprints/StacklessSprint)

### Docutils (reStructuredText) 

- Goal: add functionality, fix bugs, and facilitate applications

  Coach: [DavidGoodger](../../../people/DavidGoodger)

  Details: [/DocutilsSprint](Sprints/DocutilsSprint) IRC: #docutils

### Python Core 

- Goal: add functionality, fix bugs, and facilitate applications Coach: Brett Cannon

  Details: [/PythonCore](Sprints/PythonCore)

### TurboGears 

- Goal: add functionality, resolve tricky bugs and facilitate applications Coach: Kevin Dangoor

  Details: [/TurboGearsSprint](Sprints/TurboGearsSprint)

### PyPy 

- Goal: work in any area of interest of [PyPy](../../../implementations/PyPy) Coach: Michael Hudson, Armin Rigo, Holger Krekel

  Details: [/PyPySprint](Sprints/PyPySprint)

### Pydotorg rollout 

- Goal: Rest of content conversion for [http://beta.python.org](http://beta.python.org) and make it live on python.org on or before March 5th

  Coach: Tim Parkin (not on site but knows everything) and Stephan Deibel (onsite but knows nothing ![:-)](/wiki/europython/img/smile.png%20":-)")

  Details: [/PydotorgSprint](Sprints/PydotorgSprint)

### Conference software 

- Goal: work on a unified conference software system for [PyCon](../PyCon)

  Coach: [AndrewKuchling](../../../people/AndrewKuchling)

  Details: [/ConferenceSprint](Sprints/ConferenceSprint)

### pymon and CoyMon 3 

- Goal: release pymon 0.3.4 (monitoring server written in Twisted), work on component parts of [CoyMon](./CoyMon.html) 3 including [PyFlowCatch](./PyFlowCatch.html) and PyRRD (where we\'re building a Twisted RRDTool server)

  Coach: [DuncanMcGreggor](../../../archive/DuncanMcGreggor) Details:

  - [http://projects.adytum.us/tracs/PyMonitor/wiki/PyConTwoOhOhSix](http://projects.adytum.us/tracs/PyMonitor/wiki/PyConTwoOhOhSix) and

    [http://projects.adytum.us/tracs/CoyMon/wiki/PyConTwoOhOhSix](http://projects.adytum.us/tracs/CoyMon/wiki/PyConTwoOhOhSix)

  IRC: #adytum

### Chandler 

- Goal: work on any area of interest in Chandler

  Coach: [TedLeung](./TedLeung.html) Dates: Feb 27 and 28 only

  Details: [http://wiki.osafoundation.org/bin/view/Journal/PyCon2006](http://wiki.osafoundation.org/bin/view/Journal/PyCon2006) IRC: #chandler

### vobject

- Goal: add hCalendar, hCard, and xCalendar support to vobject

  Coach: [JeffreyHarris](./JeffreyHarris.html) Dates: Feb 27 and 28 only

  Details: [/VobjectSprint](Sprints/VobjectSprint)

### MySQL 

- Goal: Finish up MySQLdb-1.2.1 and ZMySQLDA-2.0.9

  Coach: [AndyDustman](../../../people/AndyDustman) Dates: Sunday through Tuesday

  Details: Fix bugs at [http://sourceforge.net/projects/mysql-python](http://sourceforge.net/projects/mysql-python) Submit patches/bugs in

  - advance if you have any. If you want CVS checkin ability, get a [SourceForge](../../../people/SourceForge) account.

  Cost to Attend: Sanity (optional)

### Array Interface Sprint 

- Goal: Adding a [SciPy](SciPy) inspired Array Interface to the Python Core

  Details: [/ArrayInterfaceSprint](Sprints/ArrayInterfaceSprint)

## Introduction 

### What is a sprint? 

A sprint is a focused development session, in which developers pair in a room and focus on building a particular subsystem. A sprint is organized with a coach leading the session. The coach sets the agenda, tracks activities, and keeps the development moving. The developers often work in pairs using XP\'s pair programming approach.

The sprint approach works best when the first few hours are spent getting oriented \-- presenting a tutorial for the development material, laying out the stories to tackle for the day, getting everyone a CVS or SVN checkout to work with.

[ZopeMag\'s miniGuide to Zope Sprinting](http://www.zopemag.com/Guides/miniGuide_ZopeSprinting.html) is a good introductory article; just mentally remove every \"Zope\" from the article to make it generic.

### Why sprint at PyCon? 

The sprints are intended to benefit various projects, and to encourage more people to take part in development. They will also be a good place to see [ExtremeProgramming](../../../people/ExtremeProgramming) or other [AgileMethods](./AgileMethods.html) in action, and to work closely with experienced Python developers.

[PyCon](../PyCon) will always have a core Python sprint. Other topics will come and go each year.

If you wish to participate in a sprint, please contact the sprint organizers in advance, or add your name to the list of participants for a given sprint.

### What equipment/supplies will sprints get? 

[PyCon](../PyCon) will supply the following:

- Room. Multiple sprints will share the same room; different sprints will presumably occupy different tables.
- Wireless networking.
- Easels, a tablet of paper, and markers.
- Writing paper and pens (for notes, sketches, etc.).
- Ice water.

[PyCon](../PyCon) does *not* supply food for the sprint days. Participants will have to go to [PyCon2006/NearbyRestaurants](NearbyRestaurants), or have food delivered to the hotel.

### Who makes this possible? 

The [Python Software Foundation](http://www.python.org/psf) sponsors the sprints at [PyCon2006](). Please consider making a [donation](http://www.python.org/psf/donations.html) to support this vital community activity!

### IRC 

If you cannot attend the sprints in person but would still like to follow the progress and/or participate, you can, via IRC (irc.freenode.net) or other means, as listed above. The #pycon-sprints channel can be used for general sprint-related traffic.

------------------------------------------------------------------------

[CategoryPyCon2006](CategoryPyCon2006)
