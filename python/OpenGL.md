# OpenGL

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

OpenGL is a well-known library for displaying 2D and 3D graphics.

On a Linux system, OpenGL is divided into a number of distinct libraries:

- libGL.so is the core implementation of OpenGL. If you\'re using a fancy 3D-accelerated card, this library might be a closed-source version provided by the card vendor.
- libGLU.so is the GL Utility library, providing a number of convenience functions built on top of libGL. For example, libGL provides support for evaluating polynomials; libGLU includes a function that constructs polynomials for commonly-used shapes such as spheres.
- GLX is the OpenGL/X11 interface; in theory you could encapsulate the OpenGL API in any windowing protocol, but in practice Linux users are only interested in X11 support. GLX doesn\'t seem to be a library in the formal sense; there doesn\'t seem to be a libGLX.so lying around, so I assume it\'s included in either GLU or the core GL.
- GLUT is yet another utility library. OpenGL only defines how to draw things on screen, not how to interact with them. For example, you would have to write your own X11 to open an X11 window and to handle the \'close\' event when the user tries to close the window. GLUT fills this gap by providing support for windows that can be opened/closed, the ability to render fonts, and simple pop-up menus, but it\'s not a full-featured UI toolkit like Qt; there are no dialog boxes, text entry fields, or anything more advanced than menus. GLUT also includes a few oddball functions that do things such as render spheres or teapots.

Because there are so many libraries, programming OpenGL is kind of a mess; one program may use constants and functions from several of the above libraries.

The [PyOpenGL](PyOpenGL) library is the set of Python bindings for OpenGL.
