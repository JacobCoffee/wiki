# PackagingWG/2020-12-23-pip-team-meeting

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

Wednesday 23 Dec 2020

Participants:

- Pradyun
- Sumana
- Ee
- Bernard
- Georgia

Agenda

- Assumption: next week, no meetings.

- Invoices & Pradyun\'s work

  - TODO: Sumana to send note to Accounting

- UX team
  - documentation going into hub
    - we\'re reworking outline and finding everything a home. Doable by the end of the year we hope. Written; we just need to compile.
  - raw data from surveys
    - from Zulip: Georgia said:
      - I was just chatting with one of our team members about the synthesis we\'re pulling together and we had the interesting idea of sharing as much of the raw survey data as feels reasonable (e.g. if folks in the community wanted to dig in, they could!).
      - Questions for you all:
        - Does this seem like a good idea?

        - Is there a home or location that might make the most sense for housing csvs of data? (initial thoughts are a GitHub repo, or a Drive folder or another file share location)

        - Any concerns that this raises for you?
    - No canonical place for this sort of thing
    - Sumana: I will suggest that a directory within the github.com/pypa/packaging-problems repo feels like the best fit
    - Why not Google Drive for PSF?
      - confusion over which user account manages it, provenance

      - even anonymized-as-much-as-possible survey data on GitHub (public)\.....doesn\'t feel as right as if it\'s in a fileshare owned by a UX research role owned by PSF

        - using GitHub is not an antipattern in general

        - knowledge management in general
  - UX training
    - planning \[per yesterday\'s call\] is proceeding. Probably going forward with one next week, Tues the 29th. Basically cannot make a pilot happen before then.
  - mailing list consolidation and handover
    - main question: other mailing lists are hosted on a Mailman instance, right? we would just need \..... makes sense to have mailing lists live there\...
    - right now we have a list of email addresses. idea is to house it somewhere, for future work. Existing research panel of people who said \"contact me about UX research and studies\"
      - Ee: needs list of email addresses and who would be owner. Optimally 2 people who would be owners of the list
        - TODO: Georgia to hand email addresses and names of 2 owners to Ee
      - Georgia is happy to act as the owner as\..... to help with future UX people who want to do work. Helpful handoff person.
      - Data we have: semi-identifiable info: 100% email, maybe 50% names/nicknames. Maybe other things like Twitter handles
      - TODO: check the unsubscribe list.
        - Bernard: has been unsubbing people \-- a separate table of people, already been removed from my part of it
        - TODO: confirm this.
      - TODO: Simply Secure to look at metadata to pass along in case it has stuff like \"novice vs expert\"
        - concern: maintaining in concert with a mailing list \[unsubbing from both\]
        - concern: we have generally separated this from IDs for privacy purposes

- Planning for 21.0 and removing deprecated legacy resolver
  - PG: I think we should keep legacy resolver in 21.0, remove in 21.1
    - need to get consensus from other pip maintainers
      - is there are RM for 21.0? not yet
        - TODO: Pradyun to figure out who RM for 21.0 is \..... get consensus from the other maintainers re: legacy resolver staying in, in 21.0
          - After that: gotta update documentation
  - I imagine 21.0 will come out early January

- THANK YOU EVERYONE! GREAT JOB THIS YEAR!
