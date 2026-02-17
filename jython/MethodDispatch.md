# MethodDispatch

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

One pattern of ensuring that a Jython base class implemented in Java can call an `@ExposedMethod`{.backtick} that has potentially been overridden in Python is to have a pair of methods on the base class:

- a `public`{.backtick} method named for the method to be overridden by the derived class.

- an `@ExposedMethod`{.backtick} declared as `final`{.backtick} that is available in python.

Then the derived class overrides the super class method in the [standard fashion](GeneratedDerivedClasses#Background), i.e.

- \"it will check for the existence of a (Python) method redefining (the exposed name of) that method. If it fails to find one, it calls the version in the principal class (using the `super`{.backtick} keyword in Java). If it finds a Python re-definition, it invokes that using `PyObject.__call__()`{.backtick}\"

This is done the use of the `rest`{.backtick} directive in the derived template - e.g. a typical implementation is:

:::: 
::: 
``` 
   1   base_class: PyDefaultDict
   2   want_dict: true
   3   ctr:
   4   incl: dict
   5   rest:
   6       public PyObject __missing__(PyObject key) {
   7           PyType self_type=getType();
   8           PyObject impl=self_type.lookup("__missing__");
   9           if (impl!=null) {
  10               return impl.__get__(this,self_type).__call__(key);
  11           }
  12           return super.__missing__(key);
  13       }
```
:::
::::

So the base class now defines an **@[ExposedMethod](./ExposedMethod.html)**:

:::: 
::: 
``` 
   1      @ExposedMethod
   2      final PyObject defaultdict___missing__(PyObject key) {
   3          if (defaultFactory == Py.None) {
   4              throw Py.KeyError(key);
   5          }
   6          return defaultFactory.__call__();
   7      }
```
:::
::::

and the public method calls the `@ExposedMethod`{.backtick} directly like:

:::: 
::: 
``` 
   1      public PyObject __missing__(PyObject key) {
   2          return defaultdict___missing__(key);
   3      }
```
:::
::::

So if any method in the base class calls the `public`{.backtick} method it will result in standard Java dynamic method dispatch to a `Py*Derived`{.backtick} class if the instance in question has derived from the base class and that will call the overridden python method if it exists or default back to the base classes implementation via `super`{.backtick}.
