# PyCon2007/Talks

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

2\. Python inside Imageworks Peter Shinners (Sony Pictures Imageworks) 30min Intermediate (audio and materials) categories: case study, animation A look at the deployment and usage of Python for feature films inside of Sony Pictures Imageworks.

3\. Test Automation for a Complex System: Technology and Social Aspects David Hancock (ARINC); Mrs. Anita L. Ewing; Karen Mishler (ARINC) 30min Beginner (audio and materials) categories: case study, testing Our team got enthusiastic about changing its test approach after [PyCon](PyCon) 2006. Even with excellent consulting assistance and lots of motivation, it wasn\'t easy. Ours is a large and complex system for aviation support, with many external interfaces, and the sharpened focus on test tools and approaches has begun to pay off for us.

4\. Pybots: Testing Python Projects in Real Time Grig Gheorghiu 30min Beginner (audio and materials) categories: testing, community The goal of the Pybots project (www.pybots.org) is to allow people to run automated tests for their Python projects \"in real time\". Testing is done every time a commit is made to the Python\'s subversion repository (trunk and 2.5 branch currently), with Python binaries built from the latest source.

I will talk about the setup of the Pybots buildbot farm, about the issues that the Pybots farm has helped uncover, and also about lessons learned in building, sustaining and growing an open-source community project.

5\. twill, scotch, and figleaf \-- tools for testing Dr. C. Titus Brown (Caltech) 30min Intermediate (audio and materials) categories: testing, web twill, scotch, and figleaf are recent additions to the suite of Python-based testing tools. twill is a simple Web-scripting framework based on mechanize that lets users automate Web browsing with a simple language; scotch is a WSGI proxy server & Web traffic recorder that lets users record and replay raw WSGI/HTTP traffic and translate it into twill script; and figleaf is a code coverage recorder and analyzer that is aimed at integration with large projects where coverage.py may be less suitable. I\'ll briefly discuss the genesis of the tools and their architecture, and I\'ll spend most of the time demonstrating how to combine these tools with others in order to build automated tests for Python projects.

Outline:

1\. introduction to using twill for functional web testing 2. introduction to using scotch/WSGI for web recording and playback 3. introduction to using figleaf for code coverage analysis 4. automating functional web testing in a unit test framework 5. using code coverage with unit testing to target new tests 6. instrumenting remote web sites for code coverage 7. integrating web testing with development, a demonstration 8. demonstration: automated testing of a django demo site 9. demonstration: automated testing of a cherrypy demo site 10. demonstration: automated testing of trac

6\. Developing with [IronPython](IronPython) and Windows Forms Mr. Michael J Foord; Mr. Andrzej Krzywda 30min Intermediate (audio and materials) categories: gui, dotnet An introduction to developing with [IronPython](IronPython) and Windows Forms.

It will include :

\* What is [IronPython](IronPython) \* Why use [IronPython](IronPython) (and when not to use it) \* What is Windows Forms \* Examples of using Windows Forms (quickly show off the API and the way

- to access it from [IronPython](IronPython))

\* Problems developing with [IronPython](IronPython) and differences from CPython \* Integration with C#: Extending [IronPython](IronPython), using third-party components

