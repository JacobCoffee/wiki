# NeedForSpeed/Tasks

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

These are current tasks at the sprint. Also various people are evaluating patches from the [ListOfPerformanceRelatedPatches](ListOfPerformanceRelatedPatches), and initials record the participant(s) taking those resposibilities.

- Patch list review DONE (see [ListOfPerformanceRelatedPatches](ListOfPerformanceRelatedPatches))

- Continue function call speed enhancements. Neal Norwitz patch review. Zombie frames? [TimPeters](TimPeters) will continue.

- Faster parsing of strings and bytes into int, long, and back. [TimPeters](TimPeters): patch ready - needs clean-up

- Buffer for use with network I/O [MartinBlais](MartinBlais) working in blair-bytebuf branch \--\> sandbox? \[Performance comparisons first\]

- Implement portions of the decimal module in C: [GeorgBrandl](./GeorgBrandl.html) and [JackDeiderich](./JackDeiderich.html)

- Create a [PyInt64](./PyInt64.html) type (for 32 bit machines) Evaluate source impact \...GvR: Not in 2.5! \[/Deferred?\]

- Optimize methods in stringobject.c [FredrikLundh](FredrikLundh) + [AndrewDalke](./AndrewDalke.html)

- Allow selective removal of unused features such as profiling support DONE \[[/DeferredSuccesses](./NeedForSpeed(2f)Tasks(2f)DeferredSuccesses.html)?\]

- String benchmark DONE

- Improve interpreter startup time, like in patch \[SF\]921466? [GeorgBrandl](./GeorgBrandl.html)

- Patch that Skip wrote for a possible implementation of str.partition() which returns a string subclass with pointers to the slices instead of a full copy. Any subsequent string ops lazily evaluate the slice into a full string. \[\--\> [RaymondHettinger](./RaymondHettinger.html)\]

- Build-out the collections module for optimized data structures: ordered dictionary: API? Use case?! red/black? pivot tbl? skip list: contribution? radix/crit-bit trees? [ChristianTismer](./ChristianTismer.html) + [RichardEmslie](./RichardEmslie.html)

- Struct benchmark needs to be incorporated into pybench [BobIppolito](BobIppolito)

- Improve the API for timeit.py \[SH to search python-dev and call Raymond Hettinger for details if necessary\]

- Update [PythonSpeed/PerformanceTips](../PythonSpeed/PerformanceTips) Everyone can make suggestions [SeanReifschneider](SeanReifschneider) + [JohnBenediktsson](./JohnBenediktsson.html)

- Evaluate the PEPs for optimizing global and attribute lookups
  - PEP 266 PEP 267 PEP 280

- Psyco improvements: [JohnBenediktsson](./JohnBenediktsson.html)

  - Support for generator expressions Support for nested scopes Support for more dictionary operations Speedup float arithmetic Support for more built-ins (e.g. int(), long(), float(), etc.) Upgrade for python 2.5 Better tools for profiling psyco-ness of application Investigate usefulness of IVM (with aim to producing a more streamlined dispatch loop) LLVM backend Virtualized longs (for long longs) Virtualized slots (Ability to cache getattribute() values)

\* Py3000: Make a wishlist for possible performance gains in Py3.0
