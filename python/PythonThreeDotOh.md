# PythonThreeDotOh

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

### Proposal for Funding Developing Python 3.0 

Now that the PSF has official tax-exempt 501(c)(3) corporation status, it is possible to pursue grants to fund development of Python. The timing for this is perfect. Many governments around the world are becoming very interested in using Open Source Software and Python is an attractive technology for reducing the complexity of enterprise deployment of systems. We need a plan that describes why we need grant money and how we would use it. Grant requests would target R&D funding from NSF, the EU, and private foundations. The requests would first describe how Python has had a positive impact on major segments of the IT world that use, and how this impact could be improved by the creation of Python 3.0. The Python Enhancement Proposals (PEPs) can be used as a resource for writing grant request, because they describe much of the work that needs to be carried out.

I have not found a roadmap to Python 3.0. If one exists, then we can substitute it for the seed list of features and changes that I\'ve assembled later in this document. In either case, I\'ve just put together the list as a starting point for discussion. Some of the items on the seed lists are based on comments that Guido has made about changes he would like to make in a future Python release. Some of the items are based on threads that explore potential new features. The remainder are from my own musing about what we could do if the PSF were to be funded to create the Python 3.0 release.

I have not addressed the process of writing grant requests and the infrastructure of the PSF that would need to be in place to support administering the grants. There are organizations that do this kind of work for a living that could be hired to do this aspect of the project. Please join in with improving this wiki page. I\'ve taken it about as far as I can go with my limited experience in writing grant applications.

### Some Target Markets for Python 3.0 

The first and most strategic target would be organizations that fund educational tools. The CP4E proposal could be dusted off and updated to target this audience. (NSF would be a better funding option than DARPA for the project.) The goal is to develop resources that can support the widespread use of Python in high school level computer science classes instead of Java as the introductory CS language. The project would also work towards getting Python qualified for use as an Advanced Placement language. If educational institutions start to use Python to teach computer science, then the language will carry forward as the students enter the marketplace.

The second grant target would seek funding from the financial community (and government agencies that work with financial data). The addition of native decimal numbers is the top priority for this audience. To quote Mike Cowlishaw, \<[MFC@uk.ibm.com](mailto:MFC@uk.ibm.com)\>, \"\[without decimal numbers\] Our services people won\'t touch it.\" Other tasks that will make Python more attractive to the financial services would include the addition of capabilities/proxies to the core language distribution to enable fine grain security control as is done with Zope. These grants requests could also target enhancements to the libraries with the inclusion of SQL database adaptors, and packages that provide standard financial calculations.Agencies that are funded by the [NITRD](http://www.itrd.gov/pubs/blue03/index.html) [SEW](http://www.itrd.gov/pubs/blue03/assessing_transforming_01.html) project might be receptive to this type of proposal. Also, the members of the EU are funding open source projects that could be used by governments. Finally, Wall Street is making heavy use of open source software these days. Some money might be available from that community as well.

The third grant target would be in support of Internet standards. The IT community, for better or worse, has managed to settle on XML as a standard language for representing data. The impact is very visible. XML is being used to represent virtually all information that will be exchanged over the wire. The use of XML is inappropriate for some tasks, but since the community has not agreed on a viable standard middleware language, XML gets enlisted to fill this role. Python is well suited for middleware tasks. The resent discussion of capabilities touch on one aspect of the language that could be improved to make the Python a better middleware language. At the Python conference in February 2002 Tim Berners-Lee stated that the W3C could add a W3C standards track fro Python if the Python community were behind the effort. We could pursue this avenue to give Python the special status as an officially recognized middleware language within the W3C.

A final grant target would be high end scientific computing environments. Python already has a strong presence in this IT segment and it should be relatively easy to attract support for extensions to Python that benefit a wide range of science applications. The core numeric capabilities can be used as a proof of concept and the grant would propose changes to make the language even better for this kind of application would be describe in the proposal. There may be a few core language changes to support numerics better, but most of the effort would probably be in enhancing the \"no assembly required\" distribution to support educational and scientific activities.

### Technical Approach 

It is very simple. There will be three language syntaxes, but only one byte code interpreter.

The Python 3.0 interpreter would not be a rewrite from scratch. We have watched Perl go down that route and it looks like a tremendous effort for a minimal gain. The SWIG project also concluded that a from-scratch rewrite was destine to fail. They found it better to make enhancements with the old code that were not backwards compatible, but provided benefits that justified breaking backwards compatibility. For Python 3.0, the new language syntax would be introduced using a second interpreter. The legacy interpreter would still be used to compile .py files, but new `.dp`{.backtick} files would conform to Python 3.0 syntax. (A third syntax would be added to define python Interfaces in .ipy files.)

