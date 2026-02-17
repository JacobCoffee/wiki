# LearnByObservation

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

Note : This is an experimental page, Python can be learned interactively from a prompt, and learning by observations is a good habit, so this page. \-- [BaijuMuthukadan](BaijuMuthukadan)

(This page is not linked from main pages yet.)

### Creating Integer Objects 

:::: 
::: 
``` 
   1 >>> a = 1
   2 >>> a
   3 1
   4 >>> type(a)
   5 <type 'int'>
   6 >>> b = int(1)
   7 >>> b
   8 1
   9 >>> type(b)
  10 <type 'int'>
```
:::
::::

### \_\_del\_\_ workings 

:::: 
::: 
``` 
   1 >>> class C:
   2 ...     def __del__(self):
   3 ...         print "HI"
   4 ... 
   5 >>> c=C()
   6 >>> del(c)
   7 HI
   8 >>> c=C()
   9 >>> c=1
  10 HI
  11 >>> c
  12 1
  13 >>> c=C()
  14 >>> d=c
  15 >>> c=4
  16 >>> d=7
  17 >>> d
  18 HI
  19 7
  20 >>> c=C()
  21 >>> d=c
  22 >>> c=4
  23 >>> d=7
  24 HI
```
:::
::::

### list append and assignment 

:::: 
::: 
``` 
   1 >>> a=[1,2,3]
   2 >>> print a
   3 [1, 2, 3]
   4 >>> a=a.append(4)
   5 >>> print a
   6 None
```
:::
::::

### staticmethod vs. classmethod 

:::: 
::: 
``` 
   1 >>> class C:
   2 ...     a=1
   3 ...     @staticmethod
   4 ...     def temp():
   5 ...             print C.a
   6 ... 
   7 >>> C.temp()
   8 1
   9 >>> class C:
  10 ...     a=1
  11 ...     @classmethod
  12 ...     def temp(cls):
  13 ...             print cls.a
  14 ... 
  15 >>> C.temp()
  16 1
```
:::
::::
