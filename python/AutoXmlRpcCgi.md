# AutoXmlRpcCgi

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

This is a CGI version of the \"automatic [DocXmlRpcServer](DocXmlRpcServer).\"

## Tutorial 

Suppose you have a Python module:

:::: 
::: 
``` 
   1 def spam():
   2     return "spam"
```
:::
::::

How can we quickly share this functionality?

Mark it like this:

:::: 
::: 
``` 
   1 XMLRPC_namespace = "eggs"
   2 
   3 def spam():
   4     return "spam"
```
:::
::::

Now, put that script, and the AutoXmlRpcCgi script, into a CGI directory. You\'re done!

You can use that function via XML-RPC on the CGI.

Your friends can now call your function!

:::: 
::: 
``` 
   1 import xmlrpclib
   2 
   3 server = xmlrpclib.ServerProxy("http://example.net/xrcgi.py")
   4 print server.eggs.spam()
```
:::
::::

There it is!

## Notes 

- If you set XMLRPC_namespace to None, then namespaces aren\'t used.

- This code demonstrates [ModulesAsPlugins](ModulesAsPlugins), [CgiScripts](CgiScripts), [DocXmlRpcServer](DocXmlRpcServer), and (hopefully) [PythonStyle](PythonStyle).

- If you define a function \"uli\" (`def uli(msg):`), you can call it in IRC with [UliBot!](http://onebigsoup.wiki.taoriver.net/moin.cgi/UliBot)

## Code: xrcgi.py 

:::: 
::: 
``` 
   1 #!/usr/bin/env python2.4
   2 """CGI between XML-RPC web requests, and specially marked modules.
   3 
   4 This script is a gateway (CGI) between web XML-RPC requests, and
   5 Python modules that define "XMLRPC_namespace".
   6 
   7 Functions within Modules that define the name "XMLRPC_namespace" are
   8 accessible by XML-RPC. Function names that begin with an underscore (ex:
   9 _eggs) are not published. Functions are published within the XML-RPC
  10 namespace designated by the XMLRPC_namespace value, or the base
  11 namespace if the value is None.
  12 """
  13 
  14 import time
  15 import os
  16 import imp
  17 import types
  18 
  19 import DocXMLRPCServer
  20 
  21 
  22 def find_modules(path="."):
  23     """Return names of modules in a directory.
  24 
  25     Returns module names in a list. Filenames that end in ".py" or
  26     ".pyc" are considered to be modules. The extension is not included
  27     in the returned list.
  28     """
  29     modules = set()
  30     for filename in os.listdir(path):
  31         module = None
  32         if filename.endswith(".py"):
  33             module = filename[:-3]
  34         elif filename.endswith(".pyc"):
  35             module = filename[:-4]
  36         if module is not None:
  37             modules.add(module)
  38     return list(modules)
  39 
  40 
  41 def load_module(name, path=["."]):
  42     """Return a named module found in a given path."""
  43     (file, pathname, description) = imp.find_module(name, path)
  44     return imp.load_module(name, file, pathname, description)
  45 
  46 
  47 def find_xmlrpc_modules():
  48     """Find modules that define XMLRPC_namespace.
  49 
  50     Loads all modules in the current working directory. Returns a list
  51     of modules, the modules that define XMLRPC_namespace.
  52     """
  53     modules = [load_module(m) for m in find_modules()]
  54     xmlrpc_modules = []
  55     for m in modules:
  56         if m.__dict__.has_key("XMLRPC_namespace"):
  57             xmlrpc_modules.append(m)
  58     return xmlrpc_modules
  59 
  60 
  61 def functions_in_module(module):
  62     """Find all functions in a module."""
  63     functions = []
  64     for obj in module.__dict__.values():
  65         if isinstance(obj, types.FunctionType):
  66             functions.append(obj)
  67     return functions
  68 
  69 
  70 if __name__ == "__main__":
  71     handler = DocXMLRPCServer.DocCGIXMLRPCRequestHandler()
  72 
  73     for module in find_xmlrpc_modules():
  74         for func in functions_in_module(module):
  75             if func.__name__.startswith("_"):
  76                 continue
  77             full_name = func.__name__
  78             if module.XMLRPC_namespace is not None:
  79                 full_name = "%s.%s" % (module.XMLRPC_namespace,
  80                                        full_name)
  81             handler.register_function(func, full_name)
  82 
  83     handler.set_server_title("xrserver")
  84     handler.register_introspection_functions()
  85     handler.register_multicall_functions()
  86     handler.handle_request()
```
:::
::::

# Discussion 

This could be improved. Some ideas:

- What if there\'s an exception while loading a module? What then?
- Log modules successfully loaded.
  - If you\'re either brave or insane, make use of the [LoggingModule](./LoggingModule.html).
- Perhaps perform some sort of caching, to speed up invocation.

\-- [LionKimbro](LionKimbro) 2005-04-17 05:51:41
