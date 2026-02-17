# Wasp

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

### Masthead 

URL

:   [http://robinparmar.com/wasp.html](http://robinparmar.com/wasp.html)

version

:   2.00 (*2007-07-17*)

licence
:   GPL

platforms
:   Linux, Windows

Python versions
:   Python 2.5 and above

### Deployment Platforms 

Wasp works in three modes. In client mode Wasp requires no deployment platform but compiles templates in batch mode. In CGI mode it works with an appropriate web server. In server mode it runs embedded in its own threaded web server.

### Suitability 

Suitable for those who wish the conventional URL/file website paradigm. Not (as) suitable if you wish to code your entire site in an OOP fashion with virtual files. Not WSGI compatible.

### Development Interfaces 

Python code may be freely added as plugins with no special dependencies or restrictions. Code may also be inserted into page templates. A streamlined web environment is provided with easy access to CGI info, cookies, sessions, etc.

### Environment Access 

Wasp can access any Python modules, stored in shared or restricted locations. There are no limitations on how the designer partitions business logic from other components.

### Session, Identification and Authentication 

A robust database-independent server-side session mechanism is provided, which uses cookies to store unique keys. This can be used for identification and authentication as the designer wishes.

### Persistence Support 

None provided, so you can use your favourite. Wasp is database agnostic.

### Presentation Support 

Wasp contains a simple templating system that allows Python code in template files if you so wish.

### InTheirOwnWords 

Wasp was developed when there were relatively few alternatives for Rapid Application Development in Python for the web. Now there are many such. Wasp distinguishes itself in its maturity (in development since 2001), currency (new version provides significant improvements), simplicity (installs easily with no dependencies), adherence to standard web paradigms (files are still files, URLs are still URLs), ability to run in command-line mode (no web server required to get the benefits of templating), remote debugging (really a life-saver), and thorough documentation.

Wasp may not be appropriate for high-traffic sites. Here the CGI mode might be a limiting factor, and the embedded web server mode is not (as of yet) sufficiently tested under duress to recommend.

### Comments 

### Hosting 

Any Apache setup with Python 2.5
