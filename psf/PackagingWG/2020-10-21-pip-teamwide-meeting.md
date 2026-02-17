# PackagingWG/2020-10-21-pip-teamwide-meeting

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

Wednesday 21 October

Participants

- Bernard
- Sumana
- Pradyun
- Ernest
- Georgia

Agenda:

- #8713: Pip downloads lots of different versions of the same package
  - From yesterday\'s meeting \"we need documentation\"
    - Proposed: [https://editor.nuboso.ei8fdb.org/s/SJZgHFTPw](https://editor.nuboso.ei8fdb.org/s/SJZgHFTPw)

  - Also like to propose:
    - helping the user remove the packages pip backtracks through.
      - Better solution to this is improving pip cache

  - Paul gave comments - [https://python.zulipchat.com/#narrow/stream/218659-pip-development/topic/blockers.2Fbug.20triage/near/214045901](https://python.zulipchat.com/#narrow/stream/218659-pip-development/topic/blockers.2Fbug.20triage/near/214045901)

  - Ernest: pip should probably present the message before downloading 8 packages.
    - GA: This is a good point and good feedback!
    - Ernest: We should present the message immediately when backtracking the choice, the first time (i.e. at first backtrack).
      - Bernard: we\'d discussed this at some length during the initial discussion and kind-of pulled this number out of the air.
      - B: Don\'t think presenting a message that pip \"might\" do something.
      - Sumana: show \"this could take a while\" message after the 2nd backtrack
        - Pradyun: We have n = 8, we can change it to 1 \-- I think it\'s reasonable and a good change for all the reasons Ernest has mentioned.
        - TODO: Pradyun to add an n=1 threshhold to display the initial info message

  - Next steps:
    - Pradyun and Bernard to discuss what possible solutions users can try to - [https://editor.nuboso.ei8fdb.org/b7-Q2qrdTom5KTMZGXEoNA?view#Possible-solutions](https://editor.nuboso.ei8fdb.org/b7-Q2qrdTom5KTMZGXEoNA?view#Possible-solutions)

    - Bernard to make PR.
      - Markdown-to-rST
        - Sumana suggests using pandoc

        - Pradyun: if you\'d like, feel free to look at [https://pradyunsg.me/furo/reference/](https://pradyunsg.me/furo/reference/) for A/B differences between them?
      - can possibly get this done this evening
      - ideally: merged in tomorrow
- Note: Next week is Daylight Savings for parts of the world! Just to flag the meeting time might change for some folks, and not for others!
  - Ah fun.
- Will we release pip 20.3, with new resolver as default, within next week?
  - [https://github.com/pypa/pip/projects/5](https://github.com/pypa/pip/projects/5)

    - [https://github.com/pypa/pip/issues/8664](https://github.com/pypa/pip/issues/8664) performance

      - TODO: Sumana: We\'ve not mentioned that people should try pip 20.2.4 in the issue \-- DONE

    - Requirements with (potentially conflicting) options [https://github.com/pypa/pip/issues/7846](https://github.com/pypa/pip/issues/7846)

      - legacy pip has inconsistent behavior.
      - TODO: defer to post-release \-- DONE

    - [https://github.com/pypa/pip/issues/8495](https://github.com/pypa/pip/issues/8495) & [https://github.com/pypa/pip/issues/8492](https://github.com/pypa/pip/issues/8492) New resolver error message is confusing if a package has inconsistent dependencies

      - currently being iterated.
      - TODO: Pradyun to make a comment
      - Georgia: we have survey feedback and are thinking through the best way to deliver what we can
        - Nicole is planning to post the synthesis from the survey on the issue.
        - so, when will this be a merged PR? We\'re not sure.
        - Sumana: urgency
        - TODO: Georgia: will check with Nicole, follow up, unblock. Thinks it is pretty close
          - team has been looking at and synthesizing survey results

    - pip editable install with new dependency resolver fails despite correct version numbers #8785
      - \"next step here is for \@uranusjr and \@pradyunsg to have a chat about what to do next.\"
      - They talked, but Pradyun needs to talk with him again to come up with a solution.
      - TODO: Pradyun to move conversation to issuetracker so it is visible

  - [https://github.com/pypa/pip/projects/6](https://github.com/pypa/pip/projects/6)

    - covered in other discussions

  - [https://github.com/pypa/pip/milestone/38](https://github.com/pypa/pip/milestone/38)

    - Question about [https://github.com/pypa/pip/issues/8333](https://github.com/pypa/pip/issues/8333) Check in prepare_linked_requirement for an existing directory is setuptools-specific #8333

      - Does Pradyun need to do anything about this?
      - DONE: Sumana tried to delegate to others \-- Paul will try to take a look

  - So: yes. Let\'s try to release Wed or Thurs, the 28th or 29th.
    - Pradyun: feels good.
      - date sounds fair. Maaaaaaybe a beta on 28th or 29th if we can\'t manage a stable release on 28th/29th. if we have 1-2 outstanding PRs/issues.
        - Sumana: and then a stable release the subsequent release, in early Nov.
    - Georgia: feels good
    - Bernard: feels good
    - Sumana: neutral

  - TODO: Sumana: start drafting announcement blog post(s)/email(s)/tweet(s)
- Early November - US may have civil unrest, let\'s reduce what we ask of our US people that week
  - Simply Secure is aiming to not have any meetings on Nov 3rd + 4th to allow everyone flexibility

  - TODO: Sumana to braindump some \"things to do immediately after release\" thoughts into Zulip or GitHub for Pradyun to use in case he needs to step up in her stead

  - TODO: Sumana to ask Bethanie to reschedule Nov 3-4 meetings, but NOT to Nov 5-6 (Bernard)\... perhaps do Monday instead?
