# CodingProjectIdeas/StandardLibrary/RestructuredStandardLibrary

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# A Restructured Standard Library 

Despite the continuous introduction of many new language features to Python, and compounded by the steady addition of new modules to the standard library over the years, the structure of the Python standard library has remained relatively static throughout most of Python\'s lifetime until the present day. However, new additions to the library have made the selection of appropriate library facilities relatively difficult, even for experienced developers. For example:

- Does one choose urllib or urllib2 to open connections to remote resources?
- Is popen2, commands or subprocess the best module to choose to manage spawned processes? What are the trade-offs?
- Why is URL parsing done in urlparse and not in urllib?

A persuasive argument once upon a time was the simplicity of the Python standard library\'s layout in comparison to the \"aggressively hierarchical\" layout of the standard Java APIs, for example. But with a large number of overlapping modules and packages within the Python standard library reducing its relative coherency to Java\'s API proliferation (see java.sun.com for details), it seems appropriate to perform a reorganisation of the library\'s layout in order to promote a more memorable and intuitive structure that can be more coherently documented.

## A Note on Backward Compatibility 

One argument against reorganising the standard library is that \"if you ignore them, they won\'t bother you\" - that is, the presence of many apparently haphazardly named modules is not a problem unless you need to import many of them. Fortunately, this observation can be used to work in favour of a reorganisation: the old module and package names can be retained in addition to a new layout, existing software will continue to work by importing modules via their old names, improved documentation can focus on the new layout, reference material describing the old layout could also be provided to assist those working with older software. One disadvantage might be the additional space requirement of two different library layouts, however. Another disadvantage, more serious than the first is the case where a top-level module is replaced by one with the same name but with different functionality; strict backward compatibility measures would be necessary to avoid migration issues in such cases.

# Potential Areas of Improvement 

The following sections present observations about the current situation and possible recommendations for future editions of the standard library.

## Activities, Grouping and Redundancy 

The current standard library employs many modules as siblings at the top level of a relatively shallow namespace hierarchy. Many modules have been introduced to remedy, augment or partially replace existing modules, leading to problems of redundancy and incoherency. However, a policy of preserving APIs which resemble \"system\", \"native\" or \"platform\" APIs has also been maintained, leading to the provision of numerous functions and abstractions in modules such as os, select, mmap, errno, getopt, and so on.

### Overlapping Module Groups 

The following groups of modules exhibit overlapping functionality:

- email, rfc822, mimetools, mimify, multifile
- HTMLParser, htmllib (see below)
- commands, subprocess, popen2
- urllib, urllib2 (see below)
- datetime, time, calendar

Modules in the above groups would be consolidated either within a single module or organised into a more intuitive package layout in a restructured standard library.

### Functional Module Groups 

The following groups of modules may intentionally provide similar functionality through different implementations, or may provide complementary functionality that belongs within a common \"functional group\":

- StringIO, cStringIO (different implementations)

- [UserDict](./UserDict.html), [UserList](./UserList.html), [UserString](./UserString.html) (common theme: built-in type emulation)

- base64, binhex, binascii, quopri, uu (common theme: encodings)

- HTMLParser, sgmllib, htmllib (common theme: HTML/SGML parsing)

- anydbm, whichdb, dbm, gdbm, dbhash, bsddb, dumbdbm (common theme - database file access)

- cPickle, pickle, copy_reg, marshal, shelve, pickletools (differing implementations, common theme: persistence)

- optparse, getopt (common theme: command line options)

- readline, rlcompleter, cmd, shlex, code (common theme: interpreter I/O)

- codeop, compiler, py_compile, compileall (common theme: code generation)

- pwd, spwd, grp, crypt, nis (common theme: authentication)

- asyncore, asynchat, wsgiref, BaseHTTPServer, SimpleHTTPServer, CGIHTTPServer, SimpleXMLRPCServer, DocXMLRPCServer (common theme: network and Web programming)

- asynchat, urllib, urllib2, urlparse, httplib, ftplib, gopherlib, poplib, imaplib, nntplib, smtplib, telnetlib, xmlrpclib (common theme: network client programming)

