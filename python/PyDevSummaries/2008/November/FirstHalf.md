# PyDevSummaries/2008/November/FirstHalf

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

============= Announcements =============

This is the draft of the python-dev mailing list summaries for the first half of November 2008. Please make any corrections, improvements, or comments. The contents will be finalized at the end of the month, when the summaries\' draft for the second half of November 2008 are posted. I hope to keep this schedule regularly.

========= Summaries =========

------------------------------------------------------------------------

Looking for VCS usage scenarios

------------------------------------------------------------------------

Brett Cannon solicits any use cases and scenarios that would give an understanding for the motivations in proposing Python move to or mirror officially via some distributed version control. Much discussion ensued that I didn\'t have the time to follow. This thread was over 100 posts, so anyone who followed it well, please give as concise an overview as you can.

Contributing thread:

\- `Looking for VCS usage scenarios <http://mail.python.org/pipermail/python-dev/2008-November/083272.html>`{.backtick}[ ]

Note that the intent is to be conservative. The writeup of a candidate DVCS should show how to do the tasks done today; new and improved workflows can be mentioned in the bonus section, but will have less weight. The competition is probably limited to bzr and Hg, with an outside chance for git.

------------------------------------------------------------------------

Optionally using GMP to implement long if available

------------------------------------------------------------------------

The suggestion of using the GMP library to implement Python\'s long numbers was brought in the context of an compile time option, falling back to the current in-house implementation when GMP is not available. However, the discussion points out that most distribution of Python is binary and so the LGPL issues that keep us from using GMP still apply.

Some benchmarks showed that GMP was actually slightly slower for the relatively small numbers used in most programs.

Some of the conversation also suggestion various improvements to our own implementation, mostly focused on increasing size of the base long values are stored in, particularly on 64bit systems.

Contributing thread:

\- `Optionally using GMP to implement long if available <http://mail.python.org/pipermail/python-dev/2008-November/083315.html>`{.backtick}

------------------------------------------------------------------------

Optimize Python long integers

------------------------------------------------------------------------

Several outstanding patches to optimize int and especially long objects were benchmarked and applied to the 2.6 branch for comparison. Although they are not eligable for the bugfix releases of 2.6 or 3.0, they may be likely improvements we\'ll see in 2.7 and 3.1 releases in the future. However, some related and minor bug fixes to long are likely to be applied much sooner.

Contributing thread:

\- `Optimize Python long integers <http://mail.python.org/pipermail/python-dev/2008-November/083514.html>`{.backtick}[ ]

------------------------------------------------------------------------

Fwd: Removal of GIL through refcounting removal.

------------------------------------------------------------------------

Yet Another Attempt At Removing The GIL was proposed, and had a more positive reception than most of the times it has been brought up (in my memory). While the removal of the GIL has been both proposed and successfully attempted in the past, there have always been outstanding issues that keep the lock around. One of the primary issues is that of the C API and extension modules, which all expect reference counting. A technique used in [IronClad](./IronClad.html), a project that provides use of CPython extensions in the [IronPython](IronPython) implementation of the language, was suggested to provide reference counting semantics to legacy extensions, even if the internal objects no longer require them.

Contributing thread:

\- `Fwd: Removal of GIL through refcounting removal. <http://mail.python.org/pipermail/python-dev/2008-November/083256.html>`{.backtick}

------------------------------------------------------------------------

Using Cython for standard library?

------------------------------------------------------------------------

Without much expectation that any action will actually be taken any time soon, the possibility of using Cython (and, by extension, similar solutions) was given consideration. While the benefits of these solutions are obvious, there is no particular best of breed nor yet a point of stability that a mature project might stand on. It would be exciting to one day see some variation of this happen, but that day is not today.

Contributing thread:

\- `Using Cython for standard library? <http://mail.python.org/pipermail/python-dev/2008-November/083284.html>`{.backtick}[ ]

