# CodingProjectIdeas/StandardLibrary

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

- Cleanup/modernize a module(s) in the stdlib.

- Work on unit test suite. This includes not only developing support code (such as decorators to flag tests that are implementation-specific, known to fail, etc.), but also to have more [code coverage](CodeCoverage) in the unit tests.

- Implement the [SCSU](http://www.unicode.org/reports/tr6/) codec.

- [../FileSystemVirtualization](FileSystemVirtualization)

- [../EnhancedIterTools](EnhancedIterTools)

- [../ExploreFunctionalProgramming](ExploreFunctionalProgramming)

- [../TestingImprovements](TestingImprovements)

- The modules which deal with both str and unicode sometimes treat them differently \-- which is usually a bug.

- [CompleteSslSupport](CompleteSslSupport)

- [UnicodeonWindowsExtensions](UnicodeonWindowsExtensions)

- [MakeXmlrpclibAsynchronous](./MakeXmlrpclibAsynchronous.html)

- Document the bgen tool included in the Python source distribution. Jack Jansen has a version of bgen extended for C++; see [Jack\'s home page](http://homepages.cwi.nl/~jack/) for a paper about it. Perhaps it could be incorporated.

- asyncore: There are still people using asyncore, even though Twisted has taken most of the asynchronous-socket mindshare. There\'s a small test suite for asyncore, but it\'s far from exercising every method and branch. A good first step would be to improve the test suite. That would let us fix bugs with less worry about breaking the module.

- curses: The largest outstanding issue for curses is support for Unicode, or wide characters, or however you write I18N applications with curses.

- Add cross compiling support in distutils (and otherwise improve distutils).

- Improve Python Debugger(PDB).Some general ideas are here: [PdbImprovments](PdbImprovments). If you have any suggestions related to pdb, add them there.

- Write an RPC mechanism, or prepare an existing RPC mechanism, for the standard library (note: [http://rpyc.wikispaces.com](http://rpyc.wikispaces.com)).

- Write a library around pickle that allows developers to version their pickles such that old pickles can still be read even though the code that created them has been refactored, attributes renamed, and other such changes. (Perhaps not of great interest to the community. \--amk)

- Write an easy-to-use API around the actual ftplib library, so it\'s easy and intuitive to use.

- Suggest a \"Personal Standard Library\". See [http://programming.oreilly.com/2013/10/dead-batteries-included.html](http://programming.oreilly.com/2013/10/dead-batteries-included.html) for example.
