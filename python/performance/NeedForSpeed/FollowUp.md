# NeedForSpeed/FollowUp

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

These things still need attention:

- The hotbuf branch will be completed after the sprint. I want to implement common parsing patterns (line delimited, netstrings) in C ([MartinBlais](MartinBlais)).

- The patch implementing optimizing out \"if 0\" still needs review.

- Andrew Dalke has experimented with optimizing some common cases in argument parsing, which looks very promising, but needs further attention.

- Internal string-\>object parsing routines (int(), float(), etc) need a way to bound the portion of the string they\'ll look at. This is partly bugfix, since passing a buffer object to such a Python-level routine results in anything from nonsense to segfaults now.

- Tim intends to continue work on the `tim-exc_sanity`{.backtick} branch.

- Fredrik intends to continue work on stringlib refactoring.

- Ran out of time before getting to most of the \"speed function calls\" patches. Since any speedup in that area would benefit almost all users, they\'re still well worth pursuing.

- Look at Kristján\'s ideas for speeding up lookdict_string. I\'ve played with dummy optimization and inline string compare on my machine, which gives a small but noticable speedup. IIRC, the original patch contained a few more tweaks - FL

- Any branches that are not intended to continue work should be removed before leaving the sprint. **DONE** - TP

- Coverity\'s overnight (Saturday/Sunday) run shows a few new `NULL`{.backtick} complaints; need to investigate. **DONE** - TP

- Many tests are showing refcount leaks as of Saturday; Tim suspects the new exception code. **DONE**

## Lessons Learned 

### Visual Studio / Code Coverage Tools 

If anyone uses Windows and is planning to use C code coverage tools to possibly look at improving the test suite, or perhaps for profiling, they might want to obtain them well in advance of a sprint.

I was unable to locate any free tools which worked with Visual Studio, and any commercial ones which even vaguely claimed to do so generally required an indefinite delay after submitting a marketing related form before you could access a downloadable trial version. Perhaps instead of applying for a trial version, it might be worthwhile to apply for a free license for Python development.

Here are the code coverage capable tools which I tried to obtain and use, and short notes about them:

- [Visual Studio Team System](http://msdn.microsoft.com/vstudio/teamsystem/default.aspx)

  - This cannot be downloaded, but a 180 day trial can be obtained on request mailed out on DVD. CCP had a license for it already, but strangely only had beta 2 versions which had expired and was not able to locate a final version in time despite being entitled to one.

- [DevPartner Studio](http://www.compuware.com/products/devpartner/studio.htm)

  - This requires an application for a trial version and an indefinite delay before the marketing department get back to you, by phone I believe! It is possible to locate binaries on file sharing services, which can be installed in a trial mode, but they were unusable in our experience. An older version, 7.00, required VS .NET at the latest, and I was unable to get it to work at a command line level with later versions. The more recent version 8.00, worked with VS 2005, but when a build was made with profiling instrumentation, their compiler crashed repeatedly. Version 8.00 also does not support x64 based versions of Windows.

- [Rational Purify](http://www-306.ibm.com/software/awdtools/purifyplus)

  - This appears to be the one commercial tool which offers a downloadable trial version and does not require indefinite marketing department hoops to be jumped. However, I was completely unable to create an account on IBM\'s web site, due to vague complaints about unsuitable user names and passwords. I suspect that this is a problem which others can get around, because of better guesses at suitable entries for these fields.

Here is another possibility, which I did not know about at the sprint:

- [Bullseye Coverage](http://www.bullseye.com)

  - Does not have a downloadable trial, but I believe one can be obtained after the marketing department receive your submitted application.
