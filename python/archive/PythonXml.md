# PythonXml

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

## Python and XML 

A variety of XML processing solutions are available for Python. This page attempts to list the major tools.

### Packages in the standard library 

The standard library has a number of tools available, which fall into mainly three categories:

- a pythonesque, simple-to-use and very fast XML tree library:
  - [ElementTree](../people/ElementTree) - the [xml.etree](http://docs.python.org/library/xml.etree.elementtree.html) package (new in Python 2.5 but available for older versions, also see the fast xml.etree.cElementTree and the independent implementation [lxml](http://lxml.de/))
- event-driven XML parsers:
  - [ElementTree](../people/ElementTree)\'s [iterparse()](http://docs.python.org/library/xml.etree.elementtree.html#xml.etree.ElementTree.iterparse) - a fast and easy-to-use event-driven parser with a high-level XML tree interface

  - pyexpat - a fast, low-level XML parser with an event-based callback interface

  - [Sax](Sax) - the xml.sax package, a Python implementation of the well-known low-level SAX API
- XML tree libraries that adhere to the W3C DOM standard:
  - [MiniDom](../people/MiniDom) - the xml.dom.minidom package

  - [PullDom](../people/PullDom) - the xml.dom.pulldom package

The DOM and SAX packages have the advantage of being compatible with standard or de facto standard APIs, so users who are already familiar with these APIs can use them without learning too many new things. Everyone else should start with the faster and more pythonic [ElementTree](../people/ElementTree) library, which is very well integrated into the Python language, and therefore very easy to learn and use.

### External packages 

A long list of special purpose and general purpose Python XML packages is available from [PyPI](http://pypi.python.org/pypi?:action=browse&show=all&c=500). The following is a choice of major tools that support a broader set of XML features.

#### Pythonic tools 

- [lxml](http://lxml.de/) - a pythonic, [ElementTree](../people/ElementTree)-compatible binding for the [libxml2](http://xmlsoft.org/) and [libxslt](http://xmlsoft.org/XSLT/) libraries that comes with all sorts of powerful XML (and HTML) tools, well integrated into an easy-to-use Python API

- [lxml.objectify](http://lxml.de/objectify.html) - a Python object API for XML based on lxml

- [PyXB](http://pyxb.sourceforge.net/) - generates Python classes/modules that correspond to data structures/namespaces defined by XMLSchema, with validation

- [PyXSD](http://pyxsd.org/) - an XML Schema mapping too (somewhat dated, last released in 2006)

- [generateDS](http://www.rexx.com/~dkuhlman/generateDS.html) - generates Python data structures (for example, class definitions) from an XML Schema document

- [Amara 2.x](http://xml3k.org/Amara) - Amara provides tools you can trust to conform with XML standards without losing the familiar Python feel

#### W3C DOM-like libraries 

- [PyXML](http://sourceforge.net/projects/pyxml/) - external add-on to Python\'s original XML support - (Warning: no longer maintained, does not work with recent Python versions)

- [itools.xml](http://www.ikaaro.org/itools/) - itools provides XML processing support in a fashion similar to that of [PullDom](../people/PullDom)

- [libxml2dom](http://www.python.org/pypi/libxml2dom) - PyXML-style API for the libxml2 Python bindings

- [qtxmldom](http://www.python.org/pypi/qtxmldom) - PyXML-style API for the qtxml Python bindings

- [4Suite](http://4suite.org/) - a framework for XML (and RDF) processing

#### XPath Support 

- [py-dom-xpath](http://code.google.com/p/py-dom-xpath/) - pure Python XPath implementation for use with DOM libraries

- [lxml](http://lxml.de/) - lxml has standards compliant XPath 1.0 support based on libxml2. It also supports the [EXSLT](http://www.exslt.org/) extensions (including Python regular expressions) and allows calling Python functions from within XPath expressions.

- [Amara 2.x](http://xml3k.org/Amara2) - Amara exposes an API to fully-compliant XPath (including [EXSLT](http://www.exslt.org/))

- [SaxonC](https://www.saxonica.com/saxon-c/documentation12/index.html) from Saxonica includes a Python API with full support for XPath 3.1.

#### XSLT Support 

If not mentioned otherwise, this means XSLT 1.0, not XSLT 2.0.

- [lxml](http://lxml.de/) has excellent (and easy-to-use) XSLT support that is based on [libxslt](http://xmlsoft.org/XSLT/). It also supports calling into Python code from XSL transformations through both XPath and XSLT extensions.

- [XSLTools](http://www.python.org/pypi/XSLTools) - XSL transformations on top of [libxslt](http://xmlsoft.org/XSLT/) and [libxml2dom](http://www.python.org/pypi/libxml2dom), with added Web development support

- Some tools linked from the [XQuery homepage](http://www.w3.org/XML/Query/#implementations) provide Python bindings for their XSLT2 and XPath2 implementations

- [Amara 2.x](http://xml3k.org/Amara2) - Amara exposes an API to fully-compliant XSLT (including [EXSLT](http://www.exslt.org/))

- [SaxonC](https://www.saxonica.com/saxon-c/documentation12/index.html) from Saxonica includes a Python API with full support for XSLT 3.0

#### XML-based Communications 

- [jabber.py](http://jabberpy.sourceforge.net/) - a Python module for the jabber instant messaging protocol

- [PyXMPP](http://pyxmpp.jajcus.net/) - a Python XMPP (RFC 3920,3921) and [Jabber](http://www.jabber.org/protocol/) implementation

- [xmpppy](http://xmpppy.sourceforge.net/) - a Python library that is targeted to provide easy scripting with Jabber

#### Web Services 

- [XmlRpc](../networking/XmlRpc)

  - [DocXmlRpcServer](DocXmlRpcServer)

- see [WebServices](../people/WebServices)

#### Object Serialization in XML 

- [pyxser](http://coder.cl/software/pyxser/) - a Python extension to serialize/deserialize Python objects into XML

### Books and Articles 

- [XmlBooks](../people/XmlBooks)

- [Tutorials on XML processing with Python](Tutorials%20on%20XML%20processing%20with%20Python)

### SIG 

- [http://python.org/community/sigs/current/xml-sig](http://python.org/community/sigs/current/xml-sig)

### Editorial Notes 

The above lists should be arranged in ascending alphabetical order - please respect this when adding new entries. When specifying release dates please use the format YYYY-MM-DD.
