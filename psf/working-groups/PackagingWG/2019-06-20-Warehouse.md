# PackagingWG/2019-06-20-Warehouse

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# Scoping Facebook-funded work 

Thursday, June 20th

- Ernest
- Donald
- Sumana

## Deliverables 

[Work milestone on GitHub](https://github.com/pypa/warehouse/milestone/16)

Activities/deliverables:

- Cryptographic signing and verification of artifacts (PEP 458/TUF or similar) \-- [https://github.com/pypa/warehouse/issues/5247](https://github.com/pypa/warehouse/issues/5247)

- Automated detection of malicious uploads

- Further work on API tokens + multi-factor authentication, should the need arise

- UI design around new features mentioned above

- User adoption planning/design

- Documentation

Re: autodetection of malicious uploads: we\'re being funded to build infrastructure that will also help with spam, metadata, installability, and so on. Even though some related features are not directly in scope (because, for instance, the problem of spam is distinct from the problem of malware), some of the necessary dependencies in tooling for the deliverables will also help towards these other goals.

So we\'ll work to specify our requirements so infrastructure/architecture we build on this project is pluggable.

## Deciding what\'s in scope 

In scope?

- [https://github.com/pypa/warehouse/issues/2982](https://github.com/pypa/warehouse/issues/2982) Ongoing antispam strategies:

  - Automated Spam classification for all incoming Projects and Releases
    - \[need to file standalone bug?\] same as [https://github.com/pypa/warehouse/issues/194](https://github.com/pypa/warehouse/issues/194) Automatically check uploaded packages (metadata, installability) ?
  - Admin interface for review and training of Spam classification results
    - TODO: Sumana to file bug for admin interface for review of flagged packages generally. Done: [https://github.com/pypa/warehouse/issues/6062](https://github.com/pypa/warehouse/issues/6062) **in scope**

    - [https://github.com/pypa/warehouse/issues/4011](https://github.com/pypa/warehouse/issues/4011) create \"Moderator\" level User and corresponding permissions
  - Community crowdsourced classification of spam
    - [https://github.com/pypa/warehouse/issues/3896](https://github.com/pypa/warehouse/issues/3896) Report projects that damage other packages, don\'t adhere to guidelines, or are malicious **related to project scope**

      - (User feature) - whoever is designing detection system should have in mind that we might also want to add manual flagging as an input to pipeline/admin UI

      - Depends on [https://github.com/pypa/warehouse/issues/3231](https://github.com/pypa/warehouse/issues/3231) user support ticket system
  - Admin interface for review of User Spam reports
    - [https://github.com/pypa/warehouse/issues/3218](https://github.com/pypa/warehouse/issues/3218) implement an [AdminFlag](./AdminFlag.html) for halting project/release modifications - maybe a good first issue for a new contributor **in scope**

    - [https://github.com/pypa/warehouse/issues/2976](https://github.com/pypa/warehouse/issues/2976) admin feature: bulk delete from supplied package name list

<!-- -->

- [https://github.com/pypa/warehouse/issues/3231](https://github.com/pypa/warehouse/issues/3231) User support ticket system

  - Dustin\'s branch \-- \"what to do with orphaned packages\" #1506 (PEP 541) depends on this, and per #3369 people are now a little confused about where to file package claim issues
    - Ernest has sought a platform we could use - no luck

- [https://github.com/pypa/warehouse/issues/5718](https://github.com/pypa/warehouse/issues/5718) Update roadmap with a clearly articulated security model & strategy

- Better yanking/deprecation/archiving tooling:
  - person implementing crypto signing will have to be aware of these things \-- a possible attack is modifying the responses from PyPI such that all secure releases of a project are yanked, either for everyone or targeted to a particular user (downloading). (TUF addresses this; any other solution also needs to be aware of this issue, address/mitigate)

  - detecting malicious files: should ignore archived/yanked status probably??

  - [https://github.com/pypa/warehouse/issues/5837](https://github.com/pypa/warehouse/issues/5837) implement PEP 592 \-- Yanking of Releases/Files

  - [https://github.com/pypa/warehouse/issues/345](https://github.com/pypa/warehouse/issues/345) ability to mark a version of a package as deprecated or unsupported

  - [https://github.com/pypa/warehouse/issues/4440](https://github.com/pypa/warehouse/issues/4440) implement soft deletes for projects, releases and files - probably a good requirement to add **in scope**

    - could be useful for malicious file detection - mitigate erroneous deletions by admins
    - but right now the actual thing we do is delete the DB record, but file is still avail and could be recovered, but not as trivial as undelete button

  - [https://github.com/pypa/warehouse/issues/3709](https://github.com/pypa/warehouse/issues/3709) Offer a discouraged/deprecated releases option?

  - [https://github.com/pypa/warehouse/issues/4021](https://github.com/pypa/warehouse/issues/4021) add option to archive project

  - [https://github.com/pypa/warehouse/issues/1971](https://github.com/pypa/warehouse/issues/1971) add ability to exclude packages from search

- sensitive package names (typosquatting):
  - TODO: Sumana: START NEW ISSUE for discussing pre-upload checking of typosquatting - reopened [https://github.com/pypa/warehouse/issues/4998](https://github.com/pypa/warehouse/issues/4998)

    - hard to do without LOTS of false positives
    - Netflix: remove the dashes, register resulting strings
    - we could increase scope of current normalization rules to cover more scenarios \-- there will be existing collisions, including with whitehat preemptive registration project

  - [https://github.com/pypa/warehouse/issues/2268](https://github.com/pypa/warehouse/issues/2268) Idea: post-registration alerts for packages with similar names

  - [https://github.com/pypa/warehouse/issues/2082](https://github.com/pypa/warehouse/issues/2082) Add the ability to reserve a name

    - not very related to this\... admins can already blacklist names to stop them from being registered, then unreserve when we want
      - can do this through web interface
    - this issue is more about giving this feature to end users - they can hack this right now by uploading an empty package

  - [https://github.com/pypa/warehouse/issues/4967](https://github.com/pypa/warehouse/issues/4967) prefix ID reservations? (typeshed and third-party packages)

    - see next item

  - [https://github.com/pypa/warehouse/issues/4164](https://github.com/pypa/warehouse/issues/4164) Handle security implications of PEP 561 type hinting packages

    - above 2 items: depends on what convention emerges (from PEP). May do what npm does re special typed namespaces.
      - **maybe in scope**

  - [https://github.com/pypa/warehouse/issues/2401](https://github.com/pypa/warehouse/issues/2401) Indicate in UI/API if a name has been prohibited

    - **maybe in scope** - depends on where we expose it. After all, we may not be able to produce a single canonical list

- [https://github.com/pypa/warehouse/issues/2151#issuecomment-330178574](https://github.com/pypa/warehouse/issues/2151#issuecomment-330178574) \-- unchecked checkboxes from \"lock package names that conflict with core libraries\"

  - Audit currently registered packages which conflict.
  - Determine what stdlib modules exist in other Python Interpreters, PR to stdlib_list
    - TODO: Ernest to check on these

- bad/suspicious/malware packages:
  - [https://github.com/pypa/warehouse/issues/4703](https://github.com/pypa/warehouse/issues/4703) publish a list of malicious packages that have been taken down

    - **maybe in scope** \-- if we choose to do it, this is in scope

  - [https://github.com/pypa/warehouse/issues/5117](https://github.com/pypa/warehouse/issues/5117) remove bad or suspicious packages \-- **in scope**

    - general - maybe we can make this our issue for \"removing pkgs we don\'t want\", decide what IS a bad pkg

  - [https://github.com/pypa/warehouse/issues/5213](https://github.com/pypa/warehouse/issues/5213) example? \"socketio\"

    - hard to do this one retroactively

- packages with zero releases
  - ticketing/workflow for PEP 541 \... is a user support system best for this? not sure. would be great to have a support system for PEP 541 to help user support, Van (general counsel) to approve, etc.

  - probably not directly in scope for Facebook work

  - [https://github.com/pypa/warehouse/issues/4004](https://github.com/pypa/warehouse/issues/4004) Name-Squatting on Pypi.org: Removed projects if no code is added after 6+ months

  - [https://github.com/pypa/warehouse/issues/4520](https://github.com/pypa/warehouse/issues/4520) Packages without releases should not be on /simple

  - [https://github.com/pypa/warehouse/issues/1388](https://github.com/pypa/warehouse/issues/1388) 404 for registered package with no release

  - [https://github.com/pypa/warehouse/issues/2082](https://github.com/pypa/warehouse/issues/2082) Add the ability to reserve a name

- broken packages:
  - [https://github.com/pypa/warehouse/issues/4003](https://github.com/pypa/warehouse/issues/4003) Broken/Unmaintained Python Projects on Pypi.org: Flag and then Remove after 30 days

  - [https://github.com/pypa/warehouse/issues/194](https://github.com/pypa/warehouse/issues/194) Automatically check uploaded packages (metadata, installability) \-- **related to scope**

    - whatever system we have to detect malicious uploads will be more general. pipeline, run checks, flag pkg for deletion/review/ok, etc.
    - Whoever is designing the system: consider we will probably want to put in some additional checks. But the checks themselves might not be in scope for Facebook work

- pretty sure this is NOT in scope: [https://github.com/pypa/warehouse/issues/798](https://github.com/pypa/warehouse/issues/798) Security vulnerability notification system

  - correct. not in scope. significant feature. may deserve its own grant.

## TODOs 

- Sumana to file issue on admin review of flagged packages (done: 6062) and open issue for discussing pre-upload checking of typosquatting (done: reopened 4998)

- Ernest to follow up on the open checkboxes on [https://github.com/pypa/warehouse/issues/2151#issuecomment-330178574](https://github.com/pypa/warehouse/issues/2151#issuecomment-330178574) \-- partially done, still needs to do \"Determine what stdlib modules exist in other Python Interpreters, PR to stdlib_list\"
