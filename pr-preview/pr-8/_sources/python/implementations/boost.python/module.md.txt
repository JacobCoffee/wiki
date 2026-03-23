# boost.python/module

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

## def

Boost.Python now supports a free-function version of **def** which defines its function in the current scope:

      #include <boost/python.hpp>

      BOOST_PYTHON_MODULE(my_module)
      {
        def("name", function_ptr);
        def("name", function_ptr, call_policies);
        def("name", function_ptr, "documentation string");
        def("name", function_ptr, call_policies, "documentation string");
      }

etc.

## scope

To get access to the current module, you can declare the current scope:

      #include <boost/python.hpp>

      BOOST_PYTHON_MODULE(my_module)
      {
        // set the docstring of the current module scope
        scope().attr("__doc__") = "my module's docstring";
        ...

        scope current;
        current.attr("x") = 1; // my_module.x = 1
      }

Of course, you can also set the current scope to any object:

      object some_obj;
      scope within(some_obj);
      def("foo", &foo); // define a function within some_obj as a namespace

and all subsequent definitions (classes, enums etc.) will go inside current then scope.

Be warned, however, that although you can set the current scope from a class\_\<\> instance, the class\_\<\>\'s def() member function will work properly in some cases where the free-function def() cannot, since the latter is missing information about the class type being wrapped.

***what is a scope?***

The scope is a class that has an associated global Python object which controls the Python namespace in which new extension classes and wrapped functions will be defined as attributes. Details can be found at [boost.python/scope](./boost(2e)python(2f)scope.html).
