# PackagingWG/2018-02-12-Warehouse

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

Warehouse weekly meeting notes

Monday, Feb. 12, 2018

## Present: 

- Sumana
- Laura
- Mark
- Dustin
- Ernest
- Nicole

## Current work/announcements: 

Ernest:

- \"Just dumb week last week.\"
- \[infrastructure discussion\]
- working on platform setup for deployments \-- can shift into Warehouse mode if blocked on that

Nicole:

- focused on release detail page

- functionality for managing a project is working

- will work on manage email PR

- will do testing of new UI
  - Ernest: Eagerly Volunteers :-D
  - Laura: I can help test UI

- Not blocked, needs Dustin to set up branch for reset password - \\o/ - already in progress ![:D](/wiki/europython/img/biggrin.png ":D")

Dustin:

- In Progress/blocked
  - Manage Emails
  - Reset Password
  - Delete Account - last bit of work for me in Milestone #1
- Moving on to Milestone #2

Sumana:

- bug triage, doc improvement for PyPA website
- stakeholder communication

Laura:

- twine docs PRs merged [https://github.com/pypa/twine/pulls?utf8=%E2%9C%93&q=is%3Apr+author%3Algh2+](https://github.com/pypa/twine/pulls?utf8=%E2%9C%93&q=is%3Apr+author%3Algh2+)

- Reviewed PR to add additional emails to account

- Created a draft plan for promotion post-Maintainer MVP milestone:
  - Landing page for testers will be on Packaging WG wiki
  - First reach out to a small group of active maintainers/power users (\~100 humans)
  - Then, when power users are happy, reach out to top 100 most active projects

- Brainstorming document for promotional activities: (shared with group)

- Need to test [manage email changes PR](https://github.com/pypa/warehouse/pull/2898) per Dustin

Mark:

- Donald has approved changes for PEP541, next steps to review and discuss with packaging-wg.
- Worked on \[infrastructure\], \[contact\] will hopefully get back to us soon.
- Would like to help with testing of any UI stuff.
- \[finance detail\]
- Mark out February 19th

## Bug/PR triage: 

\* [https://github.com/pypa/warehouse/issues/2850](https://github.com/pypa/warehouse/issues/2850) Support searching for an exact phrase #2850

- Sumana Suggestion: milestone 3, publicizing beta. Search is already better on Warehouse - good contribution for someone familiar with Elasticsearch - nice to have
- Sumana\'s now updated this.

\* [https://github.com/pypa/warehouse/issues/345](https://github.com/pypa/warehouse/issues/345) Ability to mark a version of a package as deprecated or unsupported #345

- Sumana Suggestion: Post-launch
- Sumana\'s now updated this.

\* [https://github.com/pypa/warehouse/issues/2206](https://github.com/pypa/warehouse/issues/2206) Sort user page project list by last release date #2206

- Was a PR, closed due to test issues - SH will reach out to see if contributor can work on it again

- [https://github.com/pypa/warehouse/pull/2213#issuecomment-352225097](https://github.com/pypa/warehouse/pull/2213#issuecomment-352225097) \-- had problems with running tests

- Sumana\'s replied and marked the issue in the beta publicizing milestone

\* JSON API documentation [https://github.com/pypa/warehouse/issues/2913](https://github.com/pypa/warehouse/issues/2913)

- Sumana Suggestion: milestone 4, launch
- PR exists - needs more prose, change pypi.python.org to pypi.org
- Should have this in time to publicize beta \-- read-only API for programmatic access
- Break into minimum (user mvp) vs. fuller docs
- Sumana\'s updated the issue

\* Request for Trio trove classifier [https://github.com/pypa/warehouse/issues/2881](https://github.com/pypa/warehouse/issues/2881)

- Sumana Suggestion: maintainer MVP
- Can only be done by administrator of pypi \-- we\'ll add admin UI to Warehouse before final launch
  - Ernest has done the trove update task, Sumana has moved [https://github.com/pypa/warehouse/issues/2649](https://github.com/pypa/warehouse/issues/2649) to milestone 4

\* [https://github.com/pypa/warehouse/issues/2401](https://github.com/pypa/warehouse/issues/2401) Indicate in UI/API if a name has been prohibited #2401

- Sumana Suggestion: milestone 4, launch
- may allow malicious users to determine what the blacklist is
- FAQ addresses why some names are prohibited - how/where do we currently link to this?
- Have UI for packages removed by author? Not common
- This is a question about UI for \*upload\*, not search, so how much does it protect non-package-maintainer users?
- PEP 541 to take care of a bunch of this\....
- SH will share thoughts with Packaging WG before commenting

\* [https://github.com/pypa/warehouse/issues/994](https://github.com/pypa/warehouse/issues/994) Add support for API keys #994

- lukesneeringer wants to scope this out and asks whether anyone objects, volunteers to do this work + two-factor auth
- Yes - Luke can work on this \-- mark as post-launch milestone
- Sumana has updated the issue

\* [https://github.com/pypa/warehouse/issues/360](https://github.com/pypa/warehouse/issues/360) Add some sort of webhooks support #360

- Sumana Suggestion: post-launch
- New feature, not in legacy
- Sumana has updated the issue

\* [https://github.com/pypa/warehouse/issues/1855](https://github.com/pypa/warehouse/issues/1855) Expose what extras are available for install #1855

- Sumana Suggestion: cool but not urgent
- Nice to have - nice additional feature
- Sumana updated the issue

\* Issue 999

- Nicole asks about this. maintainer MVP - will be closed with change password PR.

## Things to ask Donald to do: 

Sumana to find out his current PyPA work

## Maintainer MVP milestone work remaining: 

[https://github.com/pypa/warehouse/milestone/8](https://github.com/pypa/warehouse/milestone/8)

Still on schedule for maintainer MVP milestone at end of Feb, and in fact, may well be substantially earlier

[https://github.com/pypa/warehouse/projects/1](https://github.com/pypa/warehouse/projects/1) is a helpful overview, teammates say

Dustin and Nicole report they believe their Maintainer MVP issues will be resolved by Monday Feb 19th, unless her UI testing reveals showstoppers

Infrastructure readiness: Barring unforeseen issues, we can promote maintainer MVP on Heroku. Infra changeover needs to be done before milestone 3, but we can shift over a fraction of pip installs starting at milestone 2 \-- need monitoring and metrics to do this.

Cautious optimism about publicizing Maintainer MVP middle of next week

## To do: 

- Sumana to email packaging wg about [https://github.com/pypa/warehouse/issues/2401](https://github.com/pypa/warehouse/issues/2401) Indicate in UI/API if a name has been prohibited #2401
