# PyChart

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

PyChart is a Python library for creating high quality Encapsulated Postscript, PDF, PNG, or SVG charts. It currently supports line plots, bar plots, range-fill plots, and pie charts.

Here\'s a quick example of using PyChart in a CGI script to dynamically create and return a plot in PNG format. Just copy/paste the following code into a file (say, generate_plot.py), set permissions to 755, drop it into your cgi-bin directory, and point your browser at it. (Please see the official PyChart docs for plenty of nicely-commented examples.)

:::: 
::: 
``` 
   1 #!/usr/bin/python
   2 
   3 import random
   4 import sys
   5 
   6 # Not using the cgi module at the moment.
   7 #import cgi
   8 #import cgitb; cgitb.enable()
   9 
  10 from pychart import *
  11 
  12 print "Content-type: image/png"
  13 print
  14 
  15 sys.argv.append( '--format=png' )
  16 
  17 theme.get_options()
  18 theme.scale_factor = 2
  19 theme.reinitialize()
  20 
  21 data = []
  22 for i in range(10):
  23     data.append( (i, random.random()* 3.0) )
  24 
  25 xaxis = axis.X( format="/hL%d",  label="time" )
  26 yaxis = axis.Y(  label="synaptic activity" )
  27 
  28 ar = area.T( x_axis=xaxis, y_axis=yaxis, y_range=(0,None), size=(120,110) )
  29 plot = line_plot.T( label="cortex data", data=data, ycol=1, tick_mark=tick_mark.square )
  30 ar.add_plot( plot )
  31 
  32 ar.draw()
```
:::
::::

You could place a link to this CGI script directly in your html, like so: `<img src="cgi-bin/generate_plot.py">`{.backtick}. If you used the cgi module in the above script, you could parse URL-encoded values and generate an image based on what the browser asked for, say: `<img src="cgi-bin/generate_image.py?plot_type=disk_usage">`{.backtick}.

[http://home.gna.org/pychart/](http://home.gna.org/pychart/) (new)
