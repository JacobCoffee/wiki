# PyPySprint

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

## PyPy Sprint 

In the four days from 19th March till 22th March (inclusive) the [PyPy](PyPy) team will host a sprint on their new Python-in-Python implementation. The [PyPy](PyPy) project was granted funding by the European Union as part of its Sixth Framework Program, and is now on track to produce a stackless Python-in-Python Just-in-Time Compiler by December 2006. Our Python implementation, released under the MIT/BSD license, already provides new levels of flexibility and extensibility at the core interpreter and object implementation level.

Armin Rigo and Holger Krekel will also give talks about [PyPy](PyPy) and the separate py.test tool (used to perform various kinds of testing in [PyPy](PyPy)) during the conference.

Naturally, we are eager to see how the other re-implementation of Python, namely [IronPython](IronPython), is doing and to explore collaboration possibilities. Of course, that will depend on the degree of openness that Microsoft wants to employ.

The Pycon2005 sprint is going to focus on reaching compatibility with CPython (currently we target version 2.3.4) for our [PyPy](PyPy) version running on top of CPython. One goal of the sprint is to pass 60% or more of the unmodified regression tests of mainline CPython. It will thus be a great way to get to know CPython and [PyPy](PyPy) better at the same time! Other possible work areas include:

- translation to C to get a first working lower-level representation of the interpreter \"specified in Python\"
- integrating and implementing a full parser/compiler chain written in Python perhaps already targetting the new AST-branch of mainline CPython
- fixing various remaining issues that will come up while trying to reach the compatibility goal
- integrating or coding pure python implementations of some Python modules which are currently written in C.
- whatever issues you come up with! (but please tell us before hand so we can better plan introductions etc.)

If you have other interests feel free to suggest different sprint topics! Besides core developers Bea Düring, our \"process manager\" will be working off location (IRC/email) during the sprint to help improving and document our sprint and agile development process.

We are going to give tutorials about [PyPy](PyPy)\'s basic concepts and provide help to newcomers usually by pairing them with experienced pypythonistas. However, we kindly ask newcomers to be present on the first day\'s morning (19th of March) of the sprint to be able to give everyone a smooth start into the sprint. So far most newcomers have had few problems in getting a good start into our codebase. However, it is good to have the following preparational points in mind:

- experience programming in the Python language and interest to dive deeper

- subscription to [pypy-dev](http://codespeak.net/mailman/listinfo/pypy-dev) and [pypy-sprint](http://codespeak.net/mailman/listinfo/pypy-sprint).

- have a subversion-client, Pygame and graphviz installed on the machine you bring to the sprint.

- have a look at our current [documentation](http://codespeak.net/pypy/index.cgi?doc/), especially the [architecture](http://codespeak.net/pypy/index.cgi?doc/architecture) and [getting-started](http://codespeak.net/pypy/index.cgi?doc/howtopypy) documents.

The pypy-dev and pypy-sprint lists are also the contact points for raising questions and suggesting and discussing sprint topics beforehand. We are also on #pypy on freenode most of the time. Please don\'t hesitate to contact us or introduce yourself, your background and your interests!

## Logistics 

Organizational details will be posted to pypy-sprint and are or will be available in the Pycon2005-Sprint wiki here:

- [http://www.python.org/moin/PyConDC2005/Sprints](http://www.python.org/moin/PyConDC2005/Sprints)

## Registration 

send mail to [pypy-sprint@codespeak.net](mailto:pypy-sprint@codespeak.net), stating the days you can be present and any specific interests if applicable.

## Registered Participants 

If you aren\'t planning to be available for all four days of the sprints, please note which days you will be around.

- Jacob Hallén (Virginian Suites, near Rosslyn)
- Armin Rigo
- Samuele Pedroni (Virginian Suites, near Rosslyn)
- Anders Chrigström (Virginian Suites, near Rosslyn)
- Christian Tismer (Key Bridge, shares with Lutz))
- Richard Emslie (Econo Lodge Metro, shares with Holger)
- Holger Krekel (Econo Lodge Metro, shares with Richard)
- Lutz Pälike (Key Bridge, shares with Christian)
- Bob Ippolito
- Jonathan Riehl
- Alan Mcintyre (Washington Terrace Hotel)

------------------------------------------------------------------------

[CategoryPyCon2005](CategoryPyCon2005)
