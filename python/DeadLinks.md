# DeadLinks

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

Python is often used to crawl the internet. One of the useful application for that is finding dead links.

## Theory 

The basic method to check if link is dead is sending a HEAD request.

Advanced stuff requires crawling links that are alive, and skipping those that are already visited.

## Links to check 

- [PCrawler](http://math.nist.gov/~RPozo/ngraph/webcrawler.html) - NIST modular crawler, Public Domain, needs some love.

- [weblinkchecker.py](https://www.mediawiki.org/wiki/Manual:Pywikibot/weblinkchecker.py) - Wikipedia\'s Pywikibot link checker, MIT license.

- [https://pypi.python.org/pypi/LinkChecker](https://pypi.python.org/pypi/LinkChecker) - many features, GPL.
