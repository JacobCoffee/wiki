# PackagingWG/2018-04-17-Warehouse

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

## Warehouse core developers\' weekly meeting 

Tuesday, 17 April 2018 \-- postponed from Monday, April 16th because of launch hiccups

### Present 

- Nicole
- Mark
- Dustin
- Ernest
- Sumana

absent: Laura, Donald

### Blockers 

[https://github.com/pypa/warehouse/milestone/7](https://github.com/pypa/warehouse/milestone/7) is the 3 issues between us and legacy PyPI shutdown. No blockers outside of that, and (per Ernest) waiting for JFrog to [figure their stuff out](https://github.com/pypa/warehouse/issues/3275).

### Availability between now and May 9th 

- Sumana is trying to reduce PyPI time to ramp up on another client

- Nicole not available between 1-4 May

- Ernest: Just sticking to Tuesdayish Thursdayish until billable time is exhausted (that\'s 20hours by my math). (will always be around on volunteer basis).

- Mark & Dustin: no change

TODO: After call: Mark & Sumana to work on spreadsheet

### Future grants/fellowships \-- heads-up 

Current grant proposals:

- Facebook: nothing yet
- NLNet: nothing yet
- OTF - have till 26th to reply to OTF on concept note questions: Mark is working on it \-- please post to mailing list (Packaging WG) \-- TODO

Future possibilities:

- [https://open.segment.com/fellowship](https://open.segment.com/fellowship) \-- sign up for notification for when it opens if you want to spend all your time on FLOSSy things

- [https://www.opensocietyfoundations.org/grants/open-society-fellowship](https://www.opensocietyfoundations.org/grants/open-society-fellowship) \[unlikely, but on the table\]

- OTF Red Team audit \-- Sumana should submit - TODO

- [https://www.mozilla.org/en-US/grants/](https://www.mozilla.org/en-US/grants/) asking Mozilla for non-MOSS grants - Sumana TODO

### Talking publicly about money 

May Sumana publicly talk about the project wrapup (basically, mid-May) & what we could do with more money?

RESOLVED: Sumana to work on this today TODO

### PRs to review 

- Trove classifier tree [https://github.com/pypa/warehouse/pull/3273](https://github.com/pypa/warehouse/pull/3273*)

- Show \"more\" button on homepage [https://github.com/pypa/warehouse/pull/3424](https://github.com/pypa/warehouse/pull/3424*)

- update last released timestamp to visually connect it more to the latest version box [https://github.com/pypa/warehouse/pull/3481](https://github.com/pypa/warehouse/pull/3481)

Resolution: Nicole to look at all these, this week ![:)](/wiki/europython/img/smile.png%20":)") TODO

### Bug triage 

[https://github.com/pypa/warehouse/issues/3463](https://github.com/pypa/warehouse/issues/3463) give user option to see more search results in pagination

- could we ask RazerM & Honza Kral for help with this?

  - Res: Dustin to ping them in issue TODO

[https://github.com/pypa/warehouse/issues/3532](https://github.com/pypa/warehouse/issues/3532) retention policy

- Who will summarize VanL\'s reply in this issue?
  - TODO: ask Donald

[https://github.com/pypa/warehouse/issues/3632](https://github.com/pypa/warehouse/issues/3632) get \~all users to verify email addresses

- what do we need to do in the next \~3 weeks to make a PyCon publicity push useful?

  - Dustin says \-- we\'ve already added a banner\..... at some point, not today, make it not possible to upload new release unless you have a verified email address. That will catch almost everyone who has an unverified email address that we might email.
  - Ernest: we had excellent results when we asked people to verify before releasing a new pkg. a little confusion, no grouchiness.
  - might want to go back, summarize how those responses went in issues, improve messaging. Then disable uploads without verifying as next step. Then, next step \-- upon login, the only thing you can do in UI is verify
  - When to flip switches?
  - RESOLUTION: NONE; SUMANA TO COMMENT ON ISSUE TODO

[https://github.com/pypa/warehouse/issues/3689](https://github.com/pypa/warehouse/issues/3689) Make StatusPage issues more visible

- could we put a \"help wanted\" label on this?
  - Resolution: YES, use their public APIs. Sumana to ask. TODO

[https://github.com/pypa/warehouse/issues/3733](https://github.com/pypa/warehouse/issues/3733) valid email address deemed invalid

- need to fix by 30th? no, not very urgent
- Resolution: TODO DI to comment on issue
  - seems like an underlying issue with one of our dependencies

### Encourage volunteers 

Users who have made PRs we\'ve merged since \~November. Whom should we particularly ask to step up & remember to ping on open issues? \[conversation continuing elsewhere\]

### TODOs 

- All of us: reply to Mark\'s email re: answering OTF\'s questions
- Sumana:
  - Submit request for OTF Red Team audit

  - Ask Mozilla about further funding

  - Give Betsy, Mark, rest of community our thoughts on what we could do with more money

  - Comment on [https://github.com/pypa/warehouse/issues/3632](https://github.com/pypa/warehouse/issues/3632)

  - Ask for help on [https://github.com/pypa/warehouse/issues/3689](https://github.com/pypa/warehouse/issues/3689)
- Dustin:
  - Ping RazerM and Honza Kral in [https://github.com/pypa/warehouse/issues/3463](https://github.com/pypa/warehouse/issues/3463)

  - Comment on [https://github.com/pypa/warehouse/issues/3733](https://github.com/pypa/warehouse/issues/3733)
- Nicole:
  - Review outstanding design/frontend PRs
- Donald:
  - Update GDPR issue with VanL\'s reply
