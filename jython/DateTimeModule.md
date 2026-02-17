# DateTimeModule

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

[FrankWierzbicki](FrankWierzbicki) is leading the implementation of the datetime module.

### Background 

Python 2.3 introduced a new module datetime.

- [http://online.effbot.org/2003_08_01_archive.htm#librarybook-datetime-module](http://online.effbot.org/2003_08_01_archive.htm#librarybook-datetime-module)

- [http://docs.python.org/lib/module-datetime.html](http://docs.python.org/lib/module-datetime.html)

Since this module is implemented in C, it would be nice to have a Java implementation for Jython. A pure Python implementation of datetime can be found at

- [http://cvs.sf.net/viewcvs.py/python/python/nondist/sandbox/datetime/](http://cvs.sf.net/viewcvs.py/python/python/nondist/sandbox/datetime/) .

I plan on using this implementation extensively as the Java version is developed. If it turns out that a Java implementation is infeasible or will take too long, we could always fall back on using this module directly.

My original plan was to write the entire module in Java, using zxDateTime for guidance

- [http://cvs.sourceforge.net/viewcvs.py/zxpy/zxDateTime/](http://cvs.sourceforge.net/viewcvs.py/zxpy/zxDateTime/) .

However, after reading this addition by [BrianZimmer](BrianZimmer) to [JythonModulesInJava](JythonModulesInJava):

      My new approach is borrowed slightly from CPython where it's very
    common to write a C library, a straight wrapper and then a Pythonic
    wrapper. In Jython, the first two steps are really one so the
    development effort is significantly simplified. Writing a wrapper in
    Python offers the dual benefits of being easy to maintain and refactor
    as well as requiring less development time.

And after discussing it with Brian, I\'ve re-thought that approach, and I now plan to start with the pure python datetime and replace the date related code with [java.util.Calendar](http://java.sun.com/j2se/1.4.2/docs/api/java/util/Calendar.html) code.

### Design 

::: {}
  ---------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------
  **Python Class (from pure Python implementation)**   **Strategy**
  timexxx                                              I think this is just a placeholder for something in C\...
  timedelta                                            For now I plan to leave this alone, though this may be a place where a Java reimplementation may give a performance boost.
  date                                                 Replace most logic with java.util.Catalog code.
  tzinfo                                               This is an abstract class, a wrapper so that [java.util.TimeZone](http://java.sun.com/j2se/1.4.2/docs/api/java/util/TimeZone.html) could be used would be nice
  time                                                 Leave as is for now, but review later
  datetime                                             Replace most logic with java.util.Catalog code.
  ---------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------
:::

### Discussion 

[FrankWierzbicki](FrankWierzbicki) 2005-02-13

For the short term I plan to use the Python unit tests as the absolute definition of the datetime module, and will not try to go beyond the CPython implementation. This means (for example) that dates will be limited to 1-9999AD, because that is what the CPython unit tests expect. Even though java.util.Calendar does not have this limitation, I will enforce it. This may change once Jython starts to catch up with the leading edge of CPython development and we can productively review the unit tests themselves.

\-\--

Might [Joda Time](http://joda-time.sourceforge.net/) come in handy?

\- [SimonBrunning](./SimonBrunning.html)

\-\--

Joda Time is interesting but we should look to minimize Jython\'s dependencies.

\- [BrianZimmer](BrianZimmer)
