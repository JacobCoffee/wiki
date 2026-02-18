# PackagingWG/2020-09-16-pip-mini-team-meeting

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

Wednesday September 16

Participants

- Bernard
- Nicole
- Georgia
- Pradyun
- Ernest
- Sumana

Agenda

- blockers & status

  - Pradyun: not blocked on anything else, would like to have a chat with UX to talk through resolver output situation. Help organize my thoughts.

  - Nicole: had to swap this week so hi! no blockers except: I am trying to post things to Reddit, don\'t have an account, new accounts blocked by some subreddits. Bernard is helping. Am promoting \"buy a feature\" survey. Almost 120 new answers since PSF blog post publication (yesterday). Interviews progressing. Outreach done to PyLadies to encourage more sign up to UX studies, as we have not interviewed any women yet!

  - Thank you to Bernard for covering interviews yesterday
    - TODO: Sumana to give Nicole some lines to film today \-- DONE

  - Bernard: everything cooking nicely! \[checking whether UX studies has had more signups\]
    - Since PSF blogpost went out we got 9 more (290 in total now) sign-ups

  - Georgia: catching up from trying to take off last week. ![:-)](/wiki/europython/img/smile.png%20":-)") working on tweet drafts. adding to a Notion page \[INTERNAL LINK, not public please\] am working on wording, templates. Working to finish that today. Next: provide to Ernest. Ernest can please edit! ![:-)](/wiki/europython/img/smile.png%20":-)")

  - Ernest: nothing. But: halfway through Sept. Please invoice for Aug. And it would be really nice if Sept invoices came by Oct 1st, to close out quarter.

  - Sumana: Made some changes in physical work setup recently (better space separate and standing desk!). Did some publicity work, and publishing the blog post. Pinged Randall Munroe (!!) to give us some love. Sending Nicole lines for the video, and planning to take next week off! Interested in setting some dates/deadlines about 20.3. Invoices please!
    - Next week: other people to run meeting and take notes

- Performance issues in the new dependency resolver - progress on developing benchmarks?
  - Pradyun: tried a few things. someone ran some stuff wth PyPy. next step: timebox and look at the benchmarks that PyPy posted, and see whether we can make that bit faster \-- then ping Sumana or Ernest to get further on \"figure out what \'fast enough\' looks like\"

    - looks like we are doing unnecessary network requests! if so, eliminating those will help a lot!

- UX presentation by Bernard on emerging research themes
  - this is in-progress so let\'s not publicly link it to avoid people making assumptions

  - this was based on the \"who uses pip?\" research survey \-- \"pip Research: Learning about our users\" ([https://saneuxdesign.survey.fm/pip-learning-about-our-users](https://saneuxdesign.survey.fm/pip-learning-about-our-users) )

    - note for the future: Sumana would love for us to have a unique name or ID number for each survey so we can refer to a survey (internally) unambiguously in the future

  - we had a pretty good completion rate

  - \"Python software user\", \"Python software maker\", and \"Python package maintainer\" categories made sense to participants, reflect reality, felt identifiable
    - Some people are, for instance, Python package maintainers but NOT Python software makers, as in maintainers who do a lot of community engagement but very little coding.
    - Majority of people who are \"Python software users\" are not \"classically trained\" \... the more the person understands about software, and the more \"classically trained\" they are, the more likelihood they have of understanding and trying to understand what pip does and how.

  - Most participants seem to use pip interactively. And only use pip to install Python packages.

  - A lot use it in an automated (CI/CD) and most don\'t seem to have any trouble with it \-- when there are problems in the pipelines, usually pip is a messenger saying there is a problem somewhere else

  - Majority never or rarely need to build software packages from source \-- people who did do that are mainly on Windows, because often packages are not avail for Windows, but this has gotten better. There\'s an academic in the States who has a machine automatically building Windows packages.

  - SOME POSSIBLE RESEARCH QUESTIONS about people\'s mental models (it may be useful to partition this by \"how many years have you been using Python?\" since issues in the issue tracker are usually from people with very little skill or a lot of skill in using pip and that probbbbbbbbably correlates with years of experience in Python)
    - what are reasons why pip might fail/error out?

    - what is the difference between installing a wheel and a source distribution? (reason to ask this: we want to get more people to want and publish wheels [https://github.com/pypa/packaging-problems/issues/25](https://github.com/pypa/packaging-problems/issues/25) and so we want more people to understand that downloading and installing wheels would be faster. Do people already know this? let\'s check)

    - what command-line args/flags can you use? what do they do?

  - TODO: Bernard to add Pradyun to the survey, since he\'d like to look at the responses to certain questions too!

  - TO BE CONTINUED NEXT WEEK \-- talk about \"security\"-related stuff, hashes on packages, etc., source code audits, etc., thinking about security integrity

- plans for 20.3
  - deferred to Zulip/GitHub conversation
