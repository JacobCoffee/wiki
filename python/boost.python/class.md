# boost.python/class

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

**class\_\<\>** statement constructs python class object.

Usually it\'s included in BOOST_PYTHON_MODULE to wrap C++ class:

    class A { ... };
    BOOST_PYTHON_MODULE(example)
    {
      class_<A>("A");
    }

Also it can be used explicitly to create class instances from C++:

    BOOST_PYTHON_MODULE(example1)
    {
      object class_a = class_<A>("A");

      object instance_a = class_a();
    }

If you want to forbid creating class instancies from python, you now must pass `no_init`{.backtick} to class\_\<\> definition. Default, as in python, will be init with no arguments. There is no limit to number of init\<\>\'s in the boost.python.

**Abstract class**

Pure virtual (abstract) class shall be wrapped with

    class_< Abstract , boost::noncopyable>("Abstract", no_init);

Because if you don\'t tell it that class is noncopyable, Boost.Python tries to register a converter for handling wrapped functions which handle function returning values of class type. Naturally, this has to be able to copy construct the returned C++ class object into storage that can be managed by a Python object. Since this is an abstract class, that fails.

**C++ object storage**

Boost.Python allows you to specify how Python objects will hold the C++ objects they wrap. You can specify that they be held by *shared_ptr\<T\>* (or any other smart pointer), in which case the library will generate converters to/from Python for *shared_ptr\<T\>*. The *to_python converters* will simply build a new Python object around the *shared_ptr\<\>*. You can specify that your C++ object is held by *shared_ptr\<U\>*. That allows you to hold a U object for dispatching, yet still pass shared_ptrs around in your C++ code.

If you have virtual functions you want to *override in Python*, you actually have to hold the T object with a derived class U which overrides the virtual functions to dispatch back to Python. In this case, class U naturally has to have access to the Python object

There are several problems with the above arrangement, but the most important one is that if you keep the shared_ptr\<U\> alive longer than its corresponding Python object, calls to the Python-overridable virtual functions will crash, because they\'ll try to call through an invalid pointer.

**Synopsis:**

    class_<A>("A")
        .def(init<int, int>())
        .def(...)
        ;

    class_<B>("B", init<int, int>())
        .def(...)
        ;

    class_<C>("C", "C's docstring", init<int, int>())
        .def(...)
        ;

    class_<D>("D", "D's docstring", init<int, int>(), "__init__ doc")
        .def(...) 
        ;


    class_<E>("E")
        .def(...)
        ;

    class_<F>("F", no_init)
        .def(...)
        ;

    class_<G>("G", "G's docstring", no_init)
        .def(...) 
        ;

    class_<H>("H", "H's docstring")
        .def(...) 
        ;
