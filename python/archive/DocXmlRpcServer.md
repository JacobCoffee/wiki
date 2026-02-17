# DocXmlRpcServer

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

The DocXmlRpcServer is a *very* simple [XmlRpc](XmlRpc) server that is also simultaneously a self-documenting web server.

:::: 
::: 
``` 
   1 """Demonstration of the Python 2.3 DocXMLRPCServer.
   2 
   3 The demonstration publishes two functions, "message" and "wait."
   4 """
   5 
   6 import time
   7 import socket
   8 
   9 from DocXMLRPCServer import DocXMLRPCServer
  10 
  11 
  12 class SimpleShareServer:
  13     def message(self, msg):
  14         """Print message and return True.
  15 
  16         Log everything passed to this function.
  17         """
  18         print time.asctime(), msg
  19         return True
  20 
  21     def wait(self, seconds):
  22         """Wait a number of seconds, and return the number.
  23 
  24         Wait for a certain number of seconds before returning.
  25         Returns the same number passed in.
  26         """
  27         print time.asctime(), "Waiting %s seconds" % seconds
  28         time.sleep(seconds)
  29         print time.asctime(), "Finished waiting %s seconds" % seconds
  30         return seconds
  31 
  32     
  33 if __name__ == '__main__':
  34     server = DocXMLRPCServer(("", 8000), logRequests=0)
  35     server.register_introspection_functions()
  36     server.register_instance(SimpleShareServer())
  37 
  38     print time.asctime(), 'Application Starting.'
  39     server.serve_forever()
  40     print time.asctime(), 'Application Finishing.'
```
:::
::::

The benefit of using DocXMLRPCServer is that it automatically creates documentation for your XML-RPC server, just open a browser and head to [http://localhost:8000](http://localhost:8000) after starting the server.

Writing a client to call the wait function is left as an exercise for the reader. ![:)](/wiki/europython/img/smile.png ":)")

## Resources 

- [XmlRpc](XmlRpc) \-- general information on XML-RPC

- [BaseHttpServer](BaseHttpServer) \-- class that DocXmlRpcServer inherits from

- [SimpleXMLRPCServer documentation](http://www.python.org/doc/current/lib/module-SimpleXMLRPCServer.html)

- [DocXMLRPCServer documentation](http://www.python.org/doc/current/lib/module-DocXMLRPCServer.html)

- `SimpleXMLRPCServer.py`, and `DocXMLRPCServer.py` - comments includ many examples of use

- [Fast C implementation of XML-RPC for python](http://sourceforge.net/projects/py-xmlrpc/) (only for python version up to 2.2) [(more notes on it- apparently 20-100x faster!)](http://www.xmlrpc.com/discuss/msgReader$1573)

Also:

- [AutoXmlRpcServer](AutoXmlRpcServer) \-- automatically serve modules in local directory with DocXmlRpcServer

## Notes 

This page was based on [SeaPig:DocXMLRPCServer,](http://www.seapig.org/DocXMLRPCServer) with [BrianDorsey](BrianDorsey)\'s permission.

# Discussion 

(none yet!)
