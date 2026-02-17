# boost.python/InternalDataStructures

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

## Intro 

Python provides a \'Python/C API\' that allows you to create C/C++ extension modules and to embed the Python interpreter in your C/C++ programs. Pointers to PyObjects are the Python/C API\'s way to use Python objects from the C/C++ side.

[BoostPython](BoostPython) uses advanced C++ techniques to provide a much easier interface to the Python/C API. One manifestation of this is in python::object which is basically a (very) convenient, high-level wrapper around PyObject\*. A lower level wrapping around PyObject\* is python::handle.

### self

When a python class is being inherited from a c++ class, one must write a c++ wrapper around the c++ class.

This wrapper must have a pointer to a PyObject called self. It\'s the Python object which contains the C++ object instance.

## Memory consumption 

In general, a wrapped C++ object with a corresponding Python object is the size of:

- a new-style class (derived from \'object\' in Python) instance plus

- the extra size required to allow variable-length data in the instance, plus

- the size of the C++ object, plus

- the size of a *vtable* pointer, plus

- a pointer to the C++ object\'s instanceholder, plus

- zero or more bytes of padding required to ensure that the instanceholder is properly aligned.

You can see this in `boost/python/object/instance.hpp`. Most Python objects are represented by `instance<value_holder<T> >`, for some C++ class T.

All the code for implementing C++ object wrappers is in `libs/python/src/object/class.cpp`.

Instance dictionaries are created only \"on demand\", the first time the instance\'s `__dict__`{.backtick} attribute is accessed (see instance_get_dict).

        >>> a = A()  # some extension class A, no instance dict
        >>> a.x      # Attribute lookup fails, still no instance dict
        Traceback ...

        >>> a.y = 1  # y is a C++ data member, still no instance dict
        >>> a.x = 1  # creates an instance dict
        >>> z = A()
        >>> z.__dict__  # also creates an instance dict

If your C++ data structure contains pointers or smart pointers, you can arrange for Python objects to be created which only embed those pointers (instance\<pointer_holder\<Ptr\> \>). These Python objects will be in existence only as long as your Python code holds a reference to them.
