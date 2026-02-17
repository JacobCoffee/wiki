# DistutilsBof

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# Followup 

There will be a follow-up Open Space meeting on Friday at 11:30 am.

Someone should volunteer to act as a scribe for the meeting.

# Distutils BoF Topics 

There have been many proposals for changes and improvements to `distutils`{.backtick}, but any actual activity on improving `distutils`{.backtick} appears to have come to a complete halt. All activity has moved to third-party tools which layer on top of `distutils`{.backtick}.

There is a case to be made for integrating the best of the enhancements directly into `distutils`{.backtick} itself, with the most important being shared maintenance and making the tools readily available for use by smaller distributions. Currently, many larger distributions of Python code are incorporating `distutils`{.backtick} extensions directly into their distributions. This isn\'t much of a problem for large distributions (like Zope and PEAK), but seems out of place for smaller distributions of a single package (like `ZConfig`{.backtick}).

The extensions which we should consider adding directly to distutils include:

- Support for installing both modules and packages from a single distribution.

- Support for more easily installing data files into a package. Phillip Eby\'s `setuptools`{.backtick} has implemented one reasonable approach to this; there may be others.

- The ability to install packages into other packages without having to hack around in *setup.py* scripts. (For example, the option to install `zope.app.sqlscripts`{.backtick} into an existing installation of `zope.app`{.backtick}.)

- Some ability to use more declarative forms of metadata from *setup.py* without having to write a pile of extension code. This is being explored some at Zope Corporation.

- Dependency support. This is also being worked on by Phillip Eby, but it would be nice to get more information from the community about the requirements.

Anthony Baxter, [FredDrake](FredDrake), [BobIppolito](BobIppolito), and Kapil added a very simple dependency mechanism on Monday; we can discuss what was done and whether it\'s sufficient.

(Guys: you might have a look at setuptools.depends and setuptools.command.depends in the sandbox, as the dependency mechanisms there are more fleshed out (including unit tests), although they are not as smoothly integrated with distutils (e.g., I don\'t have a \"skip\" option for dependency checking yet). In particular, note that using import as a dependency checking mechanism will fail when installing to a directory not on the current PYTHONPATH; setuptools\' dependency checking can handle this correctly, even in the presence of \'extra_path\'. Also, I\'m awfully YAGNI on *provides* in general. What are the use cases? \--PJE)

\[\'provides\' is to allow packages to specify \_what\_ they provide. We can\'t use the name of the package, as often it\'s different (e.g. Twisted vs twisted). The next step will be to submit these provides lines to PyPI, so we can look them up. The \'import\' hack is just there because we don\'t have the installation database yet - this can be removed at that point. \-- anthony\]

(But what\'s the use case for packages specifying what they provide? If I rely on Twisted, why not just say I rely on Twisted? What\'s the point of having another entity? Also, how does the installation database help with existing distributions, and packages that someone installed \*before\* the database exists? That approach will have backwards-compatibility problems in deployment for an extended period, while an explicitly backwards-compatible approach could work \*now\*. \-- PJE)

# Attendees 

The following people showed up for the first hour of the BOF; once we\'d overrun our time in room 308, a much smaller subset of this group relocated to the amphitheatre to continue discussions.

- [FredDrake](mailto:fdrake@acm.org)

- Andrew Kuchling

- [BobIppolito](BobIppolito)

- Zac Bir

- Mike Orr

- Yannick Loitiere

- Tamer Fahmy

- Nathan Yergler

- Anna Ravenscroft

- Eric Smith

- Brian Dorsey

- Kevin Cole

- David Handy

- John Miller

- Barry Warsaw

- Lloyd Kvan

- Paul Prescod

- David Ascher

- Trent Mick

- Pearu Peterson

- Nester Nissen

- Tom Cocagne

- Michael Cariaso

- Eric Jones

- Steve Waterbury

This was a much larger group than expected from the initial response in this wiki; I\'ll apologize for not organizing more of an agenda.

# General Review 

Discussion quickly led to Fred realizing that people characterize distutils in two very different ways. Many people talked about distutils as a build framework, and others see it as a packaging system/tool. Both aspects are important to have available, but they are not equally important to everyone. Someone with time on their hands should consider more clearly separating the two aspects so that either can be used separately; this is perhaps of more concern to people who want to use distutils as a build system.

One proposal was to either use [SCons](http://www.scons.org/) as a foundation for the build component, or to factor out a common base set of functionality.

***(There\'s more to say here; please add it if you can, since I\'ll probably forget it before I get around to writing about it here.)***
