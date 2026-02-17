# JythonDeveloperGuide/PortingPythonModulesToJython

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

Porting an existing Python module written in C into Java that Jython understands is a pretty straightforward task so it can serve as a good introduction to the Jython codebase. I\'m going to explain how to go about porting the [csv](http://www.python.org/doc/2.3.5/lib/module-csv.html) module here.

1.  Declare your intention to implement the csv module on the Jython dev list so no one else starts working on it.

2.  Add a new class org.python.modules.\_csv.java in src to mirror \_csv.c from CPython.

3.  Add \"\_csv\" to the builtinModules array in org.python.modules.Setup

4.  Run dist/Lib/test/test_csv.py. Everything will fail since none of the csv methods are implemented yet. Now pick one of the simpler tests and start adding methods to csv to get it to work. \_csv.java will be an implementation of the stuff in \_csv.c from Python. All of csv_methods from \_csv.c needs to be implemented as static methods in \_csv.java. You can get an idea of how it\'s done from \_codecs.java and \_codecs.c or any of the module implementations in org.python.modules and their corresponding C implementation. As you add the methods to \_csv.java, Jython will pick up on them and parts of the tests will start working.

5.  Keep adding pieces to \_csv.java till the tests pass

6.  Submit a patch to the [tracker](http://www.jython.org/patches).

7.  Revel in the glory of another implemented module

The table below contains modules implemented in C in Python that are missing in Jython. Feel free to grab one of them and get started. If none of them catch your fancy, run dist/Lib/test/regrtest.py. All of the skipped tests are for modules that are present in CPython but not in Jython, so they\'re fair game too. See the \"Missing Modules\" section of [../RegressionTestNotes](./JythonDeveloperGuide(2f)RegressionTestNotes.html) for a list as of 20061123.

::: {}
  ------------- ------- -------------------------------------
  Module        Taken   Affected tests
  csv           Y       test_csv
  tarfile       N       test_tarfile
  unicodedata   Y       test_unicodedata,test_codeccallback
  heapq         N       test_heapq
  mmap          Y       test_mmap
  ------------- ------- -------------------------------------
:::

## Comments 

**Why have you called the Java file \_csv.java instead of just csv.java? Is there a convention here and if so, why don\'t all the classes follow the same convention.**

*pdrummond*: Short answer: It\'s called `_csv`{.backtick} because that is what it\'s called in CPython!

Long answer: Hmmm. Will have to swat up on CPython\'s module naming conventions to answer this properly! I think CPython\'s general convention is \"`<name>module.c`{.backtick}\" so `csv`{.backtick} really should be \"`csvmodule.c`{.backtick}\" shouldn\'t it? I guess the underscore is necessary because there is a `csv.py`{.backtick} wrapper so the \"csv\" name is already taken, but I need to check this to be sure!

*[FrankWierzbicki](FrankWierzbicki)*: This is actually a CPython convention \-- but one that is inconsistently applied \-- the 2.6 version is making this more consistent. The convention is: for a given module x, there is usually an implementation in python called x.py and a c implementation called \_x.c. Generally x.py tries to import \_x.c at the beginning \-- this way implementations like Jython can get a pure python implementation right away, but can also implement a faster version that we should call \_x.java later. I\'d like to add that I would recommend looking at the CPython implementation as you go \-- there are almost always subtleties that the tests miss - I used to assume the tests where good enough but got burned a couple of times this way.

**Will the `test_csv.py`{.backtick} file automatically appear after a build or do we have to implement this ourself?**

*pdrummond*: `test_csv.py`{.backtick} will appear auto-magically after a build in `dist/Lib/test`{.backtick} (at least, it will in the 2.3 branch) and it is a CPython test script.
