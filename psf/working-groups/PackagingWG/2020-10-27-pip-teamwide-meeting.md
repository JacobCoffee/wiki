# PackagingWG/2020-10-27-pip-teamwide-meeting

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

Tuesday, 27 October 2020

Participants:

- Pradyun
- Ernest
- Georgia
- Nicole
- Sumana

Agenda:

- Release: schedule change
  - [https://github.com/pypa/pip/issues/8936](https://github.com/pypa/pip/issues/8936)

  - consensus from group
- Individual status/blockers
  - Pradyun: yesterday was productive! ![:D](/wiki/europython/img/biggrin.png ":D") merged CI fixes which should unblock everything else. PR for flipping new resolver switch needs update re Python 2 change. Everything else: reviewing and merging PRs. Only looking at 20.3 milestone. All of this can be done in the next day assuming others are quick to respond. Reviewed many issues over the past day - nothing reproducible. So bugs likely already fixed!

    - knows what to do next
    - starting mid-Nov: reduced availability

  - Nicole: no blockers at moment. Next: #7744 summary/analysis. Also starting to summarize functionality epic. Exciting! will start interviewing about documentation this week.
    - TODO: Ernest to RT a tweet \-- DONE!

  - Georgia: no blockers. Simply Secure\'s ops person will send contract amendment to PSF.

  - Ernest: ![:-)](/wiki/europython/img/smile.png%20":-)")

  - Sumana: yesterday, co worked w/ Pradyun. Finished first drafts for (1) docs for 20.3 new resolver (2) more details in new resolver migration guide. blocked on reviews. next up: more writing (release announcements + related things)

  - Bernard: unblocked. Got review suggestions on PR, need to read & apply.
- Outstanding issues blocking release
  - Handle conflicts from installed packages when updating other packages
    - #7744 [https://github.com/pypa/pip/issues/7744](https://github.com/pypa/pip/issues/7744)

    - specifically: how/where should we convey \"Pip only considers the packages being installed, and may break installed packages.\"? Docs?

    - Long-term UX recommendation: do not intro new incompatibilities when doing an upgrade. Consider existing installed packages when making an upgrade. So, the current recommendation: create an error message telling user what is going to happen. Then, long-term, Nicole to open an issue suggesting the change in behavior longterm
      - Pradyun: yes, followup release
      - Nicole: planning: where do we publish survey results? Put them in pip docs as example of UX research!
        - Sumana: yes!!!

    - TODO: Nicole to make error message rec (ideally today), Pradyun to implement

    - TODO: Nicole to open issue re: longterm behavior change

  - Log an informational message when backtracking takes multiple rounds on a specific package
    - #9017 [https://github.com/pypa/pip/pull/9017](https://github.com/pypa/pip/pull/9017)

    - Nearly done

    - TODO: Bernard to review

  - Include backtracking in user guide
    - #9040 [https://github.com/pypa/pip/pull/9040](https://github.com/pypa/pip/pull/9040)

    - Bernard reviewing and finishing

  - [https://github.com/pypa/pip/milestone/38](https://github.com/pypa/pip/milestone/38) ? \[others?\]

    - `ResolutionImpossible`{.backtick} error message - [https://github.com/pypa/pip/issues/8495#issuecomment-714771364](https://github.com/pypa/pip/issues/8495#issuecomment-714771364)

  - [https://github.com/pypa/pip/issues/8785](https://github.com/pypa/pip/issues/8785) New resolver: Failure despite correct version numbers, when extras and already-installed package are encountered together

    - Pradyun: TP and I had a call, had a long discussion, TP wrote comments, \... looks like one of the sub-issues needs fixing before release
    - TODO: Pradyun to investigate
- non release stuff
  - Documentation tracking via Matomo
    - GDPR concerns, coz we\'re collecting data?
      - Nicole: looked up, seems like no concerns.
      - GA: Should be fine if we\'re not using IP addresses. Haven\'t looked at it yet \-- Matomo is generally better. There\'s more options (Plausible) and we can look into that if needed.
      - Nicole/GA: gonna share passwords and explore this.
    - How quickly do we need this?
