# PackagingWG/2020-07-08-pip-teamwidemeeting

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

Team Meeting - Wednesday 8th July

Attendees:

- Ernest
- Nicole
- Pradyun
- Sumana
- Georgia, needs to drop off 5-10 minutes early
- Bernard

Agenda:

- Status/blockers
  - Pradyun: has everything needed to move forward on error messaging. working on some PRs. should wrap up resolver side of things for 20.2 release. then, 20.2 work for milestone-clearing.
    - can move on to stuff to do before prod

  - Bernard:
    - working this afternoon, then off in the morning European time \[private\] Still need to move documentation from HackMD & Notion (archiving). Got research ticket working on. No blockers.

      - on archiving: unblocked

  - Nicole:
    - no blockers. status: need to make a PR for feature flag docs. Need to look into research question we will discuss later. If I have time this week, look into [https://github.com/pypa/pip/issues/8492](https://github.com/pypa/pip/issues/8492)  to give user more info when they get ResolutionImpossible error. Would be nice to have that in by 20.2. But most importantly, don\'t make the new resolver default before this is sorted.

  - Ernest:
    - reviewing draft of mid-year writeup

  - Sumana:
    - mid-year writeup \[Etherpad link\] \-- note that we are probably about 10% under budget compared to where we thought we would be midyear
      - Pradyun & Georgia - review briefly today?

      - Georgia can do midday Eastern

      - Pradyun can review after meeting
    - I also need to finish test manual-style docs and start working on release blog post etc. for 20.2

  - General: [https://twitter.com/skamille/status/1280640072719761419](https://twitter.com/skamille/status/1280640072719761419)
- UX
  - UX research topics.
    - 4 \"epics\" identified:
      - Carry out research to understand who uses pip #8518 (Bernard leading) [https://github.com/pypa/pip/issues/8518](https://github.com/pypa/pip/issues/8518)

        - this is foundational to other questions \-- connected to the other parts
          - Pradyun: \*nods aggressively in agreement\*
        - Bernard: Paul has mentioned concrete example of a pip user \..... I want to ask him what he meant by that. in terms of research question \... I will follow up on Zulip.
        - How should we share info about this with the team?
          - the diversity in types of users of pip and what they use pip for \.... if creating personas are the best way \.... any thoughts on what you\'ve seen before, how you learn about users?
            - Georgia: a meta-discussion: how to do research & produce outputs that allow pip team to use them in an ongoing fashion. Tools you can use for decisionmaking, usercentric in an ongoing way. Would personas be useful? Any good examples from other projects that we wish pip had as ongoing resources? since we won\'t always have a donorfunded roadmap with UX resource.
          - Sumana: It\'s very likely that we\'d want this to be resources used across various tools \[pipenv, warehouse more!\]
          - Sumana: Also having that conversation on d.p.o. would give us a broader audience \-- more projects, and more experience.
          - We should ask about this on Discourse - would allow us to reach a wider group, including maintainers of other packaging tools
            - Can UX team please initiate? Bernard- yes. will open today or tomorrow
              - TODO: Thread on discuss.python.org!
              - Sumana: Please offer 2 wildly different examples and ideas to help ideas flow
                - Pradyun: Discourse is the right place, but conversations there will diverge and derail quickly, so it\'s good to have a specific wording to prevent derails
                - Georgia: makes sense. Let\'s draft something ahead of time and then have a more guided discussion. Like a survey but on Discourse. Some prompted questions.

            - Nicole: would it be worth opening up [https://github.com/pypa/pip/issues/8520](https://github.com/pypa/pip/issues/8520) - what do maintainers want to know about pip? on Discourse

              - Sumana: sounds good to me.
              - Pradyun: yes-ish but not 100% sure about mixing the channels \-- no need to be discussing on Discourse.:)
              - Georgia: related to the discussion about discussions on Discourse 
              - Sumana: a better way to go about this would be to ask the discourse mods to lock the thread immediately \-- we only use it on Discourse, only to use d.p.o. for signal boosting

      - Carry out research about pip documentation #8517 (Nicole leading) [https://github.com/pypa/pip/issues/8517](https://github.com/pypa/pip/issues/8517)

        - Nicole: had a chat with a PhD candidate who may be able to help with the documentation epic - user research, data analysis. Have reached out to Daniele Procida, Django core team member who works on docs, to check whether he can review docs plan
          - \\o/
        - Sumana: any open questions?
        - Nicole: not at this stage.

      - Carry out research to understand pip functionality #8516 (Nicole leading) [https://github.com/pypa/pip/issues/8516](https://github.com/pypa/pip/issues/8516)

      - Carry out research to understand pip in the package management ecosystem #8515 (Bernard leading) [https://github.com/pypa/pip/issues/8515](https://github.com/pypa/pip/issues/8515)

        - Q: pip compared to tools in other ecosystems? or pip compared to other tools in the \*Python\* ecosystem?

        - Bernard: both of those, yes \.... pip compared to other tools in Python \..... one interview I did, a professor, brought up several questions about defaults in Python packaging tools. Asking: why are the various different documentation, confg files, etc. not in the same place in all the diff packaging tools. So, also, compare pip to tools in other ecosystems. do other managers do things in a better way that pip can learn from/adopt? that\'s the beginning thoughts. open to other research questions people would like to know about. Looking from POV of users, not developers of a package mgr.

        - Sumana: So please answer #8520 (and flag it as GH ticket 8515 so Bernard knows it\'s specifically about package managers)

        - Bernard: yes, a fine place to put it
          - Pradyun: I\'m excited about this. \\o/
          - (Bernard: can we have a call about this Pradyun?)
          - (Pradyun: yes! when?)

        - Ernest: we field stuff about network connections to Warehouse. pip can get confused re corporate proxies, etc. \.... discussions have happened re network telemetry in the pip client to help troubleshooting
          - Ernest: there are a thousand exceptions tht can happen - TLS, DNS, certificates, timestamp \.... ultiimately problem: people get a traceback and not a message \"we tried to connect to Warehouse but we had invalid certificate\" - that would be a huge UX improvement. Could find GitHub issues where the issue was a corp proxy. Converting the \"Traceback\" into an error message \-- very hard

            - Is this a place for better error messaging in pip? \-- answered already. ![:)](/wiki/europython/img/smile.png ":)")

            - Possible research question: How do other package managers deal with network funkiness/proxies? (prior research might be network redirect/portal capture pages)

        - Sumana: suggestions for resources for the packaging ecosystems \-- talking to people / reading docs etc:
          - [https://manifest.fm/](https://manifest.fm/) \-- the Manifest Podcast, a podcast about package management tools.

          - [https://blog.tidelift.com/the-state-of-package-signing-across-package-managers](https://blog.tidelift.com/the-state-of-package-signing-across-package-managers) - click around tags to explore for information/discussions about other package managers

        - Beyond comparisms with other tools \-- look into ecology of interfaces \-- what does pip draw from & live with?

          - sources of information to pip? PyPI, bandersnatch, the specific packages too, and user-written things like requirements.txt as well.
          - Things to co-exist with: conda, system package managers
          - \.... other pieces of software pip needs to interact with, or where interference might happen
            - Bernard: would like to discuss more later on
            - Georgia: relates to #8518 defining who pip users are

      - [https://github.com/pypa/pip/issues/8520](https://github.com/pypa/pip/issues/8520) - what do maintainers want to know about pip? will integrate into answers to other 4

      - 

      - Sumana: timelines for these epics? Few months to develop questions and gather information on them?
        - Nicole: yes.
        - Georgia: UX team take the TODO to chunk the Epics into more fine-grained timelines (e.g. monthly goals) by next week.
        - Bernard: (frantically tries to find the mute button) yes.

      - Sumana: any other bits of the epic, that we could discuss in this call?
        - Question about personas, and how to perform / present the user research.
- \* \* Problem - we need confirmation from the team that this research will be useful/actionable:
  - please respond to [https://github.com/pypa/pip/issues/8520](https://github.com/pypa/pip/issues/8520)

    - Nicole: got a response from Pradyun and Paul on this.
      - TODO: Pradyun to drop an email to pip\'s maintainers.
      - TODO: Nicole to cross post to discourse
        - Reach out to the moderators \*before\* to ask them to lock the discussion on discuss.python.org

        - Need to unlock the GitHub issue before we post this!

  - Idea: Run pip team workshop to validate / discover research topics/questions
    - Nicole: \[planning, budgeting, scheduling\]

    - When would we need to do this?

    - We need to establish a list of research questions. Then, after that , we would need to do this sort of thing \... in the next few weeks

    - TODO: followup on Zulip & ask Paul for his thoughts as well

  - Idea: ask contributors to vote on research topics/questions
    - Bernard: some mechanism we can use to get the team/contributors\' inputs/preference on our research objectives and what we do in the plan.
      - Kinda related to the previous discussion about things contributors would like to know about users.

    - Sumana: wanna understand something better \-- might be terminology \-- we\'ve spoken about \"epics\", things that are high level topics. we haven\'t yet formulated our research objectives. what should I expect as the relationship between these epics and the research plans/topics? Are they topics themselves? What does \"research plan\" mean?
      - Bernard:
        - Research plan: is literally how we do it, when do we do it, what order do we do it in?
        - Research epic: like \"who uses pip\"
        - Research questions: the more specific, granular questions we try to find out about?
          - eg: How does a user with a disability use pip? (not the final wording, but the intent is to look into how \[too slow typer\]
          - eg: How diverse is the usage of pip?
          - Both questions are under the epic of \*who uses pip\*?

    - Sumana: when I think sequentially, broad -\> narrow?

      - we start with epics
      - perhaps then we move into specific research questions
        - in order to address that research questions, we develop a plan
          - the plan is used to describe how we\'d ask questions, process the responses?

    - Nicole: we\'d have these questions adress the epic
      - we\'d ask specific research questions, that would address the epic?
        - EG: we know we\'re gonna look at the documentation. is there any specific part of the documentation that people want us to look into?
      - in terms of the research plan, we\'d make it public.

    - Sumana: trying to understand \"research topic\" vs \"research plan\"
      - \[correction is made in the notes\]
      - OHKAY, I better understand now.

  <!-- -->

  - Can we have a date for [https://github.com/pypa/pip/issues/8546](https://github.com/pypa/pip/issues/8546)?

    - TODO: Nicole followup on ticket with Sumana & Pradyun
