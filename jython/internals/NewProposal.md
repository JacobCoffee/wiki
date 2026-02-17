# NewProposal

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

Proposed Jython Users Guide TOC JUG = Jython User Guide DCN = Dave\'s class notes

SECTION I - BASIC JYTHON

- Introduction
  - General Python Documentation

  <!-- -->

  - 2 What is Python? 3 What is Jython? 4 Differences between Jython and CPython

  14 Installing and Running Jython
  - Requirements & Where to download

    - JVM Python

  14.2 Install Jython
  - Unix/linux MS Windows

  14.3 Basic Configuration
  - Command-line options Jython configuration files Checking configuration values Classpath and python path

<!-- -->

- 14.4 Running Jython
  - Invoking the Jython Interpreter
    - o Making Jython Scripts Executable

SECTION II - INTRODUCTION TO PYTHON

- If your new to python / jython programming
  - basic coverage more info

  5 Lexical matters
  - 5.1 Lines 5.2 Names and tokens 5.3 Blocks and indentation 5.4 Doc strings 5.5 Program structure 5.6 Operators 5.7 Code evaluation

  6 Built-in datatypes
  - 6.1 Numeric types (add bool) 6.2 Tuples and lists 6.3 Strings 6.4 Dictionaries 6.5 Files
    - 12.1 File input and output

  7 Statements
  - 7.1 Assignment
    - 9.2 Global variables and the global statement

  <!-- -->

  - 9.2.1 Doc strings for functions
    - 11.1.1 Doc strings for functions
      - 10.12 Doc strings

      7.2 import 7.3 print 7.4 if: elif: else: 9.3 lambda 7.5 try: except: 7.6 raise 8.1 for 8.2 while 8.3 continue and break 8.4 del

  9 Functions (maybe there is a better name or location for this)
  - 9.1 Arguments

  <!-- -->

  - 9.4 Iterators and generators 12.2 Unit tests 12.3 doctest 12.4 Installing Python packages
    - \+ 12.4.1 Python packages + 12.4.2 Jython packages

  10 Classes
  - 10.1 A simple class 10.2 Creating instances 10.3 Defining methods 10.4 The constructor 10.5 Member variables 10.8 Class variables 10.6 Methods 10.7 Adding inheritance 10.9 Class methods 10.10 Interfaces 10.11 New-style classes

  11 Modules, Packages, and Debugging
  - 11.1 Modules 11.2 Packages 11.3 Debugging tools

SECTION II - INTEGRATING JAVA INTO PYTHON

- Introduction

  - Using Java with Jython Advanced Python

  Database connectivity in Jython

  - 19.3 Database access
    - \+ 19.3.1 JDBC + 19.3.2 zxJDBC

  <!-- -->

  - o Using a [DataSource](./DataSource.html) (or [ConnectionPooledDataSource](./ConnectionPooledDataSource.html)) o Using a JNDI lookup

    - Getting a Cursor

      - \+ SQL Server + Oracle

      Datatype mapping callbacks through [DataHandler](./DataHandler.html)

      - \+ life cycle + developer support + binding prepared statements + building results + callable statement support

    o dbexts o Configuration file o API o Example session

  Interaction with Java Packages

  - o Accessing Java from Jython o More Details o Importing o Creating Class Instances o Calling Java Methods and Functions o Overloaded Java Method Signatures o Naming Conflicts with Python Keywords

  Converting Java to Jython

  - (stuff on how to convert java into Jython like the last part of Jython Essencials)

  [JavaBean](./JavaBean.html) Properties (own section or part of previous one?)

  - o Properties o Tuples o Event Properties o Methods, Properties and Event Properties

  Java Arrays 15 Calling Java from Jython

  - o 15.1 Calling existing Java code

  15.2 Preparing Java code to be called from Jython

  - \+ 15.2.1 A simple class, doc strings, etc + 15.2.2 Working with Jython arguments + 15.2.3 Sub-classing a Java class + 15.2.4 Emulating Jython Dictionaries, Sequences, Etc. + 15.2.5 Emulating Jython object attribute access

  Subclassing Java Classes in Jython

  - A Short Example Calling Methods in Your Superclass Invoking Your Superclass\'s Constructor

  Java Reload (experimental) simple Support - JReload

  - o Example o Java Classes Unloading o Java 1.1 o JReload Example Source Files

  19 Advanced Topics

  - 19.1 Event handling 19.2 XML
    - \+ 19.2.1 jaxp + 19.2.2 Xerces + 19.2.3 dom4j

SECTION III - INTEGRATING JYTHON INTO JAVA

- I don\'t know what would go here.

SECTION THREE - JYTHON REFERENCE

- Introduction (is this needed here?) Jython specific stuff. not sure what all may go here. Jython Configuration (more detailed then above)
  - Command-line options Jython configuration files Checking configuration values Classpath and python path
    - Running Jython Running jythonc

  The Jython Registry
  - o Registry Properties o Finding the Registry File

  Embedding Jython (merge JUG and DCN) 17 Embedding the Jython Interpreter
  - o 17.1 It\'s simple o 17.2 But, there are a few complexities o 17.3 Exposing transparent objects o 17.4 Exposing opaque objects o 17.5 Type conversion

  18 Embedding and Extending \-- A Summary 16 Compiling Jython to and for Java
  - o 16.1 Calling Jython Code from Jython o 16.2 Calling Jython Code from Java o 16.3 Another example \-- Jython-2.2a/Demo/javaclasses

  21 References and Sources
  - python.org books
    - jython essentials other books dive into python effbot

  <!-- -->

  - o Other Useful Links

  22 Credits - people that contributed to this effort.

Index! If this is more of an online doc then maybe its not needed
