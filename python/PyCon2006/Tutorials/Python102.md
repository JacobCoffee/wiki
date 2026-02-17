# PyCon2006/Tutorials/Python102

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# \"Python 102\" - What to do after you\'ve learned the syntax. 

**NEW - Follow-up session will be held Sunday afternoon. Check the schedule for details.**

**Summary:** This 3-hour tutorial session focuses on some of the more advanced features of Python. Topics include generators and iterators, classes and metaclasses, list comprehensions and advanced data structures. The course will also introduce several common library modules, demonstrating their use. Finally, some time will be spent during the session showing how to take advantage of the existing documentation.

**Target audience:** Beginning programmers who have had a little exposure to the Python language. More experienced programmers familiar with other languages but no real experience with Python.

**Recommended prerequisites:** This session assumes some familiarity - but not necessarily proficiency - with the material presented in \"The Python Tutorial\" ([http://www.python.org/doc/current/tut/tut.html](http://www.python.org/doc/current/tut/tut.html))

**Focus:** These topics will be presented in the context of several real-life examples drawn from my own personal experience. The sample programs being explored are \'real\' in that they can be used to solve real problems and aren\'t just manufactured as examples.

Topics include:[BoardGameSocial](./BoardGameSocial.html)

A. Language Features

1.  Data structures
    a.  Lists, tuples, dictionaries, sets
    b.  Nested data structures
2.  Classes and modules
    a.  Data and methods
3.  Generators and iterators
4.  List comprehensions
5.  Class decorators

A. Libraries

1.  Database access
2.  File-system access
3.  Internet-resource access
    a.  HTTP
    b.  POP3
4.  Output text formatting

**Note:** Each subject is introduced by first identifying the problem to be solved, then using these features to solve that problem. There is some time spent explaining details, but more time is spent using those features in the context of the problem.

**Case study 1:** Converting an mbox file to a relational database. The program reads the mbox file, parses it to identify key fields, creates the database table and populates it from the data in the file. (Also demonstrating how to retrieve this data from a POP3 mailbox.)

**Case study 2:** Comparing a list of file names to the contents of a directory. (Part of a process to identify duplicate files on a hard drive.)

These are just two of the case studies that will be used in this course. Others will be provided, and may be included in the class if time permits.
