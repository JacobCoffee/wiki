# PyConDC2003/Speakers

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

***Speakers by First Name, with Presentation Titles***

Note to speakers **welcome to [PyCon](../PyCon)** - Feel free to edit the section for your paper, or to start a [PyConYourName](../PyConYourName) page dedicated to just your paper(s) - Thanks to [AndrewKuchling](../../../people/AndrewKuchling) for adding synopses to most presentations - *SH*

If you have multiple talks scheduled too closely together (see [http://www.python.org/pycon/pycon-schedule.html](http://www.python.org/pycon/pycon-schedule.html)), send e-mail to Neal Norwitz ([neal@metaslash.com](mailto:neal@metaslash.com)).

## Steve Holden 

**Introduction from the Chair**

Please see *[PyConSteveHolden](../PyConSteveHolden)* for an example [CategoryPyConSpeakerPage](CategoryPyConSpeakerPage) page. The chairman\'s introductory remarks will now probably given at the end of the conference ![:-)](/wiki/europython/img/smile.png%20":-)")

## Aahz 

**Threads tutorial**

This tutorial will walk through Python\'s threading model, emphasizing an understanding of the Global Interpreter Lock (GIL), then show how to create threaded applications using \"brute force\" threads and Queue.Queue.

## Aahz 

**Objects vs classes**

This tutorial is aimed at beginning/intermediate Python programmers who want to solidify their understanding of Python\'s object system. I\'ll be using new-style classes to illustrate various aspects, so you should read [http://www.python.org/2.2.2/descrintro.html](http://www.python.org/2.2.2/descrintro.html) (you don\'t have to understand all of it). Although the C API won\'t be discussed directly, this tutorial should be especially useful for people who intend to use the C API, because I\'ll be discussing Python\'s memory management at some length.

## Allen Short 

**Twisted Reality: A Flexible Framework for Virtual Worlds**

Modelling virtual worlds flexibly in object-oriented languages has historically been difficult; the issues arising from multiple inheritance and order-of-execution resolution have restricted the sophistication of existing object-oriented simulations. Twisted Reality avoids these problems by reifying both actions and relationships, and avoiding inheritance in favor of automated composition through adapters and interfaces.

## Benjamin Saller 

**CMFTypes: Next Generation Content Type Development for Zope 2**

CMFTypes is an attempt to simplify the creation of new content types under the Zope 2 and the Content Management Framework (CMF). Many content management projects involve introducing new types of content which in the non-trivial case requires an informed understanding of how Zope and the CMF work. CMFTypes attempts to provide a simple, extensible framework that can ease both the development and maintenance costs of CMF content types while reducing the learning curve for the simpler cases.

The Zope/CMF world is populated with many projects that deal with content types. Most of these deal with one or two aspects of content management, mainly specifying what data constitutes a type and what might serve as acceptable source data for populating a content object. By these I mean defining what fields make up a type (body, teaser, etc) and products that deal with converting rich original content (Office Products, PDF, Docbook, etc) into web ready forms.

CMFTypes provides a framework that tries to provide some layering between concerns and provide a reasonable set of default policy and integration with Zope\'s leading CMF implementation, Plone (www.plone.org).

## Brett Cannon 

**Using [ReStructured Text (reST)](http://docutils.sf.net/rst.html)**

Go to [PyConBrettCannon](../PyConBrettCannon) to let your questions, comments, etc. about this tutorial be heard!

## Brian Warner 

**BuildBot: build/test automation**

The BuildBot is a system to automate the compile/test cycle required by most software projects to validate code changes. By automatically rebuilding and testing the tree each time something has changed, build problems are pinpointed quickly, before other developers are inconvenienced by the failure. The guilty developer can be identified and harassed without human intervention. By running the builds on a variety of platforms, developers who do not have the facilities to test their changes everywhere before checkin will at least know shortly afterwards whether they have broken the build or not. Warning counts, lint checks, image size, compile time, and other build parameters can be tracked over time, are more visible, and are therefore easier to improve.

The overall goal is to reduce tree breakage and provide a platform to run tests or code-quality checks that are too annoying or pedantic for any human to waste their time with. Developers get immediate (and potentially public) feedback about their changes, encouraging them to be more careful about testing before checkin.

Check out [PyConBrianWarner](../PyConBrianWarner) for more details about this presentation.

## Brian Warner 

**Perspective Broker: \"Translucent\" Remote Method calls in Twisted**

One of the core services provided by the [Twisted](http://www.twistedmatrix.com) networking framework is \"Perspective Broker\", which provides a clean, secure, easy-to-use Remote Procedure Call (RPC) mechanism. This paper explains the novel features of PB, describes the security model and its implementation, and provides brief examples of usage.

Check out [PyConBrianWarner](../PyConBrianWarner) for more details about this presentation.

## C. Donour Sizemore, Jacob R. Lilly, and David M. Beazley 

**MONDO : A Shared Library and Dynamic Linking Monitor**

- Dynamic modules are one of the most attractive features of modern scripting languages. Dynamic modules motivate programmers to build their applications as small components, then glue them together. They rely on the runtime linker to assemble components and shared libraries as the application runs. MONDO, a new debugging tool, provides programmers with the ability to monitor in real-time the dynamic linking of a program. MONDO supplies programmers with a graphical interface showing library dependencies, listing symbol bindings, and providing linking information used to uncover subtle programming errors related to the use of shared libraries. The use of MONDO requires no modification to existing code or any changes to the dynamic linker. MONDO can be used with any application that uses shared libraries.

Project details are available at our [Project Page](http://systems.cs.uchicago.edu/mondo).

## Chetan Gadgil 

**KOBRA - .NET (Wrapper) for Python**

Please see [PyConChetanGadgil](../PyConChetanGadgil) for details.

## Christopher Armstrong 

**Managing the Release of a Large Python Project**

Twisted is a Python networking framework. At last count, the project contains 60,000 lines of effective code (not comments or blank lines). When preparing a release, many nits must be checked, and many steps must be followed. We describe here the technologies and tools we use, and explain how we built tools on top of them which help us make releasing as painless as possible.

See [PyConChristopherArmstrong](../PyConChristopherArmstrong) for more info.

## Christopher Blunck 

**Python in a Rapid Development Environment**

[SkipWare](./SkipWare.html) is a series of extensions to standard Internet transport protocols that, when installed on a network device, maximizes link utilization and reliability in a stressed transmission environment. It has been developed collaboratively between GST and Comtech: GST provides the software and Comtech provides the hardware. Although [SkipWare](./SkipWare.html) is an implementation of SCPS (Space Communication Protocol Standards), a graphical user interface is required to specify configuration settings that impact overall system performance. Given that the product forwards IP (Internet) traffic, a web-based client was the most feasible interface for our customers.

Because the interface requirements were soft and time was short, we approached the interface with a rapid development mentality centered around constant customer feedback. A language decision had to be made, and we had the following choices (primarily due to our experience): C, PHP, Perl, Java, Python. This paper examines our reasons for selecting Python and discusses the effect on the project.

## Dana Moore 

**Subversion from Within. Python in a Java world** Slides at: *[PyConDanaMoore](../PyConDanaMoore)* Our goal in this paper and tutorial proposal is to preach to the unconverted rather than reinforce what some of us already know to be true - that lightweight languages and Python in particular are transformational and illuminate a path for the future of application design and delivery. We note with some concern that the emergence of the Java programming language as the \"COBOL of a new generation\" often clouds the thinking of system designers and developers. Too many designers and developers simply cannot think in terms of lightweight languages as the vehicle for delivering sophisticated and complete systems. This paper and presentation suggests a \"embrace and replace\" strategy for co-existing with languages such as Java with the eventual goal of replacing their functionality altogether.

We conduct a survey of strategies for Python and Java co-existence with discussion and practical demonstration.

We suggest that in the next generation internet, there is a crucial need for Python scripting as the way to provide the \"glue\" for distributed applications, to support fast and loose prototyping, and indeed to create applications themselves. Many in our target audience may not consider =scripting languages to be first class application vehicles, but with Java objects as invocation targets for scripting languages and Java applications as a launch platform for dynamic scripting, it is an exciting recipe for building rapid prototypes and even next generation applications.

This paper and tutorial session will explain the how and why. In particular, we focus on: Java and Python together (Jython) and discuss and demonstrate distributed applications using Java and Python via JXTA and Jabber, turning native applications into services, and creating conversational knowledgebots with Python, ECMAScript and Java.

## David Abrahams 

**Introducing Boost.Python**

Boost.Python is a free C++ library which provides a concise IDL-like interface for binding C++ classes and functions to Python. Leveraging the full power of C++ compile-time introspection and of recently developed metaprogramming techniques, this is achieved entirely in pure C++, without introducing a new syntax. Boost.Pythons rich set of features and high-level interface make it possible to engineer packages from the ground up as hybrid systems, giving programmers easy and coherent access to both the efficient compile-time polymorphism of C++ and the extremely convenient run-time polymorphism of Python.

## David C. Morrill 

**Traits: A New Way of Adding Properties to Python Classes**

Python is a weakly typed language, which as any experienced Python programmer knows has both good and bad points. In this paper we discuss \'traits\', a new Python package whose goal is to help address cases where weak typing leads to problems. In particular, the motivation for creating traits came as a direct result of work done on Chaco, an open source scientific plotting package.

## David C. Morrill 

**Chaco: A Python Plotting Package for Scientists and Engineers**

With packages such as Mathematica and [MatLab](./MatLab.html), scientists and engineers already have a variety of high-quality plotting capabilities available to them. However, if you are a scientist or engineer who is also a Python user, or you are working with a limited budget, your choices are more limited. Chaco is an open source and freely available plotting package being developed to address many of the plotting needs of the scientific and engineering communities.

## Dean W. Hall 

**[PyMite](../../../people/PyMite): A Flyweight Python Interpreter for 8-bit Architectures**

[PyMite](../../../people/PyMite) is a flyweight Python interpreter written from scratch to execute on 8-bit microcontrollers. It is a work-in-progress, but is developed enough to run demonstration programs. This paper explains the motivation for creating [PyMite](../../../people/PyMite) and gives an overview of what [PyMite](../../../people/PyMite) can and cannot do. Then the current status and the work ahead are discussed. This is followed by details on the design and implementation of [PyMite](../../../people/PyMite). Two new features are mentioned: *stackless* frames and embedded native code. Finally, information is given on how to obtain [PyMite](../../../people/PyMite).

## Francesc Alted 

**Processing And Analyzing Extremely Large Amounts Of Data In Python**

Processing large amounts of data is a must for people working in such fields of scientific applications as CFD (Computational Fluid Dynamics), Meteorology, Astronomy, Human Genomic Sequence or High Energy Physics, to name only a few. Existing relational or object-oriented databases usually are good solutions for applications in which multiple distributed clients need to access and update a large centrally managed database (e.g., a financial trading system). However, they are not optimally designed for efficient read-only database queries to pieces, or even single attributes, of objects, a requirement for processing data in many scientific fields such as the ones mentioned above.

[PyTables](../../../people/PyTables) is a Python package designed for this precise aim. Go to my [PyConFrancescAlted](../PyConFrancescAlted) wiki page for a bit more detailed explanation on my talk.

## Francesco Garelli 

**Satine: a XML Data Binding technology for Python**

The XML language is becoming quickly an important protocol to exchange information and services in wide-area networks. Unfortunately popular solutions to manage XML documents seem to be little suitable. Technologies, such as DOM and SAX, have proven to be effective for short and simple documents but they are really complex when documents size and variety is pretty large. XML data binding is a new approach that looks very promising. Through the data binding, any XML document is translated to an internal data of the programming language the application is developed with. As a result, the developer doesn\'t treat XML, but a corresponding representation in the environment he has chosen for his application.

This paper describes a XML data binding technology for Python, namely Satine XML data binding. The solution we propose takes benefit from Python weak types and it is definitely simpler than similar approaches in the Java or .NET environments.

## Fred L. Drake, Jr. and Chris McDonough 

**Application Configuration Using ZConfig**

ZConfig is a Python package supporting application configuration. The basic facilities include a simple API for the application, a configuration file format, and support for configuration schema.

ZConfig performs some of the same duties as the [ConfigParser](http://www.python.org/doc/current/lib/module-ConfigParser.html) module in Python\'s standard library, but also provides support for hierarchical sections, data conversion, and input validation. The data conversion and input validation are based on a declarative schema language in XML. Using a schema to describe configuration helps avoid some kinds of application and configuration errors.

Paper and slides now [online](http://www.zope.org/Members/mcdonc/Presentations)

## Geoffrey S. Knauth 

**Lessons Learned in Converting a Large C Program into Manageable Python Modules**

The C program in question, a large program that determines fuel requirements and examines supply and distribution options for the Defense Logistics Agency, grew appreciably between 1994 and 2002. As new web technologies evolved around it, adapting the program to handle new database tables, interactions with a service that manages nodes representing intemediate computations, and repartioning of functionality, became more difficult. External interface changes were beginning to require disproportionately large internal changes to the program. Future development of the C program, as successful as it was, seemed a dubious prospect. This presentation discusses the research effort to rewrite the C program in Python.

Presentation slides are available at [http://knauth.org/gsk/talks/PyCon-ICIS/PyConDC.htm](http://knauth.org/gsk/talks/PyCon-ICIS/PyConDC.htm).

## George Belotsky 

**Flightdeck-UI \-- a Cockpit on your Desktop**

Flightdeck-UI is a project that seeks to utilize the ideas in aircraft controls and instruments design for creating general purpose user interfaces. The project currently includes a library, and the Multi-Variable Monitor (MVM) application. The latter incorporates a graphical editor with theme support, and can be used with virtually no coding (although you are welcome to develop plug-in modules for MVM if you wish).

The presentation will cover the following topics.

- Why aerospace is a good source of ideas for more generic user interfaces.
- The architecture of Flightdeck-UI.
- Flight instruments and their Flightdeck-UI counterparts.
- How you can start using Flightdeck-UI quickly in your own projects.
- Demonstration of Flightdeck-UI, including the graphical editor and themes.

*Note: formal submission of this paper has been received.*

## Glyph Lefkowitz 

**Generalized Deferred Execution in Python**

A deceptively simple challenge faced by many multi-tasking applications is gracefully doing nothing. Systems that must wait for the results of a long-running process, network message, or database query while continuing to perform other tasks must establish conventions for the semantics of waiting. The simplest of these is blocking in a thread, but it has significant scalability problems. In asynchronous frameworks, the most common approach is to have long-running methods accept a callback that will be executed when the command completes. These callbacks will have different signatures depending on the behavior being invoked, and often, a great deal of glue code is necessary to glue one portion of an asynchronous networking system to another. Matters become even more complicated when a developer desires to wait for two different events to complete, requiring them to \"juggle\" the callbacks and create a third, incompatible callback type to handle the results.

This paper describes the mechanism used by the Twisted framework for waiting for the results of long-running operations. This mechanism, the Deferred, handles the often-neglected problems of error handling, callback juggling, inter-system communication and code readability.

## Ian Bicking 

**The Web Framework Shootout**

In the beginning for the Python web programmer there were two choices: Zope and the cgi module. On one hand you had a featureful but complex application environment, on the other a simple but featureless and low-level module. For a significant number of web applications Zope\'s features aren\'t helpful and the complexity daunting. But any developer will quickly find themselves building higher level interfaces.

And so it has happened \-- a variety of web application frameworks have been developed in the last few years, with regular additions. In this paper we will compare a variety of these frameworks, and also provide concrete examples of using them.

## Itamar Shtull-Trauring 

**Tutorial: Low-level networking with the Twisted Framework**

Twisted is an event-driven framework for building networked clients and servers. It contains a powerful and simple networking core, a full-featured suite of interoperable protocols, among them a powerful web server and applications framework.

Twisted can run protocols over TCP, SSL, UDP, multicast, Unix sockets and subprocesses. It also includes scheduling support, threading integration, RDBMS event loop integration and other basic requirements for networked applications. GUI integration includes GTK, GTK2, Qt, wxPython, Tk and win32all.

This is a tutorial on networking with Twisted - the twisted.internet package. This would include TCP networking, implementing server protocols, client protocols, GUI integration, server deployment, and so on.

## Jason Abate and John Shafaee 

**HALL: A Domain-specific Python Middleware Package**

HALL, the Hostway Abstract Logic Layer, is a domain-specific middleware layer that consists of a number of Python classes that provide the fundamental building blocks for our nusiness applications. This paper describes the motivation that led to the development of HALL, some of the main design ideas, as well as some general observations about building an enterprise-level infrastructure with Python.

## Jean-Paul Calderone 

**Applications of the Twisted Framework**

Two projects developed using the Twisted framework are described; one, Twisted.names, which is included as part of the Twisted distribution, a domain name server and client API, and one, Pynfo, which is packaged separately, a network information robot.

The slides for this presentation are available at [http://intarweb.us:8080/PyCon/applications-0.xhtml](http://intarweb.us:8080/PyCon/applications-0.xhtml)

## Jim Fulton 

**Zope Component Architecture**

Component systems allow applications to be created by assembling pre-existing components. A major new version of the Zope application server has been developed utilizing a component architecture. This new architecture makes it much easier to use Zope software in other applications and to use non-Zope software when building Zope applications.

This paper describes the Zope component architecture. The component architecture is based on a simple but powerful definition of components based on interfaces. It uses adapters to separate application-specific logic from core object behaviors and views to separate user-interface implementation from object and application functionality. The architecture provides automatic component assembly through an interface-based component registry.

## Jim Fulton 

**Tutorial: Programming with the Zope Component Architecture**

Zope 3.0 introduces a component-based architecture for extending Zope. The component-based architecture provides separation between content, application logic, and presentation logic. It significantly eases software reuse by allowing content-types or applications to be extended by simply adding or replacing components. This tutorial provides an overview of the component model.

## Joel Shprentz 

**Prevayler for Python: An alternative to relational and object-oriented databases**

Prevayler is a low-overhead, high-performance alternative to relational and object-oriented databases for applications that satisfy Klaus Wuestefeld\'s Prevalent Hypothesis: \"There is enough RAM to hold all business objects in your system.\".

Prevayler offers a new approach to object persistence. All business objects reside in RAM. Periodic snapshots are stored to disk. Transactions that modify business objects are logged to disk before execution. To recover after a system failure, the snapshot is loaded from disk and the logged transactions are replayed.

## John Aycock, David Pereira & Georges Jodoin 

**UCPy: Reverse-Engineering Python**

One of the recurring topics in the Python community is how to make Python programs run faster. Typically, a set of solutions is proposed which include: adding static type inference; somehow compiling programs into native code; translating Python programs into Parrot/ Lisp/.net code; applying research results from dynamically-typed language implementation. Progress has been made on some of these, such as Psyco, but many of these proposed solutions are qualified by the caveat no one has the time/resources to work on it.

In the Programming Languages Lab at the University of Calgary we have a research project underway, UCPy, whose short-term goal is to examine ways we can make Python run faster. We have learned some lessons through our design and implementation work to date, about both Python and the undertaking of such a project, which we present in this paper.

## Ken Manheimer 

**Conversations With Zope: Interactive Debugging Using the Python Prompt**

This is about interacting with the Zope server directly at the Python level to facilitate development, debugging, and general orientation on Zope operation. Zope is eminently extensible, and is written primarily in a Python, a particularly comprehensible interpreted language. We present ways to use the python prompt, its debugger, and various Zope faculties to talk directly with the Zope server, to poke and prod - to see and affect what is happening while the server is running.

The paper is online, along with related stuff, in a wiki at [http://www.zope.org/Members/klm/ZopeDebugging](http://www.zope.org/Members/klm/ZopeDebugging).

## Kendall Clark, Daniel Krech, A.M. Kuchling, Bijan Parsia 

**Introduction to the Semantic Web**

This 15-30 minute talk will explain the fundamentals of RDF and provide a brief overview of writing code using rdflib. [Draft slides](http://www.amk.ca/talks/semweb-intro/) are available.

## Leonard Richardson 

**Beyond The Config File: User-Friendly Configuration For Web Apps**

The usability of many web applications can be increased dramatically by putting into place a configuration framework: an end-user interface to an application\'s configuration which looks like the rest of the application. This makes the application easier to use, increasing the number of potential users, without making the developer\'s job more difficult.

More information and a work log available at [PyConLeonardRichardson](../PyConLeonardRichardson).

## Michael Bernstein 

**Case Study: A Faceted Classification Solution for a Reusable Digital Asset Repository**

Changing the metadata fields that are specific to a particular instance of a content management application is often the one area that requires an actual developer who can add and delete class attributes, HTML forms, ZCatalog indexes and metadata, and Python scripts, in order to make the necessary customizations.

In the following case study, a solution was developed to allow a user with management priveleges to change the metadata configuration of an application instance, and automatically adjust the application as appropriate.

## Moshe Zadka & Andrew Bennetts 

**The Lore Document Generation Framework**

Lore is a documentation generation system which uses a limited subset of XHTML, together with some class attributes, as its source format. This allows for lower barrier of entry than many other similar systems, since HTML authoring tools are plentiful as is knowledge of HTML writing. As an added advantage, the source format is viewable directly, so that even if Lore is not available the documentation is useful. It currently outputs LaTeX and HTML, which allows for most use-cases.

Lore is currently in use by the Twisted project to generate its documentation for versions 1.0.1 and above.

## Nathan Yergler & Vern Ceder 

**Teaching Programming with Python and [PyGame](../../../multimedia/PyGame)**

Abstract, paper, etc now available at [http://tech.canterburyschool.org/pycon](http://tech.canterburyschool.org/pycon)

At Canterbury School we have taught Python to all of our 9th and 10th graders as part of a required basic computer skills course, and also to experienced programmers in a semester elective and in a 3 week May-Term course on game programming. This paper presents our reasons for adding Python to the curriculum and our evaluation of Python as a part of a secondary school curriculum.

Our hope in switching to Python in our computer skills course was to enable coverage of some basic programming concepts and problem solving skills without as much need to worry about the syntactic \"baggage\" of languages like C or Java. In this regard, Python has been very successful.

In our advanced elective and our May-Term mini-course we wanted to introduce our students to a somewhat different style of programming language, and we wanted it to have sufficiently powerful libraries to make the creation of GUI and network applications easier, allowing more time to concentrate on program design and logic. In general, we have been happy with Python in these courses, although there are some aspects of Python that are not helpful in our advanced classes.

## Neal Norwitz 

**Building a Better Bug Detector**

[PyChecker](../../../people/PyChecker) started nearly two years ago as an experiment: was it possible to build a tool which could reliably detect bugs in Python code? Before implementing [PyChecker](../../../people/PyChecker), I thought only a few bugs could be found and the experiment would ultimately show the difficulties in uncovering bugs. I was quite happy to be proved wrong. With nearly 100 unique warnings already implemented, many potential error conditions can be found. This paper will explore the design of [PyChecker](../../../people/PyChecker), including current limitations and suggestions for alternate designs, to enable building a better bug detector.

## Paul Swartz 

**Implementing SSH in Twisted**

Conch is an implementation of the Secure Shell Protocol (currently in the IETF standarization process). Secure Shell (or SSH) is a popular protocol for remote shell access, file management and port forwarding protected by military-grade security. SSH supports multiple encryption and compression protocols for the wire transports, and a flexible system of multiplexed channels on top. Conch uses the Twisted networking framework to supply a library which can be used to implement both SSH clients and servers. In addition, it also contains several ready made client programs, including a drop-in replacement for the OpenSSH program from the OpenBSD project.

Slides from this presentation are available at [http://www.twistedmatrix.com/users/z3p/files/conch-slides.tgz](http://www.twistedmatrix.com/users/z3p/files/conch-slides.tgz) The (rough) text of the presentation is available at [http://www.twistedmatrix.com/users/z3p/files/conch-talk.html](http://www.twistedmatrix.com/users/z3p/files/conch-talk.html)

## Perry Greenfield, Jay Todd Miller, Jin-chung Hsu, & Rick White 

**numarray: A New Scientific Array Package for Python**

Python has long had an array module (Numeric) for science and engineering applications; why a replacement? We explain the motivations for developing numarray. We also describe the design issues in its development and its new features and capabilities. Numarray is highly compatible with Numeric, including the C-API, though there are some differences which are discussed. Numarray is well developed enough that it is being used in production pipelines to reduce and calibrate Hubble Space Telescope (HST) data and is being distributed to HST users along with applications for data reduction. Finally, we outline planned enhancements and improvements. Numarray is available from the Sourceforge numpy project page.

## Alexander Pletzer and Doug McCune 

**Computing magnetized plasma equilibria in a tokamak using Python**

A finite element application, RZSOLVER, for the computation of toroidal magnetohydrodynamic equilibria is described. RZSOLVER builds on two recently developed Python packages: ELLIPT2D and DISTSOLVE. The former is a general purpose finite element program to solve second order partial differential equations in two dimensions while the latter is an XML-RPC based Web service to solve sparse systems of equations.

## Roman Geus and Peter Arbenz 

**[PySparse](./PySparse.html) and [PyFemax](./PyFemax.html): A Python framework for large scale sparse linear algebra**

This paper describes our experience with the redesign and reimplementation of a large-scale application from accelerator physics using this mixed-language programming approach with Python and C.

The application code which was originally written in Fortran 90, with smaller parts written in C and Fortran 77, primarily solves eigenvalue problems and linear systems involving large sparse matrices. The order of these matrices can become as large as 7.5 million and the memory requirements of one such matrix can grow beyond 2 GBytes.

The paper also presents the two Python software packages: [PySparse](./PySparse.html), for manipulating sparse matrices, and [PyFemax](./PyFemax.html), a finite element code for computing three-dimensional electro-magnetic fields in accelerator cavities.

## Shane Hathaway 

**Adaptable Storage (Tutorial)**

For a long time, people have been requesting better relational integration in Zope. Zope has limited relational integration: you can open connections to an RDBMS and store and retrieve data, including objects. But objects from the RDBMS never reach \"first-class citizenship\" in Zope. Zope does not allow you to manipulate these objects as easily as you can work with objects stored in ZODB.

There are backends for ZODB that let you store pickled objects in relational databases. This solution satisfies those who need to store large amounts of data, but the data is stored in a special Python-only format. It prevents developers from taking full advantage of relational data storage and locks out other programming languages.

\'[AdaptableStorage](./AdaptableStorage.html)\' bridges the gap between ZODB and relational data storage. It lets developers store ZODB objects in arbitrary databases and arbitrary formats, without changing application code. It combines the advantages of orthogonal persistence with relational storage.

## Steffen Viken Valvaag, Aage Kvalnes and Kjetil Jacobsen 

**POSH \-- Python Object SHaring**

Python uses a single global lock known as the global interpreter lock (or GIL) to serialize execution of byte codes. The GIL becomes a major bottleneck when executing CPU-intensive multi-threaded Python applications.

This paper presents POSH, which is an extension module to Python that attempts to address the problems associated with the GIL by enabling placement of Python objects in shared memory. In particular, POSH allows multiple processes to share objects in much the same way that threads do with standard Python objects. We have found that the use of POSH allows some applications to be structured as if they used threads, but without the GIL bottleneck.

More information about this talk is available on [PyConSteffenVikenValvaag](../PyConSteffenVikenValvaag).

## Tom Bryan 

**Unit Testing in Python**

This presentation will show you that starting to use a standard unit test framework is so easy that you have no excuse not to use it. I will present at least unittest, a module available as part of the standard Python library. I will define \"unit testing,\" explain the basic use of at least unittest, and try to give you a sense of what development is like when using unit tests. Depending on the audience, the talk will either be a sort of tutorial for using unittest and how to start incorporating unit testing into your development, or it will be a brief introduction to the unittest module followed by an extended discussion of practical issues of using unittest to test non-trivial classes.

I will be providing more information about this talk on [PyConTomBryan](../PyConTomBryan). If you\'d like to see what this talk will (may) be about, or if you\'d like to influence what I will be presenting, please see that page.

## Tom Olivier 

**A Population Simulation System Written in Python**

This paper describes a population simulation system being developed in Python. This system is intended as a tool for biological researchers and conservationists who seek to model a range of demographic, genetic and other processes in animal populations of several hundred to a few thousand individuals. The system particularly targets populations subdivided by social groupings, space or landscape features.

## Travis B. Hartwell 

**Deployment of Twisted Web Servers**

Twisted is a Python framework for writing networked applications. Among other things, Twisted has a web server that can be used out of the box. However, because Twisted is first and foremost a framework, using it gives many advantages over conventional web servers, and deploying a server with it is possible in many different ways. Here, I will cover several advantages of using Twisted Web and the various possible ways to deploy such a server, with emphasis on UNIX-like systems. The pros and cons of various approaches will be discussed, as well as the tradeoffs that accompany the various configuration options. Finally, some current deployments of Twisted Web will be given as examples.

Slides can be found at: [http://www.twistedmatrix.com/users/nafai/pycon-paper/](http://www.twistedmatrix.com/users/nafai/pycon-paper/)

## Trent Mick and David Ascher 

**Smoke: an automated build, regression and performance tracking toolset**

Smoke is a SQL-backed client-server system used to manage information about builds of software packages \-- as the source code base evolves, which builds pass, which regression tests pass, and how performance metrics evolve with the software. Smoke is open source, and built on top of Quixote and Chaco.

## Wesley J. Chun 

**Python in Medicine**

Synarc is a medical imaging service company which utilizes Python to develop software which aids doctors in assessing patients. In this paper, we will give a high-level over- view of how Python is being used to create such applications which allow Synarc to aid pharmaceutical drug companies carry out clinical trials to test new drugs which help people suffering from symptoms in the areas of arthritis and osteoporosis.

We will describe what the various system are which perform the analyses, as well as present the basic architecture of each suite of applications. In particular, we will discuss Python\'s use as well as how 3rd party tools and software, including other Python modules, are integrated into the entire system. Finally, the rapid development time that Python provides its users is a strong motivating factor as it allows each study to be customized to a sponsor\'s needs quickly, speeding up the process by which clinical trials are conducted and worthy medicines entering the market for public consumption.

## Wesley J. Chun 

**Python In Education**

There are a variety of technical working professionals taking Python courses every year. It would be an interesting study to determine the background of the average Python student who generally has full-time employment, as well as those who are paying their own way.

The author of this paper has taught 5 such classes since January 2000. For each group of students, a survey is given to students to gauge the relative aptitude of the class. This aids the instructor in designing and customizing the course to make it as effective as possible based on the skills and background of the attending audience.

In this paper, we will present the survey that was given to all the students, as well as the cumulative empirical data that has been collected over the last 3 years. Students were asked about their programming background, their occupation, and the goals and motivation for taking a course in Python programming.

[CategoryPyConSpeakerPage](CategoryPyConSpeakerPage) [CategoryPyCon](CategoryPyCon)
