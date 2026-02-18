# ParallelProcessing

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# Parallel Processing and Multiprocessing in Python 

A number of Python-related libraries exist for the programming of solutions either employing multiple CPUs or multicore CPUs in a [symmetric multiprocessing (SMP)](http://en.wikipedia.org/wiki/Symmetric_multiprocessing) or shared memory environment, or potentially huge numbers of computers in a cluster or grid environment. This page seeks to provide references to the different libraries and solutions available.

## Just In Time Compilation 

Some Python libraries allow compiling Python functions at run time, this is called Just In Time (JIT) compilation.

- [Nuitka](https://nuitka.net/pages/overview.html) - As the authors say: Nuitka is a Python compiler written in Python !

  - You feed Nuitka your Python app, it does a lot of clever things, and spits out an executable or extension module.
  - Nuitka translates Python into a C program that then is linked against libpython to execute exactly like CPython
  - For version 0.6 of Nuitka and Python 2.7 speedup was 312% !

- [Numba](http://numba.pydata.org/) - Numba is an open source JIT compiler that translates a subset of Python and [NumPy](../science/NumPy) code into fast machine code.

  - Numba can use vectorized instructions (SIMD - Single Instruction Multiple Data) like SSE/AVX
  - Numba can simplify multithreading
  - Numba can compile on GPU

- [Pythran](https://pythran.readthedocs.io/en/latest/) - Pythran is an ahead of time compiler for a subset of the Python language, with a focus on scientific computing.

  - It takes a Python module annotated with a few interface description and turns it into a native Python module with the same interface, but (hopefully) faster.
  - It is meant to efficiently compile scientific programs, and takes advantage of multi-cores and SIMD instruction units.

- [Pyston](https://www.pyston.org/) - Pyston is a faster CPython implementation using C optimisation and [DynASM](https://luajit.org/dynasm.html) Just In Time compiler

  - After having been stopped in 2017 new version is back again since Python 3.8.8
  - It says to be 30% faster than CPython by just replacing CPython by Pyston version without updating your code.

- [Cython](https://cython.org/) - Cython is a language which adds C types declaration to Python language

  - Thus, it allows converting Cython code to C code and compile it as a C python library that can be imported as a real python package
  - Cython also helps removing the GIL to parallelize code

## Symmetric Multiprocessing 

Some libraries, often to preserve some similarity with more familiar concurrency models (such as Python\'s threading API), employ parallel processing techniques which limit their relevance to SMP-based hardware, mostly due to the usage of process creation functions such as the UNIX fork system call. However, a technique called process migration may permit such libraries to be useful in certain kinds of computational clusters as well, notably [single-system image](http://en.wikipedia.org/wiki/Single-system_image) cluster solutions ([Kerrighed](http://kerrighed.org/), [OpenSSI](http://sourceforge.net/projects/ssic-linux), [OpenMosix](http://openmosix.sourceforge.net/) being examples).

- [dispy](http://dispy.sourceforge.net/) - Python module for distributing computations (functions or programs) computation processors (SMP or even distributed over network) for parallel execution. The computations can be scheduled by supplying arguments in SIMD style of parallel processing. The computation units can be shared by multiple processes/users simultaneously if desired. dispy is implemented with asynchronous sockets, coroutines and efficient polling mechanisms for high performance and scalability.

- [delegate](http://lfw.org/python/delegate.html) - fork-based process creation with pickled data sent through pipes

- [forkmap (original)](http://honeypot.net/2007/07/06/multi-processing-map-python/) - fork-based process creation using a function resembling Python\'s built-in map function (*Unix, Mac, Cygwin*). (Original version)

- [forkfun (modified)](https://github.com/larroy/mycelium/blob/master/dist/utils/forkfun.py) - fork-based process creation using a function resembling Python\'s built-in map function (*Unix, Mac, Cygwin*). (New version from July-2011 with modifications)

- [Joblib](https://joblib.readthedocs.io/en/latest/) - Joblib is a set of tools to provide lightweight pipelining in Python. In particular:

  - transparent disk-caching of functions and lazy re-evaluation (memoize pattern)
  - easy simple parallel computing (single computer)

- [ppmap](http://honeypot.net/2008/04/16/yet-another-python-map/) - variant of forkmap using pp to manage the subprocesses (*Unix, Mac, Cygwin*)

- [POSH](http://poshmodule.sourceforge.net/) Python Object Sharing is an extension module to Python that allows objects to be placed in shared memory. POSH allows concurrent processes to communicate simply by assigning objects to shared container objects. (*POSIX/UNIX/Linux only*)

- [pp](http://www.parallelpython.com/) (Parallel Python) - process-based, job-oriented solution with cluster support (*Windows, Linux, Unix, Mac*)

- [pprocess](http://www.python.org/pypi/pprocess) (previously parallel/pprocess) - fork-based process creation with asynchronous channel-based communications employing pickled data [(tutorial)](http://www.boddie.org.uk/python/pprocess/tutorial.html) (*currently only POSIX/UNIX/Linux, perhaps Cygwin*)

- [processing](http://www.python.org/pypi/processing) - process-based using either fork on Unix or the subprocess module on Windows, implementing an API like the standard library\'s threading API and providing familiar objects such as queues and semaphores. Can use native semaphores, message queues etc or can use of a manager process for sharing objects (*Unix and Windows*). [Included in Python 2.6/3.0 as multiprocessing](http://docs.python.org/dev/library/multiprocessing.html#module-multiprocessing), and [backported under the same name](http://pypi.python.org/pypi/multiprocessing/).

- [PyCSP](http://code.google.com/p/pycsp) Communicating Sequential Processes for Python allows easy construction of processes and synchronised communication.

- [PyMP](https://github.com/classner/pymp) - OpenMP inspired, fork-based framework for conveniently creating parallel for-loops and sections. Supports Python 2 and 3. (*Unix only*)

- [Ray](https://github.com/ray-project/ray) - Parallel (and distributed) process-based execution framework which uses a lightweight API based on dynamic task graphs and actors to flexibly express a wide range of applications. Uses shared-memory and zero-copy serialization for efficient data handling within a single machine. Supports low-latency and high-throughput task scheduling. Includes higher-level libraries for machine learning and AI applications. Supports Python 2 and 3. (*Linux, Mac*)

- [remoteD](http://www.python.org/pypi/remoteD) - fork-based process creation with a dictionary-based communications paradigm (*platform independent, according to PyPI entry*)

- [torcpy](https://github.com/IBM/torc_py) - a platform-agnostic adaptive load balancing library that orchestrates the scheduling of task parallelism on both shared and distributed memory platforms. It takes advantage of MPI and multithreading, supports parallel nested loops and map functions and task stealing at all levels of parallelism.

- [VecPy](http://github.com/undefx/vecpy) (Vectorizing Python for concurrent SIMD execution) - Takes as input a Python function on scalars and outputs a symantically equivalent C++ function over vectors which leverages multi-threading and SIMD vector intrinsics. Generated code is compiled into a native, shared library that can be called from Python (as a module), Java (through JNI), and C++. (*Linux-only; requires Python 3, g++*)

Advantages of such approaches include convenient process creation and the ability to share resources. Indeed, the fork system call permits efficient sharing of common read-only data structures on modern UNIX-like operating systems.

## Cluster Computing 

Unlike SMP architectures and especially in contrast to thread-based concurrency, cluster (and grid) architectures offer high scalability due to the relative absence of shared resources, although this can make the programming paradigms seem somewhat alien to uninitiated developers. In this domain, some overlap with other distributed computing technologies may be observed (see [DistributedProgramming](../packaging/DistributedProgramming) for more details).

- [batchlib](http://seweb.se.wtb.tue.nl/~hat/batchlib.html) - a distributed computation system with automatic selection of processing services (*no longer developed*)

- [Celery](http://celeryproject.org/) - a distributed task queue based on distributed message passing

- [Charm4py](https://github.com/UIUC-PPL/charm4py) - General-purpose parallel/distributed computing framework for the productive development of fast, parallel and scalable applications. Built on top of Charm++, a mature runtime system used in High-performance Computing, capable of scaling applications to supercomputers. It is based on an efficient actor model, allowing many actors per process, asynchronous method invocation, actor migration and load balancing. Seamlessly integrates modern concurrency features into the actor model. Supports *Linux, Windows, macOS*.

- [Dask](https://dask.org/) - Dask is a flexible library for parallel computing in Python. It offers

  - Dynamic task scheduling optimized for computation. This is similar to Airflow, Luigi, Celery, or Make, but optimized for interactive computational workloads.

  - "Big Data" collections like parallel arrays, dataframes, and lists that extend common interfaces like [NumPy](../science/NumPy), Pandas, or Python iterators to larger-than-memory or distributed environments. These parallel collections run on top of dynamic task schedulers.

  - It extends Numpy/Pandas data structures allowing computing on many cores, many servers and managing data that does not fit in memory

- [Deap](http://code.google.com/p/deap/) is a evolutionary algorithm library, which contains a parallelization module named **DTM**, standing for Distributed Task Manager, which allows an easy parallelization over a cluster of computers. This module can be used separately \-- e.g. to compute something else than evolutionary algorithms \-- and offers an interface similar to the multiprocessing.Pool module (map, apply, synchronous or asynchronous spawns, etc.), providing a complete abstraction of the startup process and the communication and load balancing layers. It currently works over MPI, with mpi4py or PyMPI, or directly over TCP. Its unique structure allows some interesting features, like nested parallel map (a parallel map calling another distributed operation, and so on).

- [disco](http://discoproject.org/) - an implementation of map-reduce. Developed by [Nokia](http://research.nokia.com/). Core written in Erlang, jobs in Python. Inspired by Google\'s mapreduce and Apache hadoop.

- [dispy](http://dispy.sourceforge.net/) - Python module for distributing computations (functions or programs) along with any dependencies (files, other Python functions, classes, modules) to nodes connected via network. The computations can be scheduled by supplying arguments in SIMD style of parallel processing. The nodes can be shared by multiple processes/users simultaneously if desired. dispy is implemented with asynchronous sockets, coroutines and efficient polling mechanisms for high performance and scalability.

- [DistributedPython](http://code.google.com/p/distributed-python-for-scripting/) - Very simple Python distributed computing framework, using ssh and the multiprocessing and subprocess modules. At the top level, you generate a list of command lines and simply request they be executed in parallel. Works in Python 2.6 and 3.

- [exec_proxy](http://seweb.se.wtb.tue.nl/~hat/execproxy.html) - a system for executing arbitrary programs and transferring files (*no longer developed*)

- [execnet](http://codespeak.net/execnet/) - asynchronous execution of client-provided code fragments (formerly [py.execnet](http://codespeak.net/py/dist/execnet.html))

- [IPython](http://ipython.scipy.org/moin/) - the IPython shell supports [interactive parallel computing](http://ipython.org/ipython-doc/stable/parallel/index.html) across multiple IPython instances

- [job_stream](https://wwoods.github.io/job_stream) - An MPI/multiprocessing-based library for easy, distributed pipeline processing, with an emphasis on running scientific simulations. Uses decorators in a way that allows users to organize their code similarly to a traditional, non-distributed application. Can be used to realize map/reduce or more complicated distributed frameworks. Python 3 and 2.7+ compatible.

- [jug](http://luispedro.org/software/jug) - A task based parallel framework

- [mpi4py](http://mpi4py.scipy.org/) - MPI-based solution

- [NetWorkSpaces](http://www.lindaspaces.com/products/NWS_overview.html) appears to be a rebranding and rebinding of [Lindaspaces](http://www.lindaspaces.com/products/linda.html) for Python

- [PaPy](http://code.google.com/p/papy/) - Parallel(uses multiprocessing) and distributed(uses RPyC) work-flow engine, with a distributed imap implementation.

- [papyros](http://code.google.com/p/papyros/) - lightweight master-slave based parallel processing. Clients submit jobs to a master object which is monitored by one or more slave objects that do the real work. Two main implementations are currently provided, one using multiple threads and one multiple processes in one or more hosts through [Pyro](http://pyro.sourceforge.net/).

- [pp](http://www.parallelpython.com/) (Parallel Python) - \"is a python module which provides mechanism for parallel execution of python code on SMP (systems with multiple processors or cores) and clusters (computers connected via network).\"

- [PyCOMPSs](https://pypi.python.org/pypi/pycompss/) - A task based a programming model which aims to ease the development of parallel applications for distributed infrastructures, such as Clusters and Clouds. Offers a sequential interface, but at execution time the runtime system is able to exploit the inherent parallelism of applications at task level.

- [PyLinda](http://www-users.cs.york.ac.uk/~aw/pylinda/) - distributed computing using tuple spaces

- [pyMPI](http://pympi.sourceforge.net/) - MPI-based solution

- [pypar](http://code.google.com/p/pypar/) - Numeric Python and MPI-based solution

- [pyPastSet](http://pypi.python.org/pypi/pastset) - tuple-based structured distributed shared memory system in Python using the powerful Pyro distributed object framework for the core communication.

- [pypvm](http://pypvm.sourceforge.net/) - PVM-based solution

- [pynpvm](http://pynpvm.sourceforge.net/) - PVM-based solution for [NumPy](../science/NumPy)

- [Pyro](http://irmen.home.xs4all.nl/pyro/) PYthon Remote Objects, distributed object system, takes care of network communication between your objects once you split them over different machines on the network

- [Ray](https://github.com/ray-project/ray) - Parallel and distributed process-based execution framework which uses a lightweight API based on dynamic task graphs and actors to flexibly express a wide range of applications. Uses shared-memory and zero-copy serialization for efficient data handling within a single machine. Provides recovery from process and machine failures. Uses a bottom-up hierarchical scheduling scheme to support low-latency and high-throughput task scheduling. Includes higher-level libraries for machine learning and AI applications. Supports Python 2 and 3. (*Linux, Mac*)

- [rthread](http://www.cs.tut.fi/~ask/rthread/index.html) - distributed execution of functions via SSH

- [ScientificPython](http://dirac.cnrs-orleans.fr/ScientificPython/) contains three subpackages for parallel computing:

  - Scientific.[DistributedComputing](./DistributedComputing.html).[MasterSlave](./MasterSlave.html) implements a master-slave model in which a master process requests computational tasks that are executed by an arbitrary number of slave processes. The strong points are ease of use and the possibility to work with a varying number of slave process. It is less suited for the construction of large, modular parallel applications. Ideal for parallel scripting. Uses [\"Pyro\"](http://pyro.sourceforge.net/). (*works wherever Pyro works*)

  - Scientific.BSP is an object-oriented implementation of the [\"Bulk Synchronous Parallel (BSP)\"](http://www.bsp-worldwide.org/) model for parallel computing, whose main advantages over message passing are the impossibility of deadlocks and the possibility to evaluate the computational cost of an algorithm as a function of machine parameters. The Python implementation of BSP features parallel data objects, communication of arbitrary Python objects, and a framework for defining distributed data objects implementing parallelized methods. (*works on all platforms that have an MPI library or an implementation of BSPlib*)

  - Scientific.MPI is an interface to MPI that emphasizes the possibility to combine Python and C code, both using MPI. Contrary to pypar and pyMPI, it does not support the communication of arbitrary Python objects, being instead optimized for Numeric/NumPy arrays. (*works on all platforms that have an MPI library*)

- [SCOOP](http://scoop.googlecode.com/) (Scalable COncurrent Operations in Python) is a distributed task module allowing concurrent parallel programming on various environments, from heterogeneous grids to supercomputers. It provides a parallel map function, among others.

- [seppo](http://www.its.caltech.edu/~astraw/seppo.html) - based on Pyro mobile code, providing a parallel map function which evaluates each iteration \"in a different process, possibly in a different computer\".

- [PySpark](https://spark.apache.org/docs/0.9.0/python-programming-guide.html) - [PySpark](./PySpark.html) allow using [Spark](https://spark.apache.org) cluster with Python

- \"[Star-P for Python](http://www.interactivesupercomputing.com/getpr.php?id=246) is an interactive parallel computing platform \...\"

- [superpy](http://code.google.com/p/superpy/) distributes python programs across a cluster of machines or across multiple processors on a single machine. Key features include:

  - Send tasks to remote servers or to same machine via XML RPC call
  - GUI to launch, monitor, and kill remote tasks
  - GUI can automatically launch tasks every day, hour, etc.
  - Works on the Microsoft Windows operating system
    - Can run as a windows service
    - Jobs submitted to windows can run as submitting user or as service user
  - Inputs/outputs are python objects via python pickle
  - Pure python implementation
  - Supports simple load-balancing to send tasks to best servers

- [torcpy](https://github.com/IBM/torc_py) - a platform-agnostic adaptive load balancing library that orchestrates the scheduling of task parallelism on both shared and distributed memory platforms. It takes advantage of MPI and multithreading, supports parallel nested loops and map functions and task stealing at all levels of parallelism.

## Cloud Computing 

Cloud computing is similar to cluster computing, except the developer\'s compute resources are owned and managed by a third party, the \"cloud provider\". By not having to purchase and set up hardware, the developer is able to run massively parallel workloads cheaper and easier.

- [Google App Engine](http://code.google.com/appengine/) - supports Python.

- [PiCloud](http://www.picloud.com/) - is a cloud-computing platform that integrates into Python. It allows developers to leverage the computing power of [Amazon Web Services](http://aws.amazon.com/) (AWS) without having to manage, maintain, or configure their own virtual servers. [PiCloud](http://www.picloud.com/) integrates into a Python code base via its custom library, *cloud*. Offloading the execution of a function to [PiCloud](./PiCloud.html)\'s auto-scaling cluster (located on AWS) is as simple as passing the desired function into [PiCloud](./PiCloud.html)\'s *cloud* library.

  - For example, invoking *cloud.call(foo)* results in *foo()* being executed on [PiCloud](./PiCloud.html). Invoking *cloud.map(foo, range(10))* results in 10 functions, *foo(0)*, *foo(1)*, etc. being executed on [PiCloud](./PiCloud.html).

- [PyCOMPSs](https://pypi.python.org/pypi/pycompss/) - A task based a programming model which aims to ease the development of parallel applications for distributed infrastructures, such as Clusters and Clouds. Offers a sequential interface, but at execution time the runtime system is able to exploit the inherent parallelism of applications at task level.

- [StarCluster](http://web.mit.edu/stardev/cluster) - is a cluster-computing toolkit for the [AWS cloud](http://aws.amazon.com/). [StarCluster](http://web.mit.edu/stardev/cluster) has been designed to simplify the process of building, configuring, and managing clusters of virtual machines on Amazon's EC2 cloud. It allows you to easily create one or more clusters, add/remove nodes to a running cluster, easily build new AMIs, easily create and format new EBS volumes, write plugins in python to customize cluster configuration, and much more. See [StarCluster\'s documentation](http://web.mit.edu/stardev/cluster/docs/latest) for more details.

## Grid Computing 

- [Ganga](http://ganga.web.cern.ch/ganga/) - an interface to the Grid that is being developed jointly by the ATLAS and LHCb experiments at CERN.

- [Minimum intrusion Grid](http://code.google.com/p/migrid/) - a complete Grid middleware written in Python

- [PEG](http://grail.sdsc.edu/projects/peg/) - Python Extensions for the Grid

- [pyGlobus](http://www.python.org/pypi/pyGlobus) - see the [Python Core](http://dev.globus.org/wiki/Python_Core) project for related software

## Related Projects 

- [Hydra File System](http://content.cs.luc.edu/projects/comp412/hydrafs) - a distributed file system

- [Kosmos Distributed File System](http://kosmosfs.sourceforge.net/) - has Python bindings

- [Tahoe: a secure, decentralized, fault-tolerant filesystem](http://allmydata.org/source/tahoe/trunk/docs/about.html)

## Trove classifiers 

[Topic :: System :: Distributed Computing](http://pypi.python.org/pypi?:action=browse&show=all&c=450)

## Editorial Notes 

The above lists should be arranged in ascending alphabetical order - please respect this when adding new frameworks or tools.

------------------------------------------------------------------------
