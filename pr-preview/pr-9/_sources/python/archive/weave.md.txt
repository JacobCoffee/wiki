# weave

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

The weave package allows the inclusion of C/C++ within Python code. It is part of the larger [SciPy](SciPy) package ([http://www.scipy.org](http://www.scipy.org)), but is also available as a stand alone package ([https://pypi.python.org/pypi/weave](https://pypi.python.org/pypi/weave)) so that more people can try it out.

The GPL\'d [AsynCluster](http://foss.eepatents.com/trac/AsynCluster/wiki) project contains a package *svpmc*, which has a module [svpmc.weave](http://foss.tellectual.com/trac/AsynCluster/browser/projects/AsynCluster/trunk/svpmc/weave.py). The *Weaver* class in that module provides a convenient API for running C/C++ code with *weave.inline*. See the [svpmc.sample](http://foss.tellectual.com/trac/AsynCluster/browser/projects/AsynCluster/trunk/svpmc/sample.py) module and its companion [C code file](http://foss.tellectual.com/trac/AsynCluster/browser/projects/AsynCluster/trunk/svpmc/sample.c) for an example of usage.

------------------------------------------------------------------------

[CategoryPythonInScience](CategoryPythonInScience)
