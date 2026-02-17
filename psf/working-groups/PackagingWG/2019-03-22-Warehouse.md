# PackagingWG/2019-03-22-Warehouse

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# Prioritizing some extant (mostly security) issues 

22 March 2019

Participants:

- Dustin Ingram
- Donald Stufft
- Ernest W. Durbin III
- William Woodruff
- Sumana Harihareswara

Warehouse issues to discuss:

- [https://github.com/pypa/warehouse/issues/4440](https://github.com/pypa/warehouse/issues/4440) Implement soft deletes for projects, releases and files

  - Still open questions about how to implement this? Priority?
    - Dustin has an open branch

    - wants feature sooner rather than later\...

    - needs help making query efficient

    - Donald + Ernest thinks it\'s a nice to have, not a prereq for any planned upcoming work

    - TODO: Dustin to link to branch in issue \-- **DONE**

- [https://github.com/pypa/warehouse/issues/5247](https://github.com/pypa/warehouse/issues/5247) Roadmap update for TUF support

  - Facebook money? Pradyun work?
    - Ernest: part of Facebook research grant intends for some form of \[signing\]\.... decisions \[on implementation\] will be part of Q3/4 RFI/RFP\..... mid-April, get RFI out \.... July kickoff for project \.... decide whether TUF is what we go with \..... this is on the radar \.... funding exists \....

    - Will: is a little familiar with TUF, knows some NYU Tandon people working on it, no strong opinions on whether it\'s the right tool here

    - TODO: Sumana to update issue and link to blog post [http://pyfound.blogspot.com/2018/12/upcoming-pypi-improvements-for-2019.html](http://pyfound.blogspot.com/2018/12/upcoming-pypi-improvements-for-2019.html) \-- **DONE**

- [https://github.com/pypa/warehouse/issues/4470](https://github.com/pypa/warehouse/issues/4470) Add javascript/frontend validation of breached passwords

  - Facebook money? Priority?
    - don\'t add to OTF scope \.... unless we have a lot of empty hands at end of this funding/project

    - Dustin: we already do some breached password checking \.... not as important to also do on frontend \... would be nice if a volunteer comes along with JS experience

    - Will: agrees

    - TODO: Sumana to seek volunteers (lowkey) \-- **DONE**

- [https://github.com/pypa/warehouse/issues/798](https://github.com/pypa/warehouse/issues/798) Security Notification Systems for Python Packages

  - Facebook money? Priority?
    - Dustin: this is? also a pip issue tracker bug \.... how do we tell the user that they may be trying to install something taken down as malware??? this issue \....

    - related to the #345 and #3709 issues

    - related: [https://github.com/pypa/warehouse/issues/3896](https://github.com/pypa/warehouse/issues/3896), [https://github.com/pypa/warehouse/issues/2982](https://github.com/pypa/warehouse/issues/2982), etc\...

    - design concerns\....

    - see next point

- [https://github.com/pypa/warehouse/issues/345](https://github.com/pypa/warehouse/issues/345) Ability to mark a version of a package as deprecated or unsupported AND [https://github.com/pypa/warehouse/issues/3709](https://github.com/pypa/warehouse/issues/3709) Offer a discouraged/deprecated releases option?

  - WIP PR: [https://github.com/pypa/warehouse/pull/1462](https://github.com/pypa/warehouse/pull/1462)

  - Ernest: we need a system for generic flags and statuses on projects \... marking for moderation and abuse \....

  - chewy big system design \..... big enough to get financial help or see if partners will help by implementing it \-- Continuum maybe?

  - TODO: Sumana to list as part of \"if we had money, we could have that thing\" list seeking grants and donations \-- **DONE** at [Fundable Packaging Improvements](../../packaging/Fundable Packaging Improvements)

- [https://github.com/pypa/warehouse/issues/3417](https://github.com/pypa/warehouse/issues/3417) Add ability to configure a redirect for documentation previously hosted by PyPI

  - Read the Docs & Ernest \-- what is the next step here?

  - Implemented in conveyor: [https://github.com/pypa/conveyor/pull/3](https://github.com/pypa/conveyor/pull/3)

  - just needs UI in Warehouse to place the magic redirect file \-- was ready last year

  - TODO: Ernest to update the issue. \-- **DONE**

  - TODO: Sumana to massage issue to seek volunteers \-- **DONE**

- [https://github.com/pypa/warehouse/issues/5584](https://github.com/pypa/warehouse/issues/5584) Warehouse doesn\'t check whether uploaded packages ending in tar.gz are actually tarballs

  - Is this a problem? Priority?
    - Dustin: this is easy, we should just do it. Why aren\'t we doing it right now? Just an oversight.

    - Donald: legacy PyPI didn\'t do it; ported old behavior. Tarballs implemented 15 yrs ago, gzip 10 yrs ago ![:-)](/wiki/europython/img/smile.png ":-)")

    - Will: if easy to verify \.... in audits, people will accidentally bomb their sys in recursive validation process. Sandbox the process!

    - verifying a tarball\'s soundness can make it easy to introduce DoSes due to tarbombs

    - TODO: Will to update issue \-- **DONE**

    - TODO: Sumana to ask for volunteers \-- **DONE**

Other:

- Will seeking review on [https://github.com/pypa/warehouse/pull/5567](https://github.com/pypa/warehouse/pull/5567) WIP PR

- Dustin: about to push new discussion re manylinux spec
