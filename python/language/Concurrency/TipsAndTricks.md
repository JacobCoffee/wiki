# Concurrency/TipsAndTricks

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# Concurrency Tips & Tricks 

## Use with statement to manage locks 

Starting in Python 2.5, the `with`{.backtick} statement is a far easier way to manage locks:

:::: 
::: 
``` 
   1 some_lock = threading.Lock()
   2 
   3 with some_lock:
   4     do_stuff_requiring_lock()
```
:::
::::

This is equivalent to:

:::: 
::: 
``` 
   1 some_lock = threading.Lock()
   2 
   3 some_lock.acquire():
   4 try:
   5     do_stuff_requiring_lock()
   6 finally:
   7     some_lock.release()
```
:::
::::

## Adjust checkinterval 

Increasing the [check interval](http://docs.python.org/library/sys.html#sys.setcheckinterval) may improve performance for CPU-bound multithreaded programs, at the cost of I/O responsiveness.
