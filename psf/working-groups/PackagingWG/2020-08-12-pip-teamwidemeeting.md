# PackagingWG/2020-08-12-pip-teamwidemeeting

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

Wednesday 12 August

Participants: - Bernard - Pradyun - Sumana - Ernest - Georgia

Agenda:

- status/blockers
  - Invoices on their way!!!

  - Bernard - fine \[shared update in Zulip\]

  - Georgia - fine

  - Nicole - not blocked (as far as Georgia+Bernard know ![:)](/wiki/europython/img/smile.png ":)") ). Pradyun would like to make more progress with her on backtracking issue\.... Pradyun will work with Bernard

  - Pradyun - made 20.2.2 bugfix. Next: triaging issues. Lots of support tickets\.... NEXT WEEK, talk with Sumana about using automated testing to find likely bugs/problems in upstreams
    - Have we recieved any responses to survey #989272 that we need to route over to Pradyun?
      - Not looked at in 2 weeks \-- we can give Pradyun direct access? Yes\... as long as personally identifying information isn\'t made publicly available.

      - Pradyun: when transferring issues to [GitHub](./GitHub.html), anonymize

      - TODO: Bernard to give Pradyun direct access

      - \"don\'t expect it to be a firehose\"

      - 

  - Sumana - Have put some time toward spreading the word (Twitter + personally to people/media institutions). \"Some dent, not enough\".
    - Thinking about: What else can we do?
      - \"earned media\" \-- people to notice what you\'re doing and talk about it.
- \"who uses pip\" research update
  - [https://github.com/pypa/pip/issues/8518](https://github.com/pypa/pip/issues/8518)

  - Bernard: I put together a intial survey speaking w/ Nicole, about how we were going to do this research. Initially, thought of multiple surveys \-- doing a single one instead (less logistical work).

  - Pip disabiliy usability + who uses pip survey (single, combined)
    - Initial \"shallow\" knowledge from the survey + asking about a 20-30 minute interview?
    - First part: About you \-- how long have you been using pip, what do you use it for, and so on.
    - Second part: If pip users have any kinds of disability? What effects do those have on their usage of pip? + Assitive Technologies (usage w/ pip or Python)
      - Kinds of disabilities (in this context): Motor/Visual/Hearing/Cognitive.
      - Important to understand, since they have an impact \[snip\]
    - Piloted w/ 65 people?
      - to check that there\'s no offensive language/references etc
        - got 8 responses. Nobody said it\'s offensive.
        - sent to accessibility folks I know personall.

      - Have n? people willing to have a longer call \-- scheduling now.

      - 210 people more will be contacted (i.e. who are signed up for \"i want to take a survey\")
        - panel

      - List of surveys, in progress: [https://www.notion.so/simplysecure/b46a0992ba8548cf988200cb2a02636b?v=beba10f184b647aa87c207e832f645b4](https://www.notion.so/simplysecure/b46a0992ba8548cf988200cb2a02636b?v=beba10f184b647aa87c207e832f645b4)
    - 3 personas
      - Python software user, or
      - Python package maintainer, or
      - Python software maker
    - automated usage of pip (CI) vs interactive usage (command line)
    - Too early to give any large understand (6-8 responses yet)

  - request to advertise it as widely as possible
    - We need to get more people to sign up for the UX Studies panel (instead of sending out this particular survey to everyone)\... more organized and structured approach.

    - In general, in wide-ranging publicity, let\'s get people to sign up for the panel. In a few limited circumstances, we will direct specific audiences to specific surveys, e.g., in `ResolutionImpossible`{.backtick} error message. But that will be the exception.

  - Sumana: want to write the script for the video over the next few days (ideating right now, thanks for the inputs)

  - Using sponsors
    - PSF Sponsors should get a heads-up about new pip resolver (like PyPI\'s roll-out) to test it.
    - signal-boost it?
      - Ernest: agree! Likely needs co-ordination w/ Betsy.

      - Sumana: turn-around time?

      - Ernest: assuming \[bunch of things like content are done\], a week?

      - Sumana: There\'s [PyCon](./PyCon.html) sponsors and PyPI sponsors\... \[pradyun is slow note taker\]

        - Ernest: there\'s 2 or 3, overlap otherwise.

      - TODO: Sumana: de-duplicate and provide a list of all these companies, to Betsy

      - Ernest/Sumana: might be worth to see/repeat what we did for the PyPI rollout

      - Ernest: that might be the best avenue (via the Packaging WG, Ernest to nudge Betsy to take this forward)

  - Where would be the dream places where it would be great to get attention for this?
    - Georgia: might be worth asking PSF staff about getting a better sense about good comms channels, toward answering this question.
      - Ernest: we don\'t have an analysis/lists for something like this.

    - TODO: Ernest to look at Blogger\'s metrics/analytics on the recent pip blog posts on PSF blog and blog.python.org (where it got shared) and similar.
      - Looks like we have \*no\* analytics anymore, since it got overhauled on Blogger\'s end.

    - Google Trends - check it out to see who is talking about pip and where

    - Bernard: has gone to [AdaFruit](./AdaFruit.html), [CoderDojo](./CoderDojo.html), Raspberry Pi Foundation, emailed their mentors/community and explained \[context and ask\]. We need people who are respected and well-known in these communities to say \"let\'s do this because it will benefit us\" What we need essentially: people in different communities who have \"respect and trust\" of those communities to advertise it.

      - Different places we can go to advertise: we have a good idea. But we need respected people to vouch for us

      - some ideas: developer.moz, Twitter/Google/Facebook/ Amazon, Jira/Atlassian developer relations, Jetbrains,

      - disability association (and \"tech. usage subgroups\" - I\'m contacing disability organisations in UK, IE), \"respected/famous\" Python developers (Guido [WassHisName](./WassHisName.html)?!)

      - would be nice if tech celebrities would tweet it

    - TODO - Sumana to follow up on Zulip today
- 20.2 cycle, bugfixes, etc. going through early October
  - Basically done, I think. Can do more (20.2.3 and so on) if we have things to change/add.

  - Pradyun will be assiduous about placing relevant issues in the To Do Before Prod column in the [GitHub](./GitHub.html) board on the resolver rollout

  - TODO in a 1:1 call Pradyun-Sumana next week: look through that column and start to see the road to October
