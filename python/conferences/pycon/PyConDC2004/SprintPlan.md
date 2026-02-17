# PyConDC2004/SprintPlan

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

## PyConDC 2004 Sprint plan 

### What is a sprint? 

A sprint is a focused development session, in which developers pair in a room and focus on building a particular subsystem. A sprint is organized with a coach leading the session. The coach sets the agenda, tracks activities, and keeps the development moving. The developers work in pairs using XP\'s pair programming approach.

The sprint approach works best when the first few hours are spent getting oriented \-- presenting a tutorial for the development material, laying out the stories to tackle for the day, getting everyone a CVS checkout to work with.

[ZopeMag\'s miniGuide to Zope Sprinting](http://www.zopemag.com/Guides/miniGuide_ZopeSprinting.html) is a good introductory article; just mentally remove every \"Zope\" from the article to make it generic.

### Why sprint at PyCon? 

The sprints are intended to benefit the Python core, and to encourage more developers to take part in Python\'s development. They will also be a good place to see [ExtremeProgramming](ExtremeProgramming) or other [AgileMethods](./AgileMethods.html) in action, and to work closely with experienced Python developers. What would you like to see done, or at least attempted?

[PyCon](PyCon) will always have a core Python sprint. Other topics will come and go each year.

If you wish to participate in a sprint, please contact the sprint organizers in advance! Sprint topics are listed below.

### Sprints Being Planned for PyConDC2004 

Brief summaries of and links to approved sprints should go here.

- [CoreSprint](CoreSprint) \-- Coaches: Raymond Hettinger, Brett Cannon, and Guido van Rossum \-- work on various projects in the core Python project consisting of new features, documentation, and bug fixing. Will last all four days.

- [DocutilsSprint](DocutilsSprint) \-- Coach: David Goodger \-- Extend the Docutils project (including reStructuredText), aiming for inclusion in Python 2.4\'s standard library. Everyone welcome! No prior Docutils hacking experience is required. Participants should either be experienced Python programmers, or interested in documentation.

- [TwistedSprint](TwistedSprint) \-- There will be no [TwistedSprint](TwistedSprint) per se, but multiple mini-sprints related to Twisted. See [TwistedSprint](TwistedSprint) for more info.

- [Zope3Sprint](Zope3Sprint) \-- Coach: Jim Fulton. There will be a Zope 3 sprint. The tasks performed will depend on the interests of the participants and the things that need to be done.

- [Zope2Sprint](Zope2Sprint) \-- Coach: Chris [McDonough](./McDonough.html) \-- Not certain what to sprint on here, but a topic should come up soon. Recommended topics so far have been: bugathon, improved ZODB \"blob\" support, and documentation.

- [PloneSprint](PloneSprint) \-- Coach: Alan Runyan. A group of people familiar with Zope 2 and the Plone product with focus on performance and writing documentation on how to optimize Plone or Zope 2.

- [ChandlerSprint](ChandlerSprint) \-- Coaches: Ted Leung and Jeffrey Harris. Various topics around the Chandler repository.

- [GuidovanRobot](GuidovanRobot) \-- Coaches: Paul Carduner and Steve Howell.

### Proposed Sprint Topics 

Here are several topics that have been proposed but not yet accepted. If you think this would be a good sprint topic, add a comment in the wiki or send a comment to [Jeremy Hylton](mailto:jeremy@alum.mit.edu). In some cases, the topic has been assigned but the coach hasn\'t. Feel free to volunteer to coach one of these sprints.

- [Mailman3Sprint](Mailman3Sprint) \-- Coach: Barry Warsaw \-- Take experimental Mailman 3 code to a more viable state, concentrating especially on the major interfaces of the system. (Still tentative)

- [EmailSigSprint](EmailSigSprint) \-- Coach: Anthony Baxter or Barry Warsaw \-- Work on version 3.0 of the email library, in conjuction with discussions on the email-sig. (Still tentative)

- PyXMLSprint \-- There are a number of topics which would be worth working on, e.g. XMLSchema. \-- Martin v. Lwis

Other ideas:

- Jython sprint \-- work on some of the \"Jython should be fixed\" items from the [Jython website](http://www.jython.org/docs/differences.html)

- [DistutilsDependencies](./DistutilsDependencies.html) \-- implement a system to allow package authors to specify their dependencies, and have them automatically downloaded and installed when a user installs the package that needs the dependencies

- Distutils sprint \--
  - Finish the implementation of PEP262\'s [InstallationDatabase](./InstallationDatabase.html) class and have test cases for it.

  - The hard, messy part: update the Distutils code to update the package database when you do setup.py install.

  <!-- -->

  - The aimed-for end product could be an updated version of patch #562100 that would be ready for inclusion in Python 2.4. Optional items:

  - Build a Distutils \"uninstall\" command.

  - Write a crude command-line installer.

  - Update the [MacPython](MacPython) packager manager to use the database.

  - Make any PyPI changes that are required (to a test installation, not the live one on python.org).

    A related sprint will likely tackle [DistutilsDependencies](./DistutilsDependencies.html).

### Willing Participants Without a Particular Sprint Yet 

- [BobIppolito](BobIppolito) - Currently interested in [MacPython](MacPython), PyObjC, Stackless, [PyPy](PyPy), Distutils

- Nick Bastin - Core (Profiler) - UPDATE: Done, SF Patch 920509

- Aahz - Core, reST

- Barry Warsaw - MM3, Email, Core

- Neal Norwitz - Core, AST (Sat and/or Sun, not sure about Mon and Tue)

- [MichaelChermside](MichaelChermside) - Interested in a Jython sprint if anyone else will join me. Otherwise, I\'m available.

- Fred Drake - Docutils, [DistutilsDependencies](./DistutilsDependencies.html), distutils

- [DougFort](DougFort) - Chandler, any. If I find a job, I may not make Monday and Tuesday.

- Andrew Kuchling \-- Core, Distutils

- Jacob Hallén \-- Docutils, Twisted, Mailman \-- Will happily code Python to somebody\'s specification

- [PaulWinkler](PaulWinkler) \-- Zope 2, Zope 3, Plone.

- Brian Dorsey

- Tracy Ruggles \-- Docutils, Email, Chandler\...

- LD Landis \-- Core, Docutils, Twisted, Mailman, not arriving until Sunday.

### Logistics 

- Location:Kaiser and Elliott rooms, on the third floor. Time: 8AM - 6PM. Date: Saturday March 20 through Tuesday March 23 inclusive. Cost to attend: Free! Bring: Your laptop and a wireless card.

### Who makes this possible? 

The [Python Software Foundation](http://www.python.org/psf) is sponsoring the sprints for PyConDC2004. Please consider making a [donation](http://www.python.org/psf/donations.html) to support this vital community activity!
