# How do I keep a GUI alive during a long-running subprocess?

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

This frequently-asked question appears, for example, in [this Usenet posting](http://groups.google.com/group/comp.lang.python/msg/7edd2c4b0c7fe185). No single answer is canonical, for each has definite liabilities and limitations; there are, however, a number of expedients which apply in at least some situations:

- \"fire and forget\", that is, put the [subprocess](http://docs.python.org/lib/module-subprocess.html) in the background and let it run freely;

- put the subprocess in the background, return to the GUI\'s event loop, and poll to detect when the subprocess has terminated;

- put the subprocess in its own thread, and rely on Python [ThreadProgramming](ThreadProgramming) \...;

- launch **subprocess.Popen()** in a conventional way, but interleave attention in a single thread of control between the GUI controller and the **stdout** from the subprocess.

- the particular GUI framework involved\--wxPython, [TkInter](TkInter), probably has specific mechanisms for managing concurrency in an event-based way. The toolkit behind Tkinter, in fact, already has a Wiki page on [the subject above](http://wiki.tcl.tk/1526), many of whose hints can be adapted to other frameworks;

- \...

\[links, explanations, warnings\]
