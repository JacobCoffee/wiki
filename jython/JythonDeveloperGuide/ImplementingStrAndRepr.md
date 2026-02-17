# JythonDeveloperGuide/ImplementingStrAndRepr

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# Implementing `__str__` and `__repr__`

When coding a subclass of PyObject, it is somewhat tricky to get a correct implementation of `__repr__` and `__str__` which works through the exposed methods and the related builtins, while also supporting derived types. Here are some quick guidelines to help with this problem.

::: 
### Same implementation for `__repr__` and `__str__`

> 1.  Write the exposed method:
>
>         @ExposedMethod(names = {"__str__", "__repr__"})
>         final PyString foo_toString() {
>             // Implementation
>         }
>
> 2.  Override toString() and manually call exposed method:
>
>         @Override
>         public String toString() {
>             return foo__repr__().toString()
>         }

\[The second step is to keep the builtins repr() and str() working. `repr()` calls `PyObject#__repr__()`, which calls `Object#toString()`. And `str()` calls `PyObject#__str__()` which calls `PyObject#__repr__()`\]
:::

::: 
### Different implementations for `__str__` and `__repr__`

> 1.  Write the exposed `__str__` and call it from the overriden `__str__`:
>
>         @ExposedMethod
>         final PyString foo___str__() {
>             // Implementation
>         }
>
>         @Override
>         public PyString __str__() {
>             return foo__str__();
>         }
>
> 2.  Same thing for `__repr__`:
>
>         @ExposedMethod
>         final PyString foo___repr__() {
>             // Implementation
>         }
>
>         @Override
>         public PyString __repr__() {
>             return foo__repr__();
>         }
>
> 3.  Override `toString`:
>
>         @Override
>         public String toString() {
>             return foo___str__().toString()
>         }

\[Now, once you have overridden the three important methods, you don\'t have to care about the interrelations which are present on the default implementations of `PyObject`\]
:::

::: 
### Only implement `__str__`

Follow the step 1 of the previous recipe. Optionally you can also follow the step 3 if you want to map `toString()` to `__str__()` .
:::
