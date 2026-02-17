# PyFltk

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# pyFLTK: Multi Platform GUI Toolkit 

pyFLTK is a Python wrapper for the [FLTK](FLTK) GUI toolkit. It utilizes SWIG and wraps the current stable version of FLTK.

## GNU/Linux install tips 

These notes assume you\'re using Ubuntu GNU/Linux, your system Python (the one installed in `/usr/bin`{.backtick}), and your system OpenGL libraries. And that you\'ll be *manually* installing FLTK and pyFLTK.

### OpenGL 

Before installing FLTK, be sure you have OpenGL and its development libraries installed on your system. On Ubuntu 8.10, using a DRI-compatible card, some of these packages are:

    libgl1-mesa-dri libgl1-mesa-dev mesa-common-dev libglu1-mesa libglu1-mesa-dev freeglut3 freeglut3-dev

`aptitude install`{.backtick} any that you don\'t already have installed.

### FLTK 

The current stable release as of Jan 2009 is 1.1.9. Building and installing (into `/usr/local`{.backtick}) should be a simple matter of running `make`{.backtick} and then `sudo make install`{.backtick}. See its README for more details.

You want to build and install your own because the stock FLTK that\'s available with Ubuntu 8.10 is not configured to use OpenGL.

### pyFLTK 

First make sure you have the Python header files installed (`aptitude install python-dev`{.backtick}). After that, see the instructions in the pyFLTK distribution for instructions, which are basically:

    python setup.py build
    sudo python setup.py install

That installs the relevant python files into into `/usr/lib/python2.5/site-packages`{.backtick}. After installation, you should run the included demos to make sure everything is working right (instructions are in the INSTALL file).

## External Links 

- [http://pyfltk.sourceforge.net/](http://pyfltk.sourceforge.net/)

------------------------------------------------------------------------

[CategoryPyGUI](CategoryPyGUI)
