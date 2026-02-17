# PackagingWG/2020-08-19-pip-teamwidemeeting

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

Wednesday 19th August

Participants:

- Georgia (not available, but left notes in advance)
- Bernard
- Pradyun
- Sumana
- Nicole

Agenda:

- Nicole:
  - Can we pay for [https://matomo.org/](https://matomo.org/) for 3 months (for the pip docs)?

    - How much money?
      - 100 euro or USD for 3 months
      - Looks like 49 EUR/month for \~1,000,000 views/month (pip sees around 300,000 views)
    - GA Suggestion/Note: PSF uses Google analytics on other platforms, so maybe we can use Google Analytics on the docs as well and connect with a different property-id to the same account? Matomo is better from a privacy perspective, but might be easier to just use tools PSF is using elsewhere.
    - Pradyun\'s notes:
      - pip\'s docs don\'t have any analytics beyond what is provided by RTD today.

      - we could opt into Read The Docs\'s beta for analytics \-- [https://pasteboard.co/JmYdTbP.png](https://pasteboard.co/JmYdTbP.png) shows you a screenshot of the current analytics from Read the Docs (without the beta feature)
    - Conclusion:
      - TODO: Pradyun to opt in to RTD beta. Nicole to ask Jan if this is enough. If not, we will fall back to Matomo.

  - FYI, we are going to add an email link to the pip docs for collecting user feedback. See \# Ernest - can we have a PYPA email for this?
    - GA: We have `pip-research@simplysecure.org`{.backtick} or we could make a group on pypa.io, e.g. `ux@pypa.io`{.backtick} or `.org`{.backtick} ?

    - TODO: Sumana to ping Ernest about this

  - To discuss - collecting feedback via UI (in documentation)
    - Forthcoming [GitHub](./GitHub.html) issue.

    - Would be nice to be able to collect data from users using documentation.
      - Iteration 1: an email link for \"was this helpful to you\".
      - Iteration 2: a widget so they can submit while reading docs. Can we get funded dev time for this? probably no. Can we ID someone in community who can work on this with us?
      - TODO: Nicole to follow up with Eric about this

- [https://github.com/pypa/pip/issues/8714](https://github.com/pypa/pip/issues/8714) UX design: what should pip output when it is backtracking during dependency resolution? #8714

  - Need to develop a plan of action.
  - Want to be done w/ UX research by end of Aug
  - Potential workflow
    - Pradyun develops a few options/examples (mockups)

    - UX team provides feedback on this, based on best practices and experience.
      - no feedback loop w/ users.

    - Nicole: Not ideal, but reasonable

    - Bernard: Given the constraint of time, it\'s \[best/good\]. Pradyun, please only mock this up (don\'t implement it in code). Low fidelity is better ![:)](/wiki/europython/img/smile.png ":)")

    - Sumana: \"sketches\", not prototypes.
      - If I can think abotu what a decoration might be, two distinct approaches (examples of decorations)

    - Nicole: depends on verbosity.
      - Poetry presents no output.
      - Give just a small amount of information - e.g. what version is being tried and if it is rejected or accepted. (Thanks!)

    - Bernard: information hierarchy and verbosity
      - This is a difficult situation, because there will be somebody who will want to see all of the information all of the time.
      - Most users only care about \"worked\" vs \"didn\'t work\" \-- question of verbosity. provide the least amount of information (we can test that w/ people) \-- if it\'s missing information, we can add it in. if we add more thing, people will be less inclined to suggest removing bits.
      - Minimal is better at the beginning.
      - verbosity: give a lot of information / give a little
      - sequence: stage the process is going thru, and which components the user really needs details on. e.g.
        - stage 1: high or low verbosity: Is it important for the user to know about this? That it is happening, or what the details are?
        - stage 2: high or low verbosity: is this important to the user or not? Maybe not \-- maybe it\'s more pip internal. Log to a log file, but don\'t display on screen.
        - stage 3: high or low verbosity: maybe this is very important for user to see
        - end: high or low verbosity: maybe this is very important for user to see

    - TODO: Pradyun to make 2 mockups by early next week (\~24-25th)

- [https://github.com/pypa/pip/issues/8664](https://github.com/pypa/pip/issues/8664) New resolver: What performance is acceptable, and are we there yet? #8664

  - Pradyun: I think this is closely tied to [https://github.com/pypa/pip/issues/8380](https://github.com/pypa/pip/issues/8380) (`ResolutionTooDeep`{.backtick} error).

  - Pradyun: I will be posting more thoughts in a comment on #8664 (what performance is acceptable) issue \-- not done yet. ![:(](/wiki/europython/img/sad.png ":(")

    - `ResolutiontooDeep`{.backtick} happens when pip is trying multiple options because of conflicts. Ths is closely tied to being perceived as too slow. The heuristic we need to figure out to determine when we are taking too long will inform the error message, and vice versa: feedback from users on when pip is too slow will help us set the threshold. We are not 100% sure of how to determine the threshhold for too-slow perf or trying too many options and being slow.

  - Bernard has a question: Is this connected to the number of iterations the resolver goes thru resolutions? Previously (from memory!) it was set to a \"low\" (hundred?) number, it was then set high (millions?).
    - Was 100, is 2,000,000 now. [https://github.com/pypa/pip/pull/8275](https://github.com/pypa/pip/pull/8275)

  - Sumana: yes to bernards question, it is directly related. It is the cut-off point. Changed to 2M. The more attempts we go thru the greater the chance of finding a proper resoluton, but also there are things that pip does that people perceive to be slow. the spikeyness of taking long to do something is because of that threshold. PG is interested in not pulling decisions out of nowhere and choosing a number to set this to. What are the benchmarks we should reach for good performance. We\'ve been gathering data on what performance users are getting.

  - S did a test on her laptop and it took 100% more time in some cases to update something. We\'re gathering artisanal data - we need moar data!

  - Start by putting together manual speed tests to compare how fast the new one is vs old one.

  - based on that we decide a level of speed that is acceptable - that will then help us drive improvements. \<audio cut out, missed this bit\> make the decision. S. has some thoughts - we take some data from surveys and interviews - what are the computer setups of people that currently use pip.

    - Bernard: we don\'t have this data (from memory) BUT we can put together a survey quickly also Jetbrains surveys have OSes used by python users
      - Jetbrains survey got many thousands of responses.
      - Bernard suggests that they could put together a survey quickly
      - Good question! Data Pradyun would need for benchmarks:
        - the packages (We can grab some requirements.txt from GH)
        - the network speed
        - hardware is less of a problem
        - TODO: Nothing! UX team don\'t need to make a survey!
      - Sumana: please link to a unified document of all the current surveys \-- is now in the notes (look in previous weeks)
        - Nicole - here it is: [https://www.notion.so/simplysecure/b46a0992ba8548cf988200cb2a02636b?v=beba10f184b647aa87c207e832f645b4](https://www.notion.so/simplysecure/b46a0992ba8548cf988200cb2a02636b?v=beba10f184b647aa87c207e832f645b4)

          - Thank you!

  - we figure out how we can replicate on any machine we have access to. then, grab requirements.txt files (from issues, from [GitHub](./GitHub.html)). PG makes something to do A/B speed tests.

    - This gives us quantitative information about how much slower pip is. Let\'s assume we get information that\'s similar to what we see today (\~400% \-- 3 times slower). pip maintainers+UX folks discuss if this is OK.
    - Maybe we decide this is fine. Maybe we need to iterate a bit \-- \"may be fine but isn\'t\"
      - Basically, decide \"What are we OK with?\" \-- in clock time or %-age.

  - Bernard has a question: after the pip resolution has started, can we prompt the user after X period of time to ask \"do you want me to keep going\"?
    - back to the \"interactive mode\" problem \.....

    - also, is time the correct \"thing\" to measure \-- eg: I have a slow network and am downloading tensorflow ( \>300MB ) ![:(](/wiki/europython/img/sad.png ":(")

  - Bernard:
    - This seems like a really reasonable approach, particularly as we are not able to test every permutation
    - We will need some communication explaining that pip is being more responsible, but it will be slower. Here is how we are testing this problem to try to find a good compromise.

- Bernard: about advertisement of our main UX studies signup form
  - TODO: Ernest to speak with Betsy. Sooner rather than later. Does not need to be highly coordinated.
  - We need some signal boosting done. We currently have 262 signups. An increase of about 20-25 over the past 2 weeks.

- Incentives for research participants (Notes from Georgia)
  - A potential participant asked about incentives, which is something we do like to do, but isn\'t explicitly in the budget currently.
  - Incentives don\'t need to be directly financial (and actually this can be quite challenging to manage!)
    - Ideas:
      - Stickers (a pip contributor sticker, e.g. !PyPI contributor sticker?)
        - Could ask Stickermule for a donation here, and then it\'s just the cost of sending it out to people
      - Listing people as contributors
      - Financial
        - Giving people money for their time, OR

        - Giving people discounts for PSF things, e.g. PyCon ?

        - Vouchers for other services, e.g. VPNs, Password Managers, etc (Simply Secure can check on our source for this, but these are donated and could be in chunks of 1 month - 1 year potentially)
  - Question
    - Do we want to provide an incentive for some contexts, e.g. feedback from people with disabilities vs any participant?
    - Do we want to have a participation threshold prior to recognition with an incentive, e.g. an interview over 30 minutes, X number of surveys?
  - Guidelines/contexts:
    - [SimSec](./SimSec.html) has used \$25/hour as an interview incentive for general user interviews, and more like \$150/hour for expert interviews (e.g. specialized knowledge)

    - Design Justice Network recommends \$5/survey, \$50/hour for an interview or focus group (or equivalent, e.g. food/other resources)
      - They also recommend the idea of some comparative value trade, e.g. an hour donated in return for something, if money isn\'t an option.
  - SH: how many people?
    - Nicole estimate: maybe 10 people per research epic?? so 40 people? + whoever we have already interviewed (Bernard: 15-25 people.)
    - How many people would we incentivise?
      - Good practice: everyone.
      - Longer answer: depends on how much time they\'ve given to you.
        - example: 50 GBP if they took a 6 week long diary study (\~15-20 minutes each day, over 4-6 weeks). another 50 GBP if they took part in a closing interview (1-2 hours) \"in-depth questioning, experience\"
        - In the case of an OSS project, the contribution doesn\'t necessarily have to come w/ an incentive (fundamental premise) \-- suggested changes taken up is part of the incetive.
          - You\'re making a \[positive\] change to this project.
        - Ideally:
          - for people who took part in surveys, we\'re able to give them a limited-supply sticker.
            - higher count (relative to the next one)
          - who uses pip / user disability / nicole\'s interviews / \[missed a few\] \-- small voucher/discount?
            - small count
    - Some things are free for us.
      - eg: Listing people as contributors.
  - TODO: SH to talk to Georgia about this + budgeting.

Note for next meeting:

- Pradyun got access to limesurvey surveys today (includes pip resolver feedback), and will go through the responses over the next few days. He\'s expecting it\'ll surface \"bad\" experiences.

\[end of meeting\]
