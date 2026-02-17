# BytesIO

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

This class is like `StringIO`{.backtick} for `bytes`{.backtick} objects. There are a few notes at the bottom.

*In Python 2.6, 2.7 and 3.x, the io module provides a standard BytesIO class.*

This is a toy implementation. Known holes are marked with `XXX`{.backtick} comments.

:::: 
::: 
``` 
   1 class BytesIO(object):
   2     """ A file-like API for reading and writing bytes objects.
   3 
   4     Mostly like StringIO, but write() calls modify the underlying
   5     bytes object.
   6 
   7     >>> b = bytes()
   8     >>> f = BytesIO(b, 'w')
   9     >>> f.write(bytes.fromhex('ca fe ba be'))
  10     >>> f.write(bytes.fromhex('57 41 56 45'))
  11     >>> b
  12     bytes([202, 254, 186, 190, 87, 65, 86, 69])
  13     """
  14 
  15     def __init__(self, buf, mode='r'):
  16         """ Create a new BytesIO for reading or writing the given buffer.
  17 
  18         buf - Back-end buffer for this BytesIO.  A bytes object.
  19             Actually, anything that supports len(), slice-assignment,
  20             and += will work.
  21         mode - One of 'r', 'w', 'a'.
  22             An optional 'b' is also allowed, but it doesn't do anything.
  23         """
  24         # XXX many 'mode' possibilities aren't allowed yet: 'rw+Ut'
  25         if len(mode) == 2 and mode[-1] == 'b':
  26             mode = mode[:-1]  # binary mode goes without saying
  27         if mode not in ('r', 'w', 'a'):
  28             raise ValueError("mode must be 'r', 'w', or 'a'")
  29 
  30         self._buf = buf
  31         self.mode = mode
  32         self.closed = False
  33         if self.mode == 'w':
  34             del buf[:]
  35             self._point = 0
  36         elif self.mode == 'r':
  37             self._point = 0
  38         else: # 'a'
  39             self._point = len(buf)
  40 
  41     def close(self):
  42         self.closed = True
  43 
  44     def _check_closed(self):
  45         if self.closed:
  46             raise ValueError("file is closed")
  47 
  48     def flush(self):
  49         self._check_closed()
  50 
  51     def next(self):
  52         line = self.readline()
  53         if len(line) == 0:
  54             raise StopIteration
  55         return line
  56 
  57     def read(self, size=None):
  58         self._check_closed()
  59         if size is None:
  60             e = len(self._buf)
  61         else:
  62             e = min(self._point + size, len(self._buf))
  63         r = self._buf[self._point:e]
  64         self._point = e
  65         return r
  66 
  67     def readline(self, size=None):
  68         self._check_closed()
  69         die  # XXX TODO - assume ascii and read a line
  70 
  71     def readlines(self, sizehint=None):
  72         # XXX TODO handle sizehint
  73         return list(self)
  74 
  75     def seek(self, offset, whence=0):
  76         self._check_closed()
  77 
  78         if whence == 0:
  79             self._point = offset
  80         elif whence == 1:
  81             self._point += offset
  82         elif whence == 2:
  83             self._point = len(self._buf) + offset
  84         else:
  85             raise ValueError("whence must be 0, 1, or 2")
  86 
  87         if self._point < 0:
  88             self._point = 0  # XXX is this right?
  89 
  90     def tell(self):
  91         self._check_closed()
  92         return self._point
  93 
  94     def truncate(self, size=None):
  95         self._check_closed()
  96         if size is None:
  97             size = self.tell()
  98         del self._buf[size:]
  99 
 100     def write(self, data):
 101         self._check_closed()
 102         amt = len(data)
 103         size = len(self._buf)
 104         if self.mode == 'a':
 105             self._point = size
 106 
 107         if self._point > size:
 108             if isinstance(b, bytes):
 109                 blank = bytes([0])
 110             else:
 111                 # Don't know what default value to insert, unfortunately
 112                 raise ValueError("can't write past the end of this object")
 113             self._buf += blank * (self._point - size) + data
 114             self._point = len(self._buf)
 115         else:
 116             p = self._point
 117             self._buf[p:p + amt] = data
 118             self._point = min(p + amt, len(self._buf))
 119 
 120     def writelines(self, seq):
 121         for line in seq:
 122             self.write(line)
 123 
 124     def __iter__(self):
 125         return self
 126 
 127     @property
 128     def name(self):
 129         return repr(self)
```
:::
::::

### Notes 

You\'ll need the toy `bytes`{.backtick} implementation if you want to try this out. If you\'re in an extreme hurry you can just use this (not quite perfect):

:::: 
::: 
``` 
   1 import array
   2 def bytes(seq=()):
   3     return array.array('B', seq)
```
:::
::::

There is no `BytesIO.getvalue()`{.backtick} method because it\'s not needed. Instead, just keep a reference to the underlying buffer.

This works with lists and arrays, as well as bytes objects, but it\'s sort of a coincidence, rather than an actual design goal\...
