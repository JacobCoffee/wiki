# Philip Jenvey

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

My old and no longer in use mercurial jython repos is [here](http://hg.underboss.org) ![](http://www.hellanzb.com/hellanzb-content/anim-daemon.gif "http://www.hellanzb.com/hellanzb-content/anim-daemon.gif")

[BytecodeLoader](./BytecodeLoader.html) benchmarks (in milliseconds) on OS X:

    1.6 64 bit server
    makeClass: 941 getConstructor: 1874 newInstance: 355 getMain: 0
    makeClass: 895 getConstructor: 1744 newInstance: 325 getMain: 0
    makeClass: 954 getConstructor: 1725 newInstance: 330 getMain: 0
    makeClass: 959 getConstructor: 1772 newInstance: 354 getMain: 0
    makeClass: 979 getConstructor: 1759 newInstance: 381 getMain: 1
    makeClass: 897 getConstructor: 1785 newInstance: 323 getMain: 2

    1.6 64 bit server reflection avoidance hack
    loadClassFromBytes: 717 forName: 2301 getMain: 1
    loadClassFromBytes: 706 forName: 2264 getMain: 2
    loadClassFromBytes: 927 forName: 1995 getMain: 1
    loadClassFromBytes: 664 forName: 2241 getMain: 1
    loadClassFromBytes: 766 forName: 2379 getMain: 1
    loadClassFromBytes: 791 forName: 2325 getMain: 0
    loadClassFromBytes: 790 forName: 2221 getMain: 4
    loadClassFromBytes: 917 forName: 2090 getMain: 5


    1.5 client
    makeClass: 617 getConstructor: 1697 newInstance: 471 getMain: 0
    makeClass: 861 getConstructor: 1651 newInstance: 290 getMain: 1
    makeClass: 884 getConstructor: 1677 newInstance: 298 getMain: 0
    makeClass: 869 getConstructor: 1792 newInstance: 336 getMain: 0
    makeClass: 897 getConstructor: 1722 newInstance: 272 getMain: 0
    makeClass: 884 getConstructor: 1630 newInstance: 308 getMain: 1

    1.5 client reflection avoidance hack
    loadClassFromBytes: 441 forName: 2145 getMain: 3
    loadClassFromBytes: 465 forName: 2340 getMain: 1
    loadClassFromBytes: 470 forName: 2225 getMain: 0
    loadClassFromBytes: 466 forName: 2248 getMain: 1
    loadClassFromBytes: 470 forName: 2305 getMain: 1
    loadClassFromBytes: 479 forName: 2272 getMain: 0
    loadClassFromBytes: 485 forName: 2253 getMain: 2
    loadClassFromBytes: 498 forName: 2309 getMain: 1
