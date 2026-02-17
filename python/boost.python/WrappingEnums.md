# boost.python/WrappingEnums

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

For example, let\'s define an object in module namespace to represent **enum**:

    #include <boost/python.hpp>

    using namespace boost::python;

    enum color { red = 1, green = 2, blue = 4 };

    color identity_(color x) { return x; }

    BOOST_PYTHON_MODULE(enum_ext)
    {
        enum_<color>("color")
            .value("red", red)
            .value("green", green)
            .value("blue", blue)
            ;
        
        def("identity", identity_);
    }

The usage is follows:

    >>> from enum_ext import *

    >>> identity(color.red)
    enum_ext.color.red

    >>> identity(color.green)
    enum_ext.color.green

    >>> identity(color.blue)
    enum_ext.color.blue

    >>> identity(color(1))
    enum_ext.color.red

    >>> identity(color(2))
    enum_ext.color.green

    >>> identity(color(3))
    enum_ext.color(3)

    >>> identity(color(4))
    enum_ext.color.blue

    >>> try: identity(1)
    ... except TypeError: pass
    ... else: print 'expected a TypeError'
