# boost.python/PointersAndSmartPointers

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

## Pointers and smart pointers 

Since Python handles memory allocation and garbage collection automatically, the concept of a \"pointer\" is not meaningful in Python. However, many C++ APIs expose either raw pointers or shared pointers, to wrap these APIs we need to deal with pointers.

### Raw C++ Pointers 

The lifetime of C++ objects created by `new A` can be handled by Python\'s garbage collection by using the `manage_new_object` return policy:

    struct A {
        static A*   create () { return new A; }
        std::string hello  () { return "Hello, is there anybody in there?"; }
    };

    BOOST_PYTHON_MODULE(pointer)
    {
        class_<A>("A",no_init)
            .def("create",&A::create, return_value_policy<manage_new_object>())
            .staticmethod("create")
            .def("hello",&A::hello)
            ;
    }

A sample python program:

    from pointer import *
    an_A = A.create()
    print an_A.hello()

### Smart pointers 

The usage of smart pointers (e.g. `boost::shared_ptr<T>`) is another common way to give away ownership of objects in C++. These kinds of smart pointer are automatically handled if you declare their existence when declaring the class to boost::python. This is done by including the holding type as a template parameter to `class_<>`, like in the following example:

    #include <string>
    #include <boost/shared_ptr.hpp>
    #include <boost/python.hpp>

    using namespace boost;
    using namespace std;
    using namespace boost::python;

    struct A {
        static shared_ptr<A> create () { return shared_ptr<A>(new A); }
        std::string   hello  () { return "Just nod if you can hear me!"; }
    };

    BOOST_PYTHON_MODULE(shared_ptr)
    {
        class_<A, shared_ptr<A> >("A",init<>())
            .def("create",&A::create )
            .staticmethod("create")
            .def("hello",&A::hello)
        ;
    }

A sample python program:

    from shared_ptr import *
    an_A = A.create()
    print an_A.hello()

### Smart Pointer Example with OpenSceneGraph 

The Node.cpp file:

    #include <boost/python.hpp>
    #include <osg/ref_ptr>
    #include <osg/Node>

    using namespace boost::python;
    using namespace osg;

    // Tag the OpenSceneGraph ref_ptr type as a smart pointer.
    namespace boost {
      namespace python {
        template <class T> struct pointee< ref_ptr<T> >
        { typedef T type; };
      }}

    // Declare the actual type
    BOOST_PYTHON_MODULE(Node) {
      class_<Node, ref_ptr<Node> >("Node")
        ;
    }

This creates an opaque Node pointer. It can be extended to expose members of Node objects, or used as is to return opaque references to Node objects. For opaque references, the module must still be imported by the Python app. If Node.pyd is in a package directory, importing it in the `__init__.py` file in that directory seems to be a simple, workable solution.
