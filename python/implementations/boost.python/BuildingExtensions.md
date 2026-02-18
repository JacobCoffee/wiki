# boost.python/BuildingExtensions

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

## Building Extensions with boost.python 

### Using bjam 

bjam is a standard tool for building boost library itself. Thus it is preferable way to build Python extensions based on [boost.python]() with bjam. Basic example listed in [tutorial](http://www.boost.org/libs/python/doc/tutorial/doc/html/python/hello.html).

However if you want to add external libraries in your extension (that is why you use boost.python, isn\'t it?), you must add them to the **Jamfile**:

    # NOTE: Change [[VARIABLES]] according to your system

    # Specify our location in the boost project hierarchy
    subproject libs/python/MyExtension ; ######## if you put your dir in boost hierarchy

    # Include definitions needed for Python modules
    SEARCH on python.jam = $(BOOST_BUILD_PATH) ;

    include python.jam ;

    # Declare a Python extension
    extension Example
    :  # sources
       Example.cpp
       # dependencies
       <dll>../build/boost_python
      
    :  # requirements
       <include>[[FULL_PATH_INCLUDE_DIR]]
       <include>[[RELATIVE_PATH_INCLUDE_DIR]]
       <library-file>[[FULL_PATH_AND_LIBNAME]]
       <library-path>[[PATH_TO_LIB]]
       <library-file>[[LIBNAME]]
      ;

    # Declare a test for the extension module
    boost-python-runtest test1
        :  # Python test driver
        test1.py
        # extension modules to use
        <pyd>Example ;

Keeping your projects under boost hierarchy is often inconvenient. You may build your extension from any place by:

- changing the line `subproject` in the **Jamfile** to the

      project-root ;

- remove \<dll\> line and add to the requirements:

           # link to the appropriate library for the build variant.
          <release><find-library>boost_python
          <debug><find-library>boost_python_debug
          <debug-python><find-library>boost_python_pydebug
        
        # library path required for linking to boost_python shared lib. You
        # may need to edit this for your installation
          <library-path>$(BOOST_ROOT)/libs/python/build/VisualStudio/bin

- creating **boost-build.jam** file in the root of your project tree like that:

      BOOST_ROOT=[[PATH_TO_BOOST]] ;
      boost-build $(BOOST_ROOT)/tools/build ;

- to silence warning create empty **Jamrules** file.

### Using make 

- Make sure to link with *boost_python* or *boost_python_debug* library.

### Using SCons 

You might want to try [scons](http://www.scons.org).

It\'s really easy to build python extensions with scons. Here is an example that would build uvector.so:

    BOOST_VERSION = 'boost.cvs'
    BOOST = '/usr/local/src/' + BOOST_VERSION
    BOOSTLIBPATH = BOOST+'/stage/lib'
    env = Environment (LIBPATH=['./',BOOSTLIBPATH], CPPPATH=[BOOST, '/usr/include/python2.3'],  
                       RPATH=['./',BOOSTLIBPATH])
    env.SharedLibrary (target='uvector', source='uvector.cc', SHLIBPREFIX='', LIBS=[BOOST_PYTHON_LIB])

### Using Windows IDE 

- Make sure you keep `"Use Managed Extension" == No` if you are using Visual Studio.NET.

### Using CMake 

Save the file as CMakeLists.txt, `cd` into the directory, and run `cmake .` followed by `make`:

    cmake_minimum_required(VERSION 2.6)

    SET(ENV{BOOST_ROOT} "/path/to/my/boost")

    #substitute your version number
    find_package(Boost 1.48 EXACT REQUIRED COMPONENTS python)

    INCLUDE_DIRECTORIES("${Boost_INCLUDE_DIRS}" "/path/to/my/python/include")

    ADD_LIBRARY(MyLibrary SHARED MyLibraryInterface.cpp)
    TARGET_LINK_LIBRARIES(MyLibrary ${Boost_LIBRARIES})

On Linux, this will make a libMyLibrary.so library in the same directory.

## Tips and tricks 

To keep up with bjam rules you might want to have a *dry* run without actually building anything: {{{bjam -na }}}

------------------------------------------------------------------------

To copy resulting executable to desired directory take a look at the **stage** rule.

------------------------------------------------------------------------

To specify library in a platform-independent way you could do something like:

        local libname
        if $(NT)
        {
           libname = foo.lib
        }
        else
        {
           libname = libfoo.a
        }

            ...

        <library-file>$(libname)

in the Jamfile.

------------------------------------------------------------------------

Add -DBOOST_PYTHON_STATIC_LIB to your compiler command-line or \<define\>BOOST_PYTHON_STATIC_LIB to your bjam requirements; that will turn off exporting for win32: `__declspec(dllexport)`{.backtick}.

------------------------------------------------------------------------

If you are getting **error C1055: compiler limit : out of keys** on MS VisualC, try change /ZI (Program database for edit and continue) to /Zi (Program database).

------------------------------------------------------------------------

If you are getting error **error C1076: compiler limit - internal heap limit reached** try add /ZmNNN (with NNN=300..800)

[][][][][][][][][][][][][][][][][][][][][][][][][][][ You can use a setup.py file if u are careful ]

    #setup.py
    from distutils.core import setup
    from distutils.extension import Extension
    import os.path
    import sys
    if sys.platform == "win32" :
        include_dirs = ["C:/Boost/include/boost-1_32","."]
        libraries=["boost_python-mgw"]
        library_dirs=['C:/Boost/lib']
    else :
        include_dirs = ["/usr/include/boost-1_32","."]
        libraries=["boost_python-gcc"]
        library_dirs=['/usr/local/lib']

    files = ["test.cpp","itest.cpp"]

    setup(name="test",    
          ext_modules=[
                        Extension("test",files,
                        library_dirs=library_dirs,
                        libraries=libraries,
                        include_dirs=include_dirs,
                        depends=[]),
                        ]
         )

For the above I compile and install boost using bjam then you set the appropriate paths to your boost header and libs It works on linux and windows with mingw

That way u have nice cross platform build ![:)](/wiki/europython/img/smile.png%20":)")
