# JythonMonthly/Newsletters/October2006

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

::: {}
  ------------------------------- ---------------------------------------------------------------------------------------------------
  ***Jython Monthly***             ![](http://www.jython.org/css/jython.png "http://www.jython.org/css/jython.png")
  **October 2006 \-- Issue #4**   
  ------------------------------- ---------------------------------------------------------------------------------------------------
:::

Welcome to the October 2006 issue of Jython Monthly. The content of this newsletter will focus on using and developing the Jython languge. I want to encourage the readers of Jython Monthly to send any articles, tips, tricks, or any other Jython related material to me if you think it should be distributed with this newsletter.

Special thanks to those who submitted material for this month\'s newsletter!

\- Josh Juneau

Questions, comments, or suggestions?

Please send email to:

[jython-monthly@mchsi.com](mailto:jython-monthly@mchsi.com) or [jython-users@lists.sourceforge.net](mailto:jython-users@lists.sourceforge.net) for discussion.

# Articles 

## Scripting Jython with JDK 6 

*Submitted By: Josh Juneau*

There are many features within the JDK 6 builds which are going to open new doors for Java programmers. Perhaps one of the most unique new features of JDK 6 is the inclusion of a scripting project which allows usage of countless java scripting languages within Java applcations.

[Read Complete Article](http://wiki.python.org/jython/JythonMonthly/Articles/October2006/1)

## Web Application Development with Jython, Struts, and Hibernate 

*Submitted By: Berlin Brown*

With all the discussion centered around the java web-application frameworks including Struts, SpringMVC and [WebWork](./WebWork.html), how does one interface these with Jython and why would you want to do so. Normally, you will do this the same way that you would in a typical standalone console application. You must find a way to invoke the Jython interpreter and then execute your Jython code. The same is done in a Servlet environment. This example demonstrates how to put together a web-application that uses the Struts MVC (model, view, controller) framework and also uses Hibernate for persisting our objects to the database. The JSP files make up all the of the View code and Jython is used for all the back-end work. The goal of the \'[BotList](./BotList.html) Link Aggregator Application\' is to create a web-app that stores a set of links associated with keywords and description and also presents an interface to delete, view, edit, and list the links for the user.

[Read Complete Article](http://wiki.python.org/jython/JythonMonthly/Articles/October2006/2)

## Simple and Efficient Jython Object Factories 

*Submitted by: Charlie Groves*

Writing code in Python that can be easily called by Java code is one of the most attractive features of Jython. In last month\'s newsletter, Josh wrote Accessing Jython from Java Without Using jythonc. It shows how to easily use Jython objects implementing Java interfaces in Java code. He mentions that \"using this technique correctly is more effective than using jythonc\". I\'ll go one step further: unless you run in an environment that requires precompiled classes(e.g. in a servlet engine with security restrictions) or have extreme masochistic tendencies you shouldn\'t use jythonc. It has no speed benefits over regular Jython, requires the added complexity of a compile step and doesn\'t have basic features like line numbers in stack traces.

[Read Complete Article](http://wiki.python.org/jython/JythonMonthly/Articles/October2006/3)

# Off The Lists 

*From Craig W*:

- I am trying to read in some large files using Jython. I have no problems with something under 12mb\....but over 12mb, I get [OutOfMemoryError](./OutOfMemoryError.html): java heap space any suggestions on how to read in large files into Jython?

  - I tried: data = open(\'blah.zip\', \'rb\').read() (where blah.zip is a 13.3MB file).

*Response by Kent Johnson*:

Did you try giving more heap space to Jython? In the batch file or whatever you use to launch your program, add the Java switch -Xmx512M, that will set the max heap to 512 MB.

# Interested in Developing Jython? 

If you are interested in developing Jython, please take a look at the [current bug listing](http://sourceforge.net/tracker/?func=browse&group_id=12867&atid=112867) and submit patches for items which you can repair.

# IDE Information 

[JyConsole](http://java-source-code.com/?q=node/111) is an advanced Java graphic console for Jython, able to manipulate Jython and Java objects.

Pydev and Pydev Extensions 1.2.4 have been released

Details on Pydev Extensions: [http://www.fabioz.com/pydev](http://www.fabioz.com/pydev) Details on Pydev: [http://pydev.sf.net](http://pydev.sf.net) Details on its development: [http://pydev.blogspot.com](http://pydev.blogspot.com)

Release Highlights in Pydev Extensions:

\* Code analysis: analysis on imported modules do no longer give you errors on

- classes that have [getattribute] or [getattr] overriden

- assigns that are initially None

- assigns to a function call and not a class definition

\* Completions for parameters in a context-insensitive way, looking for all the methods/attributes declared in classes available to the project (after 3 chars)

Release Highlights in Pydev:

\* Completions for parameters based on the tokens that were defined for it in a given context \* Removed the default [PyLint](./PyLint.html) options, because its command-line interface changed (that was crashing [PyLint](./PyLint.html) in newer versions) \* Changed the grammar so that \'yield\' is correctly parsed as an expression \* Giving better error message when external file is opened without any interpreter selected \* Icons for the builtins gotten on large libraries (such as wx \-- it was optimized not to do that before) \* Adding jars relative to the project now works correctly

# Who\'s Using Jython? 

[JMS Support](http://hermesjms.com/python.html)

# Jython Blogs 

[Code Monkey Ramblings - Jython Advocate](http://www.codemonkeyramblings.com/2006/10/misc.php)

[Jython/Pydev JavaCC grammar notes](http://tomcopeland.blogs.com/juniordeveloper/2006/09/jythonpydev_jav.html)

[Java, JavaScript, and Jython Part I](http://blogs.sun.com/sundararajan/entry/java_javascript_and_jython)

[Java, JavaScript, and Jython Part II](http://blogs.sun.com/sundararajan/entry/java_javascript_and_jython_part)

[Java Integration: Beanshell and Jython](http://blogs.sun.com/sundararajan/entry/java_integration_beanshell_and_jython)

[Simplest Jython based Servlet Web Application](http://jroller.com/page/berlinbrown?entry=simplest_jython_based_servlet_web)

# Interesting Facts 

Jython - Average Job Salary & Stats in UK [http://www.itjobswatch.co.uk/jobs/uk/jython.do](http://www.itjobswatch.co.uk/jobs/uk/jython.do)

JExpress Forum (Jython scripting challenge: Automatic gene group multi-fss) - [http://molmineus.com/forum/index.php?PHPSESSID=7093e1d1e3449b4417b726ea3cbf0132&board=4.0](http://molmineus.com/forum/index.php?PHPSESSID=7093e1d1e3449b4417b726ea3cbf0132&board=4.0)

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
