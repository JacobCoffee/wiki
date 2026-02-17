# Audio

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# Audio in Python 

This page tries to provide a starting point for those who want to work with audio in combination with Python.

If you are creating a game, most of what you are looking for may already be included in the many [PythonGameLibraries](PythonGameLibraries) that are available.

If you are looking for podcasts related to Python, go to the [PythonAudioMaterial](PythonAudioMaterial) page.

## Built in modules 

The [Multimedia Services](http://docs.python.org/3/library/mm.html) allow for some basic audio functionality in Python. It consists of the following modules:

::: {}
  ------------------------------------------------------------------------- -------------------------------------------------------------------------------
  [audioop](http://docs.python.org/3/library/audioop.html)           Manipulate raw audio data.
  [aifc](http://docs.python.org/3/library/aifc.html)                 Read and write audio files in AIFF or AIFC format.
  [sunau](http://docs.python.org/3/library/sunau.html)               Provide an interface to the Sun AU sound format.
  [wave](http://docs.python.org/3/library/wave.html)                 Provide an interface to the WAV sound format.
  [chunk](http://docs.python.org/3/library/chunk.html)               Module to read IFF (e.g. AIFF) chunks.
  [colorsys](http://docs.python.org/3/library/chunk.html)            Conversions between colour systems.
  [imghdr](http://docs.python.org/3/library/chunk.html)              Determine the type of a image file.
  [sndhdr](http://docs.python.org/3/library/sndhdr.html)             Determine the type of a sound file.
  [ossaudiodev](http://docs.python.org/3/library/ossaudiodev.html)   Access to OSS-compatible audio devices (mainly important for Linux / FreeBSD)
  [winsound](http://docs.python.org/3/library/winsound.html)         Access to the basic sound-playing machinery provided by Windows platforms.
  ------------------------------------------------------------------------- -------------------------------------------------------------------------------
:::

## Beyond the default modules 

Alternatively, you might want to learn about audio programming in Python. There is a veritable forest of stuff out there, but here are some good starting points.

For a complete overview have a look at [PythonInMusic](PythonInMusic).

### Platform independent 

::: {}
  -------------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [Nsound](http://nsound.sourceforge.net)                             C++ library with Python module for audio synthesis.
  [PyAudiere](http://pypi.python.org/pypi/pyaudiere/0.2)              A high-level audio interface for Python. (deadlink)
  [Pydub](http://pydub.com)                                           A high-level audio interface for Python. Uses ffmpeg for formats other than WAVE
  [pyAudio](http://people.csail.mit.edu/hubert/pyaudio/)              Python bindings for [PortAudio](./PortAudio.html) audio input and output
  [Snack](http://www.speech.kth.se/snack/)                            Playback, recording, file and socket I/O, waveforms and spectrograms. \"Last release 2004-12-01. Dead?\"
  [Python Audio Tools](http://sourceforge.net/projects/audiotools/)   Programs for CD-ripping and conversion between audio file formats.
  [musicplayer module](https://pypi.python.org/pypi/musicplayer)     Part of a [music player](http://albertz.github.com/music-player/). It uses FFmpeg for decoding and [PortAudio](./PortAudio.html) for output. It supports gapless playback and high sample rates (96kHz or 192kHz). It also has the functionality to calculate the [ReplayGain](./ReplayGain.html) value and do loudness normalization, to calculate the [AcoustId](./AcoustId.html) fingerprint, to get the metadata (via FFmpeg) and to calculate a visual representation for a sound file.
  [sounddevice](http://python-sounddevice.rtfd.org/)                  This module provides bindings for the [PortAudio](http://www.portaudio.com/) library (using [CFFI](https://cffi.rtfd.org/)) and a few convenience functions to play and record [NumPy](http://www.numpy.org/) arrays containing audio signals.
  [simpleaudio](http://simpleaudio.readthedocs.org/en/latest/)        Simple, dependency-free audio playback for Python 3
  [libwinmedia](https://github.com/mytja/libwinmedia-py)             Tiny and simple audio and video playback for Windows and Linux. Uses [libwinmedia](https://github.com/harmonoid/libwinmedia) library.
  -------------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
:::

### Platform dependent 

[http://gstreamer.freedesktop.org/modules/gst-python.html](http://gstreamer.freedesktop.org/modules/gst-python.html)

[http://pyalsaaudio.sourceforge.net/](http://pyalsaaudio.sourceforge.net/)

[http://pypi.python.org/pypi/audiosocket/](http://pypi.python.org/pypi/audiosocket/) - pure Python solution to play audio on Windows

### Modules relying on closed source 

[pysonic](http://pysonic.sourceforge.net/) - A wrapper around the [FMOD](http://www.fmod.org)-library offering plenty of options including 3D sound and effects. FMOD is a popular closed, but free for own use, that is used in many commercial game titles.

------------------------------------------------------------------------

[CategoryDocumentation](CategoryDocumentation)
