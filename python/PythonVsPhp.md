# PythonVsPhp

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# Python vs. PHP 

This page was copied mindlessly from [http://wiki.w4py.org/python-vs-php.html](http://wiki.w4py.org/python-vs-php.html) ([Google Cache](http://72.14.203.104/search?q=cache:bo4LWB1ZHswJ:wiki.w4py.org/python-vs-php.html+php+vs+python&hl=en&gl=us&ct=clnk&cd=1))

------------------------------------------------------------------------

## Common Ground 

Both PHP and Python:

- are interpreted, high level languages with dynamic typing

- are [OpenSource](OpenSource) (except where various [Zend products](http://www.zend.com/products), recommended by some, are employed)

- are supported by large developer communities

- are easy to learn (compared to C++, Perl)

- are easy to extend in C, C++ and Java

- are extremely portable. They run on almost all platforms in existence without recompilation.

- support for variable number of function arguments.

- have the ability to freeze live objects in a string representation (for storing arbitrary objects on disk, moving them over the network, etc); they can then be converted back to identical objects with data intact. PHP\'s serialize function; Python\'s pickle and marshal modules. Note that PHP, handling of serialized objects and classes is much weaker and error prone than Python\'s due to PHP\'s lack of modules. When an object is serialized, only its attributes are stored, not its methods. Thus, the object\'s class must be present (with the exact same name) in the script that unserializes it. In Python this is handled automatically via the module/import framework. (this COULD be handled with PHP 5\'s autoload(), but is not done automatically)

- support namespaces

- support for docstring (pydoc / reflection + phpDocumenter)

- support method chaining

- have several debuggers and IDEs

- support for dates that aren\'t limited to UNIX timestamps (\<1970, \>2038)

- built-in support for cached byte-code (built-in support was added in PHP5.5)

- have a standardized database API

- support GTK and QT

- support lambdas and other builtin functional programming constructs

- have a single statement (unset/del) for all data types

- can be used for scripting and general programming (CLI sapi, embedded etc., in the case of PHP)

## Compared as Languages 

### What strengths do PHP have that Python doesn\'t? 

- the \'switch\' statement and \'do \... while\' construct
- increment and decrement and assignment operators (assignment is a statement only in Python)
- the ternary operator/statement (\... ? \... : \...)
  - Retort: *Python 2.5 has [conditional expressions](http://www.python.org/dev/peps/pep-0308/)*
- an expedient (commonly installed) environment
- one array type that doubles as a list and a dictionary. Dictionary keys are iterated in their original order.
- private, protected and public modifiers for both properties and methods
- abstract and final modifiers for both classes and methods
- interfaces
  - Note: *However, as Python has multiple inheritance, there\'s less need for interfaces. Also Python 2.6 has introduced Abstract Base Classes.*
- variable variables
- default arguments in functions
- embedding in HTML
  - Note: *mod_python got this aswell.*
- a wide range of byte-code caches available

### What weaknesses does PHP have that Python doesn\'t? 

- (more verbose) syntax from C/C++ and Perl, with lots curly braces and dollar signs and \"-\>\"-s

- confused tableau of function names. The builtin library has a wide variety of naming conventions. Functions often have prefixes to denote their source (but often not). Functions are often placed into classes to simulate namespaces.

- a somewhat weak type system (not to be confused with dynamic types)

### What does Python have that PHP doesn\'t? 

- indentation is used to mark out block structure rather than curly braces
  - Retort: *PHP curly braces make it work with HTML more easy*

- modules

- Rules that help catching typos more; reading an undefined variable is an error, it\'s not silently treated as if it was null.
  - Retort: PHP will issue E_NOTICE. This will be shown in a develop environment.
    - Counter-retort: It\'s still dangerous in production environment. As of the development, it\'s extra hassle to configure, watch logs, etc., when it could just stop, as you are supposed to eliminate these problems anyway. That PHP still has the more easy-going approach is probably because people have utilized undefined vars a lot in existing code base, so they couldn\'t fix this.

- a small core **(language or runtime?)**

  - retort: *it is not entirely true* **(substance needed)**

- very clear, concise, and orthogonal syntax

- keyword arguments (i.e., parameters passed by name instead of by position) to functions and methods, easy support for default arguments
  - Retort: *PHP have default arguments*

    - Counter-retort: *Defaults are much less useful without keyword arguments*

- true object orientation and \'first class\' classes and functions
  - Retort: *OO has been completely revamped in PHP 5*

    - Counter-retort: *But it\'s still painful, obviously a hack*

- classes are used extensively in the standard library
  - Retort: *PHP 5 has SPL which is fully class-based*

- multiple inheritance

- object-oriented file handling

- excellent introspection
  - Retort: *PHP 5 Reflection*

    - Counter-retort: *We said **excellent** introspection*

- everything is a reference! (references are painful in PHP)
  - Retort: *Not in PHP 5*

    - Counter-retort: *note that arrays are still passed around by value (unless you add an explicit &)*

      - Retort: You won\'t accidentally modify it.

- consistent case sensitivity (PHP functions are case insensitive, but variables are case sensitive)

- a simple array slicing syntax

- iterators
  - Retort: *in PHP 5*

- structured exception handling
  - Retort: *in PHP 5*

    - Counter-retort: *where are PHP 5\'s equivalent of else and finally?*

    - Counter-retort 2: *unfortunately most standard PHP functions don\'t use exceptions for reporting errors, which makes structured exception handling much less useful*

      - \'finally\' made it in PHP 5.5

- operator overloading
  - Retort: *In PHP you can use runkit extension to emulate the same feature*

    - Counter-retort: \"In PHP you have to use runkit extension to emulate the same feature\"

- SWIG integration

- threading
  - Retort: *Python have Global Interpreter Lock so it\'s not really parallel*

- \"with \... as\" statement to deal with resources that need closing reliably and concisely

- an excellent profiler
  - Retort: XDebug, a debugging and profiling extension, that supports both PHP4 and PHP5 is extremely popular

- lots of high-level data types (lists, tuples, dicts, [DateTimes](./DateTimes.html), [NumPy](NumPy) arrays, etc.)

  - Retort: *PHP had SPL Types which is included in PHP5 as a standard library*

- differentiation between arrays (lists) and associative arrays (dictionaries).
  - Retort: *PHP array is more flexible. In case developer want a true array, just use [FixedArray](./FixedArray.html) in PHP SPL*

- support for all major GUI frameworks

- strong internationalization and UNICODE support
  - Retort: *[PHP 6](http://wiki.pooteeweet.org/PhP60) will include Unicode support. This feature is available in PHP5.2 and PHP5.3 via intl extension which can be found at pecl.php.net*

  - Retort: *PHP have mbstring for Unicode*

- tends to lead to much more scalable applications \-- importing modules is safer than textually including code as in PHP: global variables are not used to exchange information.

## Compared as Web Development Frameworks 

Unlike PHP, which has web development features built directly into the core language, Python\'s web development capabilites are provided by add-on modules. Basic CGI capabilities are provided by the \'cgi\' module which comes in Python\'s standard library. There\'s also a wide range of third-party modules available for Python; some are complementary, others compete. As a result, Python provides a more flexible base for web development.

There are some adverse side effects of this flexibility. First, the range of choices can be bewildering. Unless you are working experienced Python web developers, PHP is easier to get started with. Second, support for PHP is more common with shared-hosting companies than support for the various Python options.

Another difference is that PHP is embedded in the web server, whereas Python web applications can either be embedded in the web server like PHP or run in a separate process. Here\'s a simple classification of Python web development platforms:

- emdedded in the web server process
  - Apache modules (eg. mod_python) embed the Python interpreter in Apache and allow other Apache modules to be written with Python. This is the same idea as mod_perl.
  - PyWX is an extension to AOLServer that serves the same purpose as the Apache modules above.
  - MS ASP scripts can be written using Python via Active Scripting Host.
- running in a separate process
  - non-persistent process (a new process is spawned for each request)
    - custom CGI scripts
  - persistent process (all requests are sent from the web server to one persistent process)
    - custom Fast-CGI scripts

    - \'Application Servers\' (eg. Zope, Webware, [SkunkWeb](SkunkWeb))

(Note: It\'s *possible* to write a long-running server in PHP, but there are precious few examples of it.)

The vast majority of Python Web applications are run in a separate process. This has some important implications.

## Security 

PHP has historically had a horrible history when it comes to security. See the following article as an example: [http://old.lwn.net/2001/0704/a/study-in-scarlet.php3](http://old.lwn.net/2001/0704/a/study-in-scarlet.php3) (Note: This article was published 10 years ago, and is no longer valid for more than an idea of PHPs history with security).

## Community Support 

### PHP 

- huge installed user base, but the figures are probably distorted by shared hosting
- low signal-to-noise ratio \-- because PHP is so expedient, many of the users are not invested in the technology (or even their own code) or the community

### Python 

- sizable, but not huge, installed user base
- Python Software Foundation
- lots of specialized interest groups
- very high signal-to-noise ratio

## Commercial Support 

### PHP 

- [http://www.zend.com](http://www.zend.com/)

### Python 

See the [CommercialServices](CommercialServices) page for more information.

## Documentation 

Although both PHP and Python have excellent core documentation, Python\'s is more extensive and generally higher quality. PHP has a large number of translations available. Python doesn\'t. For PHP see [http://www.php.net/docs.php](http://www.php.net/docs.php) and for Python see [http://python.org/doc/](http://python.org/doc/) Python allows documentation on modules, classes, and functions to be included in the program code. The documentation becomes an attribute of the module/class/function, accessible from inside of the language itself. Python manual is really awfully structurized and presented compared to PHP manual, which uses cross-links, a lot of colorized examples and invaluable user comments to make it easier to comprehend the magic. PHP manual merges different versions of the language together making it a little bit bloated.

## Editorial Notes 

Given the copy-and-paste origins of this document, along with the age of the original document, the text has been somewhat incoherent. Several changes have since been made to tidy up the text, drop redundant content (old comments which can be viewed in the original document, links to outdated resources and content found elsewhere in this Wiki), and to focus the remaining content on the actual topic of the page.

## Constructive Criticism / Observations 

I came here for an objective comparison between PHP and Python but what I see is a document that is not only incorrect but is also heavily biased. I realize this is a Python site but that doesn\'t give editors (read anonymous visitors) carte blanche when it comes to facts. For example - it is claimed that unset is not uniformly used in PHP but in fact it works on variables, objects and arrays. Next is the comment about Python having a profiler, so does PHP. Other items that should not be in the section labeled things that Python has that PHP doesn\'t include: method chaining, classes are used extensively in the standard library, maturity, easy support for default arguments, debuggers and IDEs and that is just the beginning.

I don\'t see the harm in referring to future functionality because leaving it out implies that it isn\'t going to be available - for example the addition of namespaces and other features in PHP5.3 is going to be a nice step for the language and the release is imminent. That having been said, OOP in PHP is not complete IMO so I would like to see objective comparisons of OOP in PHP and OOP in Python which would be an enormous benefit to myself and others.

I don\'t want seem like I hate Python, I honestly have no notions whatsoever about it but I do not like coming to a comparison page between two languages and discovering that the comments cannot be trusted. The reason I came here at all was to decide if Python would be a good fit for future projects that I intend open source but I am leaving this site unsure of the true advantages that Python has to offer. In the spirit of helping people know the difference, I suggest that you collaborate with someone who has no bias.

### Editorial Response 

Given recent anonymous edits which say things like\...

*Python is too slow to be used in web apps*

\...and\...

*on PHP you can do this: if(\$a == \$b) { echo \"true\"; } else { echo \"false\"; } : try to do that whith Python*

- Tried: *print \"true\" if a == b else \"false\"*

- Retort: *echo (\$a == \$b) ? \"true\" : \"false\";*

\...the latter either referring to some deep magic or being exceptionally uninformed, I\'d rather not see everyone wanting to pile in with mud-slinging but actually have people who have used both technologies give their informed perspectives. The restrictions on editing existed because of spam, but the maintainers of this Wiki [reserve the right](WikiGuidelines) to enforce access controls if contributions deteriorate in quality. No-one can demand to edit a site like this without showing a degree of responsibility and sincerity. \-- [PaulBoddie](PaulBoddie) 2011-07-23 19:25:57

## Using Python and PHP together 

The [Embedded Python](http://pecl.php.net/package/python) [PECL](http://pecl.php.net/) extension \"allows the Python interpreter to be embedded inside of PHP, allowing for the instantiate and manipulation of Python objects from within PHP\". The PyPI [phpserialize](http://pypi.python.org/pypi/phpserialize/) package is \"a port of the serialize and unserialize functions of php to python\". [phppython](http://code.google.com/p/phppython/) \"is a php to python code converter that currently can: convert small php code snippets, functions to python code\". [WPHP](http://pythonpaste.org/wphp/) is a WSGI-\>PHP gateway that \"allows you to run PHP processes inside of Python, using a WSGI gateway\". Alternatively take a look at phpython [https://sourceforge.net/projects/phpython/](https://sourceforge.net/projects/phpython/), a Python interpreter written entirely in PHP, to be used without the aid of WSGI, CGI or FastCGI
