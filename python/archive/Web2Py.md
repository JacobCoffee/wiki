# Web2Py

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

A framework for [WebProgramming](WebProgramming).

### Masthead 

URL

:   [http://www.web2py.com/](http://www.web2py.com/)

version
:   1.82.1

licence
:   GPL

platforms
:   Unix, Windows, Mac

Python versions

:   \>= 2.4 \< 3.x

### Deployment Platforms 

mod_wsgi is preferred as it has full WSGI support, but also it can run with FCGI, etc. It also comes with a standalone Web server for development purposes.

### URL dispatching 

URLs are mapped directly to functions in a controller. No need to use regular expressions (although them can be used).

### Environment Access 

Web2py creates request, response and session objects that are globally available.

### All-in-One 

Web2Py comes with:

- An admin interface to design, edit, test and deploy totally via web
- A database administration interface to insert, update, delete and run queries.
- Ticket system to manage errors
- Authentication: supports groups, users and privileges.
- Integrated Ajax and jquery javascript support
- HTML Helpers, Menues, Validators, URL Mapper, etc.
- Webservices support (JSON, XML_RPC, AMF_RPC, SOAP)
- Many third party libraries (rss, rtf, etc.)
- etc\...

### Persistence Support 

Web2Py\'s provides a Data Abstraction Layer (similar to an object-relational mapper), currently supports PostgreSQL, MySQL, SQLite3, MSSQL, Oracle, DB2, Ingress, Informix, Firebird and GAE with some caveats. Web2py generates customizable CRUD interfaces directly from the tables. The automatic creation and migration of database tables is supported. The DAL can handle almost the 100% of the queries elegantly in a pythonic way resembling SQL (no need to know advanced POO or learn a new complex query language).

### Presentation Support 

Web2Py\'s has a python capable template language. It looks like this:

    {{if condition!=something:}}
    {{=title}}
    {{pass}}

### Documentation 

A [book](http://www.web2py.com/book) is available both printed/pdf and freely accessible via web, written by the lead developer, who is a University Professor.

Read the [web2py about](http://www.web2py.com/examples/default/what)
