# DCPythonNov2010Sprint

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# DCPython Meetup Sprint Plan (Nov 2010)

This is the project planning page for the [Python Beginner\'s Open Source Sprint](http://meetup.zpugdc.org/calendar/15036971/), organized by the [DCPython Meetup](http://meetup.zpugdc.org/) (primarily Alex Clark).

There are a lot of people planning to attend, so a little advance planning is worthwhile. If people can figure out what projects they want to work on and use this page to connect with others interested in the same projects, it should be easier to get ourselves organized when we get together.

This is organized with a section for each \"larger\" project. If you\'re interested in a project listed here, add your name and any emphasis you\'d like to bring to the sprint. If you want to work on a project not listed already, add it!

::::: 
### Beginners

Everyone attending the sprint that has never sprinted before, add your name under \"Developers\". If you plan to be available to help these folks, add your name and add (helper) afterward.

::: 
#### Developers

- [Alex Clark](AlexClark) (helper)
- [Fred Drake](FredDrake) (helper)
- Eric Groo
- Owen Martin
- Barry Austin
- Bob Schmertz
- Mohamed Ainab \<MohamedAinab\>
- Eric Palakovich Carr
- Londell
- Gabriel Getzie
- Mike Onzay
- Adam Reilly
- Sergejs Melderis
- Ryan Luu
:::

::: 
#### Tasks

- Pick a project
- Get your laptop setup for development
- Fix bugs!
:::
:::::

::::: 
### Python core

The interpreter and standard library.

::: 
#### Developers

- [Eric Smith](./EricSmith.html)
- [Fred Drake](FredDrake)
:::

::: 
#### Tasks

- [PEP-382](http://www.python.org/dev/peps/pep-0382/), namespace packages
- Add [alternate float format specifiers](http://bugs.python.org/issue7094) (and Decimal, if time)
- Straighten out the JSON issues:
  - [json.load failure when C optimizations aren\'t built](http://bugs.python.org/issue9233)
  - [Incomplete json tests](http://bugs.python.org/issue5723)
:::
:::::

::::: 
### distutils2 (d2)

The next generation of Python packaging. You\'ll need [Mercurial (hg)](http://mercurial.selenic.com/) for revision control, and several versions of Python. See [http://bitbucket.org/fdrake/d2dev/src/tip/README.txt](http://bitbucket.org/fdrake/d2dev/src/tip/README.txt) for detailed preparation instructions.

For this, it\'s important to use \"clean\" Pythons; you don\'t want to have any extras installed in your site-python directory.

::: 
#### Developers

- [Fred Drake](FredDrake)
- [Alex Clark](AlexClark)
- [Arc Riley](ArcRiley)
:::

::: 
#### Tasks

- Remove fancygetopt; move to a clean application of optparse.
- the command line tool is now in run.py, with new options, and pass it to dist+fancygetopt to call the old system so what could be done is to list:
  1.  all command line options in dist.py that are not a call to a command and its options
  2.  move them to run.py
  3.  remove fancygetopt and clean up dist.
- Try converting a few projects to use d2, preferably based on the documentation alone.
- Continue the work on py3 support (ask tarek or regebro on irc)
:::
:::::

::: 
### Zope Toolkit (ZTK)
:::

::::: 
### Django

Look at fixing some long-standing and reasonably trivial documentation issues. Shared exploration of the code base. Help 1.3 get out the door.

::: 
#### Developers

- [Steve Holden](SteveHolden) but not on my own! ;-)
- [Steve Waterbury](StephenWaterbury) but this is not a Steves-only project! ;-)
- [Alex Clark](AlexClark) Maybe I\'ll watch! :-)
- Eric Palakovich Carr
- Adam Reilly
:::

::: 
#### Tasks

- [http://code.djangoproject.com/ticket/4027](http://code.djangoproject.com/ticket/4027)
- [http://code.djangoproject.com/ticket/3529](http://code.djangoproject.com/ticket/3529)
- [http://code.djangoproject.com/wiki/Sprints#Preparingforthesprint](http://code.djangoproject.com/wiki/Sprints#Preparingforthesprint)

Possibly consider whether context objects might benefit from the use of structural modifications.
:::
:::::

::::: 
### Plone

Python-based, open-source CMS

::: 
#### Developers

- [Alex Clark](AlexClark)
:::

::: 
#### Tasks

- PloneSoftwareCenter add-on ([http://plone.org/products/plonesoftwarecenter](http://plone.org/products/plonesoftwarecenter)) development
  - Fix bugs: [http://dev.plone.org/plone.org/search?q=psc&noquickjump=1&ticket=on](http://dev.plone.org/plone.org/search?q=psc&noquickjump=1&ticket=on)
  - Fix broken tests
:::
:::::

::::: 
### Parse2Plone

Utility app for importing static website content into Plone

::: 
#### Developers

- [Alex Clark](AlexClark)
:::

::: 
#### Tasks

- Improve test coverage from 50% to 100% for parse2plone (you\'ll need a github account for this, so you can fork: [https://github.com/collective/parse2plone](https://github.com/collective/parse2plone) and send me pull requests.)
:::
:::::

::::: 
### zc.buildout

A tool for creating repeatable environments

::: 
#### Developers

- [Alex Clark](AlexClark)
:::

::: 
#### Tasks

- Fix bugs: [https://bugs.launchpad.net/zc.buildout](https://bugs.launchpad.net/zc.buildout)
:::
:::::

::::::::: 
[]

### DCPython Meetup Sprint Wrap Up

Here is a wrap-up of what was accomplished at the sprint.

::: 
#### Distutils2 (d2)

- People
  - **Fred Drake**
  - Alex Clark
  - Travis Pinney
  - Arc Riley
  - Jim Fulton
- Progress
  - Fred schooled Travis, Alex and Jim in distutils2 setup, with a dev environment from:
    - [http://bitbucket.org/fdrake/d2dev](http://bitbucket.org/fdrake/d2dev) and a distutils2 checkout from:
    - [https://bitbucket.org/tarek/distutils2](https://bitbucket.org/tarek/distutils2)
  - The group ran the tests, but unfortunately did not manage to get much further than that.
  - Fred worked on ripping out the \"Fancy option parser\" to replace it with optparse.
  - Arc added Python 3 support to distutils2 setup.py and started adapting its unit tests to run clean on Py3.
:::

::: 
#### Buildout

- People
  - **Jim Fulton**
  - Alex Clark
- Progress
  - Jim and Alex brainstormed on the status quo: \"brittle tests\" (i.e. tests giving spurious results depending on the system they are being run on), and then began to fix tests.
  - Jim worked on a test failure having to do with zc.recipe.egg tests that used the interpreter parameter to create a script ; the script being created in the tests used a technique only valid on newer ubuntus and Windows (where #!/path/to/exe refers to another script that has #!/path/to/exe instead of an executable)
  - Alex worked on a test having to do with Buildout being able to work with more than one version of Python ; so the test requires that more than one version of Python be found. I committed a \"modernization\" here: [http://svn.zope.org/zc.buildout/?rev=118514&view=rev](http://svn.zope.org/zc.buildout/?rev=118514&view=rev) \<[http://svn.zope.org/zc.buildout/?rev=118514&view=rev](http://svn.zope.org/zc.buildout/?rev=118514&view=rev)\> (to make the test find 2.6 and 2.5 vs. 2.4 and 2.3)
    - Alex plans to do further improvements that will make the test look for all 2.x versions.
:::

::: 
#### Beginners

- People

  - **Steve Holden**
  - Bob Schmertz
  - Anyone else?

- Progress

  - Steve Holden was corralled with the beginners and discussed basic Python concepts
  - Looked at urllib as a code example
  - Some of the beginners broke off to do a \"fun\" project.
    - The \"fun\" project group mostly worked on bootstrapping an Android environment to develop an Android app with Python. The project created is called \'ConnectUs\' and the project is hosted on Google Code. [http://code.google.com/p/connectus/](http://code.google.com/p/connectus/)
  - All participants joined on other projects after lunch.

  I think next time we need to be better prepared for the beginners, and have a simple project that they can work on.
:::

::: 
#### Python Core

- People

  - **Eric Smith**
  - Eric Groo
  - Vlad Korolev
  - Bob Schmertz
  - Owen Martin

- Progress

  - The core group worked on \"Alternate float formatting\", [http://bugs.python.org/issue7094](http://bugs.python.org/issue7094), which actually affects float, Decimal, and complex. Eric Smith has posted their patch, is cleaning it up and will commit it for Python 3.2.

  - Additional comments from Londell:

        During the sprint, I also worked on some python core stuff too.  I'm chasing a buffering issue in the pty code (that I stumbled upon before
        participating in the sprint).  Eric gave me some ideas of some people to who I could reach out for more info on the pty code base.

        Additionally, Arc and I had several discussions.  He challenged me to dig deeper into the C/Python bridging code, and he challenged me to
        rethink how I implement behavior in my code to handle C and Python exceptions in the bridging code.
:::

::: 
#### Django

- People
  - **Steve Holden**
  - Anyone else?
- Progress
  - Steve Holden and at Gabe Getzie worked on and submitted a documentation bug fix for issue #3529, a long-standing though minor bug in the documentation for context.update(). This served to refresh memory about the documentation setup.
:::

::: 
#### GeoDjango

- People:
  - Eric Palakovich Carr
  - Travis Pinney
  - Adam Reilly
  - Barry Austin
- Progress:
  - The GeoDjango group managed to get a patch out for [http://code.djangoproject.com/ticket/14284](http://code.djangoproject.com/ticket/14284).
:::
:::::::::
