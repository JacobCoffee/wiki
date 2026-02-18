# PackagingWG/2019-07-31-Warehouse

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

## Audit log design 

July 31, 2019, conference call

Participants:

- Will
- Sumana
- Ernest
- Dustin
- Donald
- Nicole

Issue: [https://github.com/pypa/warehouse/issues/5863](https://github.com/pypa/warehouse/issues/5863) \-- putting summary of this meeting in a comment on that issue

Goal: review approaches to designing audit log functionality

### Basic design approach for auditing API 

Will asked a few general approach questions.

How do we want the auditing API to look? 3 choices:

- \* Option: Piggyback on existing metrics calls
  - \* Challenge: Impedance mismatch, not all audit events are metrics and vice versa
- \* Option: New API, called in tandem with metrics calls in places where both are needed/desired
  - Donald: This is my top pick as well.
  - Ernest: This is my top pick, allows for explicit addition in any context. Metrics can/are kinda diffff
  - Dustin agrees
- \* Option: New API, metrics calls folded into it
  - \* Challenge: Same impedance mismatch as above

*Our choice*: New API, called in tandem with metrics calls in places where both are needed/desired.

### Storage 

2nd question: Storage! How long a duration? Up to last n auditable records, up to last n weeks, FOREVERRR, etc.? maybe not do this inside of Postgres, use a document store?

- Ernest: I think storage with some amount of flexibility would be ideal. Tag, Time, IP, User, action \"short name\", and maybe a JSONB column for metadata or additional information?

Our journal is just Postgres tables. 2 classes of audit info to store:

- 1\) associated with projects. Project history - indefinite. Actions affecting access, releases, changes to a project: let\'s store FOREVER
- 2\) user behavior: PII-type stuff; probably want a reasonable duration on\... time-based?
  - legal: need to comply with GDPR. At request of users, need to be able to delete PII that is NOT required for the functioning of PyPI operations.

  - account stuff: audit system will be used for many kinds of events. \"New location\" & \"sign-in attempt failed\" is needed to fire at event, store for limited amount of time

  - ?? is there good prior art on duration? What does GitHub do? They don\'t explicitly say duration of user log, Donald only sees back to May 7th\.... May be the past 50 events

  - [Simply Secure](https://simplysecure.org/) might have some good resources on this

  - **TODO**: look into prior art/best practices \-- [https://github.com/pypa/warehouse/issues/3532](https://github.com/pypa/warehouse/issues/3532)

Will: what about API tokens? question of security boundary. Maintainer seeing whether an Owner has created an API token

General discussion:

- what about main/owners wondering \"whose token was used for that release just now?\"
- Surface what user published a release - maybe not auth method?
- Does this user have 2fa on or not? yes, that\'s important for transparency.
- even if we add a 2-factor flow for upload API, does it matter how a user is authenticating? But: in case of a compromise, might be useful for someone to know \"my token was compromised\" \-- to know what to revoke

### Scope of this task 

Will: scoping questions: Trail of Bits is scoped to work on (as mentioned in [https://github.com/pypa/warehouse/issues/5863#issue-445032729](https://github.com/pypa/warehouse/issues/5863#issue-445032729) ):

- Add auditing for user actions in PyPI
- Add auditing for project actions in PyPI
- Implement a User view for User auditing, allowing publishers to track all actions taken by third party services on their behalf
- Implement a Project view for Project auditing for project maintainers to audit actions similarly
- Implement an Admin view for PyPI.org administrators to audit actions similarly

Some of this is fuzzy.

Ernest: implementing necessary API calls internally is most important for scope, then implementing a handful of auditable events, creating admin view for it, exposing what makes sense TODAY. And storage. Simplest case:

- recent logins
- changed? events
- 2FA

Project aspect: enhancing current view when logging into project history

Right now: ensure we can store and retrieve. We can add more auditable events down the line.

Donald: ideally only a few lines of code to add a new event type

Will: yes - event tag, and optional things (user, project) - human-readable description, assoc metadata

Nicole: re duration of storage:

- exposing events as part of project history - how long?

Will: store project-related events indefinitely.

User events: a limit.

Will: garbage collection, recycle in databases\.... how does he make sure events get properly flushed?

Donald:

- db itself just builds up indefinitely. Whatever you cap, need datetime stamp\.... you\'ll have a cronjob basically that issues a DELETE

- we use celery for background tasks for handling that

- a good example: email table & associated jobs for clearing that out

- a potential way to hide that it\'s periodic: build filtering into queries. Have query that pulls into data for User page also filter for 2 weeks. so data isn\'t dependent on when last cron ran

Sumana: Email notifications like [https://github.com/pypa/warehouse/issues/5808](https://github.com/pypa/warehouse/issues/5808) are out of scope

Ernest:

- we may want a responder built into API \.... queue into tasks \... callback on event? a way to do some action when an event is published \.... but not in scope

Donald:

- built into SQLAlchemy, can use event hook. what we use already for purging

Ernest:

- we need 2 separate models, not 1 hardcoded event list. 1 for project things, 1 for user things

Re: who gets to see what?

- for the public as a whole: for project events, we may want to show events but hide some info about each event, e.g. IP. Nicole is taking note of this for designing templates.

### Estimated date of completion for audit logging functionality 

Will: estimate: can have additional models and views done by probably end of next week. Then, work with Nicole on UI and - for initial merge - determining initial events to expose

Nicole: then another week or so to have templates merged.

*Resolved:* Try to work towards merging on Aug 16

(But let\'s not be surprised if getting out of beta on [WebAuthn](./WebAuthn.html) and API keys ends up slowing this down)

### Miscellaneous 

Ernest: **\*\*Important\*\*** INVOICES 4 JULY PLZZZZZZZ \<3 **\*\*Important\*\***: We need to update our view on runway ![:)](/wiki/europython/img/smile.png%20":)")

### TODOs 

1.  Will, Nicole, and Sumana: submit July invoices ASAP

2.  Nicole: look into best practices/prior art for how long to store user behavior in this audit log \-- [https://github.com/pypa/warehouse/issues/3532](https://github.com/pypa/warehouse/issues/3532)
