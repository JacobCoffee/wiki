# WebClientProgramming

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# Client-Side Web Programming 

## Libraries 

- [µTidylib](http://utidylib.berlios.de/) and [mxTidy](http://www.egenix.com/files/python/mxTidy.html) \-- Python interfaces to [html tidy](http://tidy.sourceforge.net/) library to clean up HTML documents.

- [html5lib](http://code.google.com/p/html5lib) A HTML5-compliant library for parsing arbitarily-broken HTML to a range of tree formats including minidom, elementtree (including lxml) and [BeautifulSoup](./BeautifulSoup.html)

- [BeautifulSoup](http://www.crummy.com/software/BeautifulSoup/) \-- a permissive HTML parser.

- Don\'t use [HTMLParser (Python 2.x)](https://docs.python.org/2/library/htmlparser.html) or [html.parser (Python 3.x)](https://docs.python.org/3.5/library/html.parser.html) on HTML that might be invalid! That way lies pain. Either clean it up (using tidy), or use a different parser.

- [urllib](http://docs.python.org/library/urllib.html), [urllib2](http://docs.python.org/library/urllib2.html), and [httplib](http://docs.python.org/library/httplib.html) in the standard library.

- [ClientCookie](http://wwwsearch.sourceforge.net/old/ClientCookie/), [ClientForm](http://wwwsearch.sourceforge.net/ClientForm/), and [Mechanize](http://wwwsearch.sourceforge.net/mechanize/) are higher-level libraries for writing a web client.

- [mechanoid](http://pypi.python.org/pypi?:action=display&name=mechanoid) a mechanize fork.

- [libxml2dom](http://www.python.org/pypi/libxml2dom) can parse HTML by employing libxml2\'s liberal HTML parser.

## Resources 

- [Grab a document from the web](http://aspn.activestate.com/ASPN/Cookbook/Python/Recipe/52199) - from the Python Cookbook

- [Python web-client programming general FAQs](http://wwwsearch.sourceforge.net/old/bits/GeneralFAQ.html).

- [urllib \-- Open arbitrary resources by URL](http://docs.python.org/library/urllib.html)

- [urllib2 \-- extensible library for opening URLs](http://docs.python.org/library/urllib2.html)
