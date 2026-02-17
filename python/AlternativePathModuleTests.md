# AlternativePathModuleTests

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

:::: 
::: 
``` 
   1 ======================================
   2 doctest for path.py
   3 
   4 Uncomplete, and tests POSIX paths only
   5 ======================================
   6 
   7 >>> from mypath import path
   8 
   9 # Test root
  10 
  11 >>> path.ROOT
  12 path.ROOT
  13 
  14 >>> path.ROOT == path.ROOT
  15 True
  16 >>> path.ROOT < path.ROOT
  17 False
  18 >>> path.ROOT > path.ROOT
  19 False
  20 
  21 >>> path.ROOT == 'e'
  22 False
  23 >>> path.ROOT < 'h'
  24 True
  25 >>> path.ROOT > 'b'
  26 False
  27 >>> path.ROOT > 3
  28 Traceback (most recent call last):
  29 ...
  30 TypeError: Comparison not defined
  31 
  32 >>> 'a' == path.ROOT
  33 False
  34 >>> 'a' < path.ROOT
  35 False
  36 >>> 'a' > path.ROOT
  37 True
  38 >>> 3 > path.ROOT
  39 Traceback (most recent call last):
  40 ...
  41 TypeError: Comparison not defined
  42 
  43 
  44 # Basic path creation
  45 
  46 >>> path('/bin/arch')
  47 path('/bin/arch')
  48 >>> p = _
  49 >>> p[0]
  50 path.ROOT
  51 >>> p[1]
  52 'bin'
  53 >>> p[2]
  54 'arch'
  55 >>> len(p)
  56 3
  57 >>> path('hello/what')
  58 path('hello/what')
  59 >>> p = _
  60 >>> p[0]
  61 'hello'
  62 >>> p[1]
  63 'what'
  64 >>> len(p)
  65 2
  66 >>> path('.')
  67 path('.')
  68 >>> len(_)
  69 0
  70 >>> path('')
  71 path('.')
  72 >>> path()
  73 path('.')
  74 >>> path('/')
  75 path('/')
  76 
  77 # Constructing from a string
  78 
  79 >>> path('hello//what')
  80 path('hello/what')
  81 >>> path('hello//what/')
  82 path('hello/what')
  83 >>> path('/hello//what/')
  84 path('/hello/what')
  85 >>> path('//hello//what/')
  86 Traceback (most recent call last):
  87 ...
  88 NotImplementedError: Paths with two leading slashes aren't supported.
  89 >>> path('///hello//what/')
  90 path('/hello/what')
  91 
  92 # Constructing from an iterable
  93 
  94 >>> path(['hello', 'how'])
  95 path('hello/how')
  96 >>> path([path.ROOT, 'hello', 'how'])
  97 path('/hello/how')
  98 >>> path(['hello', path.ROOT, 'how'])
  99 Traceback (most recent call last):
 100 ...
 101 TypeError: Element path.ROOT is of a wrong type
 102 
 103 # Concatenation
 104 
 105 >>> path('hello/a') + path('b')
 106 path('hello/a/b')
 107 >>> path('hello/a') + 'b'
 108 path('hello/a/b')
 109 >>> path('hello/a') + 'b/c'
 110 path('hello/a/b/c')
 111 >>> 'b/c' + path('hello/a')
 112 path('b/c/hello/a')
 113 >>> 'b/c' + path('/hello/a')
 114 Traceback (most recent call last):
 115 ...
 116 ValueError: Right operand should be a relative path
 117 >>> path('hello/a') + '/b/c'
 118 Traceback (most recent call last):
 119 ...
 120 ValueError: Right operand should be a relative path
 121 
 122 # Slicing
 123 
 124 >>> p = path('/hello/a')
 125 >>> p[:2]
 126 path('/hello')
 127 >>> p[-1]
 128 'a'
 129 >>> p[:-1]
 130 path('/hello')
 131 
 132 # Multiplication
 133 
 134 >>> path('hello/a') * 3
 135 path('hello/a/hello/a/hello/a')
 136 >>> path('/hello/a') * 3
 137 Traceback (most recent call last):
 138 ...
 139 ValueError: Only relative paths can be multiplied
 140 
 141 >>> 3 * path('hello/a')
 142 path('hello/a/hello/a/hello/a')
 143 >>> 3 * path('/hello/a')
 144 Traceback (most recent call last):
 145 ...
 146 ValueError: Only relative paths can be multiplied
 147 
 148 # Comparison
 149 
 150 >>> L = ['/home/noam', '/home/allon', '/home/noam2', '/home/bbbb',
 151 ...      'home/bbbb', 'home/noam', 'home/noam2', 'home/allon', 'a/b', '/b/c']
 152 >>> L.extend([path(x) for x in L])
 153 >>> L.sort()
 154 >>> L
 155 ['/b/c', path('/b/c'), '/home/allon', path('/home/allon'), '/home/bbbb', path('/home/bbbb'), '/home/noam', path('/home/noam'), '/home/noam2', path('/home/noam2'), 'a/b', path('a/b'), 'home/allon', path('home/allon'), 'home/bbbb', path('home/bbbb'), 'home/noam', path('home/noam'), 'home/noam2', path('home/noam2')]
 156 
 157 
 158 
 159 # Matching
 160 
 161 >>> path('a/b').match('a/b')
 162 True
 163 >>> path('a/b').match('a/c')
 164 False
 165 >>> path('a/b').match('a')
 166 False
 167 >>> path('a/b').match('a/c*')
 168 False
 169 >>> path('a/b').match('a/b*')
 170 True
 171 >>> path('a/b').match('**')
 172 True
```
:::
::::
