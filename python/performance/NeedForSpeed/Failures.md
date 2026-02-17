# NeedForSpeed/Failures

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# Things that we tried but decided were not good ideas. 

**Using more aggressive calling conventions/inlining in ceval**

The Py_LOCAL/Py_LOCAL_INLINE macros can be used instead of static to force the use of a more efficient C calling convention, on platforms that support that. We tried applying that to ceval, and saw small speedups on some platforms, and somewhat larger slowdowns on others.

**List pre-allocation**

Adding the ability to pre-allocate builtin list storage. At best we can speed up appends by about 7-8% for lists of 50-100 elements. For the large part the benefit is 0-2%. For lists under 20 elements, peformance is actually reduced when pre-allocating.

**Out-thinking exceptions**

CPython spends considerable time moving exception info around among thread states, frame objects, and the `sys`{.backtick} module. This code is complicated and under-documented. Patch [1145039](http://bugs.python.org/issue1145039 "SF") took a stab at reverse-engineering a weak invariant, and exploited it for a bit of speed. That worked fine so far as it went (and a variant was checked in), but it\'s likely more remains to be gotten. Alas, the `tim-exc_sanity`{.backtick} branch set up to try that consumed a lot of time fighting mysteries, and looks like it\'s more trouble than it\'s worth.

**Singleton of [StopIteration](./StopIteration.html)**

As part of the new exceptions implementation, we tried making a singleton [StopIteration](./StopIteration.html) instance. No speedup was detected. This is primarily due to most uses of [StopIteration](./StopIteration.html) using the type object directly (ie \"raise [StopIteration](./StopIteration.html)\" vs. \"raise [StopIteration](./StopIteration.html)()\"). Even for a crafted test case where the instance use was forced there was no detectable change in speed.

**GET_SIZE Macros**

Making a [PyDict](./PyDict.html)\_GET_SIZE like [PyTuple](./PyTuple.html)\_GET_SIZE doesn\'t give a measurable improvement in pybench or pystone. This is likely because the compiler notices that those functions that use it have alreaday done NULL checks and frequently [PyDict](./PyDict.html)\_Check so we aren\'t telling it anything it didn\'t already know.

Conversely changing all Py(Tuple\|List)\_GET_SIZE to point to plain Size has no measurable slowdown! Well, in the range of 0.5%, which may just be noise. Switching the #define to the real functions generates some spurious warnings because the regular methods expect [PyObjects](./PyObjects.html) and not the more specific types.

**Specializing Dictionaries**

One man-day was spent trying to seperate the dicts used in namespaces (module.[dict], instance/type/class [dicts]) the result was changing over a quarter of the [PyDict](./PyDict.html)\* macros in the trunk to [PySymdict](./PySymdict.html) (over half if you exclude Modules/). This was such a massive change it was abandoned after sprint Day1.

**Switching to 64-bit ints on 32-bit platforms**

Tested out an idea about switching Python \"integer\" types to use 64 bits instead of 32 bits on 32-bit platforms. In the end, it would have been a major pain to do, and while it would have resulted in 34% performance improvements for apps that use integers between 32 and 64 bits, it would have been around a 10% slow-down for apps that only use 32-bit numbers. Decided not to do it for those reasons.

**Pymalloc with VC8**

Tried not using the pymalloc module in the VC8 windows build environment. MS boasts of its own fast small block allocator, but it turned out not to work. Possibly it needs to be explicitly turned on!

**Unicode Classification**

Disabling the Unicode classification stuff (isupper) and using the c-runtime supplied one, turned out to be much slower. no surprises.
