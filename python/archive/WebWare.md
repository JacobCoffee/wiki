# Webware

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

A framework for [WebProgramming](../web/WebProgramming).

### Masthead 

URL

:   [http://www.webwareforpython.org](http://www.webwareforpython.org)

version
:   1.1.1 (Date: 2013-01-18)

licence

:   [Old-style Python licence](http://www.webwareforpython.org/Docs/Copyright.html) - Webware is open source.

platforms
:   Webware works on UNIX, Windows and OpenVMS platforms.

Python versions
:   2.0 and up

### Deployment Platforms 

- Integrated with a Web server using CGI or adapters (such as mod_webkit for Apache).
- The Webware environment is provided by long-running processes.
- Work has been done to permit Webware to run as a standalone server.
- Works well with Windows,Unix and OpenVMS environments.

### Suitability 

In practice, Webware requires a Web server in order to be deployed, but to start out as a developer it is fairly straightforward to set up the supplied CGI adapter program to communicate with the [WebKit](WebKit) component of Webware. Should other means of integration be chosen later, such as adapters or even the standalone server features, Webware components and applications need not be aware of such changes in deployment.

The need to run the [WebKit](WebKit) component\'s application server process continually excludes Webware from certain hosting environments. It is possible to use a [OneShot](./OneShot.html) CGI-based mechanism to launch the application server for each request, but performance is very poor.

### Development Interfaces 

- Object-oriented, servlet-like - many classes expose request and response objects to Python components, and a hierarchy of classes attempts to model page components (or whole pages) using this paradigm.
- Presentation-oriented - certain template systems are targeted particularly at Webware, such as Python Server Pages and Cheetah.

### Environment Access 

- Webware uses Python-based configuration files to specify resource locations to Webware components, plug-ins and applications.
- It can therefore be said that Webware\'s environment access system is module-based.

### Session, Identification and Authentication 

- Webware provides mechanisms for the identification of users.

- Despite the existence of a [UserKit](UserKit), there is no apparent consensus on common authentication mechanisms.

### Persistence Support 

- A plug-in called [MiddleKit](MiddleKit) (which can be used independently of Webware) provides an object-relational mapper.

- [MiddleKit](MiddleKit) is used to generate database schemas and Python code which accesses the database whilst providing an object-oriented front end to the data being manipulated.

### Presentation Support 

- Python Server Pages - a [PythonInWebPage](../archive/PythonInWebPage) presentation technology supplied with Webware.

- Kid - Webware supports Kid templates via the [KidKit](./KidKit.html) plug-in.

- Cheetah - a popular template system originally developed for Webware but available separately.

Other presentation systems also exist for Webware.

### Comments 

Webware is relatively easy to install and comes with a reasonable amount of documentation. One of the stated strengths of Webware is that the development and deployment of code takes place in an environment that is familiar to anyone who has already developed Python applications before - in most cases, files need only to be placed in certain [WebKit](WebKit) \"context\" directories. Webware application development therefore seems more familiar to those experienced with writing CGI programs than systems working according to different principles (such as Zope), but arguably lends itself less to a \"component exchange culture\" (as seems to be the case with Zope). \-- [PaulBoddie](PaulBoddie)

Webware does not try to subsume the Python language and environment. Whenever possible, pieces of Webware are independent of each other, and it is recommended that developers use Python facilities as much as possible. There is no added syntax (except in the optional PSP component) and the interfaces are relatively minimal. \-- [IanBicking](IanBicking)
