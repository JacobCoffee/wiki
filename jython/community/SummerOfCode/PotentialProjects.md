# SummerOfCode/PotentialProjects

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

## ctypes

Get ctypes working from Jython using JNA

## new compiler optimization/cleanup etc 

The new compiler which uses ASM for bytecode generation has plenty to work on.

## new parser work 

The new parser implemented in Antlr3 has plenty of room for improvement.

## numpy

Get enough of numpy working so matplotlib will run.

## Jython Help System 

Note: This started as a weblog post from Brian Zimmer (His weblog disappeared a long time ago, but I dug it up again through the magic of the wayback machine.

One of the best features of Python IMHO is the help() function. It's the first place I turn if I need help before I open a web browser and read the docs.

I think it would be cool if we could do this:

\>\>\> from java.lang import String \>\>\> help(String)

and see the full Javadoc documentation in help format.

I think a cool project would be to create a system that could turn source code comments into a format that the Jython help system could consume (perhaps with a Doclet) runtime Javadoc parsing (if you have the source \-- this will become especially nice for Sun\'s newly GPL\'ed version) in the case of classes not already exposed with the special doc string mechanism available in Jython already.

This could be facilitated with an xdoclet like framework which when ran over a source file would produce something Jython could use at runtime. This would either be a cached file or a Java class in a special namespace. For example, if you have class a.b.c.D then maybe the class a.b.c.D_doc might have the document source available through reflection.

Of course, help() is not currently working at all in Jython \-- so the first step would be to figure out why this is and fix it. Also, we need a strategy for getting the help documentation from CPython into our new style classes.

## Jython unit testing 

Jython has two sets of unit tests \-- one which is comprised of the CPython tests and a number of Jython specific tests written in a similar style. The other is the \"bugtests\" directory \-- which contains just short of 400 tests which are numbered test000.py to test394.py. The bugtests are peculiar to Jython \-- they do many things that just wouldn\'t make sense in a CPython context. For example, the bugtests have support for compiling java source files as part of the testing. A project to clean out and modernize the bugtests (as well as the Jython specific unit tests under Lib/test) is definitely in order. The project could proceed through several steps:

1.  Determine if tests currently giving warnings are valid and need to be fixed or if they should be removed
2.  Break tests into groups for jythonc, Java integration, Jython specific functionality, and any other groupings that make sense after going through the tests
3.  Rename the tests with descriptive names instead of numbers
4.  Use nose where possible instead of the custom driver.py code
5.  Hook the bugtests into the buildbot through the Ant build

nose has just become runnable with Jython. As we add new tests to Jython and convert the existing ones, it\'d be far preferable to use nose instead of the unittest module. Add nose to Jython as an svn:external, hook it into Lib/test/regrtest.py and add some docs on writing tests with nose for Jython to the developer guide.

## Reloading in Jython 

Note: this was copied directly from a post by Paul D. Fernhout to jython-dev

How about being able to modify and restart code in a debugger thread? Part of this entails allowing restartable / resumable exceptions.

Most Smalltalks support this, and it greatly increases productivity in some cases.

For example, consider when you run a Jython-based simulation for an hour only to get an exception from a trivial typo which such a debugging system would allow you to easily correct and restart from. Instead, you need to restart the code and wait another hour for the next typo. Yes, you can try to write your code to work around this sort of problem with checkpoints and events and such, but should not this be made easier, especially for beginners? A less extreme situation is when you are processing, say, an XML file, which takes a few minutes, and you need to keep restarting with each change. Anyway, not being able to restart easily decreases Python programmer productivity.

There is also a style of \"coding in the debugger\" where you write stubs for functions and just flesh them out while running the program.

- [http://www.google.com/search?hl=en&q=%22coding+in+the+debugger%22](http://www.google.com/search?hl=en&q=%22coding+in+the+debugger%22)

To look at this more generally, essentially you are adding the capability to Python / Jython to \"edit and continue\" \-- which might include writing a PEP, likely modifying Jython (and maybe Python), and modifying a GUI to use the changes (e.g. [PyDev](./PyDev.html) might be a good choice).

Smalltalk (including Squeak) has had this since the 1970s, but even Visual Basic can do it these days:

- [http://msdn2.microsoft.com/en-us/library/bcew296c(VS.80).aspx](http://msdn2.microsoft.com/en-us/library/bcew296c(VS.80).aspx)

<!-- -->

- From there: \"Edit and Continue is a time-saving feature that enables you

to make changes to your source code while your program is in break mode. When you resume execution of the program by choosing an execution command like Continue or Step, Edit and Continue automatically applies the code changes with some limitations. This allows you to make changes to your code during a debugging session, instead of having to stop, recompile your entire program, and restart the debugging session.\"

It\'s a shame Python and Jython can\'t do what even Microsoft products can. And no, module reloading (even using xreload.py or the code I previously posted on it) is not general enough to be able to modify a running thread and resume with all the old variable values with the new code. Xreload or the code I posted is general enough to modify code in a running GUI application, but only only for future GUI events (not one currently having problems).

You can see related recent comments on this in the Python Edusig list, starting here.

- [http://mail.python.org/pipermail/edu-sig/2007-February/007776.html](http://mail.python.org/pipermail/edu-sig/2007-February/007776.html)

Guido said it was \"impossible\",

- [http://mail.python.org/pipermail/edu-sig/2007-February/007794.html](http://mail.python.org/pipermail/edu-sig/2007-February/007794.html)

so it would make a nice challenge for someone (perhaps even moving Jython ahead of Python in some ways. ![:-)](/wiki/modernized/img/smile.png%20":-)") No guarantee of success, but a worth effort which would certainly require someone to learn the core of Jython and how it does exception handling. For inspiration, see:

- \"What\'s that you say? Impossible, is it? We\'ll just see about that.\"

  [http://www.des.emory.edu/mfp/impossible.html](http://www.des.emory.edu/mfp/impossible.html)

\--Paul Fernhout

## Stackless Jython 

Allow Jython to function similar to Stackless python

## Translate the current socket and select modules to java 

From Alan Kennedy on jython-dev:

As far as I am concerned, the socket and select modules are now stable, and unlikely to change much.

It was fine keeping them in pure python while they were still changing.

But now that they\'re stable, a translation to java is the next logical step. It would be reasonably straightforward, and would very likely greatly increase performance.

And it\'s a sexy project too; the new socket and select modules could the basis of porting twisted, etc, to jython.
