# boost.python/OverridableVirtualFunctions

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# Overridable Virtual Functions 

In the previous example we exposed a simple C++ class in Python and showed that we could write a subclass. We even redefined one of the functions in our derived class. Now we will learn how to make the function behave virtually *when called from* C++.

## Example 

In this example, it is assumed that `hello::greet()`{.backtick} is a virtual member function:

    class hello
    {
     public:
        hello(const std::string& country) { this->country = country; }
        virtual std::string greet() const { return "Hello from " + country; }
        virtual ~hello(); // Good practice
        ...
    };

We\'ll need a derived class^[1](#fnref-a601a5360c1e729befc29729b3bebf6a4cd6e3fd)^ to help us dispatch the call to Python. In our derived class, we need the following elements:

1.  A PyObject\* data member (usually called `self`{.backtick}) that holds a pointer to the Python object corresponding to our C++ *hello* instance.

2.  For each exposed constructor of the base class `T`{.backtick}, a constructor which takes the same parameters preceded by an initial PyObject\* argument. The initial argument should be stored in the `self`{.backtick} data member described above.

3.  If the class being wrapped is ever returned *by value* from a wrapped function, be sure you do the same for the `T`{.backtick}\'s copy constructor: you\'ll need a constructor taking arguments (PyObject\*, const T&).

4.  An implementation of each virtual function you may wish to override in Python which uses `call_method<return-type>(self, "name", args...)` to call the Python override.

5.  For each non-pure virtual function meant to be overridable from Python, a static member function (or a free function) taking a reference or pointer to the `T`{.backtick} as the first parameter and which forwards any additional parameters neccessary to the default implementation of the virtual function. See below if the base class virtual function is private.

<!-- -->

    struct hello_callback : hello
    {
        // hello constructor storing initial self parameter
        hello_callback(PyObject *p, const std::string& x) // 2
            : hello(x), self(p) {}

        // In case hello is returned by-value from a wrapped function
        hello_callback(PyObject *p, const hello& x) // 3
            : hello(x), self(p) {}

        // Override greet to call back into Python
        std::string greet() const // 4
            { return call_method<std::string>(self, "greet"); }

        // Supplies the default implementation of greet
        static std::string default_greet(const hello& self_) const // 5
            { return self_.hello::greet(); }
     private:
        PyObject* self; // 1
    };

Finally, we add hello_callback to the `class_<>`{.backtick} declaration in our module initialization function, and when we define the function, we must tell Boost.Python about the *default* implementation:

    // Create the Python type object for our extension class
    class_<hello,hello_callback> ("hello", init<std::string>())
        // Add a virtual member function
        .def("greet", &hello_callback::default_greet);

Now our Python subclass of `hello`{.backtick} behaves as expected:

    >>> class wordy(hello):
    ...     def greet(self):
    ...         return hello.greet(self) + ', where the weather is fine'
    ...
    >>> hi2 = wordy('Florida')
    >>> hi2.greet()
    'Hello from Florida, where the weather is fine'
    >>> invite(hi2)
    'Hello from Florida, where the weather is fine! Please come soon!'

::: footnotes
1.  []You may ask, \"Why do we need this derived class? This could have been designed so that everything gets done right inside of hello.\" One of the goals of Boost.Python is to be minimally intrusive on an existing C++ design. In principle, it should be possible to expose the interface for a 3rd party library without changing it. To unintrusively hook into the virtual functions so that a Python override may be called, we must use a derived class. ([1](#fndef-a601a5360c1e729befc29729b3bebf6a4cd6e3fd-0))
:::

## Pure Virtual Functions 

A pure virtual function with no implementation is actually a lot easier to deal with than a virtual function with a default implementation. First of all, you obviously don\'t need to supply a default implementation. Secondly, you don\'t need to call *def()* on the `extension_class<>`{.backtick} instance for the virtual function. In fact, you wouldn\'t want to: if the corresponding attribute on the Python class stays undefined, you\'ll get an *AttributeError* in Python when you try to call the function, indicating that it should have been implemented. For example:

    #include <boost/python/class.hpp>
    #include <boost/python/module_init.hpp>
    #include <boost/python/def.hpp>
    #include <boost/python/call_method.hpp>
    #include <boost/ref.hpp>
    #include <boost/utility.hpp>

    using namespace boost::python;

    struct baz {
        virtual int pure(int) = 0;
        int calls_pure(int x) { return pure(x) + 1000; }
    };

    struct baz_callback : baz {
        baz_callback(PyObject *p) : self(p) {}
        int pure(int x) { return call_method<int>(self, "pure", x); }
        PyObject *self;
    };

    BOOST_PYTHON_MODULE_INIT(foobar)
    {
         class_<baz, boost::noncopyable, boost::shared_ptr<baz_callback> >("baz")
             .def("calls_pure", &baz::calls_pure);
    }

Now in Python:

    >>> from foobar import baz
    >>> x = baz()
    >>> x.pure(1)
    Traceback (innermost last):
      File "<stdin>", line 1, in ?
    AttributeError: pure
    >>> x.calls_pure(1)
    Traceback (innermost last):
      File "<stdin>", line 1, in ?
    AttributeError: pure
    >>> class mumble(baz):
    ...    def pure(self, x): return x + 1
    ...
    >>> y = mumble()
    >>> y.pure(99)
    100
    >>> y.calls_pure(99)
    1100

## Private Non-Pure Virtual Functions 

This is one area where some minor intrusiveness on the wrapped library is required. Once it has been overridden, the only way to call the base class implementation of a private virtual function is to make the derived class a friend of the base class. You didn\'t hear it from me, but most C++ implementations will allow you to change the declaration of the base class in this limited way without breaking binary compatibility (though it will certainly break the [ODR](http://cs.calvin.edu/c++/C++Standard-Nov97/basic.html#basic.def.odr)).
