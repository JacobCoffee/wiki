# CoreJythonExamples

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# Core Jython / Python Examples 

[DocumentationAndEducation](DocumentationAndEducation)

------------------------------------------------------------------------

Examples related to core Jython / Python will be here. Intended for those new to Python / Jython

## Print 

Print Hello world

:::: 
::: 
``` 
   1 print 'Hello World' 
   2 print "Hello World"
```
:::
::::

## JArray 

I was curious on how to work with jarray and move the arrays between classes after being filled with values and operated. I think this example explains some of the basics. Of course, there are more pythonic ways to do this. Cheers! Alfonso Reyes

:::: 
::: 
``` 
   1 from java.lang import Math
   2 from jarray import array, zeros
   3 import java.util.Random;
   4 
   5 class ArrayClass:
   6     """    This class will fill an array with random numbers
   7     and then return the array for further operations
   8     """
   9     def __init__(self, elems):
  10         self.N = elems
  11         systemEnergy = 0.0025
  12         self.v = zeros(self.N, "d")     # array of zeros, double type
  13         v0 = Math.sqrt(2.0 * systemEnergy / self.N)
  14         for i in range(self.N):
  15             r = java.util.Random()
  16             self.v[i] = v0 * r.nextInt(self.N)  # same velocity for all particles
  17 
  18     def out(self):
  19         for i in range(self.N):
  20             print i, self.v[i]
  21 
  22     def get(self):
  23         return self.v
  24 
  25 n = 100
  26 uarr = zeros(n, "d")    # array of double to store some operations
  27 ac = ArrayClass(n)      
  28 ac.out()                # print the array
  29 arr = ac.get()          # get the array to start doing some work on it
  30 
  31 # get a first third of the array members and times 10
  32 print "Get a first third of the array members"
  33 for i in range(n/3):
  34     uarr[i] = arr[i] * 10
  35     print i, arr[i], uarr[i]
```
:::
::::

## Multidimensional 2-D String Array 

In case you need 2-D string arrays this example may help you to start. Cheers! Alfonso Reyes, Houston-Texas

:::: 
::: 
``` 
   1 from java.lang.reflect import Array
   2 import java
   3 
   4 rows = 3
   5 cols = 3
   6 
   7 str2d = java.lang.reflect.Array.newInstance(java.lang.String,[rows, cols])
   8 str2d[0][0] = "python"
   9 str2d[1][0] = "jython"
  10 str2d[2][0] = "java"
  11 
  12 str2d[0][1] = "syntax "
  13 str2d[1][1] = "strength"
  14 str2d[2][1] = "libraries"
  15 
  16 str2d[0][2] = "unclutter"
  17 str2d[1][2] = "combine"
  18 str2d[2][2] = "graphics"
  19 
  20 print str2d
  21 
  22 print "printing multidimensional array"
  23 for i in range(len(str2d)):
  24     for j in range(len(str2d[i])):
  25         print str2d[i][j]+"\t",
  26     print
  27 print
```
:::
::::

## Finding methods in a python script 

Posted on the Jython list March 18, 2008:

This will give you name-method pairs; if you just want the names, call keys() on it.

    import inspect

    def _is_some_method(object):
        return inspect.ismethod(object) or inspect.ismethoddescriptor(object)

    def allmethods(cl):
        methods = {}
        for key, value in inspect.getmembers(cl, _is_some_method):
            methods[key] = 1
        for base in cl.__bases__:
            methods.update(allmethods(base)) # all your base are belong to us
        for key in methods.keys():
            methods[key] = getattr(cl, key)
        return methods

Usage example:

    >>> allmethods(str).keys()
    ['__unicode__', 'rjust', 'center', 'endswith', 'decode', 'translate', 'lower', 'encode', 'isunicode', '__setattr__', '__rmul__', '__add__', '__str__', 'istitle', 'lstrip', 'join', '__reduce_ex__', 'startswith', 'isalnum', 'rstrip', '__getattribute__', '__getslice__', '__eq__', '__init__', '__mod__', 'isupper', '__len__', 'rindex', 'isalpha', 'replace', '__ne__', 'strip', 'isspace', 'swapcase', 'split', 'isnumeric', 'capitalize', 'rfind', '__getitem__', '__contains__', 'title', '__ge__', 'index', '__repr__', 'ljust', 'islower', '__le__', 'isdecimal', 'expandtabs', '__delattr__', 'find', 'splitlines', 'count', 'upper', '__gt__', '__reduce__', 'isdigit', '__lt__', 'zfill', '__cmp__', '__mul__', '__hash__']
