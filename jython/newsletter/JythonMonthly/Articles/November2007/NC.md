# JythonMonthly/Articles/November2007/NC

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# Newbie Notes: The Best of Both Worlds 

#### Submitted By: Rob Andrews 

### The Two Faces of Jython 

Jython is more than just an implementation of Python syntax in Java. It actually makes available access to a library of resources from both environments.

In my first article, I emphasized syntax and ideas I felt would be of value to Java developers new to Jython\'s syntax and to novice programmers in general.

This month, I set out to balance the scales a bit, introducing the import of Java library resources and a more Java-oriented way to handle files.

### Re-inventing the Wheel? 

While learning programming, or even just learning a new language, the temptation to do things the hard way can be powerful. But both Java and Python provide standard libraries of tools for carrying out many of the most common programming tasks you will likely encounter.

Importing classes, methods, and modules from available Java resources is fairly similar to importing from the Python standard library. In the jython environment, importing from either or both within the same application is generally not a problem.

Here we see how a time stamp may be produced using either Java or Python modules:

:::: 
::: 
``` 
   1 import java.util
   2 now = java.util.Date()
   3 print now
   4 
   5 import time
   6 pyNow = time.ctime()
   7 print pyNow
```
:::
::::

If you try these in your jython interpreter, you will see that they produce two similar (but not quite identical) time stamps.

### Changing Gears: Simple Java-Style File Handling 

If you read last month\'s *Newbie Notes*, you saw examples of simple file handling in a straight-forward pythonic way.

Although I use pythonic syntax for file handling by default, the following example demonstrates some elegance and power lended by Java:

:::: 
::: 
``` 
   1 from java.io import File
   2 for x in dir(File): print x
   3 
   4 file1 = File("c:/src/dsample.txt")
   5 print file1.length()
   6 print file1.path
```
:::
::::

Access to various file attributes such as length and path are immediately available through the *File* import. Similar functionality is made available by Python modules such as *os*, but the above approach is attractively obvious.

If you approach Jython as a Java programmer on the hunt for a solid scripting solution, or a Pythonista in need of access to Java libraries, many of your familiar techniques will be available in Jython, and often in a fairly transparent manner.

### Looking Ahead: 

In upcoming articles, I plan to demonstrate the development of more meaningful programs using the power available to the Jythonista.

We will also see how to deal with some of the special challenges of working in the Jython environment.

##### About the Author 

Rob Andrews is a Programmer Analyst at [Sourcelink](http://www.sourcelink.com).
