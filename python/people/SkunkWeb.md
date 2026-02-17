# SkunkWeb

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

A framework for [WebProgramming](WebProgramming).

### What It Is 

SkunkWeb is a scalable, extensible, and easy-to-use Web application server written in Python. It is designed for handling both high-traffic sites and smaller sites. Its features include a powerful component model and an elegant templating language that encourages component-based design, highly configurable caching (on disk and/or in memory) of compiled templates and component output, message catalog support for i18n, and remote component calls. It can be used with Apache via an Apache module, or it can serve HTTP requests directly.

### Masthead 

URL

:   [http://www.skunkweb.org](http://www.skunkweb.org) (main site, but domain expired); [http://wiki.skunkweb.org](http://wiki.skunkweb.org) (SkunkWeb Wiki)

version

:   3.4.0 (*2004-09-10*)

licence

:   your choice of [GPL](http://www.fsf.org/copyleft/gpl.html) or the SkunkWeb License (a BSD license).

platforms

:   SkunkWeb works on UNIX platforms, including Linux, FreeBSD, MacOS X, Solaris, HPUX, and on Windows with the Cygwin environment (the latter is not recommended for production).

Python versions
:   2.1.1 and later (some optional libraries require 2.2 or later)

### Deployment Platforms 

- Integrated with the Apache Web server using the mod_skunkweb adapter, fcgi, scgi, or a CGI program which communicates with the SkunkWeb environment. Other webservers that support fcgi, scgi or cgi should also work.

- SkunkWeb can be run as a standalone http server instead, removing the need for Apache.

- The SkunkWeb environment is provided by long-running processes.

### Suitability 

The requirement for Web server adapter integration, or the running of a standalone server, rules SkunkWeb out for more limited hosting environments. However, where such deployment is possible, the performance should be satisfactory, given that this is clearly a priority of the developers.

### Development Interfaces 

- Presentation-oriented - one of the stated benefits of SkunkWeb is the STML template language, which is extendable with Python-based components. A PSP templating language is also available, and other templating systems (Cheetah, ZPT) could be plugged in, in addition to straight Python.

- It is easy to extend the server with custom services that affect how requests are handled.

- Applications can be deployed as SkunkWeb \"Products\", archives containing SkunkWeb components and Python modules (including SkunkWeb services, which get loaded at server startup).

### Environment Access 

- SkunkWeb uses plain text configuration files to specify resource locations.

- Additional functionality could be included in SkunkWeb applications using the Python module system - service components could import modules to access such functionality.

### Session, Identification and Authentication 

- SkunkWeb supports sessions, with both filesystem and SQL-based database system stores being provided; their use is entirely optional.

- Cookie and basic authentication support is provided, and the authentication system is easily extensible.

### Persistence Support 

- SkunkWeb includes the [PyDO](PyDO) object-relational mapper.

- Database connections for [PostgreSQL](PostgreSQL), [MySQL](MySQL), [Oracle](Oracle) and [Firebird](Firebird) can be cached (not pooled).

- SkunkWeb has a well-considered and high-performance caching system that is easily controllable on a per-component basis.

### Presentation Support 

- [STML](./STML.html) - a template language which uses special tags in order to control the final Web page output, and calls components written in Python or [STML](./STML.html) that can either write output or return Python data. Top-level documents can also be written in Python.

- Python Server Pages - a [PythonInWebPage](PythonInWebPage) presentation technology supplied with SkunkWeb (as of version 3.3)

- Python - in lieu of a templating language, straight Python can be used.

### Comments 

The SkunkWeb archive package contains formatted documentation (HTML, [PostScript](PostScript), PDF and DVI); the latest version can always be downloaded, from [http://skunkweb.sourceforge.net/](http://skunkweb.sourceforge.net/). The installation process is somewhat more involved than with other packages, but should be straightforward enough to anyone used to installing GNU autoconf-based packages.

The SkunkWeb developers emphasise performance and give caching, process forking and template precompilation as features which differentiate SkunkWeb from other frameworks and application servers; internationalisation using message catalogues is another feature which other frameworks do not provide or emphasise highly. Unlike many Python-based frameworks, Until version 3.4b3, SkunkWeb was licensed solely under the GPL, at which some in the community caviled; it is now also available under a BSD-style license.

- \-- [PaulBoddie](PaulBoddie) (with some additions [InTheirOwnWords](InTheirOwnWords))