------------------------------------------------------------------------

n.numbits: method or property?

------------------------------------------------------------------------

The basic question of a proposed method or property, numbits, drew into a small discussion about the inherent assumption of binary representation of our numbers. The numbits method or property would provide the smallest number of bits required to represent a given integer.

Contributing thread:

\- `n.numbits: method or property? <http://mail.python.org/pipermail/python-dev/2008-November/083528.html>`{.backtick}

------------------------------------------------------------------------

XXX do we need a new policy?

------------------------------------------------------------------------

Some concerns were raised for the number of XXX, TODO, and other types of comment markers in the Python source. While the OP appears to worry about the number of open issues this represents, the general concensus seems to conclude that any real issues have associated tickets, there is little benefit in dealing with all of these at once, and the 2000 or so of them represents nothing significant, in the first place.

Contributing thread:

\- `XXX do we need a new policy? <http://mail.python.org/pipermail/python-dev/2008-November/083342.html>`{.backtick}[ ]

------------------------------------------------------------------------

DVCS PEP update

------------------------------------------------------------------------

It was announced that git is being included as one of the distributed version control solutions in consideration for any proposal to move from Subversion. Some back and forth on the various questions against each option and who is representing each was also given.

Contributing thread:

\- `DVCS PEP update <http://mail.python.org/pipermail/python-dev/2008-November/083412.html>`{.backtick}

------------------------------------------------------------------------

Released fixes for CVE-2008-2315 for Python 2.4?

------------------------------------------------------------------------

It was confirmed that an additional bugfix release of 2.4 will be made, 2.4.6 in a simultaneous release with 2.5.3. However, this accepts only security fixes so the multiprocessing module backport is not eligable.

Contributing thread:

\- `Released fixes for CVE-2008-2315 for Python 2.4? <http://mail.python.org/pipermail/python-dev/2008-November/083484.html>`{.backtick}[ ]

------------------------------------------------------------------------

file open in python interpreter

------------------------------------------------------------------------

Adrian Golding inquired on where in the source code the python modules are actually opened for reading, and was pointed to import.c and a case in main.c. It was pointed out that runpy.py can indirectly open them when executing from a directory or zipfile, which does not actually match Adrian\'s specific use case.

Contributing thread:

\- `file open in python interpreter <http://mail.python.org/pipermail/python-dev/2008-November/083279.html>`{.backtick}

------------------------------------------------------------------------

How do I get my patches accepted?

------------------------------------------------------------------------

Victor Stinner sparked a myriad of concerns and suggestions about any possibly slowing response between patch submission and acceptance. While the core dev team cannot easily grow without compromising quality, it is suggested that a lot of work could be done to triage patches and mine the open tickets in a way that would make the job of the core developers a lot easier. Further, this spawned the heavy discussions of distributed version control we\'ve seen lately. The hope is that taking it out of the hands of volunteers to allow others to make new branches and demonstrate their patches.

Contributing thread:

\- `My patches <http://mail.python.org/pipermail/python-dev/2008-November/083255.html>`{.backtick}[ ]

------------------------------------------------------------------------

compiler optimizations: collecting ideas

------------------------------------------------------------------------

Daniel Furrer, as one of a group of students, solicits for optimization possibilities they might tackle. With a few suggestions, the focus came to optimizing Cython and chains of if/elif/else blocks, although a previous PEP on the later matter had been rejected.

Contributing thread:

\- `compiler optimizations: collecting ideas <http://mail.python.org/pipermail/python-dev/2008-November/083557.html>`{.backtick}

------------------------------------------------------------------------

Python 2.5.3: call for patches

------------------------------------------------------------------------

Preparing for the impending release of 2.5.3, the last bug-fixing version of 2.5, any last patches or issues to include were called for. The issues from the tracker 3677, 3367, 2588, 2589, 1040026, 2231, 2246, and 2321 were suggested, some of which were confirmed to be already included. Several issues from CVE were also given, most of which need to back-port fixes into the 2.5 branch. (CVE-2007-4965, CVE-2008-1679, CVE-2008-1721, CVE-2008-2315, CVE-2008-3144, CVE-2008-1887, CVE-2008-4864)

