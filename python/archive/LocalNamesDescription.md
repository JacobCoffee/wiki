# LocalNamesDescription

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

I hope nobody minds; This is an experimental description of the wiki\'s space using [\"Local Names.\"](http://onebigsoup.wiki.taoriver.net/moin.cgi/LocalNamesBasics)

This is so that people can link into this space (and other spaces) conveniently and automatically with some tools.

If it\'s any consolation, the tools happen to be written in Python. ![:)](/wiki/europython/img/smile.png%20":)")

## Discussion 

Please keep comments here, above the description section. \-- [LionKimbro](../people/LionKimbro) 2004-07-06 23:39:32

## Description 

      http://purl.net/net/localnames/

This page is accessed by: [http://www.python.org/cgi-bin/moinmoin/LocalNamesDescription?action=raw](http://www.python.org/cgi-bin/moinmoin/LocalNamesDescription?action=raw)

See [LocalNamesBasics](http://onebigsoup.wiki.taoriver.net/moin.cgi/LocalNamesBasics) and [LocalNamesFormat](http://onebigsoup.wiki.taoriver.net/moin.cgi/LocalNamesFormat) for more information.

      NamesListPattern http://www.python.org/cgi-bin/moinmoin/$NAME
      NamesList http://www.python.org/cgi-bin/moinmoin/TitleIndex?action=titleindex
      KeyValue INVALIDATE-UPON-CHANGE-TO http://www.python.org/cgi-bin/moinmoin/LocalNamesDescription
      KeyValue ACCEPT-ADDITION-BY-FORM http://www.python.org/cgi-bin/moinmoin/$NAME

      OtherNameSpaces
        LibraryReference http://www.python.org/cgi-bin/moinmoin/LibraryReferencesNames?action=raw
        LibRef http://www.python.org/cgi-bin/moinmoin/LibraryReferencesNames?action=raw
        Modules http://www.python.org/cgi-bin/moinmoin/LibraryReferencesNames?action=raw

      DefaultNameSpaces
        LibraryReference

INVALIDATE-UPON-CHANGE-TO: Means if a local nameserver somehow hears that the given URL has changed, to invalidate it\'s cache of the namespace.

ACCEPT-ADDITION-BY-FORM: Means if a local nameserver somehow hears that a URL has been added of the given form, to add it to the namespace description.

      LastResortNamePattern http://www.python.org/cgi-bin/moinmoin/$NAME
