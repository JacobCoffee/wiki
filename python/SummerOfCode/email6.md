# SummerOfCode/email6

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# Making the Python Email package fully functional on Python3

Based on discussions on the [Email-SIG](http://wiki.python.org/moin/Email%20SIG) [mailing list](http://mail.python.org/mailman/listinfo/email-sig), I put together a [proposal](http://www.bitdance.com/test/projects/email6/psfproposal/) for re-engineering the standard library email package\'s API and internals so that it can correctly handle Python3\'s careful separation between bytes and strings. The first two months of this proposal were [funded](http://www.python.org/psf/records/board/minutes/2009-12-14/#funding-for-python-3-email-module) by the PSF. Completing the project will require additional contributions, and one form those contributions could take would be an application from a GSoC student to work on the project.

Email processing is a very interesting subject, involving as it does a large body of legacy specifications overlain by more modern specifications that nevertheless must take account of all that went before. It is rife with corner cases and unexpected interactions between elements. This makes writing code that can handle email in the general case a good exercise in both coding skills and the ability to read and interpret RFCs. It particularly involves learning how to parse noisy data, to do parsing error recovery in the face of broken data, and to build useful object models of a very complex, real-world data type.

A GSoC student with an interest in this area can look over the [proposal](http://www.bitdance.com/test/projects/email6/psfproposal/) and pick any of the areas to work on. I have completed the [issue review](http://www.bitdance.com/test/projects/email6/issues/), the coding of a test suite framework, a body of header tests, and good chunk of framework for the Header class, but anything else is up for grabs. The current code base is located in a [launchpad branch](https://launchpad.net/python-email6)
