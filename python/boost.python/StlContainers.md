# boost.python/StlContainers

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

It\'s a pity that BPL doesn\'t wrap STL containers out of the box. It would be good to have \"batteries included\". But to be fair, a fully featured container wrapper is a lot of code and will take very long to compile. It is a major research project to develop \"a best\" fully featured container wrapper. Note that what you want depends on the element type (e.g. what makes sense for std::complex\<\> as an element type does not necessarily make sense for double, what makes sense for double might not make sense for int and vice versa, etc. etc.)! I cannot even imagine what a comprehensive solution for std::map\<\> could look like since it will have to deal with combinations of two types. To see an example of a more-or-less fully featured multi-dimensional array wrapper look at [flex_wrapper.h](http://cci.lbl.gov/cctbx_sources/scitbx/array_family/boost_python/flex_wrapper.h)

### C++ classes 

In our case we have vector and map to wrap and had to decide how to wrap them.

            using namespace std;
            class Shape;
            typedef vector<Shape> Geometry;
            typedef map<string,Geometry> Layer;

We have two choices:

a.  wrap them with *class\_\<\>* ourself or

b.  write *to_python_converter()* and some wrappers to *extract\<data\>* from python.

Our goal is to get to the working prototype as soon as we can. So in simplistic (a) approach

            using namespace boost::python;
            class_<Shape>("Shape");
            class_<Geometry>("Geometry");
            class_<Layer>("Layer");

We\'ll have our containers exposed but without any working machinery inside them. Approach (b)

            class vector_adapter

seems to be easiest to get the C++ containers exposed as Python containers

but doesn\'t work (for me :)).

So we have to revert to approach (a) and write a wrapper to add Python container machinery to the exposed classes.

### list

To pretend a Python **list** a class shall have methods:

- [len],

- [getitem] to be readable,

- [setitem] to be writable,

- [delitem] to delete elements.

We have [len] right away:

              .def("__len__", &Geometry::size)

but for others let\'s have a helper class:

    template<class T>
    struct std_item
    {
        typedef typename T::value_type V;
        static V& get(T const& x, int i)
        {
            if( i<0 ) i+=x.size();
            if( i>=0 && i<x.size() ) return x[i];
            IndexError();
        }
        static void set(T const& x, int i, V const& v)
        {
            if( i<0 ) i+=x.size();
            if( i>=0 && i<x.size() ) x[i]=v;
            else IndexError();
        }
        static void del(T const& x, int i)
        {
            if( i<0 ) i+=x.size();
            if( i>=0 && i<x.size() ) x.erase(i);
            else IndexError();
        }
        static void add(T const& x, V const& v)
        {
            x.push_back(v);
        }
    };
    void IndexError() { PyErr_SetString(PyExc_IndexError, "Index out of range"); }

which allows us to have nice pythonic negative indexes and easy to read *def*initions.

Then in BOOST_PYTHON_MODULE we use it:

    class_<Geometry>("Geometry");
      .def("__len__", &Geometry::size)
      .def("clear", &Geometry::clear)
      .def("append", &std_item<Geometry>::add,
            with_custodian_and_ward<1,2>()) // to let container keep value
      .def("__getitem__", &std_item<Geometry>::get,
            return_value_policy<copy_non_const_reference>())
      .def("__setitem__", &std_item<Geometry>::set,
            with_custodian_and_ward<1,2>()) // to let container keep value
      .def("__delitem__", &std_item<Geometry>::del)
      ;

### map

And the same approach for **map**.

    template<class T>
    struct map_item
    {
        typedef typename T::key_type K;
        typedef typename T::mapped_type V;
        static V& get(T const& x, K const& i)
        {
            if( x.find(i) != x.end() ) return x[i];
            KeyError();
        }
        static void set(T const& x, K const& i, V const& v)
        {
            x[i]=v; // use map autocreation feature
        }
        static void del(T const& x, K const& i)
        {
            if( x.find(i) != x.end() ) x.erase(i);
            else KeyError();
        }
    };
    void KeyError() { PyErr_SetString(PyExc_KeyError, "Key not found"); }

And in our case:

    class_<Layer>("Layer");
      .def("__len__", &Layer::size)
      .def("clear", &Layer::clear)
      .def("__getitem__", &map_item<Layer>::get,
            return_value_policy<copy_non_const_reference>())
      .def("__setitem__", &map_item<Layer>::set,
            with_custodian_and_ward<1,2>()) // to let container keep value
      .def("__delitem__", &map_item<Layer>::del)
      ;

But it\'s only very basic functionality. Let\'s add some convinience.

### key in container 

To use python construct `key in container` we need to implement `__contains__`{.backtick}:

- for vector (list, queue)

      static bool in(T const& x, V const& v)
      {
              return find_eq(x.begin, x.end, v) != x.end();
      }

- for map

      static bool in(T const& x, K const& i)
      {
              return x.find(i) != x.end();
      }

### iterators

Also very useful thing is to iterate through our containers.\
For the vector [boost.python](./boost(2e)python.html) has it:

    .def("__iter__", iterator<Geomery>())

And for map it needs some help

    static list keys(T const& x)
    {
            list t;
            for(T::const_iterator it=x.begin; it!=x.end(); ++it)
              t.append(it->first);
            return t;
    }
    static list values(T const& x)
    {
            list t;
            for(T::const_iterator it=x.begin; it!=x.end(); ++it)
              t.append(it->second);
            return t;
    }
    static list items(T const& x)
    {
            list t;
            for(T::const_iterator it=x.begin; it!=x.end(); ++it)
              t.append(make_tuple(it->first,it->second));
            return t;
    }

Here we used simplistic approach for the map. We didn\'t use iterator protocol, but construct appropriate lists ourselfs.

### index

Some ice on top:

    static int std_item::index(T const& x, V const& v)
    {
            int i=0;
            for(typename T::const_iterator it=x.begin; it!=x.end(); ++it,++i)
              if( *it == v ) return i;
            return -1;
    }

    static int map_item::index(T const& x, K const& k)
    {
            int i=0;
            for(typename T::const_iterator it=x.begin; it!=x.end(); ++it,++i)
              if( it->first == k ) return i;
            return -1;
    }

and we are all set.

### download

You can download container helper classes from [container.h](attachments/boost(2e)python(2f)StlContainers/container.h). \<- The file is **EMPTY**!!!
