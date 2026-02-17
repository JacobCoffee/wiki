# JythonDeveloperGuide/AttributeLookupMethods

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# Attribute Lookup Methods on `PyObject`.

::: 
### Why this document?

With the time, we have made some changes to the way the lookup methods behave on Java, to accommodate them to be as much compatible with CPython when they are exposed to Python code. As the time of this writing, `PyObject` has the following five methods related to attribute lookup.

> - `__findattr__`
> - `__findattr_ex__`
> - `__getattr__`
> - `object___getattribute__`
> - `object___findattr__`

This is without counting different signatures of the same method name. Such slight variants are not relevant to the discussion. Methods with the same name have the same semantics \-- the different variants just adapt the argument to a common type and then call the \"canonical\" implementation.
:::

::: 
### Quick Questions and Answers

If you don\'t want to read the whole history here are some generic answers, which are right on most cases:

*I\'m using Jython from Java code and want to get an attribute from a Python object. Which method should I use?*

Use `__findattr__`. Watch out for `null` return values when the attribute is not found.

*I\'m implementing a PyObject subclass. Which method should I override?*

First, make sure that you really want to override attribute lookup. Then, override `__findattr_ex__`. You can return `null` or throw `AttributeError` to report generic attribute lookup failure. Exceptions are expensive, so return `null` if you can. But if you are calling other code which may raise custom AttributeError instances, you have no chance than to let the exception propagate. Otherwise, you would \"swallow\" it. Don\'t forget to also expose your custom attribute lookup logic as `__getattribute__` since attribute lookups from Python code should yield the same results as lookup from Java code. As `__findattr_ex__` is obviously a virtual method, but the exposed one should only call final methods, use the following boilerplate:

    @ExposedType(name = "customobject")
    public class PyCustomObject extends PyObject {
    //...
        @Override
        public PyObject __findattr_ex__(String name) {
            return customobject___findattr__(name);
        }

        @ExposedMethod
        final PyObject customobject___getattribute__(PyObject arg)
            String name = asName(arg);
            PyObject ret = customobject___findattr__(name);
            if (ret == null)
                noAttributeError(name); // throw Py.AttributeError
            return ret;
        }

        // We put here what we would normally write inside ``__findattr_ex__``.
        // The goal is to avoid changing the behavior of the exposed
        // ``__getattribute__`` if ``__findattr_ex__`` is overriden on a
        // subclass.
        final PyObject customobject___findattr__(String name) {
            //
            // Implementation here!
            //
        }

    //...
    }
:::

::: 
### What\'s the difference?

First, we must differentiate between the methods which are part of the `PyObject` Java API, and those which are implementations exposed to Python. As you may expect, the ones starting with `object_` have to do with [exposed methods](PythonTypesInJava). `object__getattribute__` corresponds to the exposed `object.__getattribute`. However, `object__findattr__` is not exposed, but is an implementation detail of PyObject itself, related to the Java API methods which we will explain now in detail.

`__findattr__` and `__getattr__` are the primary ways to get an attribute from Java code. The difference is how they signal failed lookups. `__getattr__` throws `AttributeError` while `__findattr__` returns `null`. That\'s all. In practice `__findattr__` is a bit of a performance optimization, as throwing exceptions is an expensive operation. Thus, prefer it when you can.

`__findattr_ex__` is the virtual method that subclasses must implement if they need special attribute lookup logic. It may return `null` or throw `AttributeError`, whatever fits better the implementation. If there is no need to throw customized attribute error exceptions, it is preferred to return `null`, so it doesn\'t hurt the performance of, for example, the `hasattr` builtin. But if you call code which may raise custom `AttributeErrors` instances (or perhaps instances of `AttributeError` subclasses) you have to let the exception propagate, instead of swallowing it and return null (no point on doing that anyway, as the performance penalty of throwing an exception was already paid).

Thus, `__findattr__` and `__getattr__` are final methods which adapts the `__findattr_ex__` result to their stricter contract.

Now \-- unless you have a really really good reason and know what you are doing \-- , you want to reuse the exact logic implemented on `__findattr_ex__` to implement the exposed `__getattribute__` Python method. Look at the [Quick Questions and Answers](#quick-questions-and-answers) section above for a solution to this problem while still using non-overridable logic from the exposed method. After looking at it, it will be clear why the `object___findattr__` method exists.
:::
