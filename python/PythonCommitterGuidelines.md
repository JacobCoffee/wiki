# PythonCommitterGuidelines

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# Python Committer Guidelines 

This is currently just a collection of notes based on what was done during the 2.6/3.0 development cycle. Once those get released, it should be cleaned up to be a consolidated resource for Python developers with commit privileges including more on topics like:

- merging back to the currently active maintenance branch(es)
- how to identify security fixes that should also be applied to older maintenance that no longer binary releases (but may still get source-only releases)
- how to handle issues on the patch tracker
- how to handle updates to C code/Python code/documentation/other files
- information on some of the tools used to support development (subversion, svnmerge, roundup, sphinx, reitveld, DVCS mirrors, etc)
- etc.

(note that in many cases, the additional information may be links to existing documents like PEPs, the developer FAQ or some of the README files in Subversion rather than completely new information - the idea is to have a single page to point potential developers to that provides pointers to the different resources)

## General Commit Guidelines 

- run the full test suite before committing (preferably with the -uall option), as some components have additional tests in non-obvious areas of the test suite (often because the test suite is just *using* the component, rather than explicitly testing it)

- if likely to be impacted by cross-platform differences (e.g. uses system calls or may be affected by 32-bit/64-bit differences), keep an eye on the buildbots after committing to check for failures on other platforms

- if in doubt about a change, post a patch to the issue tracker and request feedback on python-dev (either the email list or the IRC channel) before committing the change

- for new developers, don\'t be \"too\" afraid of making mistakes - the ability to easily rollback mistakes is one of the major benefits of having a decent source control system.

- after making a commit, keep an eye on python-checkins and python-3000-checkins for feedback - all the core developers are (or should be) subscribed to those lists, allowing most changes to receive some additional after-the-fact review

- the python-committers mailing list is now used to keep committers advised of the state of the source tree (most importantly, when it is being frozen to allow releases to be made)

- for 2.x only changes, use the svnmerge utility to block forward porting to 3.x (or to actually do the forward port yourself)

- if the commit relates to an issue tracker item, mention the issue number in the commit message, and the commit revision on the issue tracker.

## Additional guidelines during beta period before a release 

- after the last alpha release and before the last beta release, new features may only be added with the permission of the release manager (or GvR, but he will usually defer to the release manager). The RM is identified in the relevant release PEP.
- if the new feature is needed to fix a critical bug, the RM will usually give permission, but may also decide that a better option is to just document the limitation and deal with it in a subsequent release
- if in any doubt at all about a change, consider requesting additional review on python-dev

## Additional guidelines during release candidate period before a release 

- all non-documentation changes should be reviewed by a second committer before being committed (and the reviewer named in the commit message)
- the bar for allowing a new feature to be added to fix a bug or limitation is raised a lot higher
