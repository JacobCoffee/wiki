# PythonMed

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# PythonMed 

This page attempts to collect all the Python packages associated with medicine, pre-clinical research, life science and bioinformatics for the community. Its modelled along the [Debian Med project](http://wiki.debian.org/DebianMed)

## Biopython 

Biopython facilitates the use of Python for bioinformatics through high-quality, reusable modules and classes. Biopython features include parsers for various Bioinformatics file formats (BLAST, Clustalw, FASTA, Genbank,\...), access to online services (NCBI, Expasy,\...), interfaces to common and not-so-common programs (Clustalw, DSSP, MSMS\...), a standard sequence class, various clustering modules, a KD tree data structure, etc.

- compatible with Python 2 and 3

- requires: [NumPy](NumPy)

- License: [Biopython license](http://www.biopython.org/DIST/LICENSE)

- [Biopython wiki](http://biopython.org/wiki/Biopython) [Biopython at PyPI](https://pypi.python.org/pypi/biopython)

- Linux packages: [python-biopython Debian packages](https://packages.debian.org/search?searchon=sourcenames&keywords=python-biopython) [python-biopython Ubuntu packages](http://packages.ubuntu.com/search?suite=default&section=all&arch=any&keywords=biopython&searchon=sourcenames) [python-biopython Fedora package](https://apps.fedoraproject.org/packages/python-biopython) [python-biopython Archlinux packages](https://www.archlinux.org/packages/?q=biopython)

## pysam

pysam is a Python wrapper package around [Samtools](http://www.htslib.org/), a suite of programs for reading and manipulating high-throughput sequencing data.

- compatible with Python 2 and 3

- requires: [Cython](http://cython.org/)

- License: MIT

- [pysam on github](https://github.com/pysam-developers/pysam) [pysam documentation](http://pysam.readthedocs.org)

## kPAL 

kPAL is a [k]-mer [p]rofile [a]nalysis [l]ibrary. It can be used to count k-mers and to analyze and compare k-mer distributions in DNA sequences, which is itself useful, e.g., in quality control of DNA sequencing data. The package can be used as a command line tool or as a Python library.

- compatible with Python 2 and 3

- requires: [NumPy](NumPy), [h5py](http://www.h5py.org), [Biopython](PythonMed#Biopython)

- License: MIT

- [kPAL at PyPI](https://pypi.python.org/pypi/kPAL) [kPAL documentation](http://kpal.readthedocs.org)

## DendroPy 

DendroPy is a package for phylogenetic computing. It supports a wide range of phylogenetic tree formats and can be used both as a phylogenetic library and for scripting.

- compatible with Python 2.7 and Python 3 (Python 3.1 and all later versions)

- requires: -

- License: BSD

- [DendroPy at PyPI](https://pypi.python.org/pypi/DendroPy) [DendroPy documentation](http://dendropy.readthedocs.org)

------------------------------------------------------------------------

[CategoryPythonInScience](CategoryPythonInScience)
