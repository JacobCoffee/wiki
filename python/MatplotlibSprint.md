# MatplotlibSprint

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# Matplotlib Sprint 

We\'ll be doing a sprint starting around 10AM on matplotlib. There aren\'t a fixed set of topics yet, but please joing a discussion on matplotlib-users or matplotlib-devel if you have some specific ideas, or just add it to the wiki.

We have a list of official goals at [http://matplotlib.sf.net/goals.html](http://matplotlib.sf.net/goals.html) page and we could try to pick off as many of these as possible. Here are some things of particular interest to me (John Hunter)

Topic ideas

- contribute to the user\'s guide
- support arbitrary clipping paths
- gradient fills for polygons
- provide mathtext fonts that don\'t have the licensing restrictions
  - of bakoma, eg the umbellek fonts
- unicode support / internationalization
- expose latex/tex when available for mathtext rendering
- expose agg drawing primitives (paths, etc) directly.
- mapping and projection utilities
- pygtk/matplotlib/ipython integration: build a gtk widget to embed as a shell in gtk apps
  - bonus marks, do it in a way that is backend independent.
- provide an extension code method to blit the agg canvas to wx for wxagg
- add your favorite plot type!

Participants

- John Hunter \<[jdhunter@ace.bsd.uchicago.edu](mailto:jdhunter@ace.bsd.uchicago.edu)\>

- John Gill

- Michael Twomey
