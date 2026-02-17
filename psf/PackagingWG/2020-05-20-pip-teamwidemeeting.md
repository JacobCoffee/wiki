# PackagingWG/2020-05-20-pip-teamwidemeeting

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

Teamwide meeting, May 20th

Participants

- Nicole
- Bernard
- Ernest
- Sumana
- Paul
- Tzu-Ping
- Pradyun
- Georgia

TODO:

- TODO: Sumana: follow up on this\.... publicize wider.
- TODO: DECIDED: Tues the 26th: shared day off where we will try to neither look at nor respond to work communications \-- DONE
- TODO: Sumana: work on some recurring \"no noise\" team time, no notifications. would be very beneficial
- TODO: Sumana: Are we ok to go to the Python community to ask \"what if we had specific telemetry on package dependency conflicts?\"
- TODO: let\'s do this in May, Paul to do this tomorrow or Friday: 20.2b1 \-- DONE

Agenda

- blockers/status
  - Paul: fine! not blocked on anything
  - Nicole: doing well! \[redacted\] now in the swing of things. Onboarding was a little difficult even given previous packaging knowledge. Working 10 hrs/week, Monday-Tues-Wed.
  - Ernest: doing well! would be good to have more public reporting on things in general. \[vacation plans\]
  - TP: good. not blocked.
  - Sumana: ok \[redacted\]
  - Bernard: ok. doing good. blockers: lack of bite on research about resolution too deep/resolution impossible.
    - TODO: Sumana: follow up on this\.... publicize wider.

    - In meantime: been doing other pip work, collab with Pradyun yesterday, discussing with Paul on current pip behavior (see Zulip, recent GitHub ticket)
  - Pradyun: doing well. busy in coming weeks. \[redacted, personal\] new blocker: on May 27th, Pradyun has to present a final semester internship (this) to his college. They need a 30+ page report by May 25th, but ideally tomorrow. So needs to grind on that!! Wishes he had kept up on monthly blog posts.
    - Georgia is always happy to read and respond to stuff
    - TP can be a beta reader
    - Paul is happy to be a beta reader - ping on Zulip anytime
  - Georgia: doing pretty well. \[redacted\]

- shared day off \[discussion redacted; was decided to be Tuesday 26th\]

- UX outputs
  - (Temp Draft Doc in Notion): \[redacted URL\]

  - different sub-items (see Notion)
    - Key question: whether the documentation work is in scope
      - \"This work possibly sits within wider scope of making the ecosystem around pip better. Georgia needs to look at budget / resources to confirm how far we can contribute to this idea.\"
        - Sumana: [Pip2020DonorFundedRoadmap](Pip2020DonorFundedRoadmap) \-- let\'s look at this as we embark on Phase III!

    - The pip team has no understanding of when and why the pip resolver fails (`ResolutionImpossible`{.backtick} and `ResolutionTooDeep`{.backtick} exceptions). This makes it very hard to provide useful contextual information to help the user resolve their problem(s).

      - Something needs to do the work of figuring out which contextual info to provide to the user\... could we gather metrics on failed conflict resolution in order for pip to better understand what package combos work well/don\'t? This would all assume that these metrics were gathered consensually, transparently, etc.
        - TODO: Sumana: Are we ok to go to the Python community to ask \"what if we had specific telemetry on package dependency conflicts?\"

    - The language of the some of pip\'s command implies it will do one thing, and it does another. e.g. [https://github.com/pypa/pip/issues/8238](https://github.com/pypa/pip/issues/8238)

      - Started with Paul\'s Zulip conversation. Related to \--force-reinstall more specifically, not so much a wider issue. Can discuss in that issue.
        - Paul: only spills out a little.

    - Looking at UX for the rest of the resolver.
      - Need to rationalize a lot of stuff in the output. Nicole has begun auditing all of the output that\'s currently shown to user. Comparing to pipenv and poetry, to improve overall UX

  - Question: prioritization & timeline: resolver/resolutiontoodeep/etc stuff is most crucial

    - Bernard & Nicole are trying to collect data. Make recommendations based on initial data, then be ready to revisit based on later/more data

      - We haven\'t yet had a proper publicity push for data on resolution issues
      - What we\'ve done has been limited in scope
      - Also, make it clear that there\'s a deadline for data to be collected, to push people to reply
      - Target in terms of (a range of) number of responses

    - Bernard: Zero responses so far. Sumana: What is a good number? Bernard: picking a number out of the air, 100.

    - Sumana: A range that would give us enough data to draw conclusions - order opf magnitude 100.

    - Georgia: Going off general UX guidance, we can see patterns off any number of responses, we can see patterns in fewer than 100, but could introduce bias because we on;y get certain types of response. \>50 good, 100 would be definitely able to see patterns

      - call for help: [http://www.ei8fdb.org/thoughts/2020/05/test-pips-alpha-resolver-and-help-us-document-dependency-conflicts/](http://www.ei8fdb.org/thoughts/2020/05/test-pips-alpha-resolver-and-help-us-document-dependency-conflicts/)

    - next to prioritize: audit output/error message of the rest of the resolver \-- Nicole has started a spreadsheet, will need dev time to go through that
      - Nicole to sync with Paul or Tzu-Ping

    - and then after that: figuring out \"language of a command says it does 1 thing, but it does another\" (\--force-reinstall)
      - yeah - look at output first. Audit will help us figure stuff out.

  - As we interview users - this will go into that

  - will be helpful to UX folks: have a clearer week-by-week timeline for things. deadlines. More clarity would be helpful. Release planning.
    - Sumana: agreed

- release beta this month? [https://github.com/pypa/pip/issues/8206](https://github.com/pypa/pip/issues/8206)

  - Sumana: let\'s not do this. Maybe June
    - Paul: good
    - Pradyun: good
    - TP: we talked about releasing another alpha
      - TODO: let\'s do this in May, Paul to do this tomorrow or Friday: 20.2b1 \-- DONE

- `ResolutionTooDeep`{.backtick} \-- how about an alternative strategy of \"remove the error raising logic, and see who complains about the resolution taking too long\"

  - Tzu-Ping filed a PR while we were talking. LOL

  - [https://github.com/pypa/pip/pull/8275](https://github.com/pypa/pip/pull/8275)

    - sure, let\'s ship this in the alpha. \"and tell us if things are taking too long\"
    - This also lets us unblock a lot of people who were trying to install 100+ packages in one go, e.g. with a big requirements.txt (pip would stop them from trying)
    - Next: merge PR, then Paul to release an alpha, this week, Thurs or Fri. As 20.2b1.

Pradyun:

- might be useful to talk with Donald re metrics/telemetry on PyPI/pip
- Paul, if you hit errors in release automation, Pradyun will be around, ping him on Zulip
  - Paul asks about docs about where to announce stuff
    - TODO: Sumana to add those to docs
