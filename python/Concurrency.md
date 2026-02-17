# Concurrency

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# Concurrency 

Concurrency in programming means that multiple computations happen at the same time. For example, you may have multiple Python programs running on your computer. Or you may connect multiple computers via a network (e.g., Ethernet) that work together towards a common objective (e.g., distributed data analytics). As all concurrent programs can access shared resources (e.g., files) at the same time, this can lead to a variety of problems and challenges (e.g., race conditions).

The goal of this article is to clear concurrency-related questions, problems, or issues you may have. It also serves as a first starting point for further discussions on concurrency in Python.

## Links 

- [Concurrency/99Bottles](./Concurrency(2f)99Bottles.html) - solutions to common problems in different styles/toolkits

- [Concurrency/Patterns](./Concurrency(2f)Patterns.html) - ways to structure your concurrent program

- [Concurrency/TipsAndTricks](./Concurrency(2f)TipsAndTricks.html) - Hints for writing better concurrent code

- [GlobalInterpreterLock](GlobalInterpreterLock) - a limitation for multithreading in CPython

## Talks 

- [Concurrency from the Ground Up - LIVE!](https://www.youtube.com/watch?v=MCs5OvhV9S4) [DavidBeazley](DavidBeazley) blows some minds at Pycon 2015

- [Keynote on Concurrency](https://www.youtube.com/watch?v=9zinZmE3Ogk) [RaymondHettinger](./RaymondHettinger.html) at [PyBay](./PyBay.html) 2017

- [Implementing Concurrency & Parallelism from the Ground Up](https://www.youtube.com/watch?v=31fXwpb0P9c) Pycon 2017

- [A Curious Course on Coroutines and Concurrency](https://www.youtube.com/watch?v=Z_OAlIhXziw) A Beazley tutorial from 2009.

## Concurrency support offered by the Standard Library 

- [multiprocessing](http://docs.python.org/library/multiprocessing.html) (available in CPython 2.6+ and 3, also in recent [PyPy](PyPy) 1.5 alpha builds)

- [threading](http://docs.python.org/library/threading.html) - make your GIL-burdened life easy and your code fast: use multiprocessing. ![;)](/wiki/europython/img/smile4.png ";)")

- [concurrent.futures](http://docs.python.org/3/library/concurrent.futures.html) (available in CPython 3.2 and up)

- [asyncio](http://docs.python.org/3/library/asyncio.html) (available in CPython 3.4 and up) - single-threaded concurrency

- async/await simpler syntatic sugar for coroutines (Python 3.5+)

## Popular Frameworks 

See also: [ParallelProcessing](ParallelProcessing), [Pypi Distributed Computing Trove](http://pypi.python.org/pypi?:action=browse&show=all&c=450)

- [StacklessPython](StacklessPython) - A Python Implementation That Does Not Use The C Stack. It purportedly can handle thousands of threads (tasklets) in the context of a very parallel game application, but remains pretty single-core.

- [Twisted](http://twistedmatrix.com) - Full-featured and well-tested asynchronous networking library. Concurrency model: Asynchronous code written around central objects known as Deferreds. Cooperative task scheduler via the [Cooperator](http://twistedmatrix.com/trac/browser/trunk/twisted/internet/task.py#L182) object. Time based scheduling with [LoopingCall](http://twistedmatrix.com/trac/browser/trunk/twisted/internet/task.py#L23)and reactor.callLater.

- [curio](https://github.com/dabeaz/curio) the coroutine library you were warned about

- [trio](https://github.com/python-trio/trio) Pythonic asynchronous I/O for humans and snakes

- [Greenlet](http://pypi.python.org/pypi/greenlet) - The \"greenlet\" package is a spin-off of [StacklessPython](StacklessPython), a version of CPython that supports micro-threads called \"tasklets\". Tasklets run pseudo-concurrently (typically in a single or a few OS-level threads) and are synchronized with data exchanges on \"channels\". [Documentation](http://codespeak.net/py/0.9.2/greenlet.html)

- [Gevent](http://www.gevent.org/) - coroutine-based networking library that uses greenlet to provide a high-level synchronous API on top of libevent event loop. It features standard library-inspired API and high performance.

- [Eventlet](http://wiki.secondlife.com/wiki/Eventlet) - Eventlet is a networking library written in Python. It achieves high scalability by using non-blocking io while at the same time retaining high programmer usability by using coroutines to make the non-blocking io operations appear blocking at the source code level.

- [Tornado](http://www.tornadoweb.org/en/stable/) high performance web framework and asynchronous networking library capable of scaling to tens of thouands of open connections

- [Ray](https://github.com/ray-project/ray) - Parallel (and distributed) process-based execution framework which uses a lightweight API based on dynamic task graphs and actors to flexibly express a wide range of applications. Uses shared-memory and zero-copy serialization for efficient data handling. Supports low-latency and high-throughput task scheduling. Includes higher-level libraries for machine learning and AI applications.

## Other Frameworks 

- [asyncoro](http://asyncoro.sourceforge.net) - Framework for asynchronous, concurrent, distributed and network programming.

- [Fibra](http://code.google.com/p/fibra/) - Fibra provides advanced cooperative concurrency using Python generators.

- [Cogen](http://code.google.com/p/cogen/) - cogen is a crossplatform library for network oriented, coroutine based programming using the enhanced generators. The project aims to provide a simple straightforward programming model similar to threads but without all the problems and costs.

- [Circuits](http://trac.softcircuit.com.au/circuits/) - circuits is a Lightweight, Event-driven Framework with a strong Component Architecture.

- [Kamaelia](http://www.kamaelia.org/Home) - In Kamaelia you build systems from simple components that talk to each other. This speeds development, massively aids maintenance and also means you build naturally concurrent software. It\'s intended to be accessible by any developer, including novices. It also makes it fun.

- [Concurrence](http://opensource.hyves.org/concurrence/) - Concurrence is a framework for creating massively concurrent network applications in Python. It takes a Lightweight-tasks-with-message-passing approach to concurrency.

- [Parallel Python](http://www.parallelpython.com/) - Parallel Python is a python module which provides a mechanism for parallel execution of python code on SMP (systems with multiple processors or cores) and clusters (computers connected via network).

- [pprocess](http://www.boddie.org.uk/python/pprocess/tutorial.html) - The pprocess module provides elementary support for parallel programming in Python using a fork-based process creation model in conjunction with a channel-based communications model implemented using socketpair and poll.

- [pysage](http://code.google.com/p/pysage) - lightweight high-level message passing library supporting actor based concurrency

- [pypes](http://www.pypes.org) - Pypes is a framework for designing highly scalable concurrent Flow-Based applications. It uses a component model (Stackless tasklets) to achieve modularity (very loose coupling) along with the 2.6 multiprocessing module to achieve parallelism (multi-processing support). The goals are focused on performance (capable of processing millions of documents) and ease of use. Building custom components is simple and pypes offers Paste templates for generating boiler plate component code along with supporting build files (plugins/components are eggs). Pypes also provides a full [Web 2.0 WSGI user interface](https://sourceforge.net/project/screenshots.php?group_id=271766) that allows users to create, destroy, configure, and connect components together using simple drag-n-drop functionality from any standards based web browser.

- [diesel](http://dieselweb.org/) - Diesel is a framework for writing network applications using asynchronous I/O in Python. It uses Python\'s generators to provide a friendly syntax for coroutines and continuations. It performs well and handles high concurrency with ease.

- [Chiral](http://chiral.j4cbo.com/) - Chiral is a lightweight coroutine-based networking framework for high-performance internet and Web services.

## Presentations etc. 

- **Using Coroutines to Create Efficient, High-Concurrency Web Applications** - Matt Spitz, Pycon 2011 [Video](http://blip.tv/file/4883016)

- **Concurrency and Distributed Systems** - Jesse Noller, Pycon 2009 [Slides](http://jessenoller.com//code/pycon_jnoller_distributed.pdf) [Video](http://pycon.blip.tv/file/1947511/)

- **Introduction to Multiprocessing** - Jesse Noller, Pycon 2009 [Slides](http://jessenoller.com/code/pycon_jnoller_multiprocessing.pdf) [Video](http://pycon.blip.tv/file/1947354/)

- **Inside the GIL** - a detailed analysis of how the GIL is even worse than we thought by David Beazley, [ChiPy](ChiPy) June 2009 [Slides](http://www.dabeaz.com/python/GIL.pdf) [Video](http://blip.tv/file/2232410)
