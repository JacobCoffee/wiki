# boost.python/CallPolicy

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

`CallPolicy`{.backtick} allows [boost.python]() to deal with raw references and pointers. Different policies specifies different strategies of managing object ownership.

## with_custodian_and_ward\<M,N\> 

Keeps N-th argument as long as M-th is alive.

Use of template parameters M,N:

- 1 - 1st argument (self for method calls)
- 2 - 2nd argument (1st for method calls)
- \...

For example, container operation *append* usualy uses `with_custodian_and_ward<1,2>` which means keep argument alive while container itself is alive.

## with_custodian_and_ward_postcall\<M,N\> 

ties lifetimes of the arguments and results

M,N same as before but also you can use 0 - result

## return_internal_reference

Builds a Python object around a pointer to the C++ result object (which must have a class\_\<\> wrapper somewhere), and applies some lifetime management to keep the \"self\" object alive as long as the Python result is alive. NULL pointer returning as None.

## return_value_policy\<T\> 

with T one of:

### reference_existing_object

naïve (dangerous) approach

[boost.python/ResultConverterGenerator](./boost(2e)python(2f)ResultConverterGenerator.html) which can be used to wrap C++ functions returning a reference or pointer to a C++ object.

When the wrapped function is called, the value referenced by its return value is not copied.\
A new Python object is created which contains an unowned U\* pointer to the referent of the wrapped function\'s return value, and no attempt is made to ensure that the lifetime of the referent is at least as long as that of the corresponding Python object.

This class is used in the implementation of return_internal_reference. Also NULL pointer returning as None.

### copy_non_const_reference

### copy_const_reference

[BoostPython](BoostPython) v1 approach

### manage_new_object

[BoostPython/ResultConverterGenerator](./BoostPython(2f)ResultConverterGenerator.html) which can be used to wrap C++ functions returning a pointer to an object allocated with a *new-expression* and expecting the caller to take responsibility for deleting that C++ object from heap. [boost.python]() will do it as part of Python object destruction.

Use case:

    T* factory() { return new T(); }

    class_<T>("T");

    def("Tfactory", factory, return_value_policy<manage_new_object>() );

### return_by_value

[boost.python/ResultConverterGenerator](./boost(2e)python(2f)ResultConverterGenerator.html) which can be used to wrap C++ functions returning any reference or value type.\
The return value is copied into a new Python object.
