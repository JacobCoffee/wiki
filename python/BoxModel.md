# BoxModel

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

**Box Model** refers to something like [the W3C CSS box model.](http://www.w3.org/TR/CSS21/box.html)

- Names for coordinates.
- Names for widths and heights.
- Padding, Border, Margin, top-right-bottom-left.

There are applications in *visualization* and *user interface* development.

Ideal:

- Compute X-Y coordinates for different points on the box model.
- Allow for naming the different points of the box model.
- Support different layout methods: absolute positioning, positioning by traits (padding, border, margin, contents), positioning by tensions, horizontal or vertical or grid or absolute positioning of interior contents, and so on.

Is there anything *easily reusable* in Python that presently does this sort of work?

(Perhaps [WxPython](WxPython) can be (ab)used for this purpose..? Can you do all the size calculations, without ever rendering anything, or initializing wx?)

## Example 

Here\'s some Python code that can track horizontal layouts.

That is, as long as you nest cells *horizontally,* everything works out and gets calculated.

:::: 
::: 
``` 
   1 class Rect:
   2     def __init__(self, size=0):
   3         if hasattr(size, "__int__"):
   4             (t, r, b, l) = map(int, [size]*4)
   5         elif hasattr(size, "__len__") and len(size) == 4:
   6             (t, r, b, l) = size
   7         else:
   8             raise ValueError(size)
   9         (self.top, self.right, self.bottom, self.left) = (t,r,b,l)
  10     def width(self):
  11         return self.left + self.right
  12     def height(self):
  13         return self.top + self.bottom
  14 
  15 class Cell:
  16     def __init__(self, children=[], padding=0, border=0, margin=0):
  17         self.children = children  # spatially arranged left-to-right
  18         self.padding = Rect(padding)
  19         self.border = Rect(border)
  20         self.margin = Rect(margin)
  21     def parts(self):
  22         return self.children + [self.padding, self.border, self.margin]
  23     def width(self):
  24         return sum([x.width() for x in self.parts()])
  25     def height(self):
  26         return sum([x.height() for x in self.parts()])
  27     def top(self):
  28         return sum([x.top for x in [self.margin, self.border, self.padding]])
  29     def right(self):
  30         return sum([x.right for x in [self.padding, self.border, self.margin]])
  31     def bottom(self):
  32         sum([x.bottom for x in [self.padding, self.border, self.margin]])
  33     def left(self):
  34         return sum([x.left for x in [self.margin, self.border, self.padding]])
  35     def children_height(self):
  36         if len(self.children) == 0:
  37             return 0
  38         return max([x.height() for x in self.children])
  39     def children_width(self):
  40         return sum([x.width() for x in self.children])
  41 
  42 def blank(width, height, border=0, margin=0):
  43     v = (height*1.0) / 2  # vertical
  44     h = (width*1.0) / 2  # horizontal
  45     b = Cell(padding=[v, h, v, h], border=border, margin=margin)
  46     return b
  47 
  48 def progressive_count(N):
  49     return [range(x+1) for x in range(0, N)]
  50 
  51 def indexes_from(L, indexes):
  52     return [L[i] for i in indexes]
  53 
  54 def progressive_lists(L):
  55     return [indexes_from(L, indexes) for indexes in progressive_count(len(L))]
  56 
  57 def progressive_sums(L):
  58     return map(sum, progressive_lists(L))
  59 
  60 def call_with_coordinates(func, cell, x=0, y=0):
  61     x_coords = progressive_sums([cell.left()] + [child.width() for child in cell.children] + [cell.right()])
  62     y_coords = [cell.top()] * len(cell.children)
  63     coords = zip(x_coords[0:-2], y_coords)
  64     
  65     return [func(cell, x, y),
  66             [call_with_coordinates(func, child, x+mx, y+my) for
  67              (child, (mx, my)) in zip(cell.children, coords)]]
  68 
  69 
  70 def report(cell, x, y):
  71     return "cell upper-left at (%s, %s)" % (x,y)
  72 
  73 call_with_coordinates(report, Cell([blank(3,3), blank(3,3)], margin=[2,4,2,4]))
  74 
  75 call_with_coordinates(report, Cell([blank(4, 2), blank(4, 2), blank(4, 2)], padding=2, border=1))
```
:::
::::