- audioop, aifc, chunk, sunau, wave, sndhdr (common theme: audio)

- imageop, rgbimg, imghdr (common theme: images)

- textwrap, formatter (common theme: text formatting)

- zlib, gzip, bz2, zipfile, tarfile (common theme: archiving)

- hashlib, hmac, md5, sha (common theme: cryptography)

- mailcap, robotparser, netrc, [ConfigParser](ConfigParser) (common theme: configuration, albeit with specific and generic cases)

Modules in the above groups would be placed in intuitively named packages, possibly with improved names.

### Recommendations 

Just as the current standard library documentation divides the modules into particular groups, albeit with only moderate success, the above functional groupings could be used to define package boundaries that are more useful in distinguishing between different activities. A cursory review of the above could suggest the following set of packages:

- archive
- audio
- authentication (or auth, account)
- client
- compiler
- commandline
- configuration (or config, preferences, prefs)
- cryptography (or crypto)
- database
- encoding
- image
- interpreter
- parsing
- persistence (or persist)
- server
- text
- types

The names employed above may not be entirely suitable, and due to the ambiguity of certain category names, it might be appropriate to establish packages with certain names (eg. parsing) within other packages (eg. compiler), thus providing a level of context (eg. Python source code parsing, as opposed to HTML/SGML parsing). One inspiration for top-level category names could be the MIME media type hierarchy which uses such names as application, audio, image, text, and so on, although enthusiasm for replicating that hierarchy would need to be restrained in areas beyond file type handling.

The issue remains of providing access to \"system\", \"native\" or \"platform\" APIs, especially since developers with a systems programming background may wish to make use of such APIs in preference to others, possibly to implement other abstractions or to maintain compatibility with (or resemblance to) other works. We may decide to retain a package for such APIs and not to remove them entirely from the standard library, despite the duplication of functionality that this might suggest.

## Naming 

The current standard library employs a number of naming conventions:

- string, calendar (simple singular words)

- types, collections (simple plural words)

- struct, re, repr (foreshortenings and acronyms)

- textwrap, unicodedata (combinations of simple words)

- stringprep, fpformat (combinations of foreshortenings and acronyms)

- difflib, httplib (lib-suffixed names, often using foreshortenings and acronyms)

- StringIO, [UserDict](./UserDict.html) (mixed-cased variants of combinations)

- rfc822, netrc (specific references to specifications or technical details)

- copy_reg, dummy_thread (combinations involving underscores)

### Recommendations 

