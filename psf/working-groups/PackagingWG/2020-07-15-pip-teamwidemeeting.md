# PackagingWG/2020-07-15-pip-teamwidemeeting

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

Team Meeting - Wednesday 15th July

Attendees:

- Sumana
- Nicole
- Pradyun
- Georgia
- Bernard
- Ernest (attending from half way through)

Agenda:

- Status/blockers
  - Pradyun: next up: wrapping up 20.2, want to have a release by early next week. Blockers: error messages thing, which is in the agenda today

  - Georgia: no blockers. 

  - Bernard: last week \[personal\]; am now moving documentation from Notion  and HackPad to git wiki? done.

    - TODO: Sumana can update links to more permanent location.

    - Have been using on who uses pip & pip ? user research ticket mostly, plus other activities

  - Nicole
    - Nicole requires the following to be reviewed:
      - Documentation research plan before posting to GitHub: [https://hackmd.io/q1TjDssCTyWDdi_tv_a8BQ?both](https://hackmd.io/q1TjDssCTyWDdi_tv_a8BQ?both)

        - Georgia has reviewed - thank you ![:)](/wiki/europython/img/smile.png%20":)")

        - Need others to also look at it

      - Survey for gathering user feedback on pip search: [https://forms.gle/qY7PA3U4QHmo9Ao66](https://forms.gle/qY7PA3U4QHmo9Ao66) (see [https://github.com/pypa/pip/issues/5216#issuecomment-658690246](https://github.com/pypa/pip/issues/5216#issuecomment-658690246))

        - Paul has reviewed ![:)](/wiki/europython/img/smile.png%20":)")

        - Need others to also look at it

        - also #8456 (later in meeting)

  - Sumana: [https://pyfound.blogspot.com/2020/07/pip-team-midyear-report.html](https://pyfound.blogspot.com/2020/07/pip-team-midyear-report.html) - need to work next on docs for release; no blockers

- July release timing (20.2)
  - We usually do releases early in the month, or try to. McSinyx asking about a beta - do we want to do this?

    - Pradyun has looked at what has come through and been merged. Nothing needs a beta. His code has not yet been merged. So we don\'t need a beta

  - Target date: Monday the 20th or Tues the 21st? Maybe. Pradyun is working through backlog. The warnings & installation stuff is a bigger change than expected. Also communicating around error messages/reasonable. \[possibility of vacation\]

- date for [https://github.com/pypa/pip/issues/8546](https://github.com/pypa/pip/issues/8546)              Updating the message when the user hits a conflict w/ installed packages            #8546    

  - 20.3 would be in Oct, goal is to be the default by then.
  - \[discussion about \$MONTH in the message\]
    - Pradyun: it\'s fine, not perfect, but that\'s perfectly fine.
  - answered in the issue
  - Survey is launched! ✨ 216 responses! 71.6% say they want pip to install nothing and instead error message saying it would cause incompatibility (150-ish today)
    - how should pip report warnings go?

    - Nicole has not yet gone through individual comments. Will analyze and bring back to the team.

    - TODO: criteria for closing survey? Bernard and Georgia & Nicole to decide

      - as responses increase, 71% number has not really budged.
      - we will link to survey from the error message and then change pip behavior based on that

    - response rate/speed \-- compared to PyPI surveys, slightly slower. But when you put out a question poll like this via Twitter, you get responses quickly. Single-question \-- this helps. low dropoff rate

    - Bernard \-- on Monday, I sent it to the \~180 participants of UX survey panel who had agreed to receive surveys. 216 responses is very good. And it\'s 1 question, so a few minutes of focusing time. (23 clicks from twitter + 180 emails sent to UX study so \~ 216 is very good.)

    - Georgia: looking through replies - many people are talking about what they are used to, what other tools they have mental models from. Content of responses will be useful for broader research question. Comment from the comments: \"(PS: Great scenario! Simple, clear and concise)\" Appreciating how many people are directly responding to tea & coffee use case. It took us a while to concretize an example that could be logically understood without framing with specific real packages. Tea & coffee \-- useful!

      - Nicole: and we can use iced tea, flavored coffee, etc., and expand/extrapolate!
      - YAY NICOLE for coming up with analogy!
  - concern Paul raised: don\'t show a link to that survey forever! Put the message on a timer \-- show a link for a certain number of weeks, have it disappear from pip after that point
    - Pradyun: looking at calendar and conditionally print it
    - Bernard: I AM EXCITED ABOUT THIS: can we formalize this in some way, so we can use this functionality for future work? a great way of recruiting and communicating with participants directly
      - TODO: Pradyun to file issue corresponding to this. Tag Bernard. DONE: [https://github.com/pypa/pip/issues/8586](https://github.com/pypa/pip/issues/8586)

      - Sumana: after formalization, could tie into deprecation policy (a calendar-conditional verbose message on deprecated functionality)

- Question: What is the situation with \"Print Better Error Messages\" and \"Improve User Experience\" milestones on GitHub? Are these used?

  - e.g. [https://github.com/pypa/pip/milestone/25](https://github.com/pypa/pip/milestone/25) [https://github.com/pypa/pip/milestone/10](https://github.com/pypa/pip/milestone/10)

  - Nicole was looking into research epic for improving functionality 

  - Pradyun: these are Ad hoc collections. print better error messages: some pip maintainers were storing cases where we know the error msgs could be better, didn\'t have time to figure it out in detail. not sure how to prioritize. a good thing for Nicole to review.

  - Improve UX milestone: mix of broad ideas for sweeping changes. example: speeding up how one of the slowest parts of pip works. Or improve upgrade \[thing\].  

  - Sumana: may need to slice-and-dice categories better, milestone is probably the wrong abstraction

  - Nicole: will go to backlog of tickets and see what can fit into the research epics, and crosslink them
