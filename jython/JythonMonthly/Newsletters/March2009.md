# JythonMonthly/Newsletters/March2009

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

::: {}
  ------------------------------ ---------------------------------------------------------------------------------------------------
  ***Jython Monthly***            ![](http://www.jython.org/css/jython.png "http://www.jython.org/css/jython.png")
  **March 2009 \-- Issue #28**   
  ------------------------------ ---------------------------------------------------------------------------------------------------
:::

Welcome to the March 2009 edition of the Jython Monthly Newsletter. It is amazing to see what is going on in the Jython world today as opposed to a couple of years ago. The community is live and well, the language is evolving, and the options with Jython are growing. Jython 2.5 beta 3 is now out in public with release candidates soon to follow \*\* hopefully sooner than you think \*\*! Django is alive and running well on Jython 2.5, Pylons is now functional and well\...things are good!

I had the excellent opportunity to meet some of the Jython community and developers at the Jython BoF @ this year\'s [PyCon](./PyCon.html) event. I can tell you that everyone in the Jython community is talented and looking to take the language to the next level. The development team is looking to make the language better with regards to performance and Java integration, but also plans to move forward with new releases to help bring the language closer to the CPython distributed version. It was a great BoF and I thank everyone who attended.

Announced at the BoF, there will be a new Jython book published later this year. The Definitive Guide to Jython with Django will be available as an open-source documentation set as well as published by Apress this November. Authors include Jim Baker, Frank Wierzbicki, Leo Soto, Victor Ng, and myself. We are all looking forward to distributing this new book as Jython is in need for an updated documentation set covering the latest and greatest features.

Europython 2009 will run at the end of June. More details to come.

The podcast is also available at the podcast site: [http://www.jythonpodcast.com](http://www.jythonpodcast.com)

I hope that you enjoy this month\'s issue, and please feel free to send me suggestions, questions, or feedback.

Thanks

My information is as follows:

Josh Juneau

- Podcast Website: [http://www.jythonpodcast.com](http://www.jythonpodcast.com)

- [jythonpodcast@gmail.com](mailto:jythonpodcast@gmail.com)

- Podcast Feed: [http://jythonpodcast.hostjava.net/podcasts/podcasts.xml](http://jythonpodcast.hostjava.net/podcasts/podcasts.xml)

## News 

**Jython 2.5 Beta 3 released**

Jython 2.5 Beta 3 has been released this month. This is the last planned beta release prior to the release candidates. If you do not already have this version, [go and download](http://www.jython.org) it now!

**[EuroPython](./EuroPython.html) 2009 Conference**

Registration is now open for [EuropPython](./EuropPython.html), Europe\'s Premier Python Conference, which will take place from 28th June to 4th July 2009 in Birmingham, UK. For more details, please visit the website at www.europython.eu

**The Definitive Guide To Jython (with Django) to be Published by Apress**

Look for *The Definitive Guide to Jython (with Django)* to be published by Apress later this year. The book will include beginner to advanced materials covering the Jython language in entirety. Authors include Jim Baker, Frank Wierzbicki, Leo Soto, Victor Ng, and Josh Juneau. More details to follow\...

## Articles 

**Python Quick Start Using Netbeans IDE**

*Submitted by: Josh Juneau*

Python is an elegant, easy-to-use programming language that is enjoyable to learn and has lots of community support. Even better yet, Netbeans 6.5 makes it possible to use this elegant language from within your favorite IDE. With it\'s added support for various JVM and non-JVM languages, Netbeans 6.5 opens new doors to programmers giving them an easy-to-use environment for developing in many different languages. Why is learning Python any better than learning another language such as Java? Well, given that Python has a JVM-based alternative known as Jython, learning Python gives you the opportunity to produce software that can be delivered to just about any platform. Given that combined with it\'s elegant syntax and easy usage, Python is a good candidate to use for developing your applications.

[Read More](http://wiki.netbeans.org/NBPythonQuickStart)

## Blogs 

[Jython 2.5 Beta 3 Released](http://fwierzbicki.blogspot.com/2009/03/jython-25-beta-3-released.html) - Frank Wierzbicki

[Modjy Now Fully Integrated Into Jython](http://jython.xhaus.com/?p=77) - Alan Kennedy

[WSO2 Elevator Pitch](http://heshans.blogspot.com/2009/03/wso2-elevator-pitch.html) - WSO2

[Cython and Jython](http://monsieurcactus.blogspot.com/2009/03/cython-and-jython.html) - MONSIEURCACTUS

[Jython as an ANT Replacement](http://justinworrall.com/blog/?p=257) - Justin Worrall

[Biggest Problem with New Programming Languages](http://ninjamonkeys.co.za/2009/03/11/the-biggest-problem-with-new-programming-languages/) - Vaughn Dickson

[Deploying Pylons Apps to Java Servlet Containers](http://dunderboss.blogspot.com/2009/03/deploying-pylons-apps-to-java-servlet.html) - Philip Jenvey

[Jython 2.5 and snakefight for deploying Pylons w/ SQLAlchemy + Oracle](http://pieceofpy.com/index.php/2009/03/13/jython-25-and-snakefight-for-deploying-pylons-w-sqlalchemy-oracle/)

[Comparing Version Numbers in Jython/Python](http://sebthom.de/136-comparing-version-numbers-in-jython-pytho/) - Sebastian Thomschke

[Java Games](http://chinbilly.blogspot.com/2009/03/java-games.html) - Chin Billy

[Python IDE List](http://cary929.blogspot.com/2009/03/python-ide-list.html)

## IDE 

[PyDev](http://pydev.sourceforge.net/)

[Netbeans 6.5](http://www.netbeans.org)

## Discussions 

Taken from the Jython Users Mailing List:

Question: *What compilers, if any, will be included in the final release of 2.5?*

Answer via Frank Wierzbicki:

*I\'ll start by defining \"compile\" as translating Python source code to .class bytecodes in the case of Jython. In the old world, jythonc was a completely separate compiler with a completely separate model from the internal compilation model of Jython. Also, jythonc went a little beyond this definition of compiling and did what you might call \"freezing\" Jython code. By \"freezing\" I mean that jythonc exposed a more static version of the Jython code vs. how it is normally compiled.*

When Jython executes any code, even in an interactive session, even in \"eval\" and \"exec\", it first compiles the Python source directly into .class bytecodes. The old jythonc first turned Python source into Java source, and then executed javac on the result. For a number of technical reasons, modern Python source code cannot be translated into reasonable Java source code, and so jythonc had to go.

There are lots of ways to cover the same use cases that jythonc covered without using jythonc. Some good recipes:

For using Jython from Java code:

Simple and Efficient Jython Object Factories [http://wiki.python.org/jython/JythonMonthly/Articles/October2006/3](http://wiki.python.org/jython/JythonMonthly/Articles/October2006/3)

For packaging up your Jython apps:

Distributing Jython Scripts [http://wiki.python.org/jython/JythonFaq/DistributingJythonScripts](http://wiki.python.org/jython/JythonFaq/DistributingJythonScripts)

Also note that you can pre-compile your python scripts to .class files using:

jython \[jython home\]/Lib/compileall.py \[the directory where you keep your python code\]

We do know that these recipes lack some ease of use that will be missed from jythonc. We also know that the \"freezing\" behavior of jythonc is desirable from some sort of tool. The plan is to use the exact compiler that already produces .class files in Jython and do some bytecode decoration in this new project \"clamp\". Charlie Groves has already proven that this is a viable option with the work he has done with clamp.

There are a number of reasons that we have decoupled clamp from the main Jython project. The first is that Jython as a project is very useful without a jythonc. We need to get a 2.5 released, and we don\'t want to have it delayed by the clamp project. Another reason is that clamp is very experimental. Before we bring clamp into the Jython project and rename it \"jythonc\" (if we ever do that), we will want to know that we have designed it in a way that we can live with for many years to come.

We do want to make every effort to release clamp concurrently with Jython 2.5 GA, but I don\'t think we are ready to make that guarantee. Having said that, once Jython 2.5 comes out, clamp will become one of my highest priorities. We know that the jythonc replacements above are somewhat awkward.

## Poll 

What would you like to see out of Jython the most?

- Better Performance
- Better Java Integration
- More Features

[Click Here to Take Poll](http://www.surveymonkey.com/s.aspx?sm=PQWhsiEwtHFjuGS9bkS8ig_3d_3d)

::: {}
  ----------------------------------------------------------------
  **Links**
  [Jython Home](http://www.jython.org)
  [Python Home](http://www.python.org)
  [Jython WikiPedia](http://en.wikipedia.org/wiki/Jython)
  [Freshmeat.net](http://freshmeat.net/projects/jython/)
  [Python Daily News](http://www.pythonware.com/daily/)
  [Planet Jython](http://planet.jython.org/)
  ----------------------------------------------------------------
:::
