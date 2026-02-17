# MemoryUsageProfiler

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

The objective of a memory profiler clearly would be to help a developer determine where the memory is going, why the memory was allocated and why it didn\'t get released.

There are many approaches to this problem, and they involve various aspects, such as:

- what part of the code is using up what amount of memory?
- what is the set of all memory blocks currently allocated?
- where was a block of memory allocated?
- where is a block of memory still being referenced?

# Sizing objects 

One metric for memory consumptions is certainly \"number of allocated bytes\"; others are \"number of allocated objects\", \"amount of unallocated-yet-unreleased memory\" (a.k.a. fragmentation).

To compute the number of allocated bytes, one could either track the memory allocations at the lowest level, and sum them up, or track all objects, and then compute the size each object takes in memory.

# Tracking memory 

To determine the set of allocated blocks, again one may either track memory blocks at the lowest level, or try to keep lists of objects. Python already has support for the latter, in two forms: in the debug mode, Python keeps a list of all allocated objects. In addition, even in release mode, Python keeps a list of all objects that participate in cyclic garbage collection, i.e. of all container objects. It also supports tracing references from one object to all referred-to objects, so that even non-container objects can be found.

These approaches all come with their own overheads; the latter one (use cyclic GC) has the least overhead, as the Python interpreter has to perform this bookkeeping anyway. They also differ in what kinds of errors they can detect:

- if an extension module has an error in its reference counting, objects might
  - be allocated that are nowhere referenced. The GC won\'t see them, but they will show up in the list of all objects in debug mode.
- if an extension module allocates a block of memory that is not part of an
  - object, that block won\'t even be accounted for in the list of all objects; only the lowest-layer-tracing might find that the block is still allocated.

In summary: if the suspected memory leak is not in an extension module, it should be much cheaper to track memory allocations. If extension modules may contain errors, finding those errors requires more expensive machinery.

# Classifying memory 

With a given set of memory blocks, the question is what these blocks are used for (and then, whether they are still needed). Such classification can use various strategies:

- What object type does a memory block belong to? Each Python object
  - inherently knows its type, and classifying memory by object type often already allows to determine where the memory is going.
- Where was the object allocated? Memory profilers for other languages
  - often are able to track, for each memory block, the code line at which the block was allocated. For some types (e.g. strings, lists), knowing the type doesn\'t say much what part of the code the object belongs to, so knowing where it was allocated is essential. Some of these tools even track the call stack that caused the allocation, since the allocation might have occurred in a library, yet the true reason for the allocation lies in one of the callers for the library.

# Tracking references 

Python\'s memory management is \"safe\", in the sense that memory won\'t be released while it is still referenced (unless there is a bug in an extension module). So if memory remains allocated even though it should have been released, it\'s typically because the objects are still referenced.

Again, the garbage collector provides machinery to determine what references an object has. Getting useful results out of that is a tedious task without proper tool support, though.
