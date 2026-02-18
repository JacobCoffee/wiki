# PackagingWG/2020-09-30-pip-teamwidemeeting

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

Wed Sept 30

Participants:

- Bernard
- Pradyun
- Georgia
- Sumana

Agenda:

- status & blockers

  - Bernard :chatted with Pradyun about pip output. In progress. And doing some analysis of \"who uses pip\". Considering whether people ID as someone from underrep\'d group.
    - blockers: waiting for the PSF account to tweet out surveys, to get more data.
      - GA: need to draft and ask \-- working on it.
    - Also need to send Sumana pip resolver answers output
  - Followup on research themes
    - GA (typing): Nicole, Georgia & Bernard were reviewing response rates and discussing survey status at the moment, and decided to add a question about identifing as a member of an underrepresented group, because we realized that we need to hear more from non-NA, non-EU folks, and non-male

    - going through response rates, who we\'ve heard form, who we haven\'t. who uses pip survey has lowest response rate (mostly EU/NA, mostly male). Asking PSF to tweet again.
      - Specifically talking to non-male, not NA/EU pariticapnts \-- toward reducing the bias

    - SH:
      - I do have a hope that as the video gets more widespread distribution, that more people will register -\> more people will take surveys -\> might help shift the ratios.

        - not a \"don\'t do this \[additional outreach\]\", but a hope that this will help.

      - translating into local languages
        - GA: localization lab, OTF situation makes resources tricky?
        - GA: Directed outreach?
        - GA: Specifically reaching out to under-represented groups, via Twitter?
        - SH: TP might be willing to translate to Chinese.
        - GA: Japan has a pretty big community.
        - Open Source Design \-- potentially Africa based outreach.
          - All of this is toward more diverse set of responses.
  - SH: from yesterday\'s call:
    - Georgia: giving Sumana access to resolver survey (while still giving Pradyun access to annotate things). Working on it today \-- DONE via Bernard sharing in a different medium

    - Pradyun: has filed an issue for the rollout flag, and triaged stuff and made an issue for 20.3 release \-- [https://github.com/pypa/pip/issues/8936](https://github.com/pypa/pip/issues/8936)

    - Sumana: video is done (yay) \-- [https://www.youtube.com/watch?v=B4GQCBBsuNU](https://www.youtube.com/watch?v=B4GQCBBsuNU)

      - next: invoice approval
      - trying to rearrange Tuesday meeting to half an hour later

- Georgia: Training for devs followup question!
  - GA: were talking BT,NH,GA \-- getting a better sense from SH about what the training should look like (who, what).
    - From phase 3 plans:
      - Update workflows, expand user journeys, and develop checklist for developing new features

      - Develop templates for UI bugs, commands, error messages, output, documentation, and configuration files

      - Teach other pip developers UX practices per [https://simplysecure.org/what-we-do/user-research/](https://simplysecure.org/what-we-do/user-research/)
    - SH: lecture vs workshop, one-to-many, etc has opinions
      - think the people who are major contributors to pip will be able to devote a few hours a couple of times for synchronous things
        - check availability.
        - 9-ish people who are major contributors + maintainers.
        - if we can expand it to a slightly broader group \-- pipenv/pipx/poetry, would be nice!
        - 2 sessions of 3-ish hours might work, if we can run it at different times.
        - online, resources available for later reference.
          - hands on + experience is so much better than sitting and being lectured to
          - inspired by software carpentries
    - PG: might have something later.
      - SH: Pradyun might find it easier to have a rough reference to base his ideas/understanding of off to provide feedback \"now\"
      - GA: will find a link to the a guidebook that we worked on with Internews and others re: open source projects, feedback loops, etc
        - [https://usable.tools/guidebook/](https://usable.tools/guidebook/)
      - SH: SS has experience around feedback loop, what information is useful for making decisions.
        - (PG: \*nodding aggressively in agreement\*)

- Performance
  - [https://github.com/pypa/pip/issues/8664](https://github.com/pypa/pip/issues/8664) & [https://github.com/pypa/pip/issues/8905](https://github.com/pypa/pip/issues/8905)

    - SH: avoid a disruptive rollout if we\'re not ready yet.

    - PG: marked [https://github.com/pypa/pip/pull/8932](https://github.com/pypa/pip/pull/8932) as the blocker for now, and once that\'s done, I think we\'ll be OK?

      - TP has filed some PRs based on our discussion that make the resolver less eager to hit the network, & give users more control \-- if pip is slow, we give the user the ability to restrict space it searches by trying \[something\] first. When user provides several requirements, we may try to loosen a constraint before trying tightening things?

      - in cases where we do backtracking, it feels like we can\'t do much on performance in those cases

      - but we don\'t have a good answer to `ResolutionTooDeep`{.backtick} discussion \-- if it\'s taking too long, right now we don\'t stop and say \"we\'re taking too long\".

    - SH: benchmarking?
      - Pradyun has some sample `requirements.txt`{.backtick} files locally. if it\'s not 20x slower I think we should go ahead? will post in [https://github.com/pypa/pip/issues/8664](https://github.com/pypa/pip/issues/8664) and we\'ll take discussion from there

    - uhm, the so, we have a few differnet realted problems
      - in the \"base case\" (no backtracking) \-- what level of slowdown is good enough?

      - in the \"complex case\" (because backtracking) \-- hey, the reason this is slow, it\'s because we\'re backtracking.
        - related question: if the resolver is backtracking, is it the `ResolutionTooDeep`{.backtick}

          - if pip is backtracking lots of choices, pip might want to present a message to the user that it\'s backtracking a lot.

        - Pradyun has an idea! there\'s a reporter to use.

        - TODO: Pradyun to file an issue and talk about it with Paul and TP, maybe also a PR

      - Hey UX team: figuring out the `ResolutionTooDeep`{.backtick} error message/docs will be high-priority and may displace other work, because it blocks 20.3

    - Pradyun: if we make, e.g., 20 choices that backtrack, we would tell user \"we are hitting a lot of conflicts so this might take a while\" with maybe some context and link to docs, while pip keeps working. Would this be helpful to the user who thinks \"pip is in an infinite loop?\"
      - Bernard: the issue: pip is doing something, because it needs to do this thing, trying many different options. At some point in time, user will think \"this is taking too long, what is happening?\"
        - Pradyun\'s idea: choose, after a certain \# of backtracks, tell user what\'s going on. Good idea! User is starting to ask \"what\'s happening?\"

        - If possible, it would be even better to prompt user: \"do you want me to continue doing this \[trying different choices for a candidate\] or abort?\" because it\'s practically impossible to come up with a decision that covers all users/situations. Need more work to understand on a better level. CONTINUE: maybe for another \~20. ABORT: explain why we were having the problem. \"Pip had a hard time finding a candidate that satisfies all dependencies \-- read more about that here.\"

        - Georgia: can we give them agency in this way?

        - Pradyun: good idea, but how do we do this & put it into how pip works today? Asking the user for input. We don\'t do that almost ever in pip\'s normal run as of today. CI usage, etc. \...how often we should do this\...

        - Sumana: there is a kind of splitting the difference here \-- we could spit out a message reminding the user, that here\'s how to abort
          - basically what Pradyun said, but include information to tell the user how to abort.
          - that is the easiest thing that we could implement now, that we could iterate on that.
            - adding a new interactive prompt would take a bit of infrastructural work.
          - SH: might be worth having some keyboard input to have pip say \"skip this and do the rest\"
            - PG: oh boi, lots of work.

        - SH: let\'s start with what Pradyun is suggesting, and we can iterate on this as we proceed.
          - Pradyun: it would be nice to figure out what is relevant to show user in the message. Such as \"here\'s how to abort at this time\" \-- what else does user need to know so they can understand and make a decision?
          - SH: is this something we can figure this out without additional surveys?
            - GA: yea, we should be able to figure something out based on the existing error message design work & research.

            - SH: no additional data collection?

            - BT: yes \-- nothing additional.

            - BT: \"what has pip done\", \"what is pip doing\", \"what is pip going to do\"
              - if pip\'s doing a 20th backtrack, if we can print it in the output, we should present information to the user.
              - if we can print out \"hey, at any moment, you want me to stop, Ctrl+C stops me\"

            - TODO: Bernard to talk with Pradyun about needs, then Bernard and Georgia to make a draft template of info user needs in info/error message

            - GA: the other thing people do is progress bars
              - A moving period, heartbeat. We could tweak this
              - Pradyun: what we currently do: printing out a lot of lines where only 1 number changes.

            - GA: a crazy idea!
              - estimated time of completion: If there\'s a way to check the dependency list, to tell how long it might take \-- a guesstimate?
                - PG: not sure if that\'s possible by October. ![:)](/wiki/europython/img/smile.png%20":)")

                - TODO: Sumana: great idea! let\'s file a ticket! but for far future \-- DONE, Georgia filed [https://github.com/pypa/pip/issues/8943](https://github.com/pypa/pip/issues/8943)

- pip 20.2.4 (documentation updates)
  - Q (to SH): do we only want documentation updates here? Cutting the release off master isn\'t 100% ideal (since that goes out to \*everyone\*)

- go/no-go decision: performance and go/no-go decision on new resolver as default in 20.3
  - Q: do we want a \"lame\" beta-ish release for the resolver, to ensure our changes worked? ![:o](/wiki/europython/img/redface.png ":o")

  - SH: so, over the next few days, we\'re gonna know more about performance. I\'d like our chat on Tuesday, to be focused on what do we now know and what improvements we\'ve made + what we can change \-- make a decision tree, and figure things out \-- and figure out if we\'re putting out 20.3 in October.
