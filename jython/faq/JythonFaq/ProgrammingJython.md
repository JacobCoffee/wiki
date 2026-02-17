# JythonFaq/ProgrammingJython

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# Programming Jython 

[JythonFaq](JythonFaq)

------------------------------------------------------------------------

## Why can\'t I multiply inherit from two or more Java classes? 

In earlier versions of JPython, you actually could. This was deliberately disabled in 1.1 for a variety of good reasons. For one, multiply inheriting from two Java classes breaks the single inheritance contract that is assumed when developing Java classes.

Note that you can still multiply inherit from any number of Python classes, and you can inherit from any number of Java interfaces.

------------------------------------------------------------------------

## I\'m trying to execute a \'protected\' or \'private\' Java Instance Method or attribute in a Java package. How can I get access? 

By default, as in Java, these methods are protected from external access, but there may be reasons, such as test scaffolding scripts, that this feature is not wanted. In the \[jython home\]/registry file:

      # Setting this to false will allow Jython to provide access to
      # non-public fields, methods, and constructors of Java objects.
      python.security.respectJavaAccessibility = false

------------------------------------------------------------------------

## How can I access Java protected (static) members from a Jython subclass? 

The short answer: you can\'t. At least not without setting the registry option python.security.respectJavaAccessibility to false.

It is difficult to add in a nice manner. The problem is a bit like this:

A normal (public) static method is from jython called on the parent java class:

- javaclass.method()

Such a call does not originate from the subclass, but from internal reflection code in jython. If we want to add support for calling protected static methods from a jython subclass, the call will have to originate from the subclass (ie. the proxy class), so we will have to generate a referring method in subclass proxy like:

:::: 
::: 
``` 
   1   public static void method() {
   2      javaclass.method()
   3   }
```
:::
::::

(with the right return type and throws clauses) and the jython subclass will have to call the method on its own class, not the java class.

------------------------------------------------------------------------

## How can I use a Java null value in Jython? 

A Java null is turned into a Python None value.

      import java
      >>> h = java.util.Hashtable()
      >>> print h.get("abc")
      None
      >>> if h.get("abc") is None:
      ...   print "null returned"
      ...
      null returned
      >>>

------------------------------------------------------------------------

## Where\'s the -O switch? 

Jython does not have a -O command-line switch.

Assigning [debug]=0 has been used to get -O behavior from things like \"assert\", but such assignments to [debug] are considered an error, and in the future, will raise an exception. [debug] is supposed to be a read-only variable.

------------------------------------------------------------------------

## When I write to a file, it\'s empty. Why? 

You need to close the file (or flush the buffer). You can ensure this happens by using finally or the with statement:

:::: 
::: 
``` 
   1     from __future__ import with_statement
   2     # some code...
   3     with open("myFile", "w") as f:
   4         f.write("some data")
```
:::
::::

------------------------------------------------------------------------

## The Jython\'s os module is missing some functions, why? 

For Posix and Windows, Jython implements most of the os module seen in CPython (excluding most notably fork). Under certain sandbox settings, it\'s not possible to run the necessary Java Native Runtime code for this (using JNI), so instead a pure Java version is substituted. This is also what is available when running under other OS\'s, such as zOS.

------------------------------------------------------------------------

## How can I manipulate a java.util.Date object in Jython? 

`java.util.Date.getTime()` gives the milliseconds since the epoch while Jython (just like CPython) gives seconds since the epoch. So you need to divide the values given from `java.util.Date` by 1000.

Example:

:::: 
::: 
``` 
   1 >>> from java.util import Date
   2 >>> import time
   3 >>> times=(float(Date().time)/1000,time.time())
   4 >>> times[0]-times[1]
   5 0.0
```
:::
::::

------------------------------------------------------------------------

## jythonc

jythonc is no longer available as of 2.5.

for more info on jythonc see [http://www.jython.org/Project/jythonc.html](http://www.jython.org/Project/jythonc.html)

------------------------------------------------------------------------

## How can catch a Java exception thrown from within Jython? 

How do I distinguish between different Java exceptions thrown from within jython if the `interp.exec`{.backtick} method only throws a `PyException`{.backtick} ?

     PythonInterpreter interp = new PythonInterpreter();
     String jythonCodeString = "from com.example import MyJavaException\n" +
       "raise MyJavaException('special condition occurred.')"; 

     try {
          interp.exec(jythonCodeString);
        } catch (org.python.core.PyException e) {
          if (e.value instanceof PyJavaInstance) {
            Object javaError = e.value.__tojava__(Throwable.class);
            if (javaError != null && javaError != jy.NoConversion) {
              if (javaError instanceof MyJavaException ){
                throw (MyJavaException)javaError;
              }
            }
          }

          if (Py.matchException(e, Py.KeyboardInterrupt)) {
            throw new InterruptedException(
                "Interupted while executing Jython script.");
          }
          throw e;
        } 
