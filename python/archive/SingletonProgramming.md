# SingletonProgramming

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# Singleton 

See also [http://c2.com/cgi/wiki?PythonSingleton](http://c2.com/cgi/wiki?PythonSingleton) and [http://www.python.org/workshops/1997-10/proceedings/savikko.html](http://www.python.org/workshops/1997-10/proceedings/savikko.html)

### classmethod

------------------------------------------------------------------------

**pro**

- You can use both as simple class or as a singleton.
- You do not need to write code for each class you want to act as singleton.

------------------------------------------------------------------------

**cons**

:::: 
::: 
``` 
   1 # Code is Public Domain.
   2 class Singleton:
   3     _singleton = None
   4     def getSingleton(cls):
   5         if not isinstance(cls._singleton,cls):
   6             cls._singleton = cls()
   7         return cls._singleton
   8 
   9     getSingleton = classmethod(getSingleton)
  10 
  11 if __name__=='__main__':
  12     class Test(Singleton):
  13         def test(self):
  14             print self.__class__,id(self)
  15 
  16     class Test1(Test):
  17         def test1(self):
  18             print self.__class__,id(self),'Test1'
  19 
  20     t1 = Test.getSingleton()
  21     t2 = Test.getSingleton()
  22     
  23     t1.test()
  24     t2.test()
  25     assert(isinstance(t1,Test))
  26     assert(isinstance(t2,Test))
  27     assert(id(t1)==id(t2))
  28 
  29     t1 = Test1.getSingleton()
  30     t2 = Test1.getSingleton()
  31 
  32     assert(isinstance(t1,Test1))
  33     assert(isinstance(t2,Test1))
  34     assert(id(t1)==id(t2))
  35     
  36     t1.test()
  37     t1.test1()
  38     t2.test()
  39     t1.test1()
  40 
  41     t3 = Test.getSingleton()
  42     
  43     t3.test()
  44     assert(isinstance(t3,Test))
```
:::
::::
