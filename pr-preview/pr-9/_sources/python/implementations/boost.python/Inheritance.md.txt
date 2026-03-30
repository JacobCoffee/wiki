# boost.python/Inheritance

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

## Inheritance in Python 

Boost.Python extension classes support single and multiple-inheritance in Python, just like regular Python classes. You can arbitrarily mix built-in Python classes with extension classes in a derived class\' tuple of bases. Whenever a Boost.Python extension class is among the bases for a new class in Python, the result is an extension class:

    >>> class MyPythonClass:
    ...     def f(): return 'MyPythonClass.f()'
    ...
    >>> import my_extension_module
    >>> class Derived(my_extension_module.MyExtensionClass, MyPythonClass):
    ...     '''This is an extension class'''
    ...     pass
    ...
    >>> x = Derived()
    >>> x.f()
    'MyPythonClass.f()'
    >>> x.g()
    'MyExtensionClass.g()'

## Reflecting C++ Inheritance Relationships 

Boost.Python also allows us to represent C++ inheritance relationships so that wrapped derived classes may be passed where values, pointers, or references to a base class are expected as arguments. The declare_base member function of class_builder\<\> is used to establish the relationship between base and derived classes:

    #include <memory> // for std::auto_ptr<>

    struct Base {
        virtual ~Base() {}
        virtual const char* name() const { return "Base"; }
    };

    struct Derived : Base {
        Derived() : x(-1) {}
        virtual const char* name() const { return "Derived"; }
        int x;
    };

    std::auto_ptr<Base> derived_as_base() {
        return std::auto_ptr<Base>(new Derived);
    }

    const char* get_name(const Base& b) {
        return b.name();
    }

    int get_derived_x(const Derived& d) {
        return d.x;
    }
    --------------------------------------------------------------------------------
    #include <boost/python.hpp>

    using namespace boost::python;

    BOOST_PYTHON_MODULE(my_module)
    {
        class_<Base>("Base", no_init);          
                                                                                  
        class_<Derived, bases<Base> >("Derived", no_init); 
                                                                                  
        def("derived_as_base", derived_as_base);                        
        def("get_name", get_name);                                      
        def("get_derived_x", get_derived_x); 
    }

Then, in Python:

    >>> from my_module import *
    >>> base = Base()
    >>> derived = Derived()
    >>> get_name(base)
    'Base'

objects of wrapped class Derived may be passed where Base is expected

    >>> get_name(derived) 
    'Derived'

objects of wrapped class Derived can be passed where Derived is expected but where type information has been lost.

    >>> get_derived_x(derived_as_base()) 
    -1
