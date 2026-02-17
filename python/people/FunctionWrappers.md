# FunctionWrappers

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

[FunctionWrapper](http://c2.com/cgi/wiki?FunctionWrapper "Wiki") is a design pattern used when dealing with relatively complicated functions. The wrapper function typically performs some prologue and epilogue tasks like

- allocating and disposing resources
- checking pre- and post-conditions
- caching / recycling a result of a slow computation

but otherwise it should be *fully* compatible with the wrapped function, so it can be used instead of it. (This is related to the [DecoratorPattern](DecoratorPattern).)

As of Python 2.1 and the introduction of nested scopes, wrapping a function is easy:

:::: 
::: 
``` 
   1 def wrap(pre, post):
   2     def decorate(func):
   3         def call(*args, **kwargs):
   4             pre(func, *args, **kwargs)
   5             result = func(*args, **kwargs)
   6             post(func, *args, **kwargs)
   7             return result
   8         return call
   9     return decorate
```
:::
::::

The additional decorate function is needed to work with decorator syntax introduced in Python 2.4.

Now, let\'s wrap something up:

:::: 
::: 
``` 
   1 def trace_in(func, *args, **kwargs):
   2    print("Entering function",  func.__name__)
   3 
   4 def trace_out(func, *args, **kwargs):
   5    print("Leaving function", func.__name__)
   6 
   7 @wrap(trace_in, trace_out)
   8 def calc(x, y):
   9    return x + y
```
:::
::::

The wrapping effect is:

:::: 
::: 
``` 
   1 >>> print(calc(1, 2))
   2 Entering function calc
   3 Leaving function calc
   4 3
```
:::
::::

Of course, a wrapper would normally perform some more useful task. Have a look [here](https://web.archive.org/web/20080609050524/http://aspn.activestate.com/ASPN/Cookbook/Python/Recipe/412719) for a recipe how to wrap a function that processes files so that the result is recycled from a cache file if appropriate.
