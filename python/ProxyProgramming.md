# ProxyProgramming

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# Proxy 

See also [http://www.python.org/workshops/1997-10/proceedings/savikko.html](http://www.python.org/workshops/1997-10/proceedings/savikko.html)

### special method names 

------------------------------------------------------------------------

**pro**

- ??

------------------------------------------------------------------------

**cons**

- ??

:::: 
::: 
``` 
   1 # Code is Public Domain.
   2 class Proxy(object):
   3     def __init__(self, subject):
   4         self._subject = subject
   5         
   6     def __getattr__(self, attrName):
   7         return getattr(self._subject, attrName)
   8     
   9     def __setattr__(self, attrName, value):
  10         object.__setattr__(self, attrName, value)
  11 
  12     def __delattr__(self, attrName):
  13         delattr(self._subject, attrName)
  14 
  15     def __call__(self,*args,**keys):
  16         object.__getattribute__(self,'_subject')(*args,**keys)
  17 
  18     def __getitem__(self,key):
  19         return object.__getattribute__(self,'_subject')[key]
  20 
  21 ##    should implement other special method names here
  22 ##    see http://www.python.org/doc/2.3.2/ref/specialnames.html
  23 
  24 class Test:
  25     def __init__(self):
  26         self.toto = "toto"
  27 
  28     def foo(self):
  29         print "foo"
  30 
  31     def __call__(self,a,b,more=False):
  32         print self.__class__.__name__,id(self)
  33         print a,b,more
  34 
  35     def __getitem__(self,key):
  36         return 'Test%s' % key
  37 
  38 t = Test()
  39 p = Proxy(t)
  40 
  41 print p.toto
  42 p.foo()
  43 p('1',2,more=True)
  44 print p['Blabla']
```
:::
::::
