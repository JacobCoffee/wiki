# JythonUses

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

What follows is the abstract for a proposal I submitted to [PyCon](../conferences/pycon/PyCon) 2003. Perhaps someone would like to help fill it out with examples. \-- [TomBryan](TomBryan)

## Introduction 

Jython is a powerful force in the Python world. I believe that it could become a \"killer app\" for Python. As a scripting language for Java developers, it offers a mature, easy to learn language with a strong community and a similar feel to the Java language itself (small core language with a large library, strong OOP support, etc.). As a separate implementation of the Python interpreter, it offers Python developers some interesting options. This presentation seeks to introduce Jython to an audience who already knows and uses Python. It seeks to show some of the most interesting aspects of Jython versus the standard Python interpreter (CPython).

## Install Java; program in Python 

The python.org website states that, \"Python is an interpreted, interactive, object-oriented programming language.\" That \"interpreted\" part means that, to run a program written in Python, it is necessary to start another program (the Python interpreter) to execute any Python code. The standard implementation of the Python interpreter (sometimes called CPython) is written in C. Jython is simply another Python interpreter. Python developers can use Jython to run their programs written in Python just as currently use CPython.

Jython is a Python interpreter, written in Java, that strives to be compatible with the standard Python interpreter (including the standard library set). When Sun Microsystems first introduced Java, the marketing hype claimed that developers could \"Write once, run anywhere.\" While that claim is certainly not completely true, Jython provides a Python interpreter wherever a Java Virtual Machine is installed. While Python is available on many platforms, Jython gives Python developers access to any platform that is supported by Java. This portability does not require makefile tweaks or rebuilding Python on an obscure platform. If Java is installed, the Jython interpreter should run.

Python code written for the Jython interpreter looks just like Python code written for the CPython interpreter. We will describe some of the differences between the two interpreters, such as performance and garbage collection.

## Program in Java; assemble with Python 

So, why would an honest Python developer want to switch from CPython to Jython? The most important reason is that the Jython interpreter actually compiles Python code down to Java byte code and runs it directly on the Java Virtual Machine. Because of this implementation, it is possible to access Java classes directly from a Python program written to run on the Jython interpreter.

To make sure that everyone is appropriately impressed by this concept, I will show some examples of leveraging existing Java code from within Python code. Examples will range from basic (using the standard Java library from Jython code) to complex (accessing a large Java engine, such as POI or Batik, from Jython code). Java has been a very popular language for commercial and non-commercial production software development for the last several years. Jython can give Python developers instant access within their code to any of that Java code. For projects that may involve mostly stitching together existing Java components, Jython may be an appropriate implementation language.

## Program in Python; extend in Java 

Posters on comp.lang.python often suggest that developers try writing a program in Python and then optimizing the speed critical parts in C. While Jython is generally slower than CPython and Java is generally slower than C, the same logic applies in Jython. This point is especially important for developers who don\'t know C or who break into a cold sweat whenever they see char\*\*. Some of these Pythonistas may be more comfortable working in Jython since they can switch to Java when needed.

Extending Jython with Java code is also much more straight forward than extending Python with C code. We will give a range of examples from a small, toy class to larger libraries, such as the zx extensions.

## Embed Jython in Java Applications 

We\'ve been talking about how easy it is to use Java from Jython. How easy is it to call Jython from Java? While this topic drifts more into the realm of those who develop primarily in Java, embedding Jython in a Java program shows another aspect of Jython\'s power and flexibility. A few examples will be provided, such as JEdit\'s use of Jython as a scripting language. Note that as more Java programs embed Jython to enable end-user scripting, more users will be exposed to Python!

## Prototype in Jython; develop in Java. 

For many projects, choosing the right approach can be critical. From choosing the right algorithms to properly decomposing the domain into an object model, developers often benefit from prototyping their ideas quickly to ensure their viability. Jython is an ideal prototyping language for a Java developer. It brings with it all of the strengths of Python, and it provides a language perhaps better suited to rapid application development and prototyping. After a pass at prototyping his application in Jython, a Java developer can then move his code to Java, where he can focus on details of access restrictions and data types since the basic structure of the application has already been illustrated by the prototype. Since Jython provides seamless access to Java code, entire large applications can be prototyped in Jython. Then, the prototype can be moved gradually to Java. As components are migrated to Java, the remaining Jython code can be pointed to the new Java classes so that the entire system can still be run. This approach makes it possible to prototype an application without having to throw away the prototype and start from scratch when the time to start the production coding starts. In this way, while components are being migrated to Java, they can be run in an end-to-end prototype to validate that they behave as expected. And if the product has to ship before all of the Jython code is moved to Java, then there\'s one more application in the world using Python in production code!

------------------------------------------------------------------------

[CategoryJython](CategoryJython)
