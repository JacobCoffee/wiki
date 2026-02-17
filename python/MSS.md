# MSS

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

A framework for [WebProgramming](WebProgramming).

### Masthead 

URL

:   [http://mss.cynetix.co.uk](http://mss.cynetix.co.uk)

version

:   1.0.1 (*2002-08-04*)

licence
:   MSS is free for personal use or commercial evaluation. It\'s files are freely distributable but must be kept together.

platforms

:   

Python versions

:   

### Deployment Platforms 

### Suitability 

### Development Interfaces 

### Environment Access 

### Session, Identification and Authentication 

### Persistence Support 

### Presentation Support 

### InTheirOwnWords 

**Problem Domain Background**

Typical 2-Tier client / server architecture is inflexible when it comes to code module changes. Code re-use is also limited as code modules have to be re-written or copied for each different client application. Enter 3-Tier architecture. The business logic is now extracted into the middle layer and back-end data sources are free to change, safe in the knowledge that client apps won\'t be broken, as it\'s now only one instance in the middle tier that gets changed.

**Motivation**

Although 3-Tier architecture solves many problems, there are few solutions that actually implement a simple, usable and cheap middle tier on a small scale. There are large implementations to fix large scale problems (CORBA) and technologies such as EJB that tackle the problem but all come with a learning curve.

**Solution**

MSS - A middle tier framework written in Python for plugging services in. Any client that can retrieve a web page can retrieve data from MSS - it\'s that easy. All the developer does is drop their \'new_service.py\' into the services directory and it works. No need to know how MSS works, there\'s a generic service provided so writing a new service should be a doddle and MSS will work straight out of the box.

### Comments 

### Hosting 
