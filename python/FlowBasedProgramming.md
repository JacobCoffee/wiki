# FlowBasedProgramming

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

According to wikipedia: flow-based programming (FBP) is a programming paradigm that defines applications as networks of \"black box\" processes, which exchange data across predefined connections by message passing, where the connections are specified externally to the processes. These black box processes can be reconnected endlessly to form different applications without having to be changed internally. FBP is thus naturally component-oriented.

This page describes Python packages for FBP.

## Flow Based Programming 

- [Luigi](https://marcobonzanini.com/2015/10/24/building-data-pipelines-with-python-and-luigi/) - \"Luigi is a Python tool for workflow management. It has been developed at Spotify, to help building complex data pipelines of batch jobs. Using a workflow manager like Luigi is in general helpful because it handles dependencies, it reduces the amount of boilerplate code that is necessary for parameters and error checking, it manages failure recovery and overall it forces us to follow a clear pattern when developing the data pipeline.\"

  - *To install Luigi*: ***pip install luigi***

- [Pipeless](http://asperous.us/pipeless/) - \"A simple Python library for building a basic data pipeline.\"

  - *To install pipeless*: ***pip install pipeless***

- [papy](http://code.google.com/p/papy/) - \"The papy package provides an implementation of the flow-based programming paradigm in Python that enables the construction and deployment of distributed workflows.\"

- [Orkan](https://github.com/tobigue/Orkan) - \"Orkan is a pipeline parallelization library, written in Python. Making use of the multicore capabilities of ones machine in Python is often not as easy as it should be. Orkan aims to provide a plain API to utilize those underused CPUs of yours in cases you need some extra horse power for your computation.\"

- [another pype](http://arvindn.livejournal.com/68137.html) - A simpler module for chaining operations

  - *To install pype*: ***use git repo: [https://github.com/randomwalker/pype](https://github.com/randomwalker/pype)***

- [Kamaelia](http://www.kamaelia.org/Home.html) - \"In Kamaelia you build systems from simple components that talk to each other. This speeds development, massively aids maintenance and also means you build naturally concurrent software. It\'s intended to be accessible by any developer, including novices. It also makes it fun :)\"

  - *To install Kamaelia*: ***[http://www.kamaelia.org/Home.html](http://www.kamaelia.org/Home.html)***

- [Ruffus](http://www.ruffus.org.uk/) - \"The Ruffus python module provides automatic support for: Managing dependencies, Parallel jobs, Re-starting from arbitrary points, especially after errors, Display of the pipeline as a flowchart, Reporting\"

  - *To install Ruffus*: ***sudo pip install ruffus \--upgrade***

- [zFlow](https://bitbucket.org/jslowery/zflow) - \"ZFlow is a simplistic implementation of Flow-based Programming for Python as defined by J.P. Morrison. More information about Flow-based Programming can be found here: [http://www.jpaulmorrison.com/fbp/](http://www.jpaulmorrison.com/fbp/) However, there are a few fundamental differences between ZFlow and the standard definition:

  - ZFlow does not support loops in the graph
  - ZFlow uses Python generators instead of asynchronous threads so port data flow works in a lazy, pulling way not by pushing.\"

- [pypedream formerly DAGPype](https://github.com/garywu/pypedream) - \"This is a Python framework for scientific data-processing and data-preparation DAG (directed acyclic graph) pipelines. It is designed to work well within Python scripts or IPython, provide an in-Python alternative for sed, awk, perl, and grep, and complement libraries such as [NumPy/SciPy](./NumPy(2f)SciPy.html), [SciKits](./SciKits.html), pandas, [MayaVi](./MayaVi.html), [PyTables](PyTables), and so forth. Those libraries process data once it has been assembled. This library is for flexible data assembly and quick exploration, or for aggregating huge data which cannot be reasonably assembled.\"

- [florun](https://github.com/leplatrem/florun) - \"florun is a visual workflow editor and runner\"

- [pypeman](https://github.com/mhcomm/pypeman) - \"Pypeman is a minimalist but pragmatic ESB / ETL / EAI in python.\"

- [PyF](https://pypi.python.org/pypi/pyf) - \"PyF is a python open source framework and platform dedicated to large data processing, mining, transforming, reporting and more.\"

- [Bein](https://pypi.python.org/pypi/bein) - \"Bein is a workflow manager and miniature LIMS system built in the Bioinformatics and Biostatistics Core Facility of the EPFL. It fills the gap for the working scientist between the classical shell and big workflow managers like Galaxy and major LIMS systems like OpenBIS.\"
