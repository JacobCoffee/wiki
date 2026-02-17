# PackagingWG/2020-12-02-pip-team-meeting

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

Wednesday 2 December Participants

- Ernest
- Sumana
- Pradyun
- Bernard
- Georgia

Agenda

- 20.3 responses from our public
  - Ernest offers to jump in and moderate any \"particularly spicy responses\"

  - Discussion of some responses, [https://twitter.com/pradyunsg/status/1333917512069689350](https://twitter.com/pradyunsg/status/1333917512069689350) \... Georgia notes: given the infrastructural level of change, we\'re more likely to hear from a \... \# ? of people \.... will only hear from a few people who are highly impacted

    - Great! Now we know who you are! How can we hear from you in the future?

  - Consensus that the current level of response is about what we expected, and a validation of the beta, work, testing, and outreach this year
    - Pradyun heard some people who said \"you didn\'t do enough\"
    - TODO: Sumana to round up positive responses

- CZI agenda for next week
  - [https://bit.ly/EOSS20](https://bit.ly/EOSS20)

  - Keynotes --- we could divvy up

  - networking/unstructured time we should be represented at - we can divvy it up

  - Demos --- seem to be more light lightening talks

  - Workshops/interactive sessions --- seem like we should aim to all be at

  - Each pressie has Q&A (would we be able to ask pip related questions? Probably not - only 5 min of Q&A per demo.)

    - A better way might be\...the text chat, the unstructured time (\"Hi! I\'m from pip, come talk to me\")
    - Sumana, during the pip demo/presentation, will invite people to come talk to the pip ux team
      - contact all the attendees by email to \"book a time to talk with the pip UX Team\"
        - who will do this?
          - TODO: Sumana to look at email vs chat options, ideally, send this to all meeting attendees by Monday
            - GA Comment: My guess is slack will be easiest/best based on the channels that exist. I don\'t think we can \"reply-all\" email to the attendees.
        - for response interviews: divvy this up between Bernard, Nicole, and Georgia
      - Bernard to put together a short script for questions
    - Attending presentations:

  - (i have a tiny thing to say) - Pradyun
    - have permission from team lead to attend entire thing
    - will probably have to skip most demos because of time (evening); will attend unstructured time

  - Bernard: Do any of the projects look like ones that Bernard/Georgia/etc should look at/attend in particular?
    - Pradyun: Not sure\... since the presentations will be more about the project use and less about the packaging of the project.
    - Sumana: Maybe focus on ones that came up or were mentioned in interviews/surveys.

- 20.3.1 and 20.3.2 planning & triaging issues

  - Issues to consider: [https://github.com/pypa/pip/milestone/43](https://github.com/pypa/pip/milestone/43)

  - Pradyun: will cut a release with what\'s on master at the moment. Help PyCharm. Update milestone to 20.3.2, and then\... not 100% sure what we want to get out first

  - 2 UX issues:
    - [https://github.com/pypa/pip/issues/9186](https://github.com/pypa/pip/issues/9186) 20.3 fails to resolve NumPy pre wheel name properly

      - a break due to Anaconda changing names of wheel files in their nightly index. Pradyun thinks we could improve the error message
      - TODO: Pradyun will propose a better error message later this week, then check with UX team to validate

    - [https://github.com/pypa/pip/issues/9181](https://github.com/pypa/pip/issues/9181) - straightforward to fix, need to update an error message

- deprecation timeline & 21.0

  - need to delay ripping out legacy resolver support
    - \[discussion of whether to rip out sooner or later\]
    - at some point in December we can assess whether we want to delay deprecation of old resolver to 21.1
    - Georgia: We were originally slating to release resolver as default in July. So maybe the six months window should be preserved. Think about how much time we planned for the transition. People who had breakage will probably address it quickly. But maybe give folks the courtesy of the window we had previously planned for
      - Bernard agrees
      - We should maintain that window\... what people expect, size of the window they normally have
      - respect established pattern
        - Sumana: we established a deprecation policy of \"1 release\" so we would take it out in 21.0, January
        - Bernard: on a regular basis: \"you\'ve got 1 month to make sure you are able to use new resolver\"\... every week, announce that. In January, see if it\'s possible to run a really simple survey: have you made sure your workflow, packages, etc work with the new resolver? And then do it, if it\'s possible.
      - Very hard to know how many people thought they would have a six-month migration window
      - Georgia: Part of December and January is holidays in many places\... some have a code freeze in December. Maybe that\'s a reason to delay past January. January is also busy for Lunar New Year, wedding season in India. Many companies don\'t operate at full capacity.
        - Pradyun: most major companies have a separate insulated rollout for these sorts of things. Big companies are less worrying than existing FLOSS projects and their maintainers.
        - Georgia: holiday season, plus the non-normal ness of this time (2020, pandemic) \... March might be a good window
          - but would defer to how the bugs are - fixable vs insurmountable
          - but any of it is reasonable
    - Pradyun: fine either way.
    - Sumana: can wait, and assess in late December whether problems brought up were actually easy to fix
  - DO NOT need to delay ripping out support for Python 2 since they are already only using legacy resolver
