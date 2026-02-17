# ArticleIdeas

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# Suggestions to Aspiring Writers for Magazine Articles About Python 

------------------------------------------------------------------------

- ***Python and Relational Databases***

  - Talk about the DB-API that Python has standardized on, and how easy it is to write conventional SQL. Then move into one of the ORMs for Python, perhaps SQLObject or SQLAlchemy. Discuss how data types are automatically converted, and how cross-platform the solution is. Highlight the different database engines supported, both open source and commercial.

------------------------------------------------------------------------

- ***Python and Object Databases***

  - Talk about how dynamic languages make a good match for object databases, with seamless serialization. Provide an overview of how an object database works, but focus on the end-developer and not the underlying mechanisms. Cover how the databases retain transaction support, and to what degree they provide support for the principles of ACID. Discuss the popular ZODB, Durus and APE frameworks, their tradeoffs (e.g. read-mostly usage, transaction rates) and the fact that they can be used standalone without the baggage of Zope or Quixote. Cover their lack of granular security and user identities at the database API level.

------------------------------------------------------------------------

- ***Handling Email with Python***

  - Perhaps as a two part article, cover the essentials of first parsing an incoming email and then generating an outgoing. Demonstrate how the email module makes it easy to handle multi-part email bodies and convert various character sets into unicode, which Python supports natively. Also cover how the email module supports the use of international message headers and handles their conversion between the 7-bit ASCII used on the wire. Show how the email module addresses the issue of date and addressee parsing. End with how the support of iterators makes it easy to walk over complex emails and touch upon the support added in Python 2.5 for writing email archives.

------------------------------------------------------------------------

- ***Image Processing, Array Numerics and Python***

  - Combine the use of the Python Imaging Library (PIL) module and one of the numeric modules and demonstrate how to effectively process large arrays of data, using images as something non-scientists can follow. Cover the array module, its strengths and weaknesses and then move on to the numpy/numeric/scipy framework. Note that this article could also be written using the processing of audio data instead.

------------------------------------------------------------------------

- ***Functional Programming in Python***

  - Provide an overview with examples of the functional programming features of Python. Cover the lambda, map and reduce functions but move on to the new all(), any() and generator/coroutine support in Python 2.5. Discuss the broad support Python iterators and the functionality in the itertools and functools (new in Python 2.5) modules. Lightly contrast the capabilities with existing functional programming languages like Haskell.

------------------------------------------------------------------------

- ***Mixing Network Protocols in Python***

  - Gradually assemble an example using the Twisted framework of how a single Python program can serve web pages as well as handle the telnet or imap/pop protocols. One idea is to create a telnet-based chat room, with the web page displaying a list of attendees and any icon/slogan they may have set on their avatar via the telnet interface. The Twisted framework is complex and powerful so the article needs to keep things simple in this introductory article.

------------------------------------------------------------------------

- ***Interacting with Python at the Prompt***

  - Introduce the read to the interactive nature of Python, not just the entering of expressions but use of the inspect module, how tracebacks are a programmer\'s friend and using the pprint module to display complex data structures.

------------------------------------------------------------------------

- ***Packaging your Python Application for Distribution***

  - Provide an introduction to the various packaging options for Python. Start with simple package imports and use of the zipimport module, work up to the distutils module and provide a light introduction to eggs. Wrap up with mention of the cheeseshop, what it is for and how to use easy_install to cryptographically sign and upload your work. Discuss briefly dependency resolution and perhaps compare it all to the CPAN network. Focus on what is needed to package an application and not on the underlying egg magic. Act like the reader is someone new to Python who has been given the task of packaging an existing application he didn\'t write.

------------------------------------------------------------------------

- ***Testing Your Python Program***

  - Introduce the reader to the test frameworks of Python. Cover the test and unittest modules, to show the conventional ways of building tests. Then progress to the doctest module, a more Pythonic approach, including both tests in the doc strings as well as those in standalone text files. For ideas/examples, look at how Zope3 has used text tutorial documents with embedded doctest expressions to combine teaching and testing. Consult the handouts from the Agile Testing tutorial at [PyCon](PyCon) 2006 for other ideas of what to cover.

------------------------------------------------------------------------

