# HelpSystem

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

[RyanMorillo](./RyanMorillo.html) is adding the help function from CPython to Jython as a [Google Summer of Code project](http://code.google.com/soc/psf/appinfo.html?csaid=12DAE7AC0028DD13) mentored by [CharlieGroves](CharlieGroves). In addition to exposing help for Python code as in CPython, we\'re going to try to add the ability to show help for Java code from their javadocs.

## Roughest of Plans 

1.  Add the help function to Jython
    - The help function in Python is implemented in site.py as a call into pydoc.help. We\'ll need to add the helper function and pydoc to Jython. With the current Jython (2.2b1) the previous issues with future div (A//B) are gone, leaving just the need for the inclusion of opcode.py, pydoc.py, dis.py and inspect.py and (The hard part) converting \$Python_Src/Modules/operator.c to Java for attrgetter. Further dependencies require research.
2.  Fill in the docs for builtin Jython types
    - The builtin types from Python implemented in Java in Jython(str, list, dict and the like) are missing their docstrings. We\'ll need to add these to the templating system we\'re using(src/templates in a trunk checkout) to get the basic types look decent in help.
3.  Add functionality to help to get it to work on introspected Java classes
    - Jython already uses reflection to figure out how to expose methods from java classes and make Python accessible functions out of them. We\'ll need to get help to understand a little bit about Python objects of this style to make them look decent.
4.  Spider Java source to fill in docstrings on introspected Java classes at runtime
    - The actual javadoc from Java isn\'t included in the bytecode, so we\'ll need to load it in somehow. My current idea is to add a [doc] descriptor to Java classes in Jython that loads the Javadocs from source when it\'s accessed. It\'ll look through the classpath for \<classname\>.java, and if it finds it, use [Sun\'s javadoc system](http://java.sun.com/j2se/1.4.2/docs/tooldocs/javadoc/overview.html) to parse the code and get some docstring like stuff out. It\'d be great if this could be a somewhat standalone library so all dynamic languages that run on the JVM could take advantage of it i.e. JRuby could make the same call, get the doc objects out and expose them in its own way.

## Origins 

This started as a weblog post from Brian Zimmer (His weblog disappeared a long time ago, but it was dug up again through the magic of the [wayback machine](http://www.archive.org/web/web.php)).

One of the best features of Python IMHO is the help() function. It's the first place I turn if I need help before I open a web browser and read the docs.

I think it would be cool if we could do this:

    >>> from java.lang import String
    >>> help(String)

and see the full Javadoc documentation in help format.

A good project would be to create a system that could turn Javadoc comments into a format that the Jython help system could consume (perhaps with a Doclet or xdoclet?) \-- this will become especially nice for Sun\'s newly GPL\'ed version) in the case of classes not already exposed with the special `__doc` string mechanism available in Jython already.

This could be facilitated with an xdoclet like framework which when ran over a source file would produce something Jython could use at runtime.

Of course, help() is not currently working at all in Jython \-- so the first step would be to figure out why this is and fix it. Also, we need a strategy for getting the help documentation from CPython into our new style classes.
