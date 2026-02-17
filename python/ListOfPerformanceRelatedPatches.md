# ListOfPerformanceRelatedPatches

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

Pending:

- [\[ 1479611](http://www.python.org/sf/1479611) \] speed up function calls TP

- [\[ 876193](http://www.python.org/sf/876193) \] reorganize, extend function call optimizations TP

- [\[ 1107887](http://www.python.org/sf/1107887) \] Speed up function calls/can add more introspection info TP

- [\[ 1087418](http://www.python.org/sf/1087418) \] long int bitwise ops speedup TP

- [\[ 1366311](http://www.python.org/sf/1366311) \] SRE engine do not release the GIL

- [\[ 1346214](http://www.python.org/sf/1346214) \] Better dead code elimination for the AST compiler GB

  - New patch posted, ready for review

- [\[ 1243654](http://www.python.org/sf/1243654) \] Faster output if message already has a boundary SH

Addressed:

- [\[ 1145039](http://www.python.org/sf/1145039) \] Remove some invariant conditions and assert in ceval TP

- [\[ 1442927](http://www.python.org/sf/1442927) \] `PyLong_FromString`{.backtick} optimization

- [\[ 1335972](http://www.python.org/sf/1335972) \] combo speedup and bugfix for string-\>int conversion

- [\[ 876206](http://www.python.org/sf/876206) \] scary frame speed hacks \[SUCCESS\]

- [\[ 1281707](http://www.python.org/sf/1281707) \] Speed up gzip.readline (\~40%) \[SUCCESS\]

- [\[ 1337051](http://www.python.org/sf/1337051) \] remove 4 ints from [PyFrameObject](./PyFrameObject.html)

- [\[ 1243730](http://www.python.org/sf/1243730) \] Big speedup in email message parsing SH **no speedup observed**

- [\[ 921466](http://www.python.org/sf/921466) \] Reduce number of open calls on startup GB

- [\[ 1359618](http://www.python.org/sf/1359618) \] Speed charmap encoder \[patch approved, MAL to apply\]

Deferred:

- [\[ 813436](http://www.python.org/sf/813436) \] Scalable zipfile extension

  - Addressed by SoC student

- [\[ 738094](http://www.python.org/sf/738094) \] for i in range(N) optimization

  - Related to [\[ 1472639](http://www.python.org/sf/1472639) \] make range be xrange

  - Topic was discussed endlessly for some times.

- [\[ 936813](http://www.python.org/sf/936813) \] fast modular exponentiation

  - Going to need a lot of attention, not suitable for the sprint.

- [\[ 923643](http://www.python.org/sf/923643) \] long \<-\> byte-string conversion

  - This is a feature request.

- [\[ 1353872](http://www.python.org/sf/1353872) \] a faster Modulefinder (Related to py2exe runtime performance)

  - No one interested in it.

- [\[ 1492828](http://www.python.org/sf/1492828) \] Improvements to ceval.c \--\> [RaymondHettinger](./RaymondHettinger.html)

- [\[ 1346238](http://www.python.org/sf/1346238) \] A constant folding optimization pass for the AST
