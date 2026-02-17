# PyCon2006/Talks

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

For more information about [PyCon](PyCon) 2006, see the main conference site at [http://us.pycon.org/](http://us.pycon.org/).

------------------------------------------------------------------------

#1. **Introduction to Pyparsing: An Object-oriented Easy-to-Use Toolkit for Building Recursive Descent Parsers**

[PaulMcGuire](PaulMcGuire)

pyparsing is a pure-Python module, containing a class library for easily creating recursive-descent parsers. pyparsing\'s syntax provides tools for both simple tokenization and data structuring and interpretation. I will give an overview of the basic features of pyparsing, and a \*very quick\* overview of the advanced features. I will close with 3 or 4 application examples, time-permitting. (For more detail on the type of information I have to present on pyparsing, you can visit my [SourceForge](SourceForge) project web page at [http://pyparsing.sourceforge.net.)(I](http://pyparsing.sourceforge.net.)(I) have posted the presentation materials at my personal web page: [http://www.geocities.com/ptmcg/python/index.html](http://www.geocities.com/ptmcg/python/index.html).)

------------------------------------------------------------------------

#2. **Agile Documentation: using tests as documentation**

Grig Gheorghiu

Agile Documentation means having unit tests serve a double role: testing your code and documenting it at the same time. I borrowed the term \"Agile Documentation\" from an article called \"Double Duty\" written by Brian Button.

In the talk, I will show how doctest and epydoc make it very easy to automatically generate documentation in the form of Test Lists and Test Maps. To see how it all integrates together, check out [http://agile.unisonis.com/epydoc/blogmgmt/](http://agile.unisonis.com/epydoc/blogmgmt/)

I will also show how the Django project generates API reference Web pages automatically from doctest-based unit tests.

I will finish my talk by mentioning the Wiki functionality of [FitNesse](./FitNesse.html) as a mechanism for using acceptance tests as documentation.

The talk is based on the following blog entries I posted:

[http://agiletesting.blogspot.com/2005/02/agile-documentation-with-doctest-and.html](http://agiletesting.blogspot.com/2005/02/agile-documentation-with-doctest-and.html)

[http://agiletesting.blogspot.com/2005/08/agile-documentation-in-django-project.html](http://agiletesting.blogspot.com/2005/08/agile-documentation-in-django-project.html)

[http://agiletesting.blogspot.com/2004/11/writing-fitnesse-tests-in-python.html](http://agiletesting.blogspot.com/2004/11/writing-fitnesse-tests-in-python.html)

------------------------------------------------------------------------

#4. **An Interactive Adventure Game Engine Built Using Pyparsing**

[PaulMcGuire](PaulMcGuire)

A pure-Python command interpreter engine for creating text adventure games. Used as an example of creating a custom \"little language\", in this case, the domain being a simple text-based adventure game. Provides a complete example of using pyparsing to structure input commands, with an internal Command structure to implement command behavior. (I have posted the presentation materials at my personal web page: [http://www.geocities.com/ptmcg/python/index.html](http://www.geocities.com/ptmcg/python/index.html).)

------------------------------------------------------------------------

#5. **Desktop Application Programming With PyGTK and Glade**

Michael Urban / Lion Research Center

GTK is the standard toolkit used in the Gnome desktop environment. Python, combined with PyGTK and the Glade visual designer is rapidly becoming the Visual Basic of the Gnome world for quickly and easily building fully featured GUI applications. However, applications written in Python and PyGTK are not restricted to Gnome or Linux. In fact, Python and PyGTK can fill the same roles as Java and Swing when it comes to writing cross-platform desktop applications.

In this tutorial presentation, I will show how to use the Glade visual designer plus the PyGTK module to quickly and easily build GTK applications using Python. Since GTK was originally written for programming the GIMP image manipulation program, we get a lot of very powerful image manipulation capability for free in GTK. As such, the tutorial will be focused around a simple image processing program that will give us the ability to preview images in a file window, load images for viewing, and rescale images. I will close the tutorial by giving a demonstration of a significantly complex real world Python PyGTK application that exercises many of the features of PyGTK including image editing, tables with custom table cell renderers, resizable dividers, and complex data entry forms.

------------------------------------------------------------------------

#6. **Vertebral Fracture Analysis**

Wesley J. Chun / [CyberWeb Consulting](http://cyberwebconsulting.com)

Vertebral Fracture Analysis

Several years ago, at [PyCon](PyCon) 2003, I presented a general paper on how [Synarc](http://synarc.com), a medical imaging company in San Francisco, developed medical applications using Python. This time, I would like to focus on one specific project which was my primary responsibility as a Senior Software Engineer there.

The VFract application is used as part of a set of radiology services offered by Synarc. In addition to data entry and image digitization, Synarc provides reading services using software such as VFract to obtain critical patient data necessary for pharmaceutical companies participating in clinical trials to determine the effectiveness of developing medicines. The use of such software helps automate and expedite patient assessment during the course of these clinical trials, overall accelerating the time it takes to get new medicines and treatments to market. The use of VFract has consistently resulted in a large portion of the company\'s annual revenue.

In this talk, we will discuss all four of the VFract applications, the open source components used to build them (specifically the use of Python as the primary development language), as well as what the general system hardware architecture is made up of.

------------------------------------------------------------------------

#8. **Scripting .NET with [IronPython](IronPython)**

Martin Maly / Microsoft

[IronPython](IronPython) is a fast implementation of the Python programming language on the .NET Framework. While it stays true to the beauty and simplicity of Python language, [IronPython](IronPython) offers Python programmers seamless access to the riches of .NET libraries and applications in a fully dynamic environment.

This talk will focus on practical side of utilizing the power of [IronPython](IronPython) beyond the interactive console development and exploration. It will demonstrate how to use [IronPython](IronPython) to add rich scripting support to existing .NET applications. This will allow us not only to explore and animate the application but also extend its functionality with custom Python code. We will also demonstrate how [IronPython](IronPython) can be used to bring together and orchestrate a wide variety of .NET components and services.

This talk is targeted at both Python programmers looking to take advantage the .NET Framework and at .NET programmers looking to learn how Python can make their jobs easier.

------------------------------------------------------------------------

#11. **Effective AJAX with [TurboGears](TurboGears)**

Kevin Dangoor / Blazing Things LLC

Modern web browsers, combined with programming frameworks like [TurboGears](TurboGears), allow for a rich interaction model that was not possible previously. This interaction model, which is commonly being referred to as AJAX regardless of whether XML is involved or not, brings new usability challenges. Just as people have gotten used to browser user interface elements that have become de facto standards, AJAX rises up to challenge user expectations.

This talk, and the accompanying paper, will briefly discuss some of the pitfalls and include demonstrations and code that illustrate ways to do AJAX so that users are pleasantly surprised, rather than frustrated.

Each discussion will include an example implementation done with Python and [TurboGears](TurboGears) with highlights of how the technique is actually implemented.

Though [TurboGears](TurboGears) will be used as the demonstration framework, previous experience with [TurboGears](TurboGears) will not be required to understand the talk or the examples.

The [paper and a screencast version of the talk](http://www.turbogears.org/preview/docs/tutorials/eajaxtg/) are online.

------------------------------------------------------------------------

#12. **Stackless Python in EVE Online**

Kristján Valur Jónsson / [CCP games inc.](http://www.ccpgames.com)

The massively multiplayer online role-playing game [Eve Online](http://www.eve-online.com), developed by CCP games in Reykjavík, Iceland, makes heavy use of [Stackless Python](http://www.stackless.com) to implement game features. This presentation shows how Stackless Python has been used throughout the code to create a seamless environment of cooperative multitasking in the game engine and how Python code and C code interacts in a complex real-world environment.

------------------------------------------------------------------------

#13. **Cuaima [MetaInstaller](http://cuaima.latinux.org). New tool for managing System Installations.**

Ricardo Strusberg / Latinux

Jesus Rivero / Latinux

Carlos Zager / Latinux

The intended use of this timeslot is to introduce \"Cuaima\" a new Web-Oriented (LGPL) software program we are writing to simplify the installation of custom GNU/Linux Distributions.

Cuaima is a [MetaInstaller](http://cuaima.latinux.org) for GNU/Linux and \*BSD Operating Systems that runs on top of a (Python) `WebServer` to provide local, remote and massive installations of these \*NIX flavoured Systems. The installer is capable of installing any kind of Distribution and configuring it properly with preconfigured files or custom parameters such as the Distribution to be installed, user parameters, root\'s password, network configuration, etc. Cuaima takes the whole process of installation to another level.

Cuaima is written almost entirely in Python. The rest of the code is Javascript for client-side tasks such as field validator\'s and an implementation of XMLRPC to provide real-time installation-progress information.

Cuaima is part of a larger sets of tools that is in the planning stage now to provide End-Users and Enterprises the ability to create Custom GNU/Linux Distributions for determined and particular uses.

It is proposed that the Cuaima [MetaInstaller](http://cuaima.latinux.org) be the Official Installer for the Official Venezuelan Republic GNU/Linux Distribution.

Official `HomeSite`: [http://cuaima.latinux.org](http://cuaima.latinux.org)

------------------------------------------------------------------------

#14. **Osh: An Open-Source Python-Based Object-Oriented Shell**

Jack Orenstein / Geophile, Inc.

Osh implements a language that supports the composition of commands through the piping of objects. This language is designed for use from the command-line of an ordinary shell. The objects piped from one command to the next can be Python primitives (numbers, lists, maps, etc.); other types such as dates/times, or database rows; or can represent various OS resources such as files and processes. Conversions between objects and strings simplify integration with the Unix environment. The commands included with osh manipulate objects, access databases, and execute commands remotely, including parallel execution on nodes in a cluster. Data manipulation commands allow the user to invoke functions, including lambda expressions, written on the command line.

Osh is licensed under the GPL. More information and a tarball can be obtained at [http://geophile.com/osh](http://geophile.com/osh).

------------------------------------------------------------------------

#16. **Decimal for beginners**

Facundo Batista

The idea is to let the reader to feel confident about this new data type in order to start using it, from the very beggining, explaining a lot of background concepts the user needs to start to understand floating point and decimal.

The presentation outline is:

- Why you might care?
- Technical background
- Let\'s use it!
- Some advanced use

------------------------------------------------------------------------

#17. **Large-scale, cross-platform synchronization using embedded python**

Alexis Lê-Quôc / [Wireless Generation](http://www.wirelessgeneration.com)

Wireless Generation uses python to allow the synchronization of student assessments, from 70k teachers assessing over 1.5 million students. Because python is a high-level language it is fit to solve problems both as an embedded cross-platform client and as a server-side component. This talk will present a few opportunities where python shone on the client-side:

- cross-platform support
- ease of integration with c++ libraries
- focus on higher-level logic with higher-level code
- savings in development time

Slides available [here](http://alq666.blogspot.com/2006/03/slides-from-my-pycon-2006-talk.html)

------------------------------------------------------------------------

#18. **Internet Access via Anti-Virus Policy Enforcement Software and Messaging Service**

Jason Hoerr / Albright College, Frank Wilder / P-Wave, Inc.

The presentation will cover the use of Python/wxPython/Perl/MySQL to create a set of tools to control access to the Internet for over 900 personal computers on a college campus. Access to the Internet is based on valid registration of the computer on the college network and the confirmation of a valid antivirus definition file. The tools set consist of a program that runs on each client machine as a service, another program that is used to display messages on the client machine and a set of code that manages the actual connection to the Internet via virtual network switching on Cicso switches based on setting in a MySQL database.

------------------------------------------------------------------------

#19. **State-of-the-art Python IDEs**

Jonathan Ellis / Berkeley Data Systems

This talk will build on the review of 6 IDEs done by the Utah Python UG and summarized here: [http://spyced.blogspot.com/2005/09/review-of-6-python-ides.html](http://spyced.blogspot.com/2005/09/review-of-6-python-ides.html). In the interest of time, this talk would focus on the most promising four IDEs: Komodo, [PyDev](PyDev), and Wing, which are in the review-of-6, and [SPE](http://pythonide.stani.be), which is not.

------------------------------------------------------------------------

#21. **Developing an Internationalized Application in Python: Chandler a case study**

Brian Kirsch / Open Source Application Foundation

Internationalization is the most often overlooked aspect of Application development. It is a mistaken belief that Internationalization can easily be added at anytime. This mistake ultimately results in developers frantically scrambling to patch together a solution for an architecture which was never designed for it. Too many products end up in a rewrite when the team finally discovers just how fundamental a role Internationalization plays.

This talk will cover general concepts on how to design Internationalized Applications, as well as focus in depth on the specific choices made for Chandler including leveraging Open Source libraries and designing for multiple Operating Systems.

------------------------------------------------------------------------

#23. Cancelled: **Processing XML with [ElementTree](ElementTree)**

Andrew Kuchling / PSF

[ElementTree](ElementTree) provides a simple library for processing XML that feels natural to Python programmers. This talk is a 45-minute tutorial showing how to perform basic tasks with [ElementTree](ElementTree).

------------------------------------------------------------------------

#24. **What is Nabu?**

Martin Blais / Furius

Desktop search tools (e.g. Google Desktop) build a database of the information that is stored on your computer. Wouldn\'t it be great if some of this desktop database could be used to automatically feed your online blog, or a website?

Also, wouldn\'t it be immensely useful if the \"types\" of information found in your documents could be automatically identified? (i.e. a mini \"semantic web\", but for your own files) For example, by finding all the \"addresses\" in all of your personal files, you could easily build your address book.

Are you someone who uses plain text files instead of fancy specialized programs to maintain your personal data?

If you find any of the above interesting, this talk is for you. I am proposing a system, Nabu, built in Python using [ReStructuredText](http://docutils.sf.net/rst.html), [Docutils](http://docutils.sf.net) and text files, that can be used to collect \"typed\" data from those files and fill a remote database with the extracted data. This data can then be used to feed a wiki, a blog, a web site, or any other kind of presentation layer you desire.

Related talks: [\"Docutils Developers Tutorial: Architecture, Extending, and Embedding\"](./PyCon2006(2f)Talks.html#A62) is for those interested in the implementation details of Docutils. [\"Easy Slide Shows With reStructuredText & S5\"](./PyCon2006(2f)Talks.html#A64) describes another application of Docutils.

There will also be a [Docutils sprint](./PyCon2006(2f)Sprints(2f)DocutilsSprint.html) following the conference.

------------------------------------------------------------------------

#25. **[TurboGears](TurboGears) Tutorial**

Mark Ramm

I will provide a tutorial for those interested in learning the basics of the [TurboGears](TurboGears) web programming megaframework.

------------------------------------------------------------------------

#26. **Packaging Programs with py2exe**

Jimmy Retzlaff / Aver Development Corporation

py2exe is a Python distutils extension which converts Python scripts into executable Windows programs, able to run without requiring a Python installation. This talk by the maintainer of py2exe will cover the simple use, options, more complex use, and future of py2exe.

------------------------------------------------------------------------

#28. Cancelled: **SAGE: Software For Algebra and Geometry Experimentation**

William Stein / Dept. of Math., Univ of California, San Diego

------------------------------------------------------------------------

#29. Cancelled: **Python in Business : Thyme, a business-oriented Python development framework.**

John Pinner / Clockwork Software Systems

At [PyCon](PyCon) 2005, I presented [PayThyme](./PayThyme.html), Clockwork\'s industrial-strength UK statutory payroll. There was some surprise that we had licensed such a commercial application under the GPL. Since then [PayThyme](./PayThyme.html) has been used by over 1000 companies and at London\'s [LinuxWorld](./LinuxWorld.html) expo was the outright winner of Best Open Source Application.

[PayThyme](./PayThyme.html)\'s development platform is Thyme, our own Python development framework based on Python, C and [PyQt](PyQt). It allows us to develop business applications very quickly indeed.

This presentation describes Thyme, the rationale behind its design, demonstrates it in use, and shows how we are updating and extending it.

------------------------------------------------------------------------

#30. Cancelled: **Python at Home : In Control**

John Pinner / Clockwork Software Systems

Once upon a time, a long time ago, I installed central heating in our home, a wet system with gas-fired boiler and a (then) state-of-the-art control system. Recently I replaced the boiler, but was disappointed to find that there was no modern equivalent to the old control system.

It didn\'t take long to realise that it shouldn\'t be impossible to create a new and improved controller using PC technology. After all, all we needed was a few relays to switch things on and off, some temperature sensors to measure what was going on, a spare PC, and some software to glue it all together.

So was born a Python-based project to control our heating system, the objective being to maximise comfort and minimise running costs. It has been both fun and satisfying putting it into practice.

The presentation will describe the control system and its development.

------------------------------------------------------------------------

#31. **Extending the life of CVS with Python**

Anthon van der Neut / Pinnacle SYstems

This talk describes how Python is used to overcome problems, and automate several administrative tasks in a multi-location, multi-project CVS and CVSup-mirroring setup, as well as a flexible build system for sources contained in these repositories.

------------------------------------------------------------------------

#34. **The State of Dabo**

Ed Leafe / The Dabo Project

Dabo is a 3-tier desktop application framework written in Python. Its database tier allows it to be used with just about any relational database backend, such as PostgreSQL, MySQL, SQLite and others. Its UI tier wraps the popular wxPython toolkit, and provides a much more consistent and Pythonic API for developing GUI applications. It also makes binding UI controls to data as simple as setting two properties of the control. Its business object middle tier provides flexibility and power in ensuring that the application data is validated against your business rules, and that business processes are kept independent of your choice of UI or database.

Since Dabo was first shown at [PyCon](PyCon) DC 2005, it has continued to be developed, and has matured significantly. The session will begin with an overview of the framework, discussing the target audience for Dabo and how the framework can help make application development much easier and much more maintainable. It will then cover several of the new developments in Dabo, such as the design tools, such as the Form Designer and the Report Designer.

There will also be a section on using the dabo.ui module independently of the rest of the framework. Over the past year, several wxPython developers have started to use Dabo\'s UI tier to develop their applications, even though they are not working with databases. This surprised us at first, but these developers have inspired us to focus on making the dabo.ui module more complete, by adding support for several non-data related controls as well as creating a drawing object framework that gives much better control of the direct drawing on the UI surface than the raw wxPython API does. So I will include a section in the talk contrasting raw wxPython with dabo.ui, showing how much simpler creating a UI app in Dabo is.

------------------------------------------------------------------------

#35. **[PyPy](PyPy) architecture session**

Holger Krekel / merlinux GmbH

Co-talker: Armin Rigo

After reaching important milestones, the [PyPy](PyPy) project is now (starting autumn 2005) heading towards building a specializing JIT-compiler, stackless features and translation to higher level languages into the code base. In this session we will present and interactively discuss with the audience the basic architectural pictures. We are going to emphasize the various emerging possibilities for further development part of which will be an ongoing effort of the European Union\'s funded part of the [PyPy](PyPy) project.

In particular, we\'ll describe the following architectural pictures and point out extension and optimization possibilities:

- Language Implementation: Bytecode Interpreter and Object Space interaction
- Translation to low level languages (C/LLVM)
- Translation to higher level languages (e.g. Squeak/Java)
- JIT-compiler architecture (very-low-level/l3 interpreter)
- Interweaving of Garbage Collection, threading and stackless operations into the translation process

------------------------------------------------------------------------

#36. **Python Can Survive In The Enterprise**

David Stanek & Mike Pirnat / AG Interactive

A commonly observed myth about the Python programming language is that \"it doesn\'t scale,\" particularly in the context of web applications. Thankfully, this is far from the truth; Python in fact provides the possibility to scale to significant enterprise levels. As evidence in Python\'s favor, we will discuss the scaling challenges and successes of AG Interactive.

AG Interactive develops and operates a family of large, high-traffic websites using Python. Our websites are focused primarily on the electronic greeting card and social self-expression industries, where it\'s essential to be available when our customers need to connect with one another. The most widely-recognizable brands in our network are [AmericanGreetings.com](http://www.americangreetings.com), [BlueMountain.com](http://www.bluemountain.com), and [Egreetings.com](http://www.egreetings.com); in addition, we provide the online greetings capabilities for such industry leaders as AOL, MSN, and Yahoo, as well as supporting numerous other partner integrations. Our websites deliver a monthly average of approximately 30 million page views, but we also encounter profound seasonal and holiday traffic spikes that can demand over 90 million page views within a 48-hour period. A typical day in our off-season is roughly equivalent to a sustained Slashdotting. Additionally, the needs of our business are constantly growing; to fulfill them, we implement and deploy hundreds of projects each year. Python allows us to accomplish this without exploding our staffing needs.

We will discuss the infrastructure that we\'ve put in place to respond to these challenges, how we have architected to scale to many sites as well as high volumes of traffic, and how Python allows it all to happen. We hope by our example to provide an inspiration for others to achieve success with Python in high-capacity, scalable solutions.

------------------------------------------------------------------------

#37. **Beyond Scripting: Using Python to create a medical information system with graphical template and database schema design**

Matthew Harriger / University of Nebraska Medical Center

Python is often described as a \"scripting language\". While python is an excellent choice for simple scripting tasks, it is also ideal for developing complex applications. The Department of Surgery at the University of Nebraska Medical Center is creating a medical information system called intuaCare using Python, wxPython and other open-source tools and libraries.

intuaCare and intuaDesign are wxPython-based applications that provide point-of-care access to patient records. intuaDesign is a graphical template/interface designer that gives users the ability to create their own data entry screens via drag-and-drop and also generates the appropriate database tables for the storage of data. The forms generated by intuaDesign are then used by intuaCare to collect and display clincal data. The data collected is stored in a local database on the device, and synchronized to a master Oracle database when a network connection is available.

This presentation will cover our reasons for selecting Python and wxPython as the platform for intuaCare, and some of the features we were able to implement using Python that would have been more difficult in other languages. A brief demonstration of intuaCare and intuaDesign will be included in the presentation.

------------------------------------------------------------------------

#38. **[PyPy](PyPy) \-- where we are now**

Michael Hudson / Heinrich-Heine-Universität Düsseldorf

Christian Tismer

[PyPy](PyPy), the notorious Python-in-Python project reached a significant milestone in the summer of 2005: being able to produce a standalone python interpreter with no dependencies on any of CPython\'s C code.

This talk will describe as much of the toolchain that got us to this point as it\'s possible to cram into 30 minutes :).

------------------------------------------------------------------------

#39. **The Rest Of The Web Stack**

Ian Bicking / Imaginary Landscape

This presentation describes the complete technology stack and methodology that has been developed at Imaginary Landscape, for the development and deployment of applications and web sites in a heterogeneous environment.

Much attention is payed to the programming portion of web application development. But successful web application development requires a lot of infrastructure and methodology beyond programming itself. This talk covers these parts of the process:

- Deploying applications.
- Keeping deployments and dependencies isolated.
- Identifying and managing the configuration of the applications.
- Handling application customizations.
- Source control.
- Customization.
- Cross-application navigation.
- Authentication across application and language boundaries.
- Integrating applications written in other languages for other environments.
- Handling static files associated with applications.

Some new tools will be presented, but the emphasis is on how to bring together a diversity of existing open source tools for a complete development process. While many of these tools will be familiar, often they are presented in terms of what you \*can\* do, not what you \*should\* do, and this talk presents a series of shoulds.

The motivation behind this toolset is the quick production and maintenance of small, decoupled applications, as well as their deployment in multiple contexts.

Some of the tools covered:

- Subversion
- Apache
- Server-side includes
- mod_auth_tkt
- SCGI
- easy_install
- Paste Deploy
- Paste Script
- buildutils

------------------------------------------------------------------------

#40. **SAM: Transforming a commandline tool to Web 3000 (c)**

Matt Harrison / [SpikeSource](./SpikeSource.html)

This presentation discusses Spike Asset Manager (SAM [http://developer.spikesource.com/wiki/index.php/Projects:sam](http://developer.spikesource.com/wiki/index.php/Projects:sam) ), the reasons python was chosen as implementation language as well the benefits python has provided.

SAM is a tool that detects open source components on a system (windows, linux, mac). By the time [PyCon](PyCon) rolls around SAM will have transformed from a relatively simple cross platform command line application to a network aware server capable of detecting other instances. IT users will be able to control all instances from either the command line or a gui (fancy AJAX provided in a web broswer because some systems may be headless).

This talk will discuss the evolution of SAM, the design decisions made and a few of the open source projects it uses (PDIS Xpath, [ElementTree](ElementTree), Path, Cheetah, json-py, [MochiKit](./MochiKit.html), [WebStack](WebStack), pyzeroconf, py2exe and more). The intended audience is python users who are interested in AJAX, Web2.0 or converting a commandline app into a web enabled app.

------------------------------------------------------------------------

#41. **Teaching Python - Anecdotes from the Field**

Vern Ceder / Canterbury School

Since 2001, Canterbury School in Ft Wayne, IN has been teaching a brief unit of Python as part of a required 9th grade Intro to Computer course. In 2004 we also added a 4 day unit of Python programming to our required 8th grade computer course. In addition, I will be presenting a tutorial on Python programming to K-12 teachers at the 2006 Indiana Computer Educators (ICE) conference, the 5th largest conference in the US aimed at K-12 technology teachers.

This presentation will deal with the issues encountered in using Python to introduce programming to non-programmers. I will assess how effective in my experience Python has been in that role, and will include samples of student code and reactions to Python from students and from the teachers attending the ICE tutorial.

------------------------------------------------------------------------

#45. **Implementation of the Python Bytecode Compiler**

Jeremy Hylton / Google

This talk describes the internals of the Python bytecode compiler. It describes the new bytecode compiler that will be released with Python 2.5.

The Python virtual machine and bytecode compiler use well-known techniques for interpreters. The aim of this talk is to document the specific use of those techniques in C Python. It is intended for developers interested in modifying or extending the language or its implementation \-- or anyone curious about language internals.

The talk covers the architecture of the compiler from parsing to bytecode generation. The high-level outline of topics covered is:

- Lexical analysis and parsing
- Abstract syntax
- Semantic analysis
- Code generation
- Execution

------------------------------------------------------------------------

#46. **Making Apples from Applesauce: The Evolution of cvs2svn**

Brian W. Fitzpatrick / Google, Inc.

While the goal of the Subversion project is to \"provide a compelling alternative to CVS\", the goal of the cvs2svn project is to enable CVS switchers to take all of their history with them to Subversion. cvs2svn started life as a short Python script that converted no CVS tags and branches, but it survived several rewrites and quickly grew to a 5000 line powerhouse. Today, cvs2svn not only converts CVS tags and branches, but it gracefully handles dozens of RCS edge cases and has been used to convert thousands of CVS repositories. This talk reviews the evolution, design, and implementation of cvs2svn and how we managed to discover things about CVS repositories that most people didn\'t think were possible.

(This has grown out of a talk I gave to [ChiPy](ChiPy) in April 2005 and a Python lightning talk I gave at OSCON EU 2005).

------------------------------------------------------------------------

#47. **agile open-source methods, businesses and EU-funding**

Beatrice Düring, /Change Maker,

Holger Krekel / Merlinux

There is a growing number of open-source developers organized and connected to company and money related work. We report our experiences from the first year of the [PyPy](PyPy) project which has a 7 company/university consortium and a 1.3 Million Euro research grant from the European Union.

We\'d like to present and discuss models and experiences for connecting open-source/hacking culture driven development to money related projects and goals with the audience.

We are going to briefly describe the organisation of the [PyPy](PyPy) project, showing how formal stakeholders and OSS Python community interact through agile practices like sprinting. We will also reflect on the aspect of diversity, combining technical and non technical people and skills and learnings from this.

We will relate the various agile techniques used in [PyPy](PyPy) and other projects/companies to the agile practices known from the work in the Agile Alliance (XP, Scrum, Crystal) in order to show how agile techniques have been adopted and evolved by the Python community.

Lastly we will also share our experience of various challenges and possibilities when integrating the different cultures and skills from the OSS perspective, EU perspective and the Chaos Pilot/process management perspective - managing diversities.

Links to background information on the talk:

- [http://codespeak.net/pypy/dist/pypy/doc/dev_method.html](http://codespeak.net/pypy/dist/pypy/doc/dev_method.html) [http://codespeak.net/pypy/dist/pypy](http://codespeak.net/pypy/dist/pypy)

------------------------------------------------------------------------

#48. **Extensible Desktop Applications: Abusing the Zope 3 Project**

Nathan R. Yergler / Creative Commons

In 2004, Creative Commons released ccPublisher 1.0, an application designed to allow users to easily tag and upload works to the Internet Archive.

ccPublisher 2, due for beta in December 2005, is nearly a complete rewrite of the orginal application. The release will add no new features, but will instead focus on providing an extensible, dynamic implementation of the original feature set. During the development of ccPublisher 2 and through conversations with individuals who wished to customize the application, it became clear that even a well architected, object-oriented implementation was too high a barrier for entry for some individuals.

Using products from the Zope 3 project, the new implementation allows users to edit straight-forward configuration files in order to \"configure\" the application with new components or features. Pieces appropriated from the Zope 3 project include the event model, interfaces, subscribers, adapters, and the ZCML engine. These pieces allow developers to create extensions and enhancements to ccPublisher without requiring complete, in depth knowledge of the application. In short, minor things are easy, major things are manageable.

The release due in December is actually the second rewrite of ccPublisher, and demonstrates the flexibility and usefulness of the Zope 3 project. The original iteration used Zope interfaces to define a strict, structured API. This design called for developers to subclass objects in order to customize the application\'s functionality, in class object-oriented style. As the implementation grew, however, it became apparent we were trading one problem for another: a massive, tightly integrated code base for a slightly-less-massive, tightly integrated code base that required a developer to know lots of details about how the system fit together.

Using events, adapters and subscribers from the Zope 3 project, the new iteration allows developers to customize areas of interest without delving into the inner workings of the entire system. For example, a developer who wishes to implement a new upload target does not need to know what metadata fields are collected; they only need to know how to handle \"Publish\" events, and know that an object impementing a particular interface is passed as the parameter. This wide-spread decoupling had the added benefit of making it easy to enable \"extensions\" to the application (i.e., post to my blog when I upload new media), as well as full-scale customizations.

The talk will dicuss how we went about designing an application that would be easily modifiable and extensible by other developers, and in the process improved the maitainability and clarity of our own code. It will also focus on using infrastructure pieces developed as part of the Zope 3 project for an application in a completely different domain (desktop v. web-based). Finally, we will provide brief coverage of challenges that have arisen during deployment. These include bundling ZCML configuration with our Python code in a [Py2Exe](Py2Exe) or [Py2App](./Py2App.html) bundle and boostrapping an application which is able to load 3rd party extensions from other developers.

------------------------------------------------------------------------

#50. **Using Django to supercharge Web development**

Adrian Holovaty / The Washington Post

This presentation will give an overview of Django, an open-source, full-stack, Python Web framework (djangoproject.com). I\'m the lead developer of Django, having built it from the ground up for the past two years.

The talk will include an overview of Django\'s architecture and philosophies, specific information on what functionality Django gives you out of the box, and basic code samples.

------------------------------------------------------------------------

#52. **New Tools for Testing Web Applications with Python**

Tres Seaver / Palladion Software

As web applications have evolved from the relative simplicity of CGI to the current \"slim client\" models, heavy with Javascript, asynchronous communication, and elaborate client-side processing, the need for increasingly powerful and sophisticated tools for testing such applications has grown as well.

This talk surveys several new Python-based tools and frameworks for testing web applications, and suggests strategies for using them to improve the quality and maintainability of web applications.

In particular, the talk will focus on Selenium, a browser-based testing framework scriptable from Python, and Funkload, a functional test driver written in Python.

------------------------------------------------------------------------

#53. **vobject - An iCalendar Library**

Jeffrey Harris / Open Source Applications Foundation

In recent years there has been an explosion of interest in standardized calendaring based on iCalendar (RFC2445). In 2004, several groups perceived a need for and independently implemented general Python iCalendar libraries. vobject sprung out of the Open Source Application Foundation\'s need for Chandler to interoperate with CalDAV servers and other calendar clients.

vobject has no dependence on any Chandler libraries, and its license diverges from Chandler and uses an Apache license instead of GPL.

vobject features parsing and serialization of iCalendar objects, including converting python standard timezone classes to and from iCalendar VTIMEZONE. It also integrates with the dateutil package to provide expansion of recurrence rules.

vobject\'s homepage is [http://vobject.skyhouseconsulting.com](http://vobject.skyhouseconsulting.com)

------------------------------------------------------------------------

#54. **Zanshin: Zen and the Art of Network Client Programming**

Grant Baillie / Open Source Applications Foundation

One of the key features of Chandler, OSAF\'s open source personal information manager (PIM), is to provide robust and interoperable sharing of data between users. The networking part of sharing leverages is a protocol library, named \"zanshin\", that heavily leverages existing python technologies such as Twisted, the event-driven networking framework. To be able to share interoperably, we have adopted established IETF standards like ICalendar, HTTP and WebDAV, as well as the emerging CalDAV standard.

The goal of this presentation and paper is to present a case study in implementing interoperable, standards-based network clients in Python. I plan to discuss some of the design and implementation trade-offs we\'ve made in Chandler, focusing mainly on the work done for sharing calendars, but touching also on other areas of personal information management, such as email.

------------------------------------------------------------------------

#55. **[IronPython](IronPython) Implementation**

Jim Hugunin / Microsoft Corporation

[IronPython](IronPython) is a fast implementation of the Python programming language targeting the EMCA standard Common Language Infrastructure (CLI). This talk will focus on the basic implementation strategies used in [IronPython](IronPython) and on several of the more interesting difficulties that were overcome. This talk is targeted at programmers working on Python implementations as well as those who are interested in more of the details of how an implementation works under the hood.

------------------------------------------------------------------------

#56. **Python tools for regional hydrologic modeling in South Florida**

Vic / Kelson

The South Florida Water Management District (SFWMD) is responsible for the operation and management of the engineered hydrologic system in south Florida. The engineered system of canals, structures, pump stations, dikes, and levees is managed in order to balance the needs for flood control, water supply, agriculture, and environmental protection. Engineers and managers at SFWMD make use of numerous computer models for analysis of the performance of the hydrologic system in response to various stresses, e.g. hurricanes or droughts. At the regional scale (several counties in size), the South Florida Water Management Model (SFWMM) has been the most-commonly used model code, and a wide variety of tools have been developed in support of SFWMM.

During the past decade, SFWMD has been developing a new, more general computational model code, called SFRSM (South Florida Regional Simulation Model). SFRSM is a finite volume code, based on an unstructured grid of triangles. It is an object-oriented design, implemented in C++ on Unix / Linux, and makes use of a variety of commonly available file formats, including NetCDF and HEC-DSS. SFRSM has two major components, HSE (Hydrologic Simulation Engine) and MSE (Management Simulation Engine). HSE is responsible for simulating the natural movement of water through overland flow, groundwater flow, and in canals and other conveyances, while MSE simulates the management decision process, using operational rules. At this time, HSE is more mature, and a calibrated HSE model of the entire regional system will be complete by the end of 2005.

The author has been involved in the development of SFRSM for 7 years, first as a member of the development team, and then as a contractor with SFWMD. This talk is focused on the work the author and others have done to develop a set of tools for use with SFRSM. They are all written in Python, and have been in development for several years. Currently, the toolkit includes a set of classes for postprocessing of model output, a graphical model visualization component, and tools for model calibration analysis, including automated calibration tools. Python is expected to become the language of choice for the future development of tools for SFRSM.

The talk will include:

1.  A brief explanation of what SFRSM does
2.  A discussion of the file formats and Python tools for handling them
3.  A discussion of the postprocessing components
4.  Some examples of the use of the toolkit

------------------------------------------------------------------------

#57. **pysense: Humanoid Robots, a Wearable System, and Python**

Dr. Charles C. Kemp (Charlie) / MIT CSAIL

Aaron Edsinger

In this talk, I will discuss the use of Python at the humanoid robotics lab at MIT CSAIL, and give a brief overview and demonstration of pysense, a collection of Python code that we will be releasing as open source prior to (or in conjunction with) [PyCon](PyCon) 2006.

At the humanoid robotics lab at MIT, Python now runs on most of our platforms. Two systems in particular fundamentally rely on Python, Domo a humanoid robot ( [http://people.csail.mit.edu/edsinger/domo.htm](http://people.csail.mit.edu/edsinger/domo.htm) ) and Duo ( [http://people.csail.mit.edu/cckemp/](http://people.csail.mit.edu/cckemp/) ) a wearable system. In spite of the real-time constraints of robot perception and control, we have found that Python can play an important role in most aspects of our research through pure Python and SWIG wrapped C++ modules.

Both platforms use a common Python code base named pysense for visualization, perception, and annotation. We are currently preparing to officially release this software as open source (svn access is now granted by request). Pysense consists of an efficient OpenGL based display for 3D information and video; image iterators for capturing from a variety of cameras in Linux; real-time computer vision algorithms including methods for motion processing, segmentation, and object detection; and tools for browsing and annotating video databases for machine learning.

------------------------------------------------------------------------

#58. **Introduction to Zope Application Development**

Paul Winkler / Revolution Health Group

This talk distills into tutorial form the fundamentals of application development for the Zope platform, with some best practices and practical advice along the way. It aims for the oft-noted gap between the online Zope Book (which covers only through-the-web development) and the Zope Developers\' Guide (which is a reference, not a tutorial).

In an attempt to be forward-looking, the talk will use Zope 3 / Five features in preference to Zope 2 features whenever possible and appropriate for the novice Zope developer. Five is a moving target, and this aspect of the talk will be evolving with the state of the art.

Requirements:

- Familiarity with object-oriented programming in Python
- Familiarity with HTML

I have uploaded the talk slides here: [http://slinkp.com/\~paul/pycon_2006/z2/notes.html](http://slinkp.com/~paul/pycon_2006/z2/notes.html)

------------------------------------------------------------------------

#59. CANCELLED: **Introduction to CMF Application Development**

Paul Winkler / Revolution Health Group Prerequisite: My \"Intro To Zope Application Development\" talk, or equivalent Zope development experience.

This tutorial covers the fundamentals of developing or extending content management applications using the Zope CMF framework, leveraging some of the Zope 3 features that are available today via the Five integration layer.

Why discuss vanilla CMF when all the press goes to Plone and CPS? It is very useful to gain a basic bottom-up understanding of Plone and CPS. CMF technology is the foundation, and everything in this talk applies equally to Plone and CPS. Additionally, for some projects Plone or CPS may be too heavyweight and it may be desirable to start with a smaller base.

------------------------------------------------------------------------

#60. CANCELLED: **Mission-Critical Python and the Brave New Web**

Ivan Krstic / Harvard University (presently Zagreb Children\'s Hospital)

Zagreb Children\'s Hospital is the largest children\'s hospital in Croatia. In the summer of 2002, the Hospital\'s cardiology ward started an effort to create a next-generation electronic medical record application to replace an antiquated, and increasingly unreliable, COBOL mainframe solution. The new application, implemented in Perl, ran flawlessly for two years; inspired by its success, the Hospital decided to move all of its core systems to open source, and write a large web application to interface with most aspects of standard hospital operation.

We found Perl was no longer a good fit for a project of this scope, and turned to Python after carefully evaluating our options. Given the extreme software demands of a hospital environment, we decided against using existing solutions, and wrote our own application engine called Radian. The engine pre-dates the now wildly popular Ruby on Rails framework, but features a similarly strong emphasis on agile development. The Radian core, however, comes with unmatched security features, and specialized performance and scalability layers that incorporate lessons learned from building solutions that scale to millions of users, hundreds of servers, and many hundreds of gigabytes of database data.

We\'ll talk about our experiences with Python as a language for truly mission-critical deployments. Radian is being released as free software, and will make its public debut in this talk \-- we\'ll also explain why many present solutions aren\'t well-suited to extreme-demand environments. Finally, we\'ll show how Radian addresses these problems, and give a quick tour of the functionality that sets it apart from similar systems, which will be of interest both to application developers looking to rapidly build extremely scalable and secure Python applications, and to developers of existing Python web frameworks looking to improve support for such applications in their own products.

------------------------------------------------------------------------

#62. **Docutils Developers Tutorial: Architecture, Extending, and Embedding**

- David Goodger / CDP Capital Felix Wiemann

A very quick overview of the [Docutils](http://docutils.sf.net) architecture, followed by examples of using Docutils in applications, extending Docutils with new plug-ins, languages, and Writers, and extending [reStructuredText](http://docutils.sf.net/rst.html) with directives and interpreted text roles. Finally, we will create and test a new directive, live!

Related talks: [\"Easy Slide Shows With reStructuredText & S5\"](./PyCon2006(2f)Talks.html#A64) and [\"What is Nabu?\"](./PyCon2006(2f)Talks.html#A24) both describe applications of Docutils.

There will also be a [Docutils sprint](./PyCon2006(2f)Sprints(2f)DocutilsSprint.html) following the conference, where you can put your new knowledge into practise!

------------------------------------------------------------------------

#63. **Django tutorial**

Jacob Kaplan-Moss / World Online

Django is a high-level web development framework for rapid development of database-backed web sites and applications. This tutorial will introduce Django, explain a few of the philosophies behind it, and walk through the steps involved in quickly building a full-featured web site/application with Django.

------------------------------------------------------------------------

#64. **Easy Slide Shows With reStructuredText & S5**

David Goodger / CDP Capital

A quick how-to/tutorial: writing slide shows using [reStructuredText](http://docutils.sf.net/rst.html) and [S5](http://meyerweb.com/eric/tools/s5/), Eric Meyer\'s \"Simple Standards-based Slide Show System\". The generated presentation is HTML, and can be viewed using any OS and any modern web browser that supports CSS, [JavaScript](./JavaScript.html), and XHTML. We will cover installing Docutils, writing the presentation text, generating the slides, tweaking the stylesheets, and setting up the browser for projecting the slides.

Related talks: [\"Docutils Developers Tutorial: Architecture, Extending, and Embedding\"](./PyCon2006(2f)Talks.html#A62) is for those interested in the implementation details of Docutils. [\"What is Nabu?\"](./PyCon2006(2f)Talks.html#A24) describes another application of Docutils.

There will also be a [Docutils sprint](./PyCon2006(2f)Sprints(2f)DocutilsSprint.html) following the conference. Come help make Docutils better!

------------------------------------------------------------------------

#65. **Understanding Unicode**

David Goodger / CDP Capital

A practical A-Z of Unicode for beginners & intermediate programmers. By the end of this tutorial, attendees will no longer fear the unknown, but will get past the terminology, realize Unicode\'s inherent simplicity, and be able to effectively wield this essential tool for internationalization.

------------------------------------------------------------------------

#66. **Building Pluggable Software with Eggs**

Ian Bicking / Imaginary Landscape

People have been building pluggable software in Python for some time, but the result is often difficult to manage and eclectic \-- both within and between projects.

Python Eggs \-- a new packaging system built on distutils \-- provide packages with a more formalized metadata structure, versioning, and other useful features. Several of these features, put together, produce a fairly complete process for pluggability. Eggs are being used for plugins in several systems, including setuptools itself, Paste, and Trac.

Best practice for using these tools is still being developed. This presentation will focus on the current understanding of how to best put pieces together, for both flexibility and transparency.

This presentation will focus on the concrete steps to making an application for framework extensible and pluggable using eggs, and point out both pitfalls and opportunities.

This presentation will cover:

- What Python Eggs are
- Relation to setuptools and easy_install
- Implicit and explicit loading of eggs, including version specifications and dependencies
- Programmatically finding and installing eggs
- entry_points \-- named and categorized routines that your package provides
- Finding other metadata associated with a package

------------------------------------------------------------------------

#67. **Gamma: An Atom Publishing Protocol implementation for Zope 3**

Michael Bernstein / Agile Mind

Gamma is a general-purpose Zope 3 implementation of the Atom Publishing Protocol initially targeted at weblog-like applications, but useful as a standards-based repository for many other types of applications as well. In this presentation, I will describe the implementation and demonstrate using it to add a standard API to content-management-like applications, as well as extending it with domain specific functionality.

------------------------------------------------------------------------

#69. **Python in Your Pocket: Python for Series 60**

Matt Croydon

Python for Series 60 has come a long way since it was released last winter. This session will provide an overview of Python on mobile phones, demonstrate how easy it is to develop applications with a native look and feel, explore the many aspects of a phone that can be controlled programmatically and showcase several applications written in Python.

------------------------------------------------------------------------

#70. **Simplifying Red-Black Trees**

J Adrian Zimmer / OSSM

Ordered binary trees can enable efficient lookup of ordered data. Starting at the root, an algorithm decides whether the desired value has been found or will appear in the left or right subtree. The lookup algorithm proceeds recursively down the tree until it is finds what it wants or is directed to an empty subtree.

Lookup is efficient if the tree is short and fat. Keeping the tree short and fat when doing insertions and deletions is not particularly easy \-- if it is to be done efficiently. The red-black tree is one model used to guide this process. Like others it uses a methods of morphing a tree called \"rebalancing\". Rebalancing involve numerous cases with plenty of symmetry.

This presentation is essentially a case study in one way Python can handle symmetry. The aspect of Python which is most useful to us is its handling of functions as first class objects.

When walking a tree, we want to alter our thinking about nodes. We start thinking about a node as having a left and a right child. After we have walked a node, it has a walked and an unwalked child. We also want to change the way our parent thinks about its children \-- not \"consciously\" but in terms of how that parent would take part in a rotation. In object-oriented terms, we want to change at least one of the parent\'s methods.

A complete implementation of red-black tree lookup, insertion, and deletion, will be the basis of this presentation. As the title indicates, the implementation emphasizes readability over efficiency but that does not mean it is inefficient. Additional storage is needed only for nodes between the the \"current\" node and the root. The algorithm does a few more things as it process nodes during a search but not many.

The breakdown of cases need not be different here than for published versions, but it is. Partly this is because the need to distinguish left from right when rebalancing is gone. This means we can remove some subcases based on going different directions in the past two stags. Partly the different case breakdown results from the author\'s continuing search for a case breakdown that makes beautiful intuitive sense. Whether he is any closer to that goal than what is already published is likely to be a matter of taste.

------------------------------------------------------------------------

#71. **entransit, a content delivery system**

Examines a system be able to marshall changesets from a client to a server application. the server application in turns applies the content to a set of operations which results in:

- \- xml representation of content on the filesystem - rdmbs indexes of content for ease of querying - rdf xml file that describes relationships between xml filesystem contnet - abiltiy to apply business logic e.g. URIRewriting and Indexing, for instance with Xapian.

We will demonstrate the usage and internals of the system with the Plone/Zope CMS which will deploy to a separate environment where zope 3 will display and search the information. Zope 3 will be running WITHOUT the ZODB. Finally we will release the pre-canned frontends that can use the default configuration of entransit for the following environments: PHP, .NET, Java and mod_python.

------------------------------------------------------------------------

#72. **bazaar-ng distributed version control**

Martin Pool / Canonical

bazaar-ng is a friendly open-source distributed version control system written in Python. The lead developer of bazaar-ng will explain bazaar-ng, the problems it solves, and why it\'s interesting to Python developers.

Agenda

- branch visualization
- brief demo/tutorial
- overview of model
- how we use bazaar-ng to build Ubuntu and launchpad
- some interesting version control algorithms (if time permits)

Martin Pool is the lead developer of bazaar-ng, and an employee of Canonical, the corporate parent of Ubuntu. He has given popular talks on distcc, rsync and bazaar-ng at linux.conf.au and other conferences.

More information:

- [http://bazaar-ng.org/](http://bazaar-ng.org/)

------------------------------------------------------------------------

#73. **State of Zope**

Jim Fulton / Zope Corporation

A 45-minute talk about the current state of Zope development and what\'s planned for the next year.

------------------------------------------------------------------------

#74. **The Origins of Python**

Guido van Rossum / Google

In this talk I will go back to the origins of Python. I\'ll discuss the ABC language, Python\'s precursor by a decade, and how its best and worst features affected Python. I\'ll also reveal what I stole from other languages. I\'ll even admit to some early design mistakes.

(This talk will be held during lunchtime on Friday, in the Ballroom.)

------------------------------------------------------------------------

[CategoryPyCon2006](CategoryPyCon2006)
