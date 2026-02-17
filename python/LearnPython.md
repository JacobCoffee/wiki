# LearnPython

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

**Learning python by example**

# Python XML & XSLT 

## Create and add elements 

    from xml.dom.minidom import parseString

- creating new document, and root element at the same time.

<!-- -->

    doc = parseString(u'<top/>'.encode('UTF-8'))

- print doc.toprettyxml() will show you how it looks
- this would create:

<!-- -->

    <?xml version="1.0" ?>
    <top/>

- Now we reference to our \<top/\> element by:

<!-- -->

    top_element=doc.documentElement

- We create another element by:

<!-- -->

    element1=doc.createElementNS(None,u'section1')

- Add it under our top element by:

<!-- -->

    top_element.appendChild(element1)

- Create another element and add it under element1

<!-- -->

    element1.appendChild(doc.createElementNS(None,u'subsection1'))

- How to create a text node:

<!-- -->

    text1=doc.createTextNode(u'My first text')

- Since we have no reference to subsection1. We start at reference to element1

<!-- -->

    element1.firstChild.appendChild(text1)

- add second subelement:

<!-- -->

    element1.appendChild(doc.createElementNS(None,u'subsection2'))

- create next text element, and add it to subsection2

<!-- -->

    text2=doc.createTextNode(u'My second text')
    element1.lastChild.appendChild(text2)

- We are working with references. To switch text in subsections, you could do:

<!-- -->

    element1.firstChild.appendChild(text2)
    element1.lastChild.appendChild(text1)
