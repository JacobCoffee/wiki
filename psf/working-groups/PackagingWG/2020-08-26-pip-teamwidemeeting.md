# PackagingWG/2020-08-26-pip-teamwidemeeting

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

Wednesday 26th August

Participants:

- Pradyun

- Georgia

- Sumana

- Nicole

- Bernard

- The Uber Conference AI-bot ![:)](/wiki/europython/img/smile.png ":)")

Agenda:

- PG: We have a bug report that 100% needs fixing before prod.
  - [https://github.com/pypa/pip/issues/8792](https://github.com/pypa/pip/issues/8792) \-- hashes in the constraints files

  - This needs a few decisions/tasks (do we implement this? what should the behavior be? what would be the \"shape\" of the actual implementation PR be?)
    - probably doesn\'t NEED UX inputs since it\'s mostly a case of \"we didn\'t think of this while making it and someone depends on this behavior\"

  - This will be another thing to document as behavior of constraints.

  - FYI that Pradyun will be working on this - we need to document and communicate about this
    - TODO: determine whether this is different than old behavior, and document somewhere on pip.pypa.io, maybe migration guide

- PG: Would it make sense to roll out the fast-deps feature ([McSinyx](./McSinyx.html) GSoC project) along with the resolver?

  - Would make the dependency resolution process faster, since it\'s doing a metadata lookup via a partial download (instead of the entire file).

  - I realized we could do this when reading the survey responses. I don\'t recall if I brought this up before. ![:)](/wiki/europython/img/smile.png ":)")

  - What options are we considering?
    - a\) roll it out in 20.3
    - b\) go through more usual deprecation/rollout process, start with warnings for users, etc., and then it would be early next year (21.0) it would be default or avail or users, or flip the switch in 21.0 or 21.1 and see whether users complain
    - Bernard: Ask users for their thought? Description. Would this be useful? How soon would you want it? If it\'s not a priority for users, then we can do it later, or not at all. If it is a priority for users, we can prioritise it accordingly.
    - Sumana: how much time would it take to ask this quetion?
    - Bernard: a couple of weeks or three
    - Sumana: that\'s in calendar/clock time. How much time would it take in terms of our time? Sumana: my guess - a few hours between PG and the UX team.
    - Georgia: is there any reason to uncouple it from the resolver work as a whole?
    - Pradyun is trying to figure out wheterh to couple this work to the new resolver (it mght help performance). It is adding another new behavious to pip - this may make it more difficult for users to understand, and for the pip team to maintain it.
    - It might be a good time to make this change as we are already maiking \"big\" changes.
    - If the resolver work is a big feature, is this a small piece of this larger feature and so would it make sense for it to be part of it.
    - Is it possible to release it as something with a flag, so we can follow-up with people who have performance issues.
    - Pradyun: this is currently available to users under a unstable feature flag.
    - Bernard: in which case, we ask people to test it!! Particularly people who have performance issues! We write a blogpost/post somewhere explaining the performance issue (why this has happened, and here\'s a way to try to improve it)
    - Georgia: we could include this in the resolver feedback loop.
      - Pradyun: So, that\'s step 1? I agree.

  - TODO: Pradyun: a place to ask: Github issues about performance issues, ask them to try fast-deps.

  - \[had connection issues\]

  - Bernard: In terms of time, for something to have users express their opinions \-- an hour.
    - Ideally, a very small number of questions (1 or 2) \-- this thing allows you to do X/solves Y, is this something that you want? want now, sooner or later?
    - Who\'s analysing that? Bernard says not me, suggests Pradyun.

  - resolved \-- Nicole is working on this with Bernard - pip functionality epic

- NH: Can we get any dev time on [https://github.com/pypa/pip/issues/8783](https://github.com/pypa/pip/issues/8783)? Or can we ask community to help with this specific ticket? Would like to collect data ASAP.

  - Add email link on pip\'s documentation
  - SH: yes. Maybe ask Yeray? Sviatoslav (@webknjaz)

- NH: Thank you to dev team for providing feedback on pip functionality surveys! ![:D](/wiki/europython/img/biggrin.png ":D")

- podcasts
  - FLOSS Weekly Wed Sept 2nd - every Wednesday morning at 9:30am Pacific, 12:30pm Eastern - via Skype
    - Sumana + Pradyun, Georgia as alternate

  - realpython.com [https://realpython.com/podcasts/rpp/](https://realpython.com/podcasts/rpp/)

    - Georgia is open!

  - Design podcast that\'s starting - Georgia may have an in there!

- Incentives - Follow up
  - Stickers --- If [SimSec](./SimSec.html) pursues making stickers, is there a preference about process? e.g. facilitating a conversation about a logo for pip?

    - Platypus? [https://discuss.python.org/t/the-packaging-platypus/1939](https://discuss.python.org/t/the-packaging-platypus/1939) [https://monotreme.club/](https://monotreme.club/)

      - various people: Platypus is adorable.

    - there\'s also the PyPI logo. We could do sticker packs

  - NH has drafted a survey for input on a design brief. preview: [https://forms.gle/RkEDuf1LBB19PosW9](https://forms.gle/RkEDuf1LBB19PosW9)

    - Sumana: Cool!

    - Pradyun: I like. No idea what we\'d get as \"inspiration\" \-- really curious to how this goes.

    - Stakeholders who need to approve: pip committers & triage bit holders. And then PSF\'s Trademark people

- NH has a PR open for the UX Docs addition: [https://github.com/pypa/pip/pull/8807](https://github.com/pypa/pip/pull/8807) (Thank you Nicole!)

  - online RST editor: [http://rst.ninjs.org/](http://rst.ninjs.org/)

- FYI NH has reduced availability starting September (5 hours per week, limited to Tuesdays)
  - [SimSec](./SimSec.html) team is working out the plan here, but hoping to free up more of Georgia\'s time to be more involved.

- One thing \-- PG: I need to do the drafts for Resolver backtracking thing.

\[end of meeting\]

Pradyun\'s notes from looking at the feedback survey (989272)

- TODO: Pradyun to figure out what to do with these notes I\'m not sure where to put these so that we can easily discuss these

- I made the HTML thingie (^\>^), then found that the \"expanded table\" doesn\'t contain the entire response. Using a mix of both those.

  - [https://gist.github.com/pradyunsg/91060eb4e6b9f424f78b5b990ef466fb](https://gist.github.com/pradyunsg/91060eb4e6b9f424f78b5b990ef466fb)

- Issue 1: Circular dependencies
  - [InstallationError](./InstallationError.html): Could not determine installation order due to cicular dependency\" (also note the typo)

    - TODO: fix the typo

  - \"improved logging and reporting about why different actions are being taken\"

- Issue 2: Resolution process is confusing?
  - \"it hangs trying to work out a compatible set of requirements\"
    - This is about system feedback about what it is doing right now.
  - \"New pip resolver fails to find the compatible set of dependency
    - It\'s logic based. Maybe it doesn\'t exist! It has printed the resolution impossible. -\> No action needed.
  - 44: \"the way it figures out seems weird\"
    - What is weird? Why is it weird? -\> Action: Ask the person what they mean by weird.
  - 60: \"More user feedback while dependencies are being resolved would be nice.\"
    - -\> Action: Ask the participant what more they want to see.

    - what command can I run to see dependency resolution output?
      - What is the current dependency resolution output? What does the user expect to see? And what is missing?
  - \"It seems like it\'s no longer going to install conflicting packages, but instead it hangs trying to work out a compatible set of requirements.\"
    - This is about a lack of system feedback - The user wants to know (at a high level) what is the system doing during this time. And if it fails, why it has failed (at a high level. e.g. cannot install tea - depency conflict due to coffee)
  - \"I would expect it to send an error instead of looping\"
    - system feedback, and it not being clear what the end point is, or when it will occur.

- Issue 3: hashes in the constraints files
  - User filed [https://github.com/pypa/pip/issues/8792](https://github.com/pypa/pip/issues/8792)

  - The way functionality in pip intersects is so awesome. There are never edge cases. /s

  - PG: Almost definitely needs to be done before prod IMO.

  - -\> Action:deal with this in the GH issue they\'ve opened.

- Issue 4: Speed ![:(](/wiki/europython/img/sad.png ":(")

  - \"Never had any issues with the old resolver, but the new one is more than 5 times slower.\"

  - \"for an installation pulling in \~40 packages, it may have been up to 2x slower. This is still better than some very slow installations I\'ve encountered with other package managers \"
    - PG: lol no. we\'re like, an order of mangitude worse than conda\'s resolver (which is SAT-based, and written in C)

  - Q: \"In your opinion, what needs to be improved?\" A: \"Speed\"

  - -\> Action: Send this person the information about fast-deps. Ask them to try it again with fast-deps and report any improvement, or lack there of. :).

- Issue 5: inconsistent \"invalid wheel\" error
  - Seems like a bug in fast-deps \-- might be fixed in master. Need to check.

- \"the range-based retrievals of wheels seem to work fine with Artifactory, which is good\" \-- \\o/

- Want to reach out to:
  - Response 86: how did they run pip, and could they share a minimal reproducer for the issue?
    - -\> Action: no action needed.
  - Response 136: \"pip resolver will break many builds in the scientific community.\" \-- why?
    - -\> Action: Reach out to them and ask why?
  - Response 174: does not include entire error message (or clarity about the error). \*maybe\* reach out and as what\'s up?
    - \> Action: Reach out and ask them to explain this further.
