# ExtensionTutorial

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# Creating a Python Extension Module from Scratch 

This guide will take you through the process of creating a Python extension module. It is assumed that you have a recent Python version (2.4 or later) and setuptools installed.

We\'ll be creating a project called \'examp\' (short for \'example\'.)

### Step 1: Create the project directory 

    > mkdir examp
    > cd examp

### Step 2: Create the setup.py script 

In the directory you just created, make a new file, setup.py containing the following:

:::: 
::: 
``` 
   1 from setuptools import setup, Extension
   2 
   3 setup(
   4     # Name of this package
   5     name="examp",
   6     
   7     # Package version
   8     version=0.1,
   9     
  10     # This tells setup how to find our unit tests.
  11     test_suite = "test.examp_unittest",
  12     
  13     # Describes how to build the actual extension module from C source files.
  14     ext_modules = [
  15         Extension(
  16           'examp',         # Python name of the module
  17           ['src/examp.c']  # Source files to build
  18         )]
  19     )
```
:::
::::

The `setup.py` file tells Python how to compile, test, and install your extension module.

### Step 3: Create the module source file 

This will be located in the location specified in the `setup.py` script given above; in this example, the location is `examp/src/examp.c`. This file will contain the following:

:::: 
::: 
``` 
   1 #include <Python.h>
   2 
   3 PyMODINIT_FUNC initexamp(void)
   4 {
   5     PyObject *m;
   6     
   7     m = Py_InitModule( "examp", NULL );
   8 }
```
:::
::::

As you can see, this is a pretty minimal extension module - it does nothing but establish that there is, in fact, a module. We\'ll add more to this later, but for now, let\'s just see if we can get it to compile and run.

### Step 4: Create the unit test module 

Create an empty [init.py] file in examp/test.

    > mkdir test
    > touch test/__init__.py

### Step 5: Create the unit test source file 

This will be located in `examp/test/examp_unittest.py`. This file will contain the following.

:::: 
::: 
``` 
   1 import unittest
   2 import doctest
   3 
   4 class DeviceTest( unittest.TestCase ):
   5     # This is a simple test that just tries to load the module
   6     def runTest( self ):
   7         try:
   8             import examp
   9         except ImportError, e:
  10             self.Fail( str( e ) )
```
:::
::::

The `setup.py` will automatically scan this file for unit test cases (subclasses of `unittest.TestCase`).

At this point, your directory structure should look like this:

    examp/
      setup.py
      src/
        examp.c
      test/
        __init__.py
        examp_unittest.py

### Step 6: Build and test the module 

    > python setup.py test

If everything is correct, your extension module should have built, and you should see a message on the console telling you that your unit test has passed.

------------------------------------------------------------------------

[CategoryDistutilsCookbook](CategoryDistutilsCookbook)
