# PackagingWG/2020-08-05-pip-teamwidemeeting

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

Wednesday 5 August

Participants:

- Nicole
- Pradyun
- Bernard
- Georgia
- Sumana

Agenda:

- performance [https://github.com/pypa/pip/issues/8664](https://github.com/pypa/pip/issues/8664)

  - we could \... look at places where we are hitting the cache/revisiting, etc.

  - but the real solution is to have the result of the resolution already. This is a broader lockfile discussion for packaging. This is the next step after the resolver is out.

  - In the meantime, we need to smooth the rough edges

  - And we need to have better output when we are taking too long \[#8683\]

  - TODO: guide in user guide or similar on how to make pip faster on you (user\'s) end\.... e.g., \--no-deps

  - we are in a temporary transition period \-- we could add a command line message in error/output, saying \"if this is taking too long \... try these things, tell us\" \...

  - Bernard: wants to understand: why is it slow? what can users do to make it faster? for whom is it slow? DevOps/automation people?
    - the first thing I would do \-- put together some words, e.g., in user guide, saying \"here is what has changed between las thing and current thing, and why it is slow, and maybe what you can do to make it faster, and please tell us the kinds of issues that it is causing you\"\.... because perf and speed, you can spend every waking moment on

  - there have bee other issues about other parts of pip and performance \.... example: install from directory. This happens during development so it\'s kind of ok that it is annoying

  - [https://github.com/pypa/pip/issues/2195](https://github.com/pypa/pip/issues/2195) \-- another \"slower\" situation.

  - Sumana: this could be a disaster (for us). Actions:
    - Pradyun and Sumana to work on user guide
    - UX team to look out for user feedback related to performance. E.g. how slow? what were you trying to do?
    - Bernard: relying on people\'s memory of performance is problematic\... What kinds of data are you looking for?
    - Sumana: let\'s dig into this after this call.

- output on backtracking that leads to `ResolutionTooDeep`{.backtick}: [https://github.com/pypa/pip/issues/8683](https://github.com/pypa/pip/issues/8683)

  - what output should pip give out when it is doing stuff? it looks like it is downloading different versions of the same package. right now \.....

  - what should we be printing to the user so they don\'t think pip is stuck with the new resolver? sometimes it is stuck and we need to tell user \"I need help\" \.... we need to figure out what they should be

  - Diff between this and `ResolutionTooDeep`{.backtick}? This IS RTD. What happened earlier was we deferred it in some senses\.... but we do have an error message on the RTD [GitHub](./GitHub.html) ticket.

    - [https://github.com/pypa/pip/issues/8380](https://github.com/pypa/pip/issues/8380)

  - Sumana: how many people is this affecting? Is it common?

  - Pradyun: we have 2 reports right now

  - Sumana: if we already have 2 reports (in beta, with limited publicity) then it seems like this will affect many users

  - Pradyun: it looks like the resolver is \"stalling\". This is how the user described it. One user stuck for 4 hours.

  - Pradyun: I am not sure what we should be printing \*during the resolution\* (in addition to the error message itself)

  - Sumana: we also need to define under what circumstances pip should error out, and a preliminary threshold for pip to start saying \"weird things are happening, and the user should start getting some notice and info about that\"
    - Sumana: next steps: Pradyun to book time with UX folks to define actions

    - Ticket opened to work out the UX: [https://github.com/pypa/pip/issues/8714](https://github.com/pypa/pip/issues/8714)

- using automated testing to find likely bugs/problems in upstreams
  - grabbing a bunch of requirements.txt files and setup.py files, constraints files, etc. from [GitHub](./GitHub.html) \[and libraries.io\] and running those in test environments \[idea in [https://twitter.com/zzzeek/status/1289602964420612098](https://twitter.com/zzzeek/status/1289602964420612098) and elsewhere\]

    - asking Tidelift whether we can grab some from them?

  - using [OpenStack](./OpenStack.html) applications [https://github.com/sqlalchemy/mako/issues/322#issuecomment-667551424](https://github.com/sqlalchemy/mako/issues/322#issuecomment-667551424)

  - helping users submit test cases \-- perhaps with pipdeptree?? per [https://twitter.com/westurner/status/1289612483800338434](https://twitter.com/westurner/status/1289612483800338434)

  - TODO - Sumana and Pradyun to start planning

- resolver beta testing survey \-- how many responses? & goal-setting

  - the one that is linked to from the beta resolver\... is there a unique name or number we should use to refer to it? Survey #989272

  - \"Feedback form for testing the new pip resolver\"

  - [https://tools.simplysecure.org/survey/index.php?r=survey/index&sid=989272&lang=en](https://tools.simplysecure.org/survey/index.php?r=survey/index&sid=989272&lang=en)

  - 15 complete responses, 85 incomplete, all the way from \"opened and did nothing\" to \"4/5 of the way through, or 5/5, but not pressed Submit\"

  - we have not advertised it ACTIVELY on social media in quite a while (via proactive outreach and/or replying to people whom one sees in public talking about the resolver)\.... we should check whether it is still what we are asking and want to know

  - Goals? \.... do we have any idea of the \# of people who have updated to the new resolver?
    - see pepy.tech \... download numbers: [https://pepy.tech/project/pip?versions=20.2&versions=20.2.1&versions=20.2b1&versions=20.1.1&versions=20.0.2](https://pepy.tech/project/pip?versions=20.2&versions=20.2.1&versions=20.2b1&versions=20.1.1&versions=20.0.2) \... about 1.5 million downloads of new pip versions per day. More effort to see how many people are actually using it to interact with PyPI. Need SQL queries.

      - who is using the new resolver? we can\'t know this from our metadata\..... telemetry not there\.... how does curve/download trend look? normal.

  - there is also a Google form \.... in `ResolutionImpossible`{.backtick} message, [https://forms.gle/cWKMoDs8sUVE29hz9](https://forms.gle/cWKMoDs8sUVE29hz9) survey #cWKMoDs8sUVE29hz9 \.... not what we are talking about

    - TODO: it would be good for us to keep a page of all of the active survey links + a name for each of them. Plus a column: last time we did active outreach on this survey

    - List of surveys: [https://www.notion.so/simplysecure/b46a0992ba8548cf988200cb2a02636b?v=beba10f184b647aa87c207e832f645b4](https://www.notion.so/simplysecure/b46a0992ba8548cf988200cb2a02636b?v=beba10f184b647aa87c207e832f645b4) (work in progress)

    - would make sense for all of that to live in the area of docs about user feedback

  - DEFER goalsetting stuff till next week

  - possible to get assistance on regular active advertisement of surveys? yes - publicity bit below

  - Survey platform has a team collaboration function, but comes at a cost. Is it possible for us to get that paid for, for at most a month? Would allow us to work together, create the survey together.

- publicity
  - Sumana Working on a few avenues. Podcast, Blog posts, PSF blog? Other blogs. Another podcast.
  - Talked w/ Dustin Ingram: tweet storms!
    - what\'s the resolver? what is blocked on it? what are things that we wanna hear about?
  - thinking about pip and user feedback processes\.... what is normal? how do we expect to get feedback from people? how do we channel it so it is not overwhelming for dev team? also connects to question of effective outreach channels
    - idea: have a master list/spreadsheet of regular comm outreach channels, who it reaches. These reach these people, this is how input comes in.
    - people-driven \-- people saying things and stuff happening (feedback, changes etc?) how much response do we ever expect depending on who says it.
  - TODO: Sumana to move her Paper documents into a shared place with team

- research on pip force install [https://github.com/pypa/pip/issues/8452](https://github.com/pypa/pip/issues/8452)

  - we do not need it sooner so it is ok to not urgently prioritize. doing as part of functionality epic

- Regular meeting time
  - TODO - Sumana look at Bethanie\'s findings
