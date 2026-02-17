# PerformanceEnhancements

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# Performance Enhancements Resources

Jython benchmarks (from PyPy\'s suite): [http://freya.cs.uiuc.edu/\~njriley/benchmark.html](http://freya.cs.uiuc.edu/~njriley/benchmark.html)

Plots of microbenchmarks (also from PyPy): [http://freya.cs.uiuc.edu/\~njriley/plots.html](http://freya.cs.uiuc.edu/~njriley/plots.html)

::::::: 
### Ideas

jbaker & thobe\'s JavaOne \'08 talk: [Jython Implementing Dynamic Language Features For The Java Ecosystem](http://developers.sun.com/learning/javaoneonline/2008/pdf/TS-6039.pdf?cid=925321)

::: 
#### Allocation/GC Expense

Our algorithms are not always the problem, sometimes it\'s memory {de}allocations that slow you down

- dicts/stringmap

PyStringMap/PyDictionary pay a penalty on allocation now that they\'re backed by ConcurrentHashMap. We could probably tweak the ConcurrentHashMap initialCapacity, concurrentLevel to reduce this cost

- Frames

Frames are allocated for every Python method call, which is a GC expense. CPython (and JRuby?) recycle frame objects. Reducing the number of fields on the frame can also help (but this likely isn\'t possible)
:::

::: 
#### Advanced Compiler
:::

::: 
#### Modules to rewrite in Java

- \_heapq
- select
- socket
- unicodedata
:::

::: 
#### iterlen support

Adds a length hint to various objects, mainly for smarter allocation during map and list. See test_iterlen
:::
:::::::
