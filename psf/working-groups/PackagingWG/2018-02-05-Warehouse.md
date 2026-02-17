# PackagingWG/2018-02-05-Warehouse

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

Warehouse weekly meeting notes

Monday, Feb. 5, 2018

## Present: 

- Sumana
- Laura
- Mark
- Dustin
- Ernest
- Nicole

## Current work/announcements: 

- Sumana:
  - started [https://wiki.python.org/psf/WarehousePackageMaintainerTesting](https://wiki.python.org/psf/WarehousePackageMaintainerTesting) draft

  - Package maintainer workflow \-- finding pain points
- Nicole:
  - made maintainer UI work on mobile

  - \#[2879](https://github.com/pypa/warehouse/pull/2879) - to-do list on maintainer views - should be merged by end of week

  - user testing: starting soon

  - **blocked** on [terms & conditions for](https://github.com/pypa/warehouse/issues/1989)[CoC/privacy in footer](https://github.com/pypa/warehouse/issues/1989) - Mark and Ewa working on this, we\'ll have more on Thursday
- Dustin:
  - Account management - Adding/changing/deleting primary emails, email confirmation

  - Release detail & deleting individual releases and files

  - not blocked on anything

  - see TODOs: Are journals per-project or per release?
- Ernest:
  - Unexpected but not distressed family travel beginning of this week, as well as planned and less disruptive PyTN travel at end of week
  - No blockers, eager to get into warehouse codebase more full time. - performance, monitoring, features
- Laura:
  - w/Sumana, pkg maintainer workflow testing/work

  - [Twine documentation PRs](https://github.com/pypa/twine/pulls?utf8=%E2%9C%93&q=is%3Apr+author%3Algh2+)

  - this afternoon: Ernest meeting, tester promotion/publicity meeting - discuss drafting of promotional materials
- Mark:
  - Payments to go out this week.

  - [which privacy policy & code of conduct should PyPI mention?](https://github.com/pypa/warehouse/issues/1989) - Van should be reviewing on Thursday.

  - Some funds may be available for emergency overages at the end of the project

## Bug/PR triage: 

- Pull request: RSS feed for INDIVIDUAL package updates [https://github.com/pypa/warehouse/pull/2165](https://github.com/pypa/warehouse/pull/2165)

  - A related feature already exists at [https://pypi.python.org/pypi?%3Aaction=rss](https://pypi.python.org/pypi?%3Aaction=rss) and and [https://pypi.python.org/pypi?%3Aaction=packages_rss](https://pypi.python.org/pypi?%3Aaction=packages_rss) for recent updates & newest packages on the legacy site, but this is not a feature parity issue because this is a request for individual package RSS feeds. It\'s been requested by [PyUp](./PyUp.html), which needs to know when versions are deleted.

  - Action: Sumana to mark as COOL but not urgent (Sumana\'s done so)

- Find additional JS developer(s) [https://github.com/pypa/warehouse/issues/1297](https://github.com/pypa/warehouse/issues/1297)

  - Nicole\'s work frontloaded into current milestone probably, doing \~10h/week right now; we\'re probably fine in terms of using her time and not running out of it before the end of the project
  - get a helper \.... for design work? probably not (communication overhead costs). Nicole will consider whether someone helping with, e.g., CSS would be helpful
  - Action: Nicole to let Sumana know if she finds she wants help on some dimension

- \"Latest\" version for project detail should take into account PEP 440 pre-releases [https://github.com/pypa/warehouse/issues/382](https://github.com/pypa/warehouse/issues/382)

  - polish issue \-- for after launch (Sumana\'s updated it)

- possible spamming of package namespace [https://github.com/pypa/warehouse/issues/2859](https://github.com/pypa/warehouse/issues/2859)

  - malicious/squatting packages were addressed

  - crypto names were left in place, for now.

  - people mass-register package names, namesquat stdlib packages, may be duplicate of another PEP 541 issue

  - blacklist AWS-S3

  - Action: Dustin & Ernest to review

- Inconsistent handling of packages with equivalent version numbers (e.g. v4.1 & v4.1.0) [https://github.com/pypa/warehouse/issues/2788](https://github.com/pypa/warehouse/issues/2788)

  - ability to compare versions is not ideal - ordering that shows up on project page is incorrect

  - End user MVP?

  - Action: Dustin & Sumana to review

## Things to ask Donald to do: 

- [https://github.com/python/peps/pull/566](https://github.com/python/peps/pull/566)

  - Nick Coghlan is suggesting changing BDFL delegate status - Donald needs to ok and accept PR (or something else?)

## Maintainer MVP milestone work remaining: 

[https://github.com/pypa/warehouse/milestone/8](https://github.com/pypa/warehouse/milestone/8) \* Still on schedule for maintainer MVP milestone at end of Feb

## To do: 

- Determine if Journals should be per-project or per-release
  - Per Release would be feature parity, right? I don\'t think we expose project level views right now?[#2871](https://github.com/pypa/warehouse/issues/2871)

- Dustin & Ernest to review possible spamming of package namespace [https://github.com/pypa/warehouse/issues/2859](https://github.com/pypa/warehouse/issues/2859)

- Dustin & Sumana to review Inconsistent handling of packages with equivalent version numbers (e.g. v4.1 & v4.1.0) [https://github.com/pypa/warehouse/issues/2788](https://github.com/pypa/warehouse/issues/2788)
