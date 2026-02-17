# TestingJython

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

## TestingJython 

A few notes on the various Jython test collections.

### regrtest

A large collection of test cases, many direct from CPython sources and others specific to Jython in some way, are placed in dist/Lib/test by the standard build process. These can be run standalone, or executed using the regrtest driver. After you have successfully built jython (see [JythonDeveloperGuide](JythonDeveloperGuide) for details), you can run all these tests by executing:

    jython dist/Lib/test/regrtest.py -e

or alternatively to run a single test case:

    jython dist/Lib/test/regrtest.py test_descr

To produce more verbose output:

    jython dist/Lib/test/regrtest.py -v test_descr

Run regrtest with -h to see the full list of options.

Some tests can take arguments as well, in which case it can be more convenient to execute them directly. eg to run just the \'ints\' testcase from test_descr:

    jython dist/Lib/test/test_descr.py ints

Note that running

    ant regrtest

should run the full suite using your development build.

### bugtests

A Jython-specific collection of regression tests covering various bug fixes. This suite has its own test driver and requires separate cofiguration. README.txt in the bugtests directory provides details, in summary you need to create a file support_config.py with settings for java_home, jython_home, and classpath, eg from the README\'s example:

    java_home = "/Library/Java/Home"
    jython_home = "/Users/bzimmer/Development/sourceforge/jython/dist"
    classpath = jython_home + "/jython.jar:classes"

Once this is configured you can run all the bugtests (note in these examples we are working directly is the bugtests folder):

    jython driver.py

which will produce \'OK\', \'Failure\', \'Warning\' (which may indicate a known problem that has not been resolved - see the README), or \'Skipped\' (the test was not found) for each test case. Failures will have full details printed but warnings do not by default. To get warning details run with loud_warnings enabled:

    jython driver.py -w

You can specify a subset of tests to run by number by a comma separated list (no spaces):

    jython driver.py 50,51,180

If you haven\'t configured support_config.py, but have your development environment successfully compiling jython via ant, try running:

    ant create-bugtest-config

This should create a bugtests/support_config.py suitable for dev setup. Or just try:

    ant bugtest

This will execute the tests using your development build, and should create a support_config.py if not already there. If a support_config.py already exists (say you created one by hand or had to edit the auto-generated version) it will be used without change.

### zxJDBC tests 

In Lib/test/zxjdbc is yet another set of test cases covering the zxJDBC database api. For these tests you need to configure the databases you have available in an xml config file (see the included test.xml for examples), then execute the driver \'runner.py\' for some particular db:

    jython runner.py postgresql

or

    jython runner.py

to run the tests for all configured db\'s.

### misc tests 

In Lib/test/bugs is another set of test cases, seemingly from bug reports as they are named prXYZ.py. No clue yet what drives them or if they are included from another test case somewhere, guidance appreciated!
