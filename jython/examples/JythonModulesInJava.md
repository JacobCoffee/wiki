# JythonModulesInJava

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

Writing a module extension Java for use by Jython can be done a couple of different ways.

- Write a POJO (Plain Old Java Object see [http://en.wikipedia.org/wiki/POJO](http://en.wikipedia.org/wiki/POJO)) with the same API as the Python module.

- Write a subclass of [PyObject](./PyObject.html).

The advantage to writing a POJO is the class can be reused in Java without any dependency on Jython\'s runtime. The downside to this approach is the class cannot take advantage of the dynamic nature of Python. The class cannot be modified at runtime with new methods or have its `__dict__`{.backtick} modified. It also means features such as iterators must go unimplemented.

The advantage of writing the class as a [PyObject](./PyObject.html) subclass is all of the dynamic nature of Python is available for use. For example, in Python it\'s possible to call a method with keyword arguments. This is not possible in Java and therefore the use of this feature is only available if the class implements [PyObject](./PyObject.html).

### Approach 

My original approach was to write as much of the class in Java as possible. This meant I always subclassed [PyObject](./PyObject.html) and spent the effort to write all the marshalling code in Java to make what would essentially be a POJO act as [PyObject](./PyObject.html). This results in a lot of work but it does offer the greatest amount of flexibility and speed.

My new approach is borrowed slightly from CPython where it\'s very common to write a C library, a straight wrapper and then a Pythonic wrapper. In Jython, the first two steps are really one so the development effort is significantly simplified. Writing a wrapper in Python offers the dual benefits of being easy to maintain and refactor as well as requiring less development time..
