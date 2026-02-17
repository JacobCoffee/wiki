# Wareweb

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

A framework for [WebProgramming](WebProgramming).

### Masthead 

URL

:   [http://pythonpaste.org](http://pythonpaste.org)

version
:   .4

licence
:   PSF

platforms
:   WSGI

Python versions
:   2.4+

### Deployment Platforms 

A WSGI-based framework, intended to be used under [Paste](http://pythonpaste.org/).

### Suitability 

All-purpose framework.

### Session, Identification and Authentication 

These aspects (and others) are handled by framework-neutral WSGI middleware included in Paste. In other cases (like persistence) general-purpose Python libraries should be used.

### Presentation Support 

Includes its own minimal event framework, and metaclass protocol, to make plugins/components fairly simple and general. In this case, a plugin can be written to handle templating. Only one such templating language is supported currently, in [ZPTKit](http://imagescape.com/software/ZPTKit/).

### InTheirOwnWords 

Wareweb is a refactoring of the programming model of [Webware](./Webware.html). It\'s intended to keep the same conceptual model (servlets), while natively including extensions (like [Component](http://wiki.w4py.org/component.html), and removing some aspects of Webware that were never flushed out.

It also removes the inheritance hierarchy (there\'s just one Servlet class), removes request and response objects (their functions are included in servlets natively), and separates out Webware\'s special dispatching on \_action\_ into a separate component (of which multiple dispatchers are available).

### Comments 

### Hosting 

This can be used anywhere Paste can be used, and in turn anywhere WSGI is available. If necessary it can be run as a CGI script, though this tends to be slow.
