# PackagingWG/2020-11-23-pip-team-meeting

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

Tuesday 23 November Participants

- Nicole
- Bernard
- Sumana
- Ernest
- Georgia

Agenda

- status & blockers

  - Pradyun: can join tomorrow\'s meeting in its entirety
    - only 1 blocker, #9011. Not been able to wrap his head around why resolvelib is misbehaving. Stuck. Need to tag and work with TP.

    - also, would be nice to have if we could do it in time: Mac OS Big Sur changed things, including how Mac OS tags work. That then requires an update in `packaging`{.backtick} + pip. But it\'s ok to go without.

      - this will go in 20.3.1

  - Bernard: spoke with Sumana about expectations for UX training. Now: continuing with pip research analysis, reports.
    - would like the mental model review (spreadsheet). Would be really helpful if some people looked at it.
    - TODO: Pradyun will look today
    - wants to get training stuff ready, ideally to do work in December.
    - TODO: Bernard need to pick up again the interviews with people who run package managers
    - TODO: Sumana to nudge people

  - Nicole: interviews re doc: done 3-4, have more scheduled this week. Starting to get a picture on what we should do to improve pip\'s docs. Will be ale to make strong recommendations based on that!
    - continuing to summarise research finds we have
    - no blockers right now

  - Q from Pradyun: has nicole seen the Matomo PR/discussion? [https://github.com/pypa/pip/issues/8517#issuecomment-730373194](https://github.com/pypa/pip/issues/8517#issuecomment-730373194)

    - ? what is blocking it being merged?
      - consensus
      - is there a policy on PyPA/PSF stuff?
      - Ernest: no. We use Google Analytics\... respects Do Not Track cookie. If we need a policy, we should contact Legal and start that process
      - Georgia: we don\'t want to do something out of line with what PSF is doing
      - Ernest: comes down to where data is stored. per GDPR, we do not store really anything on any PSF property that is not critical to behavior of service. \[This means a lot of GDPR does not apply\] Here, user behavior, need to be more careful, since not critical to behavior of pip.
      - Google Analytics - storing user behavior \[more detailed question about storage\]
      - Ernest: for purposes of docs, we have used GA for other similar site properties
      - Pradyun: would be using the hosted version of matomo.org
      - Georgia: wondering whether to align with, well, PSF is the org here, so, use the analytics
      - Ernest: we\'ve had minimal pushback on python.org and pypa.org having GA
      - Ernest: hosted/free service would be rad
        - by precedent, GA would not be a problem at all. a free service that is an alternative that PyPA wants to use, that is fine as a reasonable alternative
      - TODO: Sumana to take a fresh look after call at Matomo discussion
      - Bernard wanted to ask: what questions are we trying to answer by adding analytics to docs? to minimise extra data being unnecessarily gathered.
        - Georgia: what sections of docs are being used.
        - Georgia: it would be a PSF conversation to possibly move over to Matomo from Google Analytics
        - it can be hard if different sub orgs do different things

- discussion of 20.3 release - deferred till tomorrow

- discussion of prepping for UX training - deferred till tomorrow
