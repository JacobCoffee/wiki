# PortingExtensionModulesToPy3k

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

::: 
Caution!

**Python 2.x will no longer be supported after 1 Jan 2020.**

Python 2 reaches end of life in January 2020, and will no longer receive security updates. This page has resources to help with porting applications still running Python 2 to Python 3.
:::

::: 
Note

The first draft for this document was written by Benjamin Peterson at [http://docs.python.org/howto/cporting](http://docs.python.org/howto/cporting).
:::

:::::::::::: 
### Porting Extension Modules to 3.0

  --------- -------------------
  author:   Benjamin Peterson
  --------- -------------------

::: topic
Abstract

Although changing the C-API was not one of Python 3.0\'s objectives, the many Python level changes made leaving 2.x\'s API intact impossible. In fact, some changes such as `int` and `long` unification are more obvious on the C level. This document endeavors to document incompatibilities and how they can be worked around.
:::

::: 
#### Conditional compilation

The easiest way to compile only some code for 3.0 is to check if `PY_MAJOR_VERSION` is greater than or equal to 3.

    #if PY_MAJOR_VERSION >= 3
    #define IS_PY3K
    #endif

API functions that are not present can be aliased to their equivalents within conditional blocks.
:::

::::: 
#### Changes to Object APIs

Python 3.0 merged together some types with similar functions while cleanly separating others.

::: 
##### str/unicode Unification

Python 3.0\'s `str` (`PyString_*` functions in C) type is equivalent to 2.x\'s `unicode` (`PyUnicode_*`). The old 8-bit string type has become `bytes`. Python 2.6 and later provide a compatibility header, `bytesobject.h`, mapping `PyBytes` names to `PyString` ones. For best compatibility with 3.0, `PyUnicode` should be used for textual data and `PyBytes` for binary data. It\'s also important to remember that `PyBytes` and `PyUnicode` in 3.0 are not interchangeable like `PyString` and `PyString` are in 2.x. The following example shows best practices with regards to `PyUnicode`, `PyString`, and `PyBytes`.

    #include "stdlib.h"
    #include "Python.h"
    #include "bytesobject.h"

    /* text example */
    static PyObject *
    say_hello(PyObject *self, PyObject *args) {
        PyObject *name, *result;

        if (!PyArg_ParseTuple(args, "U:say_hello", &name))
            return NULL;

        result = PyUnicode_FromFormat("Hello, %S!", name);
        return result;
    }

    /* just a forward */
    static char * do_encode(PyObject *);

    /* bytes example */
    static PyObject *
    encode_object(PyObject *self, PyObject *args) {
        char *encoded;
        PyObject *result, *myobj;

        if (!PyArg_ParseTuple(args, "O:encode_object", &myobj))
            return NULL;

        encoded = do_encode(myobj);
        if (encoded == NULL)
            return NULL;
        result = PyBytes_FromString(encoded);
        free(encoded);
        return result;
    }
:::

::: 
##### long/int Unification

In Python 3.0, there is only one integer type. It is called `int` on the Python level, but actually corresponds to 2.x\'s `long` type. In the C-API, `PyInt_*` functions are replaced by their `PyLong_*` neighbors. The best course of action here is using the `PyInt_*` functions aliased to `PyLong_*` found in `intobject.h`. The abstract `PyNumber_*` APIs can also be used in some cases.

    #include "Python.h"
    #include "intobject.h"

    static PyObject *
    add_ints(PyObject *self, PyObject *args) {
        int one, two;
        PyObject *result;

        if (!PyArg_ParseTuple(args, "ii:add_ints", &one, &two))
            return NULL;

        return PyInt_FromLong(one + two);
    }
:::
:::::

:::: 
#### Module initialization and state

Python 3.0 has a revamped extension module initialization system. (See PEP [PEP 3121](http://www.python.org/dev/peps/pep-3121).) Instead of storing module state in globals, they should be stored in an interpreter specific structure. Creating modules that act correctly in both 2.x and 3.0 is tricky. The following simple example demonstrates how.

    #include "Python.h"

    struct module_state {
        PyObject *error;
    };

    #if PY_MAJOR_VERSION >= 3
    #define GETSTATE(m) ((struct module_state*)PyModule_GetState(m))
    #else
    #define GETSTATE(m) (&_state)
    static struct module_state _state;
    #endif

    static PyObject *
    error_out(PyObject *m) {
        struct module_state *st = GETSTATE(m);
        PyErr_SetString(st->error, "something bad happened");
        return NULL;
    }

    static PyMethodDef myextension_methods[] = {
        {"error_out", (PyCFunction)error_out, METH_NOARGS, NULL},
        {NULL, NULL}
    };

    #if PY_MAJOR_VERSION >= 3

    static int myextension_traverse(PyObject *m, visitproc visit, void *arg) {
        Py_VISIT(GETSTATE(m)->error);
        return 0;
    }

    static int myextension_clear(PyObject *m) {
        Py_CLEAR(GETSTATE(m)->error);
        return 0;
    }


    static struct PyModuleDef moduledef = {
            PyModuleDef_HEAD_INIT,
            "myextension",
            NULL,
            sizeof(struct module_state),
            myextension_methods,
            NULL,
            myextension_traverse,
            myextension_clear,
            NULL
    };

    #define INITERROR return NULL

    PyObject *
    PyInit_myextension(void)

    #else
    #define INITERROR return

    void
    initmyextension(void)
    #endif
    {
    #if PY_MAJOR_VERSION >= 3
        PyObject *module = PyModule_Create(&moduledef);
    #else
        PyObject *module = Py_InitModule("myextension", myextension_methods);
    #endif

        if (module == NULL)
            INITERROR;
        struct module_state *st = GETSTATE(module);

        st->error = PyErr_NewException("myextension.Error", NULL, NULL);
        if (st->error == NULL) {
            Py_DECREF(module);
            INITERROR;
        }

    #if PY_MAJOR_VERSION >= 3
        return module;
    #endif
    }

::: 
##### Embedding

When defining a module for an embedded interpreter, the module has to be registered in the PyImport_Inittab table; simply calling `PyModule_Create` or the module\'s init function is not enough. Use `PyImport_AppendInittab` to register your module with its init function:

    PyImport_AppendInittab("myextension", initmyextension);

This call should occur before Py_Initialize(), but this is not mandatory.

Note that this method also works for python 2.4 at least.
:::
::::

::: 
#### PyCObject / PyCapsule

The PyCObject is being phased out starting with Python 3.1. The new PyCapsule object should be used instead.
:::

::: 
#### Other options

If you are writing a new extension module, you might consider [Cython](http://www.cython.org). It translates a Python-like language to C. The extension modules it creates are compatible with Python 3.x and 2.x.
:::
::::::::::::

::: 
### Martin\'s notes from psycopg2 porting

- bytes vs. strings 2. To keep the implementation portable across 2.x and 3.x, I added a number of macros. Most useful was Text_FromUTF8, particularly when applied to the (many) string literals. It is defined as PyString_FromString for 2.x, and PyUnicode_FromString for 3.x.
- RO is gone, you need to use READONLY (which also works in 2.x).
- PyVarObject_HEAD_INIT needs to be used for types. I define it for 2.x if it isn\'t already defined.
- module initialization is different. I moved the majority of the code into a static function, which then gets conditionally called from either the 2.x or 3.x init routine.
- More detail written up for the [python-porting list](https://mail.python.org/pipermail/python-porting/2008-December/000010.html)
:::

::: 
### Philip Semanchuk\'s notes from porting posix_ipc and sysv_ipc

I added Python 3 compatibility to my modules [posix_ipc](http://semanchuk.com/philip/posix_ipc/) and [sysv_ipc](http://semanchuk.com/philip/sysv_ipc/) while retaining compatibility with Python 2.x (from 2.4 or 2.5, at least). I managed to keep it all in one codebase.

I didn\'t know this document existed when I did my work, so I did things the hard way. I started by reading the Python 3 C API documentation and then compiling my Python 2.x code and attacking where the compiler complained.

Note that [Python 3.0 has been given a decent burial](http://www.python.org/download/releases/3.0.1/) so you probably don\'t need to support it. Start working with Python 3.1; it\'s easier.

I used a lot of the same techniques Martin used (see psycopg notes above). One major stylistic difference is that instead of defining a macro like Martin\'s Text_FromUTF8, I have a lot of code that looks like this:

    #if PY_MAJOR_VERSION > 2
        return PyUnicode_FromString(name ? name : "(no name)");
    #else
        return PyString_FromString(name ? name : "(no name)");
    #endif

This became tedious and I think a macro might be a better solution. I used the same ifdef technique for many calls to `PyInt_FromLong/PyLong_FromLong` and think a macro might have been a better choice there, too.

Some of my code needs to accept strings that can contain C NULLs (`0x00`). Under Python 2.x the argument format code for this is s# and the caller\'s string is split ino two C variables (a `char *` and an `int`). Under Python 3.x, the preferred format code is s\* and the caller\'s string is placed into a `PyBuffer` struct.

To deal with this difference, I created a struct that mimiced `Py_buffer` so that my code could be mostly agnostic to which it was dealing with. There\'s a good example of this in the function `MessageQueue_send()` which is on line 1397 of posix_ipc_module.c in version 0.8.0 of posix_ipc.

Something that helped me a lot generally was to download the source for cx_Oracle which was a module that had already been made Python 2 & 3 compatible. When the compiler complained about a 2.x-specific function in my code (e.g. `PyInt_Check`), I grepped the cx_Oracle code to see what substitution they made for the function in question.

My modules and cx_Oracle are all BSD-licensed so even GPLed projects can mine the source code for tips.
:::

::: 
### Links

> - [Brandon Rhodes on porting a C extension module to Python 3.0](http://rhodesmill.org/brandon/2008/porting-a-c-extension-module-to-python-30/)
> - sq_slice handling has changed. Simple slicing was removed from the C API. [Notes on how to fix it.](http://renesd.blogspot.com/2009/07/python3-c-api-simple-slicing-sqslice.html)
> - [Stephen Deibel\'s blog post on supporting Python 2.0 through 3.0](http://pythonology.blogspot.com/2009/02/making-code-run-on-python-20-through-30.html)
> - [Py3kExtensionModules](https://wiki.python.org/moin/Py3kExtensionModules)
:::
