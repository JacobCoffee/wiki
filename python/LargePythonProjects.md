# LargePythonProjects

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# Description 

This page grew out of a frequently asked question on [CompLangPython](CompLangPython):

- *Are there any large projects written in Python?*

While the answer is unambiguously **Yes!**, it\'s a little bit trickier than that. For instance, we needed some clear way of defining *how* large a project is. And there were issues about people who wanted/didn\'t want attribution, and projects whose existence had to be kept secret (if we told you, we\'d have to kill you\...).

LOC(Lines Of Code)s are counted by [CLOC](http://cloc.sourceforge.net/). Only Python codes are included. Docstrings are counted as comments. Large projects are arbitrarily defined as more than 100,000 lines.

# New List 

::: {}
  --------------------------------- --------- ------------------------------------ -----------------------------------------------------------------------------------------------------------------------
  Name                              Version   LOC                                  Source access
  [TACTIC](TACTIC)           3.8       198949(blank 84138, comment 39926)   [Downloads](http://community.southpawtech.com/downloads)
  [Twisted](TwistedMatrix)   11.0.0    146136(blank 54971, comment 72686)   [SVN](http://twistedmatrix.com/documents/current/core/development/policy/svn-dev.html) releases/twisted-11.0.0
  [Django](Django)           1.3       115306(blank 26810, comment 35533)   [SVN](https://code.djangoproject.com/) releases/1.3
  [SQLAlchemy](SQLAlchemy)   0.7.2     113485(blank 32694, comment 24498)   [hg](http://www.sqlalchemy.org/develop.html) rel_0_7_2
  --------------------------------- --------- ------------------------------------ -----------------------------------------------------------------------------------------------------------------------
:::

# Old 

We decided to use [pycount](http://www.python.net/crew/gherman/pycount.html) to size the programs, and arbitrarily declared that any program of more than 10,000 lines was \"large\".

The following list is the result of that effort. Please feel free to add YOUR project as well!

# List 

::: {}
  ----------------------------- ------------------------------------------------ ------------ --------------------------------------------------- --------------
  Name                          Author                                           Size (loc)   Description                                         Last Updated
  Python (the language)         Various                                          290838       The parts of the Python project written in Python   2002-07-23
  lyntin                        Will Guaraldi, Joshua Berne, Lyn Adams Headley   11856        Extensible Mud client and framework                 2002-07-23
  omniORB                       Duncan Grisby                                    31377        CORBA Object Request Broker                         2002-07-23
  [MoinMoin](MoinMoin)   Juergen Hermann, Thomas Waldmann and others      37369        The wiki engine in Python                           2003-11-08
  [RoundUp](RoundUp)     [RichardJones](RichardJones) and others   40596        issue-tracking system                               2004-06-28
  Twisted                                                                        60000+                                                           
  Django                        Lawrence Journal-World                           59111        web application framework                           2010-07-15
  ----------------------------- ------------------------------------------------ ------------ --------------------------------------------------- --------------
:::
