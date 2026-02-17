# ParallelDistutils

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

Distutils2 currently performs all build steps strictly sequentially. For compute-expensive steps, such as compiler invocations, it would be useful to perform builds in parallel - in particular, if the system has multiple CPUs. This project should create an infrastructure in distutils for parallel builds, and provide the user a way to integrate this feature into a larger build process (such as Python\'s build process itself). Students considering this project should familiarize themselves with the [GNU make jobserver](http://mad-scientist.net/make/jobserver.html).

Bug report to track work on this: [5309](http://bugs.python.org/issue5309 "Issue")
