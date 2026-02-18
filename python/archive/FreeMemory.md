# FreeMemory

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

As Christian Heimes describes it [here](http://groups.google.com/group/comp.lang.python/browse_thread/thread/32e62acc62773a3d#d9baaa3a229ad90b), Python uses its own memory allocator for small objects (\< 257 bytes). Larger objects are allocated directly with malloc, smaller objects end up in arenas. The code is well documented [in obmalloc.c](http://svn.python.org/view/python/trunk/Objects/obmalloc.c?rev=56476&view=auto).

- Classes with a [del] method may create reference cycles. The GC can\'t break cycles when a [del] method is involved.

- keeping references to tracebacks, exception objects (except Exception, err) or frames (sys.\_getframe())

Related information:

- [tips from Christian Heimes to find memory leaking code](http://groups.google.com/group/comp.lang.python/browse_thread/thread/7249eee28515bb92/d8007feb4df9fa4f?lnk=gst&q=trac+memory#d8007feb4df9fa4f)

- [difficulties to find a leak in Edgewall Trac](http://groups.google.com/group/trac-dev/browse_thread/thread/116e519da54f16b)

- [reducing the footprint of python applications](http://wingolog.org/archives/2007/11/27/reducing-the-footprint-of-python-applications)

- [CodingProjectIdeas/PythonGarbageCollected](../getting-started/CodingProjectIdeas/PythonGarbageCollected)
