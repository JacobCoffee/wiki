# PullDom

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# The pulldom Module 

The `xml.dom.pulldom`{.backtick} module [(API)](http://docs.python.org/lib/module-xml.dom.pulldom.html) provides a \"pull parser\" which can also be asked to produce DOM-accessible fragments of the document where necessary. The basic concept involves pulling \"events\" from a stream of incoming XML and processing them, although in contrast to [SAX](./self(3a)Sax.html) which also employs an event-driven processing model together with callbacks, the user of a pull parser is responsible for explicitly pulling events from the stream, looping over those events until either processing is finished or an error condition occurs.

The example below corresponds to the \"Find Elements\" example in the [MiniDom](MiniDom) introduction.

:::: 
::: 
``` 
   1 from xml.dom.pulldom import START_ELEMENT, parse
   2 
   3 doc = parse("foo.xml")
   4 for event, node in doc:
   5     if event == START_ELEMENT and node.localName == "bar":
   6         doc.expandNode(node)
   7         print node.toxml()
```
:::
::::

Since the document is treated as a \"flat\" stream of events, the document \"tree\" is implicitly traversed and the desired elements are found regardless of their depth in the tree. In other words, one need not consider hierarchical issues such as recursive searching of the document nodes, although if the context of elements were important, one would either need to maintain some context-related state (ie. remembering where one is in the document at any given point) or to make use of the `expandNode`{.backtick} method and switch to DOM-related processing.

## Resources 

- [Tip: Using pull-based DOMs](https://www.ibm.com/developerworks/xml/library/x-tipulldom/index.html) - a description of the concept plus an example using the module

- [About PullDOM and MiniDOM](http://www.prescod.net/python/pulldom.html) - a concise description of the benefits of the module, although some details are now out-of-date
