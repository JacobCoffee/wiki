# TwistedMatrix

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

### Introduction 

\*NOT\* just framework for [WebProgramming](WebProgramming), but includes a scalable and safe web server that outperforms apache in terms of security and scalability.

### Masthead 

URL

:   [http://www.twistedmatrix.com/](http://www.twistedmatrix.com/)

stable version
:   12.1.0

licence
:   MIT

platforms
:   everywhere Python runs

Python versions
:   2.5 or later, but not 3.\*

### Deployment Platforms 

Windows, UNIX. Special support for FreeBSD kernel features.

### Protocols 

Out of the box

:   HTTP, FTP, NNTP, SSH, SOCKSv4, IRC, POP3, SMTP, Telnet, AOL\'s TOC, OSCAR, [MouseMan](./MouseMan.html), finger, Twisted Perspective Broker, see [http://www.twistedmatrix.com/products/protocols](http://www.twistedmatrix.com/products/protocols)

Through additional modules
:   LDAP

### Suitability 

### Development Interfaces 

### Environment Access 

### Session, Identification and Authentication 

### Persistence Support 

Twisted provides an interface to any Python DB-API 2.0 compliant database through an asynchronous interface which allows database connections to be used, and multiplexed by multiple threads, while still remaining thread-safe for use with Twisted\'s event-based main loop.

Twisted Enterprise integrates with Twisted Web and other Twisted services, making it easy to generate dynamic content from an enterprise data source of any variety.

The best supported database at the moment, because we here at Twisted Matrix Labs like it the best, is [PostgreSQL](PostgreSQL).

- \-- [InTheirOwnWords](InTheirOwnWords)

### Presentation Support 

### InTheirOwnWords 

Twisted integrates a large number of consistent APIs for developing new Internet services. This translates to a wide number of protocols and components that are ready to work with your new server before you\'ve written the first line of code.

In addition to legacy protocol support, the twisted.spread package allows developers to quickly develop new protocols and services with arbitrarily complex interfaces, prototyping new client functionality on the fly.

What does this mean in terms of development time? If you\'re developing a new server, it could take literally a year off of your implementation time \-- and that\'s just now. Twisted development is proceeding at a rapid pace, and by the time you\'ve finished your development you may find a host of new features that you didn\'t have to spend a moment thinking about!

Twisted comes under a relatively non-restrictive open-source license, making it suitable for both commercial and open-source development.

### Comments 

#### Twisted on Windows 

It works ok until you want to deploy as a service. I found that tricky - I had to write my own service to start and stop twisted (as of 1.3). [TwistedWebServerSampleOnWindows](TwistedWebServerSampleOnWindows)
