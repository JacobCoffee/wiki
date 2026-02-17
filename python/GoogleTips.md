# GoogleTips

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# Google Tips for Python 

People frequently have trouble finding stuff on the Python websites. Sometimes they are just too lazy to search. Other times they don\'t shine a light in the proper corner. [Google](http://www.google.com/) pokes in every corner, but you sometimes need a little help coaxing information out of it. This page gives a few idioms useful for searching Google effectively for content on the Python websites.

## Searching a Single Site 

Google enables you to restrict your search to a single site.

**site:www.python.org spam**

will search www.python.org for \'spam\'.

The next few sub-sections illustrate handy examples.

### Searching Mailing Lists 

**site:mail.python.org listname terms**

- Search for discussions of packages in python-dev: `site:mail.python.org python-dev packages`

- Search for BDFL pronouncements in python-list: `site:mail.python.org python-list guido pronouncement`

### Searching the Library Reference Manual 

**site:www.python.org library reference terms**

- Search for information about regular expressions: `site:www.python.org library reference regular expressions`

- Search for examples of using the logging module: `site:www.python.org library reference logging example`

### Searching the Language Reference Manual 

**site:www.python.org reference manual terms**

- Search for reference description of list comprehensions: `site:www.python.org reference manual list comprehension`

### Searching the PEPs 

**site:www.python.org PEP terms**

\* Search for PEP 289: `site:www.python.org PEP 289`

\* Search for PEPs about rational numbers: `site:www.python.org PEP Rational`

## Searching for a Phrase 

If you simply type your seach terms into the google search box, google will return pages that use all of your search terms, no matter where they occur. If, instead, you surround your search terms with double quote marks, you will get back an exact-phrase search.

Thus, searching for

**python wiki engine**

will return any pages that mention all three terms, many of which won\'t be about python wiki engines, per se. By contrast, a search for

\"**python wiki engine**\"

will only return pages which uses this exact phrase.
