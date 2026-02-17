# StacklessPython

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# Stackless Python 

***A Python Implementation That Does Not Use The C Stack***

## What are the benefits of this Python variant? 

A small advantage is that recursions are no longer limited by the size of the C stack, but only by the amount of available heap memory. But that\'s not the major point.

Stackless Python allows you to run hundreds of thousands of tiny tasks, called \"tasklets\", in a single main thread. These tasklets can run completely decoupled, or they can communicate via \"channels\". Channels take all the responsibility to control suspension and resuming of tasklets in a very easy-to-manage manner.

Furthermore, the concept of small, communicating tasklets can lead you to a new, very simple way of formulating your problems. \[\--much more to be said here\--\]

## How does this work? 

Without delving into the (complicated) implementation details, the following is relevant: The Python interpreter is recursive. That is, for every invocation of a Python function or method, another incarnation of the interpreter is called from C code. By decoupling the execution of Python code from the C stack, it is possible to change the order of execution. In particular, this allows to switch between multiple concurrent running \"threads\" of Python code, which are no threads in the sense of the operating system, but so-called \"green threads\".

Although in alpha state, Stackless is being heavily used by commercial applications. One outstanding example is the Massive [MultiPlayer](./MultiPlayer.html) Online Game EVE [http://www.eve-online.com/](http://www.eve-online.com/) which is completely based upon Stackless technology.

## And is this efficient? 

Oh well! As a measure of efficiency, here a couple of numbers:

With today\'s most efficient operating system threads on a specially modified Linux variant and 1 GB main memory, it is possible to run about 100.000 Threads. The switching rate is somewhere better than 1 million per second..

With its tiny Python tasklets, Stackless accomplishes similar performance within only 100 MB, but creating a million tasklets.

In conclusion, Stackless Python is very efficient and especially suited for simulations with very many autonomous tiny objects.

## Is Stackless different from Standard Python? 

Stackless is completely compatible with Standard Python, it just adds some functionality. The interpreter is changed internally, but there is no change of behavior, unless the Stackless features are used.

## Where can I find Stackless Python 

The Stackless website can be found here: [http://www.stackless.com/](http://www.stackless.com/)

## Discussion 

\[Question copied from Ward\'s Wiki (see [StacklessPython](http://c2.com/cgi/wiki?StacklessPython "Wiki"))\]

Is the stackless implementation of continuations better than, for example, a threaded implementation? What implementation does regular Python use?

------------------------------------------------------------------------

I want to hear more about what we\'ll do with all these tasklets.

I am intrigued by the idea of a vast network of reusable components sending messages one to the other.

But it also seems clear to me that, stackless alone will not make this sort of dream a reality: It will require a framework of some point, as well, for the new components to plug into, and to mediate communications.

So I hold two lines of questioning:

- Is this, indeed, the sort of dream envisioned by stackless? (If not, what is the dream?)
- If so, what frameworks are people developing to support that component architecture? Is anybody doing this?

\-- [LionKimbro](LionKimbro) 2006-03-26 18:53:59

------------------------------------------------------------------------

Tasklets aside, why isn\'t the stackless fork of Python accepted as the reference implementatio (CPython)?

\-- [DougRansom](DougRansom) 2007-10-10 12:00:00

------------------------------------------------------------------------

[CategoryImplementations](CategoryImplementations)
