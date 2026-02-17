# pso

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

A framework for [WebProgramming](WebProgramming).

### Masthead 

URL

:   [http://sourceforge.net/projects/pso/](http://sourceforge.net/projects/pso/)

version
:   0.98.D-beta (2004-07-12)

licence
:   LGPL.

platforms
:   independant

Python versions
:   2.1

### Deployment Platforms 

- any web server platform

### Suitability 

pso- Python Service objects is a package that simplifies and abstracts the use of HTTP handlers. Write once and really run on modpython, modsnake, NASAPY, fastcgi, or CGI.

- It offers an easy interface to HTTP info and built-in sessions handling.
- There are no tags to learn. Just use html and embed your own tags. This is a system for programers, who want to develop with an OO methodology with an emphasis on re-use.
- Has a simple, fast, robust and powerful extendable OO template parser.
- Used on the floor of NYSE to deliver their most used and important internet based trading service.

### Development Interfaces 

- Object-oriented, templates embedded with python tag object and and service methods.

### Environment Access 

- Adapters allow this.

### Session, Identification and Authentication , and Persistence Support 

- built-in and extentable see [HOW-TO: Easy CGI session handling using pso.session](http://sourceforge.net/docman/display_doc.php?docid=10175&group_id=49265) or [How-To: Easy mod_python Session Handling with pso.session](http://sourceforge.net/docman/display_doc.php?docid=10174&group_id=49265)

### Presentation Support 

- No special tags, just HTML templates with programmer created tags. see [pso - Building a web service with pso](http://sourceforge.net/docman/display_doc.php?docid=11561&group_id=49265) - This is a \"Build a web portal in 15 minutes\" type how-to.

### Comments 

I have just started using this as my hosting company only runs Python 2.2 at the moment and uses Zeus instead of Apache, so no mod_python. It really didn\'t take me long to pick it up and within a couple of hours I had my blog written, a set of back-end tools to manage it as well as the archive view for permalinks. I also went and added a log parser to track certain traffic patterns on my site using the PSO framework, and that took me all of 15 minutes to throw together. I haven\'t tried some of the servlet clones yet, but so far, PSO definitely suits all my needs. It\'s well put together and runs incredibly fast, even over cgi. You can see for yourself at [David Giffin\'s Thoughts, projects, ideas and ramblings](http://www.davtri.com/thoughts.cgi) If anyone knows the authors, I would love to see the project taken to completion.

\-- Dave Giffin

### Hosting 

- wherever you can run a CGI.
