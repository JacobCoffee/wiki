# JonsPythonModules

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

A framework for [WebProgramming](WebProgramming).

### Masthead 

URL

:   [http://jonpy.sf.net](http://jonpy.sf.net)

version
:   0.10 (2011-05-26)

licence
:   Old-style Python licence - open source.

platforms
:   Jonpy should work on most platforms.

Python versions
:   2.2

### Deployment Platforms 

- Integrated with a Web server using CGI or FastCGI or [ModPython](ModPython).

- With CGI, the lifespan of a program is determined by the Web server, but the FastCGI deployment option requires processes to remain responding to requests, potentially indefinitely.

### Suitability 

The deployment of applications using CGI is usually permitted in all but the most restrictive hosting environments, and with support for session storage in databases or the filesystem included in the framework, this framework is indeed suitable for limited hosting accounts. The option to use FastCGI or modpython potentially lets applications take advantage of more generous environments with a corresponding increase in performance.

### Development Interfaces 

- Object-oriented, servlet-like - request and response objects are available to Python \"handler\" objects.

- Presentation-oriented - the wt template package permits the presentation aspects of an application to be separated out into template files, with the data presented by such files being defined (or constructed) by Python objects (in a fashion similar to that of [JavaBeans](./JavaBeans.html) when used with [JavaServer](./JavaServer.html) Pages).

### Environment Access 

- Access to resources is primarily done using the Python module system and other general environment access techniques.

### Session, Identification and Authentication 

- Support for sessions which identify users is included, with filesystem and SQL-based database session stores as supported options.
- No explicit authentication support seems to be included.

### Persistence Support 

- Apart from session information, no persistence mechanisms are included.

### Presentation Support 

- wt - a template system which uses comment-like elements to delimit sections within a document (reminiscent of early DTML elements) and special markers to indicate places where values are to be substituted into the final document.

Other presentation systems could easily be used instead, given the ability to use other Python modules in the framework (the system is layered and you can use the cgi/fastcgi/modpython facilities without using the wt templating system if you wish).

### InTheirOwnWords 

### Comments 

Jonpy does not provide a complete Web application environment for the most demanding of developers, but the intention behind the development of the framework is clearly to provide a robust foundation for small applications (or applications in limited environments), with the obvious possibility to use other packages and frameworks in conjunction with this one to address larger or more \"ambitious\" problems. Moreover, the framework seems to attempt to provide solutions for the most common problem areas in the early phases of Web application development, notably session support and a convenient-but-simple object model. \-- [PaulBoddie](PaulBoddie)
