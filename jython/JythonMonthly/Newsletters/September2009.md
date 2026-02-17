# JythonMonthly/Newsletters/September2009

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

::: {}
  ---------------------------------- ---------------------------------------------------------------------------------------------------
  ***Jython Monthly***                ![](http://www.jython.org/css/jython.png "http://www.jython.org/css/jython.png")
  **September 2009 \-- Issue #34**   
  ---------------------------------- ---------------------------------------------------------------------------------------------------
:::

The podcast is also available at the podcast site: [http://www.jythonpodcast.com](http://www.jythonpodcast.com)

I hope that you enjoy this month\'s issue, and please feel free to send me suggestions, questions, or feedback.

Thanks

My information is as follows:

Josh Juneau

- Podcast Website: [http://www.jythonpodcast.com](http://www.jythonpodcast.com)

- [jythonpodcast@gmail.com](mailto:jythonpodcast@gmail.com)

- Podcast Feed: [http://feeds.feedburner.com/JythonPodcast](http://feeds.feedburner.com/JythonPodcast)

## News 

**Jython 2.5.1 Final!**

The Jython Developer team has delivered the 2.5.1 final release. This release contains multiple bug fixes as well as a few new features.

*New Features*

\- Upgraded to ANTLR 3.1.3

\- \[ 1859477 \] Dynamically loaded [ServletFilters](./ServletFilters.html) like [PyServlet](PyServlet)

\- Built in JSR 223 scripting engine, with [LiveTribe](./LiveTribe.html) JSR 223 implementation for JDK 5

\- Jython \"-J-classpath cp_args_here\" now works as expected for unix shell.

\- zxJDBC supports the with-statement: connections are committed or rollbacked; cursors are closed

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

\- \[ 1466 \] wrong handling of append only files

\- \[ 1079 \] fixed regression on issue: twisted.python.threadable module: missing attribute \'\_RLock\'

\- \[ 1461 \] assert statement should lookup [AssertionError](./AssertionError.html) using getglobal

\- \[ 1425 \] distutils/util.py assumes too much posix

\- \[ 1457 \] Cannot write an array in a file opened in r+b mode.

\- \[ 1382 \] [cmp] on certain types raises [ArrayStoreException](./ArrayStoreException.html)

\- \[ 1443 \] Can\'t update() hashlib.sha1() with array.array(\'c\')

\- \[ 1444 \] Can\'t zlib.compress() with array.array(\'c\')

\- \[ 1458 \] Builtin codecs aren\'t available without standard lib

**The JVM Language Summit Took Place September 16 - 18, 2009 at Sun Microsystems Santa Clara campus**

The 2009 JVM Language Summit is an open technical collaboration among language designers, compiler writers, tool builders, runtime engineers, and VM architects. About 75 language and VM implementers were able to attend last year---and 1/3 presented. Visit the presentations at [http://wiki.jvmlangsummit.com/Presentations](http://wiki.jvmlangsummit.com/Presentations)

**[PyCon](./PyCon.html) 2010 Call is Now Closed**

[PyCon](./PyCon.html) 2010 will be held at the [Hyatt Regency Atlanta](http://atlantaregency.hyatt.com/hyatt/hotels/events/index.jsp) in downtown Atlanta, Georgia from February 17 through 25.

For more information, please visit the [PyCon](./PyCon.html) website at [http://us.pycon.org/2010/about/](http://us.pycon.org/2010/about/)

**Open Source Jython Book Available Online at jythonbook.com**

The [Jython Book](http://www.jythonbook.com) is now available online. This is an early first draft of the book and the book authors appreciate all feedback and suggestions. To see the source, please visit the [http://kenai.com/projects/jythonbook](http://kenai.com/projects/jythonbook). For information about feedback and commenting, please see the [wiki](http://kenai.com/projects/jythonbook/pages/Home).

## Blogs 

Blogs noted in **bold** are only presented in newsletter, not on podcast.

[Jython 2.5.1 Final Is Out](http://fwierzbicki.blogspot.com/2009/09/jython-251-final-is-out.html) - Frank Wierzbicki

[The Jython Programming Language - Interview with Frank Wierzbicki](http://www.thebitsource.com/2009/09/26/jython-programming-language-frank-wierzbicki/) - the bitsource

[Intersection of built-in Modules Between CPython, Jython, and IronPython](http://sayspy.blogspot.com/2009/09/intersection-of-built-in-modules.html) - Brett Cannon

[Python - Hibernate - Jynx](http://fiber-space.de/wordpress/?p=1108) - Kay Schluhr

[Language Choice = f(number of copies)](http://computinged.wordpress.com/2009/08/26/language-choice-fnumber-of-copies/) - Mark Guzdal

[No WLST cachedir with python-cachedir-skip](http://ghattus.com/2009/09/no-wlst-cachedir-with-python-cachedir-skip.html) - Satya Ghattu

[Accessing HTTP/JSON Services with JVM Based Languages](http://theschemeway.blogspot.com/2009/09/accessing-httpjson-services-with-jvm.html) - Dominique Boucher

[Roadmap for Python WSGI Specification](http://blog.dscpl.com.au/2009/09/roadmap-for-python-wsgi-specification.html) - Graham Dumpleton

[Jython/Swing Conway\'s Game of Life](http://young-programmers.blogspot.com/2009/09/jythonswing-conways-game-of-life.html) - Dave Briccetti

[Graphical User Interface with Jython](http://young-programmers.blogspot.com/2009/09/graphical-user-interface-with-jython.html) - Dave Briccetti

[Python IDEs](http://darshantrvd.blogspot.com/2009/09/python-ides-2.html) - Darshan

[State of Python on the JVM](http://www.infoq.com/news/2009/09/state-of-python-on-the-jvm) - Craig Wickesser

[Using Scripting in Real World Applications](http://blog.looplabel.net/2009/09/18/javazone-2009-utilizing-scripting-in-real-world-applications/) - Anders Sandvig

**[JVM Language Summit 2009 - Day 3](http://www.nearinfinity.com/blogs/bryan_weber/jvm_language_summit_2009_-_day_2.html)** - Bryan Weber

**[Using Jython to Query JMX Objects/Attributes](http://chillyupnorth.blogspot.com/2009/09/using-jython-to-query-jmx-objects.html)** - Marzubus

**[Processing Array Example - in Python](http://www.16kb.com/blog/?p=122)** - James Cordiner

**[Quick Start Grinder - Part 1](http://vsbabu.org/mt/archives/2009/09/01/quick_start_grinder_part_i.html)** - Vattekkat Satheesh Babu

**[Simple Swing Application on Jython](http://dbaktiar.wordpress.com/2009/09/03/simple-swing-app-on-jython-2/)** - Daniel Baktier

**[Python - String . Random . Files](http://dian-informatics.blogspot.com/2009/08/python-string-random-files.html)** - Dian

**[Websphere Application Server 7.0 Administration Guide](http://www.wowebook.com/e-book/others/websphere-application-server-7-0-administration-guide.html)** - wowebook

**[JRuby Architects Leave Sun](http://www.sdtimes.com/content/article.aspx?ArticleID=33718)** - SD Times

**[Jython Script to Extract metadata from Java Class Files](http://www.owasp.org/index.php/Jython_Script_to_extract_metadata_from_Java_class_files_(O2P))** - owasp.org

**[Using Jython Scripting Language with WSADMIN](http://www.jtopic.nl/archives/124)** - jTopic

**[Djangocon Day 3](http://controlroom.blogspot.com/2009/09/djangocon-day-3.html)** - Kirby

**[Intersection of built-in Modules Between CPython, Jython,and IronPython](http://ironpython-urls.blogspot.com/2009/09/intersection-of-built-in-modules.html)** - Michael Ford

**[Shared JVM Infrastructure](http://wiki.jvmlangsummit.com/Jython_-W-)** - JVM Language Summit Wiki

**[Dynamic and Lightweight Programming Languages](http://itspice.net/cms/library-tutorials-online-books-white-papers-ebooks-free-boooks/dynamic-and-light-weight-programming-languages)** - it Spice

**[jHepWork : A full-featured multi-platform data analysis framework for scientists, engineers, and students](http://javamation.blogspot.com/2009/09/jhepwork-full-featured-multi-platform.html)** - JAVAMATION

**[Elastic Python Deployment Networks](http://tetamap.wordpress.com/2009/09/26/elastic-python-deployment-networks/)** - Holger Krekel

**[Using Jython as Terracotta Command Line](http://mike.hostetlerhome.com/2009/09/23/using-jython-as-a-terracotta-command-line/)** - Mike Hostetler

**[Recursive Directory Walker Using Jython](http://ssscripting.wordpress.com/2009/09/28/recursive-directory-walker-using-jython/)** - geo

## Frameworks 

[Django-Jython Project](http://code.google.com/p/django-jython/)

[Pylons on Jython](http://wiki.pylonshq.com/display/pylonscookbook/Pylons+on+Jython)

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
