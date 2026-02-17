# PyGdModule

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

GD module is an interface to the GD library written by Thomas Bouttel.

gd is a graphics library. It allows your code to quickly draw images complete with lines, arcs, text, multiple colors, cut and paste from other images, and flood fills, and write out the result as a PNG or JPEG file. This is particularly useful in World Wide Web applications, where PNG and JPEG are two of the formats accepted for inline images by most browsers.

GD module [homepage](http://newcenturycomputers.net/projects/gdmodule.html)

------------------------------------------------------------------------

Chris Gonnerman writes:

I am the current maintainer of the Python gdmodule. I took it over because I needed to annotate graphic images using [TrueType](./TrueType.html) fonts. The PIL ([PythonImagingLibrary](PythonImagingLibrary)) is probably superior otherwise, but the font support stinks.

There are two other projects, claimed to be PIL-compatible, one supporting [FreeType](./FreeType.html) ([TrueType](./TrueType.html)) and the other supporting Postscript Type 1; but when I asked here previously for examples and/or support using either of them I got resounding silence.

PIL can be found at [http://www.pythonware.com/products/pil/index.htm](http://www.pythonware.com/products/pil/index.htm)

The Image-SIG\'s t1python module is at [http://www.python.org/sigs/image-sig/t1lib/](http://www.python.org/sigs/image-sig/t1lib/) (Incidentally this may have been updated since I first looked at it, so my complaints here may no longer apply.)

Robert Kern\'s PyFT can be found at [http://starship.python.net/crew/kernr/Projects.html](http://starship.python.net/crew/kernr/Projects.html)

PIL Plus from Pythonware includes [TrueType](./TrueType.html) support (I\'ve read) but as a commercial product it was not an option for my project.

I looked for the gdmodule, and discovered Richard Jones wasn\'t supporting it anymore. When I asked about taking it over, he answered \"Sure, go ahead.\"

So I did. With help from others I have updated it to support the 2.01 (beta) libgd. There are weaknesses, in particular the terrible JPEG output (rule 1: always use PNG with the gdmodule), but at least all my TTF fonts work.

gdmodule also has a very simple interface; I don\'t have to know as much about an image file to work with it. This may be related to the crummy JPEG output\... I dunno.

I\'d love to see sample code to render either type of fonts via PIL and one or more of the above libraries. In fact, it seems like an ideal thing for a HOWTO or some such.
