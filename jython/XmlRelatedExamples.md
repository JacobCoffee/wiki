# XmlRelatedExamples

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# Jython examples using Java XML classes 

[DocumentationAndEducation](DocumentationAndEducation)

------------------------------------------------------------------------

Examples related to Java XML classes using Jython will be here.

**List of pages in this category:**

- Something simple using dom4j
- Something else simple Jdom
- Others ?
- and of course Java SDK

## Element tree 

Here is a simple example. info on element tree is at [http://effbot.org/zone/element-index.htm](http://effbot.org/zone/element-index.htm)

Download element tree from [http://effbot.org/downloads/](http://effbot.org/downloads/)

    from  elementtree import ElementTree as ET

    root = ET.Element("html")
    head = ET.SubElement(root, "head")
    title = ET.SubElement(head, "title")
    title.text = "Page Title"
    body = ET.SubElement(root, "body")
    body.set("bgcolor", "#ffffff")
    body.text = "Hello, World!"
    tree = ET.ElementTree(root)
    tree.write("page.xhtml")

    import sys
    tree.write(sys.stdout)

which produces:

    <html><head><title>Page Title</title></head><body bgcolor="#ffffff">Hello, World!</body></html>

## dom4j

This example requires [http://www.dom4j.org/](http://www.dom4j.org/) the example below was tested with v1.6.1 download it and put it in you classpath.

This was posted to the Jython-users mailing list by Claude Falbriard Sep 14, 2007,

This simply prints out a xml tree. change line 39 to a valid xml filename.

    import sys
    from org.dom4j.io import SAXReader

    def show_indent(level):
        return '    ' * level

    def show_node(node, level):
        """Display one node in the DOM tree.
        """
        if node.getNodeType() == node.ELEMENT_NODE:
            name = node.getName()
            print '%sNode: %s' % (show_indent(level), name, )
            attrs = node.attributes()
            for attr in attrs:
                aName = attr.getQualifiedName()
                aValue = attr.getValue()
                print '  %sAttr -- %s: %s' % (show_indent(level), aName,aValue,)
        if node.getName() == 'RefNum':
            val = node.getText()
            print '%stitle: "%s"' % (show_indent(level+1), val, )
        elif node.getName() == 'link':
            val = node.getText()
            print '%slink    : "%s"' % (show_indent(level+1), val, )

        if node.getNodeType() == node.TEXT_NODE:
            print '**** text node'


    def show_tree(node, level):
        show_node(node, level)
        level1 = level + 1
        children = node.elements()
        for child in children:
            show_tree(child, level1)

    def test():
        print 'Version: %s' % (sys.version, )
        reader = SAXReader()
        doc = reader.read('example.xml')
        root = doc.getRootElement()
        show_tree(root, 0)

    def main():
        test()

    if __name__ == '__main__':
         main()

## Using Jython and jaxen XPath 

From: Frank Cohen Sent: Tuesday, June 03, 2008 10:34 PM

I needed to write a SOAP-based Web service to show off the SOAP testing capabilities for [PushToTest](./PushToTest.html) [TestMaker](./TestMaker.html). I wanted to use XPath expressions to change the search expressions easily over time. I chose to use Jaxen and Xerces APIs. Figuring this out in Java wound up taking a long time - all those visits to change-compile-run-check land! So I broke out my trusty Jython (embedded in [TestMaker](./TestMaker.html)) and wrote the following script.

I like example code. So I am posting this here to help anyone else that needs to do XPath expressions.

    from java.io import ByteArrayInputStream
    from org.apache.axis.utils import XMLUtils
    from org.apache.axis.message import MessageElement
    from java.lang import String
    from org.jaxen.dom import DOMXPath

    mystring = '''<change_price_response>
        <Inventory>
            <Product number="1000">
                <InStock>
                    <part quantity="2" location="10"/>
                    <part quantity="100" location="11"/>
                    <part quantity="10" location="12"/>
                </InStock>
                <OnOrder>
                    <order customer="100323" amount="2" ordernumber="988898"/>
                    <order customer="100115" amount="1" ordernumber="988899"/>
                    <order customer="100116" amount="10" ordernumber="988900"/>
                </OnOrder>
                <prices>
                    <price amount="100" minquantity="1"/>
                    <price amount="85" minquantity="10"/>
                    <price amount="75" minquantity="20"/>
                </prices>
            </Product>
        </Inventory>
     </change_price_response>'''

    soapElementAsString = String( mystring )
    myis = ByteArrayInputStream( soapElementAsString.getBytes() )
    respdoc = XMLUtils.newDocument( myis )

    myrq = '''<change_price>
         <Product number="1000">
             <Operation type="AddStock" quantity="100" location="11"/>
         </Product>
         </change_price>'''

    soapElementAsString = String( myrq )
    myis2 = ByteArrayInputStream( soapElementAsString.getBytes() )
    rqdoc = XMLUtils.newDocument( myis2 )
    #rqme = MessageElement( rqdoc.getDocumentElement() )

    xpath1 = DOMXPath( "//Product" )
    product_number = int( xpath1.selectSingleNode( rqdoc ).getAttribute("number") )

    print "fc1", xpath1.selectSingleNode( rqdoc ).getClass().getName()

    xpath2 = DOMXPath( "//Operation[@location]" )
    xpath2 = DOMXPath( "//Operation" )

    print "fc", xpath2.selectSingleNode( rqdoc ).getClass().getName()

    quantity = int( xpath2.selectSingleNode( rqdoc ).getAttribute("quantity") )
    location = int( xpath2.selectSingleNode( rqdoc ).getAttribute("location") )

    print product_number, quantity, location

    xpath3 = DOMXPath( "//Product" )
    xpath3.selectSingleNode( respdoc ).setAttribute( "number", str(product_number))

    xpath4 = DOMXPath( '//part[@location=' + str( location ) + ']' )
    xpath4.selectSingleNode( respdoc ).setAttribute( "quantity", str( quantity ))

    print "done"
