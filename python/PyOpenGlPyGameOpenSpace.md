# PyOpenGlPyGameOpenSpace

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# PyOpenGL / PyGame OpenSpace 

## Organizer 

Mike Fletcher, PyOpenGL maintainer

## Attendees 

Tim Sharpe, Jeff Epler, Chris Hagner, Thomas Shaw, Robert Ippolito, Shawn Wheatley, Michael Cornelius

## Notes 

The initial attendees were mostly there as \"listeners\". They were interested in [PyGame](PyGame) and PyOpenGL, but didn\'t have a lot of experience. Bob Ippolito was roped into talking to us. He has used [PyGame](PyGame) as the framework for simulations \-- not for gaming.

Chris Hagner has also played around with [PyGame](PyGame), and told us that the learning curve is fairly shallow. It took only a short time and little code to get a tetris-like game on the screen. You can get into the design considerations of the game very quickly, without worrying about other implementation details.

\"[SolarWolf](./SolarWolf.html)\" was acclaimed by those that had seen it as the canonical [PyGame](PyGame) game. Also the most fun.

[PyGame](PyGame) supports sound via the SDL mixer, and displays PyOpenGL.

Mike Fletcher detached from the Business Forum at this point and joined us to lead a discussion of PyOpenGL. (Thank goodness. We were beginning to spiral out of control.) From that discussion came the following:

### How to improve PyOpenGL 

- Support modern OpenGL features.
- Change (fix) distribution mechanism. Ship the output of SWIG.

Yes, Virginia, PyOpenGL is integrated with numeric. It\'s necessary to have a good understanding of OpenGL to take advantage of this, because it\'s easy to make it dog-slow.

Finally, there are many 3D libraries (scene graph engines) available for Python:

- Ogre

- Crystal Space

- \...the list can be found on [http://www.py3d.org](http://www.py3d.org)

Mike Fletcher wants us all to know: PyOpenGL needs maintainers/developers!

Faithfully submitted via stream of consciousness, Michael Cornelius
