# PyCon2008/SprintSignups/PyPy

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# Sign Up for a Sprint!

Are you interested in sprinting in this project? Great!

Please add your name below, include your email address.

If you\'re not sure which project to join, you can register in the [generic sprint sign-up page](http://wiki.python.org/moin/PyCon2008/SprintSignups).

See you at PyCon!

**Project Info**

PyPy is a python compiler written in Python. It\'s also a very flexible compiler toolchain which can compile so called RPython (restricted Python, a subset of Python without dynamic features) into a variety of platforms including C/POSIX, JVM and CLI. PyPy also features a set of experimental features, like different GCs or different threading models, which makes it a good platform to experiment with the python language.

Project URL: [http://codespeak.net/pypy](http://codespeak.net/pypy)

Sprint Leader: Maciej Fijalkowski

This sprint is newcomer-friendly sprint. The list of task is as usual very long and depending on attendees. It\'s suggested that people would come to an IRC and chat a bit to have a clue what is feasible on a sprint and what is not. For example, we can work on:

- JVM backend bindings for Java libraries
- Extending pypy as necessary for software X to run
- Adding more modules to pypy
- Sketching ctypes-based software, killing dependency on C modules written using C/CPython API.
- Optimizing certain parts of pypy for certain micro-benchmarks.
- Whatever else\....

Software requirements: the details depends on what people would like to work on, but in general pygame, libgc and libffi are very very useful (although not needed). A PyPy checkout, gcc and such things are a must. For people wanting to work on particular backends, appropriately Java, Mono (or .NET), spidermonkey are needed.

**Sprinters**

- John Doe (deletethisline at nomail.net)

list will be available at [http://codespeak.net/pypy/extradoc/sprintinfo/pycon2008/people.txt](http://codespeak.net/pypy/extradoc/sprintinfo/pycon2008/people.txt)
