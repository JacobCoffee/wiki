# boost.python/EmbeddingPython

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# New Revisions of Boost 

Since this Wiki page was originally written, Boost::Python has added C++ wrappers for a lot of the direct C code this page references. The documentation for those wrappers are available under \"Embedding\" in the TOC. The current version, as of this writing, is here: [http://www.boost.org/doc/libs/1_46_0/libs/python/doc/v2/exec.html](http://www.boost.org/doc/libs/1_46_0/libs/python/doc/v2/exec.html)

An example similar to the one below is provided at the bottom of the page.

# Full example 

While Boost.Python does not provide all the constructs necessary for embedding Python in a C++ application, using it will still dramatically help with the task.

**Note:** Because there is very little documentation on a lot of this, I am not entirely sure that the methods I am describing are the best to accomplish the task. If there is a better way, please write it up here.

First, a simple \"Hello, World\" script, run from a C++ program:

:::: 
::: 
``` 
   1 #include <boost/python.hpp>
   2 
   3 using namespace boost::python;
   4 
   5 int main( int argc, char ** argv ) {
   6   try {
   7     Py_Initialize();
   8 
   9     object main_module((
  10       handle<>(borrowed(PyImport_AddModule("__main__")))));
  11 
  12     object main_namespace = main_module.attr("__dict__");
  13 
  14     handle<> ignored(( PyRun_String( "print \"Hello, World\"",
  15                                      Py_file_input,
  16                                      main_namespace.ptr(),
  17                                      main_namespace.ptr() ) ));
  18   } catch( error_already_set ) {
  19     PyErr_Print();
  20   }
  21 }
```
:::
::::

Compile this as a normal C++ program, linking it to libpython and libboost_python, and make sure that the compiler knows where the Python include files are. When run, it should print to the command line \"Hello, World\". Since this is all in the Boost.Python tutorial, I will skip the line-by-line explanation for now.

This is all well and good, but it is pretty useless, since you might as well have sent the Python code directly to the interpreter and saved yourself a lot of hassle. What you really want is to provide the Python code executed from the [PyRun](./PyRun.html)\_\* function with access to your C++ program\'s classes and data, so that the Python code can get some work done.

Before we can do that, let\'s define a simple C++ class that we want the Python code to access:

:::: 
::: 
``` 
   1 class CppClass {
   2 public:
   3   int getNum() {
   4     return 7;
   5   }
   6 };
```
:::
::::

Now for the fun stuff, providing the embedded Python script with access to our new class. In our previous main() function, add after the `object main_namespace`{.backtick} is declared:

:::: 
::: 
``` 
  13 main_namespace["CppClass"] = class_<CppClass>("CppClass")
  14                                .def("getNum",&CppClass::getNum);
```
:::
::::

Of course, if the `CppClass`{.backtick} were more complicated, it would be necessary to use a more complicated series of `def`{.backtick}s. Now you can replace the \"print Hello, World\" Python code with the following, to call the getNum(), and you should see \"7\" printed to the console:

:::: 
::: 
``` 
"cpp = CppClass()\n"
"print cpp.getNum()\n"
```
:::
::::

