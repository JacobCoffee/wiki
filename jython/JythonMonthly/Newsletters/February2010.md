# JythonMonthly/Newsletters/February2010

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

::: {}
  --------------------------------- ---------------------------------------------------------------------------------------------------
  ***Jython Monthly***               ![](http://www.jython.org/css/jython.png "http://www.jython.org/css/jython.png")
  **February 2010 \-- Issue #39**   
  --------------------------------- ---------------------------------------------------------------------------------------------------
:::

The podcast is also available now: [http://www.jythonpodcast.com](http://www.jythonpodcast.com) and it includes a quick review of the Dreampie Python shell under the Windows environment.

I hope that you enjoy this month\'s issue. Please feel free to send me suggestions, questions, or feedback.

Thanks

My information is as follows:

Josh Juneau

- Podcast Website: [http://www.jythonpodcast.com](http://www.jythonpodcast.com)

- [jythonpodcast@gmail.com](mailto:jythonpodcast@gmail.com)

- Podcast Feed: [http://feeds.feedburner.com/JythonPodcast](http://feeds.feedburner.com/JythonPodcast)

## News 

**Jython 2.5.2 to be Released Next, 2.6 Later This Year**

During the activities at [PyCon](./PyCon.html) 2010, the Jython developer base decided that 2.5.2 will be released next (perhaps within the next couple of months), followed by the release of 2.6 later this year. The 2.5.2 release will focus on bugfixes and a few code improvements. The general consensus is that the move to 2.6 will help bring more developers to Jython as it will be easier to work with. A Jython 2.6 release would bring Jython to the latest CPython 2.x production version today. CPython 2.7 is under active development, with a beta to be released this spring. However, instead of tracking this release, Jython development will target a 3.x release. If enough demand materializes for a Jython 2.7 release, we may consider backporting features from 3.x to 2.7.

**Dreampie 1.0 is Released**

[DreamPie](./DreamPie.html) is a Python shell which is designed to be reliable and fun.

[DreamPie](./DreamPie.html) was designed from the ground up to bring you a great interactive Python experience:

[DreamPie](./DreamPie.html) features a new concept for an interactive shell: the window is divided into the history box, which lets you view previous commands and their output, and the code box, where you write your code. This allows you to edit any amount of code, just like in your favorite editor, and execute it when it\'s ready. You can also copy code from anywhere, edit it and run it instantly. The Copy code only command will copy the code you want to keep, so you can save it in a file. The code is already formatted nicely with a four-space indentation. Features automatic completion of attributes and file names. Automatically displays function arguments and documentation. Keeps your recent results in the result history, for later user. Can automatically fold long outputs, so you can concentrate on what\'s important. Lets you save the history of the session as an HTML file, for future reference. You can then load the history file into [DreamPie](./DreamPie.html), and quickly redo previous commands. Supports interactive plotting with matplotlib. (You have to set \"interactive: True\" in the matplotlibrc file for this to work.) Supports Python 2.5, Python 2.6, Jython 2.5, [IronPython](./IronPython.html) 2.6 and Python 3.1. Works on Windows, Linux and Mac. (Mac support requires [MacPorts](./MacPorts.html).) Extremely fast and responsive. Free software licensed under GPL version 3.

**[PyDev](./PyDev.html) 1.5.5 Released**

Details on Pydev: [http://pydev.org](http://pydev.org)

Details on its development: [http://pydev.blogspot.com](http://pydev.blogspot.com)

Release Highlights:

\* Predefined completions available for code completion:

- Predefined completions may be created for use when sources are

not available

- Can also be used for providing better completions for compiled

modules (e.g.: [PyQt](./PyQt.html), wx, etc.)

- Defined in .pypredef files (which are plain Python code)
- Provides a way for generating those from a QScintilla .api file

(experimental)

- See Predefined Completions in manual for more info

\* Pydev Package Explorer:

- Showing the contents of the PYTHONPATH from the interpreter for

each project

- Shows the folder containing the python interpreter executable

(to browse for docs, scripts, etc)

- Allows opening files in the interpreter PYTHONPATH (even inside zip files)

\* Editor options:

- Find/replace dialog has option to search in currently opened editors
- Move line up/down can move considering Python indentation (not default)
- Simple token completions can have a space or a space and colon

added when applied. E.g.: print, if, etc (not default)

\* Refactoring:

- Fixed [InvalidThreadAccess](./InvalidThreadAccess.html) on refactoring

- Fixed problem doing refactoring on external files (no file was found)

\* Globals Browser (Ctrl+Shift+T):

- No longer throwing [NullPointerException](./NullPointerException.html) when the interpreter is

no longer available for a previously found token

\* General:

- When creating a new pydev project, the user will be asked before

changing to the pydev perspective

- Only files under source folders are analyzed (files in the

external source folders would be analyzed if they happened to be in the Eclipse workspace)

- Interactive console now works properly on non-english systems
- Hover working over tokens from compiled modules (e.g.: file,

file.readlines)

- JYTHONPATH environment variable is set on Jython (previously

only the PYTHONPATH was set)

- Fixed path translation issues when using remote debugger
- Fixed issue finding definition for a method of a locally created token

## Articles 

[Running Python Code in Java, the Jython Way](http://thepaksoft.net/usman/?p=506)

I am back with another technical article after ages though this time I am not sorry for being irregular over my blog because my life is going pretty smooth in general and I'm loving the way things are moving especially I'm thankful to my Tazu whom presence is making all the difference here . Now lets move on towards the topic. I was not any hardcore fan of python but recently I became one. Since I had to develop few applications for my mobile using this language I found it pretty easy and rich featured plus too simple. But the best part was when I found out that we can integrate this language within Java and run Python code from Java as well. This wasn't something too new since I had an experience of using Assembly along with code of c++ but that was the case of a low-level language with a high-level one but here both languages are high level. [Read More](http://thepaksoft.net/usman/?p=506)

[Python with ZK](http://docs.zkoss.org/wiki/Python_With_ZK)

Many people seem to want to use Python with ZK (actually Jython of course but let\'s just stick to the name Python to avoid confusion). Although there are performance penalties for using Python it certainly makes prototyping a lot quicker. With a small number of users the performance hit may not even be a problem.

The only examples of using Python with ZK seem to be limited to simple \<zscript\> included in the ZUL files. [Read More](http://docs.zkoss.org/wiki/Python_With_ZK)

## Blogs 

Blogs noted in **bold** are only presented in newsletter, not on podcast.

[Benchmarking JSR-223 Java Integration](http://tiagofernandez.blogspot.com/2010/01/benchmarking-jsr-223-java-integration.html) - Tiago Fernandez

The following micro-benchmark covers Java integration with [JavaScript](JavaScript), Python, Groovy and Ruby through JSR-223 via Rhino, Jython, Groovy and JRuby, respectively. The similar implementations calculate with Fibonacci numbers from 1 to 35 (e.g. 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ..., 9227465) recursively, populate the values in a JTree and displays it with a Frame. Although simple, this task proves valuable because it measures how a scripting engine behaves when calling Java code. [Read More](http://tiagofernandez.blogspot.com/2010/01/benchmarking-jsr-223-java-integration.html)

[My New Job at Sauce Labs](http://fwierzbicki.blogspot.com/2010/02/my-new-job-at-sauce-labs.html) - Frank Wierzbicki

I joined Sauce Labs as of January 3 this year. I met the people at Sauce Labs during the recent startup crawl in San Francisco (what a great way to find an employer, eh?). Sauce Labs is based around support for the open source Selenium functional testing framework. The inventor of Selenium, Jason Huggins is a founder. I joined Sauce Labs at the same time as Jim Baker and Raymond Hettinger, see here for more. The entire team at Sauce Labs is mind blowingly amazing - which is the main reason that I had to join. [Read More](http://fwierzbicki.blogspot.com/2010/02/my-new-job-at-sauce-labs.html)

[PyCon 2010 Brings Speed Enhancement to Python 3](http://www.linux.com/community/blogs/pycon-2010-brings-speed-enhancement-to-python-3.html) - Linux.com

Python 3 will zoom forward at [PyCon](./PyCon.html) 2010 with the incorporation of Unladen Swallow, a performance-boosting branch of Python initiated by engineers from Google. First made public at [PyCon](./PyCon.html) 2009, Unladen Swallow is already accelerating Python applications at several companies. Now the Unladen Swallow team plans to merge their code into Python 3\'s codebase, promising big speed improvements to Python 3 and a major new incentive for Python programmers to adopt the next-generation version of the Python language. [Read More](http://www.linux.com/community/blogs/pycon-2010-brings-speed-enhancement-to-python-3.html)

[Hey, Oracle!](http://catherinedevlin.blogspot.com/2010/02/hey-oracle.html) - Catherine: [PyOraGeek](./PyOraGeek.html)

In the last couple months, we\'ve learned that the new Sun will be going forward without Frank Wierzbicki, the Jython project lead, and now without Ted Leung.

The Oracle Technology Network is working hard to foster dynamic language use with Oracle. It\'s got publications, [PyCon](./PyCon.html) sponsorship, resources, and so forth. OTN delights me. [Read More](http://catherinedevlin.blogspot.com/2010/02/hey-oracle.html)

[Single File Python Apps](http://waf-devel.blogspot.com/2010/02/storing-binary-data-in-python-files.html) - waf-devel

Yet, redistribution is even easier when the application is platform-independent (scripts) and when the application is directly executable.

A naive approach for Python software is to concatenate all the dependent scripts into a single scripts. In the case of Waf, the tools are actually plugins which are not meant to be loaded all at once. Also, the resulting script would have a pretty huge size. [Read More](http://waf-devel.blogspot.com/2010/02/storing-binary-data-in-python-files.htm)

[Set Up Credit Installment Plan Dates Using java.util.Calendar in Jython](http://dbaktiar.wordpress.com/2010/02/03/setup-credit-installments-plan-dates-using-java-util-calendar-in-jython/) - Daniel Baktier

This blog shows an example on how Jython will make it easier for you to explore Java library or API.

In this sample I try to show how Jython could be used to learn a Java platform library or API interactively. Hopefully without going through the pain of code-compile-deploy-test cycles. After being familiar with certain library or API, we could come back the regular Java way to code. [Read More](http://dbaktiar.wordpress.com/2010/02/03/setup-credit-installments-plan-dates-using-java-util-calendar-in-jython/)

[Other Python VMs Upcoming Version Plans](http://trentmick.blogspot.com/2010/02/other-python-vms-upcoming-python.html) - Trent Mick

[New Python Shell is a Dreampie](http://www.h-online.com/open/news/item/New-Python-shell-is-a-DreamPie-936630.html) - H

[DreamPie](./DreamPie.html), a new interactive shell for Python developers, has been released with support for Python 2.5, 2.6 and 3.1, Jython 2.5 and [IronPython](./IronPython.html) 2.6. [DreamPie](./DreamPie.html) is described as a \"new concept for an interactive shell\", with the display divided into a history box for commands and a code box for \"in work\" Python code. The shell provides automatic completion of attributes, displays function arguments and documentation, can save session history as a HTML file and allows for interactive plotting with matpotlib. [Read More](http://www.h-online.com/open/news/item/New-Python-shell-is-a-DreamPie-936630.html)

[PyCon 2010 Sunday Plenaries](http://www.blog.pythonlibrary.org/2010/02/22/pycon-2010-sunday-plenaries/) - The Mouse vs The Python

The last plenary session for [PyCon](./PyCon.html) 2010 was on Sunday. In it, Van Lindberg told us that if we included all the vendors, our conference had hit over 1100 people. What that meant is that for [PyCon](./PyCon.html) 2011, they would probably have to put an attendance cap of 1500 so that we wouldn't run out of room at the current venue. Is this good? I don't really know. Sometimes it felt like it was already too big. Time will tell. [Read More](http://www.blog.pythonlibrary.org/2010/02/22/pycon-2010-sunday-plenaries/)

**[Pickle Objects Under Jython](http://code.activestate.com/recipes/252131-pickle-objects-under-jython/) - [ActiveState](./ActiveState.html)**

**[Sikuli Can Automate by Taking Screenshots](http://www.tuaw.com/2010/02/01/sikuli-can-automate-any-ui-by-taking-screenshots/) - TUAW**

**[Definitive Guide to Jython](http://www.codetown.us/profiles/blogs/the-definitive-guide-to-jython-1?xg_source=activity) - Codetown**

**[PyCon 2010 Frank Wierzbicki Lead Jython Developer](http://www.thebitsource.com/featured-posts/wierzbicki-jython-pycon-2010/) - [BitSource](./BitSource.html)**

**[PyCon 2010 - Worlds Largest Python Conference](http://www.thebitsource.com/tech-conferences/pycon-2010-python/) - [BitSource](./BitSource.html)**

**[Jython Book - Working with the Sources](http://jj-blogger.blogspot.com/2010/02/jython-book-working-with-sources.html) - Josh Juneau**

**[Compiling Jython Scripts in Java Class Files](http://www.dancheah.com/2010/02/compiling-jython-scripts-in-java-class-files.html) - Strange Loops**

**[Jython and Salesforce](http://gsmithfarmer.blogspot.com/2010/02/jython-and-salesforce.html) - The Programming Farmer**

## Videos 

[Sikuli, a Scripting Language Based on Screenshots](http://spokutta.wordpress.com/2010/02/07/sikuli-a-scripting-language-based-on-screenshots/)

[Extending Java Applications with Jython - Frank Wierzbicki](http://pycon.blip.tv/file/3259721/)

[How and why Python is being used to by the Military to model real-world battlefield scena - Eric Silverman](http://pycon.blip.tv/file/3261123/)

[Other PyCon Videos](http://pycon.blip.tv)

## Threads 

[Program with Jython](http://www.alice.org/community/showthread.php?t=3895)

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
