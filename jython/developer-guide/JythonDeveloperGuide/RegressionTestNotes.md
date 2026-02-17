# JythonDeveloperGuide/RegressionTestNotes

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# Windows regrtest failures

1 tests failed:
:   test_java_integration

- test_java_integration - jython.bat needs (or \'should\' as there\'s absolutely nothing subprocess can do about it) to strip surrounding quotes from command line arguments

Also still problematic:

- test_mailbox - fails so horribly that it\'s temporarily disabled from regrtest \--expected. Leaves open file handles among other things, see [http://fisheye3.atlassian.com/changelog/jython?cs=6427&csize=3](http://fisheye3.atlassian.com/changelog/jython?cs=6427&csize=3) for related fixes done to test_old_mailbox
- test_subprocess - test_communicate_pipe_buf [http://bugs.jython.org/issue1356](http://bugs.jython.org/issue1356)
