# PointsAndRectangles

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# Points & Rectangles 

A pair of classes to provide points and rectangles.

Surprisingly, I haven\'t been able to find a single Python module providing such primitive support.

[WxPython](WxPython) supports wxPoint and wxRect, but it lacks many basic functions (such as, say, adding two points together to produce a third point..!) (See: [wxPyWiki:wx.Rect](http://wiki.wxpython.org/index.cgi/wx_2eRect))

This code is lacking a zillion essential features (but interpoint distance can now be calculated). I only put in the ones I needed immediately. Please add, refactor, optimize, rename stuff to be more standard, etc., as you see fit..!

*If there\'s an actual, accessible, easy-to-include Python module, not tied to a graphics library, that does this stuff already, please write about it here! No sense in reinventing the wheel. I\'ve looked, but haven\'t found one. Hence this.*

:::: 
::: 
``` 
   1 """Point and Rectangle classes.
   2 
   3 This code is in the public domain.
   4 
   5 Point  -- point with (x,y) coordinates
   6 Rect  -- two points, forming a rectangle
   7 """
   8 
   9 import math
  10 
  11 
  12 class Point:
  13     
  14     """A point identified by (x,y) coordinates.
  15     
  16     supports: +, -, *, /, str, repr
  17     
  18     length  -- calculate length of vector to point from origin
  19     distance_to  -- calculate distance between two points
  20     as_tuple  -- construct tuple (x,y)
  21     clone  -- construct a duplicate
  22     integerize  -- convert x & y to integers
  23     floatize  -- convert x & y to floats
  24     move_to  -- reset x & y
  25     slide  -- move (in place) +dx, +dy, as spec'd by point
  26     slide_xy  -- move (in place) +dx, +dy
  27     rotate  -- rotate around the origin
  28     rotate_about  -- rotate around another point
  29     """
  30     
  31     def __init__(self, x=0.0, y=0.0):
  32         self.x = x
  33         self.y = y
  34     
  35     def __add__(self, p):
  36         """Point(x1+x2, y1+y2)"""
  37         return Point(self.x+p.x, self.y+p.y)
  38     
  39     def __sub__(self, p):
  40         """Point(x1-x2, y1-y2)"""
  41         return Point(self.x-p.x, self.y-p.y)
  42     
  43     def __mul__( self, scalar ):
  44         """Point(x1*x2, y1*y2)"""
  45         return Point(self.x*scalar, self.y*scalar)
  46     
  47     def __div__(self, scalar):
  48         """Point(x1/x2, y1/y2)"""
  49         return Point(self.x/scalar, self.y/scalar)
  50     
  51     def __str__(self):
  52         return "(%s, %s)" % (self.x, self.y)
  53     
  54     def __repr__(self):
  55         return "%s(%r, %r)" % (self.__class__.__name__, self.x, self.y)
  56     
  57     def length(self):
  58         return math.sqrt(self.x**2 + self.y**2)
  59     
  60     def distance_to(self, p):
  61         """Calculate the distance between two points."""
  62         return (self - p).length()
  63     
  64     def as_tuple(self):
  65         """(x, y)"""
  66         return (self.x, self.y)
  67     
  68     def clone(self):
  69         """Return a full copy of this point."""
  70         return Point(self.x, self.y)
  71     
  72     def integerize(self):
  73         """Convert co-ordinate values to integers."""
  74         self.x = int(self.x)
  75         self.y = int(self.y)
  76     
  77     def floatize(self):
  78         """Convert co-ordinate values to floats."""
  79         self.x = float(self.x)
  80         self.y = float(self.y)
  81     
  82     def move_to(self, x, y):
  83         """Reset x & y coordinates."""
  84         self.x = x
  85         self.y = y
  86     
  87     def slide(self, p):
  88         '''Move to new (x+dx,y+dy).
  89         
  90         Can anyone think up a better name for this function?
  91         slide? shift? delta? move_by?
  92         '''
  93         self.x = self.x + p.x
  94         self.y = self.y + p.y
  95     
  96     def slide_xy(self, dx, dy):
  97         '''Move to new (x+dx,y+dy).
  98         
  99         Can anyone think up a better name for this function?
 100         slide? shift? delta? move_by?
 101         '''
 102         self.x = self.x + dx
 103         self.y = self.y + dy
 104     
 105     def rotate(self, rad):
 106         """Rotate counter-clockwise by rad radians.
 107         
 108         Positive y goes *up,* as in traditional mathematics.
 109         
 110         Interestingly, you can use this in y-down computer graphics, if
 111         you just remember that it turns clockwise, rather than
 112         counter-clockwise.
 113         
 114         The new position is returned as a new Point.
 115         """
 116         s, c = [f(rad) for f in (math.sin, math.cos)]
 117         x, y = (c*self.x - s*self.y, s*self.x + c*self.y)
 118         return Point(x,y)
 119     
 120     def rotate_about(self, p, theta):
 121         """Rotate counter-clockwise around a point, by theta degrees.
 122         
 123         Positive y goes *up,* as in traditional mathematics.
 124         
 125         The new position is returned as a new Point.
 126         """
 127         result = self.clone()
 128         result.slide(-p.x, -p.y)
 129         result.rotate(theta)
 130         result.slide(p.x, p.y)
 131         return result
 132 
 133 
 134 class Rect:
 135 
 136     """A rectangle identified by two points.
 137 
 138     The rectangle stores left, top, right, and bottom values.
 139 
 140     Coordinates are based on screen coordinates.
 141 
 142     origin                               top
 143        +-----> x increases                |
 144        |                           left  -+-  right
 145        v                                  |
 146     y increases                         bottom
 147 
 148     set_points  -- reset rectangle coordinates
 149     contains  -- is a point inside?
 150     overlaps  -- does a rectangle overlap?
 151     top_left  -- get top-left corner
 152     bottom_right  -- get bottom-right corner
 153     expanded_by  -- grow (or shrink)
 154     """
 155 
 156     def __init__(self, pt1, pt2):
 157         """Initialize a rectangle from two points."""
 158         self.set_points(pt1, pt2)
 159 
 160     def set_points(self, pt1, pt2):
 161         """Reset the rectangle coordinates."""
 162         (x1, y1) = pt1.as_tuple()
 163         (x2, y2) = pt2.as_tuple()
 164         self.left = min(x1, x2)
 165         self.top = min(y1, y2)
 166         self.right = max(x1, x2)
 167         self.bottom = max(y1, y2)
 168 
 169     def contains(self, pt):
 170         """Return true if a point is inside the rectangle."""
 171         x,y = pt.as_tuple()
 172         return (self.left <= x <= self.right and
 173                 self.top <= y <= self.bottom)
 174 
 175     def overlaps(self, other):
 176         """Return true if a rectangle overlaps this rectangle."""
 177         return (self.right > other.left and self.left < other.right and
 178                 self.top < other.bottom and self.bottom > other.top)
 179     
 180     def top_left(self):
 181         """Return the top-left corner as a Point."""
 182         return Point(self.left, self.top)
 183     
 184     def bottom_right(self):
 185         """Return the bottom-right corner as a Point."""
 186         return Point(self.right, self.bottom)
 187     
 188     def expanded_by(self, n):
 189         """Return a rectangle with extended borders.
 190 
 191         Create a new rectangle that is wider and taller than the
 192         immediate one. All sides are extended by "n" points.
 193         """
 194         p1 = Point(self.left-n, self.top-n)
 195         p2 = Point(self.right+n, self.bottom+n)
 196         return Rect(p1, p2)
 197     
 198     def __str__( self ):
 199         return "<Rect (%s,%s)-(%s,%s)>" % (self.left,self.top,
 200                                            self.right,self.bottom)
 201     
 202     def __repr__(self):
 203         return "%s(%r, %r)" % (self.__class__.__name__,
 204                                Point(self.left, self.top),
 205                                Point(self.right, self.bottom))
```
:::
::::

## Historical Note 

It seems that [Python version 1.0.2](http://www.informatik.hu-berlin.de/Themen/manuals/python/python-texinfo/top.html) had [standard module](http://www.informatik.hu-berlin.de/Themen/manuals/python/python-texinfo/module_index.html) [rect!](http://www.informatik.hu-berlin.de/Themen/manuals/python/python-texinfo/rect.html)

## See Also 

- [Wikipedia:Cartesian coordinate system](http://en.wikipedia.org/wiki/Cartesian_coordinate_system)

- [Wikipedia:Vector](http://en.wikipedia.org/wiki/Vector_%28spatial%29)
