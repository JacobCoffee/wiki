# Asking for Help/Can Python introspect like Java?

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# Can Python Introspect Like Java? 

\"I come from a java background. Java has an API that list all classes and their methods that come with Java. Is there anything like that in python?\"

At the Python interpreter prompt, invoking the dir function as follows\...

\>\>\> dir()

\...gives a list of defined classes and variables.

In certain interactive shells (or prompts), such as [IPython](../../archive/IPython), using the TAB key on one of the existing objects opens a list of possible completions, i.e. its methods/attributes. For other plainer shells, you can call the dir function supplying an object as an argument to see the contents of that object:

\>\>\> dir(some_object)

## Discussion 

I\'m not sure this is what the OP is asking. I think s/he\'s referring to the API documentation rather than the API itself. Calling help(object) in the interpreter is a good start for help on an object.

In fact, the dir and help built-in functions make use of Python\'s introspection capabilities. Another interface can be found in the standard library inspect module. \-- [PaulBoddie](../PaulBoddie)

CL\'s answer: no, Python cannot introspect like Java; it can only do better.

## API Documentation 

The [DocumentationTools](../../documentation/DocumentationTools) page provides details of tools which can produce API documentation for Python applications and libraries, such as that provided for [wxPython](../../gui/WxPython) (a GUI-building kit for Python): [wxPython API documentation](http://www.wxpython.org/docs/api/).

------------------------------------------------------------------------

[CategoryAskingForHelp](CategoryAskingForHelp) [CategoryAskingForHelpAnswered](CategoryAskingForHelpAnswered)
