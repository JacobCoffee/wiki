# Distutils/DistributeSprint

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# Tasks for the sprint 

- A new \"generate manifest\" build command that will generate the MANIFEST file. and be pluggable. target: replace the Distutils builtin MANIFEST.in system (that will be just a plugin) - Yannick Gringas
- cleanup, test and try out \"distribute.resources\": ronny, iElectric
- buildbot, test coverage, QA; lead: ssteinerX
- reimplement the develop command, lead: agronholm
- reimplement python setup.py install \-- determine strategy wrt pip, lead: jezdez + tarek, carljm
- workon PEP 376 : tarek, carljm (lead)

# Sprint results 

- develop command:
  - Created a skeleton command for develop
  - Waiting for work to complete on the install and build_egg_info commands before work can continue here.
- build_egg_info command:
  - Rewrote this command using setuptools code as a model
  - Removed all SVN support code
  - Removed obsolete egg-info writers
  - Waiting on the manifest generation feature to finish this one
  - Will implement PEP 376 egg-info writers when possible
- PEP 376 compatible installs
  - Observations
    - Current setuptools egg-info metadata is written in a separate pre-install in-place step, which can be run independently (python setup.py egg-info). PEP 376 metadata (RECORD, INSTALLER and REQUESTED) can only be generated at install time, not in a separate step (RECORD needs actual installed paths, and REQUESTED and INSTALLED are determined by who does the install and why).
    - RECORD generation is similar to distutils\' existing \--record option, but that is implemented in a non-extendable way (buried in the midst of run() method)

  - Decided that a proof-of-concept implementation of PEP 376 installs would be cleaner and clearer if implemented directly in distutils (in a standalone branch for now), rather than layering it into distribute 0.7 on top of current distutils. Ideally this distutils branch could be installed for testing just like the distutils nightly builds at [http://nightly.ziade.org](http://nightly.ziade.org) on all recent Python versions.

  - Converted distutils into standalone hg repo at [http://bitbucket.org/carljm/python-distutils/](http://bitbucket.org/carljm/python-distutils/)

  - Currently working on testing strategy.
    - Can distutils tests be made to run apart from the full Python build tree?
    - First step will be to modify/add tests to specify PEP 376 behavior.