- ***Going International with Python***

  - Introduce the reader to the comprehensive support Python has for unicode. Cover the various codecs and the unicodedata and stringprep modules. Demonstrate use of the locale and gettest modules. Do something with the unicode, not just discuss it in an abstract manner. Perhaps show off a simple web server delivering unicode or an email generator.

------------------------------------------------------------------------

- ***Working at the Prompt - Shell Utilities in Python***

  - Reach out to the bash/awk/sed scripter. Start with the flexible parsing of command-line arguments we have in the getopt/optparse modules. Demonstrate line-by-line file processing, and cover the shutil and commands modules. For an advanced wrapup touch upon the curses module and how non-graphic apps can be quickly written in Python.

------------------------------------------------------------------------

- ***Processing Compressed Archives with Python***

  - Python has rich support for handling compressed files and archives. Demonstrate the gzip, zlib, bz2 modules for compressing single files and then advance to full archives, using the zipfile and tarfile. Wrap up with a demonstration of use, showing off the zipimport module.

------------------------------------------------------------------------

- ***Debugging and Profiling Your Python Code***

  - Talk about the power of the Python debugger, along with the profiler module and the (new for Python 2.5) cProfiler module. Contrast both the short-term ability to break on flexible conditions with the ability to profile code over the long-term. Discuss code coverage functionality and end with mentions of some of the IDE environments for Python that make some of this even easier.

------------------------------------------------------------------------

- ***Writing a Web Client with Python***

  - Walk the reader thru the creation of a program to fetch content from a website, starting with simple HTML text, adding basic/digest authentication, cookie support and SSL certificate checking. Also discuss having this program talk thru a web proxy ala SOCKS and briefly cover parsing the retrieved page using one of the DOM modules. This article would cover a lot of the API in the urllib2 module. Also show use of the robotparser module so that the client doesn\'t walk sites it should not.

------------------------------------------------------------------------

- ***System Administration with Python***

  - Highlight the useful Windows system administration tasks that can be achieved through Python - registry editing etc.

------------------------------------------------------------------------

- ***Getting Graphical with Python***

  - Start with the Python Imaging Library (PIL) introducing low-level graphic capabilities, then SDL and Pango/SVG. Continue moving up the spectrum thru OpenGL and into control of graphic applications such as Blender and GIMP. Also bring in several of the scientific graphing and visualization frameworks.

------------------------------------------------------------------------

- ***Making Things Add Up with Python***

  - An odd topic perhaps, but it would be cool to cover the various ways that Python can represent numbers. Introduce the integer / long integer pair, how conversions are automatic and then roll in the decimal module. Step up then to the [NumPy](NumPy) framework and how vast arrays can be efficiently handled in Python. Then cover the rational and units module for Python and end with an overview of one of the symbolic algebra modules for Python. An article for the language or math geek, to be sure.

------------------------------------------------------------------------

- ***PyPI (Cheeseshop) Introduction***

  - Introduce the PyPI catalog to users: how to search it, how to register your Python packages and upload files.

------------------------------------------------------------------------

- ***Deploying Python Desktop Applications***

  - Narrate packaging and writing an installer for a Python program. Important notes: Existing Python installations, additional libraries, managing upgrades and patches, various OS coverage. Bonus: Services

------------------------------------------------------------------------

- ***Connecting Python to External Devices***

  - Narrate how Python can interface a hardware device beyond the parallel and serial port and HID keyboard and joystick events. Ideally a USB IO device, either high level general purpose libraries from USB HID or bulk based IO devices to more complex driver and system interaction. Most noteworthy is how to handle device and data availability via a polled or event based management. LibUSB is a start\...

------------------------------------------------------------------------

- ***Complex Python Desktop Application IO***

  - Explore Python desktop application approaches that present a desktop user interface component while also carrying a server or persistent network connection, or interface to an IO device.

------------------------------------------------------------------------

For active discussion on advocating the use of Python, please join the [Advocacy mailing list](http://mail.python.org/mailman/listinfo/advocacy) and visit the [Advocacy - Get Involved!](http://advocacy.python.org/getinvolved) site.

------------------------------------------------------------------------

[CategoryAdvocacy](CategoryAdvocacy)
