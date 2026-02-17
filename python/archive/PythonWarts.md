# PythonWarts

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# Python Warts 

Python \"warts\" are things for which people have criticised Python, typically aspects of the language or mechanisms of its implementation, because such aspects either expose certain surprising inconsistencies, are regarded as omissions, or cause irritation for parts of the community in some sense. One goal of Python 3000 was to fix inconsistencies which could not have been fixed earlier due to the backwards compatibility constraints imposed on earlier releases of Python. This page summarises the unfixed warts, pitfalls and \"gotchas\" (which are not mere observations) from the following resources and lists Python 3000 remedies, if any:

- Andrew Kuchling\'s [\"Python Warts\"](http://web.archive.org/web/20031002184114/www.amk.ca/python/writing/warts.html) - now archived

- Hans Nowak\'s [\"10 Python pitfalls\"](http://archive.is/xBOV2) - now archived

- Steven Ferg\'s [\"Python Gotchas\"](http://web.archive.org/web/20080503031358/http://www.ferg.org:80/projects/python_gotchas.html) - now archived

- Mark Lutz\'s [\"When Pythons Attack\"](http://www.onlamp.com/pub/a/python/2004/02/05/learn_python.html) - [Archive](http://archive.is/Tjd2q)

- David Mertz\'s \"Python elegance and warts\", [Part 1](http://web.archive.org/web/20090403002610/http://www.ibm.com/developerworks/linux/library/l-python-elegance-1.html) and [Part 2](http://archive.is/MdrIm) - now archived

In the table below, the following terminology is used:

- No remedy: while some believe this to be a shortcoming, a lack of wider consensus has resulted in no remedy being pursued

- Rejected: the shortcoming in question is regarded as a feature, typically because any attempt to remove it would arguably change the language in a way which would be even more confusing - see [PEP 3099](http://www.python.org/dev/peps/pep-3099/) for a list of such requested features

Note that the [\"What\'s New in Python 3.0\" document](http://archive.is/c2tkF) also contains a list of changes in Python 3000. One can argue that many of the changes are useful fixes that were too mundane for people to write critiques about.

::: {}
  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ ----------------------- ---------------------------------------------------------------------------------------
  **Shortcoming**                                                                                                                                                                                        **Source**              **Python 3000 Remedy**
  No do statement                                                                                                                                                                                        Kuchling                *No remedy*
  Local variables and scoping                                                                                                                                                                            Kuchling, Nowak, Lutz   *No remedy*
  Calling base class methods                                                                                                                                                                             Kuchling                [New Super](http://www.python.org/dev/peps/pep-3135/)
  Catching multiple exceptions                                                                                                                                                                           Kuchling, Nowak         [Catching Exceptions in Python 3000](http://www.python.org/dev/peps/pep-3110/)
  Explicit self in methods                                                                                                                                                                               Kuchling                *Rejected* - this would require name declarations
  Doubled underscores for private variables                                                                                                                                                              Kuchling                *No remedy*
  The .join() string method                                                                                                                                                                              Kuchling                *No remedy*
  print \>\>                                                                                                                                                                                             Kuchling                [Make print a function](http://www.python.org/dev/peps/pep-3105/)
  Inconsistent indentation                                                                                                                                                                               Nowak                   *Rejected* - indentation is central to Python\'s syntax
  The += operator                                                                                                                                                                                        Nowak                   *No remedy*
  Class attributes vs instance attributes                                                                                                                                                                Nowak                   *No remedy*
  Mutable default arguments                                                                                                                                                                              Nowak, Ferg, Lutz       *No remedy*
  [Backslashes are escape characters](http://web.archive.org/web/20161025191258/https://pythonconquerstheuniverse.wordpress.com/2008/06/04/gotcha-%E2%80%94-backslashes-are-escape-characters/)   Ferg                    *No remedy*
  [Print and softspace](http://web.archive.org/web/20080503031358/http://www.ferg.org:80/projects/python_gotchas.html#contents_item_4)                                                            Ferg                    [Make print a function](http://www.python.org/dev/peps/pep-3105/)
  [Omitting parentheses when invoking a method](http://web.archive.org/web/20081029013232/http://pythonconquerstheuniverse.blogspot.com:80/2008/06/gotcha-forgetting-parentheses.html)            Ferg, Lutz              *Rejected* - taking a reference to a function/method is a feature
  Imports and reloading                                                                                                                                                                                  Lutz                    *No remedy* - improved reloading has been considered
  Inconsistent/unpredictable comparisons/ordering                                                                                                                                                        Mertz                   *No remedy*
  Deficient sequence support for iterators, generators                                                                                                                                                   Mertz                   *No remedy*
  Attribute access mechanism proliferation                                                                                                                                                               Mertz                   *No remedy* - Mertz suggests standard decorators
  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ ----------------------- ---------------------------------------------------------------------------------------
:::
