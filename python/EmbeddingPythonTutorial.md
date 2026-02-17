# EmbeddingPythonTutorial

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

While a decent amount has been written about extending Python, or in other words writing C/C++ code that plugs into Python as a module, for a variety of reasons, less has been written about embedding Python. The [Python official documentation](http://docs.python.org/ext/lower-level-embedding.html) wisely suggests one of the big reasons:

    It should be noted that extending Python and embedding Python is quite the same activity, despite the different intent. Most
    topics discussed in the previous chapters are still valid. To show this, consider what the extension code from Python to C really does:

       1. Convert data values from Python to C,
       2. Perform a function call to a C routine using the converted values, and
       3. Convert the data values from the call from C to Python.

    When embedding Python, the interface code does:

       1. Convert data values from C to Python,
       2. Perform a function call to a Python interface routine using the converted values, and
       3. Convert the data values from the call from Python to C.

    As you can see, the data conversion steps are simply swapped to accommodate the different direction of the cross-language transfer.
    The only difference is the routine that you call between both data conversions. When extending, you call a C routine, when embedding,
    you call a Python routine.

The official documentation in general does a good job introducing one to the intricacies of combining C and Python, but it leaves out a lot of embedding-specific details. This is an attempt to rectify the situation. Specifically, you will be shown how to set up an embedded Python parser to the point where all you need to do is pretend like you\'re coding a Python module, but in reverse, as the official documentation suggests.

The first thing you need to do is initialize the parser. Make sure that you have included Python.h, and are linking to the python library (for example python2.5.so on \*NIX or python2.5.dll on Windows), and have set up your compiler and linker with the proper directories for both the include file and the library file. Then the initialization itself is quite easy; a simple call to Py_Initialize() does the job. If you\'re going to be using Python a lot, you might as well leave it initialized for the duration of your application. When you are done with it, simple call Py_Finalize(). If you need to use Python again at some point after you have called Py_Finalize(), simply call Py_Initialize() again.

The next thing you need to do is set up the environment in which your Python fragments run. The easiest way to do that is to get a reference to the [main] module and namespace:

        PyObject *main_module = PyImport_ImportModule("__main__");
        PyObject *main_dict   = PyModule_GetDict(main_module);

If you want to be able to use other modules in your embedded Python, you can retrieve them the same way and then bolt it into the main module\'s namespace like so:

        PyObject *sys_module = PyImport_ImportModule("sys");
        PyObject *sys_dict   = PyModule_GetDict(sys_module);
        PyDict_SetItemString(main_dict, "sys", sys_module);

This acts just like \"import sys\" would within Python. Additionally, you can use its dictionary to access whatever variables and/or functions you want from it, like so:

        PyObject *version_obj = PyMapping_GetItemString(sys_dict, "version");
        char *version_string = PyString_AsString(version_obj);
        printf("%s\n", version_string);

You can now use the environment you created to call functions and run scripts at will. You can use the data transferring routines to pass variables into and retrieve variables out of the [main] namespace of the embedded Python interpreter. Here is a simple, but complete example you can compile to try it out:

    #include <Python.h>

    const char *pycode =
        "def fact(n):\n"
        "    if n <= 1:\n"
        "        return 1\n"
        "    else:\n"
        "        return n*fact(n-1)\n"
        "k = fact(i)";

    int main()
    {
        PyObject *main_module, *main_dict;
        PyObject *sys_module, *sys_dict;
        PyObject *version_obj, *i_obj, *k_obj;
        char *version_string;
        long int i, k;

        Py_Initialize();

        /* Setup the __main__ module for us to use */
        main_module = PyImport_ImportModule("__main__");
        main_dict   = PyModule_GetDict(main_module);

        /* Fetch the sys module */
        sys_module = PyImport_ImportModule("sys");
        sys_dict   = PyModule_GetDict(sys_module);

        /* Attach the sys module into the __main__ namespace */
        PyDict_SetItemString(main_dict, "sys", sys_module);

        /* Retrieve the Python version from sys and print it out */
        version_obj = PyMapping_GetItemString(sys_dict, "version");
        version_string = PyString_AsString(version_obj);
        printf("%s\n\n", version_string);
        Py_XDECREF(version_obj);

        /* Inject a variable into __main__, in this case i */
        i = 5;
        i_obj = PyInt_FromLong(i);
        PyDict_SetItemString(main_dict, "i", i_obj);

        /* Run the code snippet above in the current environment */
        PyRun_SimpleString(pycode);

        /* Extract the resultant variable, k */
        k_obj = PyMapping_GetItemString(main_dict, "k");
        k = PyInt_AsLong(k_obj);
        Py_XDECREF(k_obj);
        Py_XDECREF(i_obj);

        /* Show the result of the Python calculation */
        printf("Python calculated that %d! = %d\n", i, k);

        Py_Finalize();

        return 0;
    }

Save it to a file and compile it with your favorite C compiler, again remembering to set the correct include and link paths and link with the Python library, and it should run as-is.

You may also extend the embedded environment just like you would make a normal extension to give your embedded Python access to your C/C++ code. I refer you to the official documentation for further information, as it describes well how to make extensions, and how to extend embedded Python specifically. That, transferring data between Python and C, reference counting, and your imagination are all you need to do whatever you want in embedded Python. Enjoy!

------------------------------------------------------------------------

- [CategoryDocumentation](CategoryDocumentation)
