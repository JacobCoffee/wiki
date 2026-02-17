# API

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

**API** is a shortcut for \"Application Programming Interface\".

Loosely defined, API describes everything an application programmer needs to know about piece of code to know how to use it. The idea is that the programmer knows all [Signature](./Signature.html)s of classes and methods; their parameters, parameter types (or behaviour) as well as return values.

A programmer should always write against interface (API), **not** against implementation. This is especially important in Python. If you know a class has method subfrob(), you\'d be better off with

    if hasattr(obj, 'subfrob'):
        do_something(obj)
    else:
        well_do_something_else

instead of using `isinstance(obj, SomeSpecificClass)`{.backtick}. Effectively, this is applying idiom \"if it walks like a duck, quacks like a duck\...\" it\'s a duck alright. Controlling behaviour depending on class instance used is more like programming to implementation, whereas programming against \"signature\" is more like programming against interface.

An example of API can be found at [Voicent Simple Telephone Call API](../people/Voicent Simple Telephone Call API). The published class is used to encapsulate the implementation details.
