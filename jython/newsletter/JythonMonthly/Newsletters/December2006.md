# JythonMonthly/Newsletters/December2006

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

::: {}
  -------------------------------- ---------------------------------------------------------------------------------------------------
  ***Jython Monthly***              ![](http://www.jython.org/css/jython.png "http://www.jython.org/css/jython.png")
  **December 2006 \-- Issue #6**   
  -------------------------------- ---------------------------------------------------------------------------------------------------
:::

Seasons Greetings!

Welcome to the December 2006 issue of Jython Monthly. The content of this newsletter will focus on using and developing the Jython languge.

I want to encourage the readers of Jython Monthly to send any articles, tips, tricks, or any other Jython related material to me if you think it should be distributed with this newsletter. Unfortunately, there were no article submissions for this month\'s edition of Jython Monthly. Hopefully we can have better luck next month!

I wish you and your families a very happy holiday!

\- Josh Juneau

Questions, comments, or suggestions?

Please send email to:

[jython-monthly@mchsi.com](mailto:jython-monthly@mchsi.com) or [jython-users@lists.sourceforge.net](mailto:jython-users@lists.sourceforge.net) for discussion.

# Article Call 

Unfortunately, we had no article submissions for this month\'s newsletter. All of the holiday activity must have had an impact on everyone\'s schedules. I know it has had an impact on mine!

I have had a recent interest in graphics and gaming development. There are some [articles](http://www.smallshire.org.uk/jython3d.htm) available regarding Jython and Java3D development, but I have not been able to find many concerning Jython game development.

As the editor of Jython Monthly, I\'d like to ask those Jython graphics and gaming developers to submit an article for next month\'s newsletter on such a topic. Be it a tutorial or just a simple example, it would be great to add some gaming or graphical tutorials to the online Jython library.

Until then, enjoy the holiday season! The next issue of Jython Monthly is scheduled to be distributed on January 9th, 2007.

\- Josh Juneau

# Tips and Tricks 

This is an old useful trick for referencing a static method within a Jython class.

    # direct, naive approach -- doesn't work...:
    class Class1:
        def static1(name):
            print "Hello",name

    # ...but now, a call such as:
    Class1.static1("John")
    # will fail with a TypeError, as 'static1' has become 
    # an unbound-method object, not a plain function.

    # This is easy to solve with a simple tiny wrapper:
    class Callable:
        def __init__(self, anycallable):
            self.__call__ = anycallable

    # toy-example usage:
    class Class2:
        def static2(name):
            print "Hi there",name
        static2 = Callable(static2)

    # now, a call such as:
    Class2.static2("Peter")
    # works just fine, and as-expected

Thanks to Alex Martelli for posting this recipe.

[Python Cookbook](http://aspn.activestate.com/ASPN/Cookbook/Python/Recipe/52304)

# Podcasts 

### Python 411 

An excellent Python podcast which is useful for keeping current on the Python language, and also for learning how to use many of it\'s features.

[Python 411 Site](http://www.awaretek.com/python/index.html)

# Jython Blogs 

[Jython Alive and Well and Looking For Love](http://headius.blogspot.com/2006/11/jython-alive-and-well-and-looking-for.html)

[IronPython and Jython](http://rebelwithoutamouse.blogspot.com/2006/11/ironpython-and-jython.html)

[Javalobby Forum](http://www.javalobby.org/java/forums/t84455.html)

# News 

### PyCon 2007 

[PyCon](./PyCon.html) 2007 is getting closer. The event is scheduled to take place in Addison, Texas (near Dallas) on February 23-25, 2007.

The list of talks is available [here](http://us.pycon.org/apps07/talks/). Frank Wierzbicki will be giving a talk entitled ***Jython for Python Developers***. Book your reservations today and do not miss out on the event!

## JavaOne Help 

The [JavaOne](./JavaOne.html) event will be held at the Moscone Center in San Francisco, California on May 8-11 2007. The *Call for Papers* is now open and there is a need for Jython presentations. If you are interested or would like to learn more about the event, please visit [JavaOne 2007 Site](http://java.sun.com/javaone/sf/index.jsp)

## 2.2 Beta Just Around the Corner 

Developers on the Jython project are predicting that the next beta release will be due out soon\...please stay tuned to [the Jython site](http://www.jython.org) for the most recent details on this upcoming release.

# Interesting Facts 

[Code Golf](http://codegolf.com:80/)

*Based on the original perl golf, Code Golf allows you to show off your code-fu by trying to solve coding problems using the least number of keystrokes.*

*You\'re not just limited to Perl either - PHP, Python and Ruby are all available too.*

*Challenges are always open, and your entries are automatically scored so you can start playing right away!*

------------------------------------------------------------------------

Jython - Average Job Salary & Stats in UK [http://www.itjobswatch.co.uk/jobs/uk/jython.do](http://www.itjobswatch.co.uk/jobs/uk/jython.do)

# Interested in Developing Jython? 

Check out the new [Porting Python Modules to Jython](http://wiki.python.org/jython/JythonDeveloperGuide/PortingPythonModulesToJython) guide which has been posted by Charlie Groves. This guide will help beginners get a quick start on developing Jython. Thanks for the guide Charlie.

If you are interested in developing Jython, please take a look at the [current bug listing](http://sourceforge.net/tracker/?func=browse&group_id=12867&atid=112867) and submit patches for items which you can repair.

# Useful Links 

::: {}
  ----------------------------------------------------------------
  **Links**
  [Jython Home](http://www.jython.org)
  [Python Home](http://www.python.org)
  [Jython WikiPedia](http://en.wikipedia.org/wiki/Jython)
  [Freshmeat.net](http://freshmeat.net/projects/jython/)
  [Python Daily News](http://www.pythonware.com/daily/)
  ----------------------------------------------------------------
:::
