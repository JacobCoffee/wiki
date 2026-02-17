# boost.python/HowTo

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

## How to expose\... 

### static class data members 

    object x_class
        = class_<X>("X")
             .def( ... )
             ...
             ;

    x_class.attr("fu") = X::fu;
    x_class.attr("bar") = X::bar;
    ...

Since version 1.30 you can use class\_ method:

       .add_static_property("name", &fget [,&fset])

### static class functions 

It\'s likely to be in 1.30 release.

Meanwhile you should do something which mirrors pure Python:

    class foo(object):
        def f(x,y):
            return x*y
        f = staticmethod(f)

So in C++, it would be something like:

        class_<foo>("foo")
            .def("f", &foo::f)
            .staticmethod("f")  // **
            ;

In version 1.33 staticmethod is already implemented, just use the same syntax as above.

Where the marked line would be implemented something like this:

    self& staticmethod(char const* name)
    {
        dict d(handle<>(borrowed(downcast<PyTypeObject>(this->ptr())->tp_dict)));
        object method = (object)(d[name]);
        this->attr(name) = object(handle<>(
             PyStaticMethod_New( callable_check(method.ptr()) )
          ));
        return *this;
    }

To create overloaded staticmethods in python, you overload first, then you make it static.

If you want to expose a static function that returns a pointer to an already exposed C++ type, you have to specify a return policy. This is because python needs to know what to do with that pointer and how to track it after it is returned. The return policy specified what to do with the pointer, such as whether or not to free the memory after exiting. Like so:

        class_<foo>("foo")
            .def("f", &foo::f, return_value_policy<manage_new_object>())
            .staticmethod("f")  // **
            ;

This has told python that a pointer returned from foo:f() must be managed as a new object and is to be deleted when out of scope or at exit. There are more return policies. Return policies are all subtypes of [ResultConverterGenerator](./ResultConverterGenerator.html), check it out in the docs.

### module level objects 

#### at module creation time 

First, create those objects like

    object class_X = class_<X>("X");
    object x = class_X();

Second, expose them:

    scope().attr("x") = x; // injects x into current scope

By default current scope is module.

#### at run-time 

Use a function:

    template <class T>
    void set(const std::string& name, const T& value) {
      interpreter()->mainmodule()[name] = value;
    }

Note:: *interpreter()* is going to be added.

### mutable C++ object 

Perhaps you\'d like the resulting Python object to contain a raw pointer to the argument? In that case, the caveat is that if the lifetime of the C++ object ends before that of the Python object, that pointer will dangle and using the Python object may cause a crash.

Here\'s how to expose mutable C++ object during module initialisation:

      scope().attr("a") = object(ptr(&class_instance));

### std::C++ container 

You can always wrap the container with class\_ directive. For example for std::map:

    template<class Key, class Val>
    struct map_item
    {
        typedef std::map<Key,Val> Map;

        static Val& get(Map const& self, const Key idx) {
          if( self.find(idx) != self.end() ) return self[idx];
          PyErr_SetString(PyExc_KeyError,"Map key not found");
          throw_error_already_set();
        }

        static void set(Map& self, const Key idx, const Val val) { self[idx]=val; }

        static void del(Map& self, const Key n) { self.erase(n); }

        static bool in(Map const& self, const Key n) { return self.find(n) != self.end(); }

        static list keys(Map const& self)
        {
            list t;
            for(Map::const_iterator it=self.begin(); it!=self.end(); ++it)
                t.append(it->first);
            return t;
        }
        static list values(Map const& self)
        {
            list t;
            for(Map::const_iterator it=self.begin(); it!=self.end(); ++it)
                t.append(it->second);
            return t;
        }
        static list items(Map const& self)
        {
            list t;
            for(Map::const_iterator it=self.begin(); it!=self.end(); ++it)
                t.append( make_tuple(it->first, it->second) );
            return t;
        }
    }

    using namespace boost::python;
    typedef std::map<Key,Val> Map;
    class_<Map>("Map")
      .def("__len__", &Map::size)
      .def("__getitem__", &map_item<Key,Val>().get, return_value_policy<copy_non_const_reference>() )
      .def("__setitem__", &map_item<Key,Val>().set)
      .def("__delitem__", &map_item<Key,Val>().del)
      .def("clear", &Map::clear)
      .def("__contains__", &map_item<Key,Val>().in)
      .def("has_key", &map_item<Key,Val>().in)
      .def("keys", &map_item<Key,Val>().keys)
      .def("values", &map_item<Key,Val>().values)
      .def("items", &map_item<Key,Val>().items)
      ;

