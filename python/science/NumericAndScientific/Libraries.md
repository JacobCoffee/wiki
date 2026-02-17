# NumericAndScientific/Libraries

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

The following are links to scientific software libraries that have been recommended by Python users.

### Number Crunching and Related Tools 

This page lists a number of packages related to numerics, number crunching, signal processing, financial modeling, linear programming, statistics, data structures, date-time processing, random number generation, and crypto.

#### Data Structures 

- [PyPolyhedron](./PyPolyhedron.html) [\[details](http://cens.ioc.ee/projects/polyhedron/)\] [\[source](http://cens.ioc.ee/projects/polyhedron/src/polyhedron.tgz)\] Calculate polyhedron\'s V- and H-representation. This is a Python interface to a C-library cddlib (Pearu Peterson)

- avl_tree

  [\[details](http://www.nightmare.com/software.html)\] [\[source](ftp://squirl.nightmare.com/pub/python/python-ext/avl/avl-2.0.tar.gz)\] AVL module provide a hybrid between a dictionary and a list which can come in handy. AVL trees (named after the inventors, Adel\'son-Vel\'skii and Landis) are balanced binary search trees. (Sam Rushing)

- bplustree

  [\[details](http://www.pythonpros.com/arw/bplustree)\] [\[source](http://www.pythonpros.com/arw/bplustree/bplustree.py.txt)\] Classical compsci B+trees, implemented entirely in Python: Fast, portable file based indexing with range queries and including a dbm-compatibility mode. (Aaron Watters)

- fsm

  [\[details](http://musi-cal.mojam.com/~skip/python/)\] [\[source](http://musi-cal.mojam.com/~skip/python/fsm.py)\]

  [FiniteStateMachine](FiniteStateMachine) module. (Skip Montanaro)

- graph_lib

  [\[details](http://www.ece.arizona.edu/~denny/python_nest/)\] [\[source](http://www.ece.arizona.edu/~denny/python_nest/graph_lib.py)\] This module defines the Python class Graph. Graph is loosely modelled after the Library of Efficient Data types and Algorithms (LEDA). It includes methods for constructing graphs, BFS and DFS traversals, topological sort, etc.

- kjbuckets

  [\[details](http://www.pythonpros.com/arw/kjbuckets/)\] [\[source](http://www.pythonpros.com/arw/kjbuckets/kjb.tar.gz)\] kjbuckets is a C extension to python which defines three Python data types kjSet, kjGraph, and kjDict, implemented using a fast and space efficient hash table strategy. The types are tightly coupled and may be combined and manipulated using a collection of fast \"set at a time\" operations written in C. If you need to manipulate collections and mappings quickly take a look at this module. It comes with no warrantee of course, but it has been pounded pretty heavily and I consider it fairly solid. (Aaron Watters)

- npstruct

  [\[details](http://www.nightmare.com/software.html)\] [\[source](ftp://squirl.nightmare.com/pub/python/python-ext/misc/npstruct.tar.gz)\] An extension module useful for parsing and unparsing binary data structures. Somewhat like the standard struct module, but with a few extra features (bitfields, user-function-fields, byte order specification, etc\...) and a different API more convenient for streamed and context-sensitive formats like network protocol packets, image and sound files, etc. (Sam Rushing)

#### Date/Time 

- mxDateTime

  [\[details](http://www.lemburg.com/files/python/mxDateTime.html)\] [\[source](http://www.lemburg.com/files/python/egenix-mx-base-2.0.2.tar.gz)\] These types were created to provide a consistent way of transferring date and time data between Python and databases. Apart from handling date before the Unix epoch (1.1.1970) they also correctly work with dates beyond the Unix time limit (currently with Unix time values being encoded using 32bit integers, the limit is reached in 2038) and thus is Year 2000 and Year 2038 safe. (M.-A. Lemburg)

- Mayalib

  [\[details](http://www.pauahtun.org/ftp.html)\] \[FTP://www.pauahtun.org/pub/mayalib.zip \[source\]\] Mayan dates and numbers (math) for Python. (Ivan Van Laningham)

- normalDate

  [\[details](http://starship.python.net/crew/jbauer/normalDate/)\] [\[source](http://starship.python.net/crew/jbauer/normalDate/normalDate.py)\]

  [NormalDate](./NormalDate.html) is a specialized class to handle dates without all the excess baggage (time zones, daylight savings, leap seconds, etc.) of other date structures. (Jeff Bauer)

#### FFT 

- [SciPy](SciPy) \-- [http://www.scipy.org](http://www.scipy.org)

- fourier

  [\[details](http://starship.python.net/~hochberg/)\] [\[source](http://starship.python.net/~hochberg/fourier.py)\] A set of routines to perform Fourier transforms using pure (Numerical) Python. These are slower by a factor of 2-10 than pure C version in the FFT module (which is pretty good for a pure Python solution), but they make an interesting example. (Tom Hochberg)

- PyIMSL \-- [http://www.roguewave.com/products/imsl-numerical-libraries/pyimsl-studio.aspx](http://www.roguewave.com/products/imsl-numerical-libraries/pyimsl-studio.aspx)

#### Finance 

- pyfi

  [\[details](http://hobbiton.thisside.net)\] [\[source](http://hobbiton.thisside.net/pyfi-2.4.py)\] pyfi provides a set of functions that perform commonly used financial calculations.

  ([\[Rupert Scammell](http://hobbiton.thisside.net)\])

- pyFinancials

  [\[details](http://starship.python.net/~zanzi/)\] [\[source](http://starship.python.net/~zanzi/pyFinancials-0.66.tgz)\] A collection of algorithms for advanced financial calculations. (G. P. Ciceri)

- PyIMSL \-- [http://www.roguewave.com/products/imsl-numerical-libraries/pyimsl-studio.aspx](http://www.roguewave.com/products/imsl-numerical-libraries/pyimsl-studio.aspx) \-- Includes many standard financial calculations plus many other general functions used in finance.

- [MibianLib](./MibianLib.html) \-- Options Pricing Library [http://code.mibian.net](http://code.mibian.net)

#### Geometry 

- PyGTS - [http://pygts.sourceforge.net/](http://pygts.sourceforge.net/) \-- PyGTS is a python package used to construct, manipulate, and perform computations on triangulated surfaces. It is a hand-crafted and pythonic binding for the GNU Triangulated Surface (GTS) Library ([http://gts.sourceforge.net/](http://gts.sourceforge.net/)).

#### Interface 

- [SciPy](SciPy) \-- [http://www.scipy.org](http://www.scipy.org)

- SAML

  [\[details](http://topo.math.u-psud.fr/~bousch/saml-eng.html)\] [\[source](ftp://topo.math.u-psud.fr/pub/bousch/)\] Interface to the \"Simple Algebraic Math Library\", a C library for computer algebra, together with some application programs: a desktop calculator, a spreadsheet (sort of) and a program to factorize integers. (Thierry Bousch)

- pymat

  [\[details](http://claymore.engineer.gvsu.edu/~steriana/Python)\] [\[source](http://claymore.engineer.gvsu.edu/~steriana/Python/pymat.zip)\]

  [PyMat](PyMat) is an interface between [NumPy](NumPy) and a MATLAB engine session. It can be used to support [NumPy](NumPy)\'s functionality with the features of MATLAB. An example module is included that presents a very simple interface to MATLAB\'s plotting functions. This allows you to, for example, plot [NumPy](NumPy) arrays in a MATLAB plot window. (Andrew Sterian)

- PYML

  [\[details](http://www.mathsource.com/cgi-bin/MathSource/Enhancements/Interfacing/Other/0209-292)\] [\[source](http://www.mathsource.com/MathSource/Enhancements/Interfacing/Other/0209-292/pyml.tar.gz)\] PYML is an interface between the computer language Python and Mathematica. Mathematica expressions can be written in Python code, evaluated, and their results returned to Python. Support for postscript graphics returned from Mathematica exists. (David Konerding)

#### Mixed Integer and Linear Programming 

- Coopr

  [\[details](http://software.sandia.gov/trac/coopr)\] [\[download](http://pypi.python.org/pypi/Coopr)\] A COmmon Optimization Python Repository that includes Pyomo: a Pythonic Algebraic Modeling Language for mixed integer and linear programming.

- pulp-or Mixed Integer Programming (MIP) and LP

  [\[details](http://pulp-or.googlecode.com)\] [\[download](http://code.google.com/p/pulp-or/downloads/list)\] PuLP is an LP modeler written in python. PuLP can generate MPS or LP files and call GLPK, COIN CLP/CBC, CPLEX, Gurobi and XPRESS to solve linear problems. PuLP can be installed from pypi via

<!-- -->

    $easy_install pulp-or

- cvxopt

  [\[details](http://abel.ee.ucla.edu/cvxopt/)\] [\[source](http://abel.ee.ucla.edu/cvxopt/download.php)\]

  CVXOPT supports linear, quadratic and other advanced types of convex programming. It also has a interface to blas and lapack and is compatible with [NumPy](NumPy).

- lpsolvpy

  [\[details](http://eda.ei.tum.de/~mcp/lpsolvepy)\] [\[source](http://eda.ei.tum.de/~mcp/lpsolvepy/lpsolve-3.2-0.2.tar.gz)\] An interface to the LGPL\'d numerical linear program solver lp_solve. (Michael Pronath)

- Lp_solve5 (5.1 and 5.5) Mixed Integer Programming (MIP) and LP - New ones, NO python binding yet. Volunteers needed for python bindings.

  [\[details](http://groups.yahoo.com/group/lp_solve/)\] [\[source](http://groups.yahoo.com/group/lp_solve/)\] CPLEX, LINDO, AMPL/MathProg, LP etc. formats supported. (Noli Sicad)

- pycplex

  [\[details](http://www.cs.toronto.edu/~darius/software/pycplex)\] Python interface to the ILOG CPLEX Callable Library.

- GLPK (GNU Linear Programming Kit) MIP and LP

  [\[details](http://www.gnu.org/software/glpk/glpk.html)\] [\[source](http://www.gnu.org/software/glpk/glpk.html)\]

  - Python bindings [\[source](http://rpm.pbone.net/index.php3/stat/4/idpl/1709746/com/python-glpk-0.4-2mdk.i586.rpm.html)\]

  Has python bindings for 4.7 and can be used for 4.8. No debian package (use RPM then Alien for debian) CPLEX, LINDO, AMPL/MathProg, LP etc. formats supported as well. (Noli Sicad)

- [SciPy](SciPy) \-- [http://www.scipy.org](http://www.scipy.org)

- pySimplex

  [\[pysimplex](http://starship.python.net/crew/aaron_watters/pysimplex/)\] (broken link) [\[details](http://www.pythonpros.com/arw/pysimplex/)\] (broken link) [\[source](http://www.pythonpros.com/arw/pysimplex/pysimplex.tgz)\] (broken link) Pysimplex provides some basic symbolic programming tools for constructing, solving and optimizing systems of linear equations and inequalities. It includes an implementation of the classical SIMPLEX linear optimization algorithm as well as a filter for parsing and optimizing linear models encoded using the standard MPS format. (Aaron Watters)

- Simplex

  [\[details](http://web.archive.org/web/20040604151922/http://www.omniscia.org/~vivake/python/)\] [\[source](http://web.archive.org/web/20040602165806/http://www.omniscia.org/~vivake/python/Simplex.py)\] Simplex minimizes an arbitrary nonlinear function of N variables by the Nedler-Mead Simplex method. (Vivake Gupta)

- PyIMSL \-- [http://www.roguewave.com/products/imsl-numerical-libraries/pyimsl-studio.aspx](http://www.roguewave.com/products/imsl-numerical-libraries/pyimsl-studio.aspx)

#### Matrix/Vector 

- matrix

  [\[details](http://www.nightmare.com/software.html)\] [\[source](http://www.nightmare.com/squirl/python-ext/misc/matrix.py)\] Yet Another Matrix Module. This one leans more toward the flexible end of the spectrum, sacrificing performance for correctness. For example, it can correctly handle rationals and other strange things being inserted into it. Also implemented: LU\[P\] decomposition, and a simultaneous linear equation solving capability. Most of the standard matrix ops: transpose, determinant, inverse, etc.. along with some functional-style methods for mapping and iteration. (Sam Rushing)

- [SciPy](SciPy) \-- [http://www.scipy.org](http://www.scipy.org)

- Sparsemodule (Links are broken )

  [\[details](http://www.enme.ucalgary.ca/~nascheme/)\] [\[source](http://www.enme.ucalgary.ca/~nascheme/python/sparsemodule-0.4.tar.gz)\] An extension module wrapping the sparse library. It can be used for solving large systems of linear equations. (Neil Schemenauer)

- [MatPy](./MatPy.html) [\[details](http://MatPy.sourceforge.net)\] [\[source](ftp://MatPy.sourceforge.net/pub/MatPy/)\] A Python package for numerical computation and plotting with a

  [MatLab](./MatLab.html)-like interface. It currently consists of wrappers around the Numeric, Gnuplot and [SpecialFuncs](./SpecialFuncs.html) packages. It provides an alternative interface to [NumPy](NumPy) that is somewhat more convenient for matrix and vector computation. Eventually both will be based directly on the same low level routines. We are also looking for the possibility of interface to Octave. (H. Zhu)

#### Music 

- ratio

  [\[details](http://www.execpc.com/~wsannis/ratio.html)\] [\[source](http://www.execpc.com/~wsannis/ratio.py.txt)\] For those who are big fans of Just Intonation, one tedious aspect of this is that you end up fondling ratios a lot. The math gets boring after a while, though I do believe you should be able to do the math on your own to get a feel for what it is you\'re doing. Having said that, I decided I needed some help because I got sick of reducing multiplied ratios. I\'ve written a quick Python module, ratio.py, which handles a lot of the tedium. In particular, building up JI tetrachords and scales based on justly intuned chords or by katapyknosis is pretty simple with this module. (William Annis)

#### Neural Networks 

- bpnn

  [\[source](http://arctrix.com/nas/python/bpnn.py)\] A simple back-propagation neural network module. (Neil Schemenauer)

- PyIMSL \-- [http://www.roguewave.com/products/imsl-numerical-libraries/pyimsl-studio.aspx](http://www.roguewave.com/products/imsl-numerical-libraries/pyimsl-studio.aspx)

#### Numerics 

- numberTheory \[details !? FIXME: was same as source\]

  [\[source FIXME: broken link](http://www.dorb.com/python/numberTheory.py)\] Collection of functions from the book numberTheory. Darrell Gallion.

- [FixedPoint](./FixedPoint.html) [\[details: FIXME: broken link](http://sunsite.compapp.dcu.ie/pub/linux/redhat/DMA/)\] [\[source](http://sunsite.compapp.dcu.ie/pub/linux/redhat/DMA/Python/SRPMS/FixedPoint-0.0.3-2.src.rpm)\] Fixed decimal precision arithmetic.

- Fraction

  [\[details](http://www.binary.net/thehaas/fractionpy.shtml)\] [\[source](http://www.binary.net/thehaas/fraction.tar.gz)\] Simple class implemented in pure Python that does fraction arithmetic. (Mike Hostetler)

- SILOON ((FIXME: both link broken))

  [\[details](http://www.acl.lanl.gov/siloon/index.html)\] [\[source](http://www.acl.lanl.gov/distributions/siloon-current.tgz)\] SILOON (Scripting Interface Languages for Object-Oriented Numerics) gives users the ability to rapidly prototype their scientific codes in a simple yet elegant fashion using the popular scripting languages Python and Perl. While programming in these flexible and dynamic languages, SILOON users maintain the capability of accessing the full power and complexity of C++ and FORTRAN (coming soon) libraries executed on high-performance parallel computers. (SILOON Team)

- surd ((FIXME: both link broken))

  [\[details](http://sunsite.compapp.dcu.ie/pub/linux/redhat/DMA/)\] [\[source](http://sunsite.compapp.dcu.ie/pub/linux/redhat/DMA/Python/SRPMS/surd-1.1-1.src.rpm)\] Irrational numbers (surds) as objects.

- yarn ((FIXME: both link broken))

  [\[details](http://sunsite.compapp.dcu.ie/pub/linux/redhat/DMA/)\] [\[source](http://sunsite.compapp.dcu.ie/pub/linux/redhat/DMA/Python/SRPMS/yarn-0.2.0-1.src.rpm)\] Yet Another Rational Numbers module.

- escript - [\[details](http://access.edu.au/content/view/78/)\] \-- escript is a python module to define and solve coupled, non-linear, time-dependend partial differential equations (PDEs).

- PyIMSL \-- [http://www.roguewave.com/products/imsl-numerical-libraries/pyimsl-studio.aspx](http://www.roguewave.com/products/imsl-numerical-libraries/pyimsl-studio.aspx)

#### Other Tools 

- Evol

  [\[details](http://home.nikocity.de/polzin/python.html)\] [\[source](http://th.informatik.uni-mannheim.de/cgi-bin/local/download.py?name=evol.py)\] Evolutions strategies: Powerful global optimisation Basic class for a global optimisation strategie called \'Evolutionsstrategie\' by Prof. Schwefel. (Tobias Polzin)

- explore

  [\[details](http://home.nikocity.de/polzin/python.html)\] [\[source](http://th.informatik.uni-mannheim.de/cgi-bin/local/download.py?name=explore.py)\] Explore Array Data with Gnuplot Interactive Rotating, Zooming of 3D-gnuplot surface plot. (Tobias Polzin)

- emath

  [\[details](http://www.python.org/topics/scicomp/recipes_in_python.html)\] [\[source](http://www.python.org/topics/scicomp/recipes_in_python.html)\] 100% Python functions which are based on the famous Numerical Recipes \-- polynomial evaluation, zero- finding, integration, FFT\'s, and vector operations. \"They are loosely modelled after Numerical Recipes in C because I needed, at the time, actual source codes which I can examine instead of just wrappers around Fortran

  libraries like [NumPy](NumPy) and Octave. As evident from the documentations, the routines were written with emphasis on clarity rather than on runtime efficiency.\" (William Park)

- [PyClimate](./PyClimate.html) [\[details](http://starship.python.net/crew/jsaenz/pyclimate/)\] [\[source](http://starship.python.net/crew/jsaenz/pyclimate/downloads/PyClimate-1.1.1.tar.gz)\] A Python package designed to accomplish some usual tasks during the analysis of climate variability using Python. It provides functions to perform some simple IO operations, operations with COARDS-compliant netCDF files, EOF analysis, SVD and CCA analysis of coupled data sets, some linear digital filters, kernel based probabilitydensity function estimation and access to DCDFLIB.C library from Python. (Jon Saenz)

- Pythonica

  [\[details](http://home.nikocity.de/polzin/python.html)\] [\[source](http://th.informatik.uni-mannheim.de/cgi-bin/local/download.py?name=pythonica-0.2.tar.gz)\] A simple version of mathematica for python. (Tobias Polzin)

- graph-tool

  [\[details](http://graph-tool.skewed.de)\] A python module for efficient analysis of graphs (aka. networks), with algorithms implemented in C++ with the Boost Graph Library.

- [SciPy](SciPy) \-- [http://www.scipy.org](http://www.scipy.org)

- [ScientificPython](ScientificPython) [\[details](http://dirac.cnrs-orleans.fr/ScientificPython/)\] [\[download](http://sourcesup.cru.fr/projects/scientific-py/)\] A collection of Python modules that are useful for scientific computing. In this collection you will find modules that cover basic geometry (vectors, tensors, transformations, vector and tensor fields), quaternions, automatic derivatives, (linear) interpolation, polynomials, elementary statistics, nonlinear least-squares fits, unit calculations, Fortran-compatible text formatting, 3D visualization via VRML, two Tk widgets for simple line plots and

  3D wireframe models, and support for [ParallelProcessing](ParallelProcessing). ([KonradHinsen](KonradHinsen))

#### Random Number Generators 

- ccrandom

  [\[details](http://www.ccraig.org/software)\] [\[source](http://www.ccraig.org/software/ccrandom.py)\] This module is mostly compatible with Python\'s random module, but uses Linux or BSD\'s /dev/urandom device to generate numbers, thus yielding more random output than the default Python module. (Christopher A. Craig)

- crng ((FIXME: both links broken))

  [\[details](http://www.sbc.su.se/~per/crng)\] [\[source](http://www.sbc.su.se/~per/crng/crng-1.1.tar.gz)\] The Python module crng implements random-number generators (RNGs) based on several different algorithms producing uniform deviates in the open interval (0,1), i.e. exclusive of the end-point values 0 and 1. A few continuous and integer-valued non-uniform deviates are also available. Each RNG algorithm is implemented as a separate Python extension type. The RNG types are independent of each other, but have very similar interfaces. The entire module is implemented as one single C source code file. (Per J. Kraulis)

- MTRand ((FIXME: both links broken))

  [\[details](http://www.dorb.com/darrell/randomNumber/)\] [\[source](http://www.dorb.com/darrell/randomNumber/Rand.zip)\] Mersenne Twister random number generator. Far longer period and far higher order of equidistribution than any other implemented generators. Fast generation and efficient use of memory. (Darrell Gallion)

- PyIMSL \-- [http://www.roguewave.com/products/imsl-numerical-libraries/pyimsl-studio.aspx](http://www.roguewave.com/products/imsl-numerical-libraries/pyimsl-studio.aspx)

#### Special Functions 

- [SciPy](SciPy) \-- [http://www.scipy.org](http://www.scipy.org)

#### Statistics 

- scikits.statsmodels

  [\[pypi](http://pypi.python.org/pypi/scikits.statsmodels)\] [\[documentation](http://statsmodels.sourceforge.net/)\] scikits.statsmodels is a pure python package that provides classes and functions for the estimation of several categories of statistical models. These currently include linear regression models, OLS, GLS, WLS and GLS with AR(p) errors, generalized linear models for six distribution families and M-estimators for robust linear models. An extensive list of result statistics are available for each estimation problem. More models especially for time series analysis are available in the development repository on launchpad.

- stats

  [\[details](http://www.nmr.mgh.harvard.edu/Neural_Systems_Group/gary/python.html)\] [\[source](http://www.nmr.mgh.harvard.edu/Neural_Systems_Group/gary/python/stats.py)\] A collection of statistical functions, ranging from descriptive statistics (mean, median, histograms, variance, skew, kurtosis, etc.) to inferential statistics (t-tests, F-tests, chi-square, etc.). The functions are defined for operation on lists and, if Numeric is installed, also defined for array arguments. REQUIRES pstat.py (v0.3 or later) and io.py (v0.1 or later). (Gary Strangman)

- Rpy

  [\[details](http://rpy.sourceforge.net/)\] [\[source](http://rpy.sourceforge.net/)\] RPy is a very simple, yet robust, Python interface to the R Programming Language. [\[source](http://www.r-project.org/)\]. It can manage all kinds of R objects and can execute arbitrary R functions (including the graphic functions). All errors from the R language are converted to Python exceptions. Any module installed for the R system can be used from within Python. (Noli Sicad)

- [SciPy](SciPy) \-- [http://www.scipy.org](http://www.scipy.org)

For more information on related numeric packages, see the [Python Package Index](http://www.python.org/pypi).

- PyIMSL \-- [http://www.roguewave.com/products/imsl-numerical-libraries/pyimsl-studio.aspx](http://www.roguewave.com/products/imsl-numerical-libraries/pyimsl-studio.aspx)
