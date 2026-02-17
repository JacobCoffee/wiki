# PyPiTestServer

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# Create a server that tests uploaded packages on PyPI. 

## Work to be done 

The work is separated into three steps:

1.  a solution capable of running scripts when an event occurs (a new release of project X is available on PyPI)
2.  a Continuous integration server able to run the testsuite for those distributions
3.  a quality mesurement tool, able to provide feedback and indicators on the code (compliance PEP8, pyflakes, potentially malicious softwares etc.)

## Resources 

\- [2010 idea](http://tarekziade.wordpress.com/2010/03/21/another-gsoc-idea-a-pypi-testing-infrastructure/) and [code](https://bitbucket.org/mouad/pypi-testing-infrastructure-pyti/overview)

\- [2011 updated idea](http://tarekziade.wordpress.com/2011/02/21/qa-portal-ideas/)

\- On this wiki: [PyPITestingInfrastructure](PyPITestingInfrastructure)

## What do people want 

### What do people what to run 

- Run quality indicators about the code
- Run quality indicators about the packaging (compat with du2 standards for instance)
- Run Test
- Run setup.

### What do people what to know 

- Report about the run itself (does the test pass ? does the install went well ?)
- Report about system access done (FS network)
- Report about resource used ? (bonus)
