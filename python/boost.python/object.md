# boost.python/object

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

The library provides a class called **object**, which encapsulates a valid Python object and provides a similar interface to Python\'s.

##### object operators 

The first challenge was to provide support for object manipulations using a Python-like syntax, mostly in the form of operator overloads:

::: {}
  --------------- --------------------------
  Python          C++
  y = x.foo       y = x.attr(\"foo\");
  x.foo = 1       x.attr(\"foo\") = 1;
  y = x\[z\]      y = x\[z\];
  x\[z\] = 1      x\[z\] = 1;
  y = x\[3:-1\]   y = x.slice(3,-1);
  y = x\[3:\]     y = x.slice(3,\_);
  y = x\[:-2\]    y = x.slice(\_,-2);
  z = x(1, y)     z = x(1, y);
  z = x.f(1, y)   z = x.attr(\"f\")(1, y);
  not x           !x
  x and y         x && y
  --------------- --------------------------
:::

##### object conversions 

*object* has a templated constructor which can be used to convert any C++ object to Python using the same underlying mechanisms used for the arguments to call\<\>.

If an *object* instance is created without any arguments to the constructor then this instance holds the value `None`.

##### object from PyObject \* 

You cannot directly construct an object from a [PyObject](./PyObject.html) \*, see [/handle](./boost(2e)python(2f)object(2f)handle.html)
