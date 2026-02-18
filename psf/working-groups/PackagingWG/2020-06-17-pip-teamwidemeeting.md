# PackagingWG/2020-06-17-pip-teamwidemeeting

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

Teamwide meeting

Wednesday, 17 June 2020

Participants:

- Bernard
- Tzu-Ping
- Paul
- Sumana
- Nicole
- Pradyun
- Ernest

Agenda:

- User experience report/discussion
  - Georgia said: \"we started some notes on what we think are the current asks from the devs and an overall idea of where we\'re planning to head that we\'d like to share / get feedback from the team at the next meeting\"
  - This is a list of what we think the devs have asked us to work on. Need help deciding priorities
    - Error Messages and documentation for the resolver (wrapping up)

    - Auditing verbosity of pip output,
      - long task, Nicole would rather do 10 messages a week, instead of trying to do all of them in one go

    - Do users expect/want/need pip to support a new flag called \--force-**install**?

      - This is a completely new flag
      - How urgent is this? Can we address this later?
      - Paul: my view: would rather we didn\'t have it - a bunch of work we haven\'t even looked at yet. But can we have any assurance that not having it is acceptable? My priority is: getting an answer to the question: is it ok to not do it.
        - Sumana: it is OK to put out a prod release in july where we say \"known change\" that we do not support force install
          - people may be relying on doing this even though it is not valid \... current resolver treats them differently \[Pradyun, could you repeat what you said here\]

        - Can we deliver the first release & say \"you haven\'t got it yet\"

          - Pradyun: this is basically the last bit of force installation in the how to deal with conflicts doc that Nicole wrote \.... 
          - TODO; Yes, we do want research Nicole: we need to do some research on it in the short term

        - current version of pip does not refuse to install conflciting requirements.

        - Pradyun: it\'s possible to tweak the result the resolver gives by giving a toplevel req - may not have same effect for new resolver

        - People may be working around problems existings with new resolver and they may need to disentangle workaround if they can remember to do that
          - this is a transition thing. new resolver works differently and you need to transition reqs to it
            - Pradyun: yes
      - Sumana: Offering a new option to force install and working through the design etc pre-emptively should not delay the beta. And we may not want it at all. Almost every reason whty someone would resolve it would be a resolver bug or a package problem.
        - Paul: if we did try to address this, reearch can\'t just be \"do people need it?\" we would need strong guidance on how they want it to work. There are no good intuitions we have found on how you would express what you are trying to get it to do
      - Should we create an entirely new flag? Beta is fine w/o

    - Current behavior of pip \--force-**reinstall** seems to be more like pip upgrade. Some inconsistency\.... Bernard has started on some research on what we expect pip force reinstall to do

      - How urgent is this?

    - pip command overlap/duplication: if 2 different commands do essentially the same thing
      - Sumana: Phase III (foundational research will help)

    - managing pip cache (from early discussion with Pradyun)
      - How urgent is this?

      - we\'ve since had `pip cache`{.backtick} added, and there\'s basically 1 more request-for-functionality; for time/size based trimming/search capabilities.

      - I don\'t think there\'s need for research on this anymore \-- it\'s now bounded/bottlenecked on dev-time availability.

    - pip check / pip list / pip freeze etc aggregation into a single command
      - How urgent is this?
        - Sumana: not able to acheive in next month, can be pushed back. 
        - Paul: Agrees,
        - TP: not urgent, although I would refer to Pradyun.
        - Pradyun: I don\'t feel strongly either way.  Ok to do it later.
        - Sumana: will benefit a lot from the foundational research
  - \[discussion of whether we are doing in depth specific research or general foundational\]
    - 
  - Planning work for next phase
    - Sumana: what time period? Phase III (June-Dec)?
      - TODO: Georgia to clarify

    - How it\'s decided on what feature to add next?
      - unclear how that decision making process currently works

      - Gets to the heart of the issue: temporary project with time-boxed funding and time vs. opensource project contributions

      - Sometimes the UX Team have had issue where the research question hasn\'t been specified. Sometimes they go on a wildgoose chase.

      - The Python packaging toolchain is underfunded, and volunteer run -\> they do work for community spirit, or they\'re motiviated (technically) to do the work

      - Sumana thinks that none of the individual tools under PyPA banner have buisiness process for making decisions or setting roadmap (strategy)

      - Also on a tactical level, these projects also lack procedures that are universally agreed on for specific PRs or accepting filed issues.

      - Is shaking things up or trying to establish some of these procedures worthy? Lead via UX research results.

      - Nicole: yeah, we want to formally establish \"there is no procedure right now, it is all ad hoc\" and then go from there. We had not seen any procedures at all.
        - Paul: I\'ll confirm that\'s true ![:-)](/wiki/europython/img/smile.png%20":-)")

        - Pradyun: I\'ve just been nodding in agreement to the entire discussion.

        - TP: everything mentioned is true

      - Clarification: No Formal process, not documented anywhere. Who needs to be involved to make any given decision.

      - [https://github.com/pypa/pypa.io/pull/54](https://github.com/pypa/pypa.io/pull/54) \-- documentation of how Python Packaging Authority Membership is determined.

        - Jo Freeman, Tyranny of Structurelessness
          - \[Sumana summarizes\]

      - Bernard: Can we document this? So we can acknowledge it.

      - TODO \# 1: document that there is no formal process

      - TODO #2: Conversation with all pip maintainers to resolve the question \"Is something more formal even desired?\"
        - when asking: do you want something more formalized? present Pros & Cons. Pros: if there is a more formalized decisionmaking process, gives us (UX) better insight re what to research. (and make life less stressed for the contributors)

      - Bernard: I can understand documenting how previous decisions were made \.... would this be useful for us to document the not-formal-process?
        - TP: Yes. Would be useful for new contributors to PyPA projects: document, some writeup on how other ? can come in and make contributions to projects. Guidelines/advce to follow
        - Nicole: case study
        - TP: offer current UX exercises as a case stufy of how pip works. maybe grow what is informal into a more formal process, documenting current existing situation is
          - Agreed - also how previous features/work has been decided on, e.g. the need for a new resolver, how the new resolver would be invoked.

          - Sumana: currently, we have this rough idea of what tphase 3 is. we have a bunch of thing we\'d like to get done \-- one of the things is documentation.

          - contribution guide \[note taker too slow\] contribution guide (techinical) vs what we want here \-- something that includes social guidelines, how much time back and forth is likely to take. rules of thumb for judgement, advice for.

          - Nicole: maybe name it something other than a contrib guide

          - Pradyun: I think \"contributing\" fits \-- [https://pip.pypa.io/en/stable/development/contributing/](https://pip.pypa.io/en/stable/development/contributing/) \-- it\'s what the page is currently called. We might want to rewrite/add to that. (maybe, just an idea)

    - Foundational User + Context Research 
      - Understanding more about who pip\'s users are (Personas, Contexts they use pip in, Mental Model --- basic info that can evergreen inform pip development). 
      - More exploratory and qualitative

    - Look in a lightweight way at other package managers (gem, npm, apt, etc) - perhaps we can leverage other contacts to do this work (?)
      - Bernard has had a look at some prior academic research on other package managers.

    - User Engagement as a Process for pip team 
      - how does the pip team engage with pip users? not just package maintainers, not just other Python packaging tools maintainers/contributors? Putting in place some process.

    - Tools, Guidelines & Practices for the dev team so that they know how to handle user input, when to do user research (and how to approach it), what they can/should use user research for, how to leverage the community effectively to inform development work  \... how does the pip team do their own user research? Using methodologies. What tools to use for what type of research. 

      - e.g. When & how to use GitHub issues, and how to frame them, example: Bernard tries to \[not sure of summary here\] Example: Should pip support force install? 

        - Transparency

        - Work tracking

        - Decision tracking tool \-- using GitHub as a decision tracking tool

        - User engagement

      - Nicole notes: we discussed how, if we \[?\] right now, how dev team makes decisions to prioritize what we work on in open source context, we want to understand how that decision is made, and how these tools could influence that process

    - Templates for GitHub issues \[connected with that\]

      - Support vs Design Discussion vs Research Discussion vs Bug/Code/Test
        - majority of existing templates are code-centric
      - Bernard has a start on this \[where?\]; Also look for good examples, e.g. OTF/hypha-ish, others.
        - hypha: Bernard is working on a different \[unrelated?\] project
      - Pointing people to better resources
        - e.g. user support policy
          - if you have these kinds of issues \... go here\... these issues go here\...

          - see example of bottom of ResolutionImpossible documentation as an example. reflecting Paul\'s comment re disclaimer, support resource limits.

        - in some cases people should not be opening issues on pip\'s GitHub repo, but on the repo of the package that they are having trouble with

    - Adding useful functionality to pip that would support a user 
      - hypothetical idea: adding pipdeptree functionality into pip
      - hypothetical idea: a pip conflict checker that might save the user from coming up against conflicting dependency issues
        - in response to: user research participant: was uncomfortable about loosening his toplevel requirements, \[more details\] wanted to be able to see all compat versions and choose from them.
          - there is an open source project called \"pip conflict checker\" - would this add the functionality the user was seeking?

        - this exists as `pip check`{.backtick}, for post-installation.

        - and pip install prints any conflicts before installing
          - possible to hypothetically have that functionality BEFORE installation? And provide option(s) that would solve the conflict.

          - Paul: pip check specifically tests whether what\'s installed remains consistent. Doesn\'t do the \"list the options that would have satisfied these requiremetns\". \....
            - Pradyun: Doesn\'t the new resolver solve this though? like, it\'ll find the corresponding compatible version?

            - Paul: I thought the requirement was, \"given pip install X\>2, pip will choose X v4, but the user wants to know that X v3 is another possible resolution\". For later discussion maybe?

          - Paul doesn\'t know of any tool that does this\.....

          - example: [https://gist.github.com/nlhkabu/a73a9a96fe292319919646ac62dbd56a](https://gist.github.com/nlhkabu/a73a9a96fe292319919646ac62dbd56a) - is something like this possible?

            - Paul: Possible, but I\'m not sure if resolvelib offers this level of information.

Paul: \"current asks from the devs\" - should we invite suggestions from the other pip devs not in this group?

- Yes, whoever needs to have input!

Pradyun: One thing I think, that might be missing: pip check / pip list / pip freeze etc aggregation into a single command (also related to the pipdeptree discussion).

- Bernard: will add this to potential backlog

- sounds fine to me. ![:)](/wiki/europython/img/smile.png%20":)")
