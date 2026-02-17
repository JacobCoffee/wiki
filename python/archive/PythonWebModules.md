# PythonWebModules

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

A framework for [WebProgramming](WebProgramming).

### Masthead 

URL

:   [http://www.pythonweb.org](http://www.pythonweb.org)

Version

:   0.4.1 (*2004-09-13*)

Licence
:   LGPL (will consider BSD-Style or Python if LGPL is a problem)

Platforms
:   Windows, Linux, UNIX (not tested on MacOS but should work)

Python versions
:   Python 2.2 and above

Status
:   Beta (although the author uses it in commercial applications)

### Introduction 

These modules used to be known as the lemon modules. The CVS is still hosted at [http://lemon.sourceforge.net/](http://lemon.sourceforge.net/)

\"It is better to have a flexible module that can be used intuitively than an all-singing, all-dancing framework that no-one can be bothered to learn.\"

The Python Web Modules are a suite of simple and easy to use Python components desinged to allow developers to write Python CGI scripts or web applications with SQL databases, sessions, templates, email and authorisation functionality without having to install Web Application Servers.

A key part of the project is the creation of documentation and examples to allow developers with less time or expierince to understand the concepts of Python web programming without having to read all the sources and comments from the very beginning.

The modules can easily be used on shared web hosting accounts running Apache and Python for example.

### Getting Started 

First you need to download the latest relase from [http://www.pythonweb.org/projects/webmodules/release/current/](http://www.pythonweb.org/projects/webmodules/release/current/) and then read the getting started guide at [http://www.pythonweb.org/projects/webmodules/doc/current/html_multipage/overview/](http://www.pythonweb.org/projects/webmodules/doc/current/html_multipage/overview/)

### Session, Identification and Authentication 

Session handling is done through the web.session module as follows:

import web.session session = web.session.start( options\... ) session\[\'myVariable\'\] = \'This will be available at each request\'

The module supports cookies or cgi variables.

The use of the term \"session\" on its own can be confusing, especially in the context of the terminology of particular Web frameworks. Therefore, this document uses the following terms:

Identity and identification handling is achieved through the web.auth module which uses the web.session module to store its information. Users may have multiple access levels to multiple applicaitons. Login handling and password reminder code is handled automatically.

Both modules can either use a database supported by web.database or a file store to store the information between requests.

### Forms and Fields 

One of the more tedious tasks of web programing is creating HTML forms and validating field input. The web.form module allows you to create forms from Field objects. There are Field objects for all the standard HTML fields.

HTML generation and user input validation and requesting the user to correct errors are all handled by the Form object.

Fields also exist for the common Python objects such integers, string, datetime objects etc as well as email and URL fields. These fields convert the value chosen by the user in the form directly to the appropriate Python type so no conversion is required. A [DateTime](./DateTime.html) field returns a datetime.datetime object, an Integer field returns an integer. a [StringSelect](./StringSelect.html) field allows the user to choose one string from a choice and an [EmailCheckBoxGroup](./EmailCheckBoxGroup.html) allows the choice of one or more Email addresses.

### Database Support 

A major part of the project are the database modules.

The web.database module is a simple SQL abstraction layer which sits on top of a DB-API 2.0 cursor to implement data type conversions, provide database independance and offer a more Python-like interface to the data returned from queries.

Here are the main features of the module:

- 100% compatible with the underlying DB-API 2.0 cursor. A web.database cursor is also a DB-API 2.0 cursor.
- Provides methods including select(), insert(), update(), delete(), create(), alter() and drop() which build and customise the SQL depending on the database being used providing database independance.
- Provides strong typing for the data being used. No need to deal with SQL strings, the module automatically encodes and decodes data for the approriate column.

The web.database.object module is an object-relational mapper. It allows you to simply define complex database structures in Python code and then create the necessary tables automatically. It then allows you to manipulate the Python objects you have defined to transparently manipulate the underlying database including the facility to use multiple joins without knowing any SQL.

The feature which sets the web.database.object apart from rivals like SQLObject is that the Table column classes are derived from web.form.field objects which means you can transparently create HTML interfaces to edit the data structures through a web browser using the Table object\'s form() method with all validation handled for you. This makes web.database.object module ideal as a middle layer for writing data-driver websites although it has broader uses as well.

A database object can in theory have any storage driver (text, XML, SQL Datbase, DBM) although currently only a driver for the web.database module has been written. This means that any storage system with a driver for web.database can be used with web.database.object. This currently includes MySQL, ODBC, SQLite and, to an extent, Gadlfy.

More information is available in the module reference at [http://www.pythonweb.org/projects/webmodules/doc/current/html_multipage/lib/web.html](http://www.pythonweb.org/projects/webmodules/doc/current/html_multipage/lib/web.html)

### Presentation Support 

The modules support a number of presentation options including Dreamweaver MX, XYAPTU and simple \'%(value)\' style replacements. The preferred method of producing output is perhaps using Cheetah.

All templating using the parse() function. One example is:

import web.template

html = web.template.parse(type=\'cheetah\', file=\'test.tmpl\', dict={\'title\':\'Web Modules\'})

### Documentation 

Full documentation on the latest version of the software is availble at [http://www.pythonweb.org/projects/webmodules/doc/current/html_multipage/](http://www.pythonweb.org/projects/webmodules/doc/current/html_multipage/)

### Other Features 

Other features which make these modules stand out are plain and HTML email support, simple graph creation, full error handling and datetime compatibity classes for Python 2.2.

### Deployment Platforms 

The Web Modules were written because although there are quite a few web application frameworks available they are either too simplistic, or require adminster rights to install and so cannot be used with most shared hosting accounts.

The modules provide everything needed to write data-driven websites without needing installation or superuser rights. Included are database drivers and even a webserver so they should run on any computer or server which runs Python 2.2 or above. Currently the only pure-Python database supported is Gadfly and this has some limitations so ideally users should use MySQL or SQLite instead.

Developers can use the modules with other servers such as Zope or on their own but the author tends to use them in CGI scripts on Apache running on FreeBSD or Linux servers.

### Development Interfaces 

The modules are desinged to be used in any way you like. They do not tie you to a CGI way of working or a servlet architecture. You can use them as building blocks to create your own way of doing things.

If you prefer some help though the examples in the documentation assume for simplicity you are using a CGI approach.

The examples are listed at [http://www.pythonweb.org/projects/webmodules/doc/current/html_multipage/web/examples.html](http://www.pythonweb.org/projects/webmodules/doc/current/html_multipage/web/examples.html)

### Hosting 

Most UNIX hosts which support Python 2.2 or above and include a web.database supported driver such as MySQLdb will be an ideal platform for using these modules.

I use and would reccomend [http://www.gradwell.com](http://www.gradwell.com)

If you are after cheap hosting to have a play with that might break at any moment try [http://www.web-mania.com](http://www.web-mania.com)

### Future 

Future releases will also conform to the WSGI being discussed on the WEB-SIG mailing list at the moment. [Read the project plan](http://www.pythonweb.org/project/plan.html).

### InTheirOwnWords 

Although much of the functionality of these modules is replicated elsewhere, I believe this is the most complete set of modules available that doesn\'t tie you into using a particular architecture. In each component I have tried to go one stage further than other sofware available.

I would appreciate feedback, encouragement or comments if you have any to author \<at\> pythonweb.org.

### Comments 

This area is for comments and discussion with other Python Web Developers.. I\'d appreciate your thoughts.
