# PackagingWG/2020-10-28-pip-teamwide-meeting

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

Wednesday, 28 October 2020

Participants:

- Sumana
- Pradyun
- Bernard
- Georgia (30 min in)

Agenda:

- [https://github.com/pypa/pip/pull/9017](https://github.com/pypa/pip/pull/9017) \-- Log an informational message when backtracking takes multiple rounds on a specific package #9017

  - P just merged it. \\o/

- [https://github.com/pypa/pip/pull/9040](https://github.com/pypa/pip/pull/9040) \-- Include backtracking in user guide

  - Feedback?
  - \[Pradyun and Sumana review it live during call\]

- [https://github.com/pypa/pip/issues/7744](https://github.com/pypa/pip/issues/7744) \-- Handle conflicts from installed packages when updating other packages

  - Prioritization: OK to defer to \_after\_ 20.3.beta1 or should we do it \*now\*?
    - SH: I think can defer to after the beta.
      - Tradeoffs:
        - Want beta out by this week. But don\'t want to put more work on P\'s desk with all that currently needs to be done.
      - People who may not have tried 20.2.4, might try this. There\'s a benefit to better error messages reducing confusion + support load.

    - P: would prefer to wait til after the beta

    - GA & BT are fine with deferring to Pradyun!

  - [https://github.com/pypa/pip/issues/8495](https://github.com/pypa/pip/issues/8495) \-- Error message update: inconsistent/conflicting dependencies

    - #8495 \-- before beta or ok if it is after? implementation: Show dependency tree in `ResolutionImpossible`{.backtick} error message #9036

    - Language changes in error message, logic changes in behavior

    - what\'s achievable by this week? nice to have for beta, definitely have it for 20.3 release

    - We can also release another beta 2 days later with this!

    - Resolved: not hold the 20.3 BETA for this fix

- Resolver survey
  - BT: the link will work for all future survey exports
  - Pradyun is looking at the reports

Pradyun planning the rest of his evening:

- [https://github.com/pypa/pip/pull/9056](https://github.com/pypa/pip/pull/9056) \-- Documentation update: migration guide (review)

- [https://github.com/pypa/pip/pull/9044](https://github.com/pypa/pip/pull/9044) \-- Documentation update: resolver default (review)

- [https://github.com/pypa/pip/pull/9019](https://github.com/pypa/pip/pull/9019) \-- Flip the switch on new resolver (implement)
