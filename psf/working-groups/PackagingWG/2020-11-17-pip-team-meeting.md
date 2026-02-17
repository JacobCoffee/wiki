# PackagingWG/2020-11-17-pip-team-meeting

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

Tuesday 17 November 2020

Participants

- Sumana
- Ernest
- Nicole
- Bernard

Agenda

- status and blockers
  - Georgia \[absent\] - making progress on training

  - Sumana has not done outreach to package manager maintainers ![:(](/wiki/europython/img/sad.png ":(") \-- to do immediately after this meeting \[DONE\]

    - also need to write some draft release material
    - need to approve Simply Secure invoice

  - Ernest - nothing to report

  - Nicole
    - published a survey for getting feedback on docs, setting up docs interviews
      - NEED: no one booked this week or next.
        - seeking: someone who has used pip and looked at docs a bit
        - seeking: people who can say other docs they like

      - TODO - Sumana - mention this in PyLadies talk this week
    - doing analysis on existing data, submitted PR #9137 to update quickstart guide accordingly

  - Bernard
    - working on analysis of Python users, between 2-10 years, mental models of what pip is, how it works, what it does while it is installing packages, understanding of dependencies. Late last week, shared spreadsheet on Zulip. [https://python.zulipchat.com/#narrow/stream/218659-pip-development/topic/User\'s.20mental.20models.20of.20pip.2C.20package.20installation.20and.20deps](https://python.zulipchat.com/#narrow/stream/218659-pip-development/topic/User's.20mental.20models.20of.20pip.2C.20package.20installation.20and.20deps)

      - caution on Bernard\'s understanding of what pip is influencing his understanding of users\' understanding
      - NEEDS: validation of \"this is ok\" - if possible, Pradyun, Paul, Sumana, if anyone could look and improve analysis so far, helpful

    - also, working on other parts of report

    - Sumana asks: quantitative analysis?
      - Bernard: too small a sample size (n= about 70) for some quant stuff. But \"majority understood that pip is a package manager, that pip is for package installation, did NOT understand it was for building packages\" \... majority of participants knew that pip installed packages \"from the internet\" or from a repo, most commonly mentioned was PyPI. This info is sufficient for identifying parts of what\'s important\.... areas that users did NOT talk about. Important because majority of participants use pip to install, maybe upgrade packages. They are not using it for \"advanced\" or software package maintaining and building. And because of that, their understanding of what pip is and does is more basic, so they will need more support in things like pip outputs and how pip works
        - Sumana notes: sometimes people are using pip to do something but don\'t know they are doing it. For instance, installing also does building along the way, but user might not know that.
          - Bernard notes: right, and then this comes up when pip gives error/info output that mentions a bit of functionality (such as backtracking) that the user was previously unaware of.
- blocker issues
  - New resolver: Failure despite correct version numbers, when extras and already-installed package are encountered together #8785 [https://github.com/pypa/pip/issues/8785](https://github.com/pypa/pip/issues/8785)

  - [https://github.com/sarugaku/resolvelib/pull/60](https://github.com/sarugaku/resolvelib/pull/60) on carrying incompatibilities during backtracking
