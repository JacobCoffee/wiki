# NodeBox

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

NodeBox is a Mac OS X application that lets you create 2D visuals (static, animated or interactive) using Python and export them as a PDF or [QuickTime](./QuickTime.html) movie.

[nodebox.net](http://nodebox.net/)

# Supported Primitives 

NodeBox supports simple forms such as rectangles, ovals, stars, and arrows, but also bezier paths in general. It supports images (even PDF) and text (with line wrapping). You can specify fill and stroke colors using RGB, HSB or CMYK, all with alpha transparency.

Bezier path have methods for deconstructing them into contours, inserting points at arbitrary positions on the path, and constructing paths based on a list of points. You can apply all these transformations to text as well.

# Cocoa 

NodeBox is built using PyObjC, and using the Cocoa rendering engine (Quartz), which natively supports PDF.

# Libraries 

NodeBox has a large set of external libraries, all available on the [library page](http://nodebox.net/code/index.php/Library). The most notable ones are the SVG library for importing SVG paths, the bezier editor for drawing right inside of the application, and Core Image for doing Photoshop-like image manipulations (layers with blending modes, color changes, filters) using the OS X Core Image library, which is hardware accelerated.

# Documentation 

NodeBox has a lot of documentation: both a tutorial explaining the basics of programming graphics and a reference for each command in the application. The site also has a forum where users can post questions, and a gallery showcasing the latest work.
