# PackagingWG/2020-07-01-pip-teamwidemeeting

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

**Teamwide meeting**

(These notes have been edited for clarity.)

1 July 2020

- status and blockers
  - Pradyun: figuring out what to do next

  - Bernard: no real blockers - is reading correspondence

  - Nicole: no blockers \-- hopes to get a final review on documentation PR. Nicole also doing work on #8436 & #8492 \-- users finding out where dependency conflict has occurred. Hopes to work on this with Pradyun.

    - Bernard & Nicole working on research plan for Phase III

  - Georgia: no blockers/needs at the moment.

  - Sumana: flag stuff has unblocked docs work for me (beta testing stuff)

  - Ernest: we need more community communication
    - Ernest/Sumana writing sprint for a \"mid year update\"
    - TODO: Sumana set up invite for Friday 10am \-- DONE
    - Georgia can help with editing/feedback after
- new resolver enable/disable flag
  - [https://github.com/pypa/pip/issues/8371](https://github.com/pypa/pip/issues/8371) & [https://python.zulipchat.com/#narrow/stream/218659-pip-development/topic/UX.3A.20What.20flag.20will.20users.20use.20to.20call.20the.20new.20resolver.3F.20%28.23.2E.2E.2E/near/202548182](https://python.zulipchat.com/#narrow/stream/218659-pip-development/topic/UX.3A.20What.20flag.20will.20users.20use.20to.20call.20the.20new.20resolver.3F.20%28.23.2E.2E.2E/near/202548182)

  - TBD: naming + timeline of removal of \--unstable-feature

  - Nicole notes: by using a flag, you are enabling something. the state of the resolver is changing. Nicole suggests: \"user new feature = 2020 resolver\" & \"\.... legacy resolver\"

  - \"\--use-feature and \--use-deprecated be a reasonable middle ground between length and explicitness?\"

  - TODO: Nicole to add this decision to GitHub issue

  - TODO: Nicole to add documentation of \"here\'s how we do release flags\" to developer docs. 
    - Suggestion: probably in [https://pip.pypa.io/en/latest/development/release-process/](https://pip.pypa.io/en/latest/development/release-process/) ? (next to deprecation policy)

    - Pradyun: when we add developer docs???? about release flags, belongs near deprecation policy

  - how long will it take to implement the code change re \--unstable feature?
    - Pradyun: maybe 2-3 hours of work, once I know whether we are removing unstable feature now or later
      - including writing and testing
      - TP to review it
    - Nicole: happy to remove it now. Per Zulip: we would do step 1 now - replace unstablefeature with usefeature=2020 resolver

  - So this will all be ready and done within the next few days

  - We also need to notify the community.
    - Sumana: thinking about that. I think the general community expectation for \"unstable\" feature is that it may go away and that they\'ll get less notification. glad that we\'re sorting things out around rollout / features / expections.
    - I think the change docs that I\'ll be writing (how to test, how to migrate) \-- that\'s where that will go.
    - Q: what level of pro-active communication should we be doing about this flag change?
      - distutils-sig? pypi-announce? other forms of proactive communication?
      - thinking of communicating this along with the beta.
      - Bernard: to answer: have we had \"high level of usage\" of the new resolver? If yes then we should communicate it more widely.
        - TP thinks usage is quite low, based on what he hears from his local community + GitHub issues. People say they will use it when it is ready

        - Pradyun agrees: Expect usage to spike once beta & publicity push happens. So this deserves a sentence in release notes. Changed flag name
      - Nicole: with beta would be fine.
      - TODO: Bernard should update his \"use the new resolver\" blog post
      - and anywhere else that we have it documented
      - Bernard: I agree w/ Nicole\'s comment \-- will change blog post.
      - Georgia mentions: I\'m wondering how this overlaps with the write up that you and Ernest are working as well?
        - Sumana: it might come up
        - in writeup, maybe expand on decisionmaking
- beta? and timing of release
  - [https://github.com/pypa/pip/issues/8206](https://github.com/pypa/pip/issues/8206) says \"early July\" now

  - Either:
    - 1\. make an early July beta release, get feedback from it, and then do a late July release of 20.2

    - 2\. don\'t release a beta **this month**, put out a regular July release that DOES NOT default to the new resolver (but has it available via a flag), and then make a beta in early September that defaults to the new resolver, proceed to an October release that does default to new resolver

  - Pradyun: both are good options. 1st is a bit easier in terms of flags and informing people

  - Nicole: prefer the second which gives us more time for user testing

  - Pradyun: we have a explicitly documented relesaes policy saying we can do a beta [https://pip.pypa.io/en/stable/development/release-process/](https://pip.pypa.io/en/stable/development/release-process/) . this fits with that. Also lets us use that with other pip stuff\... the setup.py change that ? wants to make? both are good, but have a slight preference for approach 1 \.... more used to in terms of prcess.

    - [https://github.com/pypa/pip/issues/7628](https://github.com/pypa/pip/issues/7628) Pradyun mentioned wanting long beta cycles

      - but: we have good capacity to do a communication push around this beta, and we\'ve advertised it in general that we will do this.

  - Bernard: would prefer 2nd option \.... in practice, how would we test the new resolver with users? the user running the new resolver?
    - Scenario: Nicole and B look for people to test the new resolver with. We recruit \~10 people. How would they run the new resolver?
      - In both cases, it\'s behind a flag in the new release (in July).
      - The new resolver is included in the July release, just behind a flag

  - Pradyun: need to check if there\'s anything else in pip master/planned to be merged, that would be a reason to have a beta (I\'m not sure \-- will look!)

  - Georgia:
    - Sumana: won\'t have a communication push about the PSF write-up on \"project status / accountability writeup\".
    - We\'ll have a test this stuff push, for the main release, that is something that\'s gonna get a big announcement / publicity push.
    - So, I feel like if we want to do a beta for the new resolver, before it is made the default, that feels like either we have a beta cycle of 3-4 weeks or we wait quite some time when we have a bunch more bug-fixes, and we have more testing time, and then put the word out.
    - delays due to unforeseen circumstances

  - In option 1, is new resolver the default, or is it behind a flag, in July release?
    - Pradyun: still behind a flag, is what I would prefer.

  - Nicole: #8346 and #8492 \-- would be nice if we could get those done before we make resovler the default.

  - [https://github.com/pypa/pip/issues/8346](https://github.com/pypa/pip/issues/8346) & [https://github.com/pypa/pip/issues/8492](https://github.com/pypa/pip/issues/8492)

  - Bernard: if, in both situations, resolver is behind a flag, what is the difference to the user?

  - TP: only when it is released where the new resolver is on by default will the bulk of people use it. And I would be comfortable with us releasing it on by default in 20.2 without a preexisting beta.

  - Bernard & Nicole need time to get users, test things, and then implement changes after\.....

  - Bernard: in the early discussions, became clear, reluctance to break things for people in CI/automated usage. So, since this is a big change, if I were an engineer, and an upgrade of pip broke some things, without reading ? log & seeing official communications, I\'d be saying \"??!!\". So I would prefer to have more time\...

    - Nicole: one thing in the feature flag sys we agreed on: from step 1 of rollout, \"pip install x\" will use old resolver, and we will raise a warning if we can detect cases where old and new resolver would behave differently.  Look out, new one is coming soon. The longer we can have the warning message out ther for userss, the better. +1 from Bernard

  - Sumana: if there are refinements to the options, lets here them. Her refinement:
    - Release a beta **without** pushing/headlining stuff about the new resolver - before the 20.2 pip release

    - Spead the word wide that March release had new resolver alpha and the July has a resolver beta. Here\'s how to use it.

    - Make a big communication push around late July pip release of 20.2.

    - Plan to release pip 20.3 in October with the new resolver turned on by default.

    - Bernard: in that time (late July, August, September):
      - Testing can be done (with, and independent of the UX team)

  - Most people feel safer having the new resolver behind a flag (TP\'s POV noted).

  - Pradyun: Agree\'s with Sumana\'s refinement. Once July is out, we can still make releases, and accomodate for those in the testing instructions. The usability testing would continue with the \*newest\* release.

  - Pradyun: I was thinking that, plus once the July release is out, we can still make prereleases of 20.3, which could iterate on bug reports from beta resolver, and in the testing instructions we would say, install the latest pip regardless of whether it is a prerelease. 

  - Nicole: fine with me

  - Bernard: I think I understand & I think it makes sense. New resoover alpha was releasesd in March, new resolver beta to be released in July, that allows UX people to get testing done with users, get feedback, in period of time we can then feed back testing results from our testing, users who are not testing via Simply Secure can file GitHub issues, feed back to team, and during that period, developers are making improvements all the while.
- invoices
  - Sooner the better
  - Finished up MOSS money
  - Need to know what we can shift in CZI budget
- changing meeting rhythm now that we have fewer people?
  - Fewer restraints re: timing/schedule. Sumana will send out invitation/note via Bethany
