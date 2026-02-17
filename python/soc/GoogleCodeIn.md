# GoogleCodeIn

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

This list is by no means complete, we\'re still getting our mentors lined up for this program and are waiting for confirmation to be a mentoring org before setting up all the 3rd party projects that have been a bulk of our students in past years GSoC/GHOP.

# Code 

- [http://bugs.python.org/issue9517](http://bugs.python.org/issue9517) improve test.script_helper \[median\] (stdlib)

- Eliminate resource warnings in test_subprocess \[expert\] (stdlib)

- [http://bugs.python.org/issue9856](http://bugs.python.org/issue9856) add a deprecation warning to object.[format](s) when s is non-empty \[median\] (c)

- [http://bugs.python.org/issue9858](http://bugs.python.org/issue9858) Bring Python and C io library implementations in sync \[expert\] (stdlib)

- [http://bugs.python.org/issue940286](http://bugs.python.org/issue940286) Fix pydoc.Helper.help() to use the input output parameters \[novice\] (stdlib)

- Merge test_globals into test_scope \[novice\] (stdlib)

- Improve the test coverage of imaplib. \[median\] (stdlib)

- Merge test_smtpnet into test_smtplib. \[novice\] (stdlib)

- Adapt test_stringprep to download the data file to test its module against.

- Write tests for getpass.py. \[median\] (stdlib)

- Write tests for tabnanny.py. You may need to extend the api to make it more testable. \[median\] (stdlib)

- Write tests for formatter.py. \[median\] (stdlib)

- Add tests for the code module. \[median\] (stdlib)

- Add tests for cgitb.py. \[median\] (stdlib)

- Refactor Distutils2 command line tools so it uses argparse \[median\] (packaging)

- Refactor test_zipfile to properly clean up its resources in a nice way \[median\] (stdlib)

# Documentation 

- Complete documentation for the wsgiref module \[median\] (stdlib, wsgi)

- Write docs for undocumented urllib functions ([http://bugs.python.org/issue1722](http://bugs.python.org/issue1722)) \[median\] (stdlib)

# Outreach 

- Write an article about the advantages of Python 3 over 2.x \[novice\]

# Quality Assurance 

- Clean up Distutils2 code using \"pep8\" and \"pyflake\" (or \"flake8\") \[novice\] (packaging)

# Research 

- Find all Django dependencies that still need to be ported to Python 3 \[expert\] (wsgi)
- Find all Turbogears dependencies that still need to be ported to Python 3 \[median\] (wsgi)

# Training 

# Translation 

# User Interface 

- Enhance the Distutils2 mkcfg wizard (script to create a Distutils2 package) \[median\] (packaging)

------------------------------------------------------------------------

# Adding new tasks 

Add new tasks only in the above 8 categories.

Within each category tasks should sorted by experience level:

1.  Novice - these tasks can be done by someone with no experience working with the project
2.  Median - these tasks are suitable for someone with some experience in a project
3.  Expert - these tasks require knowledge in a specific field or extreme familiarity with a project

Task ideas should be tagged with the subproject they should be mentored for, currently:

- stdlib - Python\'s Standard Library
- packaging - The distutils (stdlib) or distutils2 projects
- wsgi - Web Service Gateway Interface and related packages