The implementation of the compiled Python 3.0 is TBD. It could continue to use the byte code interpreter with Python 2.3, or, the Python 3.0 compiler may generate no byte codes. Instead, the new syntax would be compiled to machine code by a pycho-like compiler. It may be that the compiler would fall back to using the byte code interpreter when some features of the language are used, such as name injection from other modules. I\'m being vague here, because this is just a strawman and I\'m sure someone on python-dev will come up with something very clever. We need to put something down on paper in order get grand funding. Presenting this strawman may be sufficient to get a grant funded.

The primary goal of Python 3.0 is to make the language more usable to both the newbie user and the expert user, while also introducing constraints on the language that will make it easier to compile the language to more efficient code. To accomplish this, key tasks will be undertaken to: a) Rework the syntax to eliminate visible warts of the language and to introduce improved syntax for new concepts, such as decimal numbers, unicode, generators, etc. This is also an opportunity to add new keywords. Features, such as generators will benefit from this one-time opportunity. b) Add restrictions were necessary to facilitate automated optimization. c) Enhance the library and documentation from *batteries included* to *no assembly required*. The library improvements would be the basis for a \"fat Python\" distribution.

### Seed list of features and changes for Pyton 3.0 

1\) Use decimal numbers as the default floating point type.

- (Mike Cowlishaw may be able to help with the implementation.)

2\) make object the default root of all objects, create a new \"oldclass\" type that can be used to create old style classes.

- (Per Guido\'s musing on Python 3.0 changes.)

3\) Add Interface syntax in .ipy files.

- \- Includes an optional static typing syntax definition - uses the core Zope Interface semantics.

  \-[Zooko writes](http://mail.python.org/pipermail/python-dev/2003-March/034057.html) about Pythonic type-checking:

  *Their solution is quite Pythonic, inasmuch as type-checking is dynamic, structural (an object matches a type if it offers the interface regardless of whether it is explicitly declared to be a subtype), and soft (an object can implement only part of a type).*

  These are the three noble features of Python\'s type system.

4\) Add [capabilities](http://mail.python.org/pipermail/python-dev/2003-March/034149.html) or proxy limitations to core language. Maybe have this integrated into the Interface syntax, or create a \"proxy\" alternative to the \"object\" base class that is a proxy base class. This would also be a good opportunity to refactor the import statement so that support for restricted access to objects is easier to define, understand, and managage. Should the introspection of the identity of a class be separated from the power to create an instance of the class? This currently isn\'t the case.

5\) use unicode strings as the default string type. Introduce an \'a\"string\"\' as an ascii seven bit string type. h\"bytes\" as a raw hex byte type for manipulation of non-text based streams of bytes.

6\) eliminate default comparisons (taken from this a quote on python-dev)

\> I\'d like to to this in Python 3.0, but that probably means we\'d have \> to start deprecating default comparisons except (in)equality in \> Python 2.4.)

The following quote also talks about problems with comparisons.

\"\"\"Based on reading cl.py, the validity of nonsense comparisons is one of the more surprising \'features\' of Python for beginners \-- who reasonably expect a TypeError or ValueError. Once they get past that, they are then surprised by the instability across versions. Given that universal sorting of hetero-lists is now broken, I think it would be better to do away with it cleanly. It is seldom needed and would still be available with a user-defined sorting function (which requires some thought as to what is really wanted). A Python version of the present algorithm could be included (in Tools/xx perhaps) for anyone who actually needs it. (Terry Reedy 2003-03-15)\"\"\"

7\) Seek alternative syntax for generators and other notations that are difficult to lookup in documentation. The syntax should always include a unique keyword in a statement that will easily be searched for in the tutorial. This is an opportunity to extend the list of keywords in the language.

8\) Introduce a module pragma that is required in order to enable out-of-module name injection and the use of the eval and execfile functions. (this allows for much better local analysis by isolating the manipulation of names to within the module. The pragma would allow the old style loose overloading of names to be done for those rare occasions when there is an advantage in being able to do so.) An alternative would be to only allow this to occur in old style modules. A new-to-old style translator would be run on the module to enable the old behavior.

9\) Write a Python in Python implementation. (If the Python 3.0 compiler is fast enough then the Python 2.4 interpreter would be rewritten in Python 3.0.)

10\) review the language for left to right consistency in the ordering of execution of statements. (Apparently the order of execution of code in generator definitions is confusing to some.)

11\) Incorporate numeric python into the core distribution? (at least make it a \--with-numeric option at compile time.) This is part of the \"no assembly required\" project.

