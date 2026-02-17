# Albatross

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

A framework for [WebProgramming](WebProgramming).

### Masthead 

URL

:   [http://www.object-craft.com.au/projects/albatross/](http://www.object-craft.com.au/projects/albatross/)

version

:   1.40 (*2010-03-15*)

license

:   Albatross uses a Open Source BSD-like [license](http://www.object-craft.com.au/cgi-bin/faq/albatross?req=compat#1.3) that permits most uses.

platforms
:   Unix and Windows

Python versions
:   Python 2.2 and up

### Deployment Platforms 

Allows programs to be deployed as CGI, FastCGI, mod_python or stand-alone applications on either Unix or Windows. Applications can be coded as monolithic scripts or as a collection of page modules. Switching deployment methods can be achieved by changing less than 10 lines of code.

A number of server and client side session schemes are supported.

### Suitability 

Albatross is particularly suited to building small stateful web applications quickly, but also scales well to large applications.

### Development Interfaces 

Albatross functionality is provided via a collection of mixin classes which provide variant implementations of common functional areas. There are also a collection of pre-packed classes which combine the basic mixins to implement commonly used functionality.

If any aspect of the functionality does not suit your needs you are encouraged to substitute your own mixin classes.

### Environment Access 

Albatross applications are a collection of Python modules and HTML template files. All code and templates are stored in the host file system.

### Session, Identification and Authentication 

Albatross session functionality is provided by a combination of application and execution context mixins. The supplied mixins support the following session options.

- No sessions.

- Client side sessions using MD5 signed pickles in hidden fields.

- Server side sessions using the Albatross TCP session server.

- Server side sessions using the file system.

- Server side sessions with branching - this scheme reduces the problems caused by users using the browser \<back\> button.

All session ids are randomly generated 64 bit numbers using /dev/urandom if available falling back to random module.

### Persistence Support 

No support provided - just use your favourite DB-API modules.

### Presentation Support 

Albatross uses a DTML like templating scheme. The more interesting templating functions are:

- Derive attribute values from python expressions for arbitrary tags.
- Automatic sequence pagination.
- Presentation and browsing of tree structured data with optional lazy loading and/or \"Ellipsis View\". This allows huge trees to be browsed.
- Simple but powerful macro definition and expansion.
- Switch like lookup tables to translate native Python values to arbitrary template content.

### InTheirOwnWords 

Albatross is a toolkit for developing highly stateful web applications.

### Comments 

Object Craft (the developers of Albatross) are committed to ongoing maintenance and enhancement of Albatross as they use it in a number of their consulting projects.
