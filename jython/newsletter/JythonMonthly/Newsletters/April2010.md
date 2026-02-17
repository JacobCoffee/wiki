# JythonMonthly/Newsletters/April2010

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

::: {}
  ------------------------------ ---------------------------------------------------------------------------------------------------
  ***Jython Monthly***            ![](http://www.jython.org/css/jython.png "http://www.jython.org/css/jython.png")
  **April 2010 \-- Issue #41**   
  ------------------------------ ---------------------------------------------------------------------------------------------------
:::

The podcast is will be available on April 4th: [http://www.jythonpodcast.com](http://www.jythonpodcast.com).

I hope that you enjoy this month\'s issue. Please feel free to send me suggestions, questions, or feedback.

Thanks

My information is as follows:

Josh Juneau

- Podcast Website: [http://www.jythonpodcast.com](http://www.jythonpodcast.com)

- [jythonpodcast@gmail.com](mailto:jythonpodcast@gmail.com)

- Podcast Feed: [http://feeds.feedburner.com/JythonPodcast](http://feeds.feedburner.com/JythonPodcast)

## News 

**Jython 2.5.2 to be Released This Week**

The Jython developer team has been working hard to get things in place for the next release of jython. After corresponding with some of the devs, it sounds like a release within the next 7 days is looking promising. Stay tuned for more\...if you are interested in seeing a list of enhancements and bug fixes for the upcoming release, please take a look at the [NEWS](http://jython.svn.sourceforge.net/viewvc/jython/trunk/jython/NEWS?revision=7056&view=markup) file.

**New upcoming book \"Scientific Data Analysis Using Jython scripting and Java\"**

A new book will be appearing in stores this fall entitled scientific data analysis using jython scripting and java. The premise for this book is as follows:

- Scientific Data Analysis using Jython Scripting and Java presents practical approaches for data analysis using Java scripting based on Jython, a Java implementation of the Python language. The chapters essentially cover all aspects of data analysis, from arrays and histograms to clustering analysis, curve fitting, metadata and neural networks. A comprehensive coverage of data visualisation tools implemented in Java is also included. Written by the primary developer of the jHepWork data-analysis framework, the book provides a reliable and complete reference source laying the foundation for data-analysis applications using Java scripting. More than 250 code snippets (of around 10-20 lines each) written in Jython and Java, plus several real-life examples help the reader develop a genuine feeling for data analysis techniques and their programming implementation. This is the first data-analysis and data-mining book which is completely based on the Jython language, and opens doors to scripting using a fully multi-platform and multi-threaded approach. Graduate students and researchers will benefit from the information presented in this book.

**SQLAlchemy 0.6 Has Been Released Including Jython Support**

Sqlalchemy 0.6 has been released with su port for jython 2.5.  [Philip Jenvey blogs](http://dunderboss.blogspot.com/2010/04/sqlalchemy-06-released-with-jython.html) that SQLAlchemy on Jython uses JDBC drivers via Jython\'s builtin zxJDBC DBAPI interface. It currently supports PostgreSQL, MySQL, Oracle and also MS SQL Server via jTDS.

Those are all well proven JDBC drivers, and they can be even easier to install than CPython C extension drivers. Just add their jar file to your CLASSPATH (or sys.path) and go, no compiling needed.

For all of you who are interested in learning more about using sqlalchemy with jython, take a look at the jythonbook either online in open source format, or in print from Apress.  The book covers sqlalchemy .06 beta.

## Blogs 

[How to install Python Libraries](http://freecog.com/?p=195) - [FreeCog](./FreeCog.html)

Not sure how to install python packages into jython?  If. You are unsure how to do so, just run the setup.py for the corresponding python package using jython setup.py. This is covered in the blog post along with some references to easy install.   For more information,  please take a look at the post. 

[Intercepting Java method invocations in Jython](http://slava-technical.blogspot.com/2010/04/when-ive-created-latest-version-of.html) - Borislav Andrschuk

Borislav Andrschuck has a nice post on intercepting java method invocations in jython. He writes:   When I\'ve created latest version of Grinderstone I got a problem when I cannot implement Java interface in Jython because the necessary interface is a package private. I\'ve choosed the way to create proxy around this interface if I cannot generate class using this interface using Jython (as you now Jython generates class bytecode and define it directly into classloader). For more information, please read this post.

[Options for WebSphere App Server Scripting](http://webspherecommunity.blogspot.com/2010/04/options-for-websphere-application.html) - WS Community Blog

The Websphere community blog had a post in April regarding options for web sphere scripting.    [WebSphere](WebSphere) Application Server (WAS) provides a scripting interface called wsadmin. wsadmin supports two scripting languages jacl\* and jython. Five objects are available when you use scripts: [AdminControl](./AdminControl.html): Use to run operational commands. [AdminConfig](./AdminConfig.html): Use to run configurational commands to create/modify WAS configuration. [AdminApp](./AdminApp.html): Use to administer applications. [AdminTask](./AdminTask.html): Use to run administrative commands. Help: Use to obtain general help.

WAS provides a number of aids to developers and system administrators for the development of wsadmin scripts. Different options that can be leveraged in developing wsadmin scripts are explained in the post. 

[Django vs Grails](http://western-skies.blogspot.com/2010/04/django-vs-grails.html) - Western Skies - Charles Anderson

Charles Anderson wrote a post for the Western Skies blog that compared Django with the Grails web framework.  While Charles admits that he has been a Python programmer for 15 years, he still gave a better rating to the Django framework for the plenty of reasons. To read on these reasons, please take a look at the post.

[Back To Jython DB4O](http://jimcassidy.ca/2010/04/19/back-to-jythondb4o-part-1/) - Jim Cassidy

Jim Cassidy has written na post stating that he was away from python for a while, but is coming back to it now and recommends reading the definitive guide to jython. 

## Articles 

[Scripting from Scratch:  Creating a Jython administrative script for websphere](http://public.dhe.ibm.com/software/dw/websphere/1004_gibson-pdf.pdf) - Bob Gibson

## Frameworks 

[Django-Jython Project](http://code.google.com/p/django-jython/)

[Pylons on Jython](http://wiki.pylonshq.com/display/pylonscookbook/Pylons+on+Jython)

[Web2Py](http://www.web2py.com/)

## IDE 

[Field Project](http://openendedgroup.com/field)

[PyDev 1.5.6](http://pydev.sourceforge.net/) - Now with Django Integration!

[Netbeans 6.8, 6.9 M1](http://www.netbeans.org)

[jHepWork](http://jwork.org/jhepwork)

[Intellij](http://www.jetbrains.com/idea/)

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
