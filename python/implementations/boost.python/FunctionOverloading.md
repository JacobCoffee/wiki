# boost.python/FunctionOverloading

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

From [http://www.boost.org/doc/libs/1_37_0/libs/python/doc/v2/overloads.html](http://www.boost.org/doc/libs/1_37_0/libs/python/doc/v2/overloads.html)

Few methods and functions have parameters by default.

To send this information to boost::python, you need to call theses instructions :

    BOOST_PYTHON_FUNCTION_OVERLOADS( overloadsname , functionname , arg_minimum, arg_maximum )
    BOOST_PYTHON_FUNCTION_OVERLOADS( overloadsname , classname::staticmethodname , arg_minimum, arg_maximum )

For global functions and for static methods.

    BOOST_PYTHON_MEMBER_FUNCTION_OVERLOADS( overloadsname , classname::methodname, arg_minimum, arg_maximum )

For class methods.

Sample :

    #include <boost/python/module.hpp>
    #include <boost/python/def.hpp>
    #include <boost/python/args.hpp>
    #include <boost/python/tuple.hpp>
    #include <boost/python/class.hpp>
    #include <boost/python/overloads.hpp>
    #include <boost/python/return_internal_reference.hpp>

    using namespace boost::python;

    tuple f(int x = 1, double y = 4.25, char const* z = "wow")
    {
        return make_tuple(x, y, z);
    }

    BOOST_PYTHON_FUNCTION_OVERLOADS(f_overloads, f, 0, 3)

    class X
    {
        X( const int& _loc)
        {
           localval=_loc;
        }
        int returnsame(int x=5)
        {
            return x+localval;
        }
        static int returnsum(int m,int x=10)
        {
            return m+x;
        }
        int localval;
    };

    BOOST_PYTHON_MEMBER_FUNCTION_OVERLOADS(X_returnsame_overloads, X::returnsame, 0, 1)
    BOOST_PYTHON_FUNCTION_OVERLOADS(X_returnsum_overloads, X::returnsum, 1, 2)


    BOOST_PYTHON_MODULE(args_ext)
    {
        def("f", f, 
            f_overloads(
                args("x", "y", "z"), "This is f's docstring"
            ));

        
        class_<X>("X", init<int>())
            .def("returnsame", &X::returnsame, 
                    X_returnsame_overloads(
                        args("x"), "returnsame's docstring"
                    )
            )
            .def("returnsum", &X::returnsum,
                    X_returnsum_overloads( args("x","m"), "returnsum's docstring"
                   )
            )
            .staticmethod("returnsum")
            ;
    }
