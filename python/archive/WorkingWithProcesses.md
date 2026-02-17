# WorkingWithProcesses

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

These are just some notes about working with processes in Python.

The module of interest is `os`. [(os module documentation)](http://www.python.org/doc/current/lib/module-os.html)

Environment variables are accessed through a dictionary, `os.environ`.

Processes are created with `os.popen`, [described in os 6.1.2.](http://www.python.org/doc/current/lib/os-newstreams.html#os-newstreams)

:::: 
::: 
``` 
   1 import os
   2 
   3 # Export an environment variable
   4 os.environ["FOO"] = "BAR"
   5 
   6 # Make sure environment variable set for child processes
   7 for line in os.popen("bash -c 'env'").read().splitlines():
   8     if line.startswith("FOO="):
   9         print line
  10 
  11 # Since environment variable "FOO" is exported, and since child
  12 # processes inherit environment variables from their parents, this
  13 # works.
```
:::
::::
