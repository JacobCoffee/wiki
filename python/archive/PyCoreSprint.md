# PyCoreSprint

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

Four of the guys from Pythonlabs are going to be at the sprint on plan on sprint on \*something\*. This is all being led by Guido, but he is busy and has no specific ideas of what to sprint on. If you have any, please list them below.

- Close as many bugs on SF as possible.

- Implement one of the namespace speed-up PEPs ([266](http://www.python.org/peps/pep-0266.html), [267](http://www.python.org/peps/pep-0267.html), or [280](http://www.python.org/peps/pep-0280.html)) or anything else to help prevent Guido from getting a pie in the face. =)

- My pet bug is reliable signal handling when using event loops like PyGTK. I think an extra C-level hook in the core would make it possible to do this right. (At the moment, SIGINT/KeyboardInterrupt is blocked until python regains control). I\'d be interested in participating in an effort to fix this one. - [PyConBrianWarner](PyConBrianWarner)

- Free threading (which has been asked for almost as long as namespace speed-ups ![:-)](/wiki/europython/img/smile.png ":-)") - Thomas Wouters)

- Work on the AST branch (will make Jeremy happy =)

- Fix rexec. (I happen to think it has potential and is worth saving). - Brian Warner

- Fully document classes, both classic and new-style

- make \_p_changed=1 after changing a list or a dictionary unnecessary (ZODB) - Thomas Guettler \<[guettli@thomas-guettler.de](mailto:guettli@thomas-guettler.de)\>

- Implement CALL_ATTR to speed up method calling

- Make the profiler support threads

- Implement a new I/O library

- Start work on new sockets interface as mentioned by Guido on python-dev (email at [http://mail.python.org/pipermail/python-dev/2003-March/034042.html](http://mail.python.org/pipermail/python-dev/2003-March/034042.html) )

Sprinters so far:

- Guido van Rossum (coach)
- Jeremy Hylton
- Tim Peters
- Brett Cannon
- Ka-Ping Yee
- Thomas Wouters
- Neil Schemenauer
- Aahz
- Neal Norwitz

Projects chosen so far:

- CALL_ATTR (Thomas, Brett)
- speed up new-class instance attribute lookup using a cache (Ping, Aahz)
- AST branch (Jeremy, Tim, Neil)

A summary of the speedup sprint work is in my blog: [http://www.artima.com/weblogs/viewpost.jsp?thread=4396](http://www.artima.com/weblogs/viewpost.jsp?thread=4396) \--Guido

------------------------------------------------------------------------

[CategoryPyCon](CategoryPyCon)
