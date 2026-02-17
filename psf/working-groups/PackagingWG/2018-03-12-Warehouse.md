# PackagingWG/2018-03-12-Warehouse

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

Warehouse Sync-up Meeting

Monday, March 12th

## Present 

- Laura
- Sumana
- Mark
- Ernest
- Nicole
- Dustin

**Working on/blocked/announcements**

Dustin

- user page cache purging - user profile page changes when deletes things
- making deletes cascade
- handling a lot of new contributor PRs / support - may scale back
- triaging bug reports
- mildly blocked on camo ? need to redeploy to Heroku or new thing

Mark

- PEP 541: Edit to move final decisions to the Packaging-Workgroup, use PSF Board as a advisory and resource when needed.

- As PEP 541 moves forward, would like to start a discussion about implementation: example, moving disputes, request over to [GitHub](./GitHub.html) or possible tooling in Warehouse Admin.

- Follow up e-mail sent to Open Technology Fund.

- Warehouse Fundraising tooling - possible PSF Grant.

- awaiting general feedback from Packaging wg

Nicole

- Finishing user testing - opening \*lots\* of tickets
- Writing up user testing, recruiting help with next round
- will work on things that are blocking Dustin
- Will review open PRs (PR from Laura), respond to some issues I have been pinged on
- work on bugs in next milestone - ? modal bug, refactor dropdowns
- TODO: SH look at material Nicole sent

Ernest

- Major lift of Kubes work is done, we can iterate rather quickly on it now!

- Conveyor is now running on K8s! in production

- \"Production\" instance on our new Kubernetes cluster up at [https://warehouse.cmh1.psfhosted.org](https://warehouse.cmh1.psfhosted.org) (warning may come and go, but \_shouldn\'t\_)

- Going to be getting Automated deploys working tomorrow including DB migrations. This is last mile for swapping pypi.org over to kubes!

- Today is a no MOSS grant day catching up on [PyCon](./PyCon.html) work and prepping for CLEpy.

- demo will come after meeting in Slack

Laura

- working on [https://github.com/pypa/warehouse/pull/3047](https://github.com/pypa/warehouse/pull/3047) - may need to relocate to someplace with better wifi in order to finish - Nicole to review ![:)](/wiki/europython/img/smile.png ":)")

Sumana

- did a lot of bug triage

- fixed and wrote some docs, like a migration guide for 3rd-party services [https://github.com/pypa/warehouse/pull/3153](https://github.com/pypa/warehouse/pull/3153) and API docs [https://github.com/pypa/warehouse/pull/3173](https://github.com/pypa/warehouse/pull/3173)

- updated error messages in upload API [https://github.com/pypa/warehouse/pull/3175](https://github.com/pypa/warehouse/pull/3175) & [https://github.com/pypa/warehouse/pull/3183](https://github.com/pypa/warehouse/pull/3183)

- may be unavailable around March 22-25

- made [https://wiki.python.org/psf/PackagingSprints](https://wiki.python.org/psf/PackagingSprints)

## Ernest demo - 10min 

DEMMOOOOOOOOOO Cancelled ![:(](/wiki/europython/img/sad.png ":(") Realized a screencast in #moss-grant/#packaging-wg is more useful since not everyone joins this call via the UberConference app.

## When will we hit beta? 

[https://github.com/pypa/warehouse/milestones](https://github.com/pypa/warehouse/milestones) - 8 open issues till beta, then 19 more till launch

- Dustin - many issues are small, docs, reaching out to 3rd parties - end of this week?
- Nicole - not a lot of work, this week
- Ernest - this week - will be adding metrics

## Ask Donald for 

#3108 feedback

## Bug triage 

no Last-Modified header on file downloads #3108 [https://github.com/pypa/warehouse/issues/3108](https://github.com/pypa/warehouse/issues/3108)

- Sumana suggests: fix before shutting down legacy, since we\'re stripping this date on Warehouse but it was intact on legacy +1 Ernest also thinks we should do something about it, is regression
- Ernest: +1

account recovery policy, FAQ, and tooling #3016 [https://github.com/pypa/warehouse/issues/3016](https://github.com/pypa/warehouse/issues/3016)

- What\'s our policy on helping them, and what\'s our policy on verifying their claim?
  - Case-by-case basis
  - if person can prove they have or had domain, project page \-- claims to names must be investigated case-by-case
  - Add something to FAQ, establish separate support queue for customer support
- Do Warehouse administrators want better tooling for account recovery?
  - [https://github.com/pypa/warehouse/issues/3176](https://github.com/pypa/warehouse/issues/3176) would be nice

ISO 8601 dates (and times) #3010 [https://github.com/pypa/warehouse/issues/3010](https://github.com/pypa/warehouse/issues/3010)

- Sumana suggests: we used ISO 8601 dates on legacy. Let\'s fix this before legacy shutdown, to help European users.
- DI: ISO 8601 is great for machines but \"2018-03-12\" is more ambiguous than \"March 12, 2018\" without context for what format the date is in
- Design question - assigned to Nicole

Search does not prioritize exact match when package name contains numbers #2877 [https://github.com/pypa/warehouse/issues/2877](https://github.com/pypa/warehouse/issues/2877)

- need to fix before shutting down legacy? No
- Not a huge deal

\"pip install x\" might work or not #3006 [https://github.com/pypa/warehouse/issues/3006](https://github.com/pypa/warehouse/issues/3006)

- how likely is this a problem? what milestone?
- Seems pretty unlikely to me that a package on PyPI is not pip-installable\...
- Design/UX - talk to people about expectations on PyPI
- Nicole has assigned to herself
- gatekeep - need to have conversation with maintainers if package is not pip installable
- post-legacy

"test your bus factor" promo page #3121 [https://github.com/pypa/warehouse/issues/3121](https://github.com/pypa/warehouse/issues/3121) and Add \'sole owner\' badge on list of projects #3127 [https://github.com/pypa/warehouse/issues/3127](https://github.com/pypa/warehouse/issues/3127)

- are these so \"hey come see the new site\" appealing that we should get them done before launch?

- would be fine for post-launch promotion

- we should do [https://github.com/pypa/warehouse/issues/3127](https://github.com/pypa/warehouse/issues/3127) first ![:)](/wiki/europython/img/smile.png ":)")

- if someone has spare time, not a priority, may users don\'t log in

- Sumana: sure, post-launch

- Most of the work will be design work? Might depend on how many hours left at the end for Nicole?

Add API endpoint to get latest version of all projects #347 [https://github.com/pypa/warehouse/issues/347#issuecomment-232470826](https://github.com/pypa/warehouse/issues/347#issuecomment-232470826)

- Ernest saying 2 years ago, \"to be clear, i\'m not opposed to supporting the specific feature request in this issue. but am trying to aide in guiding PyCharm off of the currently used index page they are scraping for this information. that page is incredibly expensive to generate and often causes congestion for the PyPI backends.\"

- Maybe should be part of [https://github.com/pypa/warehouse/issues/284](https://github.com/pypa/warehouse/issues/284)

- New feature - page in EWD quote is gone - post-launch, post MOSS grant

- [https://pypi.python.org/pypi/](https://pypi.python.org/pypi/) is the old page.

**TODO**

Ernest:

- Deploy camo via cabotage?

NLH:

- [https://github.com/python/pypi-theme/issues/12](https://github.com/python/pypi-theme/issues/12) (can do tomorrow)

- [https://github.com/python/pypi-theme/issues/13](https://github.com/python/pypi-theme/issues/13) (can do tomorrow)

Sumana: Add issue for customer support queue
