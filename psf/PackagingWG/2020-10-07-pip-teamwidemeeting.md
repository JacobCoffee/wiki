# PackagingWG/2020-10-07-pip-teamwidemeeting

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

Wed Oct 7

Participants

- Georgia
- Ernest
- Pradyun
- Bernard
- Sumana

Agenda

- Status & blockers

  - Pradyun: Yesterday, worked though surveys + project board. Wants help deciding order to do things in. Prioritization.

  - Georgia: No particular blockers. TODO: give Ernest a tweet. And: `ResolutionImpossible`{.backtick} error, backtracking message, clarifying what\'s needed.

  - Bernard: no real blockers. We have been getting more signups for UX Studies panel, and 20+ signups for \"who uses pip?\"

  - Ernest: there will be progress on minuting on python.org - [https://github.com/python/pythondotorg/issues/1656](https://github.com/python/pythondotorg/issues/1656) - want to be an alpha user?

    - Sumana says: yes! First iteration is specific to PSF board\'s needs, then, anything PSF is overseeing.

    - And: PSF liked our YouTube video! [https://www.youtube.com/watch?v=B4GQCBBsuNU](https://www.youtube.com/watch?v=B4GQCBBsuNU)

    - Sumana says: get Sept invoices in ASAP

  - Sumana: reschedule Tuesday meeting & approve invoices, wrangled issues with Pradyun to sort out 20.3 and 20.2.4, and working on meeting minutes

- Pip backtracking & taking too long: info message [https://editor.nuboso.ei8fdb.org/0S2BEZAUTZCJCv089n94Jw?both#](https://editor.nuboso.ei8fdb.org/0S2BEZAUTZCJCv089n94Jw?both#)

  - Pradyun: there are 3 broad things that need to happen
    - 1: what exact threshhold numbers we should use when presenting \"we\'re taking too long\" \-- \"8 backtrack choices\" for instance \-- threshold how many decisions we say \"that was a bad choice\" about
      - Georgia: how long (clock time) do n packages/backtracks take? Each one could take unknown amount of time.
      - Pradyun: we could use clock time OR \# of backtracks as threshold.
      - Bernard: per notes from yesterday: tentatively decided \"after 8 backtracks\" for 1st message because 5-6 might be reasonable
      - Georgia: time expectations depend on the type of feedback you are seeing. Seeing SOMETHING changing/loading is an indication of progress.
    - 2: exact wording of message
    - 3\. LATER: what nice things we can do once we have better output

  - Bernard: ideally we\'d test this with users. we don\'t have time, so, going by discussion with maintainers, past data & experience. In messaging, give people a way to give feedback such as \"this message is confusing\" or \"that was way too fast\"

  - [https://files.nuboso.ei8fdb.org/backtrack-messaging.mov](https://files.nuboso.ei8fdb.org/backtrack-messaging.mov) \-- 43 seconds. Thanks Pradyun for sharing a \"prototype command line output\" tool! Messages in [https://editor.nuboso.ei8fdb.org/0S2BEZAUTZCJCv089n94Jw?both#Messages](https://editor.nuboso.ei8fdb.org/0S2BEZAUTZCJCv089n94Jw?both#Messages)

    - Message 1 - displayed after X backtracks
      - INFO: pip needs to download different package versions to find a compatible set to install. This could take a long time.
      - DECISION: we\'ll stick to 8 for this message.

    - Message 2 - displayed after Y backtracks
      - INFO: This is a complicated process. It may not be successful - to abort press keys: ctrl + c
      - DECISION: we\'ll stick to 13 for this messages.

    - To improve how pip performs, tell us why this happened here: [https://github.com/pypa/pip/issues/XXXX](https://github.com/pypa/pip/issues/XXXX)

  - Timeline:
    - Bernard: don\'t foresee any potential slowdowns/issues we\'d have around this.

- 20.2.4 and 20.3 planning - [https://github.com/pypa/pip/milestone/38](https://github.com/pypa/pip/milestone/38) milestone for 20.3

  - we\'re going to put out 2 releases this month.
    - 20.3 \-- second half of Oct.
      - This \"shiny new resolver\" release.
    - 20.2.4 \-- now-ish.
      - documentation and performance improvements that we\'d get out to users who\'re trying out the beta release.
      - needs commits/PRs to be cherry-picked onto 20.2.3

  - Pradyun: this is accurate. We need to decide which exact performance & docs improvements to add in. Add to [https://github.com/pypa/pip/issues/8511](https://github.com/pypa/pip/issues/8511) . Exact commits/PRs we need to add in.

  - Outstanding questions
    - Georgia to follow up on the existing issues that haven\'t been updated yet.
      - Concerned about some overlap/tangling between current discussions around backtracking output and some other UX issues discussed earlier.
    - should we have a 20.3 beta/prerelease?
      - no specific reason \-- Pradyun was uneasy about the changeover of flags (old to new default), is less so now [https://github.com/pypa/pip/issues/8937](https://github.com/pypa/pip/issues/8937)

- UX next 3 months (notes from Georgia, as I imagine we may not get to this in the meeting today)
  - We are wrapping up survey & interview data collection in the next few weeks, and are analyzing those results to share in a useful way for the team and the community

  - From there we expect to have some recommendations overall, as well as clear resource needs for the project that will be basis for the trainings

  - We can share a larger overall update next week if that\'s helpful
    - Yes! That sounds good!

- Prioritizing Pradyun\'s work
  - reviewing and merging PRs, mostly #8932

  - cutting 20.2.4
    - things to include: [https://github.com/pypa/pip/issues/8511#issuecomment-701325392](https://github.com/pypa/pip/issues/8511#issuecomment-701325392)

      - docs: #8942 (how to default to new resolver), #8807 (ux docs), and #8933 (index page about resolver and UX work)
        - additional docs suggestions:
          - [https://github.com/pypa/pip/pull/8829](https://github.com/pypa/pip/pull/8829)

          - [https://github.com/pypa/pip/pull/8561](https://github.com/pypa/pip/pull/8561)

          - [https://github.com/pypa/pip/pull/8927](https://github.com/pypa/pip/pull/8927)

          - [https://github.com/pypa/pip/pull/7859](https://github.com/pypa/pip/pull/7859)

          - [https://github.com/pypa/pip/pull/8873](https://github.com/pypa/pip/pull/8873)

          - [https://github.com/pypa/pip/pull/8780](https://github.com/pypa/pip/pull/8780)

          - [https://github.com/pypa/pip/pull/8795](https://github.com/pypa/pip/pull/8795)
      - performance:
        - [https://github.com/pypa/pip/pull/8924](https://github.com/pypa/pip/pull/8924)

        - [https://github.com/pypa/pip/pull/8926](https://github.com/pypa/pip/pull/8926)

        - [https://github.com/pypa/pip/pull/8912](https://github.com/pypa/pip/pull/8912)

        - [https://github.com/pypa/pip/pull/8839](https://github.com/pypa/pip/pull/8839)

  - implementing backtracking info message improvements

  - implementing work needed to flip the switch [https://github.com/pypa/pip/issues/8937](https://github.com/pypa/pip/issues/8937)
