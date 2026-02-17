# CodeSpeedupExperiments/PyByteCode

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# Planned and implemented speedups for PyByteCode interpreter 

### Issue 

Currently there is a huge switch-case statement in the interpreter of `PyByteCode`. Since there are a lot of cases (upwards of 150), the compiler cannot inline any operations in the case statements. The idea is to convert the switch-case statement into a enum-based dispath.

### Background 

At this time there are two classes that extend the base abstract `PyCode` class, `PyTableCode` and `PyBytecode`, along with some helper classes (`PyBaseCode`). You will also want to look at `PyFrame`, for frame support; and `ThreadState`. (Speaking of `ThreadState`, I believe there was a discussion [here](http://blog.crazybob.org/2006/07/hard-core-java-threadlocal.html) of how to implement dynamic scoping in Java, this is best done with `java.lang.ThreadLocal`. But don\'t follow what we\'ve done with `ThreadState`, because it mixes too many ideas together that we will fix, see [this bug](http://bugs.jython.org/issue1327).)

`PyTableCode` allows us to associate code objects with methods, which minimizes the permgen overhead in contrast to wrapping with classes. (This might have changed in the recent support in Java 6 for anonymous classloaders, however.) This association is through an index, which is then switched to the correct method. Table switches like this basically don\'t inline, so that\'s a real performance limitation. `PyTableCode` objects are loaded by a custom classloader and are compiled from `CodeCompiler`. You will definitely want to look at `CodeCompiler` and eventually the `ScopesCompiler`. We wrap the ASM bytecode library with our own API; most of that is in `org.python.compiler.Code`.

`PyBytecode` implements the Python bytecode VM. It\'s a direct translation of ceval.c from CPython. Please note there were likely some changes from 2.5 (which is what I translated) to 2.6, and then to 2.7. Really the only way to know is to do a diff, this is definitely a part of Python that\'s documented only in the code. But that\'s getting ahead of where we need to be.

The marshal module (`org.python.modules._marshal`, then imported via Lib/marshal.py, this is the usual pattern) implements the logic for marshaling to/from code objects and associated constants.

The `pycimport` module (Lib/pycimport.py) allows for you to import Python bytecode objects, in the form of pyc files, when available. It\'s pretty short, but the underlying PEP 302 support for meta importers is not exactly documented well. You can see how it\'s tested in a really limited way in Lib/test/test_pbcvm.py. Ideally it would run the entire regrtest, or at least a more substantial fraction. The subprocess TODO is what\'s necessary to avoid collision because of running the same imports repeatedly.

Lastly, you can use the `compileall` module to compile ahead-of-time (henceforth AOT) Python code, either in CPython or Jython, to pyc or py\$class representations respectively. This module is used by distutils, as seen in setup.py package setup scripts. with_enum_vs_without_5_30.png

### Results 

The switch-case `PyBytecode` was converted to enum in a new file `PyBytecodeEnum`^[1](#fnref-8a9f15891d8340b808ad32b4689c550d15484e2c)^.

To compare the performance of the new code with the previous code, I used the pystone benchmarks. To make sure that the JVM could jit the code, it was run using the server flag like so (in the `dist/bin` folder:

    ./jython -J-server

The results are below:

![with_enum_vs_without_5_30.png](attachments/CodeSpeedupExperiments(2f)PyByteCode/with_enum_vs_without_5_30.png "with_enum_vs_without_5_30.png")

base
:   plain jython run

with enum
:   the modified version using the python byte code containing the enums

without enum
:   version using the python byte code

::: footnotes
1.  [][http://bitbucket.org/shashank/jython-experiments/](http://bitbucket.org/shashank/jython-experiments/) ([1](#fndef-8a9f15891d8340b808ad32b4689c550d15484e2c-0))
:::
