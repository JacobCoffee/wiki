# NeedForSpeed/Deferred

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

- Expose/develop pre-allocation arguments/methods for dict/list? API? [RichardJones](RichardJones) evaluated changes, but disapoointingly found that little or no speed advantage could be gained by preallocation of large structures!

- Evaluate the PEPs for optimizing global and attribute lookups
  - [PEP 266](http://www.python.org/dev/peps/pep-0266/), [PEP 267](http://www.python.org/dev/peps/pep-0267/), and [PEP 280](http://www.python.org/dev/peps/pep-0280/) [JackDiederich](./JackDiederich.html) suggests that these changes would be too radical to be incorporated during the sprint.

**Copyless network I/O**

A \"hot buffer\" class was implemented in order to perform I/O and parsing (using struct) without creating or copying strings around. This is compared for performance with a loop that creates strings via slices and concatenates strings. It turns out that the hot buffer version is not much faster (about the same speed) because it replaces string allocations and concatenations with dict lookup in order to access its attributes (position and limit). The version that uses strings is pretty fast since we write it using the string protocol, i.e. no dict lookup is performed. However, by implementing the common use patterns in C we should be able to make parsing of common input (e.g. netstrings) much faster. The hot buffer provides a more intuitive interface to parsing. The fact is that currently the performance gains with the initial version are not significant. (We need to complete some features to measure its impact.)
