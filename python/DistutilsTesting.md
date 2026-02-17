# DistutilsTesting

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

One problem with developing the Distutils is that there\'s no functional test suite, so figuring out if a change broke something is a scatter-shot process. (There are no unit tests either, but we\'re talking about functional tests here.) You might try building a few packages such as mxBase or PyXML, but you have no idea if everything was exercised. I\'d really like to have a testing mechanism before beginning to make significant changes; without one we might have lots of inadvertent breakage.

Testing the Distutils is difficult for two reasons:

1.  you need an entire directory for each test, containing a setup.py plus whatever source files are necessary.
2.  you really need to run an install command and check that the files wound up installed to the right place.

This page collects ideas and requirements for a Distutils test suite.

Here\'s a vague straw-man proposal:

- We have a bunch of directories in Python CVS containing example setup.py files. They might live in the nondist portion of the Python CVS tree, or in dist/distutils.

- The test script loops over these directories and does \"python setup.py install\" in all of them. \--prefix is set to some temporary directory so all files are installed to this temporary tree.

- Each directory contains a file named \"results\". If the test case is expected to fail, the first line of the file is \"#invalid\", and the rest of the file is the expected error message. If the test case is expected to succeed, the first line of the file is \"#valid\". The rest of the file is Python code that will be executed to check various things. It might be doctest code, with some pre-defined testing methods. Imaginary example:

          >>> import example     # You should be able to import the package ...
          >>> from example import subpackage   # ... and a subpackage.
          >>> exists(join(prefix, "bin", "script"))  # script should be installed
          True
          >>> # It should have compiled the .py file
          ... exists(join(prefix, "lib", PYTHON_VERSION, "example", "__init__.pyc"))
          True 

- There should be some sort of cumulative code coverage so that we can tell if the test cases exercise every possible branch of code.
