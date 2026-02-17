# PackagingWG/2018-04-02-Warehouse

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# Warehouse Sync-up Meeting 

Monday, 2 April, 2018

## Present: 

- Laura
- Sumana
- Mark
- Nicole
- Dustin
- (Ernest absent)
- (Donald absent)

## Blocked/working on/announcements 

Nicole:

- Cross browser testing - opened issues related to IE 11 - less than 3% of users affected

- Sponsor page - **blocked**: waiting for last logos? - need \[sponsor\] logo \-- Logo needed by April 9 (at latest) to not block rollout.

- working on user testing - we find it very unlikely that user test issues will be blockers for launch

- not available first week of May (1-4 May)

Dustin:

- working on digging myself out of a pile of emails
- working through PRs for merging

Laura:

- updated legacy API docs; reviewing PRs
- Help Nicole with user testing

Sumana:

- unavailable late Thurs and part of Fri; may be unavailable for a day in April

- lots of communication work

- need an OK on the TLS announcement [https://github.com/pypa/warehouse/issues/3293#issuecomment-377934325](https://github.com/pypa/warehouse/issues/3293#issuecomment-377934325) \-- need to tell Mac users on 10.13 to upgrade pip . Can \@ThePSF retweet?

Mark:

- FB and NLNet grant proposals submitted. \\o/
- Burn rate updated: \[document\]
- Should be able to announce \[infra\] Credits this week, but still awaiting the transparent logo. Ernest did ping our contact; has not replied yet.

## Proposed April schedule 

Context: we have very few open issues blocking us from launching/redirecting and shutting down legacy, and want to shut down legacy this month so we have a few days in early May to fix things while we\'re still available, pre-PyCon, have budget, etc. And Ernest is unavailable this week so we should not launch/redirect this week.

1.  Sunday April 8th: TLS 1.0/1.1 removal [https://github.com/pypa/warehouse/issues/3411](https://github.com/pypa/warehouse/issues/3411)

2.  Monday April 9th: a one-time mass email to all PyPI publishers who haven\'t published a new release since July 1 2017, telling them: \[*we don\'t have in-PyPI infrastructure for sending emails to subsets of users* *(check with Ernest?) - let\'s draw a tighter box around dates, only emailing publishers who HAVEN\'T published a release since mid-2017 but HAVE published a release in the past several years - discuss specific daterange on IRC*

    1.  we\'re in beta
    2.  migration instructions in case they\'re having problems
    3.  upcoming IRC/Twitter livechats (we would set up new ones)
    4.  get on pypi-announce for more announcements

3.  Monday April 9th: give sponsors the one-week notice that we\'re launching *\[we absolutely need all sponsor logos by this date\]*

4.  April 9-15: deal with reports from those maintainers, finish beta.

5.  Monday April 16: launch/redirect.

6.  Monday April 30: shut down legacy.

There\'s a [request from JFrog to postpone redirect to 22nd](https://github.com/pypa/warehouse/issues/3275) \-- but they can use the User-Agent redirect exclusion from legacy until we shut down Legacy, so they should be fine.

### Resolution 

Group approved this plan. Updated the [Warehouse roadmap](WarehouseRoadmap).

## Ask Donald for 

\[sponsor\] transparent logo

## Issue triage 

- Twine/Warehouse error message conflict [https://github.com/pypa/warehouse/issues/3482](https://github.com/pypa/warehouse/issues/3482) [https://github.com/pypa/twine/issues/332](https://github.com/pypa/twine/issues/332)

  - Sumana: seems worth spending a little Twine time on
  - di: we should just revert the error message for now

- give user option to see more search results in pagination [https://github.com/pypa/warehouse/issues/3463](https://github.com/pypa/warehouse/issues/3463)

  - could Nicole user test about this? Yes ![:)](/wiki/europython/img/smile.png ":)")

    - do users search for maintainer names?

- reStructuredText header issue [https://github.com/pypa/warehouse/issues/3311](https://github.com/pypa/warehouse/issues/3311)

  - could Dustin investigate? di: yes, likely a readme_renderer issue

- problem deleting project with a period character in project name [https://github.com/pypa/warehouse/issues/3491](https://github.com/pypa/warehouse/issues/3491)

  - how many projects are potentially affected? di: lots
  - di: trivial to use the non-normalized name instead
  - How many deletions a day do we get? Would be a good question to answer. deletions are uncommon, more common on Test.
    - a deleted filename cannot be reused \*even if the project name was deleted and recreated\*, but verrrrrry few users ever run into this

- which of the cross-browser bugs [https://github.com/pypa/warehouse/issues?q=is%3Aopen+is%3Aissue+no%3Amilestone+label%3A%22cross+browser+bug+%3Abug%3A%22](https://github.com/pypa/warehouse/issues?q=is:open+is:issue+no:milestone+label:%22cross+browser+bug+:bug:%22) do we need to fix before shutting down legacy?

  - deferring to Nicole - none. Priority is mobile/tablet bugs because there is higher percentage of users there than on ie11. Nothing blocking. ie11 users are \< 3% - 90% confident Nicole has found most bugs - most users use Chrome and site was developed with Chrome

## TODO 

- [Sumana to open issue about users searching for maintainer names] \-- filed as [https://github.com/pypa/warehouse/issues/3527](https://github.com/pypa/warehouse/issues/3527)
