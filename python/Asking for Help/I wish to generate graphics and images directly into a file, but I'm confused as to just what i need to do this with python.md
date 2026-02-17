# Asking for Help/I wish to generate graphics and images directly into a file, but I'm confused as to just what i need to do this with python

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# How to generate graphics and write the image directly to a file 

Have a look at the [GraphicsAndImages](GraphicsAndImages) page. It depends somewhat on the kind of graphics you want to produce: some libraries like [matplotlib](http://matplotlib.sourceforge.net/) are focused on graphs and charts, whereas the [PythonImagingLibrary](PythonImagingLibrary) supports both bitmap manipulation as well as line and shape drawing (and other similar operations) using the ImageDraw module.

Many on-screen graphics packages also support drawing onto and the saving of bitmaps (eg. [PyGame](PyGame)), and it is possible to draw to off-screen bitmaps or devices in various graphical user interface toolkits and frameworks - see [GuiProgramming](GuiProgramming) for details of the different choices.

An example of printing some off-screen picture using [PyQt](PyQt) (rather than writing a file, although the principles are the same) can be found in the following message: [\"Placing graphics & text on printed page - jan06call.jpg (0/1)\"](http://groups.google.com/group/comp.lang.python/msg/a4514729bc3430a1). \-- [PaulBoddie](PaulBoddie)

------------------------------------------------------------------------

[CategoryAskingForHelp](CategoryAskingForHelp) [CategoryAskingForHelpAnswered](CategoryAskingForHelpAnswered)
