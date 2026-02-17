# boost.python/FAQ

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

Composed from the comp.python.c++ newsgroup hosted on news.gmane.org. See[official boost.python FAQ](http://www.boost.org/libs/python/doc/v2/faq.html).

### The constructor AND the destructor of a C++ class that I am trying to wrap are private (this class is designed following the singleton DP). Is it possible to wrap such a class? 

### The constructors of some classes I am trying to wrap are private because instances must be created by using a factory. Is it possible to wrap such classes? 

Sure. Of course you can only create the instances using the factory\...

If you look at libs/python/test/test_pointer_adoption.cpp you\'ll see the factory function \"create\" is being used to generate new instances of class A. It uses return_value_policy\<manage_new_object\> to instruct Python to adopt the A\* to hold the instance.

    A* create(std::string const& s)
    {
        return new A(s);
    }

    BOOST_PYTHON_MODULE(test_pointer_adoption_ext)
    {
            // Specify the manage_new_object return policy to take
            // ownership of create's result
            def("create", create, return_value_policy<manage_new_object>());
            
            class_<A>("A", no_init)
                .def("content", &A::content)
                .def("get_inner", &A::get_inner, return_internal_reference<>())
            ;
    }

### What is the relation between this \'\'\'no_init\'\'\' and \'\'\'boost::noncopyable?\'\'\' 

The only relationship is that they both deal with constructors.

- `no_init`{.backtick} means \"do not try to create an instance of that Python object, create `__init__`{.backtick} function that throws an exception\"

- `noncopyable`{.backtick} means \"do not try to register a converter which can convert C++ return values of that class to Python\".

When wrapping an abstract class, it\'s necessary to specify both.

### Is it is possible to convert pointers to existing classes to PyObjects\* and then be able to pass an existing instance of an object directly to and from python? 

It is.

Example: In C++ I create a CWheel and I set its member m_diameter to 1233. In python I have a function that receives a CWheel and displays the diameter (Let\'s suppose that Python knows the CWheel from Boost.Python):

    def printCWheelDiam(awheel):
        print awheel.m_diameter

The safest thing to do is to create the CWheel by invoking its class wrapper:

        // Declare the CWheel extension class
        object wheel_class =
            class_<CWheel>("CWheel")
                .def_readonly("m_diameter", &CWheel::m_diameter)
                .def("some_member_function", &CWheel::some_member_function)
                ...
                ;

        object wheel_obj = wheel_class(); // construct one

Now you can pass wheel_obj back to python, and all reference counts are nicely managed. You don\'t need to \"map\" anything between C++ and Python; the library takes care of that for you.

If you really want to pass pointers around, it\'s certainly possible to tell the library to build a Python object around the pointer, but then you need to make sure the lifetime of the C++ object being referenced by the pointer extends past the lifetime of all Python references to the object or your program will crash.

### How can I check returning Python value for None? 

        object result = call_method<object>( <whatever> );
        if (result.ptr() == object().ptr())
        {
            // handle None case
        }
        else
        {
            X x = extract<X>(result);
            ...
        }

\-- Or better?

    object result = ...
    result.ptr() == Py_None

\-- Or even better?

    object result = ...
    if(!result.is_none()) {
       ...
    }

Python C/Api Reference Manual says:

[PyObject](./PyObject.html)\* Py_None \... Since None is a singleton, testing for object identity (using \"==\" in C) is sufficient. \...

### Why operators.hpp imports certain functions (such as \'str\') into the global namespace, instead of the namespace boost::python. That looks like an error\... 

It\'s only on broken compilers which don\'t support [KoenigLookup](./KoenigLookup.html), and it\'s intentional. The negative impact should be limited due to the fact that these functions only operate on objects of type boost::python::self_ns::self_t. Do you anticipate a real problem with this?

### My program crashes. What I can do? 

Incidentally, if you are on Windows and want to see what\'s really happening with the crash, #include \"\$BOOST_ROOT/libs/python/test/module_tail.cpp\" at the end of your source file.

This will cause (JIT) debugging to be invoked at the point of the crash, instead of translating it into a C++ exception. It might be useful to inspect \*this at the point of the crash (if the crash does in fact happen at the same place you\'re seeing the exception above).

------------------------------------------------------------------------

[CategoryFaq](CategoryFaq)
