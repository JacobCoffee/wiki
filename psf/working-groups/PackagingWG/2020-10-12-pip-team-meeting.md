# PackagingWG/2020-10-12-pip-team-meeting

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

Tuesday 20 October

Participants:

- Sumana
- Georgia
- Nicole
- Pradyun

Agenda:

- Are these blockers? If so, who\'s working on them/what should we do next?
  - [https://github.com/pypa/pip/issues/8686](https://github.com/pypa/pip/issues/8686) Dependency resolution and improper handling of extras

    - Tzu-ping wrote: \"Another more personal note: I am hesitant to classify this as a pip bug. Although the described usage is well within the specification, I suspect it is against the intention of the extras feature, based on my interaction with people designing it. If that's the case, this would classify better as a feature request instead, and the resolution may be that we need to fix the specification to disallow the usage, instead of introducing the feature to support it.\"
    - therefore: post-release work.

  - [https://github.com/pypa/pip/issues/8713](https://github.com/pypa/pip/issues/8713) Pip downloads lots of different versions of the same package

    - Pradyun said \"In particular, I think the important parts for this issue, in the short term, are that we get the output correct, and communicate about these changes as best as possible (through documentation of the changes + workarounds, signal boosting etc).\"

    - We have a lot of documentation-support about `ResolutionImpossible`{.backtick} but not a lot about backtracking. Do we need it?

    - Should be covered by [https://github.com/pypa/pip/pull/9017](https://github.com/pypa/pip/pull/9017)

    - Do we need a doc to link to, from message as we do for `ResolutionImpossible`{.backtick}?

      - SH: I think so, yes.

      - 20.3 can contain a link that we can update a lot faster.

      - Pradyun: an additional idea: instead of linking directly to a page & anchor hash within page, use RtD redirect support, page-to-page redir, from \"pip.pypa.io/error-help/resimpossible\" -\> wherever we want. We can change structure of doc in future. Can update faster, even if we restructure the docs.

      - TODO - create at least a small placeholder document within pip.pypa.io & link to it in error message

        - Who writes the placeholder? \-- LATER DECIDED: Bernard

  - [https://github.com/pypa/pip/issues/8115](https://github.com/pypa/pip/issues/8115) Clarify and define install/upgrade behaviour for the new resolver

    - Not a blocker.
    - Sumana: but should we preemptively document to help support user questions post-release?
    - Pradyun: Current behavior is unspecified. Part of what Paul wanted is to document what we do today and how it works. Behavior is difficult to reason about. Behavior is almost the same in basically everything, same conditionals in the same places, I\'m inclined to think this would not be a big problem.
    - TODO: Sumana to move to post-release work
      - what we\'ll be documenting is quirks

      - corner cases where we deviate from de facto behavior\.... people depend on old behavior

      - we change how constraints files work when you use a requirements file - we error on things that used to be allowed.

      - Migration Guide, Documentation of current behavior \-- add to [https://pip.pypa.io/en/latest/user_guide/#changes-to-the-pip-dependency-resolver-in-20-2-2020](https://pip.pypa.io/en/latest/user_guide/#changes-to-the-pip-dependency-resolver-in-20-2-2020)

      - Georgia suggests: interview Pradyun & others about \"what will be gotchas?\" Fireside chat about migration. Some to go in migration guide, also a blog post.

      - TODO: Sumana to add some items to migration guide from this issue.

  - [https://github.com/pypa/pip/issues/8975](https://github.com/pypa/pip/issues/8975) How to improve information provided to users when pip backtracks

    - Should be covered by [https://github.com/pypa/pip/pull/9017](https://github.com/pypa/pip/pull/9017)

  - [https://github.com/pypa/pip/issues/8711](https://github.com/pypa/pip/issues/8711) local development and pip\'s 2020 resolver

    - This is resolved.
    - TODO: Pradyun: mark issue as resolved.

  - [https://github.com/pypa/pip/issues/9011](https://github.com/pypa/pip/issues/9011) Pip 20.2.4 goes into infinite resolution of dependencies

    - This is the one where we\'re saying \"the old resolver is the escape hatch\" OR this might be a bug.
    - Needs more investigation. Might be a bug. Pradyun will look further.

  - And: re: updating docs to say new resolver is default:
    - [https://github.com/pypa/pip/issues/8937](https://github.com/pypa/pip/issues/8937)

    - TODO: Sumana to update migration/pip docs
- Will we release pip 20.3, with new resolver as default, within next 2 weeks?
  - discussion deferred to next meeting
