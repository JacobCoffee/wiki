# SummerOfCode/2011/pkumar/PackagingPy2Porting

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

- **\' [PackagingPy2Porting](PackagingPy2Porting)** \'

**\[Introduction\]**

This is a project\[1\] for the porting of \'Packaging\' over to lesser versions of python i.e. python 2.4 to python 3.2. In nutshell, the project will result in a successful release of a standalone backport of \"Packaging\" for python2.4 to python3.2 along with a detailed tutorial on the porting of \'Packaging\'. This project is more about developing a tool or mechanism to port \'packaging\' over to other specified versions of python. Thanks to Éric Araujo for his suggestions on improving various aspects of the proposal. The idea here is that we should not be working on porting of \'packaging\' again and again after each modification in \'packaging\' or a new python release. Just slight modifications in the fixers or the scripts should be enough to handle the errors due to newly made changes.

**\[Benefits to the Python community\]**

1\. Porting of \'Packaging\' will make it available to all the other versions of python i.e. python2.4 to python3.2.

2\. An automated system will be created which will port \'packaging\' over to other specified versions of python even after changes in \'packaging\' codes with ease and little modifications.

3\. It is known that python3.3 is going to be released and similar other python3.x releases have yet to be done. Since \'Packaging\' is compatible with python3.x, it would certainly be less painful to port \'Packaging\' for the lesser versions of python i.e. python3.2 to python2.4, rather than porting distutils2 to python3.x with each new release of python3.x.

4\. The tutorial provided will help in the further development of the project.

**\[Project Details\]**

1\. Make \'Packaging\' compatible with python3.2 to python2.4 which includes following steps.

\* Applying 3to2 to \'Packaging\' for all the versions of python2.

\* Fixing \'type\' issues corresponding to bytes and string using custom fixers.

\* Develop magic comment system for version specific features for all the specified versions of python.

2\. Ensure that build and installation process goes well for all the versions of python i.e. 2.4 - 3.2 which includes porting files like setup.py, setup.cfg, Makefile, etc to make it compatible with other versions of python.

3\. Write a tutorial on the porting work of \'Packaging\' to support further development of the project.

**\[Milestones\]**

Initial preparations includes the following:

- Installation of all the versions of python i.e. python 2.4 to python 3.2.
- Creating a repo for the project.
- Creating a wiki page for the documentation of the porting work.
- Going through the work already done on \'Packaging\'.
- Going through the projects using 3to2 and their methods of solving bytes and string issues using 3to2.

*Start of Program (May 24)*

Before Midterm Evaluation \[May 24 - July 12\]

1\. \[May 24 - May 29\] Porting \'Packaging\' to all the versions of python 3.x at first which includes:

- Develop magic comment system for python 3.1 considering that python 3.1 don\'t have all the features that \'packaging\' uses in python 3.3.
- Writing custom fixers if required.

2\. \[May 30 - June 6\] Testing and finalizing the porting work on python 3.x.

3\. \[June 7 - June 14\] Writing custom fixers for bytes and string issues.

4 \[June 15 - June 21\] Ensure the proper implementation of the newly created fixer on all the 2.x versions of python and fix the potential issues, if any.

5\. \[June 22 - June 28\] Developing magic comment system for python 2.7

6\. \[June 29 - July 6\] Testing and finalizing the porting for python 2.7 which includes:

- Running tests on all the modules of python 2.7.
- Writing custom fixers for python 2.7, if required.
- Fixing version specific issues, if any.

7\. \[July 7 - July 11\] Developing magic comment system for python 2.6

*Midterm Evaluation (July 12)*

**\[Deliverables\]**

1.  sdists of \'Packaging\' for all the versions of python3.
2.  Custom fixers for bytes and string issues for all the versions of python.
3.  sdist of packaging for python 2.7.
4.  Documentation on the porting work till date.

Before Final Evaluation \[July 13 - August 15\]

8\. \[July 13 - July 22\] Testing and finalizing the porting for python 2.6

9\. \[July 23 - July 30\] Developing magic comment system for python2.5 and python 2.4.

10\. \[July 31 - August 7\] Testing and finalizing the porting for python 2.5 and python 2.4.

11\. \[August 8 - August 15\] Work for the final week of the project includes:

- Ensuring the installation and working of \'Packaging\' in all the given versions of python i.e. python2.4 to python3.2.
- Testing and fixing any left over issues.
- Wrap up.

*Final Evaluation (Aug 16)*

**\[Deliverables\]**

1.  sdists of \'Packaging\' for each supported version.
2.  A script running 3to2 with custom fixers for each supported Python version.
3.  A detailed documentation on the porting of \'Packaging\'.

\[1\] [https://bitbucket.org/pkumar/packaging_cpython](https://bitbucket.org/pkumar/packaging_cpython)