In order to simplify the recollection process, names should follow a consistent naming scheme, arguably favouring descriptive names which mention the nature of the activity supported. We might decide to permit only lower-case characters, together with numbers (only where absolutely necessary), although this can often appear confusing with acronyms and word combinations (eg. stringio, cstringio). However, since the use of acronyms may potentially be relegated to the level of class names, we may at that level employ mixed-case class names, along with upper-case acronyms as apparently tolerated by [PEP 8 \"Style Guide for Python Code\"](http://www.python.org/dev/peps/pep-0008/). Thus, StringIO.StringIO would not become stringio.StringIO, but perhaps something like stringfile.StringIO or something even more descriptive.

In some situations it may be advisable to retain technical names instead of employing names which obscure the purpose of the module. For example, the base64 module refers to a specific kind of encoding, but any invented descriptive name for this module may prove be verbose and yet fail to accurately communicate the same information.

## Top-level Organisation 

Currently, the standard library \"owns\" a number of top-level module names; indeed, since the library is relatively flat, a large number of module names are effectively reserved. Here is some anecdotal evidence of the confusion caused when standard library names are inadvertently chosen for other things:

*\"Some care is required in picking a name for the application. I thought \'calendar\' would be a good name for a test application - but it turns out that this conflicts with the Python calendar library.\"* \-- [Comment on the Django tutorial](http://www.djangoproject.com/documentation/tutorial1/#c2363)

### Recommendations 

In a standard library organisation where no encapsulating top-level package exists (eg. std), care must be taken not to conflict with existing or likely independent package names. One potential conflict involves the config package, already registered in the Python Package Index. A solution may involve minimising the footprint of the library by creating as few packages as possible and by giving those packages distinct, meaningful, and possibly unlikely names.

Alternatively, an encapsulating top-level package could be chosen, with a name like one of the following suggestions:

- common
- lib (or library)
- py (or python)
- std (or stdlib, standard)

## Module Functionality 

The diversity of module naming provides an \"archaeological\" guide to the accumulation processes operating within the standard library, yet more fundamental changes in style, recommended practices and techniques exist within the code of the modules themselves. Since the results of such differing implementation techniques manifest themselves as differently organised class hierarchies or interaction patterns, users of standard library modules must often master styles of usage which are often unnecessarily complicated for the task at hand or which diverge from previously accepted abstractions for similar tasks.

However, for certain kinds of tasks it is appropriate to employ differing approaches and thus expose differing representations to users. For example, the choice of XML parsing module may involve trade-offs with respect to resource usage, convenience and performance, and no single approach is likely to satisfy the needs of all users.

### Styles of Organisation/Interaction in Modules 

The following styles of class organisation or interaction patterns appear in the standard library:

- Abstract superclass plus handler subclasses (sgmllib)

- Abstract superclass plus handler subclasses and separate processor classes (compiler, BaseHTTPServer)

- Static mix-in hierarchies ([SocketServer](./SocketServer.html))

- Dynamic mix-in hierarchies (urllib2)

The following styles of behaviour configuration are employed in the standard library:

- Module-level globals to change module function behaviour (calendar, urllib)
- Functionality registration mechanisms (copy_reg, xml.dom)
- Environment variable access (urllib2)

### Recommendations 

Clearly, a diversity of patterns, mechanisms and styles are necessary to provide different approaches to particular tasks (as noted above). However, the revision of certain approaches and the subsequent \"archaeological\" accumulation of modules suggests that contributors have not been able to settle, at least initially, on a style widely regarded as being satisfactory to many standard library users.

An interesting example of evolving styles, as well as a number of peculiarities in the APIs provided, can be found in the urllib and urllib2 modules. Here, a moderately simple initial API has evolved into a more complicated (and presumably more powerful) subsequent API, but despite the conveniences provided in \"loading up\" the configured objects with specific handler functionality in advance, an alternative might involve \"flattening\" the style of interactions by having users process responses explicitly using separate objects or functions.

# Proposals 

The most natural starting point for the definition of a restructured standard library is the package hierarchy itself. Taking the grouping recommendations into consideration, in order to identify broad categories, and taking the naming recommendations into account, we might define a more complete hierarchy:

- account (or authentication)
  - groups (replaces grp)
  - nis
  - passwords (replaces pwd, spwd)

- archive
  - bz2
  - gzip
  - tar (replaces tarfile)
  - zip (replaces zipfile)

- audio
  - aiff (replaces aifc)
  - au (replaces sunau)
  - chunk
  - header (replaces sndhdr)
  - raw (replaces audioop)
  - wav (replaces wave)

- client
  - ftp (replaces ftplib)
  - gopher (replaces gopherlib)
  - http (replaces httplib)
    - cookie (replaces cookielib - see also net.cookie)
  - mail
    - imap (replaces imaplib)
    - pop (replaces poplib)
  - nntp (replaces nntplib)
  - smtp (replaces smtplib)
  - telnet (replaces telnetlib)
  - url (replaces urllib, urllib2)
  - xmlrpc (replaces xmlrpclib)

- compiler
  - code (replaces parts of compiler, codeop, py_compile, compileall)
  - parsing (contains compiler parsing functions, replaces parser)
  - lexing (contains symbol, token, tokenize)

- commandline
  - getopt
  - options (replaces optparse)

- crypto
  - hash (replaces hashlib)
  - hmac
  - md5
  - sha

- database
  - anydbm (includes whichdb)
  - bsddb
  - bsddbm (replaces dbhash?)
  - dbm
  - dumbdbm
  - gdbm

- datetime
  - calendar (includes sched?)

- decimal

- email
  - message (replaces email, rfc822, mimetools, mimify, multifile)
  - mailbox (includes mailbox contents)
    - mh (replaces mhlib)

- encoding
  - base64
  - binascii
  - binhex
  - quopri
  - struct
  - unicode (replaces encodings, stringprep)
  - uu

- files (replaces os.path, possibly tempfile, stat)

- image
  - header (replaces imghdr)
  - raw (replaces imageop)
  - rgb (replaces rgbimg)

- interpreter
  - generic (replaces cmd)
  - python (replaces code)
  - readline (includes rlcompleter)

- io
  - curses
  - logging
  - unicode (replaces codecs)

- math
  - complex (replaces cmath)
  - operator

- net
  - async (includes parts of asyncore, asynchat)
  - cookie (replaces/includes parts of cookielib, Cookie dealing with representations)
  - url (replaces urlparse)
  - xdr (replaces xdrlib)

- persistence
  - marshal
  - pickle (replaces/combines cPickle, pickle, copy_reg, pickletools)
  - shelve

- preferences
  - mailcap

  - netrc

  - generic (replaces [ConfigParser](ConfigParser))

  - robots (replaces robotparser)

- random

- runtime (replaces sys)
  - atexit
  - context (replaces contextlib)
  - fp (replaces fpectl)
  - gc
  - importers (replaces imp)
    - zipimport
  - inspect
  - locaters (replaces pkgutil, modulefinder, runpy)
  - site
  - traceback
  - user
  - warning (replaces warnings)

- server
  - http (replaces/combines BaseHTTPServer, SimpleHTTPServer)
    - cgi (replaces CGIHTTPServer, cgitb)
    - cookie (replaces Cookie - see also net.cookie)
    - wsgi (replaces wsgiref)
    - xmlrpc (replaces/combines SimpleXMLRPCServer, DocXMLRPCServer)
  - smtp (replaces smtpd)

- system (contains \"native\" or \"platform\" APIs)
  - locale
  - mmap
  - os (could be reorganised)
  - select (could be part of the network package)
  - stat (replaces stat, statvfs)
  - tempfile
  - time (may be obsolete)
  - zlib (could be part of a compression package)

- text (replaces/includes string)
  - csv
  - diff (replaces difflib)
  - formatters
    - formatter
    - textwrap
  - gettext
  - html (replaces/combines htmllib, HTMLParser)
  - re (more specific than its text siblings, could be moved)
  - sgml (replaces sgmllib)
  - shellsyntax (replaces shlex)
  - xml (contains the top-level xml package)

- types (augments types, contains [UserDict](./UserDict.html) as dict, [UserList](./UserList.html) as list, [UserString](./UserString.html) as str)

  - array
  - collections
  - functional (replaces functools)
  - heapqueue (replaces heapq)
  - iterators (replaces itertools)
  - mutex
  - queue (replaces Queue)
  - set (replaces sets)
  - weakref

## Additional Categorisation 

Here, additional categorisation is introduced in order to distinguish between categories in different contexts. For example, http packages appear in both the client and server top-level packages. Instead of dividing the previously identified http category in this way, we might have decided to preserve a single http package and divide it into client and server subpackages. However, as suggested above, we regard the client and server categorisations as being more important than one of many technologies that may be relevant to both of these categorisations.

## Difficult Categories and Packages 

Some categories may be established at the top level despite their nature suggesting a placement in some other category. For example, the email package could in certain respects be placed in either the archive or text packages, but since this might appear counterintuitive to different users of the package, a separate placement hopefully eliminates confusion and gives the package a deservedly more prominent status in the library.

Some modules or sections of functionality can be awkward to categorise. For example, the processing of URLs as attempted by the urlparse module could be placed in various networking categories or in some other category, since URIs/URLs are also used in contexts unrelated to networking and the Internet (eg. in XML namespaces and RDF identifiers). A compromise may therefore be necessary, placing a proposed url module in the net top-level package, for example.

Some categories are difficult to justify from the selection of modules available. For example, an io package (input/output) may contain all modules involving things like streams and files, but it may be the case that such modules belong elsewhere, or perhaps the name of such a top-level package should be more suggestive, such as files or streams, even if such names are arguably too specific or start to cover other topics: a files package might include file metadata processing, too.

## System Packages 

As noted above, a special \"system\" (\"native\" or \"platform\") package could be established. Care should be taken, however, to avoid filling such a package with other packages that really ought to be disassembled, reorganised or recategorised.

## Runtime Packages 

The current standard library has a sys package along with other auxilliary packages which affect the behaviour of the runtime system. It is suggested that these packages be available under the runtime top-level package. Although sys might be a more compatible name with existing programmers\' expectations, if that name were to be preserved, the system package would need to take one of the other proposed names instead.

## Editorial Notes 

This is currently a draft, featuring a number of points that should be discussed rather than being interpreted as a final opinion or a final set of recommendations. \-- [PaulBoddie](PaulBoddie)

## Open Issues 

1.  Should there be a top-level package representing the entire standard distribution, e.g., \"std\"? `from std.database import anydbm` \-- [SkipMontanaro](SkipMontanaro)

    - *I think the proposed hierarchy (which is obviously tentative) should be at the top level, although the risk of name collisions with independent packages and the issue of how \"selfish\" the standard library should be ought to be worked out.* \-- [PaulBoddie](PaulBoddie)

    - *It\'s not obvious to me that putting all these package at the top level will improve matters significantly. On the one hand, people have been living with the current flat standard module namespace and using names that avoid collisions. By creating a bunch of top-level packages that avoid the current names you run the risk of stomping on names others have selected for their own use (text, config, audio, image, database all seem like names people might have chosen). By giving Python its own one package namespace you avoid most of that.* \-- [SkipMontanaro](SkipMontanaro)

    - *It\'s a trade-off to avoid Java-style deep hierarchies: we could move the xml package up out of the text package, but would we then want it under std? Perhaps a conservative set of names is best: put client and server under net, for example, but reserve things like audio and image. I suspect that generic standard library names are least likely to collide with published packages (and only config from the suggested names seems to do so), and there\'s an argument that the standard library provides definitive answers: the archive package is **the** archive package for Python. Would prefixing such solutions with std not add \"conceptual boilerplate\"?* \-- [PaulBoddie](PaulBoddie)

    - *Would it make any sense to have a few top-level slots for people\'s packages? Things like \"pypi\" and \"local\" or \"optlib\", \"ext\" and \"user\" (or \"spkg\" only), so that non-std packages (which I assume will be less used than the standard lib) carry the burden of deep hierarchies. It would also allow for easy hooks for some \"separated Python environments\" functionality and would extend the organization down to site-packages (e.g. PIL and numpy are de facto \"optlib\", my own dirty scripts are \"local\" or \"trash\"). And if someone really needs some special module in the top-level, a simple **mv** hack should be enough.* \-- ajaksu

    - *The danger of having user, local, trash and other subjective packages is that as soon as you promote your work to something non-dirty, you have to go and change all the imports. And people are likely to forget to do this when releasing their code, too. Of course, definitive naming in the Java world involves strict hierarchies which use Internet domains (apart from Sun\'s stuff, understandably, and Oracle\'s stuff, not so understandably), but this just produces long branches. I guess people would just have to do due diligence before choosing names, but this isn\'t a different situation to what we have now. Still, \"non-functional\" categories at the top-level is an interesting idea.* \-- [PaulBoddie](PaulBoddie)

2.  Should client and server be under net? Would this be too much of the obvious? \-- [PaulBoddie](PaulBoddie)

3.  Should encodings be under text or merged with text? \-- [PaulBoddie](PaulBoddie)

4.  Is the io package too weak? Things like XML parsers do I/O and they\'re probably best in the text package (or their own top-level package). \-- [PaulBoddie](PaulBoddie)

    - *I question whether the xml package belongs in text. Lots of people use XML for stuff other than HTML on steroids.* \-- [SkipMontanaro](SkipMontanaro)

    - *Yes, it\'s something which is potentially important enough to have its own category.* \-- [PaulBoddie](PaulBoddie)

5.  Are the io package and files package too close in purpose? Could things like tempfile (with a nicer API) be part of the files package? \-- [PaulBoddie](PaulBoddie)