12\) Introduce an easier to type syntax for reserved names, such as [iterator]. Would \@iterator be an improvement? (I\'m really in musing mode here. This is probably a throw-away.)

13\) Review all of the PEPS and prioritize the suggestions based on probability of success. Each probably could be used to describe a grant request.

14\) Removing obsolete methods, such as [cmp] from objects in Python 3.0.

- (Per Guido on python-dev on 2003-3-15). (I think this is what item 6 is suggesting.)

15\) Start over with threading - compared to other languages its a bit of a mess and for some of the targeted applications for Python 3.0, threading is very important.

### Libraries 

1\) Include wxPython or [PyGtk](http://www.moeraki.com/pygtktutorial/pygtk2tutorial/index.html) in core library? Would anygui also be a good option. Place Tkinter into legacy status? (Musing again. Seems like we need a more mainstream, higher performance standard GUI in the core distribution. wxPython is very popular, so I suggested it as an option. The [PyGtk](PyGtk) is an awesomely thin layer over the C library and it makes Gtk objects look like native Python classes.)

2\) Add appropriate numeric python libraries. Only installed if the \--with-numeric flag is set.

### Fat Python Distribution 

1\) Pull core Zope components into the standard fat python distribution. (Perhaps instead of a very fat tarball it will be a network based install. In that case one of the automated download mechanisms that had been proposed would become part of the standard distribution.) Also need to reconsider:

- from [http://src.python.org/](http://src.python.org/) import kitchenSink

2\) Create a fat python distribution that includes a full featured set of libraries. This would be a source code distribution that would be tested to automatically compile for the primary target OS platforms (various Linux distributions, Windows, Mac, various BSD distributions)

3\) Distribution would include as much Python documentation as can reasonably be assembled. Solicit special contributions that are targeted at providing courseware for K-12 and undergraduate education in computer science, as a support language for non CS disciplines.

4\) Extend the core library reference manual with extensive examples. Perhaps do this by providing hyperlinks to cookbook exercises that illustrate the use of the various library modules. Do a study to ensure that 100% of all library features are documented with real and easy to mimic examples.

### How PSF Would Use the Grant Funds 

This obviously will require much discussion and it depends on the folks at [PythonLabs](./PythonLabs.html). Here are some strawman options:

\- Move [PythonLabs](./PythonLabs.html) into PSF and let the core team work more on Python?

\- Hire full-time or contract with developers to work directly on

- specific tasks in the Grant request.

\- Create a mini-grant program in which the grant money would be

- distributed to independent developers who submit task order proposals. (This would be useful as a demonstration of a model for a new form of contracting for software improvements for organizations like the Federal government.) Some of these grants might be like retainers for maintaining and improving modules and packages for which the retainee is the principle developer.

\- Model the program after the funding model used by NSF to fund

- principle investigators in medicine and chemical research. (Give Guido and a few others a bunch of money to conduct research.

### Python 3.0 as an Enterprise Architecture Component Integration Language 

The Federal Enterprise Architecture is developing a new IT architecture for operating Federal agencies within the U.S. government. There are 24 Presidential Initiatives that target IT capabilities, such as payroll or human resource management, that are to be unified across all agencies. The approach that is being taken in to restructure the old stove pipe IT infrastructure of each agency by replacing the common capabilities with a services oriented architecture. This change will require the use of component-based software development life cycle process. The short list of candidates being considered for the architecture is .NET and J2EE. This list should also include Python. The PSF needs to make this happen.

Open source projects are notoriously poor at marketing. It just isn\'t part of the culture. People are free to use the code, or not. Were Python to be a part of a commercial venture the marketing department would capitalize on the use of Python as a systems integration language by market it as an Enterprise Architecture Component Integration Language. If Python is to grow in market share compared to Java and C# it will be necessary to sell the benefits of Python to high level management within organizations. The decision makers need to understand that Python, and a framework of Python modules and packages, provides the core components of a vendor neutral enterprise architecture construction kit.

There are plenty of examples of Python in use to demonstrate that it is a viable candidate for defining and implementing large enterprise architectures. Python is called a flexible glue language by the web development community. The terminology for this role varies in other groups. At LLNL they call Python a steering language. It has also been called a language for middleware, but the term middleware is somewhat nebulous. The role or pattern of use of Python, regardless of the label is consistent. Legacy applications are wrapped in Python to turn them into powerful Python software components. These components are integrated into larger applications which are often prototyped entirely in Python. Some Python modules are rewritten in C or C++ when performance bottlenecks are identified.

A position paper on [PythonFederalEnterpriseArchitecture](PythonFederalEnterpriseArchitecture) has been drafted. Comments on the paper from the PSF membership would be helpful in making the case for using Python to provide a vendor neutral component architecture for the FEA. This would be a critical win for Python, so it is important to make our voices heard.
