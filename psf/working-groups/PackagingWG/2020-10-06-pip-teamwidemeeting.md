# PackagingWG/2020-10-06-pip-teamwidemeeting

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

Tuesday 6 Oct 2020

Participants:

- Pradyun
- Georgia \[left after first 30 min\]
- Sumana

Agenda: what do we now know and what improvements we\'ve made + what we can change \-- make a decision tree, and figure things out \-- and figure out if we\'re putting out 20.3 in October.

- Performance
  - [https://github.com/pypa/pip/issues/8664](https://github.com/pypa/pip/issues/8664)

    - Pradyun needs to review [https://github.com/pypa/pip/pull/8932](https://github.com/pypa/pip/pull/8932) and probably merge it

    - 8932:
      - to add infra for 8932 on the resolvlib side [https://github.com/sarugaku/resolvelib/pull/57](https://github.com/sarugaku/resolvelib/pull/57) - is in progress being reviewed \-- needs to happen on resolvlib side \... this logic is reusable and should be in resolvlib. Status quo \*was\* \"put the logic in pip\". Pradyun to talk with TP to discuss path forward.

      - would need to cut a resolvlib release, update vendored version in pip, update pip implementation \-- this would take at least a day, maybe longer. ORRRRR merge #8932 in pip \[first or instead\], which would be fastest.

    - [https://github.com/pypa/pip/issues/8664#issuecomment-702345229](https://github.com/pypa/pip/issues/8664#issuecomment-702345229) worst slowdown we saw is about 3x

  - on informing user when resolver is doing a lot of backtracking
    - Pradyun and Bernard spoke today, and have a rough idea \-- came up with a few ideas on how to present this, and Pradyun thought through how to implement it, what\'s doable, and now we\'re there in terms of spec, need implementation work + exact wording. We figured out where we want to print message, what info to present to user.
    - Question: is Bernard developing exact wording? \[we believe so\]
      - Georgia will confirm in the UX meeting. Relevant Etherpad: \[removed, not sure whether it\'s a public link\]

- releases & 20.3

  - how does Pradyun feel about new resolver as default in 20.3 in october?
    - we should be able to make release in second half of the month. Assuming we don\'t find a showstopper in a bug report in next few days

  - reviewing [https://github.com/pypa/pip/projects/5](https://github.com/pypa/pip/projects/5) and [https://github.com/pypa/pip/projects/6](https://github.com/pypa/pip/projects/6)

  - Q: want to spend a minute to talk about 20.2.4 later.
    - SH: I think there\'s been some fairly clear message about what should go into 20.2.4 point releases. [https://github.com/pypa/pip/issues/8511#issuecomment-701325392](https://github.com/pypa/pip/issues/8511#issuecomment-701325392)

      - about what should go in \-- exact PRs available (merged or ez-to-merge)
        - option 1: cut a release off 20.2.3
        - option 2: cut a release off master

      - There are docs PRs we really want to get out, and there are performance & general improvements we really want to get out. 20.2.4 including performance improvements: we\'d be able to talk to users who had perf problems and ask \"does this help?\"

      - BUT: this would be a point release \-- we have merged a few things into master that cannot go into a point release. So, what would work well: bundling docs & performance improvements into 20.2.4 with them. Doable. Lets us have all the positives we talked about. BUT, tiny concern: we may have to change/update the documentation about how to use the new resolver by default.

        - [https://github.com/pypa/pip/pull/8942](https://github.com/pypa/pip/pull/8942)

        - TODO: Sumana: write a ticket to write a PR changing docs about resolver migration/default/etc., and then we shall merge it just before cutting pip 20.3

  - More general bug triage from project TODO boards:
    - TODO: Sumana to ask Nicole about [https://github.com/pypa/pip/issues/7744](https://github.com/pypa/pip/issues/7744)

    - TODO: Sumana to note on [https://github.com/pypa/pip/issues/8683](https://github.com/pypa/pip/issues/8683) that this in progress, move card to correct column \-- also #8346 \-- DONE

    - TODO: Sumana to close [https://github.com/pypa/pip/issues/7871](https://github.com/pypa/pip/issues/7871) and explain with link to these notes \-- DONE

    - TODO: Sumana mark #8346 as not a blocker, explain on issue \-- DONE

    - [https://github.com/pypa/pip/issues/8076](https://github.com/pypa/pip/issues/8076) \-- Pradyun agrees that the \"escape hatch\" should be \"the old resolver exists\" but there is KIIIIIND of a legit use case where a dependency has declared \[certain requirements\] and I want to override. And there is precedent where other package managers do it. but in any case, this is NOT a blocker for 20.3 with new resolver being default.

      - TODO: Sumana to move out of blockers (DONE), and the bug reports in late Oct will tell us more about the use cases. Here we have 3 people saying \"we want this\"; need broader info for how much this is really needed and in which cases.

    - TODO: move [https://github.com/pypa/pip/issues/8307](https://github.com/pypa/pip/issues/8307) out of blockers and explain - remove from the board entirely \-- DONE

    - [https://github.com/pypa/pip/issues/8495](https://github.com/pypa/pip/issues/8495) will be very rare. Really 2 issues: 1 if there is a diamond dependency with a conflict at the end. We print the package\'s name twice. Not ideal but not a big problem. The other issue, which Dustin has flagged, is that advice is not actionable for certain kinds of users. Valid point. There is a relatively straightforward approach to fixing this which Dustin has suggested.

      - TODO: develop concrete wording for error message change.
      - TODO: Sumana to move out of blockers column \-- DONE. Pradyun says: nice to have this in 20.3 but I don\'t want to delay release for it. Nice to have in 20.3.

    - TODO: ask Nicole about progress and what\'s necessary regarding [https://github.com/pypa/pip/issues/8492](https://github.com/pypa/pip/issues/8492) \-- \"no blockers. status: need to make a PR for feature flag docs. Need to look into research question we will discuss later. If I have time this week, look into [https://github.com/pypa/pip/issues/8492](https://github.com/pypa/pip/issues/8492) to give user more info when they get [ResolutionImpossible](./ResolutionImpossible.html) error. Would be nice to have that in by 20.2. But most importantly, don\'t make the new resolver default before this is sorted.\" \-- quote from Nicole in July

    - TODO: Pradyun to talk with TP about [https://github.com/pypa/pip/issues/8785](https://github.com/pypa/pip/issues/8785) and figure out what we need to do next

    - TODO: Pradyun to review [https://github.com/pypa/pip/issues/8827](https://github.com/pypa/pip/issues/8827) , a bugfix PR that needs to be merged.
