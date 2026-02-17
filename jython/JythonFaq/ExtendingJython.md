# JythonFaq/ExtendingJython

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# Extending Jython 

[JythonFaq](JythonFaq)

------------------------------------------------------------------------

## How do I create Java classes that emulate Jython Dictionaries and Sequences? 

In order to emulate Dictionaries and Sequences, first your Java class must \"extend\" the org.python.core.[PyObject](./PyObject.html) class. The following methods can then be defined on your class in order to emulate these basic Jython types:

- :::: 
  ::: 
  ``` 
     1     public PyObject __finditem__(PyObject key);
     2 
     3     public void __setitem__(PyObject key, PyObject value);
     4 
     5     public void __delitem__(PyObject key);
  ```
  :::
  ::::

Additionally, you might want to throw the org.python.core.Py.[KeyError](./KeyError.html) object if you have any exceptions (Note, you need not declare the Java method as throwing anything.)

------------------------------------------------------------------------

## How do I emulate Jython object attribute access with a Java class? 

You can develop your own Java class that emulates Jython objects by first extending the org.python.core.[PyObject](./PyObject.html) class. Then, implement the following methods on your Java class:

- :::: 
  ::: 
  ``` 
     1     public PyObject __findattr__(String name);
     2 
     3     public void __setattr__(String name, PyObject value);
     4 
     5     public void __delattr__(String name);
  ```
  :::
  ::::

You may also want to raise exceptions using the org.python.core.Py.[AttributeError](./AttributeError.html) error class. (Note, you do not need to declare that the method throws this class.)

As in CPython, \"a = foo.bar\" calls the [findattr] method on foo, \"foo.bar = \'baz\'\" calls the [setattr] method on foo, and \"delattr(foo, \'bar\')\" calls the [delattr] method on foo.

If you plan on storing functions as attributes of your Java object (so that you could say \"foo.bar(\'baz\', \'fizzle\')\", be forwarned that Jython \*may or may not\* call the [findattr] method to find the function object depending on the number/types of parameters. You should, additionally, implement the following methods:

- :::: 
  ::: 
  ``` 
     1     public PyObject invoke(String name);
     2 
     3     public PyObject invoke(String name, PyObject arg1);
     4 
     5     public PyObject invoke(String name, PyObject arg1, PyObject arg2);
     6 
     7     public PyObject invoke(String name, PyObject[] args);
     8 
     9     public PyObject invoke(String name, PyObject[] args, String[] keywords);
  ```
  :::
  ::::

------------------------------------------------------------------------

## How do I support \*args and \*\*kw in Java methods? 

*(thanks to Finn Bock for the information)*

In Jython (note, this does not work in JPython), you can support keyword arguments on Java methods by defining the method like so (the parameters are the important point):

- :::: 
  ::: 
  ``` 
     1     public PyObject foo(PyObject[] args, String[] keywords);
  ```
  :::
  ::::

The keywords array contains all of the keywords for the keyword-defined arguments. For example, if you called foo with:

- :::: 
  ::: 
  ``` 
     1     foo(1,2,3,four=4,five=5)
  ```
  :::
  ::::

args would be: \[1, 2, 3, 4, 5\] and keywords would be: \[\'four\', \'five\'\] (an array of 2 elements.)

Additionally, you can use the experimental argument parser org.python.core.[ArgParser](./ArgParser.html) to deal mapping these two arrays. Consult the Javadocs (or source) for further details on org.python.core.[ArgParser](./ArgParser.html).

------------------------------------------------------------------------
