# boost.python/handle

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

David Abrahams\' Guidelines (republished with permission from [http://mail.python.org/pipermail/cplusplus-sig/2008-October/013895.html](http://mail.python.org/pipermail/cplusplus-sig/2008-October/013895.html)):

- handle, essentially a smart pointer. Use when necessary.
  - a handle\<\> can be NULL, and maintains a reference count on the object it points to

  - handle\<\> y(null_ok(x)) allows y to become NULL

  - handle\<\> y(x), where x is not the result of null_ok, never results in a NULL y. An exception will be thrown if x is NULL

  - handle\<\> y(borrowed(x)) presumes that \*x is borrowed and thus increments its reference count.

  - handle\<\> y(x), where x is not the result of borrowed, presumes that someone has already incremented the reference count on \*x for us.

  - you can combine borrowed and null_ok in any order, so the following are equivalent:
    - handle\<\> y(borrowed(null_ok(x)))

    - handle\<\> y(null_ok(borrowed(x)))
- object, a higher-level notion. Use wherever possible.
  - an object can\'t be constructed from a raw [PyObject](./PyObject.html)\* because there\'s no information in that type about whether the refcount has been incremented for this additional reference

  - an object can only be constructed from a handle\<\>. Other interfaces are not for public consumption and thus not documented. Use at your own peril.

  - an instance of object always \"points to\" something (maybe None). If the constructor argument (handle) is NULL, an exception will be thrown.

You should also always give the handle\<\> a name instead of making it a temporary for the same reasons as cited in Peter Dimov\'s guideline: [\"Smart Pointer Best Practices\"](http://www.boost.org/doc/libs/1_36_0/libs/smart_ptr/shared_ptr.htm#BestPractices)
