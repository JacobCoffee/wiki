# PackagingWG/2020-07-22-pip-teamwidemeeting

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

Team Meeting: Wednesday 22 July

Attendees

- Nicole
- Bernard
- Georgia
- Sumana
- Ernest
- Pradyun

Agenda

- Status/blockers
  - Nicole - research plan for pip functionality. now done with docs research plan. Need review of pip search survey from Georgia and Bernard. Standardizing further followup call to action
    - survey: [https://docs.google.com/forms/d/1-4kiVV8NnlkBrCr6x7eb8SobnS1RVRAR2xEl8iUeu24/edit](https://docs.google.com/forms/d/1-4kiVV8NnlkBrCr6x7eb8SobnS1RVRAR2xEl8iUeu24/edit)

  - Bernard - working on pip in package manager ecosystem research plan. Looking at #8594 (#8546?) which is a blocker for Pradyun at the moment.

  - Georgia - will look at the pip search survey, working w/ b&n to put the research plans on a calendar

  - Pradyun - Circling back to 20.2. Looks like a few PRs that need to be reviewed and merged. Need UX input from #8594, and need a changelog/release notes support from Sumana.
    - Many minutes after this call - Pradyun and Sumana to talk

  - Ernest - nothing to add.

  - Sumana - No blockers at the moment. Want to support the July release and ready to do the reviews that people need of me.

- July release blockers
  - [https://github.com/pypa/pip/pull/8594](https://github.com/pypa/pip/pull/8594) (PR) ([https://github.com/pypa/pip/issues/8546](https://github.com/pypa/pip/issues/8546)) \-- need UX inputs/go-ahead? Bernard is on it! Will ping Nicole if needed.

  - [https://github.com/pypa/pip/milestone/36](https://github.com/pypa/pip/milestone/36)

  - Need changelog/release notes entry for the new resolver. (ideally, needs input from Sumana)

  - 2 PRs needed \-- updating vendored deps + removing a deprecated thing\... Pradyun is on it.

  - date: hope for release tomorrow. If not tomorrow, probably Monday to avoid Friday release

- UX Team Planning Updates - Draft Schedule ([https://www.notion.so/simplysecure/Draft-PIP-UX-Schedule-July-October-2020-a2d55ed05fa340728da75d139b24ab0b](https://www.notion.so/simplysecure/Draft-PIP-UX-Schedule-July-October-2020-a2d55ed05fa340728da75d139b24ab0b) )

  - Docs Feedback ideas
    - Sumana: Many of us are friends with the ReadTheDocs team --- maybe there should be a readthedocs feature that would help with this!

      - Maybe there\'s work that they could do and then we could inhereit
      - Nicole can follow up with Eric/ReadTheDocs Team

    - Maybe we should move the recruitment plan into July?
  - Questions for Sumana/Team
    - We\'re realizing that this scope is quite large for the time, and wondering if we should prioritize, and how to plan for other ad hoc support that may be needed
    - Are we still aiming for September/October wrap?
      - Technically CZI goes through December 2020, so we can re-work the flow of hours/time - Focus on End of November
      - TODO: Georgia check contract end dates
    - What other timing should we be aware of?
      - Release timing - October release will have the resolver by default

      - Testing pre & support for feedback on the new resolver as it switches to default in October

      - Planning around vacation/travel etc
        - Ernest out the first week of August
    - Telemetry research proposal idea --- do we want to pursue it? Under pip-ecosystem or is it out of scope?
      - Bernard: A concrete thing that we might be able to do is focusing on how telemetry is done in other package managers, e.g. pros/cons, their communities reactions, ideas gathered from other projects (e.g. groups like Tor Metrics)
        - GA: Simply Secure is actually working with Tor Metrics right now as well, so we have some insights from that data and community needs
      - Nicole: Agree that it\'d be nice if we could bundle it into the pip-ecosystem epic as well. Would the end output be a recommendations? Implementation ideas? etc?
      - Bernard: We wouldn\'t be able to recommend an implementation plan without input from the developers, so maybe instead it\'s more recommendations of the telemetry could look like
      - Nicole: also, we could share the community openness to telemetry
      - Sumana: Helpful to understand what the bits of work are --- what is possible, ethical, desired, outcomes we\'re actually seeking. This feels like an extremely important thing that I want to have happen, but maybe isn\'t in scope / possible in the time we have available
        - A good balance would be to avoid putting any specific deliverables for the telemetry, sometime at the end \*after\* the deliverable things \-- get a \"quick\" list to then make it possible to add funding on a follow up.
      - Pradyun: if we had more time, YES, this would be awesome \-- but I feel like we don\'t have enough time?
      - Georgia: Two ideas:
        - Georgia reach out to an academic who works in this area to see if someone is working on this already
          - SH: Tidelift or PyUp (and more)! Some of them work across ecosystems.

          - Georgia: CHAOSS and CleanInsights work from Guardian Project

        - UX Team ask some questions about this as part of the interviews, but not focus on an in-depth telemetry research question
          - \"get community feelings about this\"
          - SH: Right now, a desktop client sending info back to a server about stuff, eg: Crash Reporting on FF, OK because they don\'t care when they \[note taker could not follow along\]. If you are able to ask about telemetry, one of the ways is \"ongoing\" vs \"on-crash/significant-error\" telemetry.
          - Yay expertise! \\o/

        - Privacy preserving telemetry!

        - Georgia: Maybe we can align with other efforts that are going on in open source 

        - If this leads to a proposal in the future, Simply Secure can help work on this ![:)](/wiki/europython/img/smile.png%20":)")
    - If we wanted to explore the idea of creating a pip package for user research, how could that potentially happen?
      - Sumana: debian bug report CLI tool - reportbug
      - Bernard: debian popcon --- lightweight consent around collecting metrics
      - Sumana: It would need to make an API call to some service, what API does it call?
      - Georgia: The idea would be something that could be a tool in the toolkit for user feedback in an ongoing way
      - Sumana: this is something we could get volunteers to build if we have the bare architecture and policy details worked out. Leverage conference sprints.
        - What API does it call?
        - Where does the data go?
        - Who has access to it?
        - Add this idea as something to explore during August for the UX team
        - Georgia: could be a CLI tool to interact with user research surveys
