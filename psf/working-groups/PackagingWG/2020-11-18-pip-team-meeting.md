# PackagingWG/2020-11-18-pip-team-meeting

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

Wednesday 18 November 2020

Participants

- Pradyun
- Sumana
- Georgia
- Bernard

Agenda

- Status & Blockers

  - Pradyun: planning to work some this week
    - done: caught up on list discussed last time \-- #8785 is left. Decided: we can improve behavior, but this is not a blocker. We are doing better than old resolver, not as well as we want to.
      - TODO: Sumana to mark for post-release: DONE

    - now, #8495 needs Pradyun to make an update
      - also, Pradyun has a few things he needs to do: update vendored packages, check for deprecations to make or deprecated things to remove. Prediction: simple, no traps.

    - no blockers yet. Will file a PR that he needs a review on, and we will need #9124 review ([https://github.com/pypa/pip/pull/9124/files](https://github.com/pypa/pip/pull/9124/files))

      - TODO: Sumana or Bernard to look after this call \-- Sumana to take this \-- DONE
  - Bernard
    - same as yesterday:

    - working on analysis of Python users, between 2-10 years, mental models of what pip is, how it works, what it does while it is installing packages, understanding of dependencies. Late last week, shared spreadsheet on Zulip. [https://python.zulipchat.com/#narrow/stream/218659-pip-development/topic/User\'s.20mental.20models.20of.20pip.2C.20package.20installation.20and.20deps](https://python.zulipchat.com/#narrow/stream/218659-pip-development/topic/User's.20mental.20models.20of.20pip.2C.20package.20installation.20and.20deps)

      - caution on Bernard\'s understanding of what pip is influencing his understanding of users\' understanding
      - NEEDS: validation of \"this is ok\" - if possible, Pradyun, Paul, Sumana, if anyone could look and improve analysis so far, helpful
      - Ideally in the next few days, within a week
  - Sumana
    - In similar spot to yesterday
    - Have done some outreach to package maintainers
      - TODO: Sumana to reach out to Debian and Fedora people
    - TODO: also need to write some draft release material
    - TODO: need to approve Simply Secure invoice
    - TODO: Give Dustin a heads-up that release will probably be this week, please work to mobilize the support crowd
  - Georgia
    - UX team are in deep analysis, synthesizing results. Talked through mental models, functionality

    - Talked with people who have run dev workshops. Will plan some followup conversations. Useful frame: frame with developer use cases. That is often successful

    - Data analysis: want to document what we did and make data useful

    - Design logo survey: over 250 responses. Turning that into a brief, will post on OS design. May use this as another data source for mental models analysis \-- using metaphors.

    - Additional Folks from Simply Secure helping: Ngọc Triệu, Karissa McKelvey

- Blocker issues
  - Outreach to package manager maintainers
    - Debian/Fedora Python folks? Bernard reached out via IRC \-- page was shared by Pradyun a few months back.
      - TODO: Bernard to share the exact details w/ Sumana, then plan to move forward on this.
        - DONE: David Kalnischkies (Debian) for aptitude & Daniel Mach DNF/YUM (Fedora)

  - New resolver: Failure despite correct version numbers, when extras and already-installed package are encountered together #8785 [https://github.com/pypa/pip/issues/8785](https://github.com/pypa/pip/issues/8785)

    - TODO: Sumana to note on issue that this is not a blocker \-- DONE

  - [https://github.com/sarugaku/resolvelib/pull/60](https://github.com/sarugaku/resolvelib/pull/60) on carrying incompatibilities during backtracking

    - this ended up not being the right approach. As we see now that we have a test case. Needs more work and discussion to figure this out. This is a blocker (as is pip#9011). Important. Will finish other things so Pradyun can use TP\'s additional work, merge a fix, then cut release

  - [https://github.com/pypa/pip/milestone/38](https://github.com/pypa/pip/milestone/38)

    - #9092 \-- Pradyun needs to look at this further to check whether it\'s a blocker
    - We\'re fine, everything here has a simple path forward

  - [https://github.com/pypa/pip/projects/5](https://github.com/pypa/pip/projects/5)

    - Sumana and Pradyun to triage the \"needs triage\" column \-- DONE

  - Resolver survey results
    - TODO: Bernard to update the thread today \[in Zulip\]

- Plans for November

- UX Team Question/Idea
  - Documentation Ideas
    - Github issues to enable community contribution ?
    - per data from mental models survey - people might need, in pip docs, link to explanation of \"what is a package manager?\" \-- stuff the Python community recommends
    - Writing and overhauling docs would be a lot of work, not in scope for this year, but we could make recs about style, tone, linking of topics, make docs stronger for people, canonical place people turn
    - We could scope particular \[things\] comm could follow up on, community could contrib
      - What has been successful? how can we queue up community to make valuable contributions?
    - Have a page that lists all the error messages and says what they mean (inspired by rustc\'s \--explain)
    - For developers: all the info we have collected as \"this is what we did during this timeframe\" and \"tools for you to use going forward\" - mental models, etc., for feature scoping, process, etc.
    - Make things easier for ALL users to FIND info
    - Sumana:
      - Carol Willing (sp?), Python Steering Committee member, has started a documentation Working group earlier this year. The point for python core is to have a stronger process and vibrant set of volunteers to improve the ability for people to improve, maintain, contribute documentation to core Python.
      - packaging.python.org - right now is separate from pip.pypa.io --- the packging docs and the pip docs --- it could be that one of the useful ways that this could move forward is by increasing the amount and quality of stuff that is available at packaging.python.org. There are folks interested in improving packaging.python.org, there is intersection, but not total overlap with the pip docs folks. Thea Flowers worked on packaging.python.org.
        - Known as PyPUG
      - Alex Grönholm: interested in improving the state of packaging instruction. Aiming at developers who make packages
    - SH:
      - dubious about trying to optimize for contributors who don\'t write docs usually, and write docs for these things.
        - wrong assumption that \"writing docs is easy / can be first contribution\" \--\> any framework that we set out has to accomodate for people believing this
      - dubious of attempting ongoing good docs, without constant maintainance from a maintainer with capacity about doc writing (sentence and broader)
        - looking forward to the UX discussions/training w/ maitainers.
      - information design training! (potentially useful fundable thing!)
      - sustainability is also a thing to consider.
      - GSoD: scoping out some of this work for that, would make sense.
      - Being broader about this effort \-- has to be about more than pip + packaging.python.org (like setuptools, virtualenv and more!) and wanting to get links into docs.python.org for directing users to the relevant information.
    - GA:
      - need to consider how to make docs happen in a sustainable way.
      - where we\'re at right now, moving based on user feedback
      - talking to Carol \-- in a few weeks might a be good time? Or now?
    - SH:
      - earlier better than later.
      - love the idea of making packaging docs, that caters to all of the personas.
      - sharing info collected for dev usage!
    - TODO - Georgia to reach out to Carol Willing
      - TODO - Sumana to give contact info

- Bug triage for [https://github.com/pypa/pip/projects/5](https://github.com/pypa/pip/projects/5)

  - New resolver does not identify a subset of extras #8875 [https://github.com/pypa/pip/issues/8875](https://github.com/pypa/pip/issues/8875)

    - TODO: Sumana to mark as duplicate of #8785 \-- DONE

  - Incorrect failure message when multiple specifiers mention the same package, one of them pointing to a wrong version #8884 [https://github.com/pypa/pip/issues/8884](https://github.com/pypa/pip/issues/8884)

    - Separate from #8495, but deals with similar type of logic. Pradyun will investigate and work on this at the same time as working on #8495

  - [https://github.com/pypa/pip/issues/9020](https://github.com/pypa/pip/issues/9020) pip 20.2.4 with 2020 resolver does not use pinned version in the constraints file

    - TODO: Sumana to improve linking from Constraints file section of user guide to paragraph about changes in migration guide, then close as \"works as intended and there is now documentation about it in the migration guide\" \-- DONE

  - new dependency resolver runs \"forever\" due to incompatible package versions #8922 [https://github.com/pypa/pip/issues/8922](https://github.com/pypa/pip/issues/8922)

    - The new error message helps a little. Feels like this should be enough
    - TODO: SUMANA to add a note about this and remove it from the to-triage pile; close as fixed. \-- DONE
    - BUT: printing package name in error output
      - #8346 was closed
      - TODO: Pradyun to file a new issue about this idea

  - \[2020-resolver\] Pip downloads lots of different versions of the same package #8713 [https://github.com/pypa/pip/issues/8713](https://github.com/pypa/pip/issues/8713)

    - fundamentally a \"backtracking a lot and I don\'t know why\" issue plus \"how can we make this better\"
      - TODO: Pradyun: make a new issue/hook onto existing issue about the things that need doing that are blocked on Warehouse stuff/API stuff

  - Stuck in long-running loop for already satisfied requirement when using resolver. #8883 [https://github.com/pypa/pip/issues/8883](https://github.com/pypa/pip/issues/8883)

    - Same as #9011 \[blocker issue for resolver being stuck in a loop\]
    - TODO: Pradyun to close as duplicate \-- DONE

  - TODO: Pradyun to check in on privileges issue re pip committers \-- DONE
