# SummerOfCode/JITProjects

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

This page describes possible Summer of Code projects related to the Python 3 JIT, developed originally under the name \"[Unladen Swallow](http://code.google.com/p/unladen-swallow/)\". This list is not exhaustive. If you have other ideas for improvements to the JIT compiler, I\'d love to discuss them with you. The [Unladen Swallow issue tracker](http://code.google.com/p/unladen-swallow/issues/list) is a good source of ideas yet to be implemented.

**Contact: Collin Winter \<[collinwinter@google.com](mailto:collinwinter@google.com)\>**

## Reduce memory usage 

The JIT compiler currently [increases the memory usage of CPython 2.6 significantly](http://www.python.org/dev/peps/pep-3146/#memory-usage). We believe much of this increase to be waste or symptoms of bugs in LLVM or the JIT\'s usage of LLVM. The student will develop benchmarks to measure different components of memory usage; track down the various sources of the memory usage increase; develop and implement reductions in memory usage while still maintaining performance/correctness; develop tools and documentation to make future memory usage investigations easier.

[Some work](http://code.google.com/p/unladen-swallow/issues/detail?id=68) has already been done in this area, but more is needed. This work is critical to getting the JIT compiler merged into CPython 3.3.

## Faster regular expressions 

Develop a JIT-accelerated regex engine: pick up, extend [existing work](http://code.google.com/p/unladen-swallow/issues/detail?id=13) if applicable; make necessary improvements to [the common benchmark suite](http://hg.python.org/benchmarks); make necessary improvements to Python\'s correctness tests; implement JIT acceleration for 50% of regexes in benchmark suite; zero correctness regressions; zero performance regressions; demonstrate 25% performance improvement in regex benchmarks.

## Convert JIT output from stack machine to register machine 

Currently, the JIT compiler produces code that mimics the CPython bytecode interpreter loop, including the use of an explicit stack. Using the same stack idea made the initial compiler easier to implement, but the stack operations inhibit LLVM\'s optimization passes and impeded performance ([reference](http://www.tecgraf.puc-rio.br/~lhf/ftp/doc/jucs05.pdf), [reference](http://www.usenix.org/events/vee05/full_papers/p153-yunhe.pdf)). The student will design and implement changes to the JIT compiler to eliminate this explicit stack and instead use [LLVM\'s \'\'alloca\'\' instructions](http://llvm.org/docs/tutorial/LangImpl7.html), which are much easier for LLVM to optimize. This design will need to handle bailing back to the interpreter correctly. The student will demonstrate a performance improvement across relevant benchmarks, and improve the benchmark suite and correctness tests as needed.

## Optimize looping constructs 

Expose Python-level loops to LLVM\'s loop optimization passes; avoid allocating objects on the heap in the fast path; be able to bail back to the interpreter seamlessly; make necessary improvements to Python\'s correctness tests; demonstrate performance improvements across relevant benchmarks.

## JIT performance tools 

Develop tools for exposing JIT data to developers for performance debugging; annotate source code with gathered types; annotate source code with bail sites; enable developers to answer the questions, \"how do I make this application faster?\", \"why did my application slow down?\"; integrate with existing tools like cProfile, or develop new tools as appropriate.

## Develop a comprehensive suite of fuzz testing tools for Python 

[Fuzz testing](http://en.wikipedia.org/wiki/Fuzz_testing) is an important tool for stressing a compiler. With the addition of a JIT compiler to Python 3, fuzz testing is more important than ever. The student will evaluate the existing Python fuzz testing tools and extend them when needed: [pyfuzz](http://bitbucket.org/ebo/pyfuzz/overview/) for source-level fuzzing, [fusil](http://bitbucket.org/haypo/fusil/wiki/Home) for API fuzzing. The student will develop a new fuzzer for CPython bytecode to stress-test the bytecode-\>x86 JIT compiler ([reference](http://code.google.com/p/unladen-swallow/issues/detail?id=15)). The student will set up an automated system for continuously fuzzing a given CPython binary, along the lines of [the current CPython buildbot system](http://python.org/dev/buildbot/), including some kind of dashboard to display the results. The student will fix any bugs discovered by the fuzzing tools.
