# SummerOfCode/2009/Incoming

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

Drop new project ideas here, make sure to include a list of skills that\'d be needed (C, Java, OpenGL, WSGI, etc) and a link to a mentor\'s contact info who can field questions about the project. Sign with your own email address (if different) in case you need to be contacted.

In most cases we\'ll add it to the list within an hour. We\'ve made this page to avoid edit conflicts and because some people have had trouble editing the large table on the main ideas page.

### Overhaul struct + PEP 3118 

There are many open issues for the struct module, and [a suggestion](http://bugs.python.org/msg81911) that many others fixes should happen. The problems include inconsistencies in input handling and backwards-compatibility code that should be gone from 3.x.

As [PEP 3118](http://www.python.org/dev/peps/pep-3118/) also requires [a few changes in struct](http://bugs.python.org/issue3132), finishing the [memoryview object implementation](http://bugs.python.org/issue2394) and [backporting it to 2.7](http://bugs.python.org/issue2396) could be part of this project.

To tackle this, a student should know C and have some familiarity with the CPython codebase. The proposal should include an overview of open issues and, if possible, of problems in current code.

Mentors for this task should have a good understanding of the struct module, the buffer interface and PEP 3118.

**Mentor Needed**

### Clean up and improve the socket module 

The socket module is the foundation of many important parts of the stdlib. It has many open issues and RFEs, with many more being indirectly dependent on it. Major pain areas are cross-platform problems, shortcomings for a few use cases and some missing bits from the API (e.g. recvall(), sendmsg() and recvmsg()). If these can be solved quickly, going through the uses of the socket module in the stdlib to would make this project even more useful.

This project has some ugly cross-platform needs, but these can be handled by the student and the mentor together (maybe [snakebite](http://www.snakebite.org/) could help?). For students wanting to work on this, knowing C is a must, being familiar with CPython and the stdlib would be desirable. Having some prior knowledge of POSIX and Windows interfaces the socket module uses would be a nice perk.

Mentors should be able to help the student to test their code on many different platforms. Knowing the socket API in different platforms would be desirable.

**Mentor Needed**

### Helper Python core development tools 

This proposal is about improving the workflow of core developers, probably with small glue scripts. As each developer has his own personal workflow, these helper scripts should be optional, easy to extend and aimed at the most common tasks.

Identifying which tasks and steps should be optimized cannot be left to the student nor to the mentor, it must be a collective effort. Clear goals must be set before someone try to implement them.

Besides some experience with Python and tools of the trade (VCSs, bug trackers, etc.), the most important requisite for a student working on this is being able to listen to the community and taking criticism well.

At least one core Python developer should mentor, preferably one that knows how to interact well with python-dev. Ali Afshar from PIDA is willing to mentor. Daniel Diniz is available to help with the Python workflow part that touches Roundup and Rietveld.

### Linux package repositories on PyPI 

The project should organize the Linux binary packages on PyPI ([http://pypi.python.org](http://pypi.python.org)) in such a way that they can serve as a Linux package repository, for relevant Linux distributions. It should in particular provide Debian/apt repositories and RPM/yum repositories. Compatibility of packages with certain distributions should be considered.

Contact: Martin v. Löwis \<[martin@v.loewis.de](mailto:martin@v.loewis.de)\>

### Roundup / Python Tracker enhancements 

This proposal has two main goals: making the Python bug tracker more efficient for core developers and improving Roundup in areas that don\'t directly concern the PSF trackers. Most of the code would land in Roundup\'s repositories, but many instance-level changes would be focus the Python tracker.

There are many open developement ideas that could be part of a GSoC proposal. Examples include cleaning up and improving the base infrastructure, performance improvements (DB, web interface), improving end-user UI and features, adding developer-focused features to Roundup and administration enhancements. See [this thread](http://mail.python.org/pipermail/python-dev/2009-March/087560.html) for some examples.

The student should be comfortable with Python and have a grasp of general bug/issue handling procedures. Familiarity with Roundup is a huge plus, but the code is newbie-friendly. The deliverables should include patches for upstream Roundup and for the Python instance.

Stefan Seefeld and Martin von Löwis are willing to mentor this proposal. Daniel Diniz will be available to help mentors and the student in many tasks.

------------------------------------------------------------------------

[CategoryTracker](CategoryTracker)
