# RssLibraries

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# Python RSS Code 

Articles:

- [The PythonWeb services developer: RSS for Python](http://www-106.ibm.com/developerworks/webservices/library/ws-pyth11.html)

- [http://codeboje.de/blog/archives/Feeds-and-python-II.html](http://codeboje.de/blog/archives/Feeds-and-python-II.html) - Short articles about using Universal Feed Parser

Libraries:

- [the Universal Feed Parser](http://code.google.com/p/feedparser/) - Reads 9 RSS versions and Atom

- [RSS.py](http://www.mnot.net/python/RSS.py) - reads most RSS versions, produces RSS 1.0

- [SpycyRoll](SpycyRoll) - I don\'t know much about - this is an *aggregator,* and perhaps other stuff as well

- [PyRSS2Gen](http://www.dalkescientific.com/Python/PyRSS2Gen.html) - produces RSS 2.0

## Feed Parser 

Feed Parser is an awesome RSS reader. It is now hosted on Google Code & Sourceforge - [Universal Feed Parser on Google Code](http://code.google.com/p/feedparser/) ([Project Page on SourceForge](http://sourceforge.net/projects/feedparser/)).

[Universal Feed Parser documentation](http://packages.python.org/feedparser/).

Download it, and then start a Python prompt in the same directory.

:::: 
::: 
``` 
   1 import feedparser
   2 
   3 python_wiki_rss_url = "http://www.python.org/cgi-bin/moinmoin/" \
   4                       "RecentChanges?action=rss_rc"
   5 
   6 feed = feedparser.parse( python_wiki_rss_url )
```
:::
::::

You now have the RSS feed data for the [PythonInfo](../archive/PythonInfo) wiki!

Take a look at it; There\'s a lot of data there.

Of particular interest:

::: {}
  ----------------------------------------- -------------------------------------------------------------------------------------------------
  `feed[ "bozo" ]`                          `1` if the feed data isn\'t well-formed XML.
  `feed[ "url" ]`                           URL of the feed\'s RSS feed
  `feed[ "version" ]`                       version of the RSS feed
  `feed[ "channel" ][ "title" ] `           `"PythonInfo Wiki"` - Title of the Feed.
  `feed[ "channel" ][ "description" ]`      `"RecentChanges at PythonInfo Wiki."` - Description of the Feed
  `feed[ "channel" ][ "link" ]`             Link to [RecentChanges](RecentChanges) - Web page associated with the feed.
  `feed[ "channel" ][ "wiki_interwiki" ]`   ``` "Python``Info" ``` - For wiki, the wiki\'s preferred [InterWiki](InterWiki) moniker.
  `feed[ "items" ]`                         A gigantic list of all of the [RecentChanges](RecentChanges) items.
  ----------------------------------------- -------------------------------------------------------------------------------------------------
:::

For each item in `feed["items"]`, we have:

::: {}
  -------------------------- -----------------------------------------------
  `item[ "date" ]`           `"2004-02-13T22:28:23+08:00"` - ISO 8601 date
  `item[ "date_parsed" ]`    `(2004,02,13,14,28,23,4,44,0)`
  `item[ "title" ]`          title for item
  `item[ "summary" ]`        change summary
  `item[ "link" ]`           URL to the page
  `item[ "wiki_diff" ]`      for wiki, a link to the diff for the page
  `item[ "wiki_history" ]`   for wiki, a link to the page history
  -------------------------- -----------------------------------------------
:::

## Aggregating Feeds with Feed Parser 

If you\'re pulling down a lot of feeds, and aggregating them:

First, you may want to use [Future threads](http://aspn.activestate.com/ASPN/Cookbook/Python/Recipe/84317) to pull down your feeds. That way, you can send out 5 requests immediately, and wait for them all to come back at once, rather than sending out a request, waiting for it to come in, send out another request, wait for it to come back in, etc., etc.,.

:::: 
::: 
``` 
   1 from future import Future
   2 
   3 hit_list = [ "http://...", "...", "..." ] # list of feeds to pull down
   4 
   5 # pull down all feeds
   6 future_calls = [Future(feedparser.parse,rss_url) for rss_url in hit_list]
   7 # block until they are all in
   8 feeds = [future_obj() for future_obj in future_calls]
```
:::
::::

Now that you have your feeds, extract all the entries.

:::: 
::: 
``` 
   1 entries = []
   2 for feed in feeds:
   3     entries.extend( feed[ "items" ] )
```
:::
::::

\...and sort them, by [SortingListsOfDictionaries](../archive/SortingListsOfDictionaries):

:::: 
::: 
``` 
   1 sorted_entries = sorted(entries, key=lambda entry: entry["date_parsed"])
   2 sorted_entries.reverse() # for most recent entries first
```
:::
::::

Congratulations! You\'ve aggregated a bunch of changes!

## Contributors 

[LionKimbro](LionKimbro)

## Links 

- [RawDog](http://offog.org/code/rawdog.html) is an RSS aggregator written in Python & using [Feed Parser](http://diveintomark.org/projects/feed_parser/)

- [Feedjack](http://www.feedjack.org/) Planet like Feed aggregator using Universal Feed Parser and the django webframework

## Discussion 

Getting the \"author\"/\"contributor\" out of most [ModWiki](./ModWiki.html) RSS feeds with the feedparser module is a bit confusing as of now. Right now (feedparser 3.3), it goes into the \"rdf_value\" attribute of the entry.

------------------------------------------------------------------------

I\'m moving the following out of the main text:

- [RawDog](./RawDog.html) is a ready made aggregator if you don\'t want to write your own.

Are you concerned that I\'m encouraging people to reduplicate efforts, making aggregator after aggregator after aggregator?

That\'s not the case; there are good reasons to write aggregators yet.

In particular: I wrote the code because I needed a [MoinMoin](MoinMoin) macro that aggregated RSS feeds.

I imagine that there are other good reasons to write aggregating code.

That said, [RawDog](./RawDog.html) *is* Python, and it *is* using Feed Parser, so I\'ve linked it at the bottom of the page.

\-- [LionKimbro](LionKimbro) 2004-12-27 08:44:40

------------------------------------------------------------------------

Next, I moved this out of the main text:

- Usually, such performance is not necessary, unless you have thousands of feeds to retrieve every hour. If you have less than a few hundred feeds an hour to retrieve, one a time is probably better - why peak out your processor/bandwidth?

This makes sense if you\'re just writing a client aggregator for reading blogs. But if you\'re compiling parts of a web page, then you want to generate a response within 20 seconds, not 3 minutes.

Similarly, I\'m removing:

- Other things to help you be polite:
  - try and retrieve things a few times a day or week. don\'t request hourly updates unless you need them.

  - avoid updates on the hour or half hour. Try a random time into the hour, like 27 or 33 or whatever, or poll at an interval like 693 minutes rather than 600, so that only rarely do you poll sites near the hour boundry. It is problematic for sites to get polled by hundreds of aggregators on the hour.

  - be sure to use [HttpConditionalGetRequests](./HttpConditionalGetRequests.html) and honour content-expires response flags

  - be sure to support [HttpCompression](./HttpCompression.html) in the responses.

Maybe there\'s some other page on some other wiki where this belongs. I don\'t think that space is here.

I\'m mainly concerned here with giving an example of how the RSS library works, the kinds of things you can do with it, how to combine it\'s use with the Futures module.

This isn\'t really about writing aggregators.

\-- [LionKimbro](LionKimbro) 2004-12-27 08:44:40

------------------------------------------------------------------------

Can someone please give a sample of how [FeedParser](./FeedParser.html) works along with Future Threads to make an RSS AGGREGATOR.

Manasa

------------------------------------------------------------------------
