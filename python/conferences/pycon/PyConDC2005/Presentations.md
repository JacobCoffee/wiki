# PyConDC2005/Presentations

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

------------------------------------------------------------------------

#1. **Python in the IT Field**

Greg Lindstrom / [NovaSys](./NovaSys.html) Health ([http://www.novasyshealth.com](http://www.novasyshealth.com))

In business, customer service is the name of the game. In the Information Technology field, this service manifests itself in the ability to accept, format, store, and analyze data. At [NovaSys](./NovaSys.html) Health, we selected Python for our programming needs because it\'s easy to use, plays well with a variety of platforms (not only different operating systems, but a wide variety of databases) and the Python community is as helpful as it gets. This talk will discuss how Python is allowing us to list technology as a competitive advantage (accessing MS SQL database, teaching other techies, using Python\'s standard library).

------------------------------------------------------------------------

#4. **[MissionEngine](./MissionEngine.html): Multi-system integration using Python in the Tactical Language Project**

Prasan Samtani ([http://www.isi.edu/\~samtani](http://www.isi.edu/~samtani)), Hannes Vilhjalmsson ([http://www.isi.edu/\~hannes](http://www.isi.edu/~hannes))

University of Southern California - Information Sciences Institute (USC/ISI)

Project homepage URL: [http://www.tacticallanguage.com](http://www.tacticallanguage.com)

The Tactical Language Training system is designed to help learners acquire communicative competence in spoken Arabic and other languages. Learners practice vocabulary items and learn gestures, following which they apply them in a simulated Mission Environment. In the simulation environment, users interact with the systemís onscreen characters using a speech recognition interface. The simulation environment is built on the Unreal tournament Game Engine.

In the past several months, a major transition has been made from the original system in Java, to a new Python-centric architecture. This presentation traces the evolution of the Tactical Language Training System from a set of separate programs to a single integrated system. The various different system components will be introduced, and the underlying technology behind will be briefly discussed. We will go over what features of the language we found especially useful for integration (latent-typing, lambda functions, pickle), and some hurdles we found particularly tricky coming from a C++/Java background.

The talk will also address the way we tackled the problem of talking to incompatible languages. For example, Unreal Tournament uses a proprietary scripting language - [UnrealScript](./UnrealScript.html) - and in order to communicate with Unreal we had to make use of an earlier ISI technology called GAMEBOTS, which is implemented both in Python and [UnrealScript](./UnrealScript.html), and uses sockets as a method of communication.

Other topics discussed in the context of Tactical Language will adress the performance issue (writing expensive routines - the speech recognition and NLP algorithms - in C and authoring extension modules), the importance of using a powerful language for build scripts, using algorithmic optimizations over language micro-optimizations and the importance of Python\'s standard library in speeding up the development process.

------------------------------------------------------------------------

#7. **Happy Hooking: Designing Software for Extensibility and Customization**

[Ed Leafe](../../../people/Ed%20Leafe) / [The Dabo Project](http://dabodev.com)

It is rare for anyone to create any non-trivial software project that will not need customization at some point. It is therefore wise to plan for this when designing your code by inserting hook methods that are designed to be customized to add additional functionality later on. By default these methods do nothing, so they can be freely overridden by others without the risk of losing a critical behavior because a superclass method had been overridden. This is especially useful for creators of frameworks and tools that can be extended by their users. As one of the two primary authors of the Dabo framework, I am especially aware that in order to be useful, the code I create needs to be adapted and augmented by developers who build their apps with Dabo. I will show several code examples from Dabo to illustrate my points. [Paper](http://www.python.org/pycon/2005/papers/7/pyconHooking.html)

------------------------------------------------------------------------

#9. **Dabo, the 3-tier Database Application Framework)**

[Ed Leafe](../../../people/Ed%20Leafe) / [The Dabo Project](http://dabodev.com)

There are several tools available that help a developer create applications for working with data: Visual [FoxPro](./FoxPro.html), Visual Basic, Delphi, etc. They make some of the tedious parts of the app, such as ensuring that a change to a value in a text box gets propagated back to the correct column in the correct record of the correct table in the correct database on the correct host. These tools all have their strengths and weaknesses, but none are Open Source, and none are in Python!

In March 2004, two long-time Visual [FoxPro](./FoxPro.html) developers, Ed Leafe and Paul [McNett](./McNett.html), had both become convinced that Python and cross-platform apps represented the future. Trouble was that there wasn\'t a tool available that could do what we wanted; so as a result, we decided to create our own.

Dabo is designed to create true 3-tier apps, in which the UI, the business rules, and the data storage are cleanly separated, using a Chain of Responsibility pattern for the messaging between tiers. We\'ve chosen wxPython as our initial UI toolkit, but have written our UI classes so that their interfaces are not wxPython-specific. We currently support MySQL, Firebird and PostgreSQL on the backend, with more to follow. [Paper](http://www.python.org/pycon/2005/papers/9/pyconDabo.html)

------------------------------------------------------------------------

#10. **Agile Testing with Python Test Frameworks**

Grig Gheorghiu / Avamar

I present various test frameworks that are either written in Python or use Python/Jython as their scripting language. I discuss these frameworks in the context of agile testing. Here is a high-level view of the talk I\'ll give:

1\. What is agile testing?

- \"agile\" as in \"agile methodologies\", (aka Extreme Programming)

2\. Why Python?

- eminently \"agile\" language

3\. MAIN SECTION: Python-based test frameworks

- unit testing (unittest, doctest, py.test)
- continuous performance testing (pyUnitPerf)
- functional/system/integration testing (homegrown framework)
- test distribution, execution and reporting (STAF/STAX)
- acceptance testing (pyFIT/FitNesse)
- Web application testing (Selenium, MaxQ, mechanize, webunit, PBP, Twill)

4\. Jython and Dynamic Java

- Recent discussions on Java and scripting languages

- Jython is leading the pack in terms of scripting the JVM

- Java-based test frameworks can be used within Python frameworks via Jython

- Examples of Java- and Jython-based frameworks (The Grinder, [TestMaker](./TestMaker.html), Marathon)

- Using Java-based tools with Jython (example: HTTPUnit)

------------------------------------------------------------------------

#11. **Localized Type-Inference in Python**

Brett Cannon / Cal Poly SLO

This talk will present research into type inferencing in Python. The main goal of this work is to extract a performance gain from type-specific opcodes added to Python\'s VM. The type information needed to use these new opcodes during code generation comes about from a simple, localized type inferencing algorithm. The design of this algorithm required that no changed be made to the semantics of Python. Because of this requirement the type inference algorithm is hindered by Python\'s dynamic nature. This talk will discuss what in Python\'s semantics makes type inferencing difficult, the algorithm used, the added opcodes, and the results of adding the new opcodes.

------------------------------------------------------------------------

#12. **The Roundup Issue Tracker**

Richard Jones / Common Ground

Roundup is a simple-to-use and -install issue-tracking system with command-line, web and e-mail interfaces. It is based on the winning design from Ka-Ping Yee in the Software Carpentry \"Track\" design competition. This presentation will cover:

- An introduction to Roundup
- A quick tour of the Web, e-mail and command-line interfaces
- What\'s involved in setting up a tracker
- The hyperdatabase at the core of Roundup
- An indication of where Roundup\'s going
- A simple customisation of the classic tracker

------------------------------------------------------------------------

#14. **Documentation Costs Avoided using Python and other Open Standards**

Andrew Fine / Honeywell

When I started out, I did not have any experience at SGML, XML, or other markup languages. It was only when I was perilously close to reinventing the concept of markup languages, by adapting direct PythonCOM to Word interfaces from Mark Hammond\'s book, that I decided there had be a better way to do this from a design and maintenance standpoint.

A Web search provided me with a crash education on markup languages such as XML, HTML, and SGML, on how [DocBook](./DocBook.html) SGML was an overwhelmingly popular open standard, and on how an open source package named [OpenJade](./OpenJade.html) could translate a [DocBook](./DocBook.html) SGML file into Word Rich Text file.

The arrangement wasn\'t perfect but I realized two things: 1) it could save me a year in development and maintenance, and 2) I could respond rapidly to new assignments.

The purpose of this paper is to show how I integrated Python, [DocBook](./DocBook.html), and Word together to obtain the perfection my local organization demanded.

------------------------------------------------------------------------

#15. **Scripting the Mac with Python**

Jacob Kaplan-Moss

The concept of \"scripting\" is central to the Unix philosophy, but it\'s always had spotty support in GUI operating systems. Early in the Mac OS\'s history, Apple recognized this deficiency and developed a framework for scripting GUI applications. Although this framework is quite well designed, its native language is not; [AppleScript](./AppleScript.html) has been called the only \"read-only\" language in existence. With newly developed hooks into Apple\'s scripting framework, Python now gives a far superior environment for scripting. This talk will focus on using the latest and greatest Python-[AppleScript](./AppleScript.html) bridge, appscript\_, to script OSX.

Previous knowledge of [AppleScript](./AppleScript.html) is not necessary; although this talk will briefly cover reasons why [AppleScript](./AppleScript.html) coders should switch to Python, the bulk of the talk will be spent explaining how to use appscript\_ through a series of (increasingly complex) examples.

.. \_appscript: [http://freespace.virgin.net/hamish.sanderson/appscript.html](http://freespace.virgin.net/hamish.sanderson/appscript.html)

------------------------------------------------------------------------

#16. **Python for Series 60**

Erik Smartt / Nokia

Python for Series 60 brings the power and productivity of Python to Series 60 based smartphones. Join us to see the latest developments and a sneak peak of the features and tools planned for the next release. If you\'re a Python for Series 60 fan, stop by to meet some of the team and share your thoughts on the future of Python development for mobile devices!

The Nokia port of Python to Series 60 mobile devices was released December 2004 on \<[http://forum.nokia.com/\>](http://forum.nokia.com/%3E).

------------------------------------------------------------------------

#17. **Durus: A Persistence System**

David Binger / MEMS Exchange

The presentation will describe Durus, a light-weight system for maintaining a persistent collection of instances. Durus features transaction management, support for multiple connections with caches, common data structures, and source code that is small and readable.

------------------------------------------------------------------------

#18. **matplotlib - from brain surgery to rocket science**

John Hunter and Perry Greenfield / University of Chicago and STScI

matplotlib is a 2D graphics package written in Python. The design of matplotlib allows a wide variety of uses: you can create plots interactively from the shell, generate plots from scripts in a web application server, create animated or dynamic plots for instrument control, or embed them in the Python GUI of your choice. Unlike other plotting solutions for Python, which are wrappers of libraries from other languages, matplotlib is written primarily in Python, with calls to extension code for special purposes. Thus it is much easier for Python users to become developers, and matplotlib has an active community of developers who contribute to the code base. Originally designed to allow a user coming from Matlab to generate plots with a similar syntax and quality as Matlab, matplotlib now embraces the best ideas from Python, IDL, gnuplot and Matlab in the pylab interface, which is a procedural wrapper around the core object oriented API.

matplotlib is an array plotting package, and is codeveloped with the developers of numarray at STScI and has full compatibility with the Numeric and numarray array packages at the Python and extension code levels. The abstract class hierarchy is separated from the backend rendering layer, allowing the same pylab scripts to generate identical plots in GTK, WX, Tkinter and FLTK, including event handling such as mouse motion and clicks, as well as generate image output in postscript, SVG, PNG and other formats. It is fully integrated with the interactive Python shell ipython, which runs the GUI mainloops of GTK and WX in a separate thread, allowing interactive control of plots typical in packages such as Matlab and Mathematica.

There is support for most of the standard things people want to do with 2D plotting, with a special emphasis on scientific plots, including images, line plots, scatter plots, histograms, bar charts, errorbars, polar and log scaling, contouring, financial charts, legends, mathematical text with a built-in TeX math expression parser, freetype2, W3C compliant cross-platform font-management, and more. matplotlib is highly configurable, with the default appearance of every plot element controlled by a configuration file, and all of the plot elements readily customizable.

------------------------------------------------------------------------

#19. **Studying African Lions in the Serengeti Ecosystem with Python**

Michael Urban / Lion Research Center ([http://www.lionresearch.org](http://www.lionresearch.org))

The Lion Research Center, headquartered at the University of Minnesota, is responsible for the Serengeti Lion Project in Tanzania, Africa, and is known throughout the world as a leading institution in the research of African lions. In this presentation, I will discuss FELIS, which is software we developed entirely in Python for identifying, tracking, and analyzing data on African lions in the Serengeti National Park, Ngorongoro Crater, and other lion projects in Tanzania. The software uses a pyGTK interface, and uses data from multiple sources. The software stores its native data using pysqlite. However, the software is also capable of cross-referencing its own data with additional data stored in Access databases, and Excel spreadsheets by using the mxODBC module. In addition, the software includes image processing capabilities for storing and viewing photographs of lions using the Python Imaging Library. Thanks to Python, we are now able to identify lions must faster and with much greater accuracy than was possible before; extract information based on multiple data sources in seconds that used to take days to extract manually; and easily share data between field researchers in Tanzania and our researchers at our headquarters at the University of Minnesota. Python has really revolutionized the way we study African lions.

------------------------------------------------------------------------

#20. **Fast Networking with Python**

Itamar Shtull-Trauring

This talk would cover three topics, each leading into the next. While the examples are mostly Twisted specific in the first two parts, the general concepts are relevant to Python networking specifically and Python programming in general.

1\. Algorithms are very important when attempting to write fast code, including networking. The talk will cover buffering and string manipulation, and possibly scheduling, and common mistakes that can make code orders of magnitude slower. Examples will include Twisted\'s buffering algorithm rewrite between 1.3 and 2.0, use of buffer(), imaplib, and maybe comparision of scheduling algorithms between Twisted 1.3, 2.0 and glib (where Python code is faster than C code due to a superior alogrithm).

2\. This part of the talk will explain Python\'s limitations - reads from sockets/files always allocate memory, lack of good byte array datatype, general slowness - and show how C or C++ can be used to circumvent these issues. As an example I will cover Fusion, an open source C++ integration layer for Twisted, and show how it solves some of the issues Python has. I will also cover the problems caused by using C or C++ code.

3\. In the final part of the talk, I would like to cover possible improvements to Python (specifically socket and file objects) that together with the need for a new builtin type, a byte array, would allow gaining some of the speed benefits available when using C/C++.

------------------------------------------------------------------------

#21. **Intuition and Python Programming - the Python Visual Sandbox**

Michael Weigend / Holzkamp-Gesamtschule Witten, Germany

When you write a Python program, search for semantic errors, proof the correctness of a function or just talk about programming, you use intuitive models of information processing. An intuitive model is a mental concept which is simple and self evident and needs no further explanation. Usually these concepts can be visualized. Intuitive models can be useful or they can be misleading. Sometimes they are unconscious. The Python Visual Sandbox (PVS) is a collection of interactive multimedia applications ñ usually games, especially designed for programming novices. They contain more than a hundred animations which represent intuitive models including typical misconceptions. The purpose of the PVS is two fold. First of all it is a research tool to find out, what intuitive concepts Python programmers use in different contexts. Secondly it is a learning device which can be integrated in lesson plans. This contribution focuses on the learning/teaching aspect.

------------------------------------------------------------------------

#22. **Extreme Programming with Python in the Classroom**

Michael Weigend / Holzkamp-Gesamtschule Witten, Germany

Extreme Programming (XP) and Python seem to fit in several ways to the goals, needs and conditions of informatics teaching at high school. In this contribution I present class room examples to illustrate how teachers could adopt XP methodology to design successful informatics lesson plans.

------------------------------------------------------------------------

#24. **Decimal data type**

[Facundo Batista](http://www.taniquetil.com.ar/plog)

In the paper I\'ll explain what is Decimal, how to use it, and when to use it. The idea is to let the reader to feel confident about this new data type in order to start using it.

I\'ll start with the detail of the Decimal intrinsic structure (floating point, bounded precision), the major differences with binary floating point, and other advantages.

Later I\'ll show how to use the module, from the simplest way (just use it) to a more advanced interaction (from showing its methods to explain how to use the Context, including rounding methods, signals, etc.).

Finally, I\'ll present some cases to show when use and not use Decimal instead of binary floating point.

------------------------------------------------------------------------

#25. **[MultiDrizzle](./MultiDrizzle.html): Astronomical Image Analysis Software for Python**

Warren J. Hack / Space Telescope Science Institute

Multidrizzle began as a collection of FORTRAN code and IRAF scripts for the combination of Hubble Space Telescope imaging data.

- Through the use of Python and cutting edge modules such as NUMARRAY,

PYFITS, and PyRAF, we have developed a robust piece of software, in less than one year, that will become the primary tool in the Advanced Camera for Surveys (ACS) data reduction pipeline for image combination and cosmic-ray cleaning. This same software has also been made available for use by researchers to reduce their ACS data on their own systems. We will describe the motivations for moving the existing Multidrizzle code to Python, highlight the challenges that NUMARRAY, PYFITS, and PyRAF allowed us to overcome, and illustrate how it serves as a primary task in a developing astronomical data analysis suite for Python.

------------------------------------------------------------------------

#26. **An Introduction to building Chandler parcels**

Ted Leung, Katie Capps Parlante / Open Source Applications Foundation

Chandler aspires to be an innovative open source personal information manager (PIM). In addition to being written in Python, Chandler is using the following open source libraries: BerkeleyDB, [M2Crypto](../../../archive/M2Crypto), Twisted, pyLucene, and wxPython/wxWidgets. Chandler is designed to be an extensible PIM. Chandler\'s unit of extensiblity is called a parcel, and Chandler\'s \"built-in\" functionality is itself composed of parcels. Internally, Chandler is designed as layers of frameworks which provide applications functionality to parcels. Parcels communicate with each other via the data in the Chandler repository.

The goal of our presentation and paper is to allow someone to begin developing a parcel that extends the Chandler user interface.

------------------------------------------------------------------------

#27. **Pulling Java Lucene into Python: [PyLucene](http://pylucene.osafoundation.org)**

Andi Vajda / Open Source Applications Foundation

As we needed an open source text search engine library for our Python based project, we made the following bet: what if we pulled together Java Lucene, GNU\'s gcj java compiler and SWIG to build a python extension ? In this presentation we\'d like to talk about the challenges we met since this project was started a year ago.

------------------------------------------------------------------------

#29. **A Layered Event System to Provide Method Extensibility**

Jim Fulton / Zope Corporation

Developers often want to extend the behavior of existing software. For example, a developer might have a class that manages data or provides some functionality and want to provide a user interface for it. Similarly, a developer may want to incorporate an object into a framework and may need to provide additional interfaces to integrate it. We\'ve found that adaptation works well in situations like these.

Sometimes, there is a need to extend what happens \*inside\* individual methods. For example, when an object is added to a system, we might record meta data or index the object\'s data or meta data. The actions we want to take are likely to be application dependent. It shouldn\'t be the responsibility of the code that adds the object to take these extra actions. Rather, to address situations like this, we use events and subscribers. Events signal that something has happened and subscribers can be registered to perform extra computation when something happens, thus extending the methods generating the events.

This event system is related to and addresses some of the same needs as Aspect-Oriented Programming (AOP). Events are equivalent to AOP point-cuts and subscribers correspond to advice. Unlike AOP, events are explicitly introduced into application code. An AOP system might be built on top of this event system by providing tools that automatically inject events into applications.

An event system provides a very elegant way to implement hooks. Any system that uses hooks can be simplified and made more flexible with events.

Zope has a layered event system, built on an extremely simple policy-free base. Additional layers, built on this base layer, progressively add additional policy. Zope provides an adapter-based subscription framework that provides a simple rule-based system.

The basic event system would make an extremely trivial, but very useful addition to the Python standard library.

In this presentation, I\'ll discuss the motivation for, and applications of, events. I\'ll give a number of event application examples including the use of event subscribers to add layers of policy to the underlying event system.

------------------------------------------------------------------------

#30. **State of Zope**

Jim Fulton / Zope Corporation

A discussion of the current state of Zope, covering developments in the past year and plans for the future.

------------------------------------------------------------------------

#32. **Descriptors: From functional wart to decorator madness via properties**

Mike C. Fletcher / Cain Gang Inc.

This presentation introduces the beginning/intermediate Python programmer to the Descriptor API, from its origins in the functions-are-special-cases \"wart\" in Python 2.1 through the introduction of the attribute-access API in Python 2.2 and to the introduction of function-decorator support in Python 2.4 and the expected Cambrian explosion of decorator classes. We will discuss some of the mechanics of the descriptor API, then focus on \"why and when\" to use descriptors and decorators.

[Presentation Slides](http://www.vrplumber.com/programming/descriptors-pycon2005.pdf)

------------------------------------------------------------------------

#33. **Design Patterns and Python OOP: Objects by Design**

Alex Martelli

Python is multi-paradigm; however, Object-Oriented Programming (OOP) is Python\'s core paradigm, and an understanding of Design Patterns (DP) and of how to best use them is a key enabling skill in doing effective OO development. This presentation takes its contents mostly from the OO chapter of the Python Cookbook (2nd Edition), and focuses on Design Patterns and related idioms presented there, with expanded explanations of underlying language mechanisms and additional examples.

Some classic DPs are practically \"built-in\" to Python. Other patterns can be just as useful in Python as in other languages, if you know them well and apply them deliberately to structure your design; moreover, there are language-specific issues and opportunities, connected to such patterns, which it\'s important to understand fully. Other patterns yet are generally inappropriate for use in Python applications, and may be best replaced by Python-specific idioms.

Exactly because Python is multi-paradigm, it empowers you to make meaningful design choices; and, as usual, with power comes responsibility \-- you need solid, in-depth understanding of what choices you have available, and of what implications and consequences such choices have, to choose for the best.

When should you use a closure, rather than a class with callable instances? Where is inheritance appropriate, and where is it better to use containment and delegation instead? When should you define \'[slots]\', what exactly are the implications of doing so, and what alternatives approaches may often be preferable? The purpose of this presentation is also to explore this kind of questions, and to provide the fundamental knowledge and the outlook that will help you answer the questions in the most useful ways for your own applications.

------------------------------------------------------------------------

#34. **Cross Platform Desktop Applications with Python**

Nathan R. Yergler / Creative Commons

In 2004 Creative Commons began to expand their offerings to include client applications. The applications were intended to promote and complement the licenses offered by Creative Commons. After evaluating other languages, Python was chosen as the primary development language, and wxPython was chosen as the user interface toolkit. ccPublisher is the outgrowth of these early decisions.

Today the Creative Commons is preparing to ship ccPublisher 1.0 on Mac OS X, Windows, and Linux. Python and wxPython, along with a fair amount of code manipulation, have enabled us to create a single code base for all three platforms. This code base, along with a set of build tools which are also being released as Open Source software, allow developers to focus on writing quality applications which integrate well and look \"right\" on all platforms. The overriding goal has been to isolate platform-specific code and settings, in an effort to share as much code as possible.

This presentation will focus on the non-intuitive aspects of cross-platform development with Python and wxPython. We all know that Python is available for a wide variety of platforms, but what goes into creating an application that doesn\'t require end-users to be aware of dependencies or languages? In particular, this presentation will cover handling platform-specific GUI idioms (Mac OS X menu bars, drag and drop on all platforms, etc), creating distributions of your application (MSI for Windows, DMG for OS X, RPM/DEB for Linux) which bundle all the necessary dependencies and which install seamlessly, and inconsistencies and problem areas we have encountered during the development of our applications. The presentation will also present some \"best practices\" developed during the project which have proven useful in minimizing the effort required to add features and refactor a cross platform application.

This presentation will be of interest to any Python developer considering developing end user applications with Python. It would also be useful for developers looking for easier ways to manage their building and distribution process.

------------------------------------------------------------------------

#35. **Integrating RDF in Python Applications**

Nathan R. Yergler / Creative Commons

The Resource Description Framework, RDF, is an exciting and largely mis-understood area of Internet development. RDF allows developers to represent complex relationships in a way which other applications can understand, often without prior knowledge of schema or datatypes. Today RDF engines exist in many mainstream applications such as Mozilla, largely untapped by developers.

Python has excellent RDF support libraries available, and therefore should be an excellent platform for developing intelligent applications.

- This presentation will focus of three primary points: clearing up

misconceptions about RDF, providing an overview of the Python libraries which support RDF, and demonstrating a real world usage of RDF in a Python application. The discussion of Python RDF support will also highlight shortcomings and potential pitfalls associated with RDF development. Brief attention will be given to current RDF developments if time remains.

This presentation will be useful for any developer working on integrating two or more applications, and to any developer interested in leveraging future web developments. Developers will leave the presentation with a firm understanding of what RDF is and how they may use it in their applications.

About the presenter: Nathan Yergler is a Software Engineer with Creative Commons. The primary developer of mozCC, ccPublisher and ccLookup, he has been manipulating RDF for the past 18 months in an effort to provide human-level integration between applications and the ethereal Semantic Web. During that time he has become intimately familiar with Python\'s RDF offerings, and widely frustrated by his own misconceptions. He wishes he knew then what he knows now about RDF.

------------------------------------------------------------------------

#36. **Descriptors, Decorators, Metaclasses: Python\'s \"Black Magic\"?**

Alex Martelli

Python\'s versions since 2.2 have introduced, enhanced, and clarified some new advanced mechanisms: two of them are the underpinnings of Python\'s Object-Oriented Programming (OOP), Descriptors and Metaclasses; one, introduced in 2.4, is a syntax for the systematic application of an important use case for higher-order functions. This presentation takes its contents mostly from the (informally known as\...) \"Black Magic\" chapter of the Python Cookbook (2nd Edition), also known (official chapter title!) as \"Descriptors, Decorators and Metaclasses\", and focuses on some of the most interesting applications and related idioms presented there, with expanded explanations of the underlying language mechanisms and additional examples.

\_Descriptors\_ control and guide attribute access. Python offers several built-in descriptor types \-- for example, in today\'s Python, \_functions\_ are descriptors \-- and also lets you code your own.

\_Decorators\_ are a simple syntax to feed a function as the argument to another (higher-order) function, and have the latter\'s resulting value used in lieu of the original function \-- while decorator syntax (\'@deco\') is new in Python 2.4, you can use the same approach with slightly clumsier syntax (\'func = deco(func)\') in 2.3 and even 2.2.

\_Metaclasses\_ are to classes as classes are to instances. Python\'s built-in metaclass is the built-in \'type\', and you can subclass and customize it to produce custom metaclasses to control behavior of whole family of classes.

This presentation shows how to best use each of these mechanisms, both in terms of existing, Python-supplied objects and types (descriptors, decorators and metaclasses), and of coding and using your own custom ones. What are \"data\" and \"non-data\" descriptors, and how and why might you code and use either kind? When do you need introspection to ensure proprer decoration, and how can Python\'s standard library help there? How should custom metaclasses cooperate to insure peaceful coexistence of several of them, and how can you solve metatype-conflicts? And, of course \-- how do custom descriptors, decorators, and metaclasses cooperate with each other, and with other powerful Python mechanisms such as introspection, closures and advanced dynamic gyrations, to let you write elegant and powerfully customized code with minimal effort? This presentation explores this kind of questions, providing the fundamental knowledge and the outlook that will help you answer the questions in the most useful ways for your own applications.

------------------------------------------------------------------------

#37. **Iterators and Generators: it ain\'t your gramps\' loop any more!**

Alex Martelli

Python\'s versions since 2.2 have introduced, enhanced, and clarified the \*iterator protocol\*, which describes how items are produced one after the other, in sequence, typically for use in a \'for\' statement, and supporting mechanisms \-- generators, the itertools module of the standard library, and now, in 2.4, \_generator expressions\_, which can be seen as a merge between list comprehensions and generators. This presentation takes its contents mostly from the \"Iterators and Geerators\" chapter of the Python Cookbook (2nd Edition), and focuses on some of the most interesting applications and related idioms presented there, with expanded explanations of the underlying language mechanisms and additional examples.

An \_iterator\_ is any object supplying a \'next\' method, callable without arguments, that satisfies certain conditions. A \_generator function\_ is a function which uses the \'yield\' keyword to return a \_generator iterator\_ object, whose \'next\' method is based on suspending and resuming the function\'s execution. The itertools module supplies several powerful \'building blocks\' to deal with iterables (including iterators and generators) and to produce them \-- itertools lets you program at a very high abstraction level while \_increasing\_ your code\'s performance (an \'abstraction BONUS\', rather than the abstraction \*penalty\* which is more common in other languages). Generator expressions are like list comprehensions which produce their results one item at a time, via an iterator, without taking up the memory needed to store all results at once.

This presentation shows how to best use each of these mechanisms to make your control structures reusable and simplify your application level code \-- by abstracting recursion and other rich and complicated iteration mechanisms into generators and the like. How can you repeat something 17 times, \_faster\_ than by \'for i in xrange(17):\'? How do you tame unbounded (infinite) sequences to your purposes? How can you \"peek ahead\" into an iterator without disturbing its iteration-state? This presentation explores this kind of questions, providing the fundamental knowledge and the outlook that will help you answer the questions in the most useful ways for your own applications.

------------------------------------------------------------------------

#39. **How to Build an Air Traffic Control System**

Neal Norwitz / [MetaSlash](./MetaSlash.html)

I\'ve been working on creating a new ATC system. Of course, it had to be written in Python. ![:-)](/wiki/europython/img/smile.png%20":-)") It also uses Twisted and the Tk canvas widget.

- It already has modest functionality. the situation display can display

aircraft and features of an airspace, such as waypoints, routes, restricted areas, etc.

------------------------------------------------------------------------

#40. **What is the PSF**

Neal Norwitz / [MetaSlash](./MetaSlash.html)

I would like to request that a time slot be reserved for someone (not me) to make a presentation about what the PSF is, its benefits, direction, etc.

------------------------------------------------------------------------

#42. **Keep It Simple with [PythonCard](./PythonCard.html)**

Kevin Altis

In this session, Kevin Altis will demonstrate the process of building cross-platform Python applications with graphical user interfaces using the [PythonCard](./PythonCard.html) framework and tool set. By giving you access to the full power of Python without requiring you to master complex GUI libraries, [PythonCard](./PythonCard.html) becomes a power tool for scripting users and professional programmers alike. Creating graphical desktop applications that run across platforms and take advantage of Python\'s simple elegance is easier than you think. And [PyCrust](../../../people/PyCrust), the embeddable Python shell, puts the power of the Python interpreter at your fingertips.

------------------------------------------------------------------------

#43. **Breaking the Rules of Commercial Software Development : Why and How we used Python to Produce a New Deal in Payroll Software.**

John Pinner / Clockwork Software Systems

Applications like accounts and payroll are the lifeblood of real world businesses. These applications are usually proprietary and subject to the usual proprietary software licencing mechanisms.

[PayThyme](./PayThyme.html) is a brand new UK statutory payroll application, the first genuinely new payroll software for some time, and the first Open Source UK payroll.

Commercially [PayThyme](./PayThyme.html) breaks new ground in almost every respect : it is the first UK native GNU/Linux payroll, and it has no built-in licence quota on numbers of users, numbers of employees and numbers of payrolls, all of which are restricted in most commercial payrolls. Furthermore, there is just one version of [PayThyme](./PayThyme.html), suitable for both the smallest and largest of payrolls, as opposed to existing software which is usually targetted in both capability and price at specific market levels. This allows your payroll to grow with your business. To further confuse conventional business software developers, [PayThyme](./PayThyme.html) is licensed under the GPL and is available as a free download.

Technically, [PayThyme](./PayThyme.html) is also unusual. It uses the Thyme development platform, which is itself Open Source and based on Python and the [PyQt](../../../gui/PyQt) GUI platform. A novel set of data-aware widgets links GUI screens (originated in Qt Designer) with Thyme\'s database filing system, allowing rapid object-oriented application development. The product was developed by a small core team of three people working remotely using a central Subversion repository. The user interface is implemented entirely in Python.

[PayThyme](./PayThyme.html) takes advantage of Python\'s rich set of extension modules, for example in implementing Internet Filing of end-of-year returns to the Inland Revenue via the UK Government Gateway.

------------------------------------------------------------------------

#44. **Object-oriented design with Python**

Bruce Eckel / www.[MindView](./MindView.html).net

This session presents general object-oriented design principles, but focuses on object design issues where Python is distinct from mainstream statically-typed languages.

For example: What kinds of Lightweight design tools make sense in Python, and which does Python obviate? What would it mean to have interfaces in Python, and what sort of features would be valuable? Since Python produces smaller code, can objects be bigger? Tradeoffs in static vs. dynamic type checking on design and implementation. What you can do in the constructor vs statically-typed languages.

Not rules, but guidelines and ideas presented for discussion: Interface inheritance vs. implementation inheritance, substitution vs extension, the impact of Python on these concepts. Partitioning your design into objects. Not enough objects and objects that are too big/complex. Creating robust objects. Wiring together objects to create an application. Design by contract; Base classes as interfaces with constraints. Preferring composition to inheritance.

Design patterns issues: Which design patterns in GoF are so C++-ish that they don\'t make sense in Python? Does the Visitor design pattern have any relevance in Python? Built-in design patterns: Generators (special case of factories). Python and the homogeneity problem (Composite pattern, using isinstance).

An [OpenSpace](OpenSpace) discussion will follow as soon after the session as availability permits.

Bio: [http://mindview.net/Etc/About/about.html](http://mindview.net/Etc/About/about.html)

------------------------------------------------------------------------

#45. **py.test and the py lib**

holger krekel / merlinux GmbH

Authors: Holger Krekel, Armin Rigo

We present a novel testing tool which allows to write unit tests with hardly any boilerplate. Unlike the many JUnit clones, py.test lets you use the plain assert statement. If failing, you get a convenient anaylsis of intermediate values in the assert\'s expression. Example:

    def f(): 
       return 23

    def test_something(): 
       assert 42 == f()

is the full content of a file that you can run with py.test: no imports, no inheriting classes or other magic incantations needed. Just write a global function that starts with \'test\_\' and run py.test on that file. You will see in the py.test generated traceback that \"42 == 23\" failed. Reusing the \'assert\' statement is actually closer to the mother of JUnit/testing: SUnit from the Smalltalk world.

For the failing assert expression we use a hack to directly re-interpret its Syntax Tree. This is a limited AST-Mini-Interpreter, as it can only interpret expressions and a number of statements but luckily this is more than enough to give you precise clues for why a test fails at a certain assertion.

Generally, testing is a perfect match to control and make full use of Python\'s flexibility. But unfortunately, the testing mechanisms of most python projects are more or less entangled hacks around unittest.py. We think that we can and should do better than this.

Basically py.test aims to provide a new integrated and pythonic test environment which enables \_sharing\_ of common testing support code, such as HTML and PDF reporters, GUIs and customization or mock-object facilities.

But there is more. Apart from the user-exposed test facilities and features the py lib contains higher level introspection classes, support for dynamic code generation, a new approach to distribute python code across networks and processes, and a \"Path\" abstraction allowing uniform access to the local file system, subversion file systems or remote Path objects through e.g. SSH connections. We\'ll see if there is enough time to talk about all of the latter (otherwise we intend to do lightning talk demonstrations).

------------------------------------------------------------------------

#46. **The Compete File System: File System Virtualization using Python**

Christopher Gillett / Compete, Inc.

The Compete File System (CFS) is a file management and file system virtualization software layer and Unix command set. CFS provides a framework for distributing files across multiple file systems while allowing the end-user or software developer the convenience of viewing the multiple systems as though they were a single large file system. Internally, CFS uses load balancing and server scheduling algorithms to provide maximum file system space availability while maintaining file server performance. CFS provides this functionality while still remaining in user application space - modifications to the operating system kernel are not necessary, and CFS never needs to operate in kernel or protected mode. In fact, to the extent that the underlying physical file systems can map to the local host\'s file system, CFS is largely system and platform independent.

CFS is written entirely in Python. The ability to develop high quality code extremely rapidly using Python combined with the depth and sophistication of the Python runtime system allowed a very small team to create this powerful system-level software package very quickly.

------------------------------------------------------------------------

#47. **Query-directed Data Mining using Python and Parallel Processing**

Christopher Gillett / Compete, Inc.

Compete, Inc. has built a query processing system using Python which forms the basis for all query-directed data mining within our company. The system accepts queries written in \"near SQL\" syntax and performs parsing and analysis of the queries. Query decomposition allows exploitation of parallel computing resources and allows queries involving large amounts of data to be answered comparatively quickly.

The system was built entirely using Python and is used in conjunction with the Portable Batch System and various Unix utilities.

------------------------------------------------------------------------

#49. **Profiling and Visualizing Python Program Behavior**

Richard Saunders / Rincon Research Corporation

This talk gives a brief overview of Python\'s facilities for profiling and debugging, and then presents a new architecture (ULMA \-- Ultra-Light Monitor Architecture, devised in collaboration with Clinton Jeffery at New Mexico State University) for program execution monitoring. We have implemented an initial set of ULMA facilities by extending and adding instrumentation to the Python interpreter. Execution behavior information is delivered via shared memory to monitor(s) written in C, Python, or Unicon.

------------------------------------------------------------------------

#50. **Decimal Module for Beginners**

Michael Chermside / ING Direct

This is an introduction to the new decimal module. It endeavors to explain why we might want support for decimal floating point in Python, and then provides some examples of its use. If you have read PEP 327 and perhaps played around with the module once or twice, then you probably already know everything covered in this talk, but if you have heard that there was a decimal module and are curious, or if you think you might want to use such a thing but aren\'t really sure, then this is for you.

------------------------------------------------------------------------

#51. **Sequential code in an event-driven world**

Nat Goodspeed / [SolidWorks Corporation](http://www.solidworks.com)

In an event-driven system such as a game environment, it\'s common to want to start some action, such as an animation, that will run for several frames. But in an event-driven system, control reaches the same entry point over and over again. There are various ways to ensure that the right code is executed for each frame \-- but using Python generators makes it remarkably natural and readable.

This talk presents the Animator class, along with its friends and relatives TimeAnimator, Sequencer and AlarmClock.

------------------------------------------------------------------------

#53. **Writing Efficient Rule-Driven Software in Python**

Phillip J. Eby / Telecommunity Consultants

In the design of applications, rules are everywhere: business rules, game rules, routing rules, \"expert systems\", code and query optimizers, and rule-based \"agents\" and triggers. But to implement rules, they have to be converted into code \-- usually in the form of decision trees that become increasingly difficult to maintain as the number of rules grows. Recent developments in computer science, however, make it possible to automatically convert rules into decision trees that are guaranteed to be correct and efficient, even for large numbers of rules, without using a specialized logic or rule language like Prolog or Lisp. This presentation will give an overview of how to implement rule-driven systems directly in Python, using Python itself as the language for specifying rules, with faster development and execution times than would be obtained by hand-coding if-then trees. Examples will be based on the predicate dispatch implementation included in the latest version of the [PyProtocols](./PyProtocols.html) package.

------------------------------------------------------------------------

#55. **[SchoolBell](./SchoolBell.html): a Zope 3 Calendar Server**

Tom Hoffman / [SchoolTool](../../../people/SchoolTool)

[SchoolBell](./SchoolBell.html) is an open source calendar server for small to medium sized organizations, written for Zope 3. Each person, group or resource has a calendar accessible via an HTML interface. A user can integrate events from other people or groups into their calendar. iCalendar support allows interoperability with clients like Mozilla Calendar and Apple\'s iCal. Access control can be set for each calendar to allow events to be viewed or added by specific users or groups.

[SchoolBell](./SchoolBell.html) is also a Zope 3 application that breaks out of the Zope 2\'s \"folders and documents\" paradigm, instead using a directed graph data model. Application objects, such as people, groups and resources. Each object can have facets which model the object\'s responsibilities and encapsulate its data for a particular role that object plays in the system. Objects are connected via relationships. Each relationship\'s type is defined, as is each object\'s role in the relationship. Each object, relationship, role and facet is identified by a URI, facilitating a comprehensive REST-style web services API for all the application\'s functions. This architecture has broad applicability outside of calendaring.

[SchoolBell](./SchoolBell.html) is based on [SchoolTool](../../../people/SchoolTool), a free IT infrastructure for schools, funded by the Shuttleworth Foundation. The initial design for [SchoolTool](../../../people/SchoolTool) was done by Steve Alexander of Canonical Ltd. Subsequent development has been done by Programmers of Vilnius and Etria LLC.

Project manager Tom Hoffman will begin with a tour of [SchoolBell](./SchoolBell.html), followed by a discussion of its unique architecture led by Brian Skahan of Etria.

------------------------------------------------------------------------

#56. **Yarn: Working with Messages in Diverse Formats and Protocols**

Abe Fettig / [JotSpot](./JotSpot.html)

People today read, write, and organize information stored in many different places, using many different formats and protocols. In the course of a single day, a person might read and send email, get the latest news through RSS, post to their weblog, create or edit a page on their Wiki, add a new site to their del.icio.us bookmarks, upload digital photos to Flickr, monitor items being sold on eBay, and check on the status of a package being shipped through UPS.

This poses a challenge for application developers. Users want their programs to be able to access their data, regardless of the system in which the data lives. But implementing support for all these formats and protocols is expensive and time consuming.

This talk introduces Yarn, a Python library that allows developers to work with a wide range of file formats, messaging systems, and web services, using a standard API. Yarn currently provides support for reading and writing RSS, Atom, OPML, mbox, and maildir files, on a local filesystem or over HTTP or SFTP; the Atom and [MetaWeblog](./MetaWeblog.html) blogging APIs; IMAP, POP3, and SMTP; and web services including Google, Amazon, Flickr, del.icio.us, and UPS package tracking. Yarn provides APIs for reading, writing, and editing messages, searching, and navigating folder trees. It also includes such helpful features as metadata storage, connection sharing, caching, and credentials management. An extensible architecture makes it easy to support new formats and protocols through plug-ins.

Yarn is written in 100% pure Python, using the Twisted framework. It is currently licensed under the GPL, but will be released under a more liberal license before [PyCon](../PyCon) 2005.

This talk will introduce Yarn and show how it can be used to add powerful messaging and publishing functionality to Twisted applications.

- It will demonstrate how the command-line utilities included in Yarn can

be used to read and copy messages, even between systems that don\'t speak the same protocol. It will also present code examples showing to use Yarn in various ways.

------------------------------------------------------------------------

#57. **Introduction to PyObjC**

Bob Ippolito

Introduction to PyObjC is a quick tour of PyObjC suitable for anyone with Python experience looking to get their feet wet with Cocoa development with their programming language of choice. Prior Objective-C knowledge or Interface Builder experience is not necessary.

------------------------------------------------------------------------

#58. **PyObjC Hacking**

Bob Ippolito

PyObjC Hacking is a quick tour of advanced uses for PyObjC and related tools. This talk is geared toward those who have a working knowledge of PyObjC (or at least attended Introduction to PyObjC) and ideally understand data structures at the C level.

------------------------------------------------------------------------

#59. **[OpenLaszlo](./OpenLaszlo.html): A Python Success Story**

Oliver Steele / Laszlo Systems, Inc.

[OpenLaszlo](./OpenLaszlo.html) is an open source platform for developing interactive client-side web applications. It consists of a compiler, that compiles XML with embedded [JavaScript](./JavaScript.html) to (currently) Flash files; and a runtime XML and [JavaScript](./JavaScript.html) library. Applications built using the Laszlo platform have been deployed on the Earthlink home page and Yahoo, among other sites.

The [OpenLaszlo](./OpenLaszlo.html) compiler and application optimizer were implemented in Jython. The use of Jython allowed us to implement a full-featured deployable [JavaScript](./JavaScript.html)-to-bytecode compiler in a short amount of time (three months).

This talk will describe how Jython\'s introspective, interactive, and integration features enabled the use of development methodologies that made this development speed possible, and how having the compiler in Jython then allowed us to experiment with innovative new features at a rate that would have been discouraged by a static system. It will also describe the challenges of actually deploying a Jython-based solution.

------------------------------------------------------------------------

#60. **The Time of Day**

Anna Ravenscroft

This presentation will provide an overview of the options available in Python\'s datetime module, and some of the third-party packages such as dateutil that have been developed in response. We will explore such topics as time durations, recurrence rules, and fuzzy parsing, then tackle the intricacies of time zone support.

The presentation will start with datetime fundamentals, introducing the different kinds of datetime instances. It will explore some common problems with dates, then delve into the trickier issue of timezone support.

The presentation will provide a brief overview of the features available in two third-party packages: dateutil, which supplies a variety of handy utilities including finer manipulation of date operations, recurrence rules, and fuzzy parsing, and a form of timezone support; and pytz, which provides a convenient Python implementation of the Olson timezone library. The presentation will finish by exploring some of the issues involved in working with timezones and demonstrating of how these package deal with those issues.

The presentation is intended for beginners and intermediate pythonistas.

------------------------------------------------------------------------

#61. **Streaming Python**

Thomas Vander Stichele / Fluendo

Flumotion is a GPL streaming media server written in Python. It is distributed and component-based: every step in the streaming process (production, conversion, consumption) can be run inside a separate process on separate machines.

Flumotion uses Twisted and GStreamer. Twisted enables the high-level functionality, distributing components over the network. GStreamer, through the Python bindings, enables the high-speed low-level functionality: actual media processing.

Flumotion uses a central manager process to control the complete network; one or more worker processes distributed over machines to run actual streaming components; and one or more admin clients connecting to the manager to control it.

Flumotion is a young project under very active development. In its current release (0.1.4), it already supports the following features:

\- various sources: webcams, soundcards, TV cards, Firewire cameras

\- various codecs: Vorbis, Theora, mulaw, JPEG, smoke

\- various containers: Multipart, Ogg

\- username/password authentication

\- overlaying, colorbalance

\- HTTP streaming

\- disk archiving

\- administration GUI with a wizard for the most basic scenario

\- code distribution from a central location

\- local caching of the distributed code space

\- strong focus on ease of use and usability

The current design allows for the following future features:

\- multiple GUI\'s thanks to clean model/view separation in admin clients

\- any number of sources/containers/codecs/effects/protocols to be added

\- completely centralized code upgrades

\- complete code upgrades with minimal downtime

\- any kind of authentication mechanism (key exchange, challenge/response, \...)

\- any number of possible scenarios for actual content production and distribution

\- manager failover and state replication

\- loadbalancing streams over different servers or from different locations

\- internal stresstests

Some of the features are only possible or easily implementable thanks to using a high-level language like Python:

\- sending GUI code for the wizard and component administration from the manager to the admin client, making the admin GUI a lightweight shell

\- sending component code to any of the workers over the wire at startup

\- rebuilding modules and reloading code on the fly while running; allowing for a distributed code upgrade without losing clients

\- rapid development of new components, allowing to catch up with and eventually to keep one step ahead of the competition

\- easy networking code thanks to Twisted

In this project, we came up with solutions to specific problems presented to us that would be interesting to share with others.

\- all code is stored centrally and partitioned into \"bundles\" which are cached by clients who need them. Versioning and dependencies are correctly handled, and to the code being run this is handled transparently. Code can still import as if it were one big file tree.

\- the manager sends GUI code to an admin client and component code to a worker. The GUI code running on the admin machine then controls the behaviour of code running on the worker machine by going through the manager machine

\- state of components is automatically replicated one level deep to the manager, and two levels deep to all connected admin clients

\- authentication of any service in the network is handled by creating keycards which can be exchanged between all processes, implementing any type of challenge/response authentication as securely as possible.

\- Twisted\'s Perspective Broker was extended to use this generic keycard concept instead of the current (limited) username/password credentials.

\- the open-ended nature of Twisted and GStreamer is difficult to harness into a usable GUI. The wizard provides a good way of crystallizing all possibilities into a sensible task-based presentation. The design of the wizard also incorporates the flexibility of the network distribution and the dynamic code distribution by pulling in the necessary GUI code for the next step based on previous choices.

\- moving to run-time checks of functionality as opposed to compile/configure-time. Since the server can be distributed over any number of machines, and actual components have different run-time needs, all checks for features (devices, required libraries, versions, permissions)

Python also presents some specific challenges when used in a large project as compared to more low-level languages. When handled right, these can actually be turned into project engineering advantages. Python\'s weak argument typing forces developers to document the API correctly. Python\'s dynamic nature (running code from received chunks, extensive subclassing) and Flumotion\'s design (componentized functionality, lots of small pieces of code sent back and forth) forces us to aggressively write unit testing for all functionality.

------------------------------------------------------------------------

#62. **Acceptance of XML in the Python Community**

Fred L. Drake, Jr.

The acceptance of XML as a general tool in the Python community has been less than overwhelming. This presentation discusses the reasons for this, and what, if anything, should be done to change the situation.

------------------------------------------------------------------------

#64. **pyblosxom: A microkernel approach to blogging**

Ted Leung

pyblosxom is a weblogging system written in Python. It uses the filesystem storage model pioneered by blosxom, but has diverged in terms of internal architecture and organization. pyblosxom takes a microkernel approach to blogging software by providing a small core framework that embodies the blogging data flow. Callbacks are placed at strategic points so that users may override as much or as little of the framework\'s default functionality as they desire. These callbacks can be used implement plugins whose functionality can range from alternate page rendering to comments to calendar based archives.

pyblosxom has a growing user base and a small, friendly development community. Our goal for this presentation is to increase awareness of blogging in the Python community, provide an introduction to pyblosxom and its capabilities, and describe enough of the pyblosxom internals to attract additional developers to the community.

------------------------------------------------------------------------

#65. **Developing Database Applications With Schevo**

Patrick K. O\'Brien / [Orbtech](http://orbtech.com/)

[Schevo](http://schevo.org/) is both an ODBMS and an Application Framework for Python. It is a toolkit for developing object-oriented database applications, but it also provides a model for the design, persistence and evolution of application domain objects.

Schevo supports the storage of these objects in a variety of back-ends, such as Pypersyst, ZODB, and Durus. It supports the maintenance of these objects through a variety of user interface toolkits, such as Qt/PyQt, wxPython, Plone, and Nevow. And it can be used as easily by novices as it can be by experienced Python developers. Come see the latest innovation in data management - Schevo.

A companion paper on Schevo that covers more than was able to be presented (and includes lots of pretty screen shots and more detailed explanations of Schevo concepts) is available here:

[http://schevo.org/documentation/reference/current/](http://schevo.org/documentation/reference/current/)

Just look for the [PyCon](../PyCon) 2005 link.

------------------------------------------------------------------------

#67. **[PyWebOff](./PyWebOff.html): Mapping the python web application frameworks**

Michelle Levesque / University of Toronto

Python\'s simplicity principle (\"there should be one \-- and preferably only one \--obvious way to do it\") has been a major contributer towards making Python so accessible to new users. Unfortunately, this principle doesn\'t seem to apply when choosing a web application framework: there are several dozen to choose from and no guide is available to help make the decision easier.

The presentation will consist of four parts: a description of the problem and justification for why it is indeed a problem (5-10 mins), an introduction to [PyWebOff](./PyWebOff.html) (5-10 mins), a summary of some of the findings (20 mins), and a discussion of what the next few steps should be towards solving this problem (10 mins).

This 45 minute presentation would be useful to those looking to choose a framework, framework developers, and anyone who has an interest in Python as a web development tool.

------------------------------------------------------------------------

#69. **Stupidity and laser cat toys: Indexing the US Patent Database with Xapian, Twisted, and Nevow**

Michael Salib / Divmod

I recently downloaded the full text of the US Patent Database. It seemed like a good idea at the time. This talk will show how I built a cool web search engine for it using Xapian, an open source full text indexing library, Twisted, the ultimate network coffee maker, and Nevow, the most awesome web templating system ever invented. While these tools are very powerful, they all have their own pitfalls. I\'ll show how to put them all together and get something useful as a result.

------------------------------------------------------------------------

#70. **A Python Preprocessing Framework for Hydrologic Modeling**

Dr. Vic Kelson / WHPA Inc.

At our hydrological consulting firm, we often encounter modeling problems in which a variety of different hydrological model codes are to be used on a single project. We typically use models that are based on the Analytic Element Method, in which the input data for the models are vectors and the model domain is a continuum. In particular, we often use the 2-D groundwater code ModAEM (Kelson, 1998) and TimML (a 3-D analytic element model written in Python with Fortran extensions). It is becomming more and more important to make use of ModAEM for regional simulations, then extract a local 3-D model for use in TimML. In addition, we make use of inverse modeling (parameter estimation) codes, such as PEST.

The use scripts that within GIS software, such as ArcGIS or Manifold, is one option, but those codes run only on Windows, and we need the ability to run models on other platforms (e.g. a Linux cluster). We also encounter data in a wide variety of formats, ranging from GIS project files to ESRI Shapefiles to flat comma-separated variable files or even SQL databases. What we need is the ability to:

1\) Prepare model input files from spatial (and other) data sets

2\) Script the operation of our models (especially for use in inverse modeling)

3\) Use data from a wide variety of GIS and other formats

4\) Transfer results from one model as input for another

5\) Facilitate analysis of model results.

We also prefer to make use of open file formats and we use Linux systems for large computational scripts.

The author has developed a Python framework that hides the I/O details for a variety of different data storage formats, for the purpose of building preprocessing and postprocessing scripts for hydrological models. Currently, these tools are used with our in-house analytic element codes, but we expect to implement facilities for use with finite-difference codes, such as MODFLOW. The talk will describe the problem and the Python object-oriented framework for model preprocessing, including the way it has been extended for transferring data between models.

------------------------------------------------------------------------

#71. **CMFEditions Internals**

Gregoire Weber (nick: gregweb)

This is about the design goals of CMFEditions and about the architecture chosen. CMFEditions\' main design goal was easy replacement and extensibility of different components. A simple storage API allows third party to write new storages. There is also a registry for components which together define an objects boundaries.

Unfortunately I had to cancel my presentation because I had the flu. A prosa version of the presentations content is available at:

- [presentations content](http://www.incept.ch/opensource/CMFEditions/DevelDoc.html) / [at sourceforge.net (24h behind)](http://cvs.sourceforge.net/viewcvs.py/*checkout*/collective/CMFEditions/doc/DevelDoc.html?rev=1.4)

Code:

- [CMFEditions at the Plone collective at sourceforge.net](http://cvs.sourceforge.net/viewcvs.py/collective/CMFEditions/)

For questions:

- [collective-versioning@lists.sourceforge.net](mailto:collective-versioning@lists.sourceforge.net) / IRC: #cmfeditions at irc.freenode.net

------------------------------------------------------------------------

#72. **WSGIKit: Utilizing WSGI as a platform for inter-framework cooperation**

[Ian Bicking](http://blog.ianbicking.org) / [Imaginary Landscape](http://www.imagescape.com)

[WSGI](http://www.python.org/peps/pep-0333.html) (the Web Server Gateway Interface) is a new standard for connecting servers to Python web development framework. WSGI also has the potential to connect frameworks together, and to provide framework-neutral services.

WSGIKit is a reimplementation based on WSGI of the Webware For Python web framework. The implementation maintains backward compatibility, while decomposing many of the functions of Webware into framework-neutral pieces of \"middleware\". The design of WSGIKit can provide an example of how to use WSGI outside of framework-server connections.

------------------------------------------------------------------------

#73. **The Personal Internet Endpoint: Using Python and Twisted to write Reliable Peer-To-Peer Programs**

Glyph Lefkowitz / Divmod

The internet is designed to facilitate symmetric connectivity between peers. With the advent of personal internet access, however, several features of today\'s internet, including network address translation, corporate firewalls, and dynamically assigned IP addresses, those connections are now far from symmetric, and in many cases not even possible.

This paper will explore several solutions to this problem which use Python\'s inherent flexibility and Twisted\'s networking infrastructure to solve it in a general manner. Several code examples will be presented where, using Twisted\'s separation of protocol and transport layer, existing applications are made to work by modifying only one or two lines of code.

It will cover each of the obstacles to connectivity in order of difficulty: dynamic IPs, NAT, and finally firewalls. It will also discuss the security, user interface, and application ramifications of being able to provide connectable services on each user\'s PC and/or other IP connected device.

Covered networking techniques will include:

- Detecting the ability to open a port on a static, internet-visible IP, by providing a callback server.
- Using stateful UDP filters on most modern firewalls to provide a temporary, virtual connection.
- Load-balancing so that users with truly broken connections (such as those made through a corporate firewall using the \"CONNECT\" HTTP command

through a proxy) can piggyback on users with more open connections without causing them an undue amount of load.

Existing internet standards will be covered as well:

- SIP \* STUN \* UPnP

Finally, the paper will propose a standard set of techniques and an accompanying protocol for gradually and gracefully falling back to progressively less efficient techniques so that transport-level concerns don\'t interfere with an application\'s functionality until it is actually impossible to establish any kind of connection.

The presentation will cover a several of the techniques explored in the paper and will focus on real-world implementation and deployment of these techniques. It will present code examples, and include several demonstrations, hopefully using the wireless internet access provided by the conference, but with a small virtual network if that one is unavailable for some reason.

------------------------------------------------------------------------

#75. **Developing Responsive GUI Applications Using HTML and HTTP**

Donovan Preston / Divmod

Google\'s Gmail was the first high-profile example of a highly responsive web application, blurring the line between the desktop and the web. The techniques employed by it to reduce perceived latency have been available for years, but involve a large amount of [JavaScript](./JavaScript.html) that can be difficult to implement. This presentation will discuss the history of these techniques, implementation strategies, and the use of [LivePage](./LivePage.html), included within the Nevow web application framework.

------------------------------------------------------------------------

#76. **Pychinko: A Native Python Rule Engine**

Yarden Katz / MINDSWAP

Rule processing engines have proven to be useful in several areas of Computer Science and software engineering, ranging from expert systems in bioinformatics to serving as backends for web content management platforms. Pychinko is a forward-chaining rule engine capable of the generic use rule engines have traditionally received, but geared for Semantic Web applications. Pychinko, implemented purely in Python, employs the well-known and scalable Rete algorithm for expert systems. We present the use and architecture of Pychinko (including a brief exposition of the Rete algorithm), as well as several of its compelling use cases, including examples from software engineering, web applications, and Semantic Web specific tasks.

------------------------------------------------------------------------

#77. **Scratching an Itch (or, how to insure your book collection with [PyAmazon](../../../people/PyAmazon), ZODB, and wxPython)**

Michael Bernstein / Panhedron

This presentation is about how I used Python to build a simple solution for inventorying my extensive book collection for insurance purposes. It demonstrates Python\'s strengths in increasing programmer productivity through simplicity, availability of standard and third-party libraries, and flexibility.

------------------------------------------------------------------------

#78. **[PyPy](../../../implementations/PyPy) and type inference**

Armin Rigo

A technical status report on [PyPy](../../../implementations/PyPy), the Python interpreter implemented in Python.

The [PyPy](../../../implementations/PyPy) project aims at producing a simple runtime system for the Python language, expressing the basic abstractions within the Python language itself. Simplicity and Flexibility are the foremost goals. We hope to reach around [PyCon](../PyCon) a C-translated version of [PyPy](../../../implementations/PyPy) that is able to work independently of CPython.

To reach our goal, we are currently working on a Python source analysis and compilation toolchain \-- based on [PyPy](../../../implementations/PyPy) as well \-- and a minimal low-level core that doesn\'t need CPython any more. The presentation will focus on these tools, which are able to perform automatic static type inference of \"static enough\" Python programs and then compile them to various lower-level languages (currently C, Lisp, Pyrex and Java). This analysis works on fully standard Python sources (bytecodes, actually), and the distinguishing feature of the techniques we use \-- \"abstract interpretation\" \-- is to allow type inference to be performed for any language for which we have an interpreter. Moreover, it doesn\'t require explicit type annotations added by the user.

In the presentation, we will see how these tools can be used generally, i.e. how you could use them to check or improve the performance of your programs. In particular, what are the \"staticness\" restrictions that must be met for these tools to work?

We will then look under the hood:

\* how we build control flow graphs;

\* how we perform type inference, and what \"type inference\" precisely means in this context;

\* type inference is not the end of the story: good code must be generated from the source and the inferred types.

The techniques relate to Psyco\'s, the just-in-time specializer for CPython. We will compare them, and also contrast the \"internal\" notion of type used as an implementation detail (as in [PyPy](../../../implementations/PyPy) and Psyco) with the other typical approach of explicit user-specified types.

Our approach is motivated by the desire of flexibility: it allows issues that normally require early design decisions to be postponed, and addressed later in possibly more than one way, without rewriting everything. Typical example: adding Stackless-style continuations in CPython required a whole-scale rewrite, but has only a \"local\" impact on [PyPy](../../../implementations/PyPy). We will plead for a framework based on interpreters as a way to gain the most flexibility from programming languages \-- and the best performances too, for very-high-level languages!

------------------------------------------------------------------------

#79. **Improving Python\'s Memory Allocator**

Evan Jones / University of Waterloo

One of Python\'s primary benefits is that it automatically manages memory, as any high level language worth the name should. Unfortunately, Python never actually releases any RAM to the operating system. My presentation will discuss how Python\'s current memory allocator works, and describe the problem in detail. I will then present some workarounds to avoid the problem with the current version of Python. Next, I will present my proposed changes to the allocator which resolve the problem. Finally, I will suggest a future direction for Python memory management.

For additional information on this topic, see my web page about the problem, or the Python-dev archives:

[http://evanjones.ca/python-memory.html](http://evanjones.ca/python-memory.html)

[http://mail.python.org/pipermail/python-dev/2004-October/049480.html](http://mail.python.org/pipermail/python-dev/2004-October/049480.html)

------------------------------------------------------------------------

#80. **Advanced Server side Programming in Jython**

S.Prasanna / M.E Computer Science, Anna University

The paper discusses in detail about servlet and servlet filters programming in Jython. When I started Jython programming I struggled to get some useful and genuine resources on Jython server side programming especially for servlet filters. This motivated me to write a unique and a different tutorial in jython. I hacked into Jython and did some work in this area and now I use Jython instead of pure Java for server side programming.

This white paper can be regarded as a simple and a genuine Jython server side programming tutorial and its a small contribution from my side to the Jython community. This paper also explains how to compile some latest python modules in jython with a simple example.

In short the objective behind this tutorial is to portray the capabilities of Jython in server side programming and how to use Jython with some latest Python modules.

------------------------------------------------------------------------

#81. **Envisage - An Extensible Application Framework**

Martin Chilvers / Enthought Inc

The Java world has two dominant frameworks for extensible application development: Netbeans and Eclipse. Although many people think of these two projects as IDEs, they are both built upon open architectures that are designed to support generic GUI application development. Treading lightly in the footsteps of these two excellent projects, Envisage attempts to bring similar capabilities to the Python community.

The heart of Envisage is its plug-in architecture; in fact, the Envisage core is little more than a system for discovering, loading, starting and stopping plug-ins. Developers construct applications by choosing from the set of supplied plug-ins (possibly the empty set) and then adding their own to provide domain-specific functionality. Although an Envisage application need not have a GUI, Envisage comes with an ever-expanding set of plug-ins that simplify many of the more common and tedious aspects of GUI development (e.g., window management, menubars/toolbars, user preferences). It is worth noting that these \'standard\' plug-ins are written in exactly the same way as those written by an application developer. Each plug-in uses the Envisage extension mechanism not only to contribute to what came before it, but also to define how future plug-ins can contribute to it. This mechanism is simple but consistent, and ensures that even extensions to an application are extensible.

Despite the fact that development is still in its early stages (especially when compared to the enormous effort that has gone into both Netbeans and Eclipse), Envisage has already been used to deliver production applications, with two more scheduled in the first half of this year.

This presentation will introduce the Envisage plug-in architecture, and demonstrate how applications both with and without GUIs can be built with it.

------------------------------------------------------------------------

#82. **Traits - The Next Generation**

David Morrill / Enthought Inc

Traits is an open source Python package developed at Enthought, Inc. that adds an interesting collection of capabilities to the Python developer\'s toolkit. In a nutshell, one could say that Traits \"adds type checking\" to Python, but that would be a misleading oversimplification. Perhaps a more useful characterization would be in terms of the five major features of the package:

\- Initialization - Validation - Notification - Delegation - Visualization

Traits has been used at Enthought over the last two and half years in a variety of projects written for real-world clients. During that period, Traits has evolved from an interesting set of features embedded within the Chaco scientific plotting package to a separate package which, along with Envisage, is now the cornerstone for all of Enthought\'s Python development efforts.

As part of that evolution, Traits has recently been rewritten from the ground up to take advantage of our experience developing applications using the orginal Traits package, and to address a number of performance and software engineering issues that had arisen. The result is a new, streamlined, faster version of Traits which is capable of solving a much broader range of programming problems in a very straightforward, simple, efficient, and, dare we say it, elegant, fashion.

The purpose of this talk will be to introduce the audience to the Traits package, provide examples and demonstrations of Traits in action, and to describe some of the better design patterns, such as MVC (Model, View, Controller), that Traits supports, and in fact, encourages.

------------------------------------------------------------------------

[CategoryPyCon2005](CategoryPyCon2005)
