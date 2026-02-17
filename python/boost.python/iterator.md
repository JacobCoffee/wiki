# boost.python/iterator

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

### C++ Iterators 

Python iterator support a highly flexible interface allowing:

- Direct exposure of a class\' begin() and end() functions:

<!-- -->

        ...
        .def("__iter__", iterator<list_int>())

- Creation of iterators from member functions\...

<!-- -->

        ...
        .def("__iter__"
             , range(&my_class::x_begin, &my_class::x_end))

- \...and member data:

<!-- -->

        ...
        .def("__iter__"
             , range(&std::pair<char*,char*>::first, &std::pair<char*,char*>::second))

- The ability to specify [boost.python/CallPolicy](./boost(2e)python(2f)CallPolicy.html), e.g. to prevent copying of heavyweight values:

<!-- -->

        ...
        .def("__iter__"
             , range<return_value_policy<copy_non_const_reference> >(
                   &my_sequence<heavy>::begin
                 , &my_sequence<heavy>::end))

### Custom Iterators 

Suppose we have custom iterator class providing next() member function. To expose it let\'s take an approach from scitbx package:

    inline object pass_through(object const& o) { return o; }

    template<class Klass, class KlassIter>
    struct iterator_wrappers
      {
        static Klass
        next(KlassIter& o)
        {
          Klass* result = o.next();
          if (!result) {
            PyErr_SetString(PyExc_StopIteration, "No more data.");
            boost::python::throw_error_already_set();
          }
          return *result;
        }

        static void
        wrap(const char* python_name)
        {
          //using namespace boost::python;
          class_<KlassIter>(python_name, no_init)
            .def("next", next)
            .def("__iter__", pass_through)
          ;
        }
      };

    BOOST_PYTHON_MODULE(iter)
    {
      ...
      iterator_wrappers<const MyClass,MyIter>().wrap("Iterator");
    }
