# boost.python/SimpleExample

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

Suppose we have the following C++ API which we want to expose in Python:

    #include <string>

    namespace { // Avoid cluttering the global namespace.

      // A couple of simple C++ functions that we want to expose to Python.
      std::string greet() { return "hello, world"; }
      int square(int number) { return number * number; }
    }

Here is the C++ code for a python module called getting_started1 which exposes the API.

    #include <boost/python.hpp>
    using namespace boost::python;

    BOOST_PYTHON_MODULE(getting_started1)
    {
        // Add regular functions to the module.
        def("greet", greet);
        def("square", square);
    }

That\'s it! If we build this shared library and put it on our PYTHONPATH we can now access our C++ functions from Python.

    >>> import getting_started1
    >>> print getting_started1.greet()
    hello, world
    >>> number = 11
    >>> print number, '*', number, '=', getting_started1.square(number)
    11 * 11 = 121
