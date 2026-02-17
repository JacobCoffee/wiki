# PyQt/Multimedia_Resources

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# Multimedia Resources 

There seem to be a few cross-platform resources for playing video and decoding movies, some of which are available in Python. It might be worthwhile trying to create wrappers for some of the more interesting projects.

## Non-Python Resources 

The [avifile](http://avifile.sourceforge.net/) project provides a Qt 3-based player on Linux, and would seem to be a reasonable candidate for a [PyQt](PyQt) wrapper. However, there doesn\'t seem to be much documentation for it outside the header files, but it might be possible to create a reasonably high-level wrapper using SIP, and at least we know it will work with Qt\'s event loop.

[FFmpeg](http://ffmpeg.mplayerhq.hu/) provides a set of tools and libraries that could be used to play and manipulate video.

## Python Resources 

- [PyMedia](http://pymedia.org/) is a Python package that supports various audio and video formats.

- In [a message](http://www.riverbankcomputing.com/pipermail/pyqt/2009-September/024240.html) to [the PyQt mailing list](TheMailingList), Baz Walter gives an example of using GStreamer bindings for Python with PyQt (see [Using GStreamer with PyQt](Using GStreamer with PyQt)).

## Out of Process Wrappers 

Henning Schröder posted a link to his PyQt (Qt 3) MPlayer wrapper widget in [a message](http://www.riverbankcomputing.com/pipermail/pyqt/2007-June/016277.html) to [the mailing list](./TheMailingList.html). He has kindly donated the code to the community, and it can also be obtained from the [MPlayerWidget](Multimedia_Resources/MPlayerWidget) page.
