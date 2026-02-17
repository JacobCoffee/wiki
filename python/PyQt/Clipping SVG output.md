# PyQt/Clipping SVG output

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# Clipping SVG output 

In a [message to the qt-interest mailing list](http://lists.trolltech.com/pipermail/qt-interest/2009-September/012599.html), Jeremy Sanders asked if it was possible to clip polylines before sending them to a paint device. This was partly to overcome the limitations of Qt\'s SVG paint device, QSvgGenerator, which doesn\'t support clipping.

![svg_output.png](attachments/PyQt(2f)Clipping(20)SVG(20)output/svg_output.png "svg_output.png")

The following example code shows how to clip painter output when generating an SVG, using a QPainterPath as a stencil by passing the painter paths to be rendered to its QPainterPath.intersected() method and drawing the result. Note that this only works for pens with zero width.

:::: 
::: 
``` 
   1 import random, sys
   2 from PyQt4.QtCore import QSize, Qt
   3 from PyQt4.QtGui import *
   4 from PyQt4.QtSvg import *
   5 
   6 def randomColor():
   7 
   8     red = 205 + random.random() * 50
   9     green = 205 + random.random() * 50
  10     blue = 205 + random.random() * 50
  11     alpha = 91 + random.random() * 100
  12 
  13     return QColor(red, green, blue, alpha)
  14 
  15 
  16 if __name__ == "__main__":
  17 
  18     if len(sys.argv) != 2:
  19     
  20         sys.stderr.write("Usage: %s <output path>\n" % sys.argv[0])
  21         sys.exit(1)
  22     
  23     app = QApplication(sys.argv)
  24     
  25     svg = QSvgGenerator()
  26     svg.setFileName(sys.argv[1])
  27     svg.setResolution(300)
  28     svg.setSize(QSize(1024, 768))
  29     
  30     random.seed()
  31     
  32     p = QPainter()
  33     p.begin(svg)
  34     
  35     clipPath = QPainterPath()
  36     clipPath.addRect(0, 0, 1024, 768)
  37     
  38     gradient = QLinearGradient(0, 0, 1024, 768)
  39     gradient.setColorAt(0, QColor(0, 64, 64))
  40     gradient.setColorAt(1, QColor(0, 0, 64))
  41     p.fillRect(0, 0, 1024, 768, QBrush(gradient))
  42     p.setPen(Qt.NoPen)
  43     
  44     font = QFont("FreeSans")
  45     
  46     for i in range(100):
  47     
  48         w = 10 + random.random() * 200.0
  49         h = 0.5 * (1 + random.random()) * w
  50         color = randomColor()
  51         x = random.random() * 1024
  52         y = random.random() * 768
  53         
  54         rectPath = QPainterPath()
  55         rectPath.addRoundedRect(x - w/2, y - h/2, w, h, 20, 20)
  56         
  57         p.setBrush(color)
  58         p.drawPath(clipPath.intersected(rectPath))
  59         
  60         font.setPixelSize(min(w/2, h/2))
  61         metrics = QFontMetrics(font, svg)
  62         text = chr(random.randrange(97, 123))
  63         rect = metrics.boundingRect(x - w/2, y - h/2, w, h, Qt.AlignCenter, text)
  64         textPath = QPainterPath()
  65         textPath.addText(x - rect.width()/2, y + rect.height()/2 - metrics.descent(), font, text)
  66         
  67         p.setBrush(QColor(0, 0, 0, color.alpha()))
  68         p.drawPath(clipPath.intersected(textPath))
  69     
  70     p.end()
  71     
  72     sys.exit()
```
:::
::::

One way to deal with non-zero-width pens is to use QPainterPathStroker. This creates an outline of a painter path, converting pen strokes to fillable paths. We can use this to create paths which we can then effectively clip using the stencil path.

![svg_output_stroked.png](attachments/PyQt(2f)Clipping(20)SVG(20)output/svg_output_stroked.png "svg_output_stroked.png")

:::: 
::: 
``` 
   1 import random, sys
   2 from PyQt4.QtCore import QSize, Qt
   3 from PyQt4.QtGui import *
   4 from PyQt4.QtSvg import *
   5 
   6 def randomColor():
   7 
   8     red = 205 + random.random() * 50
   9     green = 205 + random.random() * 50
  10     blue = 205 + random.random() * 50
  11     alpha = 91 + random.random() * 100
  12     
  13     return QColor(red, green, blue, alpha)
  14 
  15 
  16 if __name__ == "__main__":
  17 
  18     if len(sys.argv) != 2:
  19     
  20         sys.stderr.write("Usage: %s <output path>\n" % sys.argv[0])
  21         sys.exit(1)
  22     
  23     app = QApplication(sys.argv)
  24     
  25     svg = QSvgGenerator()
  26     svg.setFileName(sys.argv[1])
  27     svg.setResolution(300)
  28     svg.setSize(QSize(1024, 768))
  29     
  30     random.seed()
  31     
  32     p = QPainter()
  33     p.begin(svg)
  34     
  35     clipPath = QPainterPath()
  36     clipPath.addRect(0, 0, 1024, 768)
  37     
  38     stroker = QPainterPathStroker()
  39     stroker.setWidth(16)
  40     stroker.setDashPattern([0.1, 1.5])
  41     
  42     gradient = QLinearGradient(0, 0, 1024, 768)
  43     gradient.setColorAt(0, QColor(0, 64, 64))
  44     gradient.setColorAt(1, QColor(0, 0, 64))
  45     p.fillRect(0, 0, 1024, 768, QBrush(gradient))
  46     p.setPen(Qt.NoPen)
  47     
  48     font = QFont("FreeSans")
  49     strokeColor = QColor(0, 127, 255)
  50     
  51     for i in range(100):
  52     
  53         w = 10 + random.random() * 200.0
  54         h = 0.5 * (1 + random.random()) * w
  55         color = randomColor()
  56         x = random.random() * 1024
  57         y = random.random() * 768
  58         
  59         rectPath = QPainterPath()
  60         rectPath.addRoundedRect(x - w/2, y - h/2, w, h, 20, 20)
  61         
  62         strokedPath = stroker.createStroke(rectPath)
  63         
  64         # Draw the background of the rounded rectangle.
  65         p.setBrush(color)
  66         p.drawPath(clipPath.intersected(rectPath))
  67         # Draw the outline of the rounded rectangle.
  68         p.setBrush(strokeColor)
  69         p.drawPath(clipPath.intersected(strokedPath))
  70         
  71         font.setPixelSize(min(w/2, h/2))
  72         metrics = QFontMetrics(font, svg)
  73         text = chr(random.randrange(97, 123))
  74         rect = metrics.boundingRect(x - w/2, y - h/2, w, h, Qt.AlignCenter, text)
  75         textPath = QPainterPath()
  76         textPath.addText(x - rect.width()/2, y + rect.height()/2 - metrics.descent(), font, text)
  77         
  78         p.setBrush(QColor(0, 0, 0, color.alpha()))
  79         p.drawPath(clipPath.intersected(textPath))
  80     
  81     p.end()
  82     
  83     sys.exit()
```
:::
::::
