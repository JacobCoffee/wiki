# JavaLibraries

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# Using Java Classes in Jython 

[DocumentationAndEducation](DocumentationAndEducation)

------------------------------------------------------------------------

### Array 

Posted to the Jython-users mailing list by Alfonso Reyes on October 14, 2007\

Here is an example of a 3D array. I am not fully satisfied with this implementation but to anybody starting with Jython and Java arrays will clarify lots of things.

To do:\
- the class should automatically instantiate and return the array\
- a print method that can print the class or any arrays operating outside the class

:::: 
::: 
``` 
   1 """     3D array with class
   2 
   3 """
   4 from java.lang.reflect import Array
   5 import java
   6 
   7 class multi:
   8     def __init__(self, i, j, k):
   9         self.m = i; self.n = j; self.p = k
  10         self.arr = Array.newInstance(java.lang.Double.TYPE, [self.m, self.n, self.p] )
  11 
  12     def get(self):
  13         return self.arr
  14 
  15     def out(self):
  16         print "printing multidimensional array inside class"
  17         for i in range(0, self.m, 1):
  18             for j in range(0, self.n, 1):
  19                 for k in range(0, self.p,1):
  20                     print self.arr[i][j][k],
  21                 print
  22             print
  23         print
  24 
  25 
  26 def out(arr,m,n,p):
  27     # TO-DO: one method that can print a class-array and a bare array
  28     print "printing multidimensional array"
  29     for i in range(0, m, 1):
  30         for j in range(0, n, 1):
  31             for k in range(0, p,1):
  32                 print arr[i][j][k],
  33             print
  34         print
  35     print
  36 
  37 
  38 tArr = multi(4,3,5)
  39 uArr = tArr.get()
  40 
  41 print uArr
  42 tArr.out()
  43 uArr[0][0][0] = 7.77
  44 uArr[3][2][4] = 7.77
  45 out(uArr,4,3,5)        # read what the array contains
```
:::
::::
