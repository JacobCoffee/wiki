# PythonGameLibraries

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

This page lists libraries that may be useful when [GameProgramming](GameProgramming) in Python.

## PyGame / related 

- Pygame ([http://www.pygame.org/](http://www.pygame.org/)) is a set of Python modules designed for writing games. It is written on top of the excellent SDL library. This allows you to create fully featured games and multimedia programs in the python language. It is the most popular, and portable game library for python, with over 1000 free and open source projects that use pygame to look at.

  The free books [\"Program Arcade Games with Python and Pygame\"](http://programarcadegames.com/), [\"Making Games with Python & Pygame\"](http://inventwithpython.com/pygame) cover the basics of the Pygame library and offers the source code for several popular video game clones.

[http://inventwithpython.com/pyganim](http://inventwithpython.com/pyganim)

- *Pyganim* is a simple module for handling sprite animation. The [tutorial](http://inventwithpython.com/pyganim/tutorial.html) covers how to use the module, and the site also provides a few demo programs.

[http://www.cosc.canterbury.ac.nz/greg.ewing/python/Albow/](http://www.cosc.canterbury.ac.nz/greg.ewing/python/Albow/)

- *Albow* (A Little Bit of Widgetry) is a graphical user interface toolkit for use in [PyGame](PyGame)-based games. Widgets include labels, buttons (text or image), check boxes, radio buttons, text fields, palettes, tables and file load/save dialogs. Layout facilities include rows, columns and grids. A theme system allows fonts and colours to be customised easily. Also provides some facilities for locating and managing resources and playing and controlling music. Can be used in conjunction with OpenGL to incorporate 2D widgets into a 3D game.

  Also available from the same site is *Humerus*, a game skeleton based on Albow. Humerus provides a framework for managing and loading levels, starting and resuming play, saving and restoring game state, and implementing an in-game level editor. A customisable main menu screen ties all these activities together.

[http://ocemp.sourceforge.net/gui.html](http://ocemp.sourceforge.net/gui.html)

- OcempGUI is an abbreviation for Ocean Empire GUI. and denotes a toolkit, which contains a set of various user interface elements based on and for pygame.

[http://www.imitationpickles.org/pgu/](http://www.imitationpickles.org/pgu/)

- pgu includes several scripts and libraries. The scripts are a tile editor and a level editor. The libraries include a state engine, a full featured gui, document layout, html rendering, text rendering, sprite and tile engine, and a timer.

[http://aharrisbooks.net/pythonGame/](http://aharrisbooks.net/pythonGame/)

- Game Engine is a high-level wrapper on Pygame that greatly simplifies game development in Python / Pygame. It is described completely in the book \"Game Programming - the L Line\" but it is available for free even if you do not purchase the book. (Look for appendix B on the website to download [GameEngine](./GameEngine.html) and the documentation)

## Pyglet / related 

[http://www.pyglet.org/](http://www.pyglet.org/)

- pyglet is a cross-platform windowing and multimedia library for Python.

  pyglet provides an object-oriented programming interface for developing games and other visually-rich applications for Windows, Mac OS X and Linux using for rendering **OpenGL**. Some of the features of pyglet are:

  - For most application and game requirements, pyglet needs nothing else besides Python, simplifying distribution and installation. Requires ctypes, and Opengl. Uses PIL, and AVBin for most format loading. Take advantage of multiple windows and multi-monitor desktops. pyglet allows you to use as many windows as you need, and is fully aware of multi-monitor setups for use with fullscreen games. Load images, sound, music and video in almost any format. pyglet can optionally use AVbin to play back audio formats such as MP3, OGG/Vorbis and WMA, and video formats such as DivX, MPEG-2, H.264, WMV and Xvid.

[http://arcade.academy](http://arcade.academy)

- Arcade is an easy-to-learn Python library for creating 2D video games. It is ideal for people learning to program, or developers that want to code a 2D game without learning a complex framework. It is built on top of Pyglet and OpenGL.

[http://cocos2d.org/](http://cocos2d.org/)

- cocos2d is a framework for building 2D games, demos, and other graphical/interactive applications. It is based on pyglet, and written in pure python, so it is cross-platform (but requires a decent/fast OpenGL platform). It provides scene flow control, sprites and actions, special effects and transitions.

[https://github.com/tartley/gloopy](https://github.com/tartley/gloopy)

- Gloopy is a simple OpenGL render loop, in pure Python, based on pyglet. It also uses PyOpenGL bindings. It is at an early stage of development and is hardly documented, although there are a couple of example demo scripts. It provides utility functions and classes for populating a 3D world with items which are rendered as VBOs. There are utilities for moving a camera around in the world, and also facilities to programmatically create and manipulate simple polyhedra, and then convert the resulting shapes into VBOs for rendering.

## PyOpenGL / related 

Generally PyOpenGL games will also make use of [PyGame](PyGame).

[http://pyopengl.sourceforge.net/](http://pyopengl.sourceforge.net/)

- PyOpenGL includes support for OpenGL v1.1, GLU, GLUT v3.7, GLE 3, WGL 4, and Togl (Tk OpenGL widget) 1.6. It also includes support for dozens of extensions (where supported in the underlying implementation). OpenGL is an environment for developing high-performance 2D and 3D applications.

[http://glewpy.sourceforge.net/](http://glewpy.sourceforge.net/)

- GLEWpy aims to bring advanced OpenGL extensions to Python. This will allow the Python OpenGL developer to use features such as fragment and vertex shaders and image processing on the GPU. It serves as a compliment to PyOpenGL and toolkits such as GLUT and SDL (pygame).

[http://slut.sourceforge.net/](http://slut.sourceforge.net/)

- Slut is a programming framework for generative, synthetic, interactive, network-enabled graphics. It is a layer above [PyGame](PyGame), PyOpenGL and Twisted.

[http://www.ixi-software.net/content/body_software_mirra.html](http://www.ixi-software.net/content/body_software_mirra.html)

- Mirra is a 2D openGL python framework.

[http://pypi.python.org/pypi/QGL](http://pypi.python.org/pypi/QGL)

- QGL is an intentionaly minimal scenegraph for rendering textured quads and text strings to an OpenGL display. It requires pygame, and is designed for building 2D games with hardware accelerated effects. It includes a pure Python and a Pyrex Renderer.

[http://rene.f0o.com/rdpyg/](http://rene.f0o.com/rdpyg/)

- A collection of code for games using python. Mostly code for use with games made with pygame, and/or pyopengl. Although some of it can be used outside.

[http://pduel.sourceforge.net/spyre/](http://pduel.sourceforge.net/spyre/)

- SPyRE is a lightweight OpenGL graphics engine, written entirely in Python. It includes a variety of cameras, several interfaces for user interaction, lighting controls and fog.

[http://opioid-interactive.com/\~shang/projects/pygext/](http://opioid-interactive.com/~shang/projects/pygext/)

- Pygame Extended (or pygext) contains additions to pygame.draw (e.g. rectangles with round corners), an opengl accelerated 2D vector graphics library and a full blown, event-based sprite/scene engine.

[http://arcticpaint.com/projects/rabbyt/](http://arcticpaint.com/projects/rabbyt/)

- Rabbyt is a fast 2d sprite library for Python. Commonly used in combination with OpenGL context of the pyglet framework listed above.

## Other 

[http://www.pythonware.com/products/pil/](http://www.pythonware.com/products/pil/)

- Adds image processing capabilities to your Python interpreter. This library supports many file formats, and provides powerful image processing and graphics capabilities.

[http://pyode.sourceforge.net/](http://pyode.sourceforge.net/)

- PyODE is a set of open-source Python bindings for The Open Dynamics Engine, an open-source physics engine.

[http://www.pymunk.org/](http://www.pymunk.org/)

- pymunk is a easy-to-use pythonic 2d physics library that can be used whenever you need 2d rigid body physics from Python. It is built on top of the very nice 2d physics library Chipmunk ( [http://chipmunk-physics.net](http://chipmunk-physics.net) ).

[https://github.com/pybox2d/pybox2d](https://github.com/pybox2d/pybox2d)

- pyBox2D is a 2D physics library for Python based on Box2D ( [http://www.box2d.org](http://www.box2d.org) ). Large set of examples with support for pyglet and pygame (with partial GTK/cairo support on the SVN).

[http://arcticpaint.com/projects/rabbyt/](http://arcticpaint.com/projects/rabbyt/)

- Rabbyt is a fast sprite library for Python.

[http://oomadness.tuxfamily.org/en/pyopenal/index.html](http://oomadness.tuxfamily.org/en/pyopenal/index.html)

- PyOpenAL is a binding of OpenAL ([http://www.openal.org](http://www.openal.org)) for Python. OpenAL is a cross-platform 3D audio API appropriate for use with gaming applications and many other types of audio applications

[http://www.libavg.de/](http://www.libavg.de/)

- libavg is a multimedia platform with powerful layout and video support that\'s scripted in python and suitable for game development.

[http://oomadness.tuxfamily.org/en/tofu/index.html](http://oomadness.tuxfamily.org/en/tofu/index.html)

- Tofu is a practical high-level network game engine, written in Python and based on Twisted.

[http://www.vrplumber.com/py3d.py](http://www.vrplumber.com/py3d.py)

- A small collection (64 packages) of pointers to Python software for working in three dimensions.

[http://www.pymedia.org/](http://www.pymedia.org/)

- [PyMedia](PyMedia) allows you to parse, demutiplex, multiplex, decode and encode wav, mp3, ogg, avi, divx, dvd, cdda etc files manipulations. (note, no new releases since 2006)

[http://panda3d.org/](http://panda3d.org/)

- Panda3D is a 3D engine: a library of subroutines for 3D rendering and game development. The library is C++ with a set of Python bindings. Game development with Panda3D usually consists of writing a Python program that controls the the Panda3D library.

[http://cgkit.sourceforge.net/](http://cgkit.sourceforge.net/)

- The Python Computer Graphics Kit is a generic 3D package that can be useful in any domain where you have to deal with 3D data of any kind, be it for visualization, creating photorealistic images, Virtual Reality or even games.

[http://trac.zeitherrschaft.org/neuro/](http://trac.zeitherrschaft.org/neuro/)

- Nedu (Neuro Engine for Demos (Underestimated)) is a game and demo engine/library. It allows you to rapidly develop games and multimedia 3D presentations under Linux and Win32.

[http://darkqueen.org/docs/code/korg_draw/](http://darkqueen.org/docs/code/korg_draw/)

- A drawing wrapper around pygame and/or PIL that offers simple graphics operations aswell as nicer text layout.

[http://louhi.kempele.fi/\~skyostil/projects/pyamanith/](http://louhi.kempele.fi/~skyostil/projects/pyamanith/)

- [PyAmanith](./PyAmanith.html) is a Python wrapper for the Amanith 2D vector graphics library. It strives to offer a pythonic interface to the library and make all its features accessible.

[http://trac.defuze.org/browser/oss/pygflw](http://trac.defuze.org/browser/oss/pygflw)

- Python bindings for the GFLW library.

[http://www.partiallydisassembled.net/euclid.html](http://www.partiallydisassembled.net/euclid.html)

- 2D and 3D vector, matrix and quaternion classes, and intersection and nearest-point finding for points, lines, rays, line segments, circles and spheres.

[http://pyallegro.sourceforge.net/](http://pyallegro.sourceforge.net/)

- Use the Allegro library from Python. Offers two versions, one direct wrapper, and one more pygame like with Python objects encapsulating Allegro\'s API.

[http://directpython.sourceforge.net/](http://directpython.sourceforge.net/)

- [DirectPython](./DirectPython.html) is an open source C++ extension to the Python programming language which provides basic access to DirectX (9.0c) API, including Direct3D, [DirectSound](./DirectSound.html), [DirectShow](./DirectShow.html) and [DirectInput](./DirectInput.html).

[https://opensvn.csie.org/traccgi/pyrr](https://opensvn.csie.org/traccgi/pyrr)

- Pyrr is a new python wrapper for the irrlicht game engine. It is still in development, a standalone demo (py2exe generated), based on the quakemap irrlicht sample, is downloadable (win32/Dx9).

[http://code.google.com/p/py-lepton/](http://code.google.com/p/py-lepton/)

- Lepton is a high-performance, pluggable particle engine and API for Python. Still under development, but already it has some useful features. It works with pygame, pyglet or PyOpenGL.

[http://www.horde3d.org/forums/viewtopic.php?f=1&t=313](http://www.horde3d.org/forums/viewtopic.php?f=1&t=313)

- Python Bindings for Horde3D: A small open source 3D rendering engine. It is written in an effort to create a graphics engine that offers the stunning visual effects expected in next-generation games while at the same time being as lightweight and conceptually clean as possible.

[http://pir.sourceforge.net](http://pir.sourceforge.net)

- Python ctypes module for Irrlicht Engine SDK. This project also have few additional nested projects: SWIG wraper, FreeBASIC object oriented library, FASM (flat assembler) and TinyCC usage examples.

[http://ignifuga.org](http://ignifuga.org)

- The Ignifuga Game Engine is a data driven and component oriented multi platform 2D engine based in Python/Cython and SDL. All your game logic code along with the engine's and supporting tools is converted to C during the build process, and compiled into one big standalone binary for each of the supported platforms (Linux 64, Win32 and Android right now, with plans to expand to OS X and iOS).

[TrueSkill](http://trueskill.org/)

- An implementation of the [TrueSkill](./TrueSkill.html)™ algorithm for Python. [TrueSkill](./TrueSkill.html)™ is a rating system among game players. It has been used on Xbox Live to rank and match players. [TrueSkill](./TrueSkill.html) system quantizes \"TRUE\" skill points by a Bayesian inference algorithm.

[Ranking](http://pythonhosted.org/ranking)

- A library to assign suitable ranks even tie scores. Also this provides most common strategies for assigning ranking: standard competition ranking (1224); modified competition ranking (1334); dense ranking (1223); ordinal ranking (1234); fractional ranking (1 2.5 2.5 4)

[Energy](http://pythonhosted.org/energy)

- Energy system for social games.

[JoBase](https://jobase.org)

- [JoBase](JoBase) is a fast Python game library for beginner coders. It is easy to use and can also run in the browser! Visit [jobase.org](https://jobase.org) to get started.

### Python kivy 

\* [Kivy](http://www.kivy.org/) - game/opengl/widget library
