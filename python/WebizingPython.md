# WebizingPython

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# Webizing Python 

This is a discussion about getting Python to merge Internet resources and Python.

# Ideas 

- syntax changes? are we interested in that?

- a basic URL type

- import hooks for importing from URLs (ex: [http://stdlib.python.org/2.3.4/pickle](http://stdlib.python.org/2.3.4/pickle))

- [NetworkedData](NetworkedData) - native data, networked across the Internet

- native support for [ComponentBus](http://c2.com/cgi/wiki?ComponentBus "Wiki") architectures - see notes below

- native inclusion of Twisted, or something like Twisted

------------------------------------------------------------------------

Importing a URL is a very bad idea. First, there are security issues, as you are executing code over which you don\'t have control. Also, you don\'t generally want libraries to be upgraded behind your back. The standard library gets upgraded, but a lot of work goes into keep that backward compatible \-- in other libraries, this isn\'t the case. You want to make upgrades explicit in that case. Languages that have the ability to import URLs \-- like PHP \-- almost never use it.

A URL literal doesn\'t seem particularly useful. It would provide an alternative to, say, `url('http://something.com/whatever')` (e.g., `<http://something.com/whatever>`), but since URLs tend to be dynamic or configurable, a literal doesn\'t add significant value. However, a good URL class would be excellent, maybe a class that has an API similar to the [path](http://www.jorendorff.com/articles/python/path/) module. It would be great if both modules were builtins (or at least in the standard library).

\-- [IanBicking](IanBicking)

Rather than be contrary again, I\'ll pose a question: what are the real benefits of importing from a URL, and from a URL/URI/URN literal? A URI object is of obvious value, but it\'s easy to imagine it being created from a string. What value is there in a literal? What can you do at the tokenizing step given a literal? What case is there for importing from a URL, when you take versions and security into account? (And C or Pyrex extensions, multiple installations, fast start-up times, unreliable network connections, etc) Like I mentioned, you can do it in PHP, but no one ever does.

\-- [IanBicking](IanBicking)

## XML literals 

Several languages have support for some kind of XML literal, including XEN, XDuce, o:XML, Comega, and others. More later.

## Networked Data 

Hi, my name is [LionKimbro](LionKimbro). I wrote a small hack module for [NetworkedData](NetworkedData). Basically, this means that a native data structure can expand, indefinitely, across the Internet. So if you have a list, for example, and three of the lists are defined elsewhere on the Internet, you can just tell those items to resolve, and they\'ll resolve *in place.* A master graph keeps records of how all the sub-graphs and data structures are connected.

It\'s *really cool* (if you ask me!), and you can read more about it on [NetworkedData](NetworkedData).

I would *love* to see something like this built into Python, Perl, PHP, etc., etc., etc.,. There\'s no need for us to be writing parsers over and over again, and communicating data in packages, when we can just post it to the Internet, and let the network take it from there.

You can build arbitrary objects by this system, because there is support (not in the implementation yet, but conceptual support) for function call resolution. Of course, you have to *allow* functions to run- you don\'t want just anyone creating just any object with any initializer- to dangerous. But you can say, \"allow this function to be called\...\" yadda yadda yadda.

\-- [LionKimbro](LionKimbro) 2004-07-21 00:14:01

## Component Bus Architecture support 

[StacklessPython](StacklessPython) would be a great place to start work on a built-in [ComponentBus](http://c2.com/cgi/wiki?ComponentBus "Wiki") architecture from.

What does this have to do with Webizing Python? Because these architectures are sort of just Micro-Internets, and naturally blend between the Internet and the programs space.

With these architectures, which are basically the same as hoards of computers connected by a bus (the Internet), but on a within-the-computer scale, naturally bleed into the Internet. By their very nature, it means you can just as well have a component within the computer, as outside of the computer, and the program would (ignoring pragmatics of bandwidth and stuff like that) run just the same.

Most programs, you\'d like people across the world to be able to observe some parts of. This implies an addressible space. Why hook up to an adaptor, when you could plug straight into the event bus (were permissions granted..)?

\-- [LionKimbro](LionKimbro) 2004-07-21 00:14:01

# References 

- [Tim Berner\'s Lee: Webizing Python](http://www.w3.org/2002/Talks/0206-python/all.htm)

- [Aaron Swartz: Webizing Python](http://logicerror.com/webizingPython) (native URIs, remote objects, URIs for objects)

- [Fredrik Lundh: XML literals](http://effbot.org/zone/idea-xml-literal.htm)

- [NetworkedData](NetworkedData), [nLSD graphs](http://onebigsoup.wiki.taoriver.net/moin.cgi/nLSDgraphs) (native data that extends across the network)
