# CgiScripts

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# CGI (Common Gateway Interface) Scripts 

The **cgi module** is part of the core library of Python.

- [cgi module (Python 2.x)](https://docs.python.org/2/library/cgi.html)

- [cgi module (Python 3.x)](https://docs.python.org/3/library/cgi.html)

The simplest CGI script that can be considered interesting involves printing out an HTTP header (\"Content-type: text/html\") and a Web page. In addition, you might want to handle any incoming inputs from things like HTML forms or request parameters. In the earliest days of CGI, shell scripts were sometimes used to do things like this, so the principles are not particularly advanced.

## Configuration 

It can be an annoying experience getting the permissions just right on a script so that Web servers like Apache will run it, but the following checklist may be of some use:

1.  Find out which user runs the Web server - it\'s not often the same one as your own user, and it may be one with very limited permissions.

2.  Check the server configuration to see if it lets you run scripts in a particular directory. Make sure that if you\'re using a configuration file for a particular directory, the global configuration permits you to define CGI script directories in that directory-local configuration file - some sites stop their users from altering such settings in such a way.

3.  Check the permissions from the top of the filesystem down to the directory where the script resides. The Web server user must be able to read and open/execute all the directories from the top right down to the script.

4.  Make sure your script is readable and executable by the Web server user.

5.  Make sure that the first line of the script refers to an interpreter that the Web server user can run. Things like `/usr/bin/env python` might not have any meaning to the Web server user because the `python` program may not be on the user\'s `PATH`.

In addition you should make sure your script has the correct \*\*line endings\*\* for your server.

## Sample Code 

The following code attempts to combine simple output of a Web page with the processing of input from users viewing the page. You may wish to choose the actual first line of the script based on one of the first two lines provided below - the first one for Windows and dependent on the Python install path, whereas the second may only work on UNIX-like systems.

:::: 
::: 
``` 
   1 #!C:\Python27\python.exe -u
   2 #!/usr/bin/env python
   3 
   4 import cgi
   5 import cgitb; cgitb.enable()  # for troubleshooting
   6 
   7 print "Content-type: text/html"
   8 print
   9 
  10 print """
  11 <html>
  12 
  13 <head><title>Sample CGI Script</title></head>
  14 
  15 <body>
  16 
  17   <h3> Sample CGI Script </h3>
  18 """
  19 
  20 form = cgi.FieldStorage()
  21 message = form.getvalue("message", "(no message)")
  22 
  23 print """
  24 
  25   <p>Previous message: %s</p>
  26 
  27   <p>form
  28 
  29   <form method="post" action="index.cgi">
  30     <p>message: <input type="text" name="message"/></p>
  31   </form>
  32 
  33 </body>
  34 
  35 </html>
  36 """ % cgi.escape(message)
```
:::
::::

## See Also 

- [WebProgramming](../web/WebProgramming) - the natural next step beyond simple CGI scripts.

- [cgi module documentation](http://www.python.org/doc/current/lib/module-cgi.html)

- [Cookie module documentation](http://www.python.org/doc/current/lib/module-Cookie.html)

- [Python CGI tutorial](http://webpython.codepoint.net/) - setup in a shared host, forms, debug, shell commands, cookies, etc

- [python CGI tutorial](http://www.cs.virginia.edu/~lab2q/lesson_7/) - w/ hints about maintaining sessions either through forms or through cookies

- [python CGI tutorial](http://gnosis.cx/publish/programming/feature_5min_python.html) - w/ hints about printing out tracebacks

- [other internet protocol module documentation](http://www.python.org/doc/current/lib/internet.html)

- [Writing CGI Scripts in Python](http://www.devshed.com/index2.php?option=content&task=view&id=198&pop=1&page=0&hide_js=1)

- [Voidspace Python CGI collection](http://www.voidspace.org.uk/python/cgi.shtml) - Working Python CGI scripts to use and/or study

------------------------------------------------------------------------

## Discussion 

- We need a good python CGI framework - Sridhar R
  - Nevow and [Wallaby](http://srid.bsdnerds.org/hacking/wallaby/) Define \"framework,\" though. Do you mean something like a Django-type deal or something that just makes it easier to write CGI apps?

------------------------------------------------------------------------

Yes\....

There are many frameworks for Python Web Application [TurboGears](../web/TurboGears) Django Zope [ModPython](ModPython) Pso Aquarium Cheetah ++++++\...

But it would be Nice if python provides native support for Session Handling, JSON - like XML-RPC Standard Environment for RPC + WSGI and future technologies\.... for Easy Web Development

-Vinoth [vinoth.3v@gmail.com](mailto:vinoth.3v@gmail.com)

Many shared hosting servers do not allow persistent processes. They kill a script if it runs for more than 3 minutes. This frameworks do not explain (or make life easier) for someone who as only cgi and ftp. Do you know any way to code easier/faster in this circumstances ? Osvaldo

------------------------------------------------------------------------

[CategoryPythonWebsite](CategoryPythonWebsite)
