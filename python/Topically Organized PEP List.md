# Topically Organized PEP List

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

PEP 1 organizes the PEPs by meta-catagory and numerically. This is merely another list, organized by topic. This index will grow as more topics are included and more PEPs show up in PEP 1.

The official list is [here](http://www.python.org/dev/peps/). The numerical index is included after the topical index, along with a mark indicating if a PEP has already been placed under at least one topic.

The idea is that a PEP can be found in more that one topic, which is sometimes the case. For the standards track proposals this is particularly true. Topics may include specific language features, in which case a PEP could be found under a dozen ore more different topics.

Non-feature/non-subject topics are first, followed by feature and subject topics in alphabetical order. Within each topic the PEPs are sub-ordered by category and then numerically. The category key is at the bottom of this page.

Index by Topic:

    cat  num  title                                                   owner
    ---  ---  -----                                                   -----

     General Core Python Development Standards PEPs
     ----------------------------------------------

     P     1  PEP Purpose and Guidelines                              Warsaw, Hylton, Goodger
     P     2  Procedure for Adding New Modules                        Faassen
     P     4  Deprecation of Standard Modules                         von Löwis
     P     5  Guidelines for Language Evolution                       Prescod
     P     9  Sample Plaintext PEP Template                           Warsaw
     P    10  Voting Guidelines                                       Warsaw
     P    11  Removing support for little used platforms              von Löwis
     P    12  Sample reStructuredText PEP Template                    Goodger, Warsaw
     P   387  Backwards Compatibility Policy                          Peterson

     I    20  The Zen of Python                                       Peters
     I    42  Feature Requests                                        Hylton

     Python Standard Library Development Standards PEPs
     --------------------------------------------------

     P     8  Style Guide for Python Code                             GvR, Warsaw

     I   257  Docstring Conventions                                   Goodger, GvR

     CPython Development Specific PEPs
     ---------------------------------

     P     7  Style Guide for C Code                                  GvR

     CPython Release PEPs
     --------------------

     P     6  Bug Fix Releases                                        Aahz, Baxter

     I   101  Doing Python Releases 101                               Warsaw, GvR
     I   360  Externally Maintained Packages                          Cannon
     I   373  Python 2.7 Release Schedule                             Peterson
     I   375  Python 3.1 Release Schedule                             Peterson
     I   392  Python 3.2 Release Schedule                             Brandl
     I   398  Python 3.3 Release Schedule                             Brandl

     IF  160  Python 1.6 Release Schedule                             Drake
     IF  200  Python 2.0 Release Schedule                             Hylton
     IF  226  Python 2.1 Release Schedule                             Hylton
     IF  251  Python 2.2 Release Schedule                             Warsaw, GvR
     IF  283  Python 2.3 Release Schedule                             GvR
     IF  320  Python 2.4 Release Schedule                             Warsaw, Hettinger, Baxter
     IF  356  Python 2.5 Release Schedule                             Norwitz, GvR, Baxter
     IF  361  Python 2.6 and 3.0 Release Schedule                     Norwitz, Warsaw

     Python Core Infrastructure PEPs
     -------------------------------

     P   374  Choosing a distributed VCS for the Python project       Cannon, Turnbull, Vassalotti, Warsaw, Ochtman
     P   385  Migrating from Subversion to Mercurial                  Ochtman, Pitrou, Brandl

     PF  347  Migrating the Python CVS to Subversion                  von Löwis

     Python 2 PEPs
     -------------

     IF  291  Backward Compatibility for the Python 2 Standard ...    Norwitz

     Py3k PEPs
     ---------

     P  3000  Python 3000                                             GvR
     P  3002  Procedure for Backwards-Incompatible Changes            Bethard
     P  3003  Python Language Moratorium                              Cannon, Noller, GvR
     P  3099  Things that will Not Change in Python 3000              Brandl

     PW 3001  Procedure for reviewing and improving standard ...      Brandl

     I  3100  Miscellaneous Python 3.0 Plans                          Cannon

     General Use Python PEPs
     -----------------------

     I   290  Code Migration and Modernization                        Hettinger


     Feature and Subject Topics
     ==========================

     Co-Function PEPs
     ----------------

     S   380  Syntax for Delegating to a Subgenerator                 Ewing
     S  3152  Cofunctions                                             Ewing

     SF  342  Coroutines via Enhanced Generators                      GvR, Eby

     IR  220  Coroutines, Generators, Continuations                   McMillan

     Data Security PEPs
     ------------------

     IF  247  API for Cryptographic Hash Functions                    Kuchling
     IF  272  API for Block Encryption Algorithms v1.0                Kuchling

     Database PEPs
     -------------

     IF  248  Python Database API Specification v1.0                  Lemburg
     IF  249  Python Database API Specification v2.0                  Lemburg

     Documentation PEPs
     ------------------

     I   287  reStructuredText Docstring Format                       Goodger

     Generic Functions PEPs
     ----------------------

     S  3124  Overloading, Generic Functions, Interfaces, and ...     Eby

     Importing PEPs
     --------------

     S   369  Post import hooks                                       Heimes

     SF  302  New Import Hooks                                        JvR, Moore

     Interfaces and Abstract Base Classes PEPs
     -----------------------------------------

     S  3124  Overloading, Generic Functions, Interfaces, and ...     Eby

     SF 3119  Introducing Abstract Base Classes                       GvR, Talin

     SR  246  Object Adaptation                                       Martelli, Evans
     SR 3133  Introducing Roles                                       Winter

     Web PEPs
     --------

     IF  333  Python Web Server Gateway Interface v1.0                Eby
     IF 3333  Python Web Server Gateway Interface v1.0.1              Eby

Numerical Index

         num  title                                                   owner
         ---  -----                                                   -----
    * P     1  PEP Purpose and Guidelines                              Warsaw, Hylton, Goodger
    * P     2  Procedure for Adding New Modules                        Faassen
    * PW    3  Guidelines for Handling Bug Reports                     Hylton
    * P     4  Deprecation of Standard Modules                         von Löwis
    * P     5  Guidelines for Language Evolution                       Prescod
    * P     6  Bug Fix Releases                                        Aahz, Baxter
    * P     7  Style Guide for C Code                                  GvR
    * P     8  Style Guide for Python Code                             GvR, Warsaw
    * P     9  Sample Plaintext PEP Template                           Warsaw
    * P    10  Voting Guidelines                                       Warsaw
    * P    11  Removing support for little used platforms              von Löwis
    * P    12  Sample reStructuredText PEP Template                    Goodger, Warsaw

    * I    20  The Zen of Python                                       Peters

    * I    42  Feature Requests                                        Hylton

     SF  100  Python Unicode Integration                              Lemburg
    * I   101  Doing Python Releases 101                               Warsaw, GvR
     IS  102  Doing Python Micro Releases                             Baxter, Warsaw, GvR

    * IF  160  Python 1.6 Release Schedule                             Drake

    * IF  200  Python 2.0 Release Schedule                             Hylton
     SF  201  Lockstep Iteration                                      Warsaw
     SF  202  List Comprehensions                                     Warsaw
     SF  203  Augmented Assignments                                   Wouters
     SR  204  Range Literals                                          Wouters
     SF  205  Weak References                                         Drake
     IW  206  Python Advanced Library                                 Kuchling
     SF  207  Rich Comparisons                                        GvR, Ascher
     SF  208  Reworking the Coercion Model                            Schemenauer, Lemburg
     SW  209  Multi-dimensional Arrays                                Barrett, Oliphant
     SR  210  Decoupling the Interpreter Loop                         Ascher
     SD  211  Adding A New Outer Product Operator                     Wilson
     SD  212  Loop Counter Iteration                                  Schneider-Kamp
     SD  213  Attribute Access Handlers                               Prescod
     SF  214  Extended Print Statement                                Warsaw
     SS  215  String Interpolation                                    Yee
     IR  216  Docstring Format                                        Zadka
     SF  217  Display Hook for Interactive Use                        Zadka
     SF  218  Adding a Built-In Set Object Type                       Wilson, Hettinger
     SD  219  Stackless Python                                        McMillan
    * IR  220  Coroutines, Generators, Continuations                   McMillan
     SF  221  Import As                                               Wouters
     SD  222  Web Library Enhancements                                Kuchling
     SF  223  Change the Meaning of \x Escapes                        Peters
     SR  224  Attribute Docstrings                                    Lemburg
     SD  225  Elementwise/Objectwise Operators                        Zhu, Lielens
    * IF  226  Python 2.1 Release Schedule                             Hylton
     SF  227  Statically Nested Scopes                                Hylton
     SW  228  Reworking Python's Numeric Model                        Zadka, GvR
     SF  229  Using Distutils to Build Python                         Kuchling
     SF  230  Warning Framework                                       GvR
     SR  231  __findattr__()                                          Warsaw
     SF  232  Function Attributes                                     Warsaw
     SD  233  Python Online Help                                      Prescod
     SF  234  Iterators                                               Yee, GvR
     SF  235  Import on Case-Insensitive Platforms                    Peters
     SF  236  Back to the __future__                                  Peters
     SF  237  Unifying Long Integers and Integers                     Zadka, GvR
     SF  238  Changing the Division Operator                          Zadka, GvR
     SR  239  Adding a Rational Type to Python                        Craig, Zadka
     SR  240  Adding a Rational Literal to Python                     Craig, Zadka
     SF  241  Metadata for Python Software Packages                   Kuchling
     SR  242  Numeric Kinds                                           Dubois
     SW  243  Module Repository Upload Mechanism                      Reifschneider
     SR  244  The `directive' statement                               von Löwis
     SR  245  Python Interface Syntax                                 Pelletier
    * SR  246  Object Adaptation                                       Martelli, Evans
    * IF  247  API for Cryptographic Hash Functions                    Kuchling
    * IF  248  Python Database API Specification v1.0                  Lemburg
    * IF  249  Python Database API Specification v2.0                  Lemburg
     SF  250  Using site-packages on Windows                          Moore
    * IF  251  Python 2.2 Release Schedule                             Warsaw, GvR
     SF  252  Making Types Look More Like Classes                     GvR
     SF  253  Subtyping Built-in Types                                GvR
     SR  254  Making Classes Look More Like Types                     GvR
     SF  255  Simple Generators                                       Schemenauer, Peters, Hetland
     SR  256  Docstring Processing System Framework                   Goodger
    * I   257  Docstring Conventions                                   Goodger, GvR
     SR  258  Docutils Design Specification                           Goodger
     SR  259  Omit printing newline after newline                     GvR
     SF  260  Simplify xrange()                                       GvR
     SF  261  Support for "wide" Unicode characters                   Prescod
     SD  262  A Database of Installed Python Packages                 Kuchling
     SF  263  Defining Python Source Code Encodings                   Lemburg, von Löwis
     SF  264  Future statements in simulated shells                   Hudson
     SR  265  Sorting Dictionaries by Value                           Griffin
     SW  266  Optimizing Global Variable/Attribute Access             Montanaro
     SD  267  Optimized Access to Module Namespaces                   Hylton
     SR  268  Extended HTTP functionality and WebDAV                  Stein
     SD  269  Pgen Module for Python                                  Riehl
     SR  270  uniq method for list objects                            Petrone
     SR  271  Prefixing sys.path by command line option               Giacometti
    * IF  272  API for Block Encryption Algorithms v1.0                Kuchling
     SF  273  Import Modules from Zip Archives                        Ahlstrom
     SW  274  Dict Comprehensions                                     Warsaw
     SR  275  Switching on Multiple Values                            Lemburg
     SR  276  Simple Iterator for ints                                Althoff
     SF  277  Unicode file name support for Windows NT                Hodgson
     SF  278  Universal Newline Support                               Jansen
     SF  279  The enumerate() built-in function                       Hettinger
     SD  280  Optimizing access to globals                            GvR
     SR  281  Loop Counter Iteration with range and xrange            Hetland
     SF  282  A Logging System                                        Sajip, Mick
    * IF  283  Python 2.3 Release Schedule                             GvR
     SR  284  Integer for-loops                                       Eppstein, Ewing
     SF  285  Adding a bool type                                      GvR
     S   286  Enhanced Argument Tuples                                von Löwis
    * I   287  reStructuredText Docstring Format                       Goodger
     SW  288  Generators Attributes and Exceptions                    Hettinger
     SF  289  Generator Expressions                                   Hettinger
    * I   290  Code Migration and Modernization                        Hettinger
    * IF  291  Backward Compatibility for the Python 2 Standard ...    Norwitz
     SF  292  Simpler String Substitutions                            Warsaw
     SF  293  Codec Error Handling Callbacks                          Dörwald
     SR  294  Type Names in the types Module                          Tirosh
     SR  295  Interpretation of multiline string constants            Koltsov
     SW  296  Adding a bytes Object Type                              Gilbert
     SR  297  Support for System Upgrades                             Lemburg
     SW  298  The Locked Buffer Interface                             Heller
     SR  299  Special __main__() function in modules                  Epler

     SF  301  Package Index and Metadata for Distutils                Jones
    * SF  302  New Import Hooks                                        JvR, Moore
     SR  303  Extend divmod() for Multiple Divisors                   Bellman
     SW  304  Controlling Generation of Bytecode Files                Montanaro
     SF  305  CSV File API                                            Altis, Cole, McNamara, Montanaro, Wells
     IW  306  How to Change Python's Grammar                          Hudson, Diederich, Coghlan, Peterson
     SF  307  Extensions to the pickle protocol                       GvR, Peters
     SF  308  Conditional Expressions                                 GvR, Hettinger
     SF  309  Partial Function Application                            Harris
     SR  310  Reliable Acquisition/Release Pairs                      Hudson, Moore
     SF  311  Simplified Global Interpreter Lock Acquisition for ...  Hammond
     SD  312  Simple Implicit Lambda                                  Suzi, Martelli
     SR  313  Adding Roman Numeral Literals to Python                 Meyer
     SF  314  Metadata for Python Software Packages v1.1              Kuchling, Jones
     SD  315  Enhanced While Loop                                     Hettinger, Carroll
     SD  316  Programming by Contract for Python                      Way
     SR  317  Eliminate Implicit Exception Instantiation              Taschuk
     SF  318  Decorators for Functions and Methods                    Smith
     SR  319  Python Synchronize/Asynchronize Block                   Pelletier
    * IF  320  Python 2.4 Release Schedule                             Warsaw, Hettinger, Baxter
     SW  321  Date/Time Parsing and Formatting                        Kuchling
     SF  322  Reverse Iteration                                       Hettinger
     SD  323  Copyable Iterators                                      Martelli
     SF  324  subprocess - New process module                         Astrand
     SR  325  Resource-Release Support for Generators                 Pedroni
     SR  326  A Case for Top and Bottom Values                        Carlson, Reedy
     SF  327  Decimal Data Type                                       Batista
     SF  328  Imports: Multi-Line and Absolute/Relative               Aahz
     SR  329  Treating Builtins as Constants in the Standard Library  Hettinger
     SR  330  Python Bytecode Verification                            Pelletier
     SF  331  Locale-Independent Float/String Conversions             Reis
     SR  332  Byte vectors and String/Unicode Unification             Montanaro
    * IF  333  Python Web Server Gateway Interface v1.0                Eby
     SW  334  Simple Coroutines via SuspendIteration                  Evans
     S   335  Overloadable Boolean Operators                          Ewing
     SR  336  Make None Callable                                      McClelland
     S   337  Logging Usage in the Standard Library                   Dubner
     SF  338  Executing modules as scripts                            Coghlan
     IW  339  Design of the CPython Compiler                          Cannon
     SR  340  Anonymous Block Statements                              GvR
     SF  341  Unifying try-except and try-finally                     Brandl
    * SF  342  Coroutines via Enhanced Generators                      GvR, Eby
     SF  343  The "with" Statement                                    GvR, Coghlan
     SS  344  Exception Chaining and Embedded Tracebacks              Yee
     SA  345  Metadata for Python Software Packages 1.2               Jones
     SW  346  User Defined ("``with``") Statements                    Coghlan
    * PF  347  Migrating the Python CVS to Subversion                  von Löwis
     SR  348  Exception Reorganization for Python 3.0                 Cannon
     SD  349  Allow str() to return unicode strings                   Schemenauer
     IR  350  Codetags                                                Elliott
     SR  351  The freeze protocol                                     Warsaw
     SF  352  Required Superclass for Exceptions                      Cannon, GvR
     SF  353  Using ssize_t as the index type                         von Löwis
     SR  354  Enumerations in Python                                  Finney
     SR  355  Path - Object oriented filesystem paths                 Lindqvist
    * IF  356  Python 2.5 Release Schedule                             Norwitz, GvR, Baxter
     SF  357  Allowing Any Object to be Used for Slicing              Oliphant
     SF  358  The "bytes" Object                                      Schemenauer, GvR
     SW  359  The "make" Statement                                    Bethard
    * I   360  Externally Maintained Packages                          Cannon
    * IF  361  Python 2.6 and 3.0 Release Schedule                     Norwitz, Warsaw
     S   362  Function Signature Object                               Cannon, Seo
     SR  363  Syntax For Dynamic Attribute Access                     North
     SW  364  Transitioning to the Py3K Standard Library              Warsaw
     SR  365  Adding the pkg_resources module                         Eby
     SF  366  Main module explicit relative imports                   Coghlan
     SS  367  New Super                                               Spealman, Delaney
     S   368  Standard image protocol and class                       Mastrodomenico
    * S   369  Post import hooks                                       Heimes
     SF  370  Per user site-packages directory                        Heimes
     SF  371  Addition of the multiprocessing package to the ...      Noller, Oudkerk
     SF  372  Adding an ordered dictionary to collections             Ronacher, Hettinger
    * I   373  Python 2.7 Release Schedule                             Peterson
    * P   374  Choosing a distributed VCS for the Python project       Cannon, Turnbull, Vassalotti, Warsaw, Ochtman
    * I   375  Python 3.1 Release Schedule                             Peterson
     SA  376  Database of Installed Python Distributions              Ziadé
     SR  377  Allow __enter__() methods to skip the statement body    Coghlan
     SF  378  Format Specifier for Thousands Separator                Hettinger
     SW  379  Adding an Assignment Expression                         Whitley
    * S   380  Syntax for Delegating to a Subgenerator                 Ewing
     S   381  Mirroring infrastructure for PyPI                       Ziadé, v. Löwis
     S   382  Namespace Packages                                      v. Löwis
     SF  383  Non-decodable Bytes in System Character Interfaces      v. Löwis
     SF  384  Defining a Stable ABI                                   v. Löwis
    * P   385  Migrating from Subversion to Mercurial                  Ochtman, Pitrou, Brandl
     SA  386  Changing the version comparison module in Distutils     Ziadé
    * P   387  Backwards Compatibility Policy                          Peterson

     SA  389  argparse - New Command Line Parsing Module              Bethard
     S   390  Static metadata for Distutils                           Ziadé
     SA  391  Dictionary-Based Configuration For Logging              Sajip
    * I   392  Python 3.2 Release Schedule                             Brandl
     S   393  Flexible String Representation                          v. Löwis
     I   394  The "python" command on Unix-Like Systems               Staley, Coghlan
     S   395  Module Aliasing                                         Coghlan
     I   396  Module Version Numbers                                  Warsaw
     S   397  Python launcher for Windows                             Hammond
    * I   398  Python 3.3 Release Schedule                             Brandl
     I   399  Pure Python/C Accelerator Module Compatibility ...      Cannon

     PR  401  BDFL Retirement                                         Warsaw, Cannon

     I   444  Python Web3 Interface                                   McDonough, Ronacher

     SR  666  Reject Foolish Indentation                              Creighton

     SR  754  IEEE 754 Floating Point Special Values                  Warnes

    * P  3000  Python 3000                                             GvR
    * PW 3001  Procedure for reviewing and improving standard ...      Brandl
    * P  3002  Procedure for Backwards-Incompatible Changes            Bethard
    * P  3003  Python Language Moratorium                              Cannon, Noller, GvR

    * P  3099  Things that will Not Change in Python 3000              Brandl
    * I  3100  Miscellaneous Python 3.0 Plans                          Cannon
     SF 3101  Advanced String Formatting                              Talin
     SF 3102  Keyword-Only Arguments                                  Talin
     SR 3103  A Switch/Case Statement                                 GvR
     SF 3104  Access to Names in Outer Scopes                         Yee
     SF 3105  Make print a function                                   Brandl
     SF 3106  Revamping dict.keys(), .values() and .items()           GvR
     SF 3107  Function Annotations                                    Winter, Lownds
     SA 3108  Standard Library Reorganization                         Cannon
     SF 3109  Raising Exceptions in Python 3000                       Winter
     SF 3110  Catching Exceptions in Python 3000                      Winter
     SF 3111  Simple input built-in in Python 3000                    Roberge
     SF 3112  Bytes literals in Python 3000                           Orendorff
     SF 3113  Removal of Tuple Parameter Unpacking                    Cannon
     SF 3114  Renaming iterator.next() to iterator.__next__()         Yee
     SF 3115  Metaclasses in Python 3000                              Talin
     SF 3116  New I/O                                                 Stutzbach, GvR, Verdone
     SR 3117  Postfix type declarations                               Brandl
     SA 3118  Revising the buffer protocol                            Oliphant, Banks
    * SF 3119  Introducing Abstract Base Classes                       GvR, Talin
     SF 3120  Using UTF-8 as the default source encoding              von Löwis
     SA 3121  Extension Module Initialization and Finalization        von Löwis
     SR 3122  Delineation of the main module                          Cannon
     SF 3123  Making PyObject_HEAD conform to standard C              von Löwis
    * S  3124  Overloading, Generic Functions, Interfaces, and ...     Eby
     SR 3125  Remove Backslash Continuation                           Jewett
     SR 3126  Remove Implicit String Concatenation                    Jewett, Hettinger
     SF 3127  Integer Literal Support and Syntax                      Maupin
     SR 3128  BList: A Faster List-like Type                          Stutzbach
     SF 3129  Class Decorators                                        Winter
     SR 3130  Access to Current Module/Class/Function                 Jewett
     SF 3131  Supporting Non-ASCII Identifiers                        von Löwis
     SF 3132  Extended Iterable Unpacking                             Brandl
    * SR 3133  Introducing Roles                                       Winter
     SF 3134  Exception Chaining and Embedded Tracebacks              Yee
     SA 3135  New Super                                               Spealman, Delaney, Ryan
     SR 3136  Labeled break and continue                              Chisholm
     SF 3137  Immutable Bytes and Mutable Buffer                      GvR
     SF 3138  String representation in Python 3000                    Ishimoto
     SR 3139  Cleaning out sys and the "interpreter" module           Peterson
     SR 3140  str(container) should call str(item), not repr(item)    Broytmann, Jewett
     SF 3141  A Type Hierarchy for Numbers                            Yasskin
     S  3142  Add a "while" clause to generator expressions           Britton
     S  3143  Standard daemon process library                         Finney
     S  3144  IP Address Manipulation Library for the Python ...      Moody
     S  3145  Asynchronous I/O For subprocess.Popen                   Pruitt, McCreary, Carlson
     SA 3146  Merging Unladen Swallow into CPython                    Winter, Yasskin, Kleckner
     SF 3147  PYC Repository Directories                              Warsaw
     SF 3148  futures - execute computations asynchronously           Quinlan
     SF 3149  ABI version tagged .so files                            Warsaw
     SD 3150  Statement local namespaces (aka "given" clause)         Coghlan
     S  3151  Reworking the OS and IO exception hierarchy             Pitrou
    * S  3152  Cofunctions                                             Ewing

    * IF 3333  Python Web Server Gateway Interface v1.0.1              Eby

    Category Key
        S - Standards Track PEP
        I - Informational PEP
        P - Process PEP

        A - Accepted proposal
        R - Rejected proposal
        W - Withdrawn proposal
        D - Deferred proposal
        F - Final proposal
        A - Active proposal
        D - Draft proposal
        S - Superseded proposal

------------------------------------------------------------------------

[CategoryDocumentation](CategoryDocumentation)
