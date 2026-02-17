# PackagingWG/2018-02-20-Warehouse

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# Warehouse Sync-up Meeting 

Monday, Feb 19 2018

## Present: 

- Sumana
- Nicole
- Laura
- Dustin
- Ernest

## Current work/announcements/blocked: 

Ernest:

- \- RIP productivity last two-weeks attending/catching up from PyTN. Was hot to trot Saturday morning when suddenly SPAM

- \- Kubernetes Object creation is all that remains for full end-to-end deployment via our new infra tooling.

- \- **Blocker -** \[infrastructure deployment issue, requires Donald\]

Dustin

- Wrapped up account management & milestone #1

- Finished anything I can in Milestone #2

- not really blocked on anything right now, working on PR review and stuff in Milestone 3

- Also pushing forward [PEP](https://www.python.org/dev/peps/pep-0566/)[566](https://www.python.org/dev/peps/pep-0566/), which will eventually enable Markdown support in Warehouse

Nicole

- finished manage account features (needs user testing)

- issue 1354 - contributor ? package detail page

- issue 2880 - ?

- issue 2127 - accessibility issue - working on ui dropdowns - not accessible with keyboard

- not blocked

- working on talk proposal for EuroPython

Laura

- met with Ernest and helped create codebase description in docs: [https://warehouse.readthedocs.io/application/](https://warehouse.readthedocs.io/application/)

- Created promotional campaign in the PSF CRM

- Created a planning document for promoting the latest milestone to maintainers: [https://docs.google.com/document/d/1j1c-Waa2l0ikbfHblto5py9_KWiOgqgo02x2SLTKmKs/edit](https://docs.google.com/document/d/1j1c-Waa2l0ikbfHblto5py9_KWiOgqgo02x2SLTKmKs/edit)

Sumana:

- \- bug triage

- \- Twine RtD fix PR [https://github.com/pypa/twine/pull/297](https://github.com/pypa/twine/pull/297)

- \- sprint planning (Packaging WG email)

- \- PR testing/review

- \- helped volunteers via IRC/GitHub/email

## Bug/PR triage 

\* [https://github.com/pypa/warehouse/issues/2285](https://github.com/pypa/warehouse/issues/2285) Rename \"/legacy\" url to something else

- Currently milestone 4 (launch). Need to coordinate with: who? Packaging guide, twine, who else? And should we do this earlier, during the beta, to shake bugs out?

- Ernest: Problem is client support, we\'ve already changed the URL once\... with much confusion/frustration. Making `/v0`{.backtick} an alias to `/legacy`{.backtick} seems fine though (also trivial)

- Dustin: Personally, I don\'t think we should do this

- Sumana: comment with arguments (done)

\* Possible spamming of package namespace #2859 [https://github.com/pypa/warehouse/issues/2859](https://github.com/pypa/warehouse/issues/2859)

- user still has concerns
- Ernest: still waiting on PEP 541 (this is strictly not a MOSS grant scoped issue.)
- Sumana: update user to wait until PEP 541, give progress update (done)

\* [https://github.com/pypa/warehouse/issues/2533](https://github.com/pypa/warehouse/issues/2533) \"499 Client Error: Client Disconnected for url: [https://upload.pypi.org/legacy/](https://upload.pypi.org/legacy/)\"

- Confusing user experience, unclear where problem originates
- Ernest: Honestly no idea either. We\'re going to be moving the upload infra soon\... so we\'ll probably solve and create a whole new host of similar issues. Unclear path forward.
- Ernest: This \_might\_ be an issue with Heroku\'s HTTP routing. Not sure :/
- Dustin: Seems like some existing issues were due to metadata failing validation? Need example distributions from affected users to be sure
- Sumana - ask user for more details (done)

\* [https://github.com/pypa/warehouse/issues/916](https://github.com/pypa/warehouse/issues/916) option to turn off indexing in robots.txt across instance (e.g., Test PyPI)

- should we offer this at all? or should such an organization use devpi?

- Ernest: Not sure what devpi has to do with this. The tl;dr is that the \"test\" instance of PyPI really has no need to be indexed by search engines.

- Task: we should do this when we can.

- Dustin: ditto, this is something we should do but is not crucial

- Can be done using headers also \-- add as a nice to have issue

- Resolution: [Sumana will update as cool-but-not-urgent] Ernest has created [a PR](https://github.com/pypa/warehouse/pull/2995)

\* [https://github.com/pypa/warehouse/issues/1000](https://github.com/pypa/warehouse/issues/1000) Email all owners when a new owner/maintainer is added

- Milestone 4: Launch?
- Ernest: New Feature, falls into security/audit \*\*Post-Launch\*\*
- Dustin: This is easy to do now. We should also send an email notification to newly added collaborators
- Resolution: Sumana to update as post-launch (done)

\* [https://github.com/pypa/warehouse/issues/998](https://github.com/pypa/warehouse/issues/998) Send confirmation when email address changes

- Milestone 4: Launch?
- Ernest: New Feature, falls into security/audit \*\*Post-Launch\*\* (BUT GREAT IDEA)
- Dustin: I punted on this in email management, would be good to do this post-launch
- Resolution: Sumana to update as post-launch (done)

\* [https://github.com/pypa/warehouse/issues/997](https://github.com/pypa/warehouse/issues/997) Email all owners when a new version of a package is uploaded

- Cool But Not Urgent?
- Ernest: New Feature, falls into security/audit \*\*Post-Launch\*\*
- Dustin: ditto
- Resolution: Sumana to update as post-launch (done)

\* [https://github.com/pypa/warehouse/issues/469](https://github.com/pypa/warehouse/issues/469) Disallow runs of special characters in project names

- just for readability, or also for user confusion that might cause security issues?
- Ernest: This would require PEPs to be modified. Not in scope for MOSS grant work.
- Resolution: Sumana to update noting it\'s not in scope for MOSS work (done)

\* [https://pyfound.blogspot.com/2017/01/time-to-upgrade-your-python-tls-v12.html](https://pyfound.blogspot.com/2017/01/time-to-upgrade-your-python-tls-v12.html)

- issue to re-publicize the upcoming deadlines?
- Ernest: Mehhhhhhhhhh our request rate for TLSv1.0 and TLSv1.1 is \_orders of magnitude\_ lower than TLSv1.2
- Ernest: Outside scope of MOSS grant work, will affect all PSF services hosted behind Fastly. Will take this to Infra-WG+
- Small number of users use outdated protocols - Ernest will ask PSF to tweet about it

\* [https://github.com/pypa/warehouse/issues/582](https://github.com/pypa/warehouse/issues/582) ability to delete legacy docs

- who should decide on the policy so we can move forward?
- Eric - wants a separate RTD instance for PyPI, but how do we know where users are coming from, and who can update those docs?
- blocked on clear path forward on handling documentation, need docs url
- Who can make authoritative decision - Packaging WG?
- Ernest will send a message to Eric
- PyPI not in business of hosting docs \-- need division of who does what

## Ask Donald to: 

- [https://github.com/pypa/warehouse/issues/2216](https://github.com/pypa/warehouse/issues/2216) \<- not just do this, but also help us make sure we can do it in the same way w/o him

  - Ties back into the dang db dump tooling. This requires some automated scrubbing to get right.

- [https://github.com/pypa/warehouse/issues/2287](https://github.com/pypa/warehouse/issues/2287) \<- Dustin can do this if Nicole or Ernest can give access to the repo (or banner can go away at launch)

  - Ernest can grant Nicole and Dustin access to that repo

## Milestone progress 

[We\'ve hit Milestone 1 and are on to Milestone 2!](https://github.com/pypa/warehouse/projects/1)

We\'ll decouple testing/promotional tasks for Milestone 2 from milestone schedule, since we\'ll hit Milestone 2 before we\'re done getting maintainer MVP feedback.

## TODO 

- add a nice to have issue for a \"report spam\" button
  - +1, once [https://github.com/pypa/warehouse/pull/2991](https://github.com/pypa/warehouse/pull/2991) is merged
- Ernest to talk to Infrastructure WG about TLS deadline
- Ernest to talk to Eric about hosted documentation question (DONE)