- and .NET classes, the [IronPython](IronPython) engine (integrating [IronPython](IronPython) into C# applications)

I \*aim\* to tailor some of the examples to show their equivalent form in Python for .NET, which can access .NET classes from a modified version of CPython.

7\. The State of Python Advocacy Jeff Rush 30min Beginner (audio and materials) categories: advocacy, community To present, as Advocacy Coordinator, the progress made in encouraging the use of Python, the tools and resources that are available and to seek input from the community on what needs to be done.

12\. The Star Schema in Python - Analysis and Reporting without Overheads Steven Lott (CTG) 30min Intermediate (audio and materials) categories: databases Data warehousing provides some powerful tools and techniques for doing data analysis and reporting. Specifically, the star-schema (or dimensional) data model gives us a design pattern that supports flexible \"slice and dice\" reporting. This technique is sometimes misunderstood, making it underutilized. This paper will present the essence of the dimensional model, implemented in Python.

13\. Developing Desktop Applications with Dabo Mr. Edward Leafe 45min Intermediate (audio and materials) categories: databases, gui Dabo is a 3-tier framework designed to help developers create desktop database applications in Python. This session will focus on using the various visual tools available in Dabo to create powerful rich-client applications.

16\. Python In Open Pit Mining Operations Mr. Carl B. Trachte (Phelps Dodge Morenci, Inc.) 30min Beginner (audio and materials) categories: case study, engineering Several (3 to 5, 5 to 10 minutes each) examples of Python scripts applied to open pit mining applications. Each example will include a description of the engineering problem, what the script accomplished (economically and operationally), and exerpts from the script\'s code showing the methodology and rationale used.

17\. Topographica: Python used for Computational Neuroscience Mr. Judah B De Paula (University of Texas, Austin) 30min Beginner (audio and materials) categories: science A review of a Python application used by Computational Neuroscientists to model brain cortex.

The Topographica simulator ([http://topographica.org](http://topographica.org)) is an open source project written in Python that is actively used by computational neuroscientists to simulate the mammalian brain. The unique properties of Python allows for the rapid prototyping of visual cortex models while simultaneously providing enough speed to run the memory-intensive linear-algebra based simulations.

Developed by the University of Edinburgh and by the University of Texas at Austin, Topographica focuses on the large-scale structure and function of neurons that are visible only when many thousands of such neurons are connected into topographic maps containing millions of connections. By using the simulator, computational neuroscientists make predictions about the structure of living tissue.

As a previous developer for Topographica, I will discuss the implementation of the application as well as the open source components also used by the system. In particular, what made Python the language of choice (syntax, flexibility, GUI) and what else was needed (Weave, Numeric, [PyLab](./PyLab.html)).

19\. Writing Parsers and Compilers with PLY David M Beazley 45min Intermediate (audio and materials) categories: parsing PLY (Python Lex-Yacc) is a 100% Python implementation of the lex/yacc toolset for Python. PLY is similar to other Python parsing efforts in that it uses a number of advanced Python features such as introspection to simplify parser construction. Moreover, PLY provides virtually almost all of the functionality found in traditional yex/yacc tools including LALR(1) parsing, good performance, extensive error checking, and useful diagnostics. This talk will provide an overview of PLY and focus on its more interesting and unusual features. In addition, I will describe some of my experiences using PLY to implement compilers, including my recollections of teaching a graduate compilers course in which students created a fully-functional compiler in Python.

20\. Becoming an Open Source Developer: Lessons from the Django Project Jacob Kaplan-Moss 30min Beginner (audio and materials) categories: case study, django It almost seems like a joke: a family-owned newspaper in Lawrence, KS (population 80,000) releases an open-source web framework. It\'s not a joke, of course: today Django is an increasingly popular web development platform. As an open-source community Django has been incredibly successful; in Tim O\'Reilly\'s OSCON keynote, he called Django \"the new face of open source.\"

But it\'s often unclear how we got here. How did a couple of programmers at a newspaper convince management to contribute to the open-source ecosystem? How does the company justify the time its developers spend on open source? And how have we as individuals and as a business had to adapt to become better open source developers?

In this session: ten lessons in becoming an open source developer from the Django project.

21\. Testing Tools Panel Grig Gheorghiu 45min Beginner (audio and materials) categories: panel, testing I maintain a \"Python Testing Tools Taxonomy\" Wiki page at

- \<[http://pycheesecake.org/wiki/PythonTestingToolsTaxonomy\>](http://pycheesecake.org/wiki/PythonTestingToolsTaxonomy%3E).

A panel where authors of some of these tools would discuss and take questions on topics such as:

- what need prompted the creation of the testing tool
- what type of testing does the tool belong to
  - (unit, functional, acceptance, system, performance)
- what specific features does the tool offer that other tools lack
- what are the most common testing scenarios you have seen
  - in your user base
- are there any OS/platform specific gotchas related to the tool
- how extensible is the tool (plugins etc.)
- how easy to learn is the tool
- how well tested is the tool
- how well documented is the tool
- others

Details and Questions: [http://us.pycon.org/TX2007/TestingToolsPanel](http://us.pycon.org/TX2007/TestingToolsPanel)

25\. The Absolute Minimum an Open Source Developer Must Know About Intellectual Property Van Lindberg 30min Beginner (audio and materials) categories: legal However you feel about intellectual property laws, they are an important feature of today\'s technology landscape. This talk will give a brief introduction to the three main areas of intellectual property law - patents, copyrights, and trademarks - with an emphasis on principles that will help keep individuals and businesses out of trouble when developing or using open source software.

Topics covered will include:

- \- A brief glossary - Defining patents, copyrights, and trademarks - Who owns my code? Who owns my idea? - Intellectual property assignment and
  - your employer

  \- Licensing, using, and distributing software - The GPL, BSD, and Python licenses

27\. Distributing your project with Python Eggs Dr. Stephen PAscoe (British Atmospheric Data Centre) 30min Intermediate (audio and materials) categories: packaging, eggs Python Eggs is an exciting technology that has the potential to revolutionise the way python projects are developed, distributed and installed. In some parts of the python community the revolution has already happened. This talk will cover how project authors and maintainers ensure that their code takes full advantage of what Eggs have to offer.

Make your project downloadable and installable in a single command; seemlessly handle dependencies on other projects; make managing revisions easier and much more.

29\. Introduction to Zope 3 - The Component Architecture Mr. Paul Carduner 30min Intermediate (audio and materials) categories: web, zope Learning the basics of the Zope 3 component architecture: interfaces, adapters, and registries.

31\. The Wonderful World of Widgets for the Web Kevin Dangoor 30min Intermediate (audio and materials) categories: web, turbogears Tosca Widgets handle form display and validation of the input with great customizability, and can even include [JavaScript](./JavaScript.html) and CSS for great user interfaces. Origionally implemented as part of the [TurboGears](TurboGears) framework, Tosca Widgets are easy to use, easy to make and have been re-implemented to work with any python web framework. Check out this introduction to Tosca Widgets ([http://toscawidgets.org/](http://toscawidgets.org/)).

32\. pyweek: making games in 7 days Alejandro J Cura (Python Argentina); Lucio Torre (Python Argentina) 30min Intermediate (audio and materials) categories: games, agile The objective of this talk is to encourage people to participate in pyweek. We explain what the contest is, when it takes place, who can and does participate and why everybody should. A quick review of the most unique games is given, plus an account of the fun experience we had developing our entries. We also talk about how python is the perfect match for this kind of tight schedules, and about what the contest brings back into the python community.

33\. A Program Transformation Tool for Python 3000 Jeremy Hylton 30min Advanced (audio and materials) categories: parsing, ast Python 3000 will not run some existing Python programs, primarily because many deprecated language features will be dropped. This paper describes a tool for automatically updating existing Python programs to run on Python 3000. The tool combines describes transformations at the level of abstract syntax. It also decorates the abstract syntax tree with information about raw tokens, preserving existing formatting in most cases.

34\. Python and wxPython for Experimental Economics Dr. Theodore L. Turocy (Texas A&M University) 30min Intermediate (audio and materials) categories: science, gui The Economic Research Laboratory at Texas A&M University has begun using Python and wxPython to develop software to implement laboratory experiments in economics. This talk outlines why this combination has been so successful for the specific requirements of laboratory economics in general, and illustrate specifically how the code for one specific experiment is evolving into a framework of reusable components.

36\. Web Frameworks Panel Dr. C. Titus Brown (Caltech) 45min Intermediate (audio and materials) categories: panel, web Frameworks:

- Zope (Jim Fulton)

- [CherryPy](CherryPy) (Robert Brewer)

- [TurboGears](TurboGears) (Kevin Dangoor?)

- Django (Adrian Holovarty?)

- Pylons (Ben Bangert)

- Quixote (Neil?)

- Twisted web (?)

- web.py (Aaron Swartz?)

I\'ll have a chat server or a Web site where people can ask followup questions, if the Internet connectivity is sufficient (it wasn\'t, last year!) Otherwise, I\'ll open the floor up to questions towards the end.

See [http://us.pycon.org/TX2007/WebFrameworksPanel](http://us.pycon.org/TX2007/WebFrameworksPanel) for more information. 38. Python, Unicode, and Internationalization Mr. Patrick G Smith (University of Toronto) 30min Intermediate (audio and materials) categories: language, technique As Python is used more and more throughout the world, internationalization of Python programs is becoming increasingly more important. This talk discusses what Unicode is, how Python natively supports Unicode, and examines a case study of the internationalization and localization of a Python application.

39\. Studying Internet Censorship: a Python case study Michelle Levesque 45min Intermediate (audio and materials) categories: case study In an increasing number of countries, significant portions of the web are being blocked from public access, from pornography to human rights sites. Studying what is being blocked and how the filtering occurs is a complex cat-and-mouse game involving rapidly changing requirements and restrictions. This presentation will examine how Python is providing the researchers with an advantage and demonstrate an example of Python being used to do some good in the world.

40\. Embedding Little Languages in Python Dan Milstein 30min Intermediate (audio and materials) categories: technique Python offers excellent support for creating Domain-Specific Languages and embedding them in your programs. This talk will explore python DSL\'s by developing several detailed examples of little languages for specific problem domains: testing web-facing servlet code; generating and processing HTML forms; sending email notifications in a workflow system. The focus will be on looking for ways to turn a complex, imperative program into a simpler, largely declarative specification.

41\. Securing Python: \"Protecting the interpreter from code wielding fresh fruit.\" Brett Cannon 30min Intermediate (audio and materials) categories: security, core Python currently has no security model. This talk discusses why this is and how I am fixing the problem. 42. Python-Dev Panel : \"We make the things that make Python work.\" Brett Cannon 45min Beginner (audio and materials) categories: panel, core A discussion panel consisting of members of the Python development team answering any and all questions tossed at them (in a hopefully cogent manner).

45\. Writing a Python Extension module in C++ using Swig Monty Taylor (MySQL) 30min Advanced (audio and materials) categories: extensions We will step through a fully functional example of how to write, build and use an extension module in C++ using swig. A portion of the NDB/Python bindings will be used as example source code, although they will not be the focus of the talk.

46\. Packaging Python apps for Linux Distributions Monty Taylor (MySQL) 45min Intermediate (audio and materials) categories: packaging An overview of packaging Python libraries and tools for the major distributions. We will cover use of setuptools and eggs, and how those interact with deb and RPM packages. Attention will be given to recent Debian decisions such as the use of python-central, as well as strategies for packaging for multiple distros.

47\. SQLAlchemy \-- the Front-to-Back database toolkit Mr. Mark R Ramm-Christensen 45min Intermediate (audio and materials) categories: databases SQLAlchemy ([http://www.sqlalchemy.org](http://www.sqlalchemy.org)) isn\'t just a ORM, it\'s a next generation, full-stack SQL Toolkit. The talk explores how to use SQLAlchemy to perform all kinds of database acrobatics at various levels.

49\. Iterators in Action Jim Baker 30min Intermediate (audio and materials) categories: language, technique Using iterators well can make your code lean and your programming fun. We will distill current best practice by investigating some (mostly) useful examples of iterators in action.

50\. Interactive Parallel and Distributed Computing with IPython Dr. Brian E Granger (Tech-X Corporation); Fernando Perez (University of Colorado at Boulder) 30min Intermediate (audio and materials) categories: science, concurrency One of Python\'s strengths is that it can be used interactively. In this talk I will describe recent developments in the IPython project ([http://ipython.scipy.org](http://ipython.scipy.org)) that extend Python\'s and IPython\'s interactive capabilites into the realm of parallel and distributed computing.

The architecture we have developed allows parallel and distributed applications to be developed, debugged, tested, executed and monitored in a fully interactive manner.

Many styles of parallelism and concurrency are supported including traditional message passing (using MPI), task farming, shared memory and custom approaches as well. This flexibility makes it easy to incorporate existing parallel codes and libraries as well as quickly design novel parallel approaches and algorithms.

I will talk about the design and implementation of the architecture, detail its basic usage and provide examples of more sophisticated usage scenarios. 51. Why and when to use ctypes? Mr. Mike C Fletcher (VRPlumber Consulting Inc.) 30min Intermediate (audio and materials) categories: extensions Experiences in wrapping a large set of C APIs using the ctypes Foreign Function Interface are presented to provide guidance to other developers considering using the technology for their own projects. 52. Understanding and Using [NumPy](NumPy) Dr. Travis E Oliphant (Brigham Young University) 45min Beginner (audio and materials) categories: science [NumPy](NumPy) is the next-generation array object that inherits from the Numeric code-base and incorporates the features of Numarray. Its purpose is to effectively combine the two array objects into one. This talk will summarize the history of array objects for Python and describe [NumPy](NumPy) and how to use it, including some of its new features. More information is available at [http://numpy.scipy.org](http://numpy.scipy.org) 55. Towards and Beyond [PyPy](PyPy) 1.0 Mr. Michael Hudson (Heinrich-Heine Universität Düsseldorf) 45min Intermediate (audio and materials) categories: implementations I will describe [PyPy](PyPy), the implementation of Python in Python, focussing on the new features implemented since the last [PyCon](PyCon) and the progress made towards a release we will be happy to call \"1.0\", and maybe speculate a little on what the future holds. 56. Using Python Eggs Dr. Stephen PAscoe (British Atmospheric Data Centre) 30min Beginner (audio and materials) categories: packaging, eggs This, first in a series of 2 talks on Python Eggs will, demonstrate how Eggs can completely change the way you install python software. After mastering the basics of the easy_install command you need never hesitate in \"trying out\" new packages again. The talk will also provide a taster for advanced features covered in the remaining talks and take you on a tour of the python cheeseshop ([http://cheeseshop.python.org](http://cheeseshop.python.org)).

57\. State of Zope Panel Jim Fulton (Zope Corporation) 30min Beginner (audio and materials) categories: web, zope This has been a big year for Zope. The Zope Foundation was formed. Zope 3 technology continued to mature and have a greater impact on Zope 2. Python technologies, like WSGI and Python eggs are making it easier for Zope to be used with other Python web frameworks.

This panel will provide a number of perspectives on the events of the past year and on plans for the coming year. the next year from a number of perspectives.

58\. Testable network programming via the Network Gateway Interface Jim Fulton (Zope Corporation) 30min Intermediate (audio and materials) categories: testing, network The Network Gateway Interface (NGI) allows tests for network applications to be written much more easily by separating application code from low-level network calls. Tests need not create network connections, threads, or processes. This talk will present the NGI and discuss it\'s strengths, limitations, and current status. A small NGI application used in production at Zope Corporation will be presented in detail to illustrate the NGI\'s use and benefits.

59\. Creating games with Pygame on the GP2X Mr. Frank K Wilder 30min Beginner (audio and materials) categories: games, handheld This talk will be about the challenges and opportunities of game development on the GP2X (an open-source, Linux-based handheld video game console) using Pygame.

60\. IPython: getting the most out of working interactively in Python Dr. Brian E Granger (Tech-X Corporation); Fernando Perez (University of Colorado at Boulder) 30min Beginner (audio and materials) categories: ide, gui, shell IPython ([http://ipython.scipy.org](http://ipython.scipy.org)) is an enhanced interactive shell for Python. It provides a large number of features not found in the default shell that make interactive work in Python more seamless and convenient.

These features include: full access to the OS, sophisticated tab-completion and object introspection, and easy access to debugging and profiling tools. All of these features are customizable by the user. It also offers support for interactively working with all major GUI toolkits from the command line.

This talk will outline the basic ideas and major features behind IPython and demo some of them directly.

61\. Easy Creation of Interactive Tutorials Dr. Andre Roberge 30min Intermediate (audio and materials) categories: education, tutorial, web In this talk, I will illustrate how a Python program (crunchy.sourceforge.net) can be used to transform easily static html-based tutorials into interactive sessions. Two types of interactive tutorials will demonstrated: those that teach about learning to program in Python, and those that teach about using a given module. 63. Creating the [WhatWhat](./WhatWhat.html) Project with [TurboGears](TurboGears) Jonathan [LaCour](./LaCour.html) 30min Intermediate (audio and materials) categories: web, turbogears, project [WhatWhat](./WhatWhat.html) Status ([http://cleverdevil.org/whatwhat](http://cleverdevil.org/whatwhat)) is a simple approach to project status tracking. It was developed at Optio Software to fill a real need, and is used there on a day-to-day basis. [WhatWhat](./WhatWhat.html) is built on top of the fantastic [TurboGears](TurboGears) web framework in the Python Programming Language. In 2006, Optio decided to release [WhatWhat](./WhatWhat.html) as an open source project.

This talk will review the functionality of the [WhatWhat](./WhatWhat.html) project, and how [TurboGears](TurboGears) made it possible to create [WhatWhat](./WhatWhat.html) in a matter of weeks, exploring every layer of the application\'s MVC (model-view-controller) stack.

64\. How I Wrote a Python App and Got \$5 Million Mr. Mark R Hinkle; Erik A Dahl; Shaun Howard 30min Intermediate (audio and materials) categories: case study, zope, twisted Zenoss CTO Erik Dahl, will discuss how he developed his Python-powered commercial open source monitoring tool and specifically why he chose Python over other technologies. 66. WSGI: An Introduction Mr. Ian S Bicking (The Open Planning Project) 45min Intermediate (audio and materials) categories: web WSGI is the Web Server Gateway Interface, a Python standard for representing HTTP requests. WSGI provides a flexible, cross-framework, and very stable way to combine web-related code. The kind of code that can be integrated includes web applications, servers, app servers like Zope, authentication systems, styling, debugging tools, and more. Especially the last year has seen an increase in WSGI-based components for a variety of tasks.

This talk will introduce the basic technical concepts of WSGI, and then discuss the architectural options available in a WSGI stack and how you can use the basic techniques and extensibility of WSGI to add functionality to a stack.

67\. Good-bye Hello World: Rethinking Teaching with Python Dr. Vern Ceder (Canterbury School) 30min Beginner (audio and materials) categories: education, k-12 In spite of introducing all of our high school students to programming with Python, interest in our programming classes was flat. A survey revealed that 95% of our students hated the Python programming unit. Some experimentation lead to throwing out some dearly held beliefs about what a first exposure to programming (and Python) should be, and student attitudes toward the programming unit have dramatically changed.

69\. Python on Parrot \-- under the hood Dr. Patrick R. Michaud 45min Intermediate (audio and materials) categories: implementations Parrot is a virtual machine environment that is being developed to support dynamic languages such as Perl, Python, Ruby, [JavaScript](./JavaScript.html), and many others. This talk provides a detailed description of the architecture of Parrot, its compiler tools, and the implementation of a Python compiler for Parrot.

70\. Accessing and serving scientific datasets with Python Roberto De Almeida 30min Intermediate (audio and materials) categories: databases, science The Data Access Protocol (DAP) is a HTTP-based data transmission protocol designed specifically for science data and widely used in the oceanography, meteorology and climate communities. The DAP is currently used by several institutions to serve hundreds of scientific datasets that can be remotely accessed by different clients, in a transparent and efficient manner regardless of storage format.

Pydap ([http://pydap.org](http://pydap.org)) is a pure Python implementation of the DAP, written from scratch. Pydap can be used as a DAP client to inspect an retrieve data from any DAP served dataset. This way, remote datasets can be introspected by the client before any data is retrieved, allowing the user to download only the desired variables and for the area and period of interest.

The module also implements an extensible DAP server as a WSGI application ([http://www.python.org/dev/peps/pep-0333/](http://www.python.org/dev/peps/pep-0333/)). The server supports different data formats (netCDF, CSV and Matlab files and SQL databases) through a simple plugin interface based on setuptools\' entry points, and can be easily deployed using Python Paste ([http://pythonpaste.org](http://pythonpaste.org)). 72. SQLSoup Jonathan Ellis 30min Intermediate (audio and materials) categories: databases SQLSoup is a SQLAlchemy extension that exposes much of the power of SQLAlchemy with a minimal learning curve and a very close correlation with SQL constructs.

76\. Using Stackless Andrew Dalke (Dalke Scientific Software) 45min Intermediate (audio and materials) categories: concurrency Stackless: What is it, how to use it, and why.

Stackless Python is modified version of CPython with support for tasklets; also called microthreads, fibers or green threads. Tasklets are an additional way to implement multithreading but with much lower overhead than system threads. They take fewer system resources so a Stackless environment may have tens of thousands of active tasklets instead of at most a few hundred threads. Context switching and inter-tasklet communication via \"channels\" are fast, making Stackless a useful platform for developing dense multitasking systems. The best known example is the game EVE Online with 30,000+ simultaneous users in the same environment. 77. [IronPython](IronPython): Present and futures Mr. Jim Hugunin (Microsoft) 45min Intermediate (audio and materials) categories: implementations [IronPython](IronPython) ([http://codeplex.com/ironpython](http://codeplex.com/ironpython)) is an implementation of the Python language targeting the Common Language Runtime. [IronPython](IronPython) has excellent performance, seamless integration with the .NET platform and very high compatibility with the standard Python implementation. The first public talk on [IronPython](IronPython) was at [PyCon](PyCon) 2004, three years ago. Since then, [IronPython](IronPython) has progressed from a rough prototype to a 1.0 release with a vibrant user community. This talk will present the present state and future directions of this Python implementation.

78\. soaplib: an easy-to-use python soap library Aaron I Bickell 30min Beginner (audio and materials) categories: web Soaplib is a very easy to use and powerful python soap library written at Optio Software. It will be open-sourced before [PyCon](PyCon) \'07.

79\. Python and vim: Two great tastes that go great together. Sean Reifschneider (tummy.com, ltd.) 30min Beginner (audio and materials) categories: gui, ide, shell The vim editor includes extensive abilities for customization and scripting. In addition to it\'s own simple macro language, vim also supports calling Python code. This Python code has access back into vim for manipulating the edit buffer as well as running normal vim commands. Examples demonstrated in this talk will include automatically detecting indentation style (tabs/N spaces), automatic update of DNS \"serial\" numbers when editing DNS zone files, mail alias tab-expansion, and a time tracking application using a \"domain specific vim\" as the user interface.

80\. Galaxy: A Python based web framework for comparative genomics Dr. James Taylor (Courant Institute) 30min Intermediate (audio and materials) categories: science, biology, web This talk will discuss the use and implementation of \'Galaxy\' ([http://g2.bx.psu.edu](http://g2.bx.psu.edu)), a Python based framework for integrating comparative genomic analysis tools.

83\. You vs. The Real World: Writing Tests With Fixtures Kumar [McMillan](./McMillan.html) 30min Intermediate (audio and materials) categories: testing One of the biggest challenges of testing is creating an environment akin to the real world that your code lives in. This talk will focus on general strategies for tackling the problem and then will move into specific examples using the fixture module for setting up and interacting with data stored in databases and other storage media.

The goal of the talk is to promote better code coverage in tests, more maintainable test suites, and techniques for easy and painless refactoring.

[http://testtools.python-hosting.com/](http://testtools.python-hosting.com/)

85\. The Essentials of Stackless Python Mr. Christian Tismer 30min Advanced (audio and materials) categories: concurrency, coroutines As a surprise for people who think they know Stackless, we present the new Stackless implementation For [PyPy](PyPy), which has led to a significant amount of new insight about parallel programming and its possible implementations. We will isolate the known Stackless as a special case of a general concept.

This is a Stackless, not a [PyPy](PyPy) talk. But the insights presented here would not exist without [PyPy](PyPy)\'s existance. 86. Python for Visual Effects and Animation Pipelines: A Case Study of Tippett Studio\'s JET Russell Darling (Tippett Studio) 30min Intermediate (audio and materials) categories: case study, animation JET is a Python-based system comprised of software tools and scripts used to implement a visual effects and animation pipeline .

87\. Scaling Python for High-Load Web Sites Mr. David J Shoemaker (Polimetrix, Inc.); Mr. Jamie W Turner (Polimetrix, Inc.) 45min Intermediate (audio and materials) categories: web Your job is to build a Python-based web application that can serve millions of dynamic hits per day. How are you going to do it?

Should you focus on the database? buying big hardware? caching? optimizing application code in C? alternative backing data stores? parallel computing?

In this presentation we will show what we\'ve learned while building such a system at [http://www.pollingpoint.com](http://www.pollingpoint.com). We will provide a specific end-to-end example of how to make a Python web application scale up to handle high load.

88\. Dateutil to the Rescue! Mr. Mike Pirnat (AG Interactive) 30min Intermediate (audio and materials) categories: case study, library A practical look at dateutil, a set of powerful extensions for Python\'s datetime module.

- When I was asked to replace a vendor-supplied reminder web application with a more robust and sophisticated Python service, two of the most fearsome requirements involved better handling of event recurrence and time zone support. Luckily, I happened across Gustavo Niemeyer\'s dateutil ([http://labix.org/python-dateutil](http://labix.org/python-dateutil)) package at exactly the right time; it quickly became the indispensable core of AG Interactive\'s new calendaring service, catering to over three million users on [AmericanGreetings](./AmericanGreetings.html).com and [BlueMountain](./BlueMountain.html).com .

I\'ll illustrate dateutil\'s capabilities, how I used it to solve some of my tricky problems, and share some interesting adventures I had with it along the way.

90\. Developing Python applications in Komodo 4.0 Mr. Todd Whiteman 30min Intermediate (audio and materials) categories: ide Komodo 4.0 is a Mozilla based IDE designed for scripting languages, primarily supporting Python, Perl, PHP, Ruby, Tcl and now [JavaScript](./JavaScript.html). It features code assistance technologies to aid in the rapid development of applications, debugging analysis to provide informative run time inspection, project management to help maintain code bases and to keep it organized and accessible, as well as providing a multitude of tools to assist in common programming tasks.

Todd, one of the authors of this IDE, will take you on a tour of all the features available to Python developers using Komodo as well as covering how Komodo itself makes use of Python internally.

Todd Whiteman is a Developer at [ActiveState](ActiveState) Software Inc and has been actively working on the Komodo IDE for the past 15 months.

91\. Unit testing with mock objects using [PyMock](./PyMock.html) jeff m younker (Data Pipes) 30min Beginner (audio and materials) categories: testing This is an introduction to mocking object behavior in unit tests using the [PyMock](./PyMock.html) module [http://www.theblobshop.com/pymock](http://www.theblobshop.com/pymock). There is a brief overview of mocking, a summary of existing python mock objects modules, and a recounting the common tasks to be accomplised using mocking and how they can be accomplised using [PyMock](./PyMock.html). 92. Write Less Code with XRC for wxPython Matt Boersma (Array [BioPharma](./BioPharma.html)) 30min Intermediate (audio and materials) categories: gui Learn an easier way to do GUI layout using wxPython\'s XML-based resource system.

93\. Jython for Python Developers Frank J Wierzbicki (Jython) 45min Intermediate (audio and materials) categories: implementations, jython Jython ([http://www.jython.org](http://www.jython.org)) is an implementation of the Python programming language designed to run on the Java Virtual Machine.

This talk will focus on using Jython to natively access JVM libraries from Python.

94\. Software Development with Trac Mr. Matthew Good 30min Beginner (audio and materials) categories: project Trac is an enhanced wiki and issue tracking system for software development projects. This talk will introduce users to using Trac to integrate their issue tracking and version control, use plugins for automated builds and testing, and demonstrate how to extend Trac with new plugins.

[http://trac.edgewall.org/](http://trac.edgewall.org/) 95. Writing Your Own Python Types in C Mr. Jack Diederich (Psynchronous Communications, Inc) 30min Intermediate (audio and materials) categories: extensions Hand writing C versions of your important Python classes isn\'t a mystery - or shouldn\'t be. This talk translates what you know about writing python classes to their lower level C equivalents. By example a Sudoku solver (everyone\'s favorite play thing) will get a 30% speedup by writing a from-scratch version of Python\'s set() in 300 lines of C.

96\. PyDX: mathematics is code Mr. Simon Burton (EWT LLC. and The Australian National University) 30min Intermediate (audio and materials) categories: science PyDX is a package for working with calculus (differential geometry), arbitrary precision arithmetic, and interval arithmetic.

97\. Parsing revisited: a grammar transformation approach to parsing Ernesto Posse (School of Computer Science - [McGill](./McGill.html) University) 30min Advanced (audio and materials) categories: parsing We present a new parser generator for Python applications called \"aperiot\" based on grammar transformation. This approach retains the complexity and performance advantages of LL(1) parsers while allowing to parse a large set of non-LL(1) grammars and without imposing a lookahead limit. We demonstrate the practicality of this approach with a case-study of a realistic language.

100\. Visual Python in a Computational Physics Course Dr. Richard P Olenick (University of Dallas) 45min Beginner (audio and materials) categories: education, university Using VPython physics students develop simulation programs to model a variety of physical systems.

101\. Embedding Jython applications in a Firefox Extension Mr. Ed Brannin; Dr. Jonathan I Schull (Rochester Institute of Technology) 30min Beginner (audio and materials) categories: packaging, jython This summer, I embedded a Jython-based web service in a Firefox extension. This talk (and accompanying files) will show how to do the same, particularly focusing on: - embedding Jython in a Java app, - porting a (fairly simple) [CherryPy](CherryPy)-based web service to Jython - common pitfalls, such as Jython quirks and where to store files, - and any other Really Nifty applications or techniqutes that I discover before February.

102\. Python for Students of the Modern World Dr. Andrew Harrington (Loyola University Chicago) 30min Beginner (audio and materials) categories: education, university I teach liberal arts students brought up in the information age. I expose them to the computing discipline and show them the power and enjoyment they can have using my Hands-on Python Tutorials, [http://www.cs.luc.edu/anh/python/hands-on](http://www.cs.luc.edu/anh/python/hands-on). The tutorials require active interaction and provide examples involving graphics, text processing, and dynamic web pages. I use Python as a tool to illuminate various parts of computer science.

103\. Weaving Together Women and IT Anna Martelli Ravenscroft 45min Beginner (audio and materials) categories: advocacy, community Women are woefully underrepresented in IT in general, and programmin and other higher-level IT areas in particular. Further, this is not merely a United States problem, but is worldwide: with few exceptions, women represent less than 30% of the IT workforce, primarily in the lower-skill areas, while comprising approximately half of the workforce. Even worse, the rate of undergraduate admission of women to CS majors has been trending downward. This deplorable situation has many causal factors, and has been studied extensively since the 1980s, yet the underlying causes are not clear. No single presentation can address all the factors, or all aspects, from K-12 to university undergraduate and graduate studies, to job and career development and retention. This presentation will focus primarily (but not exclusively) on entry to IT.

------------------------------------------------------------------------

[CategoryPyCon2007](CategoryPyCon2007)