Contributing thread:

\- `Python 2.5.3: call for patches <http://mail.python.org/pipermail/python-dev/2008-November/083517.html>`{.backtick}[ ]

------------------------------------------------------------------------

datetime and timedelta enhancement

------------------------------------------------------------------------

Several enhancements to the datetime and timedelta objects are proposed, including converting timedelta to specific units, finding the ratio of two deltas, and easily obtaining a timestamp from a datetime object. However, patches exist for the datetime to timestamp conversion that seem to be rejected at [http://bugs.python.org/issue1665292](http://bugs.python.org/issue1665292)

Contributing thread:

\- `datetime and timedelta enhancement <http://mail.python.org/pipermail/python-dev/2008-November/083564.html>`{.backtick}

=============== Skipped Threads ===============

\- `Why don't range and xrange threat floats as floats? <http://mail.python.org/pipermail/python-dev/2008-November/083429.html>`{.backtick}[ - `[Python-3000] RELEASED Python 3.0rc2 <http://mail.python.org/pipermail/python-dev/2008-November/083483.html>`{.backtick}] - `Python 3.0rc2: problem with exec()ing files <http://mail.python.org/pipermail/python-dev/2008-November/083513.html>`{.backtick}[ - `Feedback from numerical/math community on PEP 225 <http://mail.python.org/pipermail/python-dev/2008-November/083493.html>`{.backtick}] - `buffer function <http://mail.python.org/pipermail/python-dev/2008-November/083262.html>`{.backtick}[ - `How to select text of text field in python&#8207;Card <http://mail.python.org/pipermail/python-dev/2008-November/083277.html>`{.backtick}] - `RELEASED Python 3.0rc2 <http://mail.python.org/pipermail/python-dev/2008-November/083481.html>`{.backtick}[ - `Summary of Python tracker Issues <http://mail.python.org/pipermail/python-dev/2008-November/083485.html>`{.backtick}] - `Getting Set Up dev doc <http://mail.python.org/pipermail/python-dev/2008-November/083504.html>`{.backtick}[ - `A statistic for Python tickets <http://mail.python.org/pipermail/python-dev/2008-November/083534.html>`{.backtick}] - `How does one build Python25.chm on Windows? <http://mail.python.org/pipermail/python-dev/2008-November/083549.html>`{.backtick}[ - `Upgrade SVN server to 1.5.4 <http://mail.python.org/pipermail/python-dev/2008-November/083551.html>`{.backtick}] - `[ANN] VPython 0.1 <http://mail.python.org/pipermail/python-dev/2008-November/083257.html>`{.backtick}[ - `Packaging the PyPI version of the SSL module for Debian <http://mail.python.org/pipermail/python-dev/2008-November/083291.html>`{.backtick}] - `New "stage" field in the tracker <http://mail.python.org/pipermail/python-dev/2008-November/083331.html>`{.backtick}[ - `Python2.5 _sre deepcopy regression? <http://mail.python.org/pipermail/python-dev/2008-November/083348.html>`{.backtick}] - `test - please ignore <http://mail.python.org/pipermail/python-dev/2008-November/083418.html>`{.backtick}[ - `AST-level type inference optimizations <http://mail.python.org/pipermail/python-dev/2008-November/083438.html>`{.backtick}] - `test message - spam work... <http://mail.python.org/pipermail/python-dev/2008-November/083556.html>`{.backtick}[ - `Getting Set Up doc now online <http://mail.python.org/pipermail/python-dev/2008-November/083568.html>`{.backtick}] - `hg branch gone? <http://mail.python.org/pipermail/python-dev/2008-November/083292.html>`{.backtick}[ ]
