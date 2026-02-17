# JythonFaq/GeneralInfo

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# General Information 

[JythonFaq](JythonFaq)

------------------------------------------------------------------------

## What is Jython? 

Jython follows closely the Python language and its reference implementation CPython, as created by Guido van Rossum. Jython 2.7 corresponds to CPython 2.7.

Jython started as JPython, created by Jim Hugunin in 1997. JPython was renamed to Jython by Barry Warsaw in 1999 with the 2.0 release. Since then, Jython 2.x releases have corresponded to equivalent CPython 2.x releases.

## Is Jython the same language as Python? 

Yes. Jython is an implementation of the Python language for the Java platform. Jython 2.7 implements the same language as CPython 2.7, and nearly all of the Core Python standard library modules. (CPython is the C implementation of the Python language.) Jython 2.7 uses the same regression test suite as CPython, with some minor modifications.

There are a number of differences. First, Jython programs cannot currently use CPython extension modules written in C. These modules usually have files with the extension .so, .pyd or .dll. If you want to use such a module, you should look for an equivalent written in pure Python or Java. However, it is technically feasible to support such extensions, as demonstrated by [IronPython](./IronPython.html). For the next release of Jython, we plan to support the C Python Extension API.

There are a number of other differences between the two implementations that are unlikely to go away. These range from the trivial - Jython\'s code objects currently do not have a co_code attribute because it is not possible to directly access Java bytecode from a class, without loading the file; to the significant - Jython uses Java\'s true garbage collection rather than Python\'s reference counting scheme.

------------------------------------------------------------------------

## What is the current status of Jython? 

Jython 3.x development is in progress.

Jython 2.7.0 was released on May 3, 2015. Jython 2.7.1 release candidates will be released soon (September 2015).

Jython 2.5.3 is the last stable release for 2.5.x; we plan to release 2.5.4 final shortly (September 2015).

Unsupported releases:

Jython 2.2 was released on August 22, 2007, with 2.2.1 released on October 13, 2007.

Jython 2.1 was released on December 31, 2001

Jython 2.0 was released on January 17, 2001

------------------------------------------------------------------------

## How fast is Jython? 

The startup time and runtime performance for Jython are largely determined by the JVM. Startup time can be mitigated by using a tool like Nailgun. Running an older release of Java 7 can be much slower, due to bytecode verification.

Jython is approximately as fast as CPython\--sometimes faster, sometimes slower. Because most JVMs\--certainly the fastest ones\--do long running, hot code will run faster over time.

Areas that are known to be slower include the expat emulation (which is used by [ElementTree](./ElementTree.html)), bisect, datetime, decimal, heapq, and unicodedata, since these are all currently written in Python instead of Java; in CPython, these are all written in C. Future releases of Jytho can address this situation.

If you find a specific area where Jython performance is worse than CPython, and especially if you have a patch, please file a bug at [http://bugs.jython.org](http://bugs.jython.org).

------------------------------------------------------------------------

## How do I learn more about Jython? 

You might want to start with the the Apress book documenting Jython 2.5, [The Definitive Guide to Jython](http://apress.com/book/view/9781430225270), which is also available online as the [Jython Book](http://jythonbook.com), an open source version.

Since Jython and Python are so closely related any good python book or documentation works well. There are also many good choices available and can be found easily by using your favorite search engine and searching for Jython. Here are a few of the frequently used references:

These are good starting points for learning python but by no means a complete list:

- The [official Python documentation](http://python.org/doc/) - (note this covers the 2.6 version of the language and libraries). This is currently being patched against the small changes seen in Jython. Note that class decorators, the ast module, and the namedtuple factory function from 2.6 were implemented in Jython 2.5.0.

- [Dive into Python](http://diveintopython.net) is a great learning resource

for Jython specific starting points try these:

- [The Jython Users Guide](UserGuide)

- An excellent book, [\"Jython Essentials\"](http://www.oreilly.com/catalog/jythoness/), by Samuele Pedroni & Noel Rappin

- as the song goes, [\"\...getting to know you..\"](http://www.ibm.com/developerworks/java/library/j-alj07064/)

- An excellent [online course](http://www.rexx.com/~dkuhlman/jython_course_03.html) by Dave Kuhlman

Be sure to check out the references at the bottom of the online course.

These are just a sampling of what\'s available. There is a lot out there and it covers a wide variety of topics. This will get you started and on you way to becoming a Jython developer and when you are ready for more, it\'s just a few clicks away.

------------------------------------------------------------------------

## Can I use Jython to make apps for mobile phones? 

Unfortunately not. The Android operating system does use Java as its primary programming language, but there is no known port of Jython to the platform. If you want to make apps for Android smartphones, see the Python Wiki\'s [Android page](https://wiki.python.org/moin/Android) for alternative approaches.

Some older mobile phones have [Java ME (Micro Edition)](http://en.wikipedia.org/wiki/Java_Platform,_Micro_Edition), but Jython requires [Java SE (Standard Edition)](http://en.wikipedia.org/wiki/Java_Platform,_Standard_Edition), so it cannot be used on them either.

However, Jython is Free and Open Source, so if you have the skills then feel free to start porting it to any platform that interests you.

------------------------------------------------------------------------
