# BaseHttpServer

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# BaseHTTPServer 

You can use this to make a simple HTTP web server.

## Official Documentation 

- [BaseHTTPServer module documentation](http://docs.python.org/lib/module-BaseHTTPServer.html) - what we use directly

- [SocketServer module documentation](http://docs.python.org/lib/module-SocketServer.html) - behind the BaseHttpServer

## Example Code 

### Responding with an HTML Page 

:::: 
::: 
``` 
   1 import time
   2 import BaseHTTPServer
   3 
   4 
   5 HOST_NAME = 'example.net' # !!!REMEMBER TO CHANGE THIS!!!
   6 PORT_NUMBER = 80 # Maybe set this to 9000.
   7 
   8 
   9 class MyHandler(BaseHTTPServer.BaseHTTPRequestHandler):
  10     def do_HEAD(s):
  11         s.send_response(200)
  12         s.send_header("Content-type", "text/html")
  13         s.end_headers()
  14     def do_GET(s):
  15         """Respond to a GET request."""
  16         s.send_response(200)
  17         s.send_header("Content-type", "text/html")
  18         s.end_headers()
  19         s.wfile.write("<html><head><title>Title goes here.</title></head>")
  20         s.wfile.write("<body><p>This is a test.</p>")
  21         # If someone went to "http://something.somewhere.net/foo/bar/",
  22         # then s.path equals "/foo/bar/".
  23         s.wfile.write("<p>You accessed path: %s</p>" % s.path)
  24         s.wfile.write("</body></html>")
  25 
  26 if __name__ == '__main__':
  27     server_class = BaseHTTPServer.HTTPServer
  28     httpd = server_class((HOST_NAME, PORT_NUMBER), MyHandler)
  29     print time.asctime(), "Server Starts - %s:%s" % (HOST_NAME, PORT_NUMBER)
  30     try:
  31         httpd.serve_forever()
  32     except KeyboardInterrupt:
  33         pass
  34     httpd.server_close()
  35     print time.asctime(), "Server Stops - %s:%s" % (HOST_NAME, PORT_NUMBER)
```
:::
::::

### Responding with URL Redirection 

This code demonstrates simple URL redirection:

:::: 
::: 
``` 
   1 """
   2 URL redirection example.
   3 """
   4 
   5 import BaseHTTPServer
   6 import time
   7 import sys
   8 
   9 
  10 HOST_NAME = 'example.net' # !!!REMEMBER TO CHANGE THIS!!!
  11 PORT_NUMBER = 80 # Maybe set this to 9000.
  12 REDIRECTIONS = {"/slashdot/": "http://slashdot.org/",
  13                 "/freshmeat/": "http://freshmeat.net/"}
  14 LAST_RESORT = "http://google.com/"
  15 
  16 class RedirectHandler(BaseHTTPServer.BaseHTTPRequestHandler):
  17     def do_HEAD(s):
  18         s.send_response(301)
  19         s.send_header("Location", REDIRECTIONS.get(s.path, LAST_RESORT))
  20         s.end_headers()
  21     def do_GET(s):
  22         s.do_HEAD()
  23 
  24 if __name__ == '__main__':
  25     server_class = BaseHTTPServer.HTTPServer
  26     httpd = server_class((HOST_NAME, PORT_NUMBER), RedirectHandler)
  27     print time.asctime(), "Server Starts - %s:%s" % (HOST_NAME, PORT_NUMBER)
  28     try:
  29         httpd.serve_forever()
  30     except KeyboardInterrupt:
  31         pass
  32     httpd.server_close()
  33     print time.asctime(), "Server Stops - %s:%s" % (HOST_NAME, PORT_NUMBER)
```
:::
::::

## Parameterizing 

When you want to make your server respect some parameters, it\'s easiest to do so via the *server,* rather than the *handler.*

That is, make a subclass of the server, that accepts some additional parameters. Have the server record those parameters.

Then, in the handler, use `s.server` to get to the server, and access the parameters through it.

## See Also 

- [DocXmlRpcServer](DocXmlRpcServer) \-- self-documenting XML-RPC servers

- [CgiScripts](CgiScripts) \-- using invoked CGI scripts, rather than running micro-web servers

# Discussion 

I\'d ultimately like to see a BaseHttpServer here that can both handle XML-RPC requests (with *that* request handler,) and normal web requests (with a custom handler.)

Yes- I know and love [TwistedPython](./TwistedPython.html). But I want to make something that works in a single install. \-- [LionKimbro](LionKimbro) 2004-05-31 01:13:16

I\'d also like to add code here showing how to service a POST request.

\-- [LionKimbro](LionKimbro) 2004-07-03 23:07:53

There exist tools like [CherryPy](CherryPy) which will create a single-file Python HTTP server (based on BaseHTTPServer). This is a fair amount easier to work with than the raw BaseHTTPServer. For most cases, using a more complete framework will be preferable (see [WebProgramming](WebProgramming)). \-- [IanBicking](IanBicking)

I like the BaseHttpServer because it is in the default Python distributions. I encourage all work towards putting a standard web framework into the default Python distribution. I\'m not picky, just as long as something is chosen. \-- [LionKimbro](LionKimbro) 2005-01-25 04:53:53

What\'s the matter with server_close()? I can call the method, but it is undocumented (see [http://docs.python.org/lib/node634.html](http://docs.python.org/lib/node634.html)). Could someone knowledgable either remove the calls, or add a comment why they\'re necessary? Thanks. \-- Anonymous Coward, 23 Oct 2007