To compile, you might need to add \'typename\' before Map::const_iterator.

### \"Raw\" function 

*I want to write in python:*

        def function( *args ):
            # Mess arount with elements of args.

#### Method 1 (old way) 

You can make one with the library\'s implementation details. Be warned that these interfaces may change, but hopefully we\'ll have an \"official\" interface for what you want to do by then.

    python::objects::function_object(
        f                       // must be py_function compatible
        , 0, std::numeric_limits<unsigned>::max()  // arity range
        , python::detail::keyword_range());        // no keywords

will create a Python callable object.

**f** is any function pointer, function reference, or function object which can be invoked with two [PyObject](./PyObject.html)\* arguments and returns something convertible to a [PyObject](./PyObject.html)\*.

You can add this to your module namespace with:

    scope().attr("name") = function_object(f, ... );

Now you can also

    class_<foo>("foo")
        .def("bar",function_object(f, ... ) );

as well, but ***not***

    function_object bar(f, ... );
    ...
    class_<foo>("foo")
        .def("bar",bar);

because function_object is a function, not a class.

#### Method 2 (new way) 

There\'s a poorly documented function called **raw_function** in boost::python that makes defining the functions with arbitrary arguments much easier. Another advantage of this method is that this is not using any functionality from the **details** namespace, so this should be more stable.

This is our goal:

:::: 
::: 
``` 
   1 def function(*args, **kwargs):
   2         # do stuff here
```
:::
::::

To accomplish this from C++, we must wrap our functionality into a function with the following signature:

:::: 
::: 
``` 
   1 object bar(tuple args, dict kwargs)
   2 {
   3         // do stuff here
   4 }
```
:::
::::

Then we can use **raw_function** to add it to our class:

:::: 
::: 
``` 
   1 class_<foo>("foo")
   2     .def("bar", raw_function(bar, 1) );
```
:::
::::

**raw_function** takes two parameters - the function pointer and the minimum number of arguments.

### \"Raw\" constructor 

What if you wanted to make a constructor that takes in an arbitrary number of arguments and/or an arbitrary number keyword arguments?

:::: 
::: 
``` 
   1 class foo:
   2         def __init__(*args, **kwargs):
   3                 # do stuff here
```
:::
::::

It turns out that boost::python can do **raw_function**, and it can do **make_constructor**, but how to combine these two to get a **raw constructor** is not obvious. We describe two methods. Method 1 uses only the public API, which makes it reliable, but the code is a bit hack-ish. Method 2 leads to straight-forward client code, but requires one to write a custom header that uses internal implementation details of boost::python to get the desired effect.

#### Method 1 (official) 

