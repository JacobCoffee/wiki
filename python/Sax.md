# Sax

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

\"Sax\" is an XML parser that operates element by element, line by line.

[MiniDom](MiniDom) sucks up an entire XML file, holds it in memory, and lets you work with it. Sax, on the other hand, emits events as it goes step by step through the file.

**NOTE**: A similarly fast but much simpler way to extract information from an XML document in an event-driven, memory efficient fashion is [ElementTree.iterparse()](http://docs.python.org/library/xml.etree.elementtree.html#xml.etree.ElementTree.iterparse).

## Example 

:::: 
::: 
``` 
   1 import xml.sax
   2 
   3 class InkscapeSvgHandler(xml.sax.ContentHandler):
   4     def startElement(self, name, attrs):
   5         if name == "svg":
   6             for (k,v) in attrs.items():
   7                 print k + " " + v
   8 
   9 parser = xml.sax.make_parser()
  10 parser.setContentHandler(InkscapeSvgHandler())
  11 parser.parse(open("svg.xml","r"))
```
:::
::::

## Links 

- [HtmlParser](./HtmlParser.html) \-- similar module, tailored to HTML interpretation

- [Python Library Reference, xml.sax](http://docs.python.org/lib/module-xml.sax.html) \-- API documentation

- [Python XML FAQ and How-to](http://www.rexx.com/~dkuhlman/pyxmlfaq.html) \-- describes sax & [MiniDom](MiniDom)

- [SAX: The Simple API for XML](http://pyxml.sourceforge.net/topics/howto/section-SAX.html) \-- wordy tutorial

- [Charming Python:Revisiting XML tools for Python](http://www-106.ibm.com/developerworks/linux/library/l-pxml.html) \-- kind of old

- [Usings SAX for Proper XML Output](http://www.xml.com/pub/a/2003/03/12/py-xml.html)
