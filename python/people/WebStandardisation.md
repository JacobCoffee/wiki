# WebStandardisation

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# Web Standardisation for Python 

Traditionally, Python Web technology support entered the standard library through a process of gradual aggregation (see the cgi, httplib and urllib modules). However, various discussion groups, mailing lists and independent endeavours have sought to establish more usable standard APIs and modules over the years.

## Standardisation Attempts and Proposals 

- [WebStack](WebStack) presents a common request, response and session API for numerous servers and environments.

- [PEP 3333 \-- Python Web Server Gateway Interface v1.0.1](http://legacy.python.org/dev/peps/pep-3333/) is the community standard for connecting relatively low-level Web components together - see also [WSGIImplementations](WSGIImplementations).

- [Indra](http://furius.ca/indra/) defines Web component interfaces that are somewhat reminiscent of [WebStack](WebStack)\'s API.

- [httpy - a sane and robust Python HTTP server and library](http://www.zetadev.com/software/httpy/)

## Resources 

- [The old but still useful Web Programming topic guide](http://www.python.org/topics/web/) - this should have been the focus for presenting the state of the art; the [WebProgramming](WebProgramming) section now fulfils that role.

- [Web SIG](http://www.python.org/sigs/web-sig/) (the Python Web Special Interest Group) along with a mailing list for discussion of community standards. Some initial ideas for the Web SIG are described on the [WebSIGTasks](WebSIGTasks) page.

## Commentaries 

Despite rumours in the summer of 2006 that the [BDFL](BDFL) had endorsed one particular [Web framework](WebFrameworks), the official position on community standardisation after clarifications were made presumably remains as summarised in the following quote:

*\"I do recommend that web developers (I\'m still not much of one) get together, share experiences, and ask the web framework developers to standardize low-level APIs in additionn \[sic\] to WSGI (PEP 333).\"*

(Source: [Please Teach me Web Frameworks for Python](http://www.artima.com/forums/flat.jsp?forum=106&thread=146149&message=204823#204823))
