# CodeSpeedupExperiments

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

## Code Speedup Experiments 

This is a log of the speed up experiments that we are conducting.

Here are some experiments we could conduct. For each, we would compare against a pure Python implementation: Fib hand optimized to Java, no frames or other call setup support as seen in `PyBaseCode`.

- Fib pure Python, but with indy.

- Nested loops. Array multiplication?

- Guard failure of a loop, call into interpreter (`PyBytecode`) with well-known offset and synthesized frame. (Limited CPS.)

- Etc

### Related Speedups 

Before venturing into these experiments, I tried to speedup the `PyByteCode`. You can view the page on that at [CodeSpeedupExperiments/PyByteCode](./CodeSpeedupExperiments(2f)PyByteCode.html)

### Repository 

All the work is being done at a mercurial repo at [http://bitbucket.org/shashank/jython-experiments/](http://bitbucket.org/shashank/jython-experiments/)
