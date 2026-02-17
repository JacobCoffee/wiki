# boost.python/RuntimeErrors

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

[boost.python](./boost(2e)python.html) tries hard to provide best possible run-time errors. But often enough they need futher explanation. Some of them are mentioned below:

### TypeError: bad argument type for built-in operation 

Usualy means BPL couldn\'t find c++ method/function with appropriate signature. Very often that is wrong number of arguments, wrong argument(s) type and so on.

### TypeError: No to_python converter found for C++ type: \<type\> 

### TypeError: No to_python (by-value) converter found for C++ type: \<type\> 

BPL was unable to get C++ value from Python object.

For example, when calling ` extract<int>(<object>.attr("__len__")()) ` to get object length you omitted \"**()**\".

### RuntimeError: This class cannot be instantiated from Python 

Attempt to instantiate a class with *no_init* descriptor. It may be private constructor or abstract class.

### RuntimeError: unidentifiable C++ Exception 

Boost.Python provides a default exception handler that translates selected standard exceptions, then gives up with that message.

To install your own exception translator **don\'t** see [tutorial](http://www.boost.org/libs/python/doc/tutorial/doc/exception_translation.html). ![:)](/wiki/europython/img/smile.png ":)") (**&** missed in register_exception_translator call)\
Use that:

    struct PodBayDoorException;
    void translator(const PodBayDoorException& x) {
      PyErr_SetString(PyExc_UserWarning, "I'm sorry Dave...");
    }
    BOOST_PYTHON_MODULE(kubrick) {
      register_exception_translator<
      PodBayDoorException>(&translator);
      ...
    }
