# VirtualPython

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

Currently, [virtualenv](http://virtualenv.org) is a separate application, allowing virtualization of Python installations. For Python 3.3, a built-in mechanism is being developed.

Possible GSoC projects:

- [Creating a test suite](https://bitbucket.org/carljm/cpythonv/issue/8/add-test-suite) for this virtualization mechanism.

- Building [the standard-library module](https://bitbucket.org/carljm/cpythonv/issue/7/add-virtualizepy-to-standard-library) that will actually create virtual environments, by copying or symlinking the python binary to a given location and placing a default virtualization config file near it.

Important background information to review if proposing to work on this:

- [Distutils-SIG](http://mail.python.org/mailman/listinfo/distutils-sig) mailing list threads mentioning \"pythonv,\" beginning with \"[early preview of pythonv](http://mail.python.org/pipermail/distutils-sig/2011-March/017498.html).\"

- The [work-in-progress repository](https://bitbucket.org/carljm/cpythonv) at Bitbucket and its [open issues](https://bitbucket.org/carljm/cpythonv/issues).

- The [source code of virtualenv](https://github.com/pypa/virtualenv).

- This [PyCon presentation](http://pycon.blip.tv/file/4881525/) on how virtualenv works.
