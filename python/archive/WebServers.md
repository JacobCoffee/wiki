# WebServers

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# Web Servers and Python 

Python-based Web servers have been available in the standard library for many years (see the BaseHTTPServer, SimpleHTTPServer and CGIHTTPServer modules). To address various issues of scalability, robustness and convenience with such existing servers, other server frameworks and solutions have been developed since that time.

## Web Servers written in Python 

- [Chaussette](https://pypi.python.org/pypi/chaussette/) - A web server capable of running using multiple different underlying http engines

- [CherryPy - a pythonic, object-oriented HTTP framework](http://www.cherrypy.org)

- [Gunicorn](http://gunicorn.org/) - inspired by the Ruby server, Unicorn

- [Rocket](https://launchpad.net/rocket/) - a pure python HTTP server for WSGI applications and static files which runs on cPython 2.5-3.x and Jython 2.5

- [Spawning](http://pypi.python.org/pypi/Spawning/) - a WSGI server which supports multiple processes, multiple threads, green threads, non-blocking HTTP io, and automatic graceful upgrading of code.

- [Tornado](http://www.tornadoweb.org/) - an open source version of the scalable, non-blocking web server and tools that power [FriendFeed](./FriendFeed.html).

- Twisted includes [a very scalable web server](http://twistedmatrix.com/trac/wiki/TwistedWeb) written in Python.

- [Waitress](https://pypi.org/project/waitress/) - A WSGI server that runs on Windows and UNIX under [PyPy](../implementations/PyPy), CPython 2.X and CPython 3.X.

## Web Servers embedding Python 

In addition to the above, some non-Python-based Web servers support Python-based applications by embedding the Python virtual machine for improved performance:

- [G-WAN](http://gwan.ch/) is a (Linux-only) Web application server that supports servlet scripts written in Python among other languages

- [mod_wsgi](http://www.modwsgi.org) embeds Python in the Apache HTTP server

- [Modjy](http://modjy.xhaus.com/) embeds a jython interpreter in Java Servlet containers, e.g. Tomcat, Glassfish, Websphere, etc, and supports WSGI. Distributed with jython since March 2009.

- [ModPython](ModPython) embeds Python in the Apache HTTP server

- [Nginx WSGI](http://wiki.nginx.org/NginxNgxWSGIModule) support module for Nginx HTTP server

- [PyWX](../archive/PyWX) embeds Python in AOLServer

## Standard Library Technologies 

- [BaseHTTPServer](../archive/BaseHttpServer) (along with successors such as [DocXmlRpcServer](../archive/DocXmlRpcServer)) can be considered as the original Python Web framework, but it really just provides the ability to process HTTP requests and to generate responses using a relatively primitive API. Some [WebFrameworks](../web/WebFrameworks) use it as the basis for serving content, however.

------------------------------------------------------------------------

[CategoryPythonWebsite](CategoryPythonWebsite) [CategoryJython](CategoryJython) [CategoryJython](CategoryJython)
