# WSGIImplementations

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# Implementations of the Web Server Gateway Interface 

Note: many of these implementations may be partial/incomplete or noncompliant as of the current draft spec. If you can\'t get the code samples in the spec to work with one of these implementations, there\'s a good chance that the implementation is broken: contact the implementation\'s author.

See [PEP 333](http://www.python.org/peps/pep-0333.html) for more information on WSGI.

## Web Server implementations 

- [Divmod Nevow](http://divmod.org/trac/wiki/DivmodNevow) Twisted Web-based templating framework with a WSGI implementation

- [Eventlet](http://wiki.secondlife.com/wiki/Eventlet/Documentation#Using_eventlet.wsgi) - allows for the implementation of massively concurrent servers which would require prohibitive amounts of memory under a traditional preemptive multi-threading or multi-process model \... can also run inside of the nginx Web server using the mod_wsgi package for nginx

- [flup](http://www.saddi.com/software/flup/) has AJP, SCGI and FastCGI servers

- see Jonpy below\<br\>

- [isapi_wsgi](http://isapi-wsgi.python-hosting.com) - a WSGI implementation for IIS ISAPI

- [modjy](http://modjy.xhaus.com/) - a WSGI implementation for Jython

- [mod_wsgi](http://code.google.com/p/modwsgi/) module for Apache

- [nginx mod_wsgi](http://wiki.codemongers.com/NginxNgxWSGIModule?highlight=%28wsgi%29) module for Nginx

- [Peak](http://peak.telecommunity.com/) has CGI and FastCGI gateway and server options [more info](http://mail.python.org/pipermail/web-sig/2004-October/000966.html)

- [Paste#http](http://pythonpaste.org/module-paste.httpserver.html) a SimpleHTTPServer-based server

- see [Python Paste](http://mail.python.org/pipermail/web-sig/2006-January/001859.html) below

- [SWAP](http://www.idyll.org/~t/www-tools/wsgi/) - a WSGI adapter for [SCGI](http://www.mems-exchange.org/software/scgi/).

- [Twisted Web2](http://twistedmatrix.com/projects/web2) Experimental HTTP server with a WSGI implementation

- [Toolserver Framework for Python](http://pyds.muensterland.org/wiki/toolserver.html) - a WSGI implementation in a Medusa-based webservice framework

- [wsgiref](http://mail.python.org/pipermail/web-sig/2004-October/000956.html) - a library of base classes covering most of the \"hard parts\" of a WSGI server implementation, written by the PEP author. It also includes utility functions and classes that may be useful for application/framework implementors, and should be considered a \"must read\" for server implementors. (Update: most of the limitations mentioned in the linked post have now been resolved; wsgiref now includes sensible default error handling and logging, automatic calculation of Content-Length when possible, and greater test coverage. See [wsgiref](http://svn.eby-sarna.com/wsgiref) for source code.)

- see WSGIUtils below

## Web Framework implementations 

- [CherryPy](CherryPy) 2.1 beta includes a mutli-threaded WSGI server

- [Colubrid](http://wsgiarea.pocoo.org/colubrid/) - simple to use WSGI implementation compatible with python2.2 or higher. It parses formdata, url parameters, cookies and implements some simple to use URL dispatchers.

- [Django](http://www.djangoproject.com/) - An emerging framework generating a lot of buzz that has [recently added support](http://code.djangoproject.com/changeset/169) for WSGI

- [Jonpy](http://st0rm.hopto.org/wsgi/) - this also includes a HTTP server with a WSGI backend

- [Nevow](http://divmod.org/trac/wiki/DivmodNevow) - the reimplementation of Twisted\'s woven, doesn\'t require Twisted.

- [Paste WebKit](http://pythonpaste.org/webkit/) - a [Webware](http://w4py.org) reimplementation, implemented with a degree of framework-neutrality in mind.

- [Python Web Modules](http://www.pythonweb.org) - New version contains a WSGI server and middleware.

- [Python Paste](http://pythonpaste.org/) - a collection of low-level WSGI tools including a multi-threaded SSL-enabled WSGI [server](http://svn.w4py.org/Paste/trunk/paste/httpserver.py), and an [auth](http://svn.w4py.org/Paste/trunk/paste/auth/) package with signed cookies, sessions, form and digest authentication.

- [Pylons](http://pylonshq.com/) - a WSGI-based framework using Mako and Paste

- [QWIP](http://www.idyll.org/~t/www-tools/wsgi/) - a WSGI adapter for [Quixote](http://quixote.ca/) applications.

- [TurboGears](http://www.turbogears.org) also provides a WSGI front-end.

- [Wareweb](http://pythonpaste.org/wareweb/) - a rethinking of Webware/WebKit

- [weblayer](http://packages.python.org/weblayer/) - weblayer is a lightweight, componentised Python package for writing WSGI applications

- [WSGIUtils](http://www.owlfish.com/software/wsgiutils/) - A multi-threaded WSGI server implementation and a simple framework providing basic user authentication, signed cookies, and persistent sessions.

- [Zope](http://www.zope.org) Zope 3 is now a WSGI application. It ships with the Twisted

  - WSGI server implementation and also includes an asyncore-based server implemenatation.
