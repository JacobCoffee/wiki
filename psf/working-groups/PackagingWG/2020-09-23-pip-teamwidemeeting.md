# PackagingWG/2020-09-23-pip-teamwidemeeting

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

Wednesday September 23

Participants

- Bernard
- Georgia
- Pradyun

\[Sumana away on vacation\]

Agenda

- Status and blockers
  - Pradyun: not been too productive
  - Georgia: don\'t think I\'m blocked on anything. status: talking to a prof, getting a grad student to work on the ecosystem question. need to do the video.
    - Haven\'t heard back from Ernest w.r.t. tweets \-- I guess that\'s a blocker.
      - Pradyun might ping.
      - Ernest wrote back --- Georgia will make these clearer. Attempting to work in the notion table wasn\'t working 😅
  - Bernard: Fine! Switching gears has been a little hard this week. Last week spoke with Pradyun about pip output and read thru the issue. Deep in interviews (++ Nicole) and had a helpful debrief with Nicole and Georgia yesterday.
- Performance stuff
  - Pradyun\'s instincts about network usage was right. Unsure about how to fix it. It feels like its something that would block the release, but since we are not sure how to fix it, it doesn\'t seem like a thing that should block it. Wrote a GH issue and got comments (with some home test cases) on it. Needs to read them and work out what to do next.
  - Can we help Pradyun to work out what to do? He thinks he needs some discussion time with Paul/TP/someone and work out what to do next.
- 20.3 prep
  - Don\'t have a tracking issue for it. It\'ll be what\'s on master.
  - Real question: what could block the release?
    - Need to add the flags to flip behaviors.

    - TODO: Pradyun needs to file issues for the discussion \[done: [https://github.com/pypa/pip/issues/8936](https://github.com/pypa/pip/issues/8936) \]
- Video!
  - GA / Pradyun hasn\'t sent theirs in yet
  - Unsure about Paul, Ernest
  - Bernard, TP did
  - Bernard will send a reminder on Zulip?
- pip output discussion
  - Any follow ups?

  - 2 issues what the resolver outputs and what happens when its doing too much

  - \"I don\'t know what pip is doing\" [https://github.com/pypa/pip/issues/8683](https://github.com/pypa/pip/issues/8683)

  - Pradyun unsure what to do next. Not sure where UX help can

  - BT: the best type of approach would be UX team working w/ you.
    - Would it be worth spending, let\'s say, a period of time saying we\'re trying to redo pip\'s output from scratch.
    - TODO: Pradyun and Bernard to organise a time - invite Georgia, Nicole
- Interview Research Themes so far
  - Tension between pip has a basic packaging tool vs more advanced functionality like building wheels

  - Trying to untangle a lot of things, but there\'s fundamental things that need discussions/exposure.

  - GA: the challenge is that it makes it harder for users to know to expect.
    - why can you build wheels, but not publish it?

    - there\'s \<advanced functionality\>, why not \<other advanced functionality\>?

  - Pradyun would like a list of \"here are the things we need to discuss\" out of the research we\'re doing. (this is helpful - thank you)
    - How should we do read-outs form the research
      - around theme, GH issue, something else?
      - summarise the broad theme, while flagging things I\'m unsure about -
        - example: if I was able to say that I am very sure that majority of participants find the pip output very noisy.
          - what they\'re looking for is XYZ \-- that\'s a common need.
          - best practice to not have a noisy interface.
        - Things we sure about, and things we are not fully sure about
          - GA: I think percentage can be useful if they\'re clear.
            - trying to understand \-- the data point can be hard as straight percentages.
            - \"Dissecting\" the results into smaller groups, to see patterns in that group.
              - Based on how long they\'ve been using pip.
            - Themes: the kind of issue people have. eg: these are issues with people trying to use wheels, compile stuff, use pip in different contexts.
              - E.g. how each of these groups spoke about compiling stuff
                - less than 2 years: had a lot of problems, essentially cold not do this
                - 2-10 years: 70% could do this, but it caused a lot of issues with dependcies, hacks
                - +20 years: drew on their experience and made it work
    - TODO: Georgia/Nicole/Bernard:
      - how do we share
      - Ways to group information: (rough draft for starting)
        - High Level Themes
        - Experience Level with pip
        - User Type
        - role/job/what they do with Python
        - pip functionality specifics

  - What is pip\'s personality - I\'m not really smart, I\'m a little smart

  - There\'s no distinction between the easy cases and the complicated (`pip install something-simple`{.backtick} looks the same as `pip install something-really-complicated`{.backtick})
