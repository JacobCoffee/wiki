# PythonFederalEnterpriseArchitecture

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

### Audience and Status of Position Paper 

This position paper, and the comments submitted by the community, will be presented to the Federal Enterprise Architecture Program Office. The paper is still a work in progress. It evolved out of a long email message so some of needs to be reworded. Also, footnotes need to be changed to hyperlinks.

### Python and the Federal Enterprise Architecture 

The goal of the position paper is to get Python to be considered as a peer to the .NET and J2EE technologies for defining enterprise components. The paper supports the PSF position that Python should be used to define the FEA core components. Python is often referred to as non-proprietary middleware \[1\], or executable pseudo code. It has the advantage of not being associated with a major corporation in the industry, so picking Python will not be picking a winner from the current short list of politically charged candidates. Python also has the advantage of being compatible with both .NET and J2EE \[2\]. It is compatible in the sense that the Jython implementation of Python runs on top of Java, so any Java object can also be used as a Jython object. There is also a Python implementation in .NET.

It would be inappropriate for either .NET and J2EE to be selected for the role as they are primarily proprietary technologies. Selecting one of them will cause no end of trouble because of the political posturing that will ensue. On a technical level, both technologies are more brittle than necessary. Their roots are in statically typed, purely object oriented languages. While this is a very popular programming paradigm, it restricts the design of applications to a single programming technique.

Python is a much more dynamic language and this results in a higher level of component reuse. Python blends many programming styles into a simple language that can easily be taught to non-computer science users. Python is unique in that an engineer, an accountant, or a seasoned computer scientist will all be productive with the language after a few days \[3\]. They will also not find the language restrictive after years of using it.

Python has a large and growing following. Sourcefoge lists Python as being just behind Perl in the number of projects that use the language. Python isn\'t as well known as C# or Java, but that is because Python does not have a major corporation backing the language. Instead, Python is growing in popularity due to word of mouth. This is all the more impressive if you consider that anyone choosing a lesser known language is faced with a battle against peer pressure and management mandates. There must be a very compelling reason for a language like Python to thrive in spite of the pressure of the network effect.

A language alone does not make an enterprise architecture. It is a combination of the language and the available software components that provide the utility needed for efficiently building enterprise applications. The Python community has kept pace with J2EE and .NET in developing enterprise components. Virtually every database and graphical user interface technology has been wrapped into Python modules and packages. All of the major Internet protocols are supported in the standard Python library of modules and packages.

The maintainence of legacy software is the largest expense of operating an enterprise IT infrastructure. Layers and layers of legacy software have built up over time. The tangled web of interacting systems is difficult to manage and any technology selected to build a component software based architecture must interface with many legacy systems. The ability to easily integrate legacy software into Python components is a differentiating characteristic of Python. By wrapping the legacy software in Python, the old software becomes an integral part of the Python component library with a object interface that is indistiguishable from any other Python object. The Python interface to the legacy systems can then be used to glue together systems that had never been designed to work together. The process reduces the cost of managing legacy software and provides a mechanism for isolating and phasing out obsolete software systems. Over time the functions performed by the legacy software can be rewritten in Python, or a new package can aquired that can be configured to conform to the interface of the legacy system.

In addition to the standard Python distribution there are many open source projects that are developing very innovative alternatives to the traditional techniques for building enterprise applications. One example of a Python package that is both innovative and applicable to the FEA is [TwistedMatrix](TwistedMatrix) \[4\]. This package was developed for building applications that allow many users to interactively collaborate on the Internet. The original goal of the project was to create a package that could be used to build role playing games on the Internet. The software pattern for a role playing game is nearly identical to the requirements of the FEA. Realtime state information about the individuals participating in the game must be maintained and security measure must be in place to ensure that individual\'s, and the game engine are safe from attacks.

Adapting technology developed from the gaming industry is not as odd as it might sound. The military use to purchase very expensive 3-D computer graphics computers from SGI and IBM in order to conduct simulated exercises. The power of these graphics computers has been overtaken by the graphics cards developed for the home game industry. These products were developed in parallel with the commodity personal computers and they have exploited Moore\'s law to create incredibly powerful 3-D simulation capabilities. The military now uses the commercial products, at a great cost savings. The economies of scale make this possible. The same holds for software technology that has evolved in the game industry.

The game industry is huge and the technology has matured over twenty years. The simulated worlds that are created in multiuser games are extremely sophisticated. The sophisticated security mechanisms developed for these game platforms are not suprising. The computer hackers who frequently play these games are famous for going to great lengths to try to break into the systems. The security systems of the games has evolved to defeat the hackers. This has resulted in the game engines developing sophisticated methods for isolating information from attack.