This is how the boost::python unit tests implement a raw constructor, see [test/raw_ctor.cpp](https://github.com/boostorg/python/blob/master/test/raw_ctor.cpp). A documented example:

:::: 
::: 
``` 
   1 #include <boost/python.hpp>
   2 #include <boost/python/make_constructor.hpp>
   3 #include <boost/python/raw_function.hpp>
   4 using namespace boost::python;
   5 
   6 class A {
   7 public:
   8   int number_;
   9 
  10   A(int n)
  11     : number_(n)
  12   {}
  13 };
  14 
  15 // raw constructor
  16 object
  17 A_init(tuple args, dict kwargs) {
  18   // strip off self
  19   object self = args[0];
  20   args = tuple(args.slice(1,_));
  21 
  22   // call appropriate C++ constructor
  23   // depending on raw arguments, these
  24   // C++ constructors must be exposed to
  25   // Python through .def(init<...>())
  26   // declarations
  27   if (len(args) > 0) {
  28     const int n = extract<int>(args[0]);
  29     return self.attr("__init__")(n);
  30   }
  31   if (kwargs.contains("n")) {
  32     const int n = extract<int>(kwargs["n"]);
  33     return self.attr("__init__")(n);
  34   }
  35   return self.attr("__init__")(0);
  36 }
  37 
  38 BOOST_PYTHON_MODULE(raw_ctor) {
  39   // using no_init postpones defining __init__ function until after
  40   // raw_function for proper overload resolution order, since later
  41   // defs get higher priority.
  42   class_<A>("A", no_init)
  43     .def("__init__", raw_function(A_init), "raw ctor")
  44     .def(init<int>()) // C++ constructor, shadowed by raw ctor
  45     .def_readwrite("number", &A::number_)
  46   }
```
:::
::::

#### Method 2 

The technique for making a **raw_constructor** described here was devised by Hans Meine and and originally posted here: [http://article.gmane.org/gmane.comp.python.c++/8881/match=raw+constructor](http://article.gmane.org/gmane.comp.python.c++/8881/match=raw+constructor)

In order to implement the **raw_constructor**, we use some internal implementation details of boost::python. This code was tested with boost 1.42 built on Visual Studio 2008.

**raw_constructor.hpp**

:::: 
::: 
``` 
   1 #ifndef RAW_CONSTRUCTOR_HPP
   2 #define RAW_CONSTRUCTOR_HPP
   3 
   4 #include "boost/python.hpp"
   5 #include "boost/python/detail/api_placeholder.hpp"
   6 
   7 namespace boost { namespace python {
   8 
   9 namespace detail {
  10 
  11   template <class F>
  12   struct raw_constructor_dispatcher
  13   {
  14       raw_constructor_dispatcher(F f)
  15      : f(make_constructor(f)) {}
  16 
  17       PyObject* operator()(PyObject* args, PyObject* keywords)
  18       {
  19           borrowed_reference_t* ra = borrowed_reference(args);
  20           object a(ra);
  21           return incref(
  22               object(
  23                   f(
  24                       object(a[0])
  25                     , object(a.slice(1, len(a)))
  26                     , keywords ? dict(borrowed_reference(keywords)) : dict()
  27                   )
  28               ).ptr()
  29           );
  30       }
  31 
  32    private:
  33       object f;
  34   };
  35 
  36 } // namespace detail
  37 
  38 template <class F>
  39 object raw_constructor(F f, std::size_t min_args = 0)
  40 {
  41     return detail::make_raw_function(
  42         objects::py_function(
  43             detail::raw_constructor_dispatcher<F>(f)
  44           , mpl::vector2<void, object>()
  45           , min_args+1
  46           , (std::numeric_limits<unsigned>::max)()
  47         )
  48     );
  49 }
  50 
  51 }} // namespace boost::python
  52 
  53 #endif // RAW_CONSTRUCTOR_HPP
  54 
```
:::
::::

This is the \"raw python\" factory method signature for our class:

:::: 
::: 
``` 
   1 class Foo {
   2         static shared_ptr<Foo> create_raw(tuple args, dict kwargs)
   3         {
   4                 // do stuff here
   5         }
   6         // ....
   7 };
```
:::
::::

and this is the wrapper:

:::: 
::: 
``` 
   1 class_<Foo, noncopyable, shared_ptr<Operator> > ("Foo", no_init)
   2         .def("__init__", raw_constructor(&Foo::create_raw, 2));
```
:::
::::

**raw_constructor** takes the same parameters as **raw_function**, but it only works for wrapping the **[init]\_** method.

### getter and setter methods as a property 

Suppose you have class \"C\" with methods \"getA\" and \"setA\" and you want to expose them as a property \"a\". Then

    .add_property("a", &C::getA, &C::setA)

will work unless you need to assign a [CallPolicy](./boost(2e)python(2f)CallPolicy.html) to them. In that case use \"make_function\":

    .add_property("a",
          make_function(&C::getA, return_value_policy<...>()),
          make_function(&C::setA, with_custodian_and_ward<...>())
    )

### named constructors / factories (as Python initializers) 

There is a poorly documented make_constructor() function for this purpose. (The best available documentation seems to be in libs/python/test/injected.cpp of the boost source tree.)

It may be used like this:

    static boost::shared_ptr<MyClass> makeClass(const object& data)
    {
      long val = extract<long>(data);
      return boost::shared_ptr<MyClass>(new MyClass(val));
    }

    class_<MyClass, boost::shared_ptr<MyClass> >("MyClass")
        .def("__init__", make_constructor(makeClass))

or simply like this:

    static boost::shared_ptr<MyClass> makeClass(long val)
    {
      return boost::shared_ptr<MyClass>(new MyClass(val));
    }

    class_<MyClass, boost::shared_ptr<MyClass> >("MyClass")
        .def("__init__", make_constructor(makeClass))

### boost.function objects 

There are times when you want to have the fast callbacks of C++ in boost.function objects to be used both from C++ and python, and also have them to access both C++ and Python code. I have been using this file [py_boost_function.hpp](attachments/boost(2e)python(2f)HowTo/py_boost_function.hpp) in a regular basis, but of course it admits a lot of improvement. Be aware that this header uses boost.function_types; a library which currently is not in the main boost distribution.

Usage example:

For the boost.python C++ module:

         ...
         #include <boost/python.hpp>
         ...
         #include "py_boost_function.hpp"
         ...

         void module_greeter_f(string const& origin)
         {
               cout << "Hello world, by " << origin << endl;
         }


         boost::function< void( string const& ) > module_greeter(
              module_greeter_f
         ) ;
         ...

         BOOST_PYTHON_MODULE( foo ) {

              using namespace boost::python;
              ...

              def_function< void(string const&) >(
                  "greeter_function_t",
                  "A greeting function"
              );

              ...
              scope().attr("module_greeter") = module_greeter;
         }

From python code:

\- Invoke:

              >>> import foo
              >>> foo.module_greeter("world")

\- Create instances from python:

              >>> def my_greetings(hi):
              >>> ... print hi, ", world"
              >>> ...
              >>> grfunc = foo.greeter_function_t.from_callable( my_greetings )

### a package within a single extension module 

See [Packages in Python extension modules](http://isolation-nation.blogspot.com/2008/09/packages-in-python-extension-modules.html).

## How to get\... 

### C++ object from Python 

If you have a reference, use `handle`{.backtick}:

    handle<> x(whatever);   // new reference
    handle<> x(borrowed(whatever));  // borrowed reference

    object(x); // now we have an object.

Than you can try to `extract`{.backtick} a value:

    Type v = extract<Type>(x);

Or from the start. Suppouse you wrap your class T as:

    object Tclass = class_<T>("T")/* defs, etc. */;

Then you can create such object by

    object pyt = Tclass(/* constructor args*/);

and get the underlying T this way:

    T& t = extract<T&>(pyt);

See [../extract](./boost(2e)python(2f)extract.html)

### SWIG exposed C++ object from Python 

This is how SWIG encapsulates Pointers in Python

    struct PySwigObject {
        PyObject_HEAD
        void * ptr;
        const char * desc;
    };

We use this function to extract the Pointer from the Python object

    void* extract_swig_wrapped_pointer(PyObject* obj)
    {
        char thisStr[] = "this";
        //first we need to get the this attribute from the Python Object
        if (!PyObject_HasAttrString(obj, thisStr))
            return NULL;

        PyObject* thisAttr = PyObject_GetAttrString(obj, thisStr);
        if (thisAttr == NULL)
            return NULL;
        //This Python Object is a SWIG Wrapper and contains our pointer
        void* pointer = ((PySwigObject*)thisAttr)->ptr;
        Py_DECREF(thisAttr);
        return pointer;
    }

This call ensures that for objects of type SWIGClass our converter function will be used.

    boost::python::converter::registry::insert(&extract_swig_wrapped_pointer, type_id<SWIGExposedClass>());

We can then have a normal exposed function take our SWIGExposedClass

    void foo(SWIGExposedClass* x)
    

### Multithreading Support for my function 

One approach to safely unblock Python threads is to write a thin wrapper around your function which uses Py_BEGIN_ALLOW_THREADS and Py_END_ALLOW_THREADS around a call to the real function.

A better approach is to use a class that releases the GIL in the constructor and re-acquires it in the destructor, using the common C++ idiom \"Resource Acquisition Is Initialization\" ([http://en.wikibooks.org/wiki/More_C%2B%2B_Idioms/Resource_Acquisition_Is_Initialization](http://en.wikibooks.org/wiki/More_C++_Idioms/Resource_Acquisition_Is_Initialization)):

    class ScopedGILRelease
    {
    // C & D -------------------------------------------------------------------------------------------
    public:
        inline ScopedGILRelease()
        {
            m_thread_state = PyEval_SaveThread();
        }

        inline ~ScopedGILRelease()
        {
            PyEval_RestoreThread(m_thread_state);
            m_thread_state = NULL;
        }

    private:
        PyThreadState * m_thread_state;
    };

This will ensure that the GIL is re-acquired even if an exception occurs. Sample code:

    int foo_wrapper(int x)
    {
        ScopedGILRelease scoped;
        return foo(x);
    }

### ownership of C++ object 

Wrap object with auto_ptr\<\> storage:

    class_<Myclass, auto_ptr<MyClass> >("MyClass");

Write a small helper function to call the function which wants to take ownership of [MyClass](./MyClass.html) object:

    void caller(auto_ptr<MyClass> obj)
    {
      new_owner_function(obj.get());
      obj.release();
    }

Wrap `caller` under the `new_owner_function` Python name.

See also [http://www.boost.org/libs/python/doc/v2/faq.html#ownership](http://www.boost.org/libs/python/doc/v2/faq.html#ownership)

### ownership of C++ object extended in Python 

The method defined upper does not work if part of your object is written in Python. The PyObject\* associated to the object may still be delete by Python. If you want to ensure the lifetime of the object, you have to increase manually the reference couting in the C++ Wrapper *and* use the above method. With this, you\'ll be sure the PyObject\* is not destroyed while the C++ still exists.

So, write the MyClassWrap as :

    class MyClassWrap : public MyClass
    {
      MyClassWrap( PyObject* self_) : self(self_) { PyINCREF(self); }
      MyClassWrap( PyObject* self_, const MyClass& copy ) : MyClass(copy), self(self_) { PyINCREF(self); }
      ~MyClassWrap() { PyDECREF(self); }
      ...
      PyObject *self;
    };

And in the module definition :

    class_<MyClass, auto_ptr<MyClassWrap> >("MyClass");
    implicitly_convertible<auto_ptr<MyClassWrap>, auto_ptr<MyClass> >();

And you still write the thin wrapper as described above.

### python object from derived C++ object 

The first, but incomplete, way to do this is to create an object with :

    void MyFct( MyClass* my_obj )
    {
      object obj(my_obj);
      python_fct(obj);
    }

The problem is, if the dynamic type of my_obj is not MyClass but a class derived from MyClass, you won\'t have, in Python, the interface of the derived class. If you want to create the object with the interface of the real dynamic type you have to use the ResultConverter created by Boost :

    void MyFct( MyClass* my_obj )
    {
      reference_existing_object::apply<MyClass*>::type converter;
      PyObject* obj = converter( my_obj );
      object real_obj = object( handle<>( obj ) );
      python_fct(real_obj);
    }

The python object must not be keep outside the execution of `python_fct`. If you do, then you have to take extra care about the lifetime of the Python object and the underlying C++ object for there are no lifetime guards possible (the original object being a C++ one, you have no automatic way to tie the lifetime of this object with the lifetime of the Python wrapper).

Now, if you can copy the object and use the copy instead of a reference, you can change the ResultConverter and use `return_by_value` instead of `reference_existing_object`.

### python object from extended C++ object 

We still want the previous behaviour, but now the C++ class may be extended in Python. We so have a class wrapper :

    class MyClassWrap : public MyClass
    {
    public:
      MyClassWrap(PyObject *self_, ...) : MyClass(...), self(self_) { ... }
      virtual bool virtual_method() { return call_method<bool>(self, "virtual_method"); }
      ...
      PyObject *self;
      ...
    };

Let\'s say you have a C++ method, calling Python with the object. If you create the function as :

    bool my_fct(MyClass* my_obj)
    {
      bool result = extract<bool>( python_function(my_obj) );
    }

Boost will create a new MyClass wrapper and you won\'t have access to the Python methods. To access the Python object you have to explicitly send the Python wrapper boost gave you at the object creation :

    bool my_fct(MyClass* my_obj)
    {
      MyClassWrap *wrap_obj = dynamic_cast<MyClassWrap*>(my_obj);
      object final_obj;
      if( wrap_obj != NULL ) // Means we have a Python-defined object
        {
          final_obj = object(handle<>(borrowed(wrap_obj->self)));
        }
      else
        {
          final_obj = my_obj;
        }
      return extract<bool>( python_function(final_obj) );
    }

Of course, if you also have C++ classes derived from MyClass, you\'ll have to implement the function as :

    bool my_fct(MyClass* my_obj)
    {
      MyClassWrap *wrap_obj = dynamic_cast<MyClassWrap*>(my_obj);
      object final_obj;
      if( wrap_obj != NULL ) // Means we have a Python-defined object
        {
          final_obj = object(handle<>(borrowed(wrap_obj->self)));
        }
      else
        {
          reference_existing_object::apply<const Base*>::type converter;
          final_obj = object(handle<>(convert(my_obj)));
        }
      return extract<bool>( python_function(final_obj) );
    }

### access to a Python extension in the same app that embeds Python? 

Suppose you have an extension module \"hello\" with function \"greet\".

Module init function named \"inithello\" must be imported:

      PyImport_AppendInittab("hello", inithello);

before

      Py_Initialize();

and later:

      object strRes(handle<>(PyRun_String(
                    "from hello import *\n"
                    "result = greet()\n",
                    Py_file_input,
                    main_namespace.ptr(),
                    main_namespace.ptr()) ));

      const char* res = extract<const char*>(main_namespace["result"]);

It is worth noting that if your function is created by the macro BOOST_PYTHON_MODULE that it is named differently based on what version of python you are extending. For python 2 it is:

    inithello

For python 3 however it\'s:

    PyInit_hello

## How to make\... 

### Dynamic template to-python converters. 

Assume you want to create a wrapper that will quickly allow you to define a converter for an std::pair holding any two types. Create the following templated static structure.

    template<class T1, class T2>
    struct PairToTupleConverter {
      static PyObject* convert(const std::pair<T1, T2>& pair) {
        return incref(make_tuple(pair.first, pair.second).ptr());
      }
    };

If you have a look at the specifications for python object converters for the to_python_object template in the boost::python documentation, you will notice that the above satisfies the requirements of being an object with a static function convert() that accepts the type-to-be-converted and returns a python object pointer([PyObject](./PyObject.html)\*). This is reusable for an std::pair holding any two types like so:

      to_python_converter<std::pair<int, int>, PairToTupleConverter<int, int> >();

Such a statement would be present in your exports (BOOST_PYTHON_MODULE() definition) for any std::pair you wish to export to python as a result of function return values; of course, the above example is for a pair of *int*s. Another thing one will notice is that these may be used recursively. If we first register a to_python_converter for a pair of *int*s, then we can later register a pair of int-pairs like so:

      typedef std::pair<int, int> IntPair;
      // This is our previous registration function (as above) using the cleaner typedef.
      to_python_converter<IntPair, PairToTupleConverter<int, int> >();
      // Registers a converter for a pair of int-pairs.
      to_python_converter<std::pair<IntPair, IntPair>, PairToTupleConverter<IntPair, IntPair> >();

The second registration function call (actually an instantiation) will delve recursively into the to_python_converter registry to find our previous registration of a converter for *int*-pairs. The lifetime of the object depends on the return_value_policy that you apply to the export of the function which returns one of these manually registered convertible types. A similar thing can be done for containers; std::vector to boost::python::tuple, std::vector to boost::python::list, std::map to boost::python::dict.

## Howto debug your extensions.. 

### \[NOTE\] Problems using MS Visual C++ Debugger 

If you want to debug your extensions using the MS Visual C++ debugger you need to remember to compile all libraries and extensions with the **/MDd** flag.

If you forget this compiler flag, it\'s likely that your debugger will halt on a breakpoint with an error something like this:

`HEAP[python.exe]: Invalid Address specified to RtlValidateHeap( 00E30000, 00D48FA8 )`

The actual statement which halts your debugger is executed in the NTDLL and therefor is not debuggable. While this seems to apply to all of the boost libraries, it can be annoying and it\'s hard to actually find the problem.

As far as I know, the actual problem is, if you\'ve not compiled all your libs/extensions with */MDd*, that you have objects on different heaps and the debugger stops with an assert because the extensions tries to access objects from the wrong heap.
