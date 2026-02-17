# XmlRpc

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# XML-RPC 

XML-RPC is a neat way to send messages across the Internet.

The neat thing about XML-RPC is that it transports *native data structures*- you can ship off lists, strings, dictionaries, and numbers.

You can [read more about it over on C2,](http://c2.com/cgi/wiki?XmlRpc "Wiki") or on [the XML-RPC home page.](http://www.xmlrpc.com/)

## Sample Code 

:::: 
::: 
``` 
   1 import xmlrpclib
   2 
   3 XMLRPC_SERVER_URL = "http://www.python.org/cgi-bin/moinmoin/?action=xmlrpc"
   4 
   5 pythoninfo = xmlrpclib.ServerProxy( XMLRPC_SERVER_URL )
   6 allpages = pythoninfo.getAllPages() # this is the XML-RPC call
   7 
   8 print ", ".join( allpages )
```
:::
::::

This code calls the [PythonInfo](PythonInfo) wiki, and receives the [TitleIndex](TitleIndex) as a list.

## Message Format 

If you can communicate strings, you can do XML-RPC. You could even do it by e-mail!

Here\'s how to make your string:

:::: 
::: 
``` 
   1 import xmlrpclib
   2 
   3 func_name = "foo"
   4 arg_1 = "robot"
   5 arg_2 = { "some":1, "dict":2 }
   6 arg_3 = [1,2,3,4,5]
   7 
   8 call_string = xmlrpclib.dumps( (arg_1,arg_2,arg_3,), func_name )
```
:::
::::

\...resulting in the following `call_string` value:

    <?xml version='1.0'?>
    <methodCall>
    <methodName>foo</methodName>
    <params>
    <param>
    <value><string>robot</string></value>
    </param>
    <param>
    <value><struct>
    <member>
    <name>dict</name>
    <value><int>2</int></value>
    </member>
    <member>
    <name>some</name>
    <value><int>1</int></value>
    </member>
    </struct></value>
    </param>
    <param>
    <value><array><data>
    <value><int>1</int></value>
    <value><int>2</int></value>
    <value><int>3</int></value>
    <value><int>4</int></value>
    <value><int>5</int></value>
    </data></array></value>
    </param>
    </params>
    </methodCall>

\...which can then be turned *back* into Python data:

:::: 
::: 
``` 
   1 call_data = xmlrpclib.loads( call_string )
```
:::
::::

\...which then builds:

    (('robot', {'some': 1, 'dict': 2}, [1, 2, 3, 4, 5]), u'foo')

That is, the first item is the arguments tuple, and the second item is the name of the function.

The capabilities are described under \"Convenience Functions\" in [the xmlrpclib documentation.](http://docs.python.org/lib/module-xmlrpclib.html)

## See Also 

- [official xmlrpclib example](http://docs.python.org/lib/xmlrpc-client-example.html)

- [xmlrpclib documentation](https://docs.python.org/2/library/xmlrpclib.html)

- [XML-RPC: It Works Both Ways (onlamp.com)](http://www.onlamp.com/pub/a/python/2001/01/17/xmlrpcserver.html)

- [DocXmlRpcServer](DocXmlRpcServer) - class to help make an XML-RPC server

- [Providing XML-RPC Services via CGI](http://effbot.org/zone/xmlrpc-cgi.htm)
