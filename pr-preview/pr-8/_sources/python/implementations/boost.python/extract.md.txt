# boost.python/extract

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

extractor interface which can be used to extract C++ types from Python objects.

From the [extract boost.python reference documentation](http://www.boost.org/doc/libs/1_48_0/libs/python/doc/v2/extract.html): \"Exposes a mechanism for extracting C++ object values from generalized Python objects. Note that extract\<\...\> can also be used to \"downcast\" an object to some specific ObjectWrapper. Because invoking a mutable python type with an argument of the same type (e.g. list(\[1,2\]) typically makes a copy of the argument object, this may be the only way to access the ObjectWrapper\'s interface on the original object.\"

We have discussed two main use cases for extractions

1\. In user code which needs to retrieve C++ objects from their corresponding Python objects:

a.  Simple example
    a.  Getting value:
        - void f(object x)
              {
                  int y = extract<int>(x); // retrieve an int from x
              }
    b.  Users may also want to explicitly check for convertibility:
        - int g(object x)
              {
                  extract<int> get_int(x);
                  if (get_int.check())
                      return get_int();
                  else
                      return 0;
              }
b.  Using extract to modify mutable objects in place
    - As cited from the Boost.Python reference documentation (see above) you need to use extract\<\> to apply the convenient boost::python::object & derived types interface to modify an existing (mutable) object (or PyObject\*), without making a copy:

          namespace bp = boost::python;

          // bp::object x;
          dict d = bp::extract<bp::dict>(x.attr("__dict__"));
          d["whatever"] = 3;          // modifies x.__dict__ !


          // PyObject* pyobj;
          PyObject* __dict__ = PyObject_GetAttrString(pyobj, const_cast<char*>("__dict__"));
          // (see also http://article.gmane.org/gmane.comp.python.c%2B%2B/15664)
          bp::dict dictobj = bp::extract<bp::dict>(__dict__);
          dictobj["whatever"] = 3;          // modifies pyobj __dict___!

      (see also [Boost.Python tutorial: Extracting C++ objects](http://www.boost.org/doc/libs/1_48_0/libs/python/doc/tutorial/doc/html/python/object.html#python.extracting_c___objects))

      Note: You could also fall back to using the Python C-API to modify `__dict__`:

          bp::object value(3);
          PyDict_SetItemString(__dict__, "whatever", value.ptr())
c.  Example for extracting elements out of more complex structures: In order to extract elements out of complex structures such as lists and tuples, we must nest extraction calls. The reason for this example is that it may not be immediately obvious to do this. Let\'s say you have a C++ class that contains a python-usable boost::python::list:
    - class A {
          public:
            boost::python::list list;
            void listOperation(list& l);
          };

      Then you expose the class to python as:

          class_<A>("A")
            .def_readwrite("b", &A::list)
            .def("op", &A::listOperation)
          ;

      It is completely reasonable for python script to do something like this:

          a = A()
          a.b = [(1,2),(3,4),(5,6)]
          a.op(a.b)

      In order for you to extract the elements of tuples within the list, we use the index operator of the list:

          void A::listOperation(list& l) {
             // Extract first element of first tuple in the list.
             extract<int>(extract<tuple>(list[0])())();
          }

2\. In the implementation of sequence from_python converters (e.g. Python tuple/list -\> std::vector)
