# MacPython/CoreAudio

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

Links:

- [MusicKit](http://www.musickit.org/) - [/PyObjC](./MacPython(2f)CoreAudio(2f)PyObjC.html)

- [Boodler](http://www.eblong.com/zarf/boodler/) - [/Python](./MacPython(2f)CoreAudio(2f)Python.html)

I ([DonovanPreston](DonovanPreston)) have been noodling around with wrapping the low level [/CoreAudio](./MacPython(2f)CoreAudio(2f)CoreAudio.html) APIs necessary to generate sound on Mac OS X using Python. After struggling with threading and callbacks into Python issues I managed to get a simple hello world going which just plays a sine wave for 5 seconds. The bulk of the code is in a pyrex file here:

- [http://soundfarmer.com/content/code/coreaudio/coreaudio.pyx](http://soundfarmer.com/content/code/coreaudio/coreaudio.pyx)

And here is the simple driver python script:

- [http://soundfarmer.com/content/code/coreaudio/catest.py](http://soundfarmer.com/content/code/coreaudio/catest.py)

You compile the pyrex to a c file, and then there is a setup script which will build the extension module:

- [http://soundfarmer.com/content/code/coreaudio/setup.py](http://soundfarmer.com/content/code/coreaudio/setup.py)

Other links:

- [http://aldebaran.armory.com/\~zenomt/macosx/](http://aldebaran.armory.com/~zenomt/macosx/)

- [http://www.mat.ucsb.edu/\~c.ramakr/illposed/craudiounits.html](http://www.mat.ucsb.edu/~c.ramakr/illposed/craudiounits.html)

- [http://www.pete.yandell.com/software/pymidi/Read%20Me.html](http://www.pete.yandell.com/software/pymidi/Read%20Me.html)
