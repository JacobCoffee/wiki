# PyDSTool

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

PyDSTool is an integrated simulation, modeling and analysis package for dynamical systems, written in Python. It is being developed at Cornell University by Robert Clewley, Drew LaMar, and Erik Sherwood. For full documentation see our [wiki](http://pydstool.sourceforge.net) site. To download, please go to the [SourceForge](http://www.sourceforge.net/projects/pydstool) files page, where you can read the release notes. The source code is available under the terms of the BSD license.

The PyDSTool software is \"research code\" in a Beta stage of development, and should not be treated as a complete or comprehensive dynamical systems package, with the associated expectation that its design and implementation have thoroughly stabilized and have been well tested. We have added features as and when we have had a use for them in our own research, and have omitted many important features that we would love to add if time permits us, or if our research so demands.

You might like to submit feature requests, or you may also like to contribute to the code yourself. We are also interested to hear your opinions about the possibility of adding some of our classes to [SciPy](SciPy) (perhaps in modified form). Please contact us at the [SourceForge](http://sourceforge.net/forum/?group_id=140858) open discussion forum or via email.

# Features implemented 

- Efficient and state-of-the-art ODE / DAE / discrete map simulation tools (using dynamically-linked and automatically generated C code, if external compiler available) (see [wiki page](http://www.cam.cornell.edu/~rclewley/cgi-bin/moin.cgi/Generators))

- Hybrid model and event-driven simulation support (see [wiki page](http://www.cam.cornell.edu/~rclewley/cgi-bin/moin.cgi/HybridSystems))

- Simulations and analysis can be forced to be \"bounds safe\", e.g. for \"non-negativity preservation\" (see [wiki page](http://www.cam.cornell.edu/~rclewley/cgi-bin/moin.cgi/BoundsSafety))

- Bifurcation analysis and continuation tools in-built, via [PyCont](http://www.cam.cornell.edu/~rclewley/cgi-bin/moin.cgi/PyCont)

- Support for data-driven modeling (see [wiki page](http://www.cam.cornell.edu/~rclewley/cgi-bin/moin.cgi/DataDrivenModels))

- Interactive command-line / script-based interface

- \"Index-free\" and context-heavy data structures, including an enhanced version of arrays (see [wiki page](http://www.cam.cornell.edu/~rclewley/cgi-bin/moin.cgi/Pointsets))

- Symbolic expression utilities (including evaluation, substitution, derivatives, some simplification) (see [wiki page](http://www.cam.cornell.edu/~rclewley/cgi-bin/moin.cgi/Symbolic))

- Easy to build complex models using hierarchical object-oriented data structures that contain composable model specifications (see [wiki page](http://www.cam.cornell.edu/~rclewley/cgi-bin/moin.cgi/ModelSpec))

- Memory management utilities, data import & export (inc. basic SBML conversion and LaTeX markup via the [SloppyCell](./SloppyCell.html) package)

- Modular code design allows easy expansion to support other algorithms (contributions welcome)

- Data structures and toolkits for parameter estimation / model fitting and other time-series and data-driven problems

- Seamless use with tools in [SciPy](http://www.cam.cornell.edu/~rclewley/cgi-bin/moin.cgi/SciPy), etc. through dynamic typing

- Additional toolboxes for specific applications, including biomechanical modeling, computational neuroscience, and systems biology (see [wiki page](http://www.cam.cornell.edu/~rclewley/cgi-bin/moin.cgi/ToolboxDocumentation))

- Many tutorial examples and documentation available online at the [wiki](http://pydstool.sourceforge.net)

# User interface 

Users of PyDSTool need to be familiar with working in interactive, command-line environments such as UNIX and Matlab, including the writing of simple command scripts. There is presently no graphical interface for PyDSTool. Our emphasis is on the interactivity of a command-line and the rapid prototyping possibilities of script-based computing.

In building a core library of Python classes, supporting many fundamental concepts in dynamical systems modeling, we provide more than just a glue with which to interface multiple tools. Our classes involve storing and maintaining a \"context\" that carries a lot of useful mathematical baggage. Through interaction with our Python environment at the script level, users can build complex models in a structured way, and have access to mathematically intuitive information about the models, using the intrinsic context of all the Python objects at the heart of their computations.

Our UI model is for users to interactively \"query\" objects for basic information (known in Python-speak as introspection), and also to be able to treat them as unitary objects of computation for use with tools and utilities such as optimizers, parameter estimators, and so forth.

We believe it is crucial for users to be able to combine the application of tools in a nested or interleaved fashion, in order to make the most flexible and dynamic manipulations of a model. Such rich combinations are practically impossible in disjointed software environments, and we believe our community is eager to be able to smoothly set-up and maintain such situations for their own modeling projects. It is a challenge to cleanly and efficiently interface different legacy algorithms with the core Python code in order to maximize the use and re-use of the context associated with the core objects.

Users are provided with an interface for the specification of both simple and complex dynamical systems models, using minimal programming syntax, and a range of options in converting these abstract specifications into instantiated numerical solvers for a specific system. Within the same interactive session, users have immediate access to analysis tools for continuation, parameter estimation, optimization, and so on. These tools are each tailored for use with the core PyDSTool structures to ensure the user has to write as little additional computer code as possible. Extensive documentation for the project has been provided online on this wiki.

A key aspect in the design of PyDSTool is the provision of adequate diagnostic information and querying utilities for data structures and computations. Users can expect helpful information regarding the status of their model development and computations beyond the guidance of the online documentation, through in-built querying commands and detailed error messages. The object-oriented nature of the software also provides inherent protection of the users' conceptualization of data-flow and control in their PyDSTool scripts.

# Design philosophy 

In our design we have emphasized modularized data structures and interface design that facilitates data-driven approaches to the modeling of physical processes, and we have built upon standard numerical, scientific and graphics libraries for Python (for instance, [SciPy](http://www.cam.cornell.edu/~rclewley/cgi-bin/moin.cgi/SciPy) and [Matplotlib](http://matplotlib.sourceforge.net)). These, in turn, make use of well-established and efficient legacy codes for numerical integration of ODEs, and for dealing with linear algebra, optimization, and root solving (for instance, the [LAPACK](http://netlib2.cs.utk.edu/lapack/) and [MINPACK](http://www.netlib.org/minpack/) Fortran libraries). These legacy codes are typically interfaced using [SWIG](http://www.swig.org). The low-level languages of these codes provide the computational speed that Python itself lacks, in the places for which computation is most intensive.

All of the code involved in the PyDSTool project is open source, and we have aimed to create as few dependencies on external software packages as possible. In particular, the package can be used with Microsoft Windows, Mac OS X and Linux machines.

On top of the third-party libraries we have added several new tools and capabilities. We have enhanced legacy numerical integration code for ordinary differential equations to perform various additional tasks of use in hybrid systems modeling, implemented at the C-code level for maximal efficiency. This includes supporting discrete event detection during dynamical evolution. Adding arbitrary user-specified event detection to a model permits ODEs and maps to be used in combination as \"hybrid\" dynamical systems. Also, the inclusion of data-based time series inputs to a dynamical system's evolution equations is a feature that aids data-driven modeling.

Utilities have been added that allow the movement of data and model specifications both in and out of PyDSTool, for sharing in other software environments. As well as basic importing and exporting of numerical data as text files, this also includes more systems-level interfacing. For instance, a user can export a dynamical model's definition to a Matlab environment in which Automatic Differentiation is available for parameter sensitivity calculations (via the package ADMC++). Also, PyDSTool can be interfaced with the systems biology modeling package [SloppyCell](./SloppyCell.html), through which PyDSTool inherits access to an interface with the Systems Biology Markup Language (SBML) for model specification, and the LaTeX mathematical markup language. Further interfaces to packages are in active development, such as to the original [DsTool](http://www.cam.cornell.edu/~rclewley/cgi-bin/moin.cgi/DsTool) and to other simulation tools such as [XPP](http://www.math.pitt.edu/~bard/xpp/xpp.html) or [NEURON](http://neuron.duke.edu/).
