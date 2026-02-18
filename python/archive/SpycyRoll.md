# SpycyRoll

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

Web site: [http://spycyroll.sourceforge.net/](http://spycyroll.sourceforge.net/)

I don\'t know much about SpycyRoll, except that it\'s an RSS aggregator of some sort. Though, looking through the code, I also saw a logger, so I\'m not sure what that\'s about.

Neat things:

- It aggregates RSS feeds, so you don\'t have to!

- It seems to do well at [WorkingWithTime](../archive/WorkingWithTime). Glancing at the time interpreter, it seemed to be pretty intelligent. I don\'t think ISO8601 time zones are going to fool it, or whatever else is predominant in RSS feeds.

Questions about it:

- Does this go *far beyond* aggregating? For example, does it not just aggregate the feeds, but produce HTML as if you were using this [PythonModule](./PythonModule.html) as your very own personal news aggregator?

- Is this something that is meant to run alone, or is this something that you can reuse in your own code. For instance, could you get a bunch of RSS feeds, mix them together and sort them by date, and then output the result in your own custom way?

I wish they had a wiki for their project.

We really need a nice easy RSS module, or collection of modules, that reads everything, and allows you to do everything RSS. That\'d be nice. See [RssLibraries](RssLibraries).

\-- [LionKimbro](LionKimbro) 2004-04-16 08:37:29
