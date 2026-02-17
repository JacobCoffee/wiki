# CodingProjectIdeas/PythonWebProgrammingIdeas

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

## Introduction 

The idea has to be substantive enough to be\... well, to be sufficiently substantive. Not all of these ideas are so substantive, so a proposal might use one of these as a starting point, or might be a combination of several ideas. Also see Python [WebProgramming](WebProgramming) (there\'s a lot!).

If you have questions you can contact [web-sig@python.org](mailto:web-sig@python.org) ([Web-SIG](http://www.python.org/sigs/web-sig/)), or one of the potential advisors listed at the end of this page. (But if you aren\'t willing to do some homework on these projects, that obviously won\'t look good\... ask smart questions!)

See also [../WebServiceStack](./CodingProjectIdeas(2f)WebServiceStack.html)

## The Web-Server Gateway Interface 

[WSGI](http://www.python.org/peps/pep-0333.html) is mostly an aspect of the implementation; many kinds of frameworks and tools could fit into that framework.

- A WSGI file-serving application. This application should understand all the relevant conditionals (If-Modified-Since, etc), gzipped encoding, etc.

- A proxy WSGI application (i.e., a WSGI application that echos another HTTP server).

- A forking backend to [Twisted](http://twistedmatrix.com), so that non-threadsafe/non-asynchronous applications could be run under Twisted.

- A web-based debugger. Given an exception or breakpoint, the user could inspect local variables in different frames (different levels of the stack), evaluate expressions in those frames, etc. This would be a great place to use Ajax.

- A Zope WSGI Server, making it possible to run WSGI applications under Zope.

- WSGI scheme for Python\'s urllib(2), so WSGI applications can be accessed like remote sites.

- A library/framework/WSGI application for a WebDAV server.

- Code that records and plays back WSGI interactions, so you can record a test session and replay it against an application.

- A WSGI application for progress-tracking uploads. Most frameworks don\'t give control to user code until after the entire request has been parsed; to track progress in uploading you have to have a special request parser that can write progress reports while it\'s processing the upload.

- A WSGI publish/subscribe messaging service to route requests for services, provided by other WSGI servers. For example, a WSGI interface to a template parser, such as Meld3, could subscribe to requests for templating. That service could in turn send a (sub)request of a template, such as a request for a database query. Likewise an ORM, such as SQLalchemy or SQLobject could subscribe to requests for database access, and receive notification of such subrequests. The goal would be to eliminate hard coded service routing (the \"pipe\" model of the WSGI \"stack\"), and replace it with discoverable WSGI services, to enable simultaneous processing of \"page\" elements (micro-formats?).

## Spyce 

[Spyce](http://spyce.sourceforge.net) is a web application environment similar to [ASP.NET](http://asp.net) or [Tapestry](http://jakarta.apache.org/tapestry/), in that all these frameworks allow you to create reusable components containing model, view, and controller. Spyce provides the convenience of [active handlers](http://spyce.sourceforge.net/docs/doc-lang_handlers.html) without imposing a leaky event model on your application. Spyce could use help with

- Ajax support, perhaps using the [Prototype](http://prototype.conio.net/) library

- Validation tags, similar to [ASP.NET\'s](http://www.w3schools.com/aspnet/aspnet_refvalidationcontrols.asp)

- More demos and/or tutorials

## Paste 

Anything related to WSGI will benefit [Paste](http://pythonpaste.org), but there are some tasks that would apply specifically to Paste:

- Logging support. The standard logging module provides a kind of framework, but it would be very useful to make that configurable through Paste, and make it easy for applications to use. Also, lots of stuff internal to Paste should be converted to using logging instead of print statements.

## Other ideas 

- Fixing/improving the Python-XPCOM bindings for Mozilla (that allow you to script Mozilla in Python). The code is there, but maybe needs some loving.

- A generic Python library for doing things with Google Maps. (For the record, there\'s the beginning of libgmaps.py here: [http://cvs.sourceforge.net/viewcvs.py/libgmail/gmaps/](http://cvs.sourceforge.net/viewcvs.py/libgmail/gmaps/).) \-- turns out [Google can\'t sponsor this one](http://groups-beta.google.com/group/summer-discuss/browse_thread/thread/21789da7c473e478)

- A system to comment on pages; specifically one that is applicable to the Python standard reference. Simple commenting (PHP.net-style) would be a start; annotation would be even better. Another Ajax opportunity; though of course the server-side implementation should be in Python.

- Create a full-featured WSGI app server (taking into account projects like [flup](http://www.saddi.com/software/flup/)) with special attention to things like resource usage and restarting after crashes, to make it suitable for commodity hosting environments ([contact](mailto:ianb@colorstudy.com)).

- Push-button web. A prototype system exists to manage HTML and ReST content in a relational database and publish it as static HTML. The wxPython GUI needs improvement and a more consistent substitution mechanism is required, together with better documentation and a supporting web content (which should be managed as a push-button web).

- A client side web browser. Grail is not currently maintained, and the others are almost entirely for automated or testing purposes, without a good interactive mode. But try to keep the scope reasonable, somehow. Perhaps hooking beautifulsoup or tidy to elementtree, urllib or urllib2, cookielib, and a text (or very basic) Tk front end? Do keep the DOM exposed, so that others can build on it more easily. Alternatively extracting an HTML 2 Tk widget from the grail project and them building more support of HTML 4 into in would be very useful.

- Add a web-based admin interface and/or user-oriented views to [DrProject](http://www.third-bit.com/drproject), a lightweight project management portal intended for use in software engineering courses.

- There are a number of potential [TurboGears](TurboGears) projects that may be interesting related to Kid, SQLAlchemy and [TurboGears](TurboGears) itself (like the [FastData](./FastData.html) package).

- A web-based IDE offering through-the-web editing (with version control), execution, and testing of code (see [SummerOfCode/WebIDE](./SummerOfCode(2f)WebIDE.html))

- Help make [Nevow\'s](http://nevow.com) stan a fully separate package, documented. Stan is a DOM-like representation of markup, and could potentially be used by many projects outside of Nevow.

- Separate out Nevow\'s [LivePage](./LivePage.html) code.

- Add client-side Javascript validation to [FormEncode](http://formencode.org).

- Plone Projects
  - Work on Plone or a related Plone Product.

    See [Plone\'s Summer of Code Page](http://plone.org/events/other/summerofcode) for details.

- A home media center.
  - Features include; Web Interface(Allowing control from psp, cellphone, laptop, etc.), feedreader(with ability to manage feeds, process audio, video, bittorrent files), Media manager(playlists for audio and video, ability to manage files, etc.), DVR functionality.

## Advisors 

- Most of my own interests center around WSGI middleware, or [Paste](http://pythonpaste.org) (which in practice is nearly the same thing). WSGI just about implementation really; nearly any kind of web programming infrastructure or application can fit into that. You can come up with something yourself or ask me; either way, I\'m open to advising. \-- [IanBicking](IanBicking)

- I would be happy to advise anyone interested in Spyce. \-- Jonathan Ellis (jonathan at utahpython dot org)

(other people who may be willing to advise should add a note here)
