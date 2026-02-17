# PackagingWG/2018-03-06-Warehouse

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# Warehouse Sync-up Meeting 

Tuesday, March 6th

## Present 

- Mark
- Nicole
- Dustin
- Ernest
- Sumana
- (partially) Donald

## Just finished/working on/blockers/announcements/vacations 

Mark

- Ewa and Mark reviewing PEP 541 (Wednesday, March 7th), going over workflow and roles.
- Budget updates: have sent and approved invoices for February.
- opentech.fund application completed, will follow up on Friday, March 9th on application status.
- Need to schedule one on one with Ernest on Warehouse Infra.

Nicole

- User testing \\o/

- each one takes 30-60 min, has 3 more lined up

- got a lot of feedback, opening some new issues

- need to respond to issues where she has been pinged

- unavailable some of last week of March, incl Monday March 26 - (25th-29th to be precise ![:)](/wiki/europython/img/smile.png ":)") )

Dustin

- Updates/migrations/packaging for version canonicalization
- Password strength gauge merge
- Debugging camo issues - https proxy for embedded images
- no big blockers, except needing Donald review
- unavailable some/all of last week of March

Ernest

- AWS Infra is stood up and heavily tested from a \"nuts and bolts\" perspecitve

- dicing out the millions of tiny differences between minikube, google kubernetes, and \"tectonic\" (our Kubernetes infra tooling)

- This week has been rough. [PyCon](./PyCon.html) CoC trainings, [PyCon](./PyCon.html) Schedule launch :/ but making steady progress.

- Disconnected April 1-7 \'cept for emergencies

Sumana

- bug triage, documentation

- ran IRC meetings & doing \"please test\" outreach

- volunteer: twine

- submitting talk to [JupyterCon](./JupyterCon.html) today [https://conferences.oreilly.com/jupyter/jup-ny/public/cfp/621](https://conferences.oreilly.com/jupyter/jup-ny/public/cfp/621)

Laura (absent, sick)

- PR re avatar/name display

## Grant money update & burn rate 

\~2 months left?

- we came in a little less in Feb vs Jan
- we\'ll run probably right about 2 months

What can we get done by the end of April?

- Dustin: get infra up & some traffic over, not all of it

- Ernest: positive: once we have infra up, can cut traffic over. Less concerned about turning off legacy - is positive we will hit that by end of April

- Nicole: a lot of nice to haves in there, could safely recategorize

- TODO Sumana to recategorize

When will we hear back on Open Tech Fund grant? - March 9

## PyCon sprint planning 

Sumana, Dustin, and (partially) Ernest to be there, but Nicole won\'t

- Ernest - don\'t count on his participation

Activities we could pre-plan/announce now:

- API keys? Luke Sneeringer? [https://github.com/pypa/warehouse/issues/994](https://github.com/pypa/warehouse/issues/994)

- Bus factor promo? [https://github.com/pypa/warehouse/issues/3121](https://github.com/pypa/warehouse/issues/3121)

Should we estimate what it will cost for us to be \"working\" at the sprints?

- Sumana to do this and talk with Ewa and Mark

- share info with Nicole re [EuroPython](./EuroPython.html)

- Should we apply for a sprint grant? (Do sprint grants even exist?)

## Milestone update (infra and features) 

Milestone 3 (publicizing the beta): [https://github.com/pypa/warehouse/milestone/10](https://github.com/pypa/warehouse/milestone/10) and Milestone 4 (redirect & launch): [https://github.com/pypa/warehouse/milestone/1](https://github.com/pypa/warehouse/milestone/1)

- relatedly: infra credits announcements? when?

- Mark is waiting for marketing stuff - Donald to poke Trevor

- Sumana to look through this & recategorize stuff that can wait

## Ask Donald for 

- review [https://github.com/pypa/warehouse-camo/pull/1](https://github.com/pypa/warehouse-camo/pull/1) Switch to fork with content length redirect

- review/merge/release [https://github.com/pypa/readme_renderer/pull/65](https://github.com/pypa/readme_renderer/pull/65) Handle invalid address errors

- Sumana timing re visit

heads-up, Thursdays and Fridays are now his packaging days, rather than Tuesdays and Wednesdays

## Bug triage 

Anything from [https://github.com/pypa/warehouse/issues/2976](https://github.com/pypa/warehouse/issues/2976) or [https://github.com/pypa/warehouse/issues/2982](https://github.com/pypa/warehouse/issues/2982) for spam cleanup , like bulk delete from a supplied package name list, that we need to plan around?

- Sumana\'s double-checking here, knows this is not strictly MOSS work

- [https://github.com/pypa/warehouse/pull/2969](https://github.com/pypa/warehouse/pull/2969) and [https://github.com/pypa/warehouse/pull/2991](https://github.com/pypa/warehouse/pull/2991) are still open

- No, not now

- no action needed

Frontend tests per [https://github.com/pypa/warehouse/issues/2154](https://github.com/pypa/warehouse/issues/2154) , and cross-browser test UI per [https://github.com/pypa/warehouse/issues/1317](https://github.com/pypa/warehouse/issues/1317) ?

- Sumana: fine to postpone. Your thoughts?

- lack of tests is not slowing Nicole down

- Nicole has access to [BrowserStack](./BrowserStack.html) - testing is easy - the problems that we find via it are the things that take time

- Analytics from last month (Feb 2018): Chrome 67.76%, Firefox 16.92%, Safari 7.38%, Internet Explorer 2.79%. Site has been built using Chrome - I don\'t foresee too many problems ![:)](/wiki/europython/img/smile.png ":)")

- Testing the Stimulus controller(s) seems more feasible

Move Conveyor back to using test.pypi.org [https://github.com/pypa/warehouse/issues/1211](https://github.com/pypa/warehouse/issues/1211)

- Sumana: ok to postpone past shutdown?
- Dustin can do this if he can get access to the conveyor heroku app
- should deploy to cabotage on Thursday

## TODOs 

- Donald to do stuff in \"ask Donald for\" section, and to check with Trevor about credits and marketing
- Mark to follow up on 541, Ernest conversation re: infra, Open Tech Fund grant, other grant opportunities
- Sumana to recategorize less-essential Milestone 3, 4, and 5 issues (in progress), and talk with Ewa and Mark about sprint budget
- Nicole to reply to issues where she\'s been pinged
- Ernest to follow up on #1211
