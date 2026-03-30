# PyBots

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

### Welcome to Pybots, the Python Community Buildbots 

For the impatient: to view the buildmaster\'s status page, please select one of the following:

- [All](http://www.python.org/dev/buildbot/community/all/) builders

- Only builders for the [trunk](http://www.python.org/dev/buildbot/community/trunk/)

- Only builders for the Python [2.5](http://www.python.org/dev/buildbot/community/2.5/) branch

### A little history 

by Grig Gheorghiu (grig at gheorghiu dot net)

The idea behind the **Pybots** project is to allow people to run automated tests for their Python projects, while using Python binaries built from the very latest source code from the Python subversion repository.

The idea originated from [Glyph](http://glyf.livejournal.com/), of [Twisted](http://twistedmatrix.com/trac/) fame. He sent out a message to the python-dev mailing list (thanks to John J. Lee for bringing this message to my attention), in which he said:

*I would like to propose, although I certainly don\'t have time to implement, a program by which Python-using projects could contribute buildslaves which would run their projects\' tests with the latest Python trunk. This would provide two useful incentives: Python code would gain a reputation as generally well-tested (since there is a direct incentive to write tests for your project: get notified when core python changes might break it), and the core developers would have instant feedback when a \"small\" change breaks more code than it was expected to.*

Well, Neal Norwitz made this happen by setting up a buildmaster process on one of the servers maintained by the PSF. He graciously allowed me to maintain this buildmaster, and I already added a buildslave which runs the Twisted unit tests (in honor of Glyph, who was the originator of this idea) every time a check-in is made in the Python trunk or in the 2.5 branch.

If you are interested in participating in this project, please read these [Instructions on setting up a Pybots buildslave](http://agiletesting.blogspot.com/2006/08/setting-up-pybots-buildslave.html), take a look at the [PyBotsFaq](PyBotsFaq), then send a message to the [Pybots mailing list](http://lists2.idyll.org/listinfo/pybots) and I will send you a slavename and a password.
