# DistributedProgramming

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

A guide and a discussion page for Python related distributed programming.

This [link](http://groups.google.com/group/comp.lang.python/browse_frm/thread/3df7b51071dbfad) points to an informal comparison of distributed computing technologies, including [CORBA](CorbaPython), [XML-RPC, SOAP](WebServices), \... in *comp.lang.python*.

## Software 

You\'ll find here a (partial) list of relevant projects:

### Dopy 

- [http://www.mindhog.net/\~mmuller/projects/dopy/](http://www.mindhog.net/~mmuller/projects/dopy/)

  - [Dopy](Dopy) is a small distributed object system written entirely in Python. It is not intended to be *CORBA* compliant. Instead, it aims to be extremely easy to use and to support Python\'s dynamic nature - methods are invoked dynamically, parameters are passed by copy. Any python object that can be pickled can automatically be passed as a parameter or a return value, and any Python object can be published as a distributed object.

### Fnorb 

- [http://fnorb.sourceforge.net/](http://fnorb.sourceforge.net/)

  - *Fnorb* is a CORBA 2.0 ORB for Python first developed by DSTC. Fnorb\'s claim to fame is its size and pure Python implementation. These features allow it to be used whever Python may used (for example, within Jython) unlike other ORBs that rely on binary runtimes.

### ICE 

- [http://www.zeroc.com/index.html](http://www.zeroc.com/index.html)

  - ICE (Internet Communications Engine) is a GPL\'d CORBA-like middleware. It\'s

    simple, fast, and powerful, and in [serious production use](http://www.zeroc.com/customers.html).

  - Languages: Python, C++, Java, PHP, C#, and Visual Basic.

  - Platforms: [http://www.zeroc.com/platforms.html](http://www.zeroc.com/platforms.html)

### omniORB 

- [http://omniorb.sourceforge.net/](http://omniorb.sourceforge.net/)

  - *omniORB* is a robust high performance CORBA ORB for C++ and Python. It is freely available under the terms of the GNU Lesser General Public License (for the libraries), and GNU General Public License (for the tools). It is one of only three ORBs to be awarded the Open Group\'s Open Brand for CORBA.

### OSE 

- [http://www.dscpl.com.au/wiki/OSE](http://www.dscpl.com.au/wiki/OSE)

  - *OSE* is a generic application framework suitable for constructing general purpose applications, *distributed systems* and web based services. The four main parts of OSE are an extensive C++ class library, a set of Python wrappers, a build environment based on GNU Make, and a set of documentation extraction tools.

### PiCloud 

- [http://www.picloud.com](http://www.picloud.com)

  - *PiCloud* is a cloud-computing platform that integrates into Python. It allows developers to leverage the computing power of [Amazon Web Services](http://aws.amazon.com) (AWS) without having to manage, maintain, or configure their own virtual servers. [PiCloud](http://www.picloud.com) integrates into a Python code base via its custom library, *cloud*. Offloading the execution of a function to PiCloud\'s auto-scaling cluster (located on AWS) is as simple as passing the desired function into PiCloud\'s *cloud* library. For example, invoking *cloud.call(foo)* results in *foo()* being executed on PiCloud. Invoking *cloud.map(foo, range(10))* results in 10 functions, *foo(0)*, *foo(1)*, etc. being executed on PiCloud.

### PyBrenda 

- [PyBrenda](PyBrenda) is a tuple spaces implementation for Python.

### Pyro 

- [http://irmen.home.xs4all.nl/pyro/](http://irmen.home.xs4all.nl/pyro/)

  - [Pyro](Pyro) is an acronym for **Py**thon **r**emote **o**bjects. It is a library that enables you to build applications in which objects can talk to each other over the network, with minimal programming effort. You can just use normal Python method calls, with almost every possible parameter and return value type, and Pyro takes care of locating the right object on the right computer to execute the method. It is designed to be very easy to use, and to generally stay out of your way. But it also provides a set of powerful features that enables you to build distributed applications rapidly and effortlessly. Pyro is written in 100% pure Python and therefore runs on many platforms and Python versions, including Python 3.x.

### Python-Orbit 

- [http://sourceforge.net/projects/orbit-python](http://sourceforge.net/projects/orbit-python)

  - *Python-Orbit* is a project to develop Python bindings for ORBit. It supports dynamic loading of IDL (no IDL compiler required), and most of ORBit\'s Type Codes.

### Ray 

- [https://github.com/ray-project/ray](https://github.com/ray-project/ray)

  - Ray is a high-performance distributed execution framework targeted at clusters as well as large multicore machines. It uses a shared-memory distributed object store and zero-copy serialization to efficiently handle large data through shared memory, and it uses a bottom-up hierarchical scheduling architecture to achieve low-latency and high-throughput scheduling. It uses a lightweight API based on dynamic task graphs and actors to express a wide range of applications in a flexible manner, and it includes higher-level libraries for machine learning and AI applications.

### RPyC 

- [http://rpyc.sourceforge.net/](http://rpyc.sourceforge.net/)

  - [RPyC](RPyC) (pronounced like are-pie-see), or Remote Python Call, is a transparent and symmetrical python library for remote procedure calls, clustering and distributed-computing. RPyC makes use of object-proxying, a technique that employs python\'s dynamic nature, to overcome the physical boundaries between processes and computers, so that remote objects can be manipulated as if they were local.

### SCOOP 

- [http://www.pyscoop.org/](http://www.pyscoop.org/)

  - SCOOP (Scalable COncurrent Operations in Python) is a distributed task module based on PEP-3148 allowing concurrent parallel programming on various environments, from heterogeneous grids to supercomputers.

### Spread 

- [http://www.python.org/other/spread/](http://www.python.org/other/spread/)

  - *Spread* is a toolkit that provides a high performance messaging service that is resilient to faults across external or internal networks. Spread functions as a unified message bus for distributed applications, and provides highly tuned application-level multicast and group communication support. Spread services range from reliable message passing to fully ordered messages with delivery guarantees, even in case of computer failures and network partitions. Spread is designed to encapsulate the challenging aspects of asynchronous networks and enable the construction of scalable distributed applications, allowing application builders to focus on the differentiating components of their application.

### Twisted 

- [http://www.twistedmatrix.com/](http://www.twistedmatrix.com/)

  - [TwistedMatrix](TwistedMatrix) is a framework, written in Python, for writing networked applications. It includes implementations of a number of commonly used network services such as a web server, an IRC chat server, a mail server, a relational database interface and an object broker. Developers can build applications using all of these services as well as custom services that they write themselves. Twisted also includes a user authentication system that controls access to services and provides services with user context information to implement their own security models.

### YAMI 

- [http://msobczak.com/prog/yami/](http://msobczak.com/prog/yami/)

  - *YAMI* project is supposed to provide a simple language- and platform-independent alternative to other, commercially and freely available communication infractructures like COM, CORBA or JavaRMI. It\'s not supposed to become their substitution :), but thanks to much simpler rules it\'s built on, it can become a useful part in some class of distributed systems, whether they are full-blown object-oriented systems or the simplest client-server solutions. YAMI is a complete and consistent environment, and currently supports:

  - Operating Systems: FreeBSD, Linux, MS Windows, SunOS

  - Programming Languages: C, C++, ***Python***, Tcl
