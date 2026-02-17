# PackagingWG/2018-01-10-Warehouse

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# Maintainer MVP Milestone discussion 

Sync-up and discussion of due date January 10, 2018

Present:

- Sumana Harihareswara
- Laura Hampton
- Ernest W. Durbin III
- Nicole Harris
- Dustin Ingram
- Donald Stufft
- Mark Mangoba

## Current work 

What are you working on? Any blockers?

- Ernest: Next layer up of deployment infra - Service management and configuration. Timeline: Hope to have MVP for service creation/management next week, deploying warehouse to Kubernetes

- Dustin: issues in first milestone, role maintenance, password resets 

- Nicole: architecture for managers, [#424](https://github.com/pypa/warehouse/issues/424), password reset pages needs feedback re UI 

- Donald: Discussing PR feedback 

## Maintainer MVP milestone work remaining 

Schedule and decide tentative deadline for [first milestone](https://github.com/pypa/warehouse/milestone/8)

- Many issues are dependent on Nicole\'s availability

- [\"Enable pages to delete, hide, unhide a project/release/file\"](https://github.com/pypa/warehouse/issues/424) - needs files (Hide/unhide is not critical)

- Ernest notes: maintainers may need journal for auditing. New tickets for journal? - only need release journal for first milestone

- TODO: Nicole and Donald: move issue re information from sdist [https://github.com/pypa/warehouse/issues/2734](https://github.com/pypa/warehouse/issues/2734) (conversation regarding `PKG-INFO`{.backtick} display that we currently support)

- TODO: Nicole/Ernest - rough in buttons for managing/deleting documentation (Ernest notes: no real blocker as he is sure Nicole can help him fix it up in a PR, after Ernest finishes current infrastructure tasks)

- Nicole is working on page for managing versions and viewing journal

- Nicole blocked on:
  - [documentation needs (Sumana\'s addressed (as of Friday))](https://github.com/pypa/warehouse/issues/1322#issuecomment-352983065)

  - [documentation needs (Sumana\'s addressed (as of Friday))](https://github.com/pypa/warehouse/issues/1989#issuecomment-352898668)

  - Needs [password PR](https://github.com/pypa/warehouse/pull/1262) merged (now done)

  - Needs role/collaborator form updated - [Dustin is working on this](https://github.com/pypa/warehouse/pull/2705)

  - Nicole: view for logged in users to view detail of a release (this view can be empty, for now Nicole just needs a URL so she can build a static form / tables, etc.; Dustin is working on this)

## Statements/News 

- Ernest: I have Warehouse Logo stickers arriving today. Need your mailing addresses :-p

## Questions 

Ernest: Have we gotten an idea where we are at with \$ burn and time remaining for participants?

- Mark: answer to come (was provided to team later that week)

Dustin: How do we want to handle PR reviews given Donald\'s limited time?

- Ernest: Assignments via GitHub work best for me to keep on top of (I see now that I have had a review requested\... this is a tab I just learned about D:)

- TODO: Sumana to check on requests for Donald, ping him (Sumana\'s now started doing this)

- Need more committers, but no one available

- Committers: Donald, Ernest, Nicole, Dustin, Alex Gaynor (does dependency upgrades)

- Need more reviewers in the long run \-- we aim to grow this capability somewhat organically
