# PackagingWG/2020-11-02-pip-teamwide-meeting

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

Monday, 2 Nov 2020

Participants:

- Pradyun
- Sumana
- Georgia

Agenda:

- Yay, beta is out!
  - Feels like we checked the checkbox! ![:-)](/wiki/europython/img/smile.png ":-)")

- Status & blockers

  - UX team: no blockers to report. status: analyzing surveys, still doing some interviews. Will check further re blockers.
  - Pradyun: beta is out! issues: mostly as listed below.
  - Sumana: did some triage + replaying to issue. some announcements (not widespread, likely today). making a \"things that I do after a pip release\" list.

- Note: Ernest has a week off.

- Invoices!

- issue followup on things that we would like to finish before stable 20.3 release (from [https://github.com/pypa/pip/projects/5](https://github.com/pypa/pip/projects/5) , [https://github.com/pypa/pip/projects/6](https://github.com/pypa/pip/projects/6) , and [https://github.com/pypa/pip/milestone/38](https://github.com/pypa/pip/milestone/38) )

  - New resolver: Failure despite correct version numbers, when extras and already-installed package are encountered together #8785 [https://github.com/pypa/pip/issues/8785](https://github.com/pypa/pip/issues/8785)

    - last TODO was that Pradyun would investigate - any outcomes?
      - Not yet \-- haven\'t looked into this since the call w/ TP.
      - Upon re-look: hairy problem. Bunch of edge case. Surfacing more often than we had expected. Needs to be fixed before 20.3.
      - TODO: Will need 3-4 hrs of Pradyun diving into it, connecting in currently unresolved issues.

  - [https://github.com/pypa/pip/issues/8380](https://github.com/pypa/pip/issues/8380) `ResolutionTooDeep`{.backtick} error message

    - Have we resolved this with some other PR that maybe didn\'t get attached?

    - We basically removed the `ResolutionTooDeep`{.backtick} error in [https://github.com/pypa/pip/pull/8275](https://github.com/pypa/pip/pull/8275), because we figured \"how many package names have we looked at\" is a bad metric. ![:)](/wiki/europython/img/smile.png ":)")

      - We should probably to reintroduce this, as a hard-stop error at 1000 backtracks on the same package name.

      - should this block the 20.3 release? It\'s nice-to-have for when resolver behaves badly, as in #9011\.... current threshold of 2 million is A LOT.

      - `ResolutionTooDeep`{.backtick} \-- we changed it to 2 million package names, so no one ever sees it

        - but users will get backtracking error message

      - PG: should not block 20.3 release
        - SH: ok with not blocking the release on re-introducing this error. the backtracking provides context to the users.
        - GA: sounds good.
        - TODO: Sumana to explain this on the bug and move it out of blockers

  - [https://github.com/pypa/pip/issues/9011](https://github.com/pypa/pip/issues/9011) Pip 20.2.4 goes into infinite resolution of dependencies #9011

    - What\'s next here? Investigation or implementation?
      - Investigation needed, seems a resolvelib bug.
      - Definitely a blocker for 20.3.
      - Not sure how likely it is that users hit this, since \"when does this happen\" is not clear.
        - But users hit this already, so, likely definitely gonna be a problem if not solved.
      - TODO: Pradyun to investigate \[probably to talk with TP as well\]

  - printing warnings about pip potentially introducing conflicts involving existing dependencies: [https://github.com/pypa/pip/issues/7744#issuecomment-717773481](https://github.com/pypa/pip/issues/7744#issuecomment-717773481)

    - What needs to happen next here? Implementation, or more UX work to polish the warnings/information messages?
    - Implementation, and then \*maybe\* another round of reviews if I was wrong about what\'s do-able.
    - TODO: Pradyun to implement

  - Including backtracking in the user guide [https://github.com/pypa/pip/pull/9040](https://github.com/pypa/pip/pull/9040)

    - incorporate Sumana\'s commit and merge?
    - TODO: Pradyun to \^

  - [https://github.com/pypa/pip/issues/8495](https://github.com/pypa/pip/issues/8495) New resolver error message is confusing if a package has inconsistent dependencies #8495

    - Is this post-release work or do we need it for 20.3?
    - Should be doable for 20.3, but I wouldn\'t block the release for it.
    - TODO: Sumana to note in issue: not a 20.3 blocker

  - [https://github.com/pypa/pip/issues/9083](https://github.com/pypa/pip/issues/9083) numpy, PEP 440, comparison, version normalization

    - How hard is this to fix?
      - Has an approved PR, can be merged as is (waiting on writing a test tho): [https://github.com/pypa/pip/pull/9085](https://github.com/pypa/pip/pull/9085)

      - Pradyun resigns himself to making the 5-line test

      - TODO: implement test, merge
