# ModPython

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

A framework for [WebProgramming](../web/WebProgramming).

### Masthead 

- **URL:** [http://www.modpython.org/](http://www.modpython.org/)

  **platforms:**

  - stable version for Apache 1.\*: 2.7.10 (*2004-01-22*)

  - stable version for Apache 2.\*: 3.2.8 (*2006-02-24*)

  **Python versions:** Python 1.5.2, 1.6, 2.0, 2.1, mod_python 3.\* requires 2.2.1

  **licence:** The Apache Software License, Version 1.1

### Deployment Platforms 

Linux and Windows. RPMs available.

### Suitability 

mod_python can be used to develop fast and small web tools and applications, and as part of larger custom application frameworks. It provides an object publishing mechanism similar to (but much simpler than) Zope, and a very clean mapping from URLs to functions. This makes it especially suitable for building web-accessible libraries using HTTP GET/POST as function call serialization.

### Community 

See the mod_python [mailing list](http://www.modpython.org/pipermail/mod_python/).

### ModPython Compatible Web Application Frameworks 

**ModPython itself:**

- ModPython now has built-in support for cookies and sessions, PSP templates, etc., and a CGI handler for compatibility with regular CGI python scripts.

**Web application frameworks that support multiple kinds of deployments including ModPython:**

- [WebStack](WebStack) aims to provide a common API regardless of the underlying server or framework environment (be it ModPython, CGI, [Webware](./Webware.html), etc.).

- [Quixote](../web/Quixote) is a web application framework that has a ModPython handler.

- [Albatross](../web/Albatross) applications can be deployed to ModPython or CGI.

- [Karrigell](../archive/Karrigell) is meant primarily for running small standalone web applications, but now has a ModPython handler as well.

- [Aquarium](../web/Aquarium) is a MVC web application framework using [Cheetah](http://cheetahtemplate.org) for templating with some resemblance to Struts and a ModPython WSAdaptor.

**Frameworks designed specifically for ModPython:**

- [Pylets](http://pylets.sf.net/) is a new web framework with aspect-oriented [MetaClasses](./MetaClasses.html).

- [PyWork](http://pywork.sf.net/) is a Model-View-Controller framework with similarities to Struts.

- [JOTWeb](http://jotweb.tummy.com/) also separates the view and the model in part by using TAL templates.

- [Django](http://www.djangoproject.com/) runs in stand-alone mode for development purpose, but relies on ModPython for production.

### Environment Access 

mod_python provides a similar API to mod_perl, allowing low-level access to Apache\'s request handling mechanisms.

### Session, Identification and Authentication 

mod_python 3.1.3 and later provides support for server-side sessions with memory or dbm-based storage. It also supports session locking. For earlier versions, [JonsPythonModules](../archive/JonsPythonModules) implement session management as well as templating and database pooling. mod_python has a very straightforward and flexible system for basic authentication, allowing access rules to be configured at the module and function level.

### Persistence Support 

Scripts remain in memory between page loads. The Python interpreter can be configured to run per-site or per-directory, allowing the scope of the persistence to be limited as necessary.

### Presentation Support 

mod_python provides a php-like built-in templating system called Python Server Pages (PSP), but there are many others that can also be used ([Cheetah](http://www.cheetahtemplate.org/) for example).

### InTheirOwnWords 

mod_python is an Apache module that embeds the Python interpreter within the server. With mod_python you can write web-based applications in Python that will run many times faster than traditional CGI and will have access to advanced features such as ability to retain database connections and other data between hits and access to Apache internals.

### Comments 

mod_python has been \"donated\" to the Apache Software Foundation. Here is author Gregory Trubetskoy\'s official statement as of Thursday, Sept. 12, 2002:

It is my pleasure to announce that Mod_Python has been donated to the Apache Software Foundation, and is now a subproject of the httpd server project (see [http://httpd.apache.org/](http://httpd.apache.org/)).

I am grateful to ASF for accepting this donation and committing resources to further the support of Mod_Python. I believe that this action will advance the development of Mod_Python, resulting in an ultimately better and more popular tool for Python developers. I also believe it will serve to better position Python as a language of choice for web development, a need that has been expressed by many.

There are no implications to the current Mod_Python users - the license is the same with the sole difference in that the copyright belongs to ASF now.

As a consequense of the donation, the CVS repository is now hosted on cvs.apache.org. Do not use the [SourceForge](SourceForge) repository anymore, it will soon be removed.

There will also be website and mailing changes, but the details are still being finalized and will be announced when ready.

Regards,

Grisha Trubetskoy

### Hosting 

Unknown

### Tutorials 

- [Modpython Tutorial](http://webpython.codepoint.net/mod_python) - An introduction to modpython\'s high level handlers: Publisher and PSP.
