# PyTables

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# What is PyTables? 

[PyTables](http://www.pytables.org) is a package for managing hierarchical datasets and designed to efficiently and easily cope with extremely large amounts of data.

[PyTables](http://www.pytables.org) is built on top of the [HDF5](http://www.hdfgroup.org/HDF5/) library, using the Python language and the [NumPy](http://numpy.scipy.org/) package. It features an object-oriented interface that, combined with C extensions for the performance-critical parts of the code (generated using [Pyrex](http://www.cosc.canterbury.ac.nz/greg.ewing/python/Pyrex/)), makes it a fast, yet extremely easy to use tool for interactively dealing with, processing and searching very large amounts of data. One important feature of [PyTables](http://www.pytables.org) is that it optimizes memory and disk resources so that data takes much less space (specially if on-flight compression is used) than other solutions such as relational or object oriented databases.

# Design goals 

PyTables has been designed to fulfill the next requirements:

1.  Allow to structure your data in a **hierarchical** way.

2.  **Easy to use**. It implements the **natural naming** scheme for allowing convenient access to the data.

3.  All the **cells** in datasets can be **multidimensional** entities.

4.  Most of the **I/O operations speed** should be **only limited by the underlying I/O subsystem**.

5.  Enable the end user to save large datasets in a efficient way, i.e. **each single byte** of data on disk has to be **represented by one byte plus a small fraction** when loaded in memory.

# Where to find it 

For more info, documentation and downloads of PyTables, please go to its official [home page](http://www.pytables.org).
