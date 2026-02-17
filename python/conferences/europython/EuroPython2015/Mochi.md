# EuroPython2015/Mochi

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# Mochi Sprint at EuroPython 2015 

[Mochi](https://github.com/i2y/mochi) is a new functional language that is written in Python 3 and compiles down to Python 3. It provides interesting functional feature while keeping two-way compatability with Python 3 (CPython and [PyPy](PyPy)). There was a [talk](https://ep2015.europython.eu/conference/talks/functional-python-with-mochi) about Mochi at [EuroPython](EuroPython) 2015. The [talk slides](http://www.python-academy.com/talks/europython2015/Functional%20Python%20with%20Mochi.slides.html) and the [video](https://www.youtube.com/watch?v=Pv7Whze78ac) (start at 2:20:30) give more details.

## Potential Sprint Topics 

### Documentation 

- Start documentation for syntax
- Start documentation for builtin functions
- Create a tutorial
- Create a simple sample application written in Mochi

### Language Features 

- Support for Python 3.5
- Replace a part of the builtin functions with toolz/cytoolz or a similar module (This may reduce documentation cost for builtin functions.)

### Testing 

- More tests ([testing guide](https://github.com/i2y/mochi/blob/master/doc/TESTS.rst))

### IPython Notebook Kernel 

- [Fix stderr (should go to notebook to not only to console)]

- Include kernel source into Mochi source

- Add support for magic functions

- Add call tips and help with \"?\"
