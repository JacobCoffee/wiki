# JythonMonthly/Newsletters/March2010

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

::: {}
  ------------------------------ ---------------------------------------------------------------------------------------------------
  ***Jython Monthly***            ![](http://www.jython.org/css/jython.png "http://www.jython.org/css/jython.png")
  **March 2010 \-- Issue #40**   
  ------------------------------ ---------------------------------------------------------------------------------------------------
:::

The podcast is also available now: [http://www.jythonpodcast.com](http://www.jythonpodcast.com).

I hope that you enjoy this month\'s issue. Please feel free to send me suggestions, questions, or feedback.

Thanks

My information is as follows:

Josh Juneau

- Podcast Website: [http://www.jythonpodcast.com](http://www.jythonpodcast.com)

- [jythonpodcast@gmail.com](mailto:jythonpodcast@gmail.com)

- Podcast Feed: [http://feeds.feedburner.com/JythonPodcast](http://feeds.feedburner.com/JythonPodcast)

## News 

**Jython 2.5.2 to be Released Soon**

The next release of Jython is coming, and it should arrive within the coming month. More information will be available about 2.5.2 once it has been released.

**Django 1.2 - Beta 1 Released**

The Django web framework has released version [1.2-Beta1](http://www.djangoproject.com/weblog/2010/feb/06/12-beta-1/). This is the next major release of the web framework that includes some great new features. While it is not yet functional with Jython, it is certainly a good one to keep an eye on.

For more information, please visit the [Django Weblog](http://www.djangoproject.com/weblog/2010/mar/).

## Articles 

No articles for March 2010.

## Blogs 

Blogs noted in **bold** are only presented in newsletter, not on podcast.

[The Grinder IDE: GrinderStone, 2.5.0 Release](http://slava-technical.blogspot.com/2010/02/grinder-ide-grinderstone-250-release.html) - Borislav Andruschuk

Primary goal of this release was fixing compatibility issues between several versions of Eclipse, The Grinder and [PyDev](./PyDev.html). Secondary goal was to add compatibility with recently release Jython 2.5.0 and 2.5.1. [Read More](http://slava-technical.blogspot.com/2010/02/grinder-ide-grinderstone-250-release.html)

[The JVM Crowd](http://www.ahmedsoliman.com/2010/03/01/the-jvm-crowd/) - Ahmed Soliman

The JVM is an industry-proven environment for enterprise applications development and it has been receiving lots of updates especially after moving to be open source. The only problem was the Java programming language in my opinion. Java is an excellent language for its simplicity and consistency (people may argue) but it's not a "modern" language and lacks most of the features that the current modern crowd is looking for. [Read More](http://www.ahmedsoliman.com/2010/03/01/the-jvm-crowd/)

[Embedding Jython Script in Java with ScriptEngine\...](http://szyzygycode.wordpress.com/2010/03/03/embedding-jython-script-in-java-with-scriptengine/) - The Darker Side of Programming

In an idle hour I did some more playing about with the Java [ScriptEngine](./ScriptEngine.html) (see the earlier post on !Reinventing the Wheel) and decided to see just how easy it was to introduce another [ScriptEngine](./ScriptEngine.html) into the mix. It was a toss-up between JRuby and Jython, but in the balance I went with Jython because it has certain benefits to work I frequently get engaged in relating to middleware, although I am altogether less familiar and comfortable with Jython/Python than JRuby/Ruby. [Read More](http://szyzygycode.wordpress.com/2010/03/03/embedding-jython-script-in-java-with-scriptengine/)

[Poll: Python Version](http://www.learningpython.com/2010/03/04/poll-python-version/) - Learning Python

There was a poll taking place on the learning python blog which asked which version of Python you are currently using. I can say that most Jython developers are more likely than not using 2.5, however, there are some that I know are locked into older versions for one reason or another. What version are you currently using? Unfortunately, I don\'t think the poll is open any longer, but you can still check out the results and it looks like the majority of people are using 2.6, although 2.5 is coming in second place, followed by 3.1. [View Poll](http://www.learningpython.com/2010/03/04/poll-python-version/)

[Book Review: The Definitive Guide to Jython](http://breaking-catch22.com/?p=140) - Mark Freeman

The authors describe this book as having the intended audience of a Java developer wishing to use a dynamic language other than Groovy orJRuby. This is a very accurate assessment.

The first section serves as a quick introduction to the Python language, however should not be completely skipped even by seasoned Python developers. As a Python and Java developer, it was good to see comparisons of similar features from both languages. In many cases, the authors took the time to show code examples from both languages, side by side. [Read More](http://breaking-catch22.com/?p=140)

[Replacing JythonC in Jython 2.5](http://hasandiwan.info/2010/03/replacing-jythonc-in-jython-25.html) - Hasan Diwan

I heard, on the jython podcast\'s latest episode, of a replacement for jythonc. After the flip, I\'ve edited Dan Cheahs jythonc replacement, compile.java, to add per file output and use the system-wide, platform-independant temporary directory, as denoted by the java.io.tmpdir property.[Read More](http://hasandiwan.info/2010/03/replacing-jythonc-in-jython-25.html)

[Working with Images Using Django on Jython](http://jj-blogger.blogspot.com/2010/03/working-with-images-using-django-on.html) - Josh Juneau

If you\'ve tried to use Django on Jython along with an [ImageField](./ImageField.html), you know well that Django on Jython does not support this field. This is because the [ImageField](./ImageField.html) in Django relies on the Python Imaging Library (PIL). Jython does not support the PIL since it is C based, and there is not currently a version of the PIL that has been ported to Java. [Read More](http://jj-blogger.blogspot.com/2010/03/working-with-images-using-django-on.html)

**[Using vSphere Java API in Jython and other JVM Languages](http://www.doublecloud.org/2010/03/using-vsphere-java-api-in-jython-and-other-jvm-languages/) - [DoubleCloud](./DoubleCloud.html)**

**[ODI Variables and the Operator Module](http://www.business-intelligence-quotient.com/?p=762) - Uli Bethke**

**[Maven, Jython, and Glassfish Example](http://www.adrianwalker.org/2010/03/maven-jython-glassfish-example.html) - Adrianwalker.org**

**[ODI Series - When is a planning refresh not a refresh](http://john-goodwin.blogspot.com/2010/03/odi-series-when-is-planning-refresh-not.html)**

**[http://aruna-inampudi.blogspot.com/2010/03/modify-integration-module-promoted.html](http://aruna-inampudi.blogspot.com/2010/03/modify-integration-module-promoted.html)**

**[Jython/Python Cheat Sheet](http://blog.cmaeda.com/2010/02/jython-python-cheat-sheet.html) - Chris Maeda**

**[Java Technology Predictions](http://gregluck.com/blog/archives/2010/03/java-technology-and-one-other-predictions-for-the-next-few-years/) - Greg Luck**

**[Sikuli Python Source Code with Pictures](http://divineprogrammer.blogspot.com/2010/03/sikuli-python-source-code-with-pictures.html) - Mikael Kindborg**

**[TOPCAT & STILTS](http://blogs.us-vo.org/news/?p=125) - US National Virtual Observatory News**

**[Using Vmware Vcloud API with Jython](http://blog.chmouel.com/2010/05/17/using-jython-with-the-vcloud-api/)**

## Threads 

[Question About Using Jython When Running a Receiving Socket in Python](http://stackoverflow.com/questions/2532943/a-question-about-using-jython-when-run-a-receving-socket-in-python)

[Breaking the Loop in Jython](http://stackoverflow.com/questions/2528192/breaking-the-loop-in-jython)

[Next Line in Jython](http://stackoverflow.com/questions/2520574/next-line-in-jython)

## Frameworks 

[Django-Jython Project](http://code.google.com/p/django-jython/)

[Pylons on Jython](http://wiki.pylonshq.com/display/pylonscookbook/Pylons+on+Jython)

[Web2Py](http://www.web2py.com/)

## IDE 

[Field Project](http://openendedgroup.com/field)

[PyDev 1.5.4](http://pydev.sourceforge.net/)

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
