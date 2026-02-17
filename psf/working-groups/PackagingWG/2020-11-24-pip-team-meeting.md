# PackagingWG/2020-11-24-pip-team-meeting

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

Wed 24 Nov

Participants

- Pradyun
- Sumana
- Bernard
- Georgia

Agenda

- 20.3 release
  - [https://github.com/pypa/pip/milestone/38](https://github.com/pypa/pip/milestone/38)

    - #9011 is the blocker.

    - a patch that needs to be vendored in, for Mac OS Big Sur & new PEP support

      - what\'s realistic re Pradyun\'s work availability on weekdays\.... some availability and capacity

    - 8011 - big discussion\.... Pradyun will merge PR before release, will deal with any fallout from that

  - timing
    - Monday Nov 30th - the last day of November
      - how do we mitigate risk re infinite resolution looping thing\....
      - need help from Tzu-ping
      - TODO: Sumana to make a personal ask \-- OBVIATED by TP\'s work

  - pip resolver survey response updates
    - TODO: Bernard to refresh from last week
- prepping for UX training
  - [https://wiki.python.org/psf/PackagingWG/2020-09-30-pip-teamwidemeeting](https://wiki.python.org/psf/PackagingWG/2020-09-30-pip-teamwidemeeting)

  - [https://wiki.python.org/psf/PackagingWG/2020-09-29-pip](https://wiki.python.org/psf/PackagingWG/2020-09-29-pip)

  - from Bernard-Sumana conversation
    - 10-15 participants who are key contributors - that would be a happymaking number for Sumana
    - pip has a group of \~6 active maintainers, and then there\'s the larger group of \~40 people who are pypa maintainers (some crossover)
      - mailing list: pypa-committers
      - setuptools, wheel, twine, etc
    - Logistics:
      - Cluster of timezones?
        - Mostly NA + Western EU
        - Tzu-ping, frostming (sp) --- Taiwan, Japan (maybe) \-- CORRECTION, China
        - Maybe some in Australia
        - Pradyun: \"Seems like 4 people outside of Europe/NA out of all 72.\"
          - 72 people in the PyPA, including very low-frequency contributors and people who only have triage powers.
          - Sumana suggests: there are about 40 people who work on maintenance tasks, even sporadically
          - Pradyun: maybe 20-25 people.

      - Day time contributors vs nights & weekends contributors?

        - Most people aren\'t being paid to work on the tools

      - in poll, understaand 4-hr vs 2-hr chunks

      - combo of prerecorded plus live workshop
        - maybe workshop comes first?
          - workshop before pre-recorded could be more effective
            - do - watch - do would be very effective.
          - live session recording
            - interactive workshops wouldn\'t translate well to video
            - presentations would be effective
            - toward providing multiple ways of folks (and/or style choice)
          - Multiple formats toward being more accessible to more folks

      - discussion of offering dates in Dec plus Jan
        - SH: grateful that SS is flexible.
          - don\'t want folks to do volunteer work that they should\'ve been paid for.
        - GA: this for us is also a way to get feedback from this community
          - it\'s part of the work we do
          - we\'re happy to do it \-- we\'d rather make sure it\'s a workshop that\'s accessible to as many folks as possible, regardless of contract end dates.

      - Outreach
        - Framing the value relative to a UX course \-- and pointing out that this is bespoke, won\'t come around again, rare, valuable as professional development
          - Bernard: \"a generic UX 2 day course would be £2000.\"
          - Tailored to pip/pypa/python frame
          - Easier to access in reasonable sized time frames (2-4 hours vs 2 days)
        - Value proposition around having a common language to talk about pypa/pip as products, with a user-centered frame
        - get peer leadership from respected PyPA folks
- CZI convening \[December\]
  - would be great if Nicole could attend just the docs working group
- Analytics - may talk about it today
