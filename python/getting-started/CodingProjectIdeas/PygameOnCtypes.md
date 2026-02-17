# CodingProjectIdeas/PygameOnCtypes

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# PygameOnCtypes 

**This project idea did in fact get picked up for the 2006 Summer of Code. Development of the project continues as the [Pyglet](http://code.google.com/p/pyglet/) library. See [http://www.pyglet.org](http://www.pyglet.org) for more.**

Pygame wraps some SDL libraries (SDL, SDL_Image etc) using C code. It also provides some extra misc. C functions.

Python2.5 will include [ctypes](ctypes) in the standard library. SoC 2006 is a good opportunity to recreate the pygame API using ctypes. This will let the average python programmer, who does not work with C, to hack on and extend pygame.

This same work (ctypes conversion) is already happening with PyOpenGL. Note that the pyopengl-ctypes project has been going for years now, and is still not complete.

Some notes\...

- you need to know C to work with C types. However it does mean you can work on some things without a compiler. Which is a big part of the hurdle on some platforms.
- pygame-ctypes will probably need C. Just like pyopengl-ctypes does. Pygame is not only a binding to SDL.
- ctypes does not have a stable api yet, and does not work on ARM. Both of which should be fixed in the future.
- This work will also include binding the SDL companion libraries like SDL_mixer, SDL_ttf, etc. It would be worth looking at other libraries such as SDL_gfx to replace large portions of pygame C code.
