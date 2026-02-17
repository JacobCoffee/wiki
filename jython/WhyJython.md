# WhyJython

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

*Jython, lest you do not know of it, is the most compelling weapon the Java platform has for its survival into the 21st century - [SeanMcGrath](./SeanMcGrath.html)*

------------------------------------------------------------------------

## Why Jython 

There are numerous alternative languages implemented for the Java VM. The following features help to separate Jython from the rest:

- Dynamic compilation to Java bytecodes - leads to highest possible performance without sacrificing interactivity.
- Ability to extend existing Java classes in Jython - allows effective use of abstract classes.
- Optional static compilation - allows creation of applets, servlets, beans, \...
- Bean Properties - make use of Java packages much easier.
- Python Language - combines remarkable power with very clear syntax. It also supports a full object-oriented programming model which makes it a natural fit for Java\'s OO design.

## What Does Jython Do Well? 

- Prototyping
- Java investigation
  -     >>> from java.util import Date
            >>> d = Date()
            >>> print d
            Sat Jan 08 16:26:16 CST 2005
            >>> from java.util import Random
            >>> print dir(Random)
            ['__init__', 'nextBoolean', 'nextBytes', 'nextDouble', 'nextFloat',
            'nextGaussian', 'nextInt', 'nextLong', 'seed', 'setSeed']
            >>>
- Making bean properties accessible
  -     >>> print Date().time
            1105500911121
- Glues together libraries already written in Java
- Excellent embedded scripting language
  - Object Domain UML Tool

  - [PushToTest](./PushToTest.html)

  - Drools

------------------------------------------------------------------------

## Differences - Python & Jython 

**Python 2.7**

- C

- Multi-platform

- Compiles to .pyc

- Extend with C

- GIL ^[1](#fnref-0edd12e1f236f8b9c64bb66c211e066bace41c1a)^

- Python garbage collection, which mixes ref counting and mark and sweep

**Jython 2.7**

- Written mostly in Java, does use Java Native Runtime for C access, but works with security manager restrictions
- Java 7 or Java 8
- Compiles to \$py.class files
- Extend with Java or C using JFFI; full CFFI, ctypes, and C Extension API support planned for the future
- Truly multi-threaded
- Java garbage collection, including choice of standard Java GCs; but also provides same API as Python 2.7 to observe GC

::: footnotes
1.  []Global Interpreter Lock, explained in \[[http://docs.python.org/api/threads.html](http://docs.python.org/api/threads.html) Python documentation, chapter 8.1\] ([1](#fndef-0edd12e1f236f8b9c64bb66c211e066bace41c1a-0))
:::
