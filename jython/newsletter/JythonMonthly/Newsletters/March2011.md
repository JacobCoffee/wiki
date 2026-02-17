# JythonMonthly/Newsletters/March2011

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

::: {}
  --------------------------------------- ---------------------------------------------------------------------------------------------------
  ***Jython Monthly***                     ![](http://www.jython.org/css/jython.png "http://www.jython.org/css/jython.png")
  **February/March 2011 \-- Issue #48**   
  --------------------------------------- ---------------------------------------------------------------------------------------------------
:::

This is the Jython Monthly newsletter for the months of February and March of 2011. Jython 2.5.2 has been released! Please download this release you haven\'t done so already to take advantage of the new features and bug repairs!

If you have any questions or suggestions for the newsletter, please feel free to send them to [jythonpodcast@gmail.com](mailto:jythonpodcast@gmail.com). I appreciate the feedback!

Thanks

My information is as follows:

Josh Juneau

- Podcast Website: [http://www.jythonpodcast.com](http://www.jythonpodcast.com)

- [jythonpodcast@gmail.com](mailto:jythonpodcast@gmail.com)

- Podcast Feed: [http://feeds.feedburner.com/JythonPodcast](http://feeds.feedburner.com/JythonPodcast)

## News 

**Jython 2.5.2 RC3 Has Been Released**

The Jython development team proudly announced the release of Jython 2.5.2 just ahead of [PyCon](./PyCon.html) 2011. This release is packed with bug repairs and quite a few enhancements to make Jython even better.

*New Features*

\* The socket module now includes ipv6 support

\* The socket module now also includes Internationalized Domain Names (RFC 3490) support on Java 6

\* Performance improvements around method invocation. 2.5.2 runs the richards benchmark 3x faster and the pystone benchmark 20% faster than 2.5.1

\* The posix/nt module was rewritten in Java and the performance of its often performance-critical stat function has significantly improved

\* Improved OSError errno messages on Windows

\* Slightly improved startup time (ongoing Issue #1380)

\* Better readline module emulation (required for IPython support)

\* Python functions can be directly passed to Java methods that take a single method interface (such as Callable or Runnable)

\* Google indexer

\* Lots of bug fixes!

Please go the [Jython downloads](http://www.jython.org/downloads.html) and grab the release today!

**Jython 2.6 Development Underway**

There was a Jython sprint at [PyCon](./PyCon.html) 2011 in which the developers were able to get underway with 2.6! If you are interested in viewing the roadmap or contributing to the release, please check out the [roadmap](http://wiki.python.org/jython/RoadMap) on the wiki to see what is actively being worked on at this time!

**Django-Jython 1.2.0rc1 Has Been Released**

The Django-Jython project has made release 1.2.0rc1 available. This release contains a handful of bug fixes since the 1.2.0b1 release in early March. The Django-Jython project is on- target to release 1.2.0 FINAL by the end of March given that no show stoppers remain within the bindings. There have been a couple of issues found regarding the use of the interactive console in Windows environments as well as the creation of superusers on Windows. However, these issues have been found to be linked to Jython proper, so there will have to be some work done there to repair the issues. I am on this issue at this time and will send updates to the Jython and Django-Jython developer mailing lists.

**Django 1.3 Has Been Released**

Altough not directly related to Jython, the Django web framework has released version 1.3 this past week. The overview states:

*Django 1.3's focus has mostly been on resolving smaller, long-standing feature requests, but that hasn't prevented a few fairly significant new features from landing, including:*

A framework for writing class-based views. Built-in support for using Python's logging facilities. Contrib support for easy handling of static files. Django's testing framework now supports (and ships with a copy of) the unittest2 library. There's plenty more, of course; see the coverage of new features below for a full rundown and details.

To download the latest release, please visit the [Django download](http://www.djangoproject.com/download/) page.

*The Django-Jython project is currently running tests against the Django 1.3 codebase and plans to release a beta for Django-Jython 1.3 as early as next week. Please download Django-Jython 1.3b1 once it is released and test!*

## Articles 

**The Prevalance of Non-Java languages on the JVM**

The current Java.net poll is showing some interesting early results. With the number of responses approaching 100 so far, the poll question How much of your JVM-based programming is in languages other than Java? reveals that just over half of the respondents replied \"All my JVM programming is in Java.\" In my experience, an even higher percentage of Java developers do not do any \"JVM programming\" outside the Java language itself. However, I\'ll admit that I had expected more than half of the respondents to a Java.net survey to be regular users of JVM languages other than Java. There has always been a disconnect between the everyday Java developer and the Java developer who regularly reads and responds to online Java community resources such as Java.net.

[Read More](http://www.javaworld.com/community/?q=node/7468)

**Scripting in Oracle Data Integrator: Jython, Java [BeanShell](./BeanShell.html), Java, Open Tools, ODI API & SDK, ODI Substitution API**

Here is another post on the various scripting options in ODI. It gives a brief overview when to use each and the advantages and disadvantages.

[Read Article](http://www.business-intelligence-quotient.com/?p=1161)

## Blogs 

[NQUAD Parsing Using Jython](http://captsolo.net/info/blog_a.php/2011/02/21/nquad_parsing_using_jython)

[Using Java Components from JRuby and Jython](http://rudamoura.com/jruby-jython.html)

[Networkspaces and Jython](http://watercooler.biola.edu/nurometic/tidbits/networkspaces-and-jython)

[Jython 2.5.2 Benchmarks 20% Faster](http://java.dzone.com/dose/daily-dose-release-jython-252)

[Python VM Summit Rough Notes](http://www.boredomandlaziness.org/2011/03/python-vm-summit-rough-notes.html)

[Live Processing with Jython Over ActiveMQ or Stomp](http://forum.processing.org/topic/live-processing-with-jython-over-activemq-or-stomp)

## Projects 

[jythonet](http://code.google.com/p/jythonet/)

jythonet is the best bridge between Jython and Java Servlet.

[Jython Documentation Set](http://sourceforge.net/projects/jythondocs/)

The Jython documentation set has been made available to the public via Sourceforge.net. If you would like to pull down the latest set of documentation for using Jython, go to the project and check it out. You can build the sources using Sphinx, and the sources are available via Mercurial. We are always looking for contributors, so if anyone is interested in helping keep the docs up to date, please grab a copy of them and send mail to the Jython-dev list for commit privileges.

## Video 

[Jython Concurrency](http://blip.tv/file/4881528) - Jim Baker

[Measuring Performance of Jython with OpenCore's Agent Bundle & Console](http://opencore.jinspired.com/?p=2623)

## Frameworks 

[Django-Jython Project](http://code.google.com/p/django-jython/)

[Pylons on Jython](http://wiki.pylonshq.com/display/pylonscookbook/Pylons+on+Jython)

[Web2Py](http://www.web2py.com/)

[Jython-Swingutils v1.0.1](http://bitbucket.org/agronholm/jython-swingutils/)

## IDE 

[Field Project](http://openendedgroup.com/field)

[PyDev 1.6.5](http://pydev.sourceforge.net/)

[Netbeans 7.0 Beta](http://www.netbeans.org)

[jHepWork](http://jwork.org/jhepwork)

[Intellij](http://www.jetbrains.com/idea/)

[Jython Processor with Swing GUI](http://jythonprocessor.sourceforge.net/)

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
