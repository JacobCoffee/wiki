# PackagingWG/2017-12-19-Warehouse

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

Meeting: Tuesday, Dec. 19th Attendees:

- Laura Hampton
- Ernest W. Durbin III
- Dustin Ingram
- Mark Mangoba
- Sumana Harihareswara
- Donald Stufft
- Nicole Harris

**I. Which of these issues ought to be in the Maintainer MVP milestone?** Maintainer MVP milestone: [https://github.com/pypa/warehouse/milestone/8](https://github.com/pypa/warehouse/milestone/8) Probable:

- [https://github.com/pypa/warehouse/issues/424](https://github.com/pypa/warehouse/issues/424) We need UI that will allow users to modify the project/release/files they register & upload to Warehouse.

  - Upload may be deprecated, but how should users modify?

  - *Resolution:* Ernest - absolutely MVP milestone

  - Ernest: Do we need to update this to include \"delete\" for files, releases, projects?

  - Ernest: Sounds like we may not want to allow for updating metadata at all

  - Followup with Donald?

  - Donald - don\'t allow modifying metadata
    - Dustin: give people an alternative, e.g., staged releases, Markdown support
    - but current feature parity does not demand that.

  - *Resolution:* WONTFIX the metadata change \-- people generally legitimately want this because of a typo in .rst, so test it first. otherwise, open to malicious stuff, & changing this breaks pip show. But the sub-issue that\'s about deletion needs to happen, as does managing hidden vs unhidden releases

    - TODO: Sumana & Donald to update per above

- [https://github.com/pypa/warehouse/issues/423](https://github.com/pypa/warehouse/issues/423) - Enable users to modify their own account

  - *Resolution:* Ernest - absolutely MVP milestone

  - Existing PR: [https://github.com/pypa/warehouse/pull/1847](https://github.com/pypa/warehouse/pull/1847)

    - TODO: Sumana to message contributor to say \.... \-- we have time to work on this, do you have time to update & rebase in the next few days?

  - Nicole: do we want to do dummy backend first? or backend first? if someone could create empty view with empty template in next few days, I have somewhere to put HTML, I could work on it
    - Dustin will provide this

- [https://github.com/pypa/warehouse/issues/956](https://github.com/pypa/warehouse/issues/956) UI for adding maintainers

  - *Resolution:* Ernest - absolutely MVP milestone

- [https://github.com/pypa/warehouse/issues/1228](https://github.com/pypa/warehouse/issues/1228) Implement \"forgot password\" feature

  - *Resolution:* Ernest - absolutely MVP milestone

  - Existing PR: [https://github.com/pypa/warehouse/pull/1262](https://github.com/pypa/warehouse/pull/1262)

    - TODO: Sumana to message contributor to say \.... \-- we have time to work on this, do you have time to update & rebase in the next few days?

- [https://github.com/pypa/warehouse/issues/2216](https://github.com/pypa/warehouse/issues/2216) Classifiers in development DB are out of date

  - Dustin - mild annoyance for users - consult Donald; issue is out of date

  - *Resolution:* push to later milestone

- [https://github.com/pypa/warehouse/issues/2418](https://github.com/pypa/warehouse/issues/2418) Blacklisting project does not purge the cache

  - Security implications?

  - Ernest: this is just a bug\... self-assigned!

  - *Resolution:* Ernest - part of MVP milestone

Also need to discuss (issues added during meeting):

- [https://github.com/pypa/warehouse/issues/61](https://github.com/pypa/warehouse/issues/61) OpenID Login/Google Login?

  - Ernest: Probably \_should\_ be available, but not \_strictly\_ necessary for Maintainer MVP

  - Donald: Deprecate before legacy shutdown

  - Ernest: TODO: Deprecation notice on Google Auth/OpenID Login

  - *Resolution:* Donald - not maintainer MVP since all maintainers will not be using Google Auth/OpenID

  - Donald: TODO: Poke hornets nest on this (distutils-sig discussion)

- [https://github.com/pypa/warehouse/issues/582](https://github.com/pypa/warehouse/issues/582) Removal/Redirect \-- documentation uploaded to python-hosted

  - Explanation: you used to be able to upload a tarball we would extract & host on a path at pythonhosted and people used that as official hosting (some people)

  - has never worked great. S3 usage is expensive \-- when we switched uploading to Warehouse, did not implement doc upload API. All those people who had previously uploaded files to this static site needed a way to deal with that. Ernest? implemented a button to delete all files we had \[for each user?\] \.... unhappiness re throwing away juice

  - Ernest: happy to own & drive this, Nick Coghlan. Ernest TODO to lead on community basis on getting out of this situation and moving forward.

    - *Resolution:* biggest thing for maintainer MVP: a delete button and/or redirect button

    - but open redirect problem/issue/ to watch out for

Maybe:

- [https://github.com/pypa/warehouse/issues/398](https://github.com/pypa/warehouse/issues/398) Hook sessions into pyramid_tm to make them transactional

  - Ernest - this may done? Implementation detail.

  - *Resolution:* Donald - not an issue for the MVP milestone

- [https://github.com/pypa/warehouse/issues/2144](https://github.com/pypa/warehouse/issues/2144) import SCSS tools

  - Ernest - consult Nicole

  - *Resolution:* Nicole: just a refactor, not for any milestone

- [https://github.com/pypa/warehouse/issues/1919](https://github.com/pypa/warehouse/issues/1919) functionality to rename a project

  - *Resolution:* Ernest: new feature! def not MVP/milestone1 likely an \"admin\" feature.

- [https://github.com/pypa/warehouse/issues/472](https://github.com/pypa/warehouse/issues/472) Handle Version Sorting *(or a related issue, or breaking out a sub-issue?)*

  - *Resolution:* Ernest: [https://github.com/pypa/warehouse/issues/472#issuecomment-295899658](https://github.com/pypa/warehouse/issues/472#issuecomment-295899658) notes that this is not milestone1

- [https://github.com/pypa/warehouse/issues/1536](https://github.com/pypa/warehouse/issues/1536) Tests depend on `manifest.json`{.backtick} existing

  - *Resolution:* Dustin - not part of MVP milestone

Sumana wonders whether previous decision was correct ![:)](/wiki/europython/img/smile.png%20":)") :

- [https://github.com/pypa/warehouse/issues/2486](https://github.com/pypa/warehouse/issues/2486) File size limit error message should include size of the limit

  - *Resolution:* Dustin - I think this can be included in the MVP

  - Existing PR: [https://github.com/pypa/warehouse/pull/2487](https://github.com/pypa/warehouse/pull/2487)

- [https://github.com/pypa/warehouse/issues/1322](https://github.com/pypa/warehouse/issues/1322) Add roadmap to documentation - link to it from footer

  - Donald - out of date one may be worse than none
  - Sumana - need roadmap only during project, and then remove?
    - *Resolution:* add to MVP milestone, remove in launch milestone

- [https://github.com/pypa/warehouse/issues/2170](https://github.com/pypa/warehouse/issues/2170) How to update the \"Description\" in pypi.org ?

  - Dustin - Likely not going to be supported
    - Instead: staged releases [https://github.com/pypa/warehouse/issues/726](https://github.com/pypa/warehouse/issues/726) , supporting Markdown [https://github.com/pypa/warehouse/issues/2206](https://github.com/pypa/warehouse/issues/2206) , telling people to run `python setup.py check -r -s`{.backtick} first [https://github.com/pypa/python-packaging-user-guide/issues/210](https://github.com/pypa/python-packaging-user-guide/issues/210)

  - Ernest - not part of MVP milestone

  - Donald - not part of MVP milestone

  - Ernest: Indeed, this ties back into #424 relating to not allowing for update to metadata

  - Ernest: Personally I\'m \_for\_ allowing description updates in a limited time period after release (1-2wks)

  - *RESOLUTION:* say: we\'re not going to do this right now, but let\'s discuss on distutils-sig (this is now at [https://mail.python.org/pipermail/distutils-sig/2017-December/031826.html](https://mail.python.org/pipermail/distutils-sig/2017-December/031826.html) )

    - TODO: Donald to WONTFIX

- [https://github.com/pypa/warehouse/issues/789](https://github.com/pypa/warehouse/issues/789) Dependency and Reverse Dependency

  - *Resolution:* Ernest: Definitely not MVP/milestone1, this is a new feature ![:)](/wiki/europython/img/smile.png%20":)")

**II. Discuss schedule and decide: what is our tentative deadline for the first milestone?** Assignments - what\'s on whose plate?

- Dustin:
  - Will stub out some pages for Nicole so she can get started, wrap up role maintenance as well

- Ernest:
  - Ernest: Deprecation/Password warning on Google/OpenID Login for pypi-legacy

  - Ernest: [https://github.com/pypa/warehouse/issues/582](https://github.com/pypa/warehouse/issues/582) notes on delete/redirect for pythonhosted

  - Ernest: Ping E. Holscher on [https://github.com/pypa/warehouse/issues/582](https://github.com/pypa/warehouse/issues/582)

  - Ernest: Continuing to push platform/foundation for kuberenetes deploy - Hope to have this done and move onto actual warehouse things by EOW

- Donald:
  - leave comments on updating description & openID/Google login (2170 & 424 & 61)

- Nicole:
  - maintainer UI & forgot password (956 & 1228)

- Sumana & Laura:

  - turn notes from this meeting into [GitHub](./GitHub.html) updates, solidify Milestone 1

Deferred till after [GitHub](./GitHub.html) updates:

- Figure out hours estimates for these issues and delivery date range