So, now you can create C++ objects in Python, but you will probably want the Python code to be able to access existing C++ data. To do this, first create an instance of `CppClass`{.backtick} (we\'ll call ours `cpp`{.backtick}) at the beginning of `main()`{.backtick}. Now, after the `class_`{.backtick} declaration, add:

:::: 
::: 
``` 
   7 main_namespace["cpp"] = ptr(&cpp);
```
:::
::::

Now, you should be able to change your Python code to `"print cpp.getNum()"`{.backtick}, and the number 7 should again be printed to the command line. The difference here is that the Python code and C++ code all share the same object. We passed a `ptr`{.backtick} into the Python interpreter to prevent a copy of the object from being made. We could have directly assigned `cpp`{.backtick} to the namespace, but any changes made to the object by the Python code would have been made to a local version of the object, not the instance which the C++ code has access to.

Now would also be a good time to point out that while Python manages memory for you, C++ does not. Always make sure that data available to the Python interpreter is actually available, or you will get mysterious crashes which may be hard to track down.

So, we finally have access to our C++ application\'s data, but now the script programmers are complaining that all of the data is in the global namespace, mucking up their scripts and generally getting in the way. To avoid this, and provide proper encapsulation, we should put all of our classes and data into a module. The first step is to remove all the lines which modify the `main_namespace`{.backtick} object, and then add a standard Boost module definition:

:::: 
::: 
``` 
   1 BOOST_PYTHON_MODULE(CppMod) {
   2   class_<CppClass>("CppClass")
   3     .def("getNum",&CppClass::getNum);
   4 }
```
:::
::::

Now, inside `main()`{.backtick} and **before** the call to `Py_Initialize()`{.backtick} we want to call `PyImport_AppendInittab( "CppMod", &initCppMod );`{.backtick} `initCppMod`{.backtick} is a function created by the `BOOST_PYTHON_MODULE`{.backtick} macro which is used to initialize the Python module `CppMod`{.backtick}. At this point, your embedded python script may call `import CppMod`{.backtick} and then access `CppClass`{.backtick} as a member of the module.

It would be convenient, however, if the module was already imported, so that the programmer does not have to manually load the module at the beginning of each script. To do this, add the following after the `main_namespace`{.backtick} object has been initialized:

:::: 
::: 
``` 
object cpp_module( (handle<>(PyImport_ImportModule("CppMod"))) );
main_namespace["CppMod"] = cpp_module;
```
:::
::::

The first line loads the module, executing the `initCppMod`{.backtick} function, and the second line makes the loaded module available in the main namespace. Scripts may now refer to `CppMod`{.backtick} without needing to manually import it.

This also allows us to add data to the already-imported module. We can do this from within `main()`{.backtick} with the following line:

:::: 
::: 
``` 
scope(cpp_module).attr("cpp") = ptr(&cpp);
```
:::
::::

Scripts are now able to access the `cpp`{.backtick} instance of `CppClass`{.backtick} from the `CppMod`{.backtick} module.

While this is certainly not complete, hopefully it will provide a starting point for using Boost.Python to embed Python scripts in your applications.

\--Thomas Stephens \<spiralman at gmail.com\>

# Tips and Tricks 

## Loading a module by full or relative path 

The main benefit of this approach is that you don\'t need to worry about escaping strings.

:::: 
::: 
``` 
   1 boost::python::object
   2 myapp::python::import( const myapp::Path & s )
   3 {
   4   using namespace boost::python;
   5   try
   6   {
   7     // If path is /Users/whatever/blah/foo.py
   8     dict locals;
   9     locals["modulename"] = s.filebase(); // foo -> module name
  10     locals["path"]   = s.get(); // /Users/whatever/blah/foo.py
  11     exec("import imp\n"
  12          "newmodule = imp.load_module(modulename,open(path),path,('py','U',imp.PY_SOURCE))\n",
  13          globals(),locals);
  14     return locals["newmodule"];
  15   }
  16   catch( error_already_set )
  17   {
  18     error(currentException());
  19     return object();
  20   }
  21 }
```
:::
::::

## Extracting Python Exceptions 

:::: 
::: 
``` 
   1 std::string
   2 extractException()
   3 {
   4   using namespace boost::python;
   5 
   6   PyObject *exc,*val,*tb;
   7   PyErr_Fetch(&exc,&val,&tb);
   8   PyErr_NormalizeException(&exc,&val,&tb);
   9   handle<> hexc(exc),hval(allow_null(val)),htb(allow_null(tb));
  10   if(!hval)
  11   {
  12     return extract<std::string>(str(hexc));
  13   }
  14   else
  15   {
  16     object traceback(import("traceback"));
  17     object format_exception(traceback.attr("format_exception"));
  18     object formatted_list(format_exception(hexc,hval,htb));
  19     object formatted(str("").join(formatted_list));
  20     return extract<std::string>(formatted);
  21   }
  22 }
```
:::
::::

## Line-oriented Logging of Python Exceptions 

The following sample is written using log4cxx. It may be trivially adapted to any other line-oriented logging system that prefixes every log message, such as syslog.

:::: 
::: 
``` 
   1 void
   2 logPythonException()
   3 {
   4   using namespace boost::python;
   5 
   6   PyObject *exc, *val, *tb;
   7   PyErr_Fetch(&exc, &val, &tb);
   8   PyErr_NormalizeException(&exc, &val, &tb);
   9   handle<> hexc(exc), hval(allow_null(val)), htb(allow_null(tb));
  10   if(!hval)
  11   {
  12     // With log4cxx::LoggerPtr logger previously declared and 
  13     // initialized with log4cxx::Logger::getLogger("some.name")
  14     LOG4CXX_ERROR(logger, std::string(extract<std::string>(str(hexc)));
  15   }
  16   else
  17   {
  18     object traceback(import("traceback"));
  19     object format_exception(traceback.attr("format_exception"));
  20     list formatted_list(format_exception(hexc,hval,htb));
  21     for(int count = 0; count < len(formatted_list); ++count)
  22       LOG4CXX_ERROR(logger, std::string(extract<std::string>(formatted_list[count].slice(0,-1))));
  23   }
  24 }
```
:::
::::

## Working with Unicode 

Python supports unicode and string objects. If you have your own string type that stores UTF-8 it is very simple (I think) to support Unicode from Python:

      struct String_from_python_str
      {
        String_from_python_str()
        {
          boost::python::converter::registry::push_back(
            &convertible,
            &construct,
            boost::python::type_id<String>());
        }

        static void* convertible(PyObject* obj)
        {
          return
            (PyString_Check(obj) || PyUnicode_Check(obj)) 
            ? obj
            : 0
            ;
        }

        static void construct(
          PyObject* obj,
          boost::python::converter::rvalue_from_python_stage1_data* data)
        {
          namespace py = boost::python;
          if(PyString_Check(obj))
          {
            const char* value = PyString_AsString(obj);
            MY_CHECK(value,translate("Received null string pointer from Python"));
            void* storage = ((py::converter::rvalue_from_python_storage<String>*)data)->storage.bytes;
            new (storage) String(value);
            data->convertible = storage;
          }
          else if(PyUnicode_Check(obj))
          {
            py::handle<> utf8(py::allow_null(PyUnicode_AsUTF8String(obj)));
            MY_CHECK(utf8,translate("Could not convert Python unicode object to UTF8 string"));
            void* storage = ((py::converter::rvalue_from_python_storage<String>*)data)->storage.bytes;
            const char* utf8v = PyString_AsString(utf8.get());
            MY_CHECK(utf8v,translate("Received null string from utf8 string"));
            new(storage) String(utf8v);
            data->convertible = storage;
          }
          else
          {
            error(translate("Unexpected type for string conversion"));
          }
        }
      };

      BOOST_PYTHON_MODULE(whatever)
      {
        ...
        String_from_python_str();
      }
