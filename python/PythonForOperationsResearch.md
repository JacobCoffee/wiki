# PythonForOperationsResearch

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

This page attempts to collect information and links pertaining to the field of Operations Research, which includes problems in Linear Programming, Integer Programming, Stochastic Programming, and other Optimization methods in python.

- **[APM Python](http://apmonitor.com/wiki/index.php/Main/PythonApp)** - APM Python is free optimization software through a web service. Nonlinear Programming problem are sent to the APMonitor server and results are returned to the local Python script. A web-interface automatically loads to help visualize solutions, in particular dynamic optimization problems that include differential and algebraic equations. Default solvers include APOPT, BPOPT, and IPOPT. Pre-configured modes include optimization, parameter estimation, dynamic simulation, and nonlinear control.

- **[Coopr](https://projects.coin-or.org/Coopr)** - The Coopr software project integrates a variety of Python optimization-related packages.

- **[CVOXPT](http://abel.ee.ucla.edu/cvxopt/)** - CVXOPT is a free software package for convex optimization based on the Python programming language. It can be used with the interactive Python interpreter, on the command line by executing Python scripts, or integrated in other software via Python extension modules. Its main purpose is to make the development of software for convex optimization applications straightforward by building on Python's extensive standard library and on the strengths of Python as a high-level programming language.

- [OpenOpt](http://www.openopt.org) (license: BSD) contains connections to tens of solvers and has some own Python-written ones, e.g. nonlinear solver with specifiable accuracy: [interalg](http://www.openopt.org/interalg), graphic output of convergence and some more numerical optimization \"MUST HAVE\" features. Also OpenOpt can solve [FuncDesigner](http://www.openopt.org/FuncDesigner) problems with automatic differentiation, that usually work faster and gives more precise results than finite-differences derivatives approximation.

- **[prodyn](https://github.com/yabata/prodyn)** - a generic implementation of the dynamic programming algorithm for optimal system control.

- **[PuLP](https://projects.coin-or.org/PuLP)** - PuLP is an LP modeler written in python. PuLP can generate MPS or LP files and call GLPK, COIN CLP/CBC, CPLEX, and GUROBI to solve linear problems.

- **[Pyomo](https://software.sandia.gov/trac/coopr/wiki/Pyomo)** - The Python Optimization Modeling Objects (Pyomo) package is an open source tool for modeling optimization applications in Python. Pyomo can be used to define symbolic problems, create concrete problem instances, and solve these instances with standard solvers. Pyomo provides a capability that is commonly associated with algebraic modeling languages such as AMPL, AIMMS, and GAMS, but Pyomo\'s modeling objects are embedded within a full-featured high-level programming language with a rich set of supporting libraries. Pyomo leverages the capabilities of the Coopr software library, which integrates Python packages for defining optimizers, modeling optimization applications, and managing computational experiments.

- **[pyOpt](http://www.pyopt.org/)** - pyOpt is a package for formulating and solving nonlinear constrained optimization problems in an efficient, reusable and portable manner (license: LGPL).

- **[PySCIPOpt](https://github.com/SCIP-Interfaces/PySCIPOpt)** - PySCIPOpt provides an interface from Python to the SCIP Optimization Suite.

- **[SAMBO](https://sambo-optimization.github.io)** - a near zero-deps library for few-shot, sequential and model-based optimization (includes SCE-UA, SMBO, SHGO) of non-convex derivative-free black-box functions with minimal `scipy.optimize.minimize()`-like API and state-of-the-art performance on a common benchmark.

- **[scipy.optimize](http://www.scipy.org/SciPyPackages/Optimize)** - some solvers written or connected by [SciPy](SciPy) developers.

- **[ticdat](https://github.com/opalytics/opalytics-ticdat)** - ticdat simplifies the process of developing modular mathematical engines to read from one schema and write to another. Specifically designed with Mixed Integer Programming problems in mind, it can be used for rapidly developing a wide variety of mathematical engines.

- **[moptipy](https://thomasweise.github.io/moptipy)**, the Metaheuristic Optimization in Python package, offers a set of metaheuristic optimization algorithms, including randomized local search, evolutionary algorithms, simulated annealing, and memetic algorithms, that can be applied to a wide variety of problems from operations research, both industrial or scientific. It also comes with a facility for executing replicable experiments in a parallel or distributed fashion as well as with a set of tools for evaluating experimental results. (license: GPL 3)
