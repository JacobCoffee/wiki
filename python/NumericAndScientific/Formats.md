# NumericAndScientific/Formats

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

Scientific applications are known for their ability to generate huge amounts of data which are sometimes hard to manage. This page lists some of the tools which have been made available for interfacing with standard scientific file formats, as well as Python-specific tools for manipulating arrays and text files.

Interfaces to Standard Formats

- [Unidata NetCDF](http://www.unidata.ucar.edu/packages/netcdf/) Interfaces The netCDF datafile format stores large, uniform, data arrays efficiently and avoids byte-order problems when moving binary data between different machines. It is well-documented and looks like a good compromise between simplicity and generality.

  - \+ [NetCDF interface in ScientificPython](http://dirac.cnrs-orleans.fr/ScientificPython/) - NetCDF interface that makes array variables look like [NumPy](NumPy) arrays. ([KonradHinsen](KonradHinsen))

    \+ [NetCDF interface](http://snow.cit.cornell.edu/noon/ncmodule.html) - Interface to NetCDF portable data files (William Noon)

    \+ [interface](http://www.geog.ubc.ca/~kschalmNetCDF) - A Numeric-Python aware NetCDF portable data file interface (Kyle Schalm)

    \+ [PyNIO](http://www.pyngl.ucar.edu/Nio.shtml) - A Numeric-based Python package that allows read and/or write access to a variety of data formats (NetCDF, HDF 4, GRIB) using an interface modelled on [KonradHinsen](KonradHinsen)\'s [NetCDF interface](http://dirac.cnrs-orleans.fr/ScientificPython/).

  <!-- -->

  - \+ [PyPnetCDF](http://www.pyacts.org/pypnetcdf) - A Numeric-based Python package that allows read and/or write access to NetCDF file in a parallel environment using MPI and an interface to the [PnetCDF](http://www-unix.mcs.anl.gov/parallel-netcdf/) library. The object PNetCDFVariable and PNetCDFFile are very similar to [KonradHinsen](KonradHinsen)\'s definitions but PyPnetCDF implements a parallel access in a transparent and simple way to the programmer.

    \+ [netcdf4-python](http://code.google.com/p/netcdf4-python/) - python/numpy interface to netCDF version 4 library. netCDF version 4 has many features not found in earlier versions of the library, such as hierarchical groups, zlib compression, multiple unlimited dimensions, and new data types. It is implemented on top of HDF5. This module implements many of the new features, and can read and write netCDF files compatibile with older versions of the library. The API is modelled after Scientific.IO.NetCDF, and should be familiar to users of that module (Jeff Whitaker).

    \+ [pupynere](http://pypi.python.org/pypi/pupynere/1.0) - a PUre PYthon NEtcdf REader, and now also a Writer. Pupynere implements the NetCDF specification from scratch, written in pure Python, and only depends on Numpy. It uses the same syntax as the Scientific.IO.NetCDF module, and allows you to read and create NetCDF files.

- PyPDB is an interface to the PDB Portable Data Format library which is part
  - of the PACT system (by the LLNL crew). It is available as part of the LLNLPython distribution.

- HDF5 interfaces
  - Interface to the [HDF5](http://hdf.ncsa.uiuc.edu/HDF5/) format (hierachically organised datasets).

  HDF5 is a general purpose library and file format for storing scientific data. It\'s more complex and powerful than NetCDF, and the forthcoming NetCDF-4 is based on it.
  - \+ [PyHL interface](ftp://ftp.hdfgroup.org/HDF5/contrib/hl-hdf5/README.html) - A High Level Interface to the HDF5 File Format. (Anders Henja and Daniel B. Michelson)

    \+ [PyTables interface](http://pytables.sf.net/) - HDF5 interface with full support of 64-bit data address and data indexing. (Carabos Coop. V.)

Python-specific Tools

- [TableIO](http://php.iupui.edu/~mmiller3/python/#TableIO) by Mike Miller.

  - \"When I first started using Python, I wanted to read lots of numbers into

    [NumPy](NumPy) arrays. This can be done with the standard Python file reading methods, but I found that to be prohibitively slow for largish data sets. So I wrote TableIO (\_tableio.c and TableIO.py), which lets me start with a file containing a rectangular array of ASCII data (a \`table\') and read it into Python so I can manipulate it. For example, if I have a file containing an table in a file with 10 columns and 50 rows, I can use

          >>> d = TableIO.readTableAsArray(file)

    to get an array with shape (50,10). If I only want to read a couple of columns,

    say the first and ninth and tenth, I can use

          >>> [x, y, dy] = TableIO.readColumns(file, [0, 8, 9])

    to read the first column in to the 1D array x and the eigth and ninth into yand dy.\"

- [Scientific.IO.FortranFormat](http://dirac.cnrs-orleans.fr/ScientificPython/) by [KonradHinsen](KonradHinsen).

  - \"This module provides two classes that aid in reading and writing Fortran-formatted text files. Only a subset of formatting options is supported: A, D, E, F, G, I, and X formats, plus string constants for output. Repetition (e.g. 4I5 or 3(1X,A4)) is supported. Complex numbers are not supported; you have to treat real and imaginary parts separately.\"

- [numpyio](http://starship.python.net/~da/Travis/numpyio/) by Travis Oliphant.

  - \"Once compiled, numpyio is a loadable module that can be used in python for reading and writing arbitrary binary data to and from Numerical Python arrays. I work in Medical Imaging and often have large data sets to manipulate. I do much of my interactive data analysis with MATLAB, however, only having doubles to work with really puts a crimp on the sizes of the data sets I can manipulate. The fact that Numerical Python has more data types defined than doubles encouraged me to try it out. I have been very impressed with its speed and utility, but I needed some way to read large data sets from an arbitrary binary file into Numerical Python arrays. I didn\'t see any obvious way to do this so I wrote an extension module. Although there is not much documentation, having the sources available is ultimately better than documentation. But, as this is my first extension module, my style may not be elegant as I may not be using the correct APIs. Feel free to send me corrections.\"
