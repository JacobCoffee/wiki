# SummerOfCode/2017/python-core

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# About Core Python 

Core Python encompasses projects that affect the core infrastructure, libraries and CPython.

Python is a popular high-level programming language. It is a general-purpose language used by scientists, developers, and many others who want to get things done quickly and effectively. In this spirit, our primary project this year is about helping make Python faster! Python is a language that can be interpreted and implemented in different ways. The [reference implementation](https://en.wikipedia.org/wiki/Reference_implementation) of Python is [CPython](https://en.wikipedia.org/wiki/CPython), so named because it\'s written in C. But it\'s not the only option! [PyPy](http://pypy.org/) is an implementation of Python written in Python that prides itself on a great performance. [Jython](http://www.jython.org/) is a Python implementation that compiles Python code to Java bytecode. [IronPython](http://ironpython.net/) is an implementation of Python for the .NET framework. And there are others.

# Getting Started 

The website to help you get started in Core Python development is [http://pythonmentors.com/](http://pythonmentors.com/).

Since this year\'s project is focused on performance, you should probably [Take a look at the PyPy benchmarks](http://speed.pypy.org/) and the [Python Performance Benchmark Suite](https://github.com/python/performance) \-- what can you learn about the performance of python? Can you run those benchmarks yourself and see if you get similar results? Try comparing your results to another applicant\'s and see if you both can learn!

# Contact info 

To chat with the Core Python mentors, please use the [core-mentorship@python.org](mailto:core-mentorship@python.org) mailing list. [Sign up](https://mail.python.org/mailman/listinfo/core-mentorship)

Want to talk in realtime? You can also ask questions on our IRC channel:

- [#python-gsoc](http://webchat.freenode.net/?channels=python-gsoc) on irc.freenode.net

Please join us there to chat with your fellow students and mentors! If you\'re new to IRC, you might want to check out [http://www.irchelp.org/](http://www.irchelp.org/)

# Ideas 

## Improve performance benchmarks and performance in Python implementations 

**Description**: Python is a popular language for many things, including scientific development and big data, where better performance could help allow researchers and programmers to understand data more quickly, or to process more data with limited resources. The goal of this project is to find ways to help Python performance improve in several ways:

1.  Create new performance tests. Performance benchmarks are a specialized type of test suite that allows people to understand and pinpoint places where performance is good and places where performance could be enhanced, as well as compare performance between different implementations. Creating such performance tests will likely be the primary goal of this project since it should be possible to create a number of tests over the GSoC period. The goal here is to find things that find \"interesting\" performance issues, such as places where the performance varies noticeably between two or more implementations of python or places where performance is especially slow on workloads that are interesting to a lot of people (e.g. common types of a scientific dataset).
2.  Suggest performance enhancements for implementations based on information from performance tests. Getting performance patches committed upstream in different implementations is a much more advanced task as there are politics and other considerations that may affect their approval, but the ideal student will be expected to get to the point of describing what enhancements will be needed and possibly provide initial patches that can serve as a basis for a final solution.
3.  Blog posts/infographics or other ways of communicating performance findings, issues found, and other things you\'ve learned to the wider Python community.

**Skills**: Python experience, as well as experience in other languages used for python implementations (e.g. C for CPython). At least basic understanding of computer performance issues, such as what sort of tasks will be limited by memory, CPU, etc. ([Here\'s a simplistic article about those basics](https://hubpages.com/technology/Improving-the-Performance-of-your-Computer). If that all sounds familiar to you, you\'re good to go, if it doesn\'t, do some research before applying.)

**Difficulty Level**: Intermediate, although it can be variable. An advanced beginner might be able to do initial performance tests but less on the enhancement front, someone more at expert level might be able to do more actual performance improvements.

**Related Reading**: The [PyPerformance documentation](http://pyperformance.readthedocs.io/) is a good place to start.

Take a look at [https://speed.python.org/](https://speed.python.org/) and [the PyPy benchmarks](http://speed.pypy.org/). Try getting copies of existing performance tests and running them on your own machine as a warm-up.

You probably also want to take a look at [the python speed list](https://mail.python.org/mailman/listinfo/speed) ([archives](https://mail.python.org/pipermail/speed/)) to see hear both the latest news and the history of python speed testing.

**Mentors**: Ramya Meruva (meruvaramya116 (at) gmail.com) and Jaysinh Shukla (jaysinhp (at) gmail.com).

## Other projects 

Python welcomes student ideas not on this list, but be warned that if you want to have a chance of being accepted you MUST find at least one mentor who is interested in working with you on your project, and these mentors must be qualified to mentor you (i.e. be experienced python developers known to the community, preferably with an experienced code contributor). We may be able to help you find backup mentors if you can get at least one mentor on board. You must have discussed this with them before submitting your application. Please have your mentor email gsoc-admins(at)python.org to express interest in GSoC so that they can be signed up to review your application by April 4th at the latest or your application may be rejected due to no mentor interest.
