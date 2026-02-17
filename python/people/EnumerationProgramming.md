# EnumerationProgramming

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# Enumeration Programming 

### Why, When 

This Implementation is really near to the UML description of [\<\<Enumeration\>\>]. It uses new style class.

### Code 

:::: 
::: 
``` 
   1 # code is public domain
   2 
   3 class Enumeration(object):
   4     
   5     def __new__(cls, arg):
   6         if hasattr(cls, arg):
   7             return getattr(cls,arg)
   8         else:
   9             return object.__new__(cls, arg)
  10     
  11     def __init__(self, name):
  12         self._name = name
  13         setattr(self.__class__, name, self)
  14 
  15     def __str__(self):
  16         return '#%s' % self._name
  17 
  18     def __repr__(self):
  19         return "%s('%s')" % (self.__class__.__name__, self._name)
  20 
  21     def getEnumerationSet(cls):
  22         result = set()
  23         for attr in dir(cls):
  24             attr = getattr(cls, attr)
  25             if isinstance(attr, Enumeration):
  26                 result.add(attr)
  27         return result
  28     getEnumerationSet = classmethod(getEnumerationSet)
```
:::
::::

### Example 

:::: 
::: 
``` 
   1 class PrimaryColorKind(Enumeration):
   2     pass
   3 PrimaryColorKind('Rouge')
   4 PrimaryColorKind('Vert')
   5 PrimaryColorKind('Bleu')
   6 
   7 print PrimaryColorKind.Rouge, PrimaryColorKind.Vert, PrimaryColorKind.Bleu
   8 print PrimaryColorKind.getEnumerationSet()
   9 
  10 class ColorKind(PrimaryColorKind):
  11     pass
  12 ColorKind('Violet')
  13 
  14 
  15 print ColorKind.Rouge, ColorKind.Violet
  16 print ColorKind.getEnumerationSet()
  17 print repr(ColorKind.Rouge), repr(ColorKind.Violet)
  18 assert(ColorKind.Rouge is ColorKind('Rouge'))
```
:::
::::

output is :

    #Rouge #Vert #Bleu
    Set([PrimaryColorKind('Vert'), PrimaryColorKind('Rouge'), PrimaryColorKind('Bleu')])
    #Rouge #Violet
    Set([PrimaryColorKind('Vert'), PrimaryColorKind('Rouge'), ColorKind('Violet'), PrimaryColorKind('Bleu')])
    PrimaryColorKind('Rouge') ColorKind('Violet')
    mirville Python 79 % python Enumeration.py
    #Rouge #Vert #Bleu
    Set([PrimaryColorKind('Vert'), PrimaryColorKind('Rouge'), PrimaryColorKind('Bleu')])
    #Rouge #Violet
    Set([PrimaryColorKind('Vert'), PrimaryColorKind('Rouge'), ColorKind('Violet'), PrimaryColorKind('Bleu')])
    PrimaryColorKind('Rouge') ColorKind('Violet')
