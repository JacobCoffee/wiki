# PackagingWG/2020-06-24-pip-teamwidemeeting

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

Teamwide meeting

Wednesday, 24 June 2020

Agenda:

- Prioritize and finalize the blockers to the beta
  - [https://github.com/pypa/pip/projects/6](https://github.com/pypa/pip/projects/6)

    - 7871 - testing the new resolver - tracking issue for the remaining tests that are still failing. Needs to be finished before prod. Would love to have it before beta, but it will get finished by spinoff tickets. Paul\'s remaining paid work days are tomorrow (25th June 2020).
      - TP: FYI the count of `fails_on_new_resolver`{.backtick} in master is now 3, and all are actively being addressed.

    - Go through the list of how we communicated about Warehouse and start reaching out to them re: pip;  making blog posts at fairly visible locations (i.e. not my personal blog), possibly going on podcasts, well-timed actionable emails etc.  \-- this is Sumana

    - #8493 Add resolver docs  - in progress

    - What flag will users use to call new resolver? in progress in Zulip

    - Handle conflicts from installed packages when updating other packages  #7744
      - serious policy question. Approach 1 vs 2.

      - Paul\'s view: we should say: Pip only considers the packages being installed, and may break installed packages. Will not guarantee that your env will be consistent all the time. If you install x and then y, it\'s possible for y to be different than \"install x y\" in 1 command. That is, to me, how we should go. And is what we currently have implemented.

      - Pradyun disagrees. We should \"Pip considers all installed packages, and will not allow installation of an inconsistent set of versions to be present.\" . Have an escape hatch re dependency hell. The reason we aren\'t seeing \"we want that but with an escape hatch\" is that users don\'t have an escape hatch yet. And would be simpler to implement once we have the override mechanism.

      - TP: do we have a way to find out which behavior is more popular among pip users? Beneficial to have a \"strict\" mode for pip, so that packages are always consistent, but not sure which model should be behind the flag.

      - Pradyun: What we have right now: 2 implementations in master. The error msg people see when there is a conflict that they are dealing with takes them to a page we have written, and we say \"we think 1 would be another way to handle this, and would you like that?\" 

      - TP: strict \... and if that fails, direct user to documentation that instructs them to have a flag, like \--override. That is sort of where I think it would be nicer than running 2 commands and things breaking on the 2nd one.

      - Bernard: possible to ask user during process which would you like me to do?

      - Paul: people use pip in CI and similar places where there is no user far too often.

      - Bernard: could we ask user to say \"this is not interactive\" \.... unattended installs \.... in my experience, doing and researching, that is by someone who knows what they are doing. They can recover from something that the automation has done. Whereas: Somebody using it interactively \-- there\'s a real human there, so let\'s use them!

      - Essentially it\'s 2 different  modes of use: human intervention, and automation

      - Paul: the point at which we find out there\'s a question that needs to be asked: we are partway through the process of resolution or installation under 1 of these options. We are halfway through doing a strict install, find out it\'s not going to work, so asking user \"do you want me to not be strict?\" just as easy to error out and say \"try again with a lax flag\"
        - but The UX of asking the question and then doing the right thing automatically would be nicer
        - but historically, for expedience, we said \"we can\'t do it this way, try again\"

      - Bernard: I get that! UX of attended installs of Windows OS, and then finding out \"I could do this automated!\" So I write a little companion script that answres the questions it will ask me, and an option then changes, but then I can go check and say \"oh it hasn\'t configured this widget\" and I go fix that \.... 

      - What is the most common mode of use of pip? Attended or unattended? Human sitting in front of the screen or an automated situation?

      - We don\'t have numbers on that. Broader change we want to make to how we track info about installs, and we want to track that.

      - Paul: Probably fair to say that unattended installs are mostly in the majority, but

      - How many unique installs are attended/unattended?

      - every once in a while \[something\] is flaky - network blip, CI

      - it takes time for people to dig thru and find there was an issue. One of the great thing atbout attended is the human can see the output of what they just did

      - Let\'s also not assume that \"attended\" mode means that interactive is right. So \-- I would want to be considered as a CI system. I hate chatty software. I don\'t want pip to ask me questions. I am maybe in the minority.

      - Bernard: I agree, Paul. At the moment, pip is designed solely for that unattended usage, and if the #s shake out that 95% of pip usage is unattended, there\'s the 80/20 rule for majority. Then that design is fine. But it\'s still important that the 20% of the users - we also have accommodation, but they may need to do more work/answer more questions \.... pip doesn\'t know what to do. So 
        - Paul: pip doesn\'t know what the user wants \-- but because it\'s upfront, that means \"give them a command line option\" \... I get the idea of asking them questions \...

        - the mental model is pip needs to know inconsistencies instead of \<?\>

        - its also mpossible instead of asking at th beginning to make a guess about what the user wants and then go back and ask later on. guess something and apologise later

        - Bernard: if Pradyun, Paul, TP, team feels this is something they need input from UX, Bernard is happy to do some research on this, if it is a high priority.  Would be helpful to get input on the question I need to ask

      - Pradyun: Yes! Room for input here. I also think we should think about directing users who might want strict to be able to provide \"I want that\" inputs on that in the beta. Maybe involving CLI printout, something in docmenttnation\... but preserve the current behavior for now. 
        - Paul: so \-- we decide that, in the immediate term, we leave things as they are, but we reserve the right to change that decision based on feedback?
        - Pradyun: yes, but also we actively encourage user input here.

      - Paul: not particularly attached to any decision here. But if we go for (1) we need to allocate those resources; (2) is more expedient. So feasible to take (2) for now, but make people aware that it is not the final decision.

      - Bernard: is this something Bernard needs to do research on? No is the shorter answer. Longer answer - this is part of a larger research question (Unattended/attended installs), phase 3.

      - Bernard: should I open a GitHub ticket for this piece of research to say that \"this needs to be done but not in the short term\"? Yes

      - RESOLVED: Pradyun: and if we all agree with what Pradyun proposed? Yes!!
        - TODO: Pradyun to file a tracking issue, documenting this and what we\'re going to do here.

    - WIP: Do not upgrade the installed version when an explicit URL for that version is given            #8359
      - Paul - no longer sure of behavior of current master \.... need to clarify. Paul would need to do more work to see whether this is still an issue
        - Pradyun & TP: this test still fails on master
      - TP: \... made a new PR 8483.
      - OK, we may have a solution \-- in progress
      - moved to prod milestone

    - Write \"implications of this change\" document (migration guide like [https://warehouse.readthedocs.io/api-reference/integration-guide/#migrating-to-the-new-pypi](https://warehouse.readthedocs.io/api-reference/integration-guide/#migrating-to-the-new-pypi) to link to in release notes)

      - Sumana needs to develop this

    - Sumana: write announcement blog posts
      - Sumana needs to write

    - Sumana: create manual testing guide
      - PR exists - WIP

    - More verbose explanation why \"Could not find a version that satisfies the requirement\"            #6526
      - [https://github.com/pypa/pip/issues/6526](https://github.com/pypa/pip/issues/6526) - Maybe need to remind the user pip ignores incompatible distributions (data-requires-python, wheel tags, eggs, etc.); files they see on PyPI is not always installable

        - TP: current `ResolutionImpossible`{.backtick} message \.... the union of all the specifiers results in an empty set. But user may be confused if they do not think it is an empty set! Version 1.0 with only wheel for Windows. They install on Linux and pip will not select a Windows wheel and we do not know why. Address in REsolutionImpossible message

        - Bernard: is this a case, like with RsImpos, where we can add some documentation to explain that situation?

        - TP: probably \.... not exactly sure how we can tackle this\.... without outputting links that users will ignore \... 
          - Sumana: do we need to address this before beta?
          - TP: people don\'t complain that much right now

        - Pradyun: before prod but not beta

        - Paul: fact that diagnostic info given is poor is not new. Less a new resolver issue and more about longer term UX work. Can defer it into general UX improvement.

        - Pradyun (over chat/text): Maybe we need \"no compatible versions on this platform\" or something like that?

        - Paul: pip doesn\'t have this info at the time of running into the error, so this will not just be a few hours of work. Collecting info needed to debug will be hard. User could look at a bunch of stuff on PyPI 

        - Bernard: I\'ll open a ticket for this \*but will need help understanding\*! 
          - Maybe you can reuse the existing ticket? 6526

    - 6628 Declaring extras in constraints file installs also extra dependencies even if not instructed to            #6628
      - before beta: We just need to document what\'s up 

  - [https://github.com/pypa/pip/projects/5](https://github.com/pypa/pip/projects/5)

    - what flag will we use? in progress in Zulip

    - Add note to changelog about how we are handling constraints. \-- Sumana is making progress

    - Write documentation for ResolutionImpossible error message      #8459 \-- in progress, discussion in Zulip since Nicole is not here

  - Anything that isn\'t on the board yet?
    - Bernard: Georgia: TP, Paul, Pradyun: nothing from me
    - Ernest: no, but reallyenjoyed listennig to interactive vs noninteractive usage conversation.
    - We are reaching halfway point, we have an oppotunity to consider publicity around what\'s been done, what progress has been made, where we are standing with funding, where we plan to go. recognizing that the world has been a weird place this year. Board and community would be interested in a summary in the last 5.5 months
      - TODO: Ernest & Sumana - might take an hour to do a writing sprint on this

- [https://github.com/pypa/pip/issues/8492](https://github.com/pypa/pip/issues/8492) - is this something we can do with remaining funding? - Nicole

  - Sumana: yes, in Phase III

  - TODO: Georgia & Sumana to talk about a work plan for Phase III

    - Wait for a week or 2 til SaveInternetFreedom campaign calms down (Bernard: +1)

      - [https://saveinternetfreedom.tech/](https://saveinternetfreedom.tech/) for more info

      - [https://www.theguardian.com/media/2020/jun/18/voice-of-america-independence-fears-after-trump-ally-purges-senior-officials](https://www.theguardian.com/media/2020/jun/18/voice-of-america-independence-fears-after-trump-ally-purges-senior-officials)

      - [https://www.nytimes.com/2020/06/23/us/politics/michael-pack-global-media.html](https://www.nytimes.com/2020/06/23/us/politics/michael-pack-global-media.html)

  - Paul: Pradyun did some work on visualisation - is that likely to be relevant?
    - Might be!

- TODO: \[outside of call\] Please review Nicole\'s latest documentation for ResolutionImpossible. Pull request in progress: [https://github.com/pypa/pip/pull/8493](https://github.com/pypa/pip/pull/8493)

  - please try to do this by the end of your workday today

Let\'s try to get this beta out by the end of June!

Also: Pradyun, TP, Paul, and Bernard are speaking on a podcast tomorrow! Test & Code
