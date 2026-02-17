# MigrateBugtests

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

Jython currently runs many of the tests from CPython\'s std lib in addition to some of its own tests written in the same style. It also has a stepchild of a test directory, bugtests. These are over 400 individual test modules that each contain a single test case. Many of the tests in them are valuable and should be run regularly as part of Jython development, but there are also tests for features that have changed or gone away which have been disabled for years. As part of the 2.5 process, we\'re going through and converting the valuable tests into unittest.[TestCases](./TestCases.html) like our main body of tests, and discarding the ones whose time has passed.

Tests of using and extending Java should be added to Lib/test/test_java_integration.py. Any Java code used by the test should be moved to tests/java.

For tests of Python features, first check if the test is valid for Python 2.5. If it\'s no longer supported in Python, just delete it and make a note of why you deleted it. If it is valid, check if there\'s an equivalent test in Lib/test or CPythonLib/test. If so, delete it and note why.

If a test doesn\'t meet any of those criteria, then it should be migrated into a test file for the module it\'s testing in Lib/test. The general naming convention for tests like this should be test\_\<module name\>\_jy.py. Since there\'s usually already a test in CPythonLib for a given module, \_jy is appended to allow them to all run side by side. If a \_jy test already exists for the module, just migrate this test into it. If not, create a new \_jy test for it in the style of test_str_jy or test_dict_jy.

Tests that raise support.[TestWarning](./TestWarning.html) are for bugs that have been identified but not yet fixed. It\'s probably worth asking if the problem it\'s hiding is worth fixing or if the test should just be tossed.

Tests 1-75 have already been migrated, but 76-400 remain to be done.
