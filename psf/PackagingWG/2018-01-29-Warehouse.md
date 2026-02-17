# PackagingWG/2018-01-29-Warehouse

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# Maintainer MVP Milestone discussion 

Sync-up, bug triage, and discussion of Maintainer MVP delivery date

January 29, 2018

## Summary 

We\'re tentatively saying the Maintainer MVP milestone will be ready Feb. 28th, 2018.

Present:

- Sumana Harihareswara
- Laura Hampton
- Ernest W. Durbin III
- Nicole Harris
- Dustin Ingram
- Mark Mangoba

## Current work 

What are you working on? Any blockers?

- Sumana:
  - Requested [the new PyPI announce mailing list](https://mail.python.org/mm3/mailman3/lists/pypi-announce.python.org/), tested uploading a package to TestPyPI, and investigated other Warehouse dependencies (that last activity is continuing).

  - No external blockers.
- Ernest:
  - Reminds us that it\'s Pie Pea Eye not Pie Pie :-D (we\'re not [PyPy](./PyPy.html); consistent pronunciation is helpful for community outreach).

  - Has been SQL querying for active maintainers/projects (have maintainer contact info). Planning to start writing some announcer emails for active maintainers & big projects tomorrow! Will share in Slack channel with other teammates.

  - Has been working on the last stretch of deployment tooling, got hamstrung on a stupid Docker Auth thing. Got great help from community here ![:)](/wiki/europython/img/smile.png ":)")

  - No external blockers at the moment.
- Dustin:
  - Has been working on logged-in profile/project management, on changing user display name, and on adding email addresses, and the feature where users can confirm email addresses.
  - No external blockers.
- Nicole:
  - Is working on profile management page, which is done from a UI perspective.

  - Needs to style the feature(s) Dustin is working on.

  - Next, will work on mobile UI for project releases and maintainers pages.

  - Called out [issue 1989](https://github.com/pypa/warehouse/issues/1989) where we are waiting on answer for privacy and CoC; Mark says he can ping Van.

  - Called out [issue 2809](https://github.com/pypa/warehouse/issues/2809), as we are missing information on how to create new release on a project \-- this needs to point to documentation. Sumana to update issue noting it needs discussion.

  - Is blocked on manage release page (list files of release, list release journal) - needs an empty view to get started. Dustin to do this.
- Laura:
  - Has prepared a spreadsheet of most-downloaded packages from PyPI & using libraries.io metrics, proxy for important projects in Python ecosystem, complement to SQL queries Ernest has run.

  - Blocked on discussing: promotion to testers, media, schedule, & landing page for Warehouse testers.

## Bug triage 

What milestone does each issue belong in?

- [Determine new API URL structure for warehouse (starting with new JSON API)](https://github.com/pypa/warehouse/issues/284)

  - Even though this may be necessary for some Twine improvements, we decided that this is not a Pre-launch or Maintainer MVP ticket. This is a new feature and is best suited for Post-Launch; Warehouse needs to be done before we can improve twine.

  [Missing Access-Control-Allow-Origin in redirect headers](https://github.com/pypa/warehouse/issues/2825)

  - This seems reasonable, but not critical. We think it should be considered a \"task\" in the canonical URL handling code. It can be done post-launch and it should have a \"good first contribution\" tag.

- [Search method in XML-RPC API problem](https://github.com/pypa/warehouse/issues/1886)

  - This is probably a small fix and is a theoretical bugfix \-- we need to compare it to behavior on legacy PyPI. (XML-RPC is not the direction we want to go in, regardless.) Milestone: End user MVP.

- [Add documentation for admin logins in dev](https://github.com/pypa/warehouse/issues/2713)

  - This should be addressed as part of or while addressing [the issue on updating the development database](https://github.com/pypa/warehouse/issues/2216). It\'s a developer experience bug. It\'s already documented but kinda buried [in our development docs](https://warehouse.pypa.io/development/getting-started/?highlight=password#what-did-we-just-do-and-what-is-happening-behind-the-scenes). We should put this in a post-Maintainer MVP milestone, perhaps in End User MVP, and add a note to have Ernest and Donald add instructions for logging in into the developer docs.

- [Disable \"view project\" links when project has no releases](https://github.com/pypa/warehouse/issues/2828)

  - Dustin and Nicole agreed this belongs in Maintainer MVP.

## Maintainer MVP milestone work remaining 

Schedule and decide tentative deadline for [first milestone](https://github.com/pypa/warehouse/milestone/8)

- On an infrastructure level: Overall, our timeline is that it\'ll be done very soon, and we estimate we\'ll have an end-to-end demoable this week. We need to get the basic bits out and start knocking them around. We\'re going to have some infrastructure credits and, once we get those confirmed, we\'ll get a Kubernetes cluster up. We\'re also throwing an MVP of [Cabotage (our deployment tooling)](https://github.com/cabotage/cabotage-app) on top of that. Once the infrastructure piece is solid, Ernest can turn more of his attention to Warehouse feature development, bugfixing, and code review.

- In parallel, Nicole and Dustin are working on the remaining issues in the milestone; Nicole thinks it\'ll take her 2-3 weeks to finish the remaining issues on her plate (e.g., mobile UIs). Dustin believes we can probably finish the Maintainer MVP milestone in the month of February.

Summary: we expect to have the Maintainer MVP milestone out by Feb. 28th.

## To Do 

- Sumana:
  - note on [issue 2809](https://github.com/pypa/warehouse/issues/2809) that it needs discussion.
- Dustin:
  - Stub out individual release view to unblock Nicole
- Mark:
  - Revisit policy/documentation around [CoC/privacy policy issue](https://github.com/pypa/warehouse/issues/1989)
- Ernest:
  - Investigate [how current DB fixtures were created (#2216)](https://github.com/pypa/warehouse/issues/2216) and [Ask Donald, address #2713 - docs re admin login along the way](https://github.com/pypa/warehouse/issues/2713).

  - Coordinate annoucements re infra credits
