# SummerOfCode/2016/python-core

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# About Core Python 

Core Python encompasses projects that affect the core infrastructure, libraries and CPython.

# Getting Started 

The website to help you get started in Core Python development is [http://pythonmentors.com/](http://pythonmentors.com/).

# Contact info 

To chat with the Core Python mentors, please use the [core-mentorship@python.org](mailto:core-mentorship@python.org) mailing list. [Sign up](https://mail.python.org/mailman/listinfo/core-mentorship)

# Ideas 

Core Python is still getting its ideas page together, please ask on the mailing list if you need more information!

## 1. FAT Python 

- **Project description**: FAT Python is a new static optimizer for CPython 3.6. It specializes functions using guards. Specialization is a new feature (PEP 510) which allows to implement new kinds of optimizations like loop unrolling and function inlining. The goal of the GSoC is to implement new optimizations in fatoptimizer to prove that the design allows to really make CPython faster. Then maybe also help on the low-level parts like fat (guards implemened in C) and help to finish the work on PEPs 509 (dict version), PEP 510 (specialization) and PEP 511 (API for AST optimizers).

- **Skills**: know how a compiler works, know compiler optimizations especially static optimizations

- **Difficulty level**: Hard

- **Related Readings/Links**: [http://fatoptimizer.readthedocs.org/en/latest/gsoc.html](http://fatoptimizer.readthedocs.org/en/latest/gsoc.html)

- **Potential mentors**: Victor Stinner

## 2. Roundup 

- **Project description**: Work on Roundup, [http://bugs.python.org/](http://bugs.python.org/) to improve github integration, etc.

- **Skills**: python, git

- **Difficulty level**: Intermediate

- **Related Readings/Links**: [https://mail.python.org/mailman/private/core-mentorship/2016-February/003422.html](https://mail.python.org/mailman/private/core-mentorship/2016-February/003422.html)

- **Potential mentors**: Terry, David, Stephen

## 3. A gui (tkinter) front end for pip 

- **Project description**: Many users are not familiar with the command line and thus find difficulties using and accessing PIP. This project would involve creating interactive menus to help guide new users through the process of installing packages using PIP. [https://bugs.python.org/issue23551](https://bugs.python.org/issue23551) contains preliminary design ideas.

Such a visual tool would be extremely useful, and I would make it accessible from IDLE. Once a basic version were written, the additional feature set for the project could be adjusted to fit the time remaining.

- **Skills**: python, usability, pip

- **Difficulty level**: Intermediate

- **Related Readings/Links**: [https://bugs.python.org/issue23551](https://bugs.python.org/issue23551)

- **Potential mentors**: Terry, ??
