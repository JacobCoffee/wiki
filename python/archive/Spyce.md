# Spyce

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

A framework for [WebProgramming](WebProgramming).

### Masthead 

URL

:   [http://spyce.sf.net](http://spyce.sf.net)

version

:   2.1.3 (*2006-11-17*)

licence

:   OSI approved licence - open source. (See [http://sourceforge.net/projects/spyce/files/spyce/](http://sourceforge.net/projects/spyce/files/spyce/) )

platforms
:   Spyce should work on most platforms.

Python versions
:   2.3 or later.

### Deployment Platforms 

- Integrated with Apache using mod_python or with any Web server using CGI.
- With CGI, the lifespan of a program is determined by the Web server, but mod_python should provide long-lived processes.

### Suitability 

The deployment of applications using CGI is usually permitted in all but the most restrictive hosting environments. The use of mod_python may be more appropriate to in-house deployments or more comprehensive hosting environments.

### Development Interfaces 

- Python code inside HTML documents - comparable to ASP, JSP and PHP.
- Spyce modules can be written in Python to provide extra functionality.

### Environment Access 

- Access to resources is primarily done using the Python module system and other general environment access techniques.

### Session, Identification and Authentication 

- Support for sessions which identify users is included, currently only with filesystem support for stored session information, although SQL-based storage seems to be planned.
- No explicit authentication support seems to be included.

### Persistence Support 

- Apart from session information, no persistence mechanisms are included.

### Presentation Support 

- The embedded Python code concept gives a certain flexibility in presentation.
- The Cheetah templating system is explicitly supported through a Spyce module.

Other presentation systems could presumably be used instead, given the ability to use other Python modules in the framework.

### InTheirOwnWords 

### Comments 

Spyce addresses many areas of interest to Web application developers within a widely-known \*SP paradigm: sessions, pooled objects, templating, and so on. Some novel features are also supported: automatons, for example, which attempt to encapsulate multi-stage transactions (or \"application flows\" as the documentation calls them). However, by design, Spyce does not attempt to provide everything - it aims to do dynamic Web content generation well and integrate with other things easily (see [http://spyce.sourceforge.net/](http://spyce.sourceforge.net/)). Moreover, it can also be used as a standalone processing tool completely outside a Web application environment. \-- [PaulBoddie](PaulBoddie)
