# JythonMonthly/Newsletters/August2009

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

::: {}
  ------------------------------- ---------------------------------------------------------------------------------------------------
  ***Jython Monthly***             ![](http://www.jython.org/css/jython.png "http://www.jython.org/css/jython.png")
  **August 2009 \-- Issue #33**   
  ------------------------------- ---------------------------------------------------------------------------------------------------
:::

The podcast is also available at the podcast site (Available on 8/31/2009): [http://www.jythonpodcast.com](http://www.jythonpodcast.com)

I hope that you enjoy this month\'s issue, and please feel free to send me suggestions, questions, or feedback.

Thanks

My information is as follows:

Josh Juneau

- Podcast Website: [http://www.jythonpodcast.com](http://www.jythonpodcast.com)

- [jythonpodcast@gmail.com](mailto:jythonpodcast@gmail.com)

- Podcast Feed: [http://feeds.feedburner.com/JythonPodcast](http://feeds.feedburner.com/JythonPodcast)

## News 

**Jython 2.5.1 RC1 - To Be Released Soon!**

The Jython Developer team is hard at work for developing the 2.5.1 release. This release will be geared towards some performance boosts as well as bug fixes. The first release candidate is scheduled for early September, with indications pointing towards September 1!

*New Features*

\- Upgraded to ANTLR 3.1.3

\- \[ 1859477 \] Dynamically loaded [ServletFilters](./ServletFilters.html) like [PyServlet](PyServlet)

\- Built in JSR 223 scripting engine, with [LiveTribe](./LiveTribe.html) JSR 223 implementation for JDK 5

\- Jython \"-J-classpath cp_args_here\" now works as expected for unix shell.

*Bugs Fixed*

\- \[ 645615 \] cannot import through symbolic links

\- \[ 1366 \] parsing of lamda expression fails

\- \[ 1365 \] continuation lines fail in interactive interpreter

\- \[ 1377 \] Event names shadowed by a field name on Java types leads to a NPE

\- \[ 1381 \] Redundant declarations of interface implementation hides overriden methods

\- \[ 1189 \] MD5 hash is incorrectly calculated when string contains non-latin chars and using python md5 lib

\- \[ 1802339 \] Problem printing unicode when stdout intercepted

\- \[ 1145 \] Jython 2.5 compatibility problem with JSR 223

\- \[ 1400 \] Evaluating expression via JSR 223 [ScriptEngine](./ScriptEngine.html) returns null instead of True/False

\- \[ 1413 \] Array data type (PostgreSQL) is not supported (NPE)

\- \[ 1434 \] Cannot get return code from a process started with os.popen with Jython 2.5 (worked in 2.2)

\- \[ 1391 \] socket.getaddrinfo() breaks ftplib FTP client

\- \[ 1409 \] JSR-233 engine version numbers backwards

\- \[ 1408 \] JSR-223 engine doesn\'t implement I/O redirection

\- \[ 1393 \] [TypeError](./TypeError.html): \_new_impl(): expected 1 args; got 0

\- \[ 1415 \] ast Node creation fails with no arg constructors

\- \[ 1405 \] Executing [run].py from .jar throws exception([SystemExit](./SystemExit.html): 0) in main when sys.exit(0) is called

\- \[ 1439 \] Can\'t write() array.array

\- \[ 1139 \] crashes on isinstance

\- \[ 1430 \] Oracle JDBC Connection close

\- \[ 1406 \] Parsing a simple PEP 342 coroutine crashes Jython 2.5

\- \[ 1407 \] [ClassCastException](./ClassCastException.html) in plain Python coroutine

**The JVM Language Summit - September 16 - 18, 2009 at Sun Microsystems Santa Clara campus**

The 2009 JVM Language Summit is an open technical collaboration among language designers, compiler writers, tool builders, runtime engineers, and VM architects. About 75 language and VM implementers were able to attend last year---and 1/3 presented. You an see an agenda posted at jvmlangsummit.com

**[PyCon](./PyCon.html) 2010 Call or Tutorial Proposals is Now Open**

Do you enjoy teaching classes or tutorials? Are you good at it? [PyCon](./PyCon.html) 2010 is looking for proposals for tutorials. The [PyCon](./PyCon.html) Tutorial Days will be Wednesday February 17th & Thursday February 18th, 2010, followed by three Conference Days and four days of Development Sprints. here will be morning and afternoon tutorial sessions (3 hours each, plus a 30-minute break). Presenters may request multiple sessions, but must submit separate proposals (details below). Tutorials may be on any topic, but obviously should be instructional in nature.

[PyCon](./PyCon.html) 2010 will be held at the [Hyatt Regency Atlanta](http://atlantaregency.hyatt.com/hyatt/hotels/events/index.jsp) in downtown Atlanta, Georgia from February 17 through 25.

For more information, please visit the [PyCon](./PyCon.html) website at [http://us.pycon.org/2010/about/](http://us.pycon.org/2010/about/)

**Open Source Jython Book Available Online at jythonbook.com**

The [Jython Book](http://www.jythonbook.com) is now available online. This is an early first draft of the book and the book authors appreciate all feedback and suggestions. To see the source, please visit the [http://kenai.com/projects/jythonbook](http://kenai.com/projects/jythonbook). For information about feedback and commenting, please see the [wiki](http://kenai.com/projects/jythonbook/pages/Home).

## Blogs 

Blogs noted in **bold** are only presented in newsletter, not on podcast.

[Jython Shell Script Verbosity](http://www.stevemilner.org/blog/2009/08/08/jython-shell-script-verbosity) - Steve Milner

[Genral Shape Drawing Application with Jython and JFace](http://bit.ly/D6qWJ) - Darius

[Jython - Convert File to Byte Array](http://flexonjava.blogspot.com/2009/08/jython-convert-file-into-byte-array.html) - Lior Boord

[JDBC Connection Pool Status](http://ullaslinux.blogspot.com/2009/08/jdbc-connection-pool-status-using.html) - Ullas T

[GSoC Update](http://heshans.blogspot.com/2009/08/gsoc-update.html) - Heshan Suriyaarachchi

[GSoC Experience](http://heshans.blogspot.com/2009/08/gsoc-experience.html) - Heshan Suriyaarachichi

[Invokedynamic and Jython Part I](http://fwierzbicki.blogspot.com/2009/08/invokedynamic-and-jython-part-i.html) - Frank Wierzbicki

[jacl2jython Utility](http://wpcertification.blogspot.com/2009/08/jacl2jython-utility.html) - Websphere Certification Blog

[Faster Websphere wsadmin Jython Scripting with Imports](http://dohdolordollar.blogspot.com/2009/08/faster-websphere-wsadmin-jython.html) - Bill Birch

[Comparison Script Languages for the Fractal Geometry](http://mastrodonato.info/index.php/2009/08/comparison-script-languages-for-the-fractal-geometry/?lang=en) - Marco Mastrodonato

[Java Integration in Future Jython](http://journal.thobe.org/2009/08/java-integration-in-future-jython.html) - Tobias Ivarsson

[Jynx 0.3 - How to Fix Custom Class Loaders for Use with Jython](http://fiber-space.de/wordpress/?p=1089) - Kay Schluhr

**[Jython Websphere script to systematically change JDBC Provider Path](http://budilov.com/blog/?p=19) - Buddilov.com**

**[Issue with Python re Module and Jython](http://vrajasankar.blogspot.com/2009/08/issue-with-python-re-module-and-jython.html) - Rajasankar**

**[Python Programming](http://chipkidz.wordpress.com/2009/08/06/phython-programming/) - chipkidz**

**[Jython Web Application on Sun Web Server 7.0](http://ekschi.com/technology/2009/08/07/jython-web-application-on-sun-web-server-70-6) - teknologi**

## Frameworks 

[Django-Jython Project](http://code.google.com/p/django-jython/)

[Pylons on Jython](http://wiki.pylonshq.com/display/pylonscookbook/Pylons+on+Jython)

## Audio 

[Interview with Frank Wierzbicki for Webdevradio](http://www.webdevradio.com/index.php?id=93)

Michael Kimsal, editor of the [GroovyMag](./GroovyMag.html), had a great interview with Frank Wierzbicki this past month. The podcast is posted on webdevradio.com and it is available right now. In the interview they talk about lots of Jython-related topics, and they also do some comparisons between Jython and other languages such as Perl and PHP

## Jobs 

[ALATEC Hiring Jython Wargaming Developers](http://www.java-forums.org/jobs-offered/20812-alatec-hiring-wargaming-devs.html)

## Discussions 

[Comparison Ruby, Python, Php, Groovy, Jython, etc](http://www.pubbs.net/ruby/200908/48570/)

This is a discussion all about the blog post that we mentioned earlier. A post that compared each of the languages while using Fractal geometry. Lots of people posted their opinions and thoughts on the topic\...go and check out the discussion if interested in reading more about it.

## IDE 

[Field Project](http://openendedgroup.com/field)

[PyDev](http://pydev.sourceforge.net/)

[Netbeans 6.7.1](http://www.netbeans.org)

[jHepWork](http://jwork.org/jhepwork)

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
