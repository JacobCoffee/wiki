# boost.python/PeekUnderTheHood

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

Dave Abrahams explains:

### What happens when you declare a class? 

         struct boring {};
         ...etc...
         class_<boring>("boring")
             ;

- A new (Python) subclass of Boost.Python.Instance (see libs/python/src/object/class.cpp) is created by invoking Boost.Python.class, the metatype:

                    >>> boring = Boost.Python.class(
                    ...     'boring'
                    ...   , bases_tuple       # in this case, just ()
                    ...   , {
                    ...         '_module_' : module_name
                    ...       , '_doc_' : doc_string # optional
                    ...     }
                    ... )

  - A handle to this object is stuck in the m_class_object field of the registration associated with typeid(boring). The registry will keep that object alive forever, even if you wipe out the \'boring\' attribute of the extension module (probably not a good thing).

    Because you didn\'t specify `class<boring, non_copyable, ...>`, a to-python converter for *boring* is registered which copies its argument into a value_holder held by the the Python *boring* object.

    Because you didn\'t specify `class<boring ...>(no_init)`, an `_init_`{.backtick} function object is added to the class dictionary which default-constructs a *boring* in a value_holder (because you didn\'t specify some smart pointer or derived wrapper class as a holder) held by the Python *boring* object. register_class_from_python is used to register a from-python

    converter for `shared_ptr<boring>`. boost::shared_ptrs are special among smart pointers because their *Deleter* argument can be made to manage the whole Python object, not just the C++ object it contains, no matter how the C++ object is held.

    If there were any `bases<>`, we\'d also be registering the relationship between these base classes and *boring* in the up/down cast graph (inheritance.\[hpp/cpp\]). In earlier versions of the code, we\'d be registering lvalue from-python converters for the class here, but now from-python conversion for wrapped classes is handled as a special case, before consulting the registry, if the source Python object\'s metaclass is the Boost.Python metaclass.

### brief overview of the data structures that are present in the registry 

The registry is simple: it\'s just a map from typeid -\> registration (see boost/python/converter/registrations.hpp). lvalue_chain and rvalue_chain are simple endogenous linked lists.

### overview of type conversions from c++ to python and back 

Big subject. I suggest some background reading: look for relevant info in the LLNL progress reports and the messages they link to. Also,

- [http://mail.python.org/pipermail/c++-sig/2002-May/001023.html](http://mail.python.org/pipermail/c++-sig/2002-May/001023.html)

- [http://mail.python.org/pipermail/c++-sig/2002-December/003115.html](http://mail.python.org/pipermail/c++-sig/2002-December/003115.html)

- [http://aspn.activestate.com/ASPN/Mail/Message/1280898](http://aspn.activestate.com/ASPN/Mail/Message/1280898)

- [http://mail.python.org/pipermail/c++-sig/2002-July/001755.html](http://mail.python.org/pipermail/c++-sig/2002-July/001755.html)

#### from c++ to python 

- It depends on the type and the call policies in use or, for

  call\<\>(\...), call_method\<\>(\...), or object(\...), if *ref* or *ptr* is used. There are also two basic categories to to-python conversion, \"return value\" conversion (for Python-\>C++ calls) and \"argument\" conversion (for C++-\>Python calls and explicit object() conversions). The behavior of these two categories differs subtly in various ways whose details I forget at the moment. You can probably find the answers in the above references, and certainly in the code. The \"default\" case is by-value (copying) conversion, which uses to_python_value as a to-python converter.

  - Since there can sensibly be only one way to convert any type to python (disregarding the idea of scoped registries for the moment), it makes sense that to-python conversions can be handled by specializing a template. If the type is one of the types handled by a built-in conversion (builtin_converters.hpp), the corresponding template specialization of to_python_value gets used. Otherwise, to_python_value uses the m_to_python function in the registration for the C++ type.

  Other conversions, like by-reference conversions, are only available for wrapped classes, and are requested explicitly by

  using ref(\...), ptr(\...), or by specifying different [../CallPolicy](CallPolicy) for a call, which can cause a different to-python converter to be used. These conversions are never registered anywhere, though they do need to use the registration to find the Python class corresponding to the C++ type being referred to. They just build a new Python instance and stick the appropriate *Holder* instance in it.

#### from python to C++ 

- Once again I think there is a distinction between \"return value\" and \"argument\" conversions, and I forget exactly what that is. What happens depends on whether an lvalue conversion is needed

  (see [http://mail.python.org/pipermail/c++-sig/2002-May/001023.html](http://mail.python.org/pipermail/c++-sig/2002-May/001023.html)) All lvalue conversions are also registered in a type\'s rvalue conversion chain, since when an rvalue will do, an lvalue is certainly good enough. An lvalue conversion can be done in one step (just get me the pointer to the object - it can be NULL if no conversion is possible) while an rvalue conversion requires two steps to support wrapped function overloading and multiple converters for a given C++ target type: first tell me if a conversion is possible, then construct the converted object as a second step.
