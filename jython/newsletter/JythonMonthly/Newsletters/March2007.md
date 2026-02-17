# JythonMonthly/Newsletters/March2007

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

::: {}
  ----------------------------- ---------------------------------------------------------------------------------------------------
  ***Jython Monthly***           ![](http://www.jython.org/css/jython.png "http://www.jython.org/css/jython.png")
  **March 2007 \-- Issue #9**   
  ----------------------------- ---------------------------------------------------------------------------------------------------
:::

Welcome to the March 2007 issue of Jython Monthly. The content of this newsletter will focus on using and developing the Jython languge. I want to encourage the readers of Jython Monthly to send any articles, tips, tricks, or any other Jython related material to me if you think it should be distributed with this newsletter.

There was a lot of activity in the Python community this past month. The Pycon 2007 event took place and it appears to have been a complete success. Unfortunately, I was unable to attend the event myself, but I have been told by many that it was an excellent event. Please visit the [PyCon website](http://us.pycon.org/apps07/schedule/) for a complete listing of the topics discussed.

The Jython community has been busier than ever. If you are a member of the Jython mailing lists then you know what I mean, it is hard to stay current with all of the e-mail postings from the community. Please contribute to future newsletters by writing articles or tutorials based on your experiences with Jython!

\- Josh Juneau

Questions, comments, or suggestions?

Please send email to:

[jython-monthly@mchsi.com](mailto:jython-monthly@mchsi.com) or [jython-users@lists.sourceforge.net](mailto:jython-users@lists.sourceforge.net) for discussion.

# News 

[JSR223 Engine updated](http://news.java-virtual-machine.net/news/13-february-2007-a-sundararajan-updated-jython-jsr-223-engine-with-jython-22b1.html)

# Articles 

[Jython Beta with All Features of Python Version 2.2 Released](http://www.pythonthreads.com/index2.php?option=com_content&do_pdf=1&id=305)

[Write Eclipse JUnit Tests in Jython](http://www.devx.com/Java/Article/26602/0/page/1)

# Off The Lists 

***Question Submitted By Richard M.:***

I just installed jython and looked at the Demo examples in the installed folder but didn\'t see how to call java methods from python code.

The action i want to get is if a certain button is pressed in python code (wxpython) a java method is being called with several variables. is this possible with this tool ? and how should i approach it.

I tried to download the tutorial from Barry Feigenbaum at the jython home page but it was corrupter and couldn\'t open it on my system. Is there another helpfull tutorial available that will describe these basic actions.

***Answer From Jeff Emanuel:***

Yes, when a button is pressed, Jython can Java methods. The usual Python GUI toolkits aren\'t available in Jython, though. You\'ll need to code the GUI against the Java awt or swing api.

Have you seen these?

[http://www.jython.org/docs/usejava.html](http://www.jython.org/docs/usejava.html)

[http://www.jython.org/Project/userguide.html#accessing-java-from-jython](http://www.jython.org/Project/userguide.html#accessing-java-from-jython)

# Interested in Developing Jython? 

If you are interested in developing Jython, please take a look at the [current bug listing](http://sourceforge.net/tracker/?func=browse&group_id=12867&atid=112867) and submit patches for items which you can repair.

# Jython Blogs 

[Jython and JNDI](http://www.briggs.net.nz/log/2007/02/28/jython-and-jndi/)

[Blogging Regarding Jython and Unicode Data](http://eternusuk.blogspot.com/2007_02_01_archive.html)

# IDE 

[JAIDA and Jython](http://java.freehep.org/jaida/jython-jaida.html)

[JyDT for Eclipse](http://www.redrobinsoftware.net/jydt/)

**Pydev and Pydev Extensions 1.3.0 have been released**

Details on Pydev Extensions: [http://www.fabioz.com/pydev](http://www.fabioz.com/pydev)

Details on Pydev: [http://pydev.sf.net](http://pydev.sf.net)

Details on its development: [http://pydev.blogspot.com](http://pydev.blogspot.com)

*Release Highlights in Pydev Extensions:*

------------------------------------------------------------------------

\* Find References: Ctrl+Shift+G can be used to find the references to the selected token in the editor

\* Fix: Code-analysis: Fixed false positive for statement with no effect

*Release Highlights in Pydev:*

------------------------------------------------------------------------

\* Code-completion: Deep analysis for discovering arguments in constructs \'from imports\' now can be configured given the number of chars of the qualifier

\* Refactoring for override methods: changed so that it uses the pydev code-completion engine for getting the hierarchy and methods

\* Fix: Python Nature Restore: begin rule does not match outer scope rule fixed

\* Fix: Package Explorer: if show-in is in a deep structure, it will show it is the 1st try and not only in the 2nd

\* Fix: Package Explorer: some intercepts removed elements incorrectly, and ended up messing the navigator and search (which has \'null\' elements because of that)

# Discussions 

[Websphere Extended Repository Service & Jython Scripting](http://www-128.ibm.com/developerworks/forums/dw_thread.jsp?message=13919392&cat=9&thread=151729&treeDisplayType=threadmode1&forum=778#13919392)

[Help Porting Jython to UIQ3](http://developer.sonyericsson.com/thread.jspa?threadID=37982&tstart=0)

*Upcoming Discussions*

[Orlando JUG: Introducing Jython](http://www.orlandojug.org/)

# Interesting Facts 

Jython - Average Job Salary & Stats in UK [http://www.itjobswatch.co.uk/jobs/uk/jython.do](http://www.itjobswatch.co.uk/jobs/uk/jython.do)

# Useful Links 

[Jacl v2.5 Released](http://www-1.ibm.com/support/docview.wss?rs=180&uid=swg24012144)

The IBM® Jacl to Jython Conversion Assistant ([Jacl2Jython](./Jacl2Jython.html)) is a program that assists in converting [WebSphere](WebSphere)® administrative (wsadmin) scripts written in Jacl into Jython syntax.

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
