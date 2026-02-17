# JOTWeb2

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

A framework for [WebProgramming](WebProgramming).

### Masthead 

URL

:   [http://jotweb.tummy.com/](http://jotweb.tummy.com/)

version

:   1.10 (*2005-12-30*)

licence
:   GPL

platforms
:   Linux, possibly others

Python versions
:   2.3.4 or above

### Deployment Platforms 

Requires Apache and mod_python; is therefore constrained by the deployment requirements of those components.

### Suitability 

### Development Interfaces 

Seems to focus on templating and rather simple published handler functions inside Python modules.

### Environment Access 

Provides a configuration mechanism and employs a context containing application-related data for convenient access by the presentation templates.

### Session, Identification and Authentication 

Provides filesystem and relational database sessions, along with authentication support.

### Persistence Support 

Does not appear to provide explicit support for persistence mechanisms (apart from the session support mentioned above).

### Presentation Support 

Uses Zope 3\'s TAL for templating.

### InTheirOwnWords 

### Comments 

These notes were added to provide a brief overview of the software. However, I have not actually evaluated the software myself. \-- [PaulBoddie](PaulBoddie)

### Hosting 

The usage of Apache and mod_python seems to dictate hosting options.
