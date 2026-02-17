# PyCon2006/Tutorials/AgileDevelopmentAndTestingInPython

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

## Agile development and testing in Python 

### Summary 

We will present a Python application that we developed together as an \"agile team\", using agile development and testing approaches, techniques and tools. The value of the tutorial will consist on one hand in detailing the development and testing methodologies we used, and on the other hand in demonstrating specific Python tools that we used for our development and testing. We will cover TDD, unit testing, code coverage, functional/acceptance testing, Web application testing, continuous integration, source code management, issue tracking, project management, documentation, Python package management.

### Outline 

1st hour:

- Intro: agile development and testing concepts

- Source control management ([subversion](http://subversion.tigris.org/)) and issue tracking/project management ([Trac](http://www.edgewall.com/trac/))

- TDD/unit testing ([py.test](http://codespeak.net/py/current/doc/test.html), [doctest](http://docs.python.org/lib/module-doctest.html), [nose](http://somethingaboutorange.com/mrl/projects/nose/), [TestOOB](http://testoob.sourceforge.net/))

- unit tests as documentation ([doctest and epydoc](http://agiletesting.blogspot.com/2005/02/agile-documentation-with-doctest-and.html))

2nd hour:

- code coverage (the [coverage](http://www.nedbatchelder.com/code/modules/coverage.html) module)

- source code analysis ([pylint](http://www.logilab.org/projects/pylint), [pyflakes](http://divmod.org/projects/pyflakes))

- acceptance/functional testing ([PyFit/FitNesse](http://agiletesting.blogspot.com/2004/11/writing-fitnesse-tests-in-python.html), [TextTest](http://texttest.org/))

- performance testing ([FunkLoad](http://funkload.nuxeo.org/), [twill](http://www.idyll.org/%7Et/www-tools/twill.html))

3rd hour:

- Web application testing with [Selenium](http://confluence.public.thoughtworks.org/display/SEL/Home) and twill

- Scripting Selenium tests using a [Twisted-based server](http://agiletesting.blogspot.com/2005/03/web-app-testing-with-python-part-2.html)

- Python package management ([distutils](http://docs.python.org/lib/module-distutils.html), [setuptools](http://peak.telecommunity.com/DevCenter/setuptools), [Cheesecake index](http://pycheesecake.org))

- Continuous integration and \'smoke test\' ([buildbot](http://buildbot.sourceforge.net/))

### Audience 

Python developers and testers interested in agile methodologies

### Presenter contact info 

- [Grig Gheorghiu](http://agiletesting.blogspot.com) \<grig at gheorghiu dot net\>

- [Titus Brown](http://www.advogato.org/person/titus/) \<titus at caltech dot edu\>
