# JythonMonthly/Newsletters/January2007

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

::: {}
  ------------------------------- ---------------------------------------------------------------------------------------------------
  ***Jython Monthly***             ![](http://www.jython.org/css/jython.png "http://www.jython.org/css/jython.png")
  **January 2007 \-- Issue #7**   
  ------------------------------- ---------------------------------------------------------------------------------------------------
:::

Welcome to the January 2007 issue of Jython Monthly. The content of this newsletter will focus on using and developing the Jython languge. I want to encourage the readers of Jython Monthly to send any articles, tips, tricks, or any other Jython related material to me if you think it should be distributed with this newsletter.

This month\'s newsletter includes two articles which should be of interest. The first article explains how to develop a Jython web application using web.py. This appears to be a powerful alternative way to develop Jython web applications. The second article shows how you can translate a Java program into Jython and make it work with the JOGL API.

You will also see some excellent Python tips in this month\'s distribution. Each of these tips have been taken from the Python Cookbook and tested under Jython.

Special thanks to those who submitted material for this month\'s newsletter!

\- Josh Juneau

Questions, comments, or suggestions?

Please send email to:

[jython-monthly@mchsi.com](mailto:jython-monthly@mchsi.com) or [jython-users@lists.sourceforge.net](mailto:jython-users@lists.sourceforge.net) for discussion.

# Articles 

## Adding JARS to sys.path During Runtime 

*Submitted by: Steve Langer*

During Oct-Nov 2006 there was a thread in the jython-users group titled \"adding JARs to sys.path\". More accurately the objective there was to add JARs to the sys.path at runtime. Several people asked the question, \"Why would you want to do that?\" Well there are at least 2 good reasons. First, if you want to distribute a jython or Java package that includes non-standard Jars in it. Perhaps you want to make life easier for the target user and not demand that they know how to set environment variables. A second even more compelling reason is when there is no normal user account to provide environment variables.

[Read Entire Article](http://wiki.python.org/jython/JythonMonthly/Articles/January2007/3)

## Web Application Development Using web.py and Jython 

*Submitted by: Colin*

Given the recent discusion on the Jython-dev list of getting popular CPython applications ported to run on Jython I took a look at whether it was possible to get the increasingly poplar web.py web appplication (anti)framework to work on the Jython platform. It turned out it was relatively easy to get it running and most of the basic functionality working: db connectivity, form.py and template.py.

[Read entire article](http://wiki.python.org/jython/JythonMonthly/Articles/January2007/1)

## Proof of Concept: Using Jython with the JOGL API 

*Submitted by: Josh Juneau*

My everyday job consists of Java and/or PL/SQL programming and database development. That is why I thought it would be fun to start looking into Java and Jython game development for something fun. I\'ve chosen to implement a Jython program which utilizes the Java Binding for OpenGL (JOGL) API. This brief article is not meant to be a tutorial for using JOGL API as there are many good references already available (see below), but rather it is meant to be a \"proof-of-concept\" that Jython does work with JOGL for the most part.

[Read entire article](http://wiki.python.org/jython/JythonMonthly/Articles/January2007/2)

# Off The Lists 

*Question from \"Divya\":*

I would like to parse \". java \" / \".class\" files and detect class name\'s, attributes name\'s and type\'s (and or list of methods).

Is there any module who can parse easily a java file using jython?

*Answer from Luis:*

It would probably be easiest to work on compiled .class files and use the reflection API.

If you have access to Java 6, you could even use the compiler API. See the following article:

[http://www.javalobby.org/java/forums/t44534.html](http://www.javalobby.org/java/forums/t44534.html)

------------------------------------------------------------------------

*Question from Mike:*

I\'m embedding Jython in a Java servlet and have set the \'python.path\' to include a directory which contains python scripts I have written and packaged.

For example I have a folder \"/package\" which contains \'myscript.py\' and \'[init].py\'.

My servlet executes some arbitary python script which imports the module \'myscript\'. The first time this happens \'myscript.py\' is compiled to \'myscript\$py.class\' which is fine. However, if I change \'myscript.py\' there is no detection of the new script and I must shutdown and restart the servlet to reload my changes.

Is there any simple way around this?

*Answer from Leouser:*

have you tried the reload function yet?

{{{import Thing Thing.doSomething() #change Thing.py src reload(Thing) Thing.doSomething() }}}

# Interested in Developing Jython? 

If you are interested in developing Jython, please take a look at the [current bug listing](http://sourceforge.net/tracker/?func=browse&group_id=12867&atid=112867) and submit patches for items which you can repair.

# Tips and Tricks 

[Python Cookbook: Reload Classes Dynamically](http://aspn.activestate.com:80/ASPN/Cookbook/Python/Recipe/499295)

[Python Cookbook: The KeyedDict object keeps a list of approved key values](http://aspn.activestate.com:80/ASPN/Cookbook/Python/Recipe/499296)

[Python Cookbook: Calculate hamming distance between two strings](http://aspn.activestate.com/ASPN/Cookbook/Python/Recipe/499304)

# Noteworthy Book Releases 

[Python Phrasebook](http://www.techbookreport.com/tbr0278.html)

# Jython Blogs 

[Great Jython blogs from Paul Drummond](http://gushieblog.blogspot.com:80/)

[CherryPy + Jython + modjy + JBoss = true](http://henkenotes.blogspot.com/2006/12/cherrypy-jython-modjy-jboss-true.html)

# Discussions 

*Discussion Submitted by Thomas Muller*

Hello jython users,

I want to suggest a new project, but need your help. There is an open source python written serverless instant messenger out (based on a kademlia DHT lookup for buddies):

[http://cspace.in](http://cspace.in)

Version 1.26 (though the icons in version 1.24 are better). As well a linux porting exists. [http://www.aabdalla.com/releases/](http://www.aabdalla.com/releases/)

I want to initiate a project to port the python messenger to java using jython. But I cannot do it alone. We could register a sf.net project for \"cspace-java\". Is jython ready to just compile it and get a jar out and a source-file out? Can someone send this through jython or help?

The server is serverless and this means independence from any central instance. It uses to identify the buddy a RSA-Key and a CSpace-ID from the developer-server. In the long run, only the RSA-Key should be used. Unfortunatly you cannot a) create an RSA-key without that central server and b) you cannot launch the application without the Cspace-ID.

Anyway, we can use it with the tachyon server for creation, but communication and buddy-lookup is decentral and encrypted like skype as well.

But what we need is a java version. Maybe the cspace developers did not played around with jython either, and instead of coding windows and Linux or MacOSX port, we can switch to interoperable java.

But as there are less resources, I want to ask the mailinglist of jython to fix the current status of the application over jython to java please.

The serverless Messenger in java could be easily built in into many applications, which need an instant messenger:

\- yacy.net - serverless p2p webindex search engine in java - sf.net/projects/antsp2p - already a jeti-jabber buddylist integrated for bootstrapping, but it is central. - limewire.com of course - azureus.sf.net of course - wikisari, the google pendant, still under development [http://lists.wikia.com/pipermail/search-l/2006-December/000004.html](http://lists.wikia.com/pipermail/search-l/2006-December/000004.html)

Does anyone agree on that potentials? kind regards tom

# Interesting Facts 

Jython - Average Job Salary & Stats in UK [http://www.itjobswatch.co.uk/jobs/uk/jython.do](http://www.itjobswatch.co.uk/jobs/uk/jython.do)

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
