# JythonMonthly/Newsletters/April2009

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

::: {}
  ------------------------------ ---------------------------------------------------------------------------------------------------
  ***Jython Monthly***            ![](http://www.jython.org/css/jython.png "http://www.jython.org/css/jython.png")
  **April 2009 \-- Issue #29**   
  ------------------------------ ---------------------------------------------------------------------------------------------------
:::

The podcast is also available at the podcast site: [http://www.jythonpodcast.com](http://www.jythonpodcast.com)

I hope that you enjoy this month\'s issue, and please feel free to send me suggestions, questions, or feedback.

Thanks

My information is as follows:

Josh Juneau

- Podcast Website: [http://www.jythonpodcast.com](http://www.jythonpodcast.com)

- [jythonpodcast@gmail.com](mailto:jythonpodcast@gmail.com)

- Podcast Feed: [http://jythonpodcast.hostjava.net/podcasts/podcasts.xml](http://jythonpodcast.hostjava.net/podcasts/podcasts.xml)

## News 

**Jython 2.5b4 Released**

The fifth beta for the 2.5 version of Jython has been released.

Per Frank Wierzbicki:

Jython 2.5b4 is available for download here: [http://downloads.sourceforge.net/jython/jython_installer-2.5b4.jar](http://downloads.sourceforge.net/jython/jython_installer-2.5b4.jar). See the installation instructions here: [http://www.jython.org/Project/installation.html](http://www.jython.org/Project/installation.html).

While no new features have been added since Beta 3, we have fixed a number of bugs. One of the bugs prompted an almost total re-write of our Tuple and List implementations, which is the reason that this is another beta and not a release candidate. Expect a release candidate real soon now.

We also applied a patch that allows Jython to function in a system that does not have write access to the filesystem so that Jython can run unpatched in Google App Engine. See here for more: [http://groups.google.com/group/google-appengine-java/web/will-it-play-in-app-engine](http://groups.google.com/group/google-appengine-java/web/will-it-play-in-app-engine).

This is a beta release so be careful.

**Django-Jython 1.0b1 Released**

This is a great milestone for the Django-Jython project. This project is focused on implementing Django on the Jython language and ensuring that the databases function correctly with Django on Jython. Release notes state that modjy integration and war management command are updated to work with Jython 2.5b2 and later. Added junitxmlrunner, a Django test runner for producing JUnit compatible XML output. WAR command has been updated changing \--include-py-libs option by renaming it to \--include-py-path-entries to avoid misinterpretations. Also, numerous bug fixes have been made.

Currently supporting only PostgreSQL database, but look for more in the near future.

[Django-Jython Home](http://code.google.com/p/django-jython/)

**[JavaOne](./JavaOne.html) 2009 Conference**

The [JavaOne](./JavaOne.html) conference will be held June 2nd through 5th at the Moscone center in San Francisco, CA. You can register online now.

Highlights for Jython include:

- BoF entitled \'Language Interoperability on the JVM Made Simple\' - Tobias Ivarsson

- Tech Session entitled \'Exploiting Concurrency with Dynamic Languages\' - Tobias Ivarsson

- Panel entitled \'Script Bowl 2009: A Scripting Languages Shootout\' - Roberto Chinnici, Sun Microsystems, Inc.; Thomas Enebo, Sun Microsystems, Inc. ; Rich Hickey, Clojure; Guillaume Laforge, [SpringSource](./SpringSource.html); Martin Odersky, EPFL; Raghavan Srinivas, Self; Frank Wierzbicki, Sun Microsystems, Inc.

- Tech Session entitled \'Toward a Renaissance VM\' - Brian Goetz, Sun Microsystems, Inc.; John Rose, Sun Microsystems

- Tech Session entitled \'Dynamic Languages Powered by Glassfish AS V3\' - Jacob Kessler, Sun Microsystems; Vivek Pandey, Sun Microsystems, Inc.

- Tech Session entitled \'Alternative Languages on the JVM Machine\' - Cliff Click, Azul Systems

[Register for JavaOne](http://java.sun.com/javaone/2009/registration.jsp)

**[EuroPython](./EuroPython.html) 2009 Conference**

Registration is now open for [EuropPython](./EuropPython.html), Europe\'s Premier Python Conference, which will take place from 28th June to 4th July 2009 in Birmingham, UK. For more details, please visit the website at www.europython.eu

**The Definitive Guide To Jython (with Django) to be Published by Apress**

Look for *The Definitive Guide to Jython (with Django)* to be published by Apress later this year. The book will include beginner to advanced materials covering the Jython language in entirety. Authors include Jim Baker, Frank Wierzbicki, Leo Soto, Victor Ng, and Josh Juneau. More details to follow\...

## PyCon 2009 - Jython Video and Slides 

Panel VMS - [http://us.pycon.org/2009/conference/schedule/event/21/](http://us.pycon.org/2009/conference/schedule/event/21/)

A Better Python for the JVM - Tobias Ivvarsson [http://us.pycon.org/2009/conference/schedule/event/32/](http://us.pycon.org/2009/conference/schedule/event/32/)

Jython Progress - Frank Wierzbicki [http://us.pycon.org/2009/conference/schedule/event/46/](http://us.pycon.org/2009/conference/schedule/event/46/)

Pylons on Jython - Philip Jenvey [http://us.pycon.org/2009/conference/schedule/event/50/](http://us.pycon.org/2009/conference/schedule/event/50/)

Django on Jython 101 - Leo and Jim [http://us.pycon.org/2009/conference/schedule/event/54/](http://us.pycon.org/2009/conference/schedule/event/54/)

## Articles 

Unfortunately, I found no articles for this month\'s newsletter.

## Blogs 

Blogs noted in **bold** are only presented in newsletter, not on podcast.

[PyCon 2009](http://fwierzbicki.blogspot.com/2009/04/pycon-2009.html) - Frank Wierzbicki

[Best PyCon Evar](http://www.sauria.com/blog/2009/04/03/best-pycon-evar/) - Ted Leung

[PyCon 2009 Summary](http://percious.com/blog/archives/28) - Percious.com

[Scripting Oracle UCM with Jython](http://bexhuff.com/2009/04/scripting-oracle-ucm-with-jython) - Bex Huff

[Jython Programming](http://techparade.blogspot.com/2009/04/jython-programming.html) - Thomas Beek

[Python Browser Games](http://metapep.wordpress.com/2009/04/04/python-browser-games-possible-or-fantasy/) - Meta Pepsite

[Load Runner vs The Grinder vs Apache JMeter](http://niyunjiu.javaeye.com/blog/361732) - niyunjiu

[Another Reason to Fool Around with Meta](http://tovganesh.blogspot.com/2009/03/another-reason-to-fool-around-with-meta.html) - V. Ganesh

[Jython on Google App Engine](http://jython.xhaus.com/?p=88) - Alan Kennedy

[Modjy Running on GAE](http://jython.xhaus.com/modjy-running-on-google-appengine/) - Alan Kennedy

[WSGI Apps on Google App Engine with Modjy](http://jython.xhaus.com/how-to-run-jython-wsgi-applications-on-google-appengine-with-modjy/) - Alan Kennedy

[Django-Jython 1.0b1 Released](http://blog.leosoto.com/2009/04/django-jython-10b1-released.html) - Leo Soto

[GSoC Application Accepted](http://yangyan5.blogspot.com/2009/04/gsoc-application-accepted.html) - Yang Yang

[The Future: Part I](http://blog.headius.com/2009/04/future-part-one.html) - Charles Nutter

[JDK7 Adaptation of Jython](http://robilad.livejournal.com/47962.html) - Robilad

**[Is Java the new COBOL?](http://nullpointers.wordpress.com/2009/04/05/is-jave-the-new-cobol/)**

**[Python Programming with JavaTM Class](http://www.booktraining.net/2009/04/python-programming-with-javatm-class.html)**

**[Python and Jython: They\'re the Main Two](http://kennethhansenhp.livejournal.com/2856.html)**

**[Using Jython Script to Deploy and Undeploy Apps in Weblogic 10](http://d-dixit.blogspot.com/2009/04/using-jython-scruit-to-deploy-and.html)**

**[Compiling Python with Jython](http://www.bemasher.net/archives/317)**

## Examples 

[Jython + Processing Example](http://gist.github.com/99571)

## IDE 

**Open Source Field Project**

The Field Project is about to release beta 7! This project is an open source IDE for JVM languages geared towards digital art and coding.

[Field Project](http://openendedgroup.com/field)

[PyDev](http://pydev.sourceforge.net/)

[Netbeans 6.5 and 6.7 beta](http://www.netbeans.org)

## Poll 

What would you like to see out of Jython the most? - RESULTS ARE IN!!!

- Better Performance - 30.8%
- Better Java Integration - 38.5%
- More Features - 30.8%

NEW POLL - Which database are you interested in using with Django on Jython? - NEW POLL

- MySQL
- PostgreSQL
- Oracle
- MS-SQL
- Other

[Click Here to Take Poll](http://www.surveymonkey.com/s.aspx?sm=3IJG1BKCStT4Wq_2fz4zZi_2fQ_3d_3d)

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
