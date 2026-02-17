# WebSIGTasks

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

Bill Janssen has suggested reviving the Web SIG: [http://mail.python.org/pipermail/meta-sig/2003-September/001277.html](http://mail.python.org/pipermail/meta-sig/2003-September/001277.html)

Possible deliverables:

# SSL server support 

Add SSL server-side support to the \"socket\" module. This will include some way of managing certificates. Probably modelled strongly after the way we did it in ILU, if \[Bill Janssen does\] it :-).

[http://pyopenssl.sourceforge.net/](http://pyopenssl.sourceforge.net/) and [http://www.post1.com/home/ngps/m2/](http://www.post1.com/home/ngps/m2/) are more complete wrappers.

# HTTP client updates 

Update the \"httplib\" module to include all of the client-side functionality available in the Linux \"curl\" program (a reasonable checklist, I think, but am open to better suggestions).

Better support for HTTP Digest Authentication.

# HTTP server improvements 

Replace/extend the BaseHTTPServer and SimpleHTTPServer modules with an extended webserver module which provides at least the functionality in Medusa.

# cgi module improvements 

The cgi module is really old and has a number of obsolete classes. It should be cleaned up and modernized.

Anecdote: file upload support in Quixote was unreliable until Greg Ward threw up his hands, ditched cgi.py, and reimplemented file uploads from scratch.

# Add request/response objects to standard library 

This has been brought up on the [pyweb mailing list](http://www.amk.ca/pipermail/pyweb/).

Add a module containing the HTTP status codes.
