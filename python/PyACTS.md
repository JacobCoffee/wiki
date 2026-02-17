# PyACTS

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

PyACTS Package [http://pyacts.umh.es](http://pyacts.umh.es)

The ACTS Collection ([http://acts.nersc.gov/](http://acts.nersc.gov/)) is a set of software tools that help programmers to write high performance scientific codes for parallel computers. ACTS is an umbrella project that has brought the tools (ScaLAPACK, SuperLU, Hypre, . . . ) together and is funding developers to provide interoperability. ACTS tools are mostly libraries (some are C libraries, some C++ class libraries, and some are Fortran libraries). They are primarily designed to run on distributed memory parallel computers, using MPI for communication. Portability and performance were both considerations in their design.

We work in the development of PyACTS as a set of Python based modules that provide a high level user interface to functionality available in the ACTS Collection. With PyACTS, we will provide an interoperable environment, where different libraries can be used interchangeably. For this purpose, we define a new class object in Python: PyACTS Array.

- The basic design features illustrate how easy it will be to incorporate new tools in the PyACTS interface. We have also get some of the initial benefits of PyACTS with some examples

with its PyBLACS and PyPBLAS interfaces . Tests made in show that the Python layer gives us an easy programming tool without any major performance penalty.

Also is available in: [http://sourceforge.net/projects/pyacts](http://sourceforge.net/projects/pyacts)
