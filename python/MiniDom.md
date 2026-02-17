# MiniDom

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

**NOTE**: Some people think that MiniDOM is a slow and very memory hungry DOM implementation. According to these people, if you are looking for a fast, memory efficient and simple to use tool for working with XML, try [ElementTree](ElementTree) instead (in the [xml.etree](http://docs.python.org/library/xml.etree.elementtree.html) package), or use the external [lxml](http://lxml.de/) implementation.

Some notes on how to use `xml.dom.minidom`:

:::: 
::: 
``` 
   1 from xml.dom.minidom import parse, parseString
   2 
   3 dom1 = parse( "foaf.rdf" )   # parse an XML file
   4 dom2 = parseString( "<myxml>Some data <empty/> some more data</myxml>" )
   5 print dom1.toxml()
   6 print dom2.toxml()
```
:::
::::

## Examples of Use 

- node.nodeName
- node.nodeValue
- node.childNodes

### Find Elements 

You can manually walk through the `childNodes` tree, comparing `nodeName`s.

You might be able to use `getElementsByTagName` as well:

:::: 
::: 
``` 
   1 from xml.dom.minidom import parse
   2 dom = parse("foo.xml")
   3 for node in dom.getElementsByTagName('bar'):  # visit every node <bar />
   4     print node.toxml()
```
:::
::::

`getElementsByTagName` finds all children of a given name, no matter how deep, thus working recursively. This is usually good, but can cause problems if similar nodes exist at multiple levels and the intervening nodes are important.

### Add an Element 

Create & add an XML element (Something like `<foo />`) to an XML document.

:::: 
::: 
``` 
   1 from xml.dom.minidom import parse
   2 dom = parse("bar.xml")
   3 x = dom.createElement("foo")  # creates <foo />
   4 dom.childNodes[1].appendChild(x)  # appends at end of 1st child's children
   5 print dom.toxml()
```
:::
::::

### Add an Element with Text Inside 

Create & add an XML element to an XML document, the element has text inside.

ex: `<foo>hello, world!</foo>`

:::: 
::: 
``` 
   1 from xml.dom.minidom import parse
   2 dom = parse("bar.xml")
   3 x = dom.createElement("foo")  # creates <foo />
   4 txt = dom.createTextNode("hello, world!")  # creates "hello, world!"
   5 x.appendChild(txt)  # results in <foo>hello, world!</foo>
   6 dom.childNodes[1].appendChild(x)  # appends at end of 1st child's children
   7 print dom.toxml()
```
:::
::::

### Import a Node 

You can use DOM 2 \"importNode\" to take part of one XML document, and put it into another XML document.

:::: 
::: 
``` 
   1 from xml.dom.minidom import parse
   2 dom1 = parse("foo.xml")
   3 dom2 = parse("bar.xml")
   4 x = dom1.importNode(dom2.childNodes[1],  # take 2nd node in "bar.xml"
   5                     True)  # deep copy
   6 dom1.childNodes[1].appendChild(x)  # append to children of 2nd node in "foo.xml"
   7 print dom1.toxml()
```
:::
::::

## Links 

- [Python Library Reference, xml.dom.minidom](http://docs.python.org/lib/module-xml.dom.minidom.html) \-- API documentation

- [Dive into Python, Chapter 5](http://www.faqs.org/docs/diveintopython/kgp_divein.html#kgp.divein) \-- works almost entirely out of the minidom API

## See Also 

- [Sax](Sax), [PythonXml](PythonXml)
