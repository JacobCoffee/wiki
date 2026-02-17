# Draco

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

A framework for [WebProgramming](WebProgramming).

### Masthead 

URL

:   [http://draco.boskant.nl/](http://draco.boskant.nl/)

version

:   0.99.4 (*2003-03-27*)

licence
:   GPL

platforms
:   Apache with mod_python

Python versions
:   2.2/2.3

### Deployment Platforms 

Draco plugs into the Apache/mod_python combination. Both Apache 1.3 and Apache 2.0 are supported. For serious use, a relational database must be installed. Currently, the popular MySQL and PostgreSQL database systems are supported.

### Suitability 

### Development Interfaces 

No special development environment is available. Draco applications can be made just like a regular Python application using a text editor.

### Environment Access 

Most of the standard CGI environment is available as properties or methods of a collection of global Python objects.

### Session, Identification and Authentication 

Draco has an integrated and automatic session management mechanism. Both cookie and url tagging methods are supported. Sessions can be logged in, made persistent and optionally made secure by using SSL. Authentication and authorization have to be performed by the application.

### Persistence Support 

Draco make use of the **namespace** concept. A namespace is a place where you can store (almost) arbitrary Python variables using the Python dictionary API (ns\[\'varname\'\] etc.). There are different namespaces, some of which are persistent. These include the *session*, *user*, *application* and *server* namespace.

Technically, persistence is implemented by a relational database backend.

### Presentation Support 

#### Process Logic versus Markup Logic 

In Draco program logic is conceptually separated into process and markup logic. The process logic is the logic that processes a request and performs the desired action. The markup logic is the logic that formats the results of the process logic in the html.

#### Handlers and Templates 

Draco makes use of **handlers** and **templates**. The process logic is put in a handler. This handler processes the client\'s request and performs the requested operations. The result of these operations is put in a special namespace called the *interface*.

The template is template as exist in many web frameworks, namely an html file with embedded code blocks. The only thing this code should do is format the results from the **interface** namespace into the html. All variables from the **interface** namespace are directly available to this code as global variables.

### InTheirOwnWords 

### Comments 

### Hosting 
