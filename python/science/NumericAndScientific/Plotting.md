# NumericAndScientific/Plotting

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# Graphical Representations of Data 

Over the years many different plotting modules and packages have been developed for Python. For most of that time there was no clear favorite package, but recently matplotlib has become the most widely used. Nevertheless, many of the others are still available and may suit your tastes or needs better. Some of these are interfaces to existing plotting libraries while others are Python-centered new implementations.

## Image Processing and Analysis 

- The [PIL Toolkit](http://www.pythonware.com/downloads.htm#pil) provides a very powerful set of tools for manipulating images. [Documentation](http://www.pythonware.com/library/pil/handbook/index.htm)

- [PyQtGraph](http://www.pyqtgraph.org) is a pure-python graphics library built on [PyQt4](PyQt4) and numpy. It is intended for use in mathematics / scientific / engineering applications. The library provides widgets and graphicsItems for displaying / analyzing live image data (including 16-bit) as well as translate/scale/rotatable region-of-interest widgets for interactively slicing numpy arrays. The library is very fast due to its heavy leverage of numpy and Qt\'s graphicsView framework.

## Plotting Tools 

- [Matplotlib](http://matplotlib.sourceforge.net) is an Open Source plotting library designed to support interactive and publication quality plotting with a syntax familiar to Matlab users. Its interactive mode supports multiple windowing toolkits (currently: GTK, Tkinter, Qt, and wxWindows) as well as multiple noninteractive backends (PDF, postscript, SVG, antigrain geometry, and Cairo). Plots can be embedded within GUI applications or for non-interactive uses without any available display in batch mode. Matplotlib provides both a Matlab-like functional interface as well as an object oriented interface. [IPython](http://ipython.scipy.org) has a \"pylab\" mode which is specifically designed for interactive plotting with matplotlib.

- [Bokeh](http://bokeh.pydata.org/en/latest) is a [BSD licensed, open source](https://github.com/bokeh/bokeh) Python interactive visualization platform that targets modern web browsers for presentation. Bokeh can create [richly interactive](http://bokeh.pydata.org/en/latest/docs/user_guide/interaction.html) visualizations and data applications, as [standalone HTML documents](http://bokeh.pydata.org/en/latest/docs/gallery.html#standalone-examples), [sophisticated server-backed applications](http://bokeh.pydata.org/en/latest/docs/gallery.html#server-app-examples), or [inline in Jupyter Notebooks](http://nbviewer.jupyter.org/github/bokeh/bokeh-notebooks/blob/master/index.ipynb). Bokeh has an extensive [User\'s Guide](http://bokeh.pydata.org/en/latest/docs/user_guide.html) and other additional resources for learning:

  - [SciPy 2016 Tutorial video](https://www.youtube.com/watch?v=LXLQTuSSKfY) with related [Jupyter Notebooks](http://nbviewer.jupyter.org/github/bokeh/bokeh-notebooks/blob/master/tutorial/00%20-%20intro.ipynb)

  - Hosted example apps at [https://demo.bokeh.org](https://demo.bokeh.org)

  - Community supported [public mailing list](https://groups.google.com/a/continuum.io/forum/#!forum/bokeh), Twitter feed [\@BokehPlots](https://twitter.com/bokehplots)

  - [RBokeh](http://hafen.github.io/rbokeh/) for creating Bokeh visualizations from the R language

- [Backtesting.py](https://kernc.github.io/backtesting.py/) features a Bokeh-based framework for plotting OHLC & financial data.

- [Plotly](https://plot.ly) is a collaborative browser-based plotting and analytics platform. You can generate graphs and analyze data from the in-browser [Python sandbox](https://plot.ly/demo/script) (numpy supported) or the [Plotly API](https://plot.ly/api/python) (download [here](https://pypi.python.org/pypi/plotly/0.5)). Plotly supports [interactive graphs](http://nbviewer.ipython.org/github/plotly/IPython-plotly/tree/master/) with IPython notebooks. Graphs are interactive, can be styled with Python or the GUI, and [sharable by link](https://plot.ly/~jackp/614/). Scripts, graphs, and data can be shared, collaboratively edited, and stored and run in Plotly.

- [GR](http://gr-framework.org) is a universal framework for cross-platform visualization applications, ranging from publication quality 2D graphs to the representation of complex 3D scenes. GR provides both MATLAB-like convenience functions as well as a low-level functional interface. GR can be used in imperative programming systems or integrated into modern object-oriented systems, in particular those based on GUI toolkits (Qt, wxWidgets, Gtk) or interactive browser environments (Jupyter). GR can also be used as a backend for Matplotlib and speed up existing applications. The GR framework is especially suitable for real-time environments.

- [Veusz](http://home.gna.org/veusz/) is a GPL scientific plotting package written in Python and [PyQt](PyQt), designed to create publication-quality output. Graphs are built up from simple components, and the program features an integrated command-line, GUI and scripting interface. Veusz can also be embedded in other Python programs, even those not using [PyQt](PyQt).

- [Visvis](http://code.google.com/p/visvis/) is a pure Python library for visualization of 1D to 4D data in an object oriented way. Essentially, visvis is an object oriented layer of Python on top of [OpenGl](./OpenGl.html), thereby combining the power of [OpenGl](./OpenGl.html) with the usability of Python. A Matlab-like interface in the form of a set of functions allows easy creation of objects (e.g. plot(), imshow(), volshow(), surf()).

- [Chaco](http://code.enthought.com/projects/chaco/) is a device-independent 2D plotting package based on a DisplayPDF API. It supports **fast** vector graphics rendering for **interactive data analysis** (read: fast live updating plots) and custom plot construction. Chaco is easy to embed in python GUI applications (wxWindows, Qt) and provides nice abstractions for overlays and tools (select regions, zoom/pan, cross-hairs, labels, data inspectors, etc.). Chaco is able to output to any raster format supported by [PIL](http://www.pythonware.com/downloads.htm#pil), as well as PDF, [PostScript](PostScript) and SVG backends. See [the gallery](http://code.enthought.com/projects/chaco/gallery.php) for screenshots and code examples.

- [diaGrabber](./radjkarl(2e)github(2e)io(2f)diaGrabber.html) is based on [PyQtGraph](http://www.pyqtgraph.org/) and allows you to read, filter, process, interpolate and plot n-dimensional values from different sources (like libreOffice- or csv-files) and variable size. Through interactive reading it\'s also possible to evaluate streams in a kind of \'software-oscilloscope\'.

- [KonradHinsen](KonradHinsen) has some plotting support in his [ScientificPython](ScientificPython) package, for example [TkPlotCanvas](./TkPlotCanvas.html).

- Michael Haggerty has [a Gnuplot module](http://gnuplot-py.sourceforge.net/) that interfaces with [the GNUPLOT package](http://www.gnuplot.info).

- [plot_wrap](http://php.iupui.edu/~mmiller3/python/#plotwrap) A module by Mike Miller which wraps the functions in [the GNU plotutils](http://www.gnu.org/software/plotutils/plotutils.html) package.

- [BLT](http://www.tcltk.com/blt/) BLT is an extension to the tk widgets that can produce X/Y plots and bar charts. The BLT package can be used through [the Pmw package](http://pmw.sourceforge.net/), a framework for the creation of megawidgets built on top of Tkinter.

- [PyQwt](http://pyqwt.sourceforge.net/) is a set of Python bindings for the Qwt C++ class library which extends the Qt framework with widgets for scientific and engineering applications.

- [GUIQwt](http://pypi.python.org/pypi/guiqwt/) is a Python library based on Qwt providing efficient 2D data-plotting features (curve/image visualization and related tools) for interactive computing and signal/image processing application development.

- [DISLIN](http://www.linmpi.mpg.de/dislin/) DISLIN is a high-level and easy to use graphics library for displaying data as curves, bar graphs, pie charts, 3D-color plots, surfaces, contours and maps. The software is available for several C, Fortran 77 and Fortran 90 compilers. For some operation systems, the programming languages Python and Perl are also supported by DISLIN. DISLIN is free for the Linux and FreeBSD operating systems and for the MS-DOS and Windows 95/NT compilers GCC, G77 and ELF90. Other DISLIN versions are available at low prices and can be tested free of charge.

- [Mayavi](http://code.enthought.com/projects/mayavi/) Starting from Mayavi2, the 3D data visualization program Mayavi is fully scriptable from Python, can be integrated in larger applications, and exposes a simple pylab/matlab-like interface for plotting arrays.

- [gdmodule](http://newcenturycomputers.net/projects/gdmodule.html) GD is a graphics library for the creation of GIF pictures, written by Thomas Boutell. gdmodule is an Python extension for this library. It can do lines, arcs, fills, fonts and can also manipulate other GIF pictures. Included in the gdmodule is a graphing module, which can produce line plots from data.

- [Gist](ftp://ftp-icf.llnl.gov/pub/python) Extension to the gist graphics library, which is part of another numeric environment named \[[ftp://ftp-icf.llnl.gov/pub/Yorick](ftp://ftp-icf.llnl.gov/pub/Yorick) yorick\]. It can produce line, contour, surface plots on quadrilateral meshes. On top of the low-level interface the people from LLNL have build an object-oriented interface which can also do isosurface and 3D slicing plots together with light and script based animation. The interface is well documented. The package is now part of the LLNL Python distribution. Gist originally ran only under Unix-like operating systems. The latest source and a Windows installer are available from the [University of Tokyo](http://bonsai.ims.u-tokyo.ac.jp/~mdehoon/software/python/).

- [pgplot](http://www.astro.caltech.edu/~tjp/pgplot/) Extension to the pgplot graphics library, a portable, device independent graphics package for making simple scientific graphs. The library is intended for making graphical images of publication quality with minimum effort on the part of the user. All functions are directly callable from Python, through the use of SWIG for wrapper code generation. Pgplot has drivers for many different graphics formats and devices, although there are problems with the MS-Windows driver.

- [Py-OpenDX](http://people.freebsd.org/~rhh/py-opendx/index.html) OpenDX is the open-source version of the IBM Data Explorer (DX). DX is a visualization system providing a full set of tools for manipulating, rendering and animating data, especially 3D data from simulations or acquired from observations. It provides a GUI, a scripting interface and the API C libraries. Py-OpenDX is a Python binding for the OpenDX API. Currently only the DXLink library is wrapped. That wrapper allows one to start up a DX executive and communicate with it via the DXL API.

- [VTK](http://public.kitware.com/VTK/) VTK is an OO-framework for visualisation, written in C++ with bindings to TCL, Python and Java. It\'s not really a plotting package, but a visualisation system, where one needs to program to get a picture. It\'s very huge and resource demanding and best used on hardware with good graphics performance. It uses mainly OpenGL for rendering, so it can not produce vector graphics or high quality postscript output. Besides of that VTK is very powerful and can produce really great views of your data.

- [RPy](http://rpy.sourceforge.net/) \-- a Python interface to [the R programming language](http://www.r-project.org). R is a large, robust package for doing math and statistics; it includes many, many graphing options.

- [R/SPlus Python Interface](http://www.omegahat.org/RSPython/). Another R interface. Currently it allows Python code to call [R](http://www.r-project.org/) functions, and write R code to create Python objects and call Python functions and methods. This allows Python programmers unfamiliar with the syntax of R to easily use its functionality.

- [PyX](http://pyx.sourceforge.net) is a library for creating figures in Postscript and PDF, which uses TeX/LaTeX for the text output.

- [Biggles](http://biggles.sourceforge.net/) is another plotting library that supports multiple output formats, as is [Piddle](http://piddle.sourceforge.net/).

- [Pychart](http://home.gna.org/pychart/) is a library for creating EPS, PDF, PNG, and SVG charts. It supports line plots, bar plots, range-fill plots, and pie charts.

- [PyNGL](http://www.pyngl.ucar.edu/) is a Python interface to the high quality 2D scientific visualizations in the [NCAR Command Language](http://www.ncl.ucar.edu) (NCL).

- [pygooglechart](http://pygooglechart.slowchop.com/) is a Python interface to the [Google Chart API](http://code.google.com/apis/chart/).

- [WHIFF](http://whiff.sourceforge.net/) includes built in support for generating Adobe Flash chart widgets using either the amCharts charting package or the Open Flash Chart package. The generated charts may be embedded in dynamic web pages.

- [PyQtGraph](http://www.pyqtgraph.org) is a pure-python graphics library built on [PyQt4](PyQt4) and numpy. It is intended for use in mathematics / scientific / engineering applications. The library is very fast due to its heavy leverage of numpy and Qt\'s graphicsView framework. Major features: 1) a feature-rich plotting system, and 2) an image display system with translate/scale/rotatable region-of-interest widgets.

- [sambo.plot](https://sambo-optimization.github.io/doc/sambo/plot.html) module from [SAMBO](https://sambo-optimization.github.io) includes functions for plotting n-d partial dependence, convergence, regret, and sequence of evaluations in global optimization.

- [pyla](http://pyla.codeplex.com) is a set of pure-python 3 (3.x) libraries for 2D/3D plotting using Gnuplot, linear algebra (vector-matrix) operation, ode (ordinary differential equation) solvers, optimization and nonlinear algebraic equation solvers. It is in alpha release and its gplot library has been released. pyla-gplot is a very simple yet powerful library very similar to [Gnuplot.py](http://gnuplot-py.sourceforge.net/) but works under python 3.x and does not require Numpy.

- [cartesius](http://tkrajina.github.com/cartesius/) is a small library for 2d coordinate system images.

## Also of Note 

- There is an interface to the OpenGL library called [PyOpenGL](http://starship.python.net/~da/PyOpenGL/) that can be used to write sophisticated visualization tools from scratch.

- The [FXPy](http://fxpy.sourceforge.net/) bindings to [the FOX GUI library](http://www.cfdrc.com/FOX/fox.html) support OpenGL, so might be a good starting point for new applications.
