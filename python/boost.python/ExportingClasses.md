# boost.python/ExportingClasses

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

Now let\'s expose a C++ class to Python:

    #include <iostream>
    #include <string>

    namespace { // Avoid cluttering the global namespace.

      // A friendly class.
      class hello
      {
        public:
          hello(const std::string& country) { this->country = country; }
          std::string greet() const { return "Hello from " + country; }
        private:
          std::string country;
      };

      // A function taking a hello object as an argument.
      std::string invite(const hello& w) {
        return w.greet() + "! Please come soon!";
      }
    }

To expose the class, we use a *class\_* builder. Class member functions are exposed by using the *def()* member:

    #include <boost/python.hpp>
    using namespace boost::python;

    BOOST_PYTHON_MODULE(getting_started2)
    {
        // Create the Python type object for our extension class and define __init__ function.
        class_<hello>("hello", init<std::string>())
            .def("greet", &hello::greet)  // Add a regular member function.
            .def("invite", invite)  // Add invite() as a regular function to the module.
        ;

        def("invite", invite); // Even better, invite() can also be made a member of module!!!
    }

Now we can use the class normally from Python:

    >>> from getting_started2 import *
    >>> hi = hello('California')
    >>> hi.greet()
    'Hello from California'
    >>> invite(hi)
    'Hello from California! Please come soon!'
    >>> hi.invite()
    'Hello from California! Please come soon!'

Notes:

- We expose the class\' constructor by calling *def()* on the *class\_* builder with an argument whose type is *constructor\<params\>*, where *params* matches the list of constructor argument types;

- Regular member functions are defined by calling *def()* with a member function pointer and its Python name;

- Any function added to a class whose initial argument matches the class (or any base) will act like a member function in Python.

- To define a nested class, just place class\_\<\> builder inside another class `scope`{.backtick}:

      BOOST_PYTHON_MODULE(nested_ext)
      {
          using namespace boost::python;

          // Establish X as the current scope.
          scope x_class(
              class_<X>("X", init<int>())
                 .def(str(self))
              );

          // Y will now be defined in the current scope
          class_<Y>("Y", init<int>())
              .def(str(self))
              ;
      }

We can even make a subclass of hello.world:

    >>> class wordy(hello):
    ...     def greet(self):
    ...         return hello.greet(self) + ', where the weather is fine'
    ...
    >>> hi2 = wordy('Florida')
    >>> hi2.greet()
    'Hello from Florida, where the weather is fine'
    >>> invite(hi2)
    'Hello from Florida! Please come soon!'

Pretty cool! You can\'t do that with an ordinary Python extension type! Of course, you may now have a slightly empty feeling in the pit of your little pythonic stomach. Perhaps you wanted to see the following *wordy* invitation:

    'Hello from Florida, where the weather is fine! Please come soon!'

After all, *invite* calls *hello::greet()*, and you reimplemented that in your Python subclass, *wordy*. In [the next section](./boost(2e)python(2f)OverridableVirtualFunctions.html) we\'ll make *greet* virtual, and we\'ll see how to make C++ code see our overrides from Python.

It is important to note that boost::python will not allow you to make dynamic type casts (through polymorphism) if the function/method is considered \"unsafe\". That means that an appropriate method-wrapper will not be created for functions that execute potentially exception-generating code where exceptions do not have python mappings. Let\'s have a look at an example:

We make a base class we can derive from:

    class Base {
    public:
      boost::python::list list;
      virtual void x() = 0;
    };

And derive from that in the classic way, implementing the function x() in such a way that it uses unprotected boost::python::extract instances without catching potential exceptions:

    class Derive : public Base {
    public:
      virtual void x() {
        int y = boost::python::extract<int>(list[0])();
      }
    };

Exporting the classes like this:

    class BaseWrap : public Base, public wrapper<Base> {
    public:
      virtual void x() { this->get_override("x")(); }
    };

    class_<BaseWrap, boost::noncopyable>("Base")
      .def("x", boost::python::pure_virtual(&Base::x))
      ;

    class_<Derive, bases<Base> >("Derive");

Will generate the following error whenever you try to cast an instance of Derive to Base\*:

    TypeError: No registered converter was able to produce a C++ rvalue of type int from this Python object of type method-wrapper

What to do? Simply use try{}catch(){} blocks around any boost::python code that can produce an exception, such as the extract operation.
