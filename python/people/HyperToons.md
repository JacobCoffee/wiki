# HyperToons

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

The hypertoon concept is not platform or content specific. The general idea is to create a screen saver type visual, i.e. something that runs indefinitely, unattended, using a network of animations that segue through key frames.

Although I defined the concept in 1996, only recently did two curves intersect: my programming skills (improving) and the the difficulty of doing animations with Python tools (decreasing). My first coded \"proof of concept\" uses VPython with Python 2.4.

The particular hypertoon implementation I review in my Open Space talk involves geometric figures transforming into each other. The key frames are polyhedra, defined with VPython cylinder and sphere objects. The transformations manipulate the polyhedra in various ways. Any time you come to a key frame, a randomizer chooses for you which scenario to play next.

I also show how two threads ( = playheads) might be launched within the hypertoon, allowing more than one scenario to run simultaneously (\"\"). This would only produce coherent results for some themes, e.g. these sorts of abstract geometry cartoons.

- Source Code: [http://www.4dsolutions.net/ocn/python/hypertoons/](http://www.4dsolutions.net/ocn/python/hypertoons/)

- Concept Page: [http://www.grunch.net/synergetics/hypertoon.html](http://www.grunch.net/synergetics/hypertoon.html)
