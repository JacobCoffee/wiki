# CodingProjectIdeas/PythonGarbageCollected

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

It would be nice to see the reference implementation of Python change from reference counting and use another garbage collection scheme. The should improve runtime performance in both CPU and locality of reference.

\-\--

I actually got a semi-working python running with boehm GC, but did not complete the conversion, and have not yet posted it anywhere. If you\'re interested, let me know, and I can resurrect and post the patch-so-far on my website. However, it\'s unlikely to actually run faster, because you can\'t use tricks like keeping free lists, and the Boehm GC is conservative, so it can\'t move objects, so allocating memory is just as expensive as usual, only we\'d be doing way more of it. With CPython I believe it is essentially impossible to use a copying GC because of its heavy integration with and dependance upon C code, so unless you\'re planning on making something other than CPython the reference implementation, this is very unlikely to be successful. \--[James Y Knight](http://fuhm.net)

I agree with James that this is doable, but it is a much bigger project than one might think since CPython is heavily dependent on the idea of reference counting. Several places perform optimization tricks based on the refcount of an object; changing the scheme would require ferretting out all of that code and changing it to work with whatever scheme is used. So if you do decide to attempt this, brace for an actual performance drop. =) \-- Brett Cannon

I agree with everything said so far \-- it would be great to see someone do a really thorough job of exploring the possibilities in this area, but unless you find some way of playing nice to C extensions and still having a copying collector, I wouldn\'t be too optmistic that any actually useful code would come from it. \-- [MichaelHudson](MichaelHudson)

------------------------------------------------------------------------

[CategoryEditors](CategoryEditors)
