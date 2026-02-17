# PackagingWG/2020-11-10-pip-teamwide-meeting

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

Nov 10th, 2020

Participants:

- Ernest W. Durbin III
- Georgia Bullen
- Sumana Harihareswara
- Pradyun Gedam
- Bernard Tyers

Agenda:

- Issues that need followup
  - #9011 [https://github.com/pypa/pip/issues/9011](https://github.com/pypa/pip/issues/9011)

    - Fix is in [https://github.com/sarugaku/resolvelib/pull/60](https://github.com/sarugaku/resolvelib/pull/60)

      - looks like TP needs help developing a good test for this - will be Pradyun (as far as us counting on who does it)

  - [https://github.com/pypa/pip/issues/7744](https://github.com/pypa/pip/issues/7744) - Warn users about dependency conflicts when updating other packages

    - Pradyun\'s working on a patch \-- a few different parts, one is done
      - Nicole followup on improving the message - [https://github.com/pypa/pip/issues/7744#issuecomment-718396220](https://github.com/pypa/pip/issues/7744#issuecomment-718396220)

        - TODO: followup conversation

  - [https://github.com/pypa/pip/issues/8785](https://github.com/pypa/pip/issues/8785) New resolver: Failure despite correct version numbers, when extras and already-installed package are encountered together

    - Pradyun to look at this before tomorrow\'s meeting

  - [https://github.com/pypa/pip/pull/9040](https://github.com/pypa/pip/pull/9040) - Bernard, backtracking error message

    - run `nox -s lint`{.backtick} locally to print the error message locally and then fix things up

    - TODO: help Bernard grab Sumana\'s commit \-- DONE
      - [https://github.com/pypa/pip/commit/e6acca646abcaaac7515da9b964d5b5291264142](https://github.com/pypa/pip/commit/e6acca646abcaaac7515da9b964d5b5291264142)

- Nicole did some analysis on the survey about what pip should do when upgrading another package (take already-installed packages into account?) and filed a few issues \-- #9094 & #9095

  - For Pradyun to look into

- pip 20.3 release next week?
  - TODO: Sumana to give Georgia some language to circulate to civic tech groups \-- DONE
  - Pradyun has feeling but not certainty that next week is a reasonable target
