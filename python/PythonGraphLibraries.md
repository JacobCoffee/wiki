# PythonGraphLibraries

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# Python Graph Libraries 

These libraries are concerned with graphs and networks, not the plotting of numeric data in graphical form.

From the [Python Graph API](PythonGraphApi) page, plus some others discovered through searching the Internet, quoting the descriptions for each package. We provide the pip installable name (`dist`{.backtick}) and the importable name (`pkg`{.backtick}).

- [graph-tool](https://graph-tool.skewed.de/) (dist: `graph-tool`{.backtick}, mod: `graph_tool`{.backtick}) is an efficient package for manipulation and statistical analysis of graphs, based on the C++ Boost Graph Library and parallelized using OpenMP. It is not pip-installable, but available through conda. It is the newest of the bunch, so its author seems to have spent some time to implement a comparative amount of features compared to the others.

- [NetworKit](https://networkit.github.io) (dist: networkit, mod: networkit) [NetworKit](./NetworKit.html) is a general open-source toolkit for large-scale network analysis. Its aim is to provide tools for the analysis of large networks in the size range from thousands to billions of edges. For this purpose, it implements efficient graph algorithms, many of them parallel to utilize multicore architectures In this respect, [NetworKit](./NetworKit.html) is comparable to packages such as NetworkX, albeit with a focus on parallelism and scalability.

- [NetworkX](https://networkx.org/) (dist: `NetworkX`{.backtick}, mod: `networkx`{.backtick}) is a Python package for the creation, manipulation, and study of the structure, dynamics, and functions of complex networks. It is implemented based on [NumPy](NumPy) and [SciPy](SciPy) and therefore supports all common platforms.

- [python-igraph](https://igraph.org/python/) (dist: `igraph`{.backtick}, mod: `igraph`{.backtick}) is the set of Python bindings for [igraph](http://cneurocvs.rmki.kfki.hu/igraph/), a collection of network analysis tools with the emphasis on efficiency, portability and ease of use. It is easily installable from wheels for an extensive array of platforms and it benefits from contributions coming in through users of the C library and R bindings.

- [rustworkX](https://www.rustworkx.org) (dist: rustworkx, mod: rustworkx) Rustworkx is a general purpose graph library for Python written in Rust to take advantage of the performance and safety that Rust provides. It is designed to provide a high performance general purpose graph library for any Python application.

All of the above have options for graph generation, IO, algorithms, statistics, and drawing (to image files, Matplotlib, and Cairo). All are free software or open source.

The following Python package is based on the concept of [implicit graphs](https://en.wikipedia.org/wiki/implicit_graph) and provides algorithm implementations specifically for this context. It is free software.

- [NoGraphs](https://nographs.readthedocs.io) (dist: nographs, mopd: nographs) Graph analysis - the lazy (evaluation) way. NoGraphs simplifies the analysis of graphs that can not or should not be fully computed, stored or adapted, e.g. infinite graphs, large graphs and graphs with expensive computations.

## Unmaintained libraries 

The following are marked as or at least seem unmaintained:

- [Another Python Graph Library](https://github.com/charanpald/APGL) (dist&mod: `apgl`{.backtick}) is a simple, fast and easy to use graph library with some machine learning features. (Last commit in 2014, marked unmaintained in 2018, author recommends NetworkX or igraph)

- [py_graph](http://compbio.washington.edu/~zach/py_graph/doc/html/public/py_graph-module.html) (dist&mod: `py_graph`{.backtick}) is a native python library for working with graphs. (Page offline as of 2021)

- [python-graph](https://github.com/Shoobx/python-graph/) (dist: `python-graph-core`{.backtick}, mod: `pygraph`{.backtick}) is a library for working with graphs in Python. This software provides ﻿a suitable data structure for representing graphs and a whole set of important algorithms. (Last commit in 2018, no issue page)

## Other libraries 

- [EasyGraph](https://easy-graph.github.io/) (dist: `Python-EasyGraph`{.backtick}, mod: `easygraph`{.backtick}) is a multi-processing, hybrid (written in Python and C++) graph library for analyzing undirected, directed graphs and multigraphs. It integrates state-of-the-art graph processing approaches, and covers a series of advanced graph processing algorithms include structural hole spanners detection (HIS, MaxD, Common_Greedy, AP_Greedy and HAM), and graph representation learning (deepwalk, node2vec, LINE and SDNE).

## Editorial Notes 

The above lists should be arranged in ascending alphabetical order - please respect this when adding new entries. When specifying release dates please use the format YYYY-MM-DD.
