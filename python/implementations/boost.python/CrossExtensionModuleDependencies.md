# boost.python/CrossExtensionModuleDependencies

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

[DavidAbrahams](./DavidAbrahams.html): This is going to have to be a FAQ about dynamic linking, RTTI, and exception-handling issues in general.

There are three basic dynamic linking models; I\'ll call these

- Global - \"everything\" is shared across the link boundary.
  - This is what usually happens on Unix systems when dynamic linking; it\'s much like static linking (but not exactly). The global model is not available on Windows (this might be a good thing).

  Explicit - explicitly marked symbols are shared across the link boundary.
  - This is what Windows compilers do with DLLs

    using `__declspec(dllexport)/__declspec(dllimport)`{.backtick}. Although the explicit model is technically available on many Unices, it\'s usually very cumbersome and requires special support from scripts outside the compiler.

  Insular - This is the model used for plugins where no symbols are shared.
  - Instead, you open the shared library explicitly and get (function) pointers to the symbols you\'re looking for. Python uses this model to open extension modules, so that extension module writers don\'t need to know what symbols other extension modules might be using.

On Unix systems, Python is an executable which opens extension modules using the Insular model (dlopen), and on most systems the Python symbols used by extension modules are simply left unresolved and, as far as I know, because they are unresolved they automatically get hooked up to the symbols in the Python executable. AIX is a bit different - because it has true insulation Python explicitly hooks all its symbols up to the extension module when it is loaded.

On Windows, that implicit back-linking is not available, so the Python executable is just a shell which links Explicitly to the Python DLL. Extension modules are loaded by Python using the Insular model but also link to the Python DLL using the Explicit model. I think Python doesn\'t do something similar for AIX only because of a failure of the imagination ;-\>

On Windows, [boost.python]() extension modules link to the Boost.Python library using the Explicit model. On Unix systems, they use the Global model. Note, however, that the fact that two extension modules are linked to the same library with the Global model does not mean the extension modules share all symbols. In fact (excepton Tru64 when -tlocal is not used to link \-- not recommended), the extension modules will **only** share a symbol which is also present in a library they are both linked to.

Most of the subtle problems with dynamic linking C++ have to do with symbols C++ generates implicitly:

- RTTI and EH information
- virtual tables
- static data members of class template instantiations
- static variables in function template instantiations

Typically, in the Global model this information (known as \"weak symbols\" on Linux) is generated in every translation unit where it is used, and resolved away at link time. Of course, that leaves us with a single copy per link unit (executable or shared library), and which copy is used needs to be resolved at load time.\*\*

The solutions generally come down to controlling where those symbols are generated and how they are shared across boundaries.

Whether the first two things are a problem for your application depends in part on the ABI (application binary interface) of your compiler. The ABI encompasses issues such as function calling convention, class layout, the format of EH tables, the format of RTTI information, and of course, the procedures the compiler uses to manipulate that information.

Your problem with boost::any was an interaction with the compiler\'s implementation of dynamic_cast. Recent GCCs determine dynamic type equivalence by comparing the **addresses** (not the contents) of their RTTI information. Because your two extension modules are not sharing any symbols other than those in the Boost.Python library, each one gets its own copy of the RTTI for the class in the any object, and the template instantiation of the any_cast on each side of the library boundary uses a different copy. The solution is to get that RTTI information generated in a place that both libraries can see. The best way to achieve that is to link both extension modules to a common shared library using the global model, and put the RTTI information there. For the case in question, you might achieve that by explicitly instantiating the any_cast template there.

The problem we had earlier with catching exceptions is an interaction with the compiler\'s implementation of EH and the behavior of glibc under dynamic linking. Recent glibc implementations have an \"inconvenient\" (charitably speaking) behavior with weak symbols. The result is that if the symbol appears in both extension modules **and** in the Boost.Python shared library, the first extension module loaded will share a copy with the Boost.Python library and each module loaded thereafter will get its own copy. Fortunately, I knew that classes with non-inline virtual functions are different, and usually a **strong** symbol gets generated in the translation unit containing the class\' first non-inline virtual function. By adding a virtual destructor in the Boost.Python library we ensured that both extension modules got the same copy of the exception\'s EH info.

\>\> The Windows crash, FWIW, is a poor-QOI issue \"bug\" in the Dinkumware standard library that ships with vc6. vc7 solves it.

This problem is that the vc6 associative containers use a special static data member representing a \"NULL\" node, used as a sentinel to tell the container implementation where the \"edge\" is, so it would stop searching there. Because you instantiated the map\<\> template in two separate extension modules, each one got it\'s own copy of the \"NULL\" node, and a map passed across the boundary would contain the wrong sentinel value for the code on the other side.