The [TwistedMatrix](TwistedMatrix) project is one example of a game engine technology that has applied the lessons learned in defending user information. They have focused on developing a component architecture that provides easy to use methods for selectively sharing complex objects within the game environment. Some of the information is restricted to access by specific types of users and other pieces of information are globally accessible. The analogy to providing access to an individual\'s personal information in a federal database is direct. In the virtual world you may provide access to some information to your friends, but restrict access to the same information to your enemy. Doctors may be given full access to your medical records, but a reporter from a newspaper may not be allowed to view the same information. This same ability to set access rules will be required in the FEA.

There is another economic aspect of the Python community that will impact the cost of developing the FEA. The .NET and J2EE solutions, along with the web services approach to sharing information, are approaches that where created by the commercial software vendor market. The open source market takes a very different approach to software development. The open source community is a collaborative development activity, that fundamentally differs from the competitive market of commercial software vendors. The basic motivations of the two groups differ in that open source developers will go to great lengths to exploit the work of their peers and the vendors will go to great lengths to differentiate themselves from competitors. The former leads to components that, by design, work well together and the latter leads to components that fail to interoperate because they differ in trivial details. Tapping into the open source \"market\" will reduce complexity because the open source developers invest considerable effort in reducing complexity.

At the language implementation level the choice between a Python based architecture and a Java or C# architecture are at odds in a fundamental aspect of language design. Dynamic languages do not require the definition of types prior to the execution of an application. This is a fundamental tradeoff between runtime error detection and compile time error detection. Another tradeoff is in the complexity of the software source code. Component definitions Python tend to be much shorter than the equivalent Java or C# definitions. A typical Python module will be 1/2 to 1/5th the size of a comparable Java module. The lines of code count is important because the bug count tends to be proportional to length of the application. Fewer lines of code translates to fewer bugs \[5\].

The fundamental difference between an architecture based on the .NET and J2EE platforms and a platform base on Python is that Python assumes a higher level language interface to the core architecture. And while Python is a higher level language, it provides pragmatic interfaces to lower level languages. It does so by wrapping the lower level language into Python so that they appear to be a core part of the Python language. Thus, you get all the advantages of the legacy technologies, but wrapped these technologies become wrapped into components that are much easier to use. By shifting to a Python based architecture you provide a legacy code migration strategy, while simplifying the overall architecture. It\'s a win-win approach to defining the FEA.

I have not discussed many of the opportunities to improve on the current Python design. These are the subject for the definition of Python 3.0. If the FEA were to adopt Python as a core technology, then the evolution of Python would become an important topic of discussion. A glimpse of what might be instore for Python 3.0 has been outlined in a Wiki page \[6\] at python.org.

### Ideas Needing to be Expanded 

An explaination of a LDAP based distributed authentication capability that would tie in with [TwistedMatrix](TwistedMatrix) would be a good addition to the paper. An explanation for why fat clients need to be used instead of Java in a web browser clients would also be a good addition. The contents of the paper should eventually be integrated into the \"E-Gov Enterprise Architecture Guidance\" paper that is available from FEAMO. They get some things correct, but there are some real fumbles in the document. The appendix with the list of \"standards\" should be thrown out and they should start over.

\[1\] [http://www.tundraware.com/Technology/Python-Is-Middleware/Python-Is-Middleware.html](http://www.tundraware.com/Technology/Python-Is-Middleware/Python-Is-Middleware.html)

- \"Cheap Energy was literally the fuel of the first Industrial Revolution.
  - Cheap Software is the fuel of this Economic Revolution.\"

\[2\] [http://www.zoteca.com/information/wp/pythonEAI.htm](http://www.zoteca.com/information/wp/pythonEAI.htm)

\[3\] [http://www.linuxjournal.com/article.php?sid=3882](http://www.linuxjournal.com/article.php?sid=3882)

\[4\] [http://www.twistedmatrix.com/services/success](http://www.twistedmatrix.com/services/success)

\[5\] [Message on Google groups](http://groups.google.com/groups?hl=en&lr=&ie=UTF-8&frame=right&rnum=41&thl=980713582,980649948,980645230,980554902,980498258,980423686,980411800,980365774,980304453,980230385,980230381,980224668&seekm=MRLN246641E232%40merlin.envox.local.hr#link48)

\[6\] [http://www.python.org/cgi-bin/moinmoin/PythonThreeDotOh](http://www.python.org/cgi-bin/moinmoin/PythonThreeDotOh)

Perhaps \"Snow Crash\" on the required reading list for anyone working on the FEA:-)

------------------------------------------------------------------------

[CategoryPythonInBusiness](CategoryPythonInBusiness)
