# DecoratorPattern

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# Decorator Pattern 

The [DecoratorPattern](http://c2.com/cgi/wiki?DecoratorPattern "Wiki") is a pattern described in the [DesignPatternsBook](http://c2.com/cgi/wiki?DesignPatternsBook "Wiki"). It is a way of apparently modifying an object\'s behavior, by enclosing it inside a decorating object with a similar interface.

This is not to be confused with [PythonDecorators](../archive/PythonDecorators), which is a language feature for dynamically modifying a function or class.

## Example 

This is an example of using the Decorator Pattern within Python.

:::: 
::: 
``` 
   1 """
   2 Demonstrated decorators in a world of a 10x10 grid of values 0-255. 
   3 """
   4 
   5 import random
   6 
   7 def s32_to_u16( x ):
   8     if x < 0:
   9         sign = 0xf000
  10     else:
  11         sign = 0
  12     bottom = x & 0x00007fff
  13     return bottom | sign
  14 
  15 def seed_from_xy( x,y ): return s32_to_u16( x ) | (s32_to_u16( y ) << 16 )
  16 
  17 class RandomSquare:
  18     def __init__( s, seed_modifier ):
  19         s.seed_modifier = seed_modifier
  20     def get( s, x,y ):
  21         seed = seed_from_xy( x,y ) ^ s.seed_modifier
  22         random.seed( seed )
  23         return random.randint( 0,255 )
  24 
  25 class DataSquare:
  26     def __init__( s, initial_value = None ):
  27         s.data = [initial_value]*10*10
  28     def get( s, x,y ):
  29         return s.data[ (y*10)+x ] # yes: these are all 10x10
  30     def set( s, x,y, u ):
  31         s.data[ (y*10)+x ] = u
  32 
  33 class CacheDecorator:
  34     def __init__( s, decorated ):
  35         s.decorated = decorated
  36         s.cache = DataSquare()
  37     def get( s, x,y ):
  38         if s.cache.get( x,y ) == None:
  39             s.cache.set( x,y, s.decorated.get( x,y ) )
  40         return s.cache.get( x,y )
  41 
  42 class MaxDecorator:
  43     def __init__( s, decorated, max ):
  44         s.decorated = decorated
  45         s.max = max
  46     def get( s, x,y ):
  47         if s.decorated.get( x,y ) > s.max:
  48             return s.max
  49         return s.decorated.get( x,y )
  50 
  51 class MinDecorator:
  52     def __init__( s, decorated, min ):
  53         s.decorated = decorated
  54         s.min = min
  55     def get( s, x,y ):
  56         if s.decorated.get( x,y ) < s.min:
  57             return s.min
  58         return s.decorated.get( x,y )
  59 
  60 class VisibilityDecorator:
  61     def __init__( s, decorated ):
  62         s.decorated = decorated
  63     def get( s,x,y ):
  64         return s.decorated.get( x,y )
  65     def draw(s ):
  66         for y in range( 10 ):
  67              for x in range( 10 ):
  68                  print "%3d" % s.get( x,y ),
  69              print
  70 
  71 # Now, build up a pipeline of decorators:
  72 
  73 random_square = RandomSquare( 635 )
  74 random_cache = CacheDecorator( random_square )
  75 max_filtered = MaxDecorator( random_cache, 200 )
  76 min_filtered = MinDecorator( max_filtered, 100 )
  77 final = VisibilityDecorator( min_filtered )
  78 
  79 final.draw()
```
:::
::::

\...which outputs something like:

    100 100 100 100 181 161 125 100 200 100
    200 100 100 200 100 200 200 184 162 100
    155 100 200 100 200 200 100 200 143 100
    100 200 144 200 101 143 114 200 166 136
    100 147 200 200 100 100 200 141 172 100
    144 161 100 200 200 200 190 125 100 177
    150 200 100 175 111 195 193 128 100 100
    100 200 100 200 200 129 159 105 112 100
    100 101 200 200 100 100 200 100 101 120
    180 200 100 100 198 151 100 195 131 100

So, what about this is the [DecoratorPattern](http://c2.com/cgi/wiki?DecoratorPattern "Wiki") ?

It\'s that objects are enclosing other objects, that they share similar interfaces, and that the decorating object appears to mask or modify or annotate the enclosed object.

## Discussion 

Isn\'t there a better way to do this in Python?

*To make decorators, to solve this particular problem, or what?* \-- [LionKimbro](LionKimbro) 2005-05-05 17:52:12
