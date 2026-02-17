# boost.python/GettingStarted

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

## Introduction 

The [BoostPython](BoostPython) Library binds C++ and Python in a mostly-seamless fashion. It is just one member of the boost C++ library collection at [http://www.boost.org](http://www.boost.org).

Use the [BoostPython](BoostPython) Library to quickly and easily export C++ to Python such that the Python interface is very similar to the C++ interface. It is designed to be minimally intrusive on your C++ design. In most cases, you should not have to alter your C++ classes in any way in order to use them with Boost.Python. The system should simply *reflect* your C++ classes and functions into Python. Boost.Python bindings are written in pure C++, using no tools other than your editor and your C++ compiler.

The Python [C++-sig](http://www.python.org/sigs/current/cplusplus-sig/) serves as a mailing list for users of the library. Documentation for the current release is available at [http://www.boost.org/libs/python/](http://www.boost.org/libs/python/). Development documentation, which is usually more up-to-date, is available through the [Boost CVSWeb](http://cvs.sourceforge.net/cgi-bin/viewcvs.cgi/*checkout*/boost/boost/libs/python/doc/index.html) interface.

### Relationship to the Python C API 

Python already provides an API for gluing together Python and C. So what is Boost::Python? Boost::Python is a wrapper for the Python/C API.

Using the Python/C API, you have to deal with passing pointers back and forth between Python and C, and worry about pointers hanging out in one place when the object they point to has been thrown away. Boost::Python takes care of much of this for you. In addition, Boost::Python lets you write operations on Python objects in C++ in OOP style.

For example, using the Python/C API, to do the C++ equivalent of \"y = object_x\[i\]\", you might do:

    y = PySequence_GetItem(object_x, i);

By contrast, in Boost::Python, you can just do:

    y = object_x[i];

In addition, Boost::Python makes it easy to EXPORT your C++ classes into Python, without even changing them. Boost::Python is designed with the idea in mind that users never touch a PyObject\*.

### If you need to get to the underlying Python/C API 

If you do use Boost::Python, though, you can still use stuff from the Python/C API in your C++ code. You don\'t even need to import the Python.h header file. Just use the functions. For example, to clear an error in Python that you caught in C++, you could do this in the middle of an otherwise purely Boost::Python program:

    PyErr_Clear();

In C++, the Python/C API represents Python objects by [PyObject](./PyObject.html) pointers. In Boost::Python, these are wrapped by instances of the boost::python::object class.

If you need the underlying [PyObject](./PyObject.html) of any boost::python::object, you can get it via the ptr() method of boost::python::object, which returns a [PyObject](./PyObject.html)\*. You can then use it in Python/C API calls. For example, to test if a boost::python::object called boostObj has an attribute called \"myAttributeName\", you can do:

    PyObject_HasAttrString(boostObj.ptr(), "myAttributeName");
