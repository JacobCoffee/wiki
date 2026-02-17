# NumPy

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

NumPy is Python\'s fundamental package for scientific computing. It is a library that provides a multidimensional array object, various derived objects (such as masked arrays and matrices), and an assortment of routines for fast operations on arrays, including mathematical, logical, shape manipulation, sorting, selecting, I/O, discrete Fourier transforms, basic linear algebra, basic statistical operations, random simulation and much more.

NumPy is used at the core of many popular packages in the world of Data Science and machine learning.

## Learning NumPy 

- The [official NumPy documentation](https://numpy.org/doc/stable/) offers multiple thorough manuals including a getting started manual.

- Python Land offers a short and free [getting started with NumPy tutorial](https://python.land/data-science/numpy) and a comprehensive paid [NumPy course](https://python.land/product/numpy-course) called \'a gentle, hands-on introduction to NumPy\'

- There\'s a complete but outdated (2006) manual by the principal author of Numpy, Travis Oliphant, is [available](http://csc.ucdavis.edu/~chaos/courses/nlp/Software/NumPyBook.pdf) for free (although donations are accepted).

## NumPy examples 

Many examples of NumPy usage can be found at [http://wiki.scipy.org/Numpy_Example_List](http://wiki.scipy.org/Numpy_Example_List)

- **numpy Example**

<!-- -->

    from numpy import *

    from PIL import Image


    ar = ones((100,100),float32)

    ar = ar * 100

    for i in range(0,100):
        ar[i,:] = 100 + (i * 1.5)

    im = Image.fromarray(ar,"F")
