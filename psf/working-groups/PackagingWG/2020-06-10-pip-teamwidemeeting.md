# PackagingWG/2020-06-10-pip-teamwidemeeting

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

## Teamwide meeting 

Wednesday, 10 June 2020

Participants:

- Sumana
- Pradyun
- Georgia
- Nicole
- Tzu-ping
- Paul
- Bernard

Following up on TODOs from previous meetings:

- TODO: Tzu-Ping to finish and merge Ilan\'s testing work.

- TODO: Sumana: set up next 4 weekdays of optional collab time

- TODO: Sumana to follow up on this (inform the team: who pip users are, what they want, etc. all research we can cather/what format would this be most useful to share this) with examples

- TODO: separate call about this (planning for rollout).

- TODO: Nicole & TP: agree to add a \"please report this to the pip issue tracker\" prompt to the error message

- TODO: Re: ResolutionImpossible - add \"please report this to [https://github.com/pypa/packaging-problems/issues/](https://github.com/pypa/packaging-problems/issues/) \"

- TODO: team to finish this change (\"some small changes that would be low-cost and radically improve the UX\"/\"easy formatting and info layout changes\" recommended by UX) within the next week.

- TODO: by next week, we\'ll have some basic docs published. We\'ll have a placeholder up soon

- TODO: Re: \"how do we pass tasks to UX folks?\" - follow up, Sumana - Bernard - Georgia - Nicole

- TODO: Sumana: followup on ballooning meeting time

Agenda:

- Availability:
  - Nicole working Monday and Friday (instead of Tues, Wed) for the week starting Monday 22nd June (back to normal after that week)
  - Pradyun - \[private\]
  - TP will be largely unavailable this week (other occupations), but should be back at half-time next week (15th until the end of the month)

- TODO followups (above)
  - Tzu-Ping to finish and merge Ilan\'s testing work.
    - TP has not had time to do this, has an idea of how to work on it. Will do first thing next week

  - TODO: Sumana to follow up on this (inform the team: who pip users are, what they want, etc. all research we can cather/what format would this be most useful to share this) with examples
    - still needs followup with UX

  - TODO: separate call about this (planning for rollout).
    - still needs followup - Sumana

  - TODO: Nicole & TP: agree to add a \"please report this to the pip issue tracker\" prompt to the error message

    - Re: ResolutionImpossible - add \"please report this to [https://github.com/pypa/packaging-problems/issues/](https://github.com/pypa/packaging-problems/issues/) \"

    - team to finish this change (\"some small changes that would be low-cost and radically improve the UX\"/\"easy formatting and info layout changes\" recommended by UX) within the next week.

    - piggyback off Bernard work (see later in agenda)

  - TODO: by next week, we\'ll have some basic docs published. We\'ll have a placeholder up soon
    - prep for the beta - still needs followup - Sumana

  - TODO: Re: \"so: no new UX research on these 2 issues,\" - \[Sumana to finish taking notes on what she said\] (oops!)
    - still for Sumana to do

  - TODO: Re: \"how do we pass tasks to UX folks?\" - follow up, Sumana - Bernard - Georgia - Nicole
    - to followup - Sumana & UX

  - TODO: Sumana: followup on ballooning meeting time
    - Sumana TODO

- Resolver \"readiness\"
  - may decide to defer this\...\... we don\'t have a dashboard/list representing the state of the resolver, checking off \"we\'re done and now we are beta ready\" \... we have a rough feel, but no concrete list of things left. How close to almost there? boards are out of date\..... flag this, we have to do it, more than discuss

  - Paul: did a brief review earlier today & posted a summary on Zulip. mostly, looking at how close we are to sorting out the remaining tests. we have 2 real categories

    - test message output differences (UX team discussion later\.... we should decide how to handle implementation details. how can tests deal with differences)

    - constraints \-- we have deliberately chosen to implement specifier constraints. change in functionality compared to the existing resolver & implementation in that. Assuming we don\'t change our minds over that decision, we need to figure out how to deprecate old functionality, catch usage and warn users of deprecation

  - other that, we don\'t have a clear list of what else might be outstanding. Lack of a checklist makes it uncertain

  - TP: I think I have 1 more: how we report hash error, in case download fom PyPI doesn\'t match hash, raise an error? error msg in legacy resolver is difficult to do in new resolver. Figure out how to do that. Main thing TP has on this checklist\.... not sure what the best format is for such a checklist. I\'ve used a few ways to write down what is failing, what\'s been solved/done, but none of those work very well. Would be nice if someone had better ideas on how to organize this. (TP: I'm currently using HackMD [https://hackmd.io/TkGB1hPQTcu9y_4JwAtGyA?view](https://hackmd.io/TkGB1hPQTcu9y_4JwAtGyA?view) )

  - Sumana: here\'s what I would suggest: the resolver is a piece of work that has various stages \-- whether or not we \"expose\" the state of the resolver to the user (we have current \"unstable\" in the master branch; it\'ll be default in the future). we\'ve had some discussions we\'ve had about what criterion to use. This sounds like a GitHub project board. (can make issues/PRs/independy card)

  - TP: should we make new issues for each failure?

  - Sumana: can make cards without issues.

  - Paul: we shouldn\'t have all the error as separate issues/cards.

  - Pradyun: there are some cases of feature requests for the resolver that we have deferred till we get beta feedback, like relaxing constraints or ignoring them, whether show came from \... those fit in

  - Sumana: those fit in the next column

  - Paul: I think we don\'t want to have focus on fixing remaining test failures\... that is a nice bounded problem. one card that says \"sort them out\"\.... we do need a way to track the other stuff that keeps coming up and never getting addressed, like \"how do we handle the rollout process\". Where we need to make a decision and everyone is waiting for someone to make a decision.
    - TODO: Pradyun, Sumana, and Paul, collab time tomorrow morning to create this

- Resolver flag
  - Pradyun: I will be making a detailed post on Zulip later today, asking for inputs.

- TP posted some improvements to the resolver issue template and hopes Nicole could take a look [https://github.com/pypa/pip/pull/8329](https://github.com/pypa/pip/pull/8329) Nicole: Thank you TP, will look today ![:)](/wiki/europython/img/smile.png%20":)")

- Error message testing findings and recommendations [https://editor.apps.ei8fdb.org/s/rylD-Qp3L](https://editor.apps.ei8fdb.org/s/rylD-Qp3L)

  - \[Bernard walks us through, including [https://www.notion.so/Testing-scenario-6e6b3910a22c40418cb7b1271588e33f](https://www.notion.so/Testing-scenario-6e6b3910a22c40418cb7b1271588e33f) testing scenario\]

    - The error message being tested is at the bottom of  [https://github.com/pypa/pip/issues/8377#issuecomment-638776768](https://github.com/pypa/pip/issues/8377#issuecomment-638776768)

    - Paul notes: Paul says \"\~=\" is a very rare construct and very rarely seen/used

    - Red text on practically any background has bad contrast. The problem was observed by participants of many ages. The word \"Error\" might be in red but not all the rest of the text

    - Paul notes: \"Just a technical note: Constraints are supplied by the projects being installed - it\'s not something pip has control over.\"

    - If we were able to create a page about the specific type of problem they have, the more specific, the better.
      - Bernard tested a slightly genericized (still specific to the type of problem) documentation page, with the particular packages and version #s removed, and it was still helpful to users

    - Disclaimer to remove?: \"This documentation is **not** meant to act as a list of PyPA agreed best practices or recommendations, but rather an attempt to help users who find themselves stuck and are unsure what steps they can take to solve their problem.\"

    - Bernard is almost done with this document

  - Followup questions:
    - TP: We can add a space between the comma-separated version parts, would it help?
      - Yes!

      - TODO: add space in comma-separated parts.

      - [https://editor.apps.ei8fdb.org/s/rylD-Qp3L#Questions-Comments](https://editor.apps.ei8fdb.org/s/rylD-Qp3L#Questions-Comments) 

      - Technical notes: We need support from pypa/packaging

    - OK to link to all of these documents publicly in the notes, on GitHub, etc.?

      - Yes!

    - The forking solution within \"A package that you are using has requirements that are too strict\" \-- ideological reasons for this?
      - if we do that, let\'s be clearer about Empowering Users!
      - \"explaining to users how to request the package maintainer\" \-- good idea!
      - Nicole suggests: say first, it\'s a good idea to request from maintainer, and then if project is dormant or doesn\'t have time, you have the ability to do it yourself.
      - Paul: question of the audience.  Some of these folks don\'t understand a version specifier because it\'s difficult to read
      - how do you help people at lots of levels of experience\....
        - Georgia suggests an approach: skimmability for the right audience. If you were to go overinclusive on documenting for your newest user in a way that\'s effective, then format it so it is approachable and skmmable by expert, like a \"TL;DR\" section at the top of any documentation page\.... useful strategy \.... but having more detailed docs
        - Big docs overhaul stuff unfortunately phase III \.... let\'s \..... parcel out what to do in this particular page, here, now, good enough for beta, from the big docs overhaul in Phase III
      - Pradyun: Forking has (negative) consequences, and we want to explicitly mention in the process the pros and cons and when is best to do this.

    - Force install information seen as confusing \-- ideological reasons for this
      - Pradyun: I requested this: there have been requests for this functionality, but it introduces signif complexity in implementation. we don\'t want to add it till we know there is a rea pool of users who wants this. 

      - Paul: by overriding the wishes of the pkg maintainer, you are doing the same in principle as with forking. You are explicitly opting out of support from that pkg maintainer. So it\'s important that we understand pros and cons in people\'s ninds about why they want to do that. Give people tools & let them use them, but maintainer\'s point of view, users saying \"what do I do now, having used this flag\" \-- packaging community may lack resoures to support people if that becomes a common thing to do

      - TP has a wonderful solution, but the page margin is too narrow
        - I got this reference! \[face emoticon\]
        - Fermat\'s Last Theorem joke! :-D
        - you could have a tool to let users fork \[?\] \.... a followup tool conversation!
          - Oh no no no no. :0
        - TODO: let\'s have that conversation

      - Should this be briefly explained, and then suggest they request this feature open a GH issue?

      - TP: people who want these will ask anyway \.... if they don\'t ask explicitly, with current wording of error msg, they will file an issue on issuetracker \..... if override is right solution for them we can figure that out \..... TP is more in favor of removing that part

      - TODO: Let\'s work out the wording in GitHub - Bernard

    - the \"**not** meant to act as a list of PyPA agreed best practices or recommendations\" - policy reasons for this? No - this was just Nicole trying to avoid bikeshedding.  Also not clear how something becomes \"official\" doc

      - Pradyun: pip maintainers \"bless\" it. ![:)](/wiki/europython/img/smile.png%20":)")

      - Paul: Personally, I\'m not too keen on \"blessing\" practices like this\...

      - Pradyun: exactly why I suggested/agreed to having this. ![:)](/wiki/europython/img/smile.png%20":)")

      - Paul: does not like giving people advice in this way, support issues, maintainability\.... if we start saying \"you could try this\" then when something goes wrong, user will come back to PyPA to ask for advice.
        - strongly in favor of a disclaimer. But I do understand why the users \*want\* this.

      - Bernard: understand the political side of this. But from user\'s POV: very experienced users, maintainers of packages: I understand why it\'s there, but I\'ve used an official Python tool (pip), I\'m coming to the PyPA documentation, I kind of expect that these are suggested\... official\....
        - Pradyun: political leads to logistical?

      - Bernard: nobody expected this would solve their problem completely. I don\'t think having this disclaimer helped. from past experience, I\'ve seen users are blind to disclaimers. users don\'t expect that the docs will 100% solve their problem\.... the framing purpose of the docs are helpful.

      - Nicole: we can control language - don\'t use \" should \" \... say \"you could try x, y\" \-- suggestion, rather than \"should\"

      - Paul: I get what you\'re saying, I stay very strongly in the favor of a disclaimer, to protect the maintainers.

      - Sumana: how important/urgent is this?

      - Bernard: \[note taker was slow\] second or third tier. Prefer to focus on error message.

    - Error message: Paul: all the principles are implementable and \-- when will we get more concrete stuff?
      - Bernard is fleshing them out

    - \[from HackMD\]

    - Pradyun: (regarding `~=`{.backtick}) I do think we should use a different scenario in the error message example in docs, which has more common operators (`==`{.backtick},`&lt;`{.backtick}, etc). It might make sense to separate out the explaination of version specifiers.

      - Paul: Error message is based on the user\'s exact issue. Do you mean the documentation here?
        - Yes! \*hides face under pillow\*
      - I\'d say the same scenario, but without the \"\~=\" operator.

- \* \* Paul: Just a technical note: Constraints are supplied by the projects being installed - it\'s not something pip has control over.
  - Pradyun: red is a well-established color for error messaging. nearly all development tools use red to denote failures. I guess we should move the bulk of the reading part away from red. :/
    - TP: One thing I just noticed in some tools is they only color the \"ERROR:\" header, not the messages themselves.

    - In agreement \-- that\'s the same thought I had in the second sentence. ![:)](/wiki/europython/img/smile.png%20":)")

    - Bernard: yes. \"Error\" labels red: fine. Helps red-green colorblind people. Rest of the error text should be in default color

    - Sounds good! \[happy face emoticon\]

  - Pradyun: Thank you for changing to more generic message; generating a page for the dedicated user issues is\... not feasible on the techincal front with how pip\'s docs works today AFAIK.

  - Nicole: what do we want to do about the force install section in the docs? \[addressed above\]

  - discussion of \"ToBeAdded - `1. <, <, 2.`{.backtick} left to right - lower to higher\"

    - TODO: this would be deferred to packaging lib - Sumana to re-open the issue and explain

    - [https://github.com/pypa/packaging/issues/312](https://github.com/pypa/packaging/issues/312)

  - Sumana: user research is great - a culmination of all the work we have been doing together \\o/

  - Paul: thank you Bernard for doing this work - it\'s confirmed a lot of what we knew and have discussed ![:)](/wiki/europython/img/smile.png%20":)")

  - Bernard: when all user interviews are published please read the notes, it will give everyone great insight into our users

  - Pradyun: thank you Bernard!! ![:)](/wiki/europython/img/smile.png%20":)")

- Ballooning meeting times:
  - Sumana: now I know UX findings discussions take about an hour.
