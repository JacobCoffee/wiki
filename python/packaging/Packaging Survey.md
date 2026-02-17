# Packaging Survey

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

This survey will be put online in a [SurveyMonkey](./SurveyMonkey.html)-like system whenever it is ready\...

# 1. Part 1, how do you work ? 

- Who are you ? (one answer)
  1.  Professional developer using Python exclusively.
  2.  Professional developer using Python sometimes.
  3.  Professional developer using Python unable to use Python \"at work\".
  4.  Hobbyist using Python.

- How do you organize your application code most of the time ? (one answer)
  1.  I put everything in one package
  2.  I create several packages and use a main package or script to launch the application
  3.  I create several packages and use a tool like zc.buildout or Paver to distribute the whole application
  4.  I use my own mechanism for aggregating packages into a single install.

- For libraries you don\'t distribute publicly, do you you create a setup.py script? (one answer)
  1.  Yes
  2.  No

- What is the main tool or combination of tools you are using to package and distribute your Python application ? (one answer)
  1.  None

  2.  distutils

  3.  setuptools

  4.  zc.buildout and setuptools

  5.  zc.buildout and distutils

  6.  Paver and distutils

  7.  Paver and setuptools

  8.  Other : \<say which\>

- How do you install a package that does not provide an standalone installer (but provides a standard setup.py script) most of the time ? (one answer)
  1.  I use easy_install

  2.  I use pip

  3.  I download it and manually run the `python setup.py install`{.backtick} command

  4.  I use the packaging tool provided in my system (apt, yum, etc)

  5.  I move files around and create symlinks manually

  6.  Other : \<say which\>

- How do you remove a package ? (check all that apply)
  1.  manually, by removing the folder and fixing the .pth files
  2.  using the packaging tool (apt, yum, etc)
  3.  I use one virtualenv per application, so the main python is never polluted, and only remove entire environments
  4.  I change PYTHONPATH to include a directory of the packages used by my application, then remove just that directory
  5.  I don\'t know / I fail at uninstallation

- How do you manage using more than one version of a library on a system? (check all that apply)
  1.  I don\'t use multiple versions of a library

  2.  I use setuptools\' multi-version features

  3.  I use virtualenv

  4.  I use zc.buildout

  5.  I build fresh Python interpreter from source for each project

  6.  I set PYTHONPATH to select particular libraries

  7.  I set sys.path in my scripts

  8.  Other: \<say what\>

- Do you work with setuptools\' namespaced packages ? A namespace package is a package that may be split across multiple project distributions. For example, Zope 3\'s zope package is a namespace package, because subpackages like zope.interface and zope.publisher may be distributed separately (see [http://peak.telecommunity.com/DevCenter/setuptools](http://peak.telecommunity.com/DevCenter/setuptools)) (one answer)

  1.  Yes
  2.  No

- Has PyPI become mandatory in your everyday work (if you use zc.buildout for example) ? (one answer)
  1.  Yes
  2.  No

- If you previously answered Yes, did you set up an alternative solution (mirror, cache..) in case PyPI is down ? (one answer)
  1.  Yes
  2.  No

- Do you register your packages to PyPI ? (one answer)
  1.  Yes
  2.  No

- Do you upload your package to PyPI ? (one answer)
  1.  Yes
  2.  No

- If you previously answered No, how do you distribute your packages ? (one answer)
  1.  One my own website, using simple links
  2.  One my own website, using a PyPI-like server
  3.  On a forge, like sourceforge

- Where are you located ?
  - \<open question\>

# 2. Part 2, What\'s missing ? What is wrong ? 

- What are in your opinion, the 5 most important problems (bad behaviors or missing features) in Distutils today ?
  - \<open question\>
- What are the 5 most important features that exists in third-party tools, you would like to see included by the Python standard Library ?
  - \<open question\>
- What are the other things you like to say in order to help building Distutils roadmap ?
  - \<open question\>

------------------------------------------------------------------------

# 3. Questions 

1.  Regarding the questions that ask \"what are the 5 most important X\", is it possible for the survey to instead list a number of choices and let the person taking the survey rank them from most- to least-important?
    - You probably don\'t know all the possible answers. Ask the user \"What are they?\" and they will tell you. Ask the user \"Which of these\", and they tend to think only of the choices on your list.
