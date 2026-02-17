# Aquarium

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

A framework for [WebProgramming](WebProgramming).

### Masthead 

URL

:   [http://aquarium.sourceforge.net](http://aquarium.sourceforge.net)

version

:   2.3 (Date:2007-01-01)

licence
:   Aquarium is open source software available under a BSD-style license.

platforms
:   Unix and Windows

Python versions
:   2.3 or higher

### Deployment Platforms 

CGI, [ModPython](ModPython), FastCGI and custom python-based web servers are supported via Web Server Adaptor classes, as is its own Web server, Glass. WSGI support is currently in CVS.

### Suitability 

### Development Interfaces 

### Environment Access 

### Session, Identification and Authentication 

Classes for session management are provided, sessions can be stored in memory, in the database, or a custom session container can be written easily.

### Persistence Support 

Provides a [DatabaseAssistant](http://aquarium.sourceforge.net/api/public/aquarium.database.DatabaseAssistant.DatabaseAssistant-class.html) class that abstracts and assists in database connectivity using DBAPI modules

### Presentation Support 

Uses and tightly integrates [Cheetah](http://www.cheetahtemplate.org) templating engine. The Aquarium project leader is also now a co-developer of Cheetah, so the integration of Cheetah can only improve from an already high level.

### InTheirOwnWords 

Aquarium is a Web application framework, written in Python. It provides an approach to producing a Web application without duplication of effort by reducing the amount of code you need to write. It offers convenient libraries and extensible APIs for items such as session management and Web server integration (including CGI, mod_python, FastCGI, or its own Web server, Glass). It provides tight integration with Cheetah, including autocompilation of Cheetah templates. Last of all, it offers a convenient approach to Web development. As a developer, you just \"plug in\" modules; Aquarium ties them all together.

Aquarium\'s features were inspired by a broad range of Web technologies (such as PHP\'s [FreeTrade](http://share.whichever.com/index.php?SCREEN=freetrade), Java\'s Struts, Perl\'s Mason, and Python\'s Zope). It is Open Source software, available under a BSD-style license. Aquarium is compact\--just a few thousand lines of code\--and extremely well documented. It\'s a useful tool for creating any highly-dynamic, custom Web application written in Python.

Aquarium is based around these ideas:

- Web applications can be thought of as a combination of a bunch of different types of modules. Aquarium serves as the framework for dynamically tying all of these modules together.
- The main request flow of an application involves a controller that does work and produces data. That data is passed off to a view that displays that data. See aquarium.screen.ScreenAPI for more on this.
- A view\'s superclass should take care of layout details automatically. In fact, a view should not need to do anything other than declare who it is subclassing (who you subclass and how many layers there are in the class hierarchy should not require you to change the name of your main method). See aquarium.layout.LayoutAPI for more on this.

Aquarium is now used world wide. I.e. there are people in at least the following countries using it: US, England, the Netherlands, the Ukraine, and Australia.

### Hosting 
