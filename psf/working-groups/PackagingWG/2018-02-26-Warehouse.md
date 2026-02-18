# PackagingWG/2018-02-26-Warehouse

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

## Warehouse weekly meeting, Feb 26, 2018 

### Present 

- Sumana
- Laura
- Ernest
- Dustin
- Nicole

(Mark absent, as he\'d told us he would be)

### Done/working on/blockers 

- Nicole
  - Not blocked
  - Reviewing contributor PRs
  - Working on user testing the UI
  - Hope to have issues to address by the end of the week
- Dustin
  - Just various PRs

  - Added Stimulus JS framework - disabled confirmation button for delete - will make things clearer & simpler

  - Working on making updates to make Markdown READMEs happen
- Laura
  - Assisted Sumana with scheduling IRC office hours for maintainers

  - Fixed [https://github.com/pypa/warehouse/issues/2869](https://github.com/pypa/warehouse/issues/2869)

  - Created a PR for [https://github.com/pypa/warehouse/issues/2875](https://github.com/pypa/warehouse/issues/2875), about to revise to address Dustin\'s review

  - open to hearing what bug to work on next (Sumana suggests [https://github.com/pypa/warehouse/issues/1299](https://github.com/pypa/warehouse/issues/1299) )
- Ernest
  - Spam: ate time, but not in scope of MOSS grant.

  - Performance & Memory consumption whack-a-mole - performance tidying

  - Final integration between Cabotage (our deploy tool) and Kubernetes (our deploy platform)

  - Let\'s get this out to \[infra\]! \[redacted\]
- Sumana
  - got PyPA membership (yay!) - working on some twine tickets

  - wrote some API docs (#3055) & packaging guide updates ( [https://github.com/pypa/python-packaging-user-guide/pull/440](https://github.com/pypa/python-packaging-user-guide/pull/440) , [https://github.com/pypa/python-packaging-user-guide/pull/439](https://github.com/pypa/python-packaging-user-guide/pull/439) )

  - waiting on Nicole to merge [https://github.com/nlhkabu/nlhkabu.github.io/pull/10](https://github.com/nlhkabu/nlhkabu.github.io/pull/10) so Sumana can reply to #2417, #2562, maybe #945 and #1935 - Will look at this tonight \-- DONE

  - next: lots of outreach/publicity and docs
- Mark - not present
  - Open Tech Fund grant proposal - deadline at end of this month
  - PEP 541

### Reschedule March 5th meeting 

- Nicole \-- is later on Monday March 5th ok, or should we move to Tuesday the 6th? - Either works, but I\'d prefer tues if it works for everyone else ![:)](/wiki/europython/img/smile.png%20":)")

  - Laura to update \-- DONE

### IRC livechats/office hours 

1.  Tuesday Feb 27th: 1700 UTC / noon-1pm EST
2.  Tuesday Feb 27th: 2300 UTC / 6pm-7pm EST
3.  Thursday March 1st: 1700 UTC / noon-1pm EST
4.  Thursday March 1st: 2300 UTC / 6pm-7pm EST

you\'ll get calendar invites

### Open Tech Fund grant-seeking - improving security for users 

- Mark needs our help on Etherpad. See Slack and packaging-wg thread
  - Nicole, Ernest, Sumana, Dustin, Laura are all in

  - Submit an estimate

  - add accessibility audit? Esp. important given use of [JavaScript](./JavaScript.html)

  - Localization
- let\'s put all our ideas in the Etherpad and winnow from there

### Milestone progress, publicity planning 

- Milestones 1 & 2 cleared

  - [https://pyfound.blogspot.com/2018/02/python-package-maintainers-help-test.html](https://pyfound.blogspot.com/2018/02/python-package-maintainers-help-test.html) posted

  - some of [https://docs.google.com/document/d/1j1c-Waa2l0ikbfHblto5py9_KWiOgqgo02x2SLTKmKs/edit](https://docs.google.com/document/d/1j1c-Waa2l0ikbfHblto5py9_KWiOgqgo02x2SLTKmKs/edit) still not done yet - Sumana needs to execute

  - pypi-legacy banner?
    - Yes, add banner - don\'t put on non-logged in pages, just for logged in maintainers

  - Sumana will continue to send emails and promote Warehouse to testers

- [https://github.com/pypa/warehouse/projects/1](https://github.com/pypa/warehouse/projects/1) We\'re closing in on Milestone 3: Publicize beta

  - Warehouse: 7 open bugs in [https://github.com/pypa/warehouse/milestone/10](https://github.com/pypa/warehouse/milestone/10)

  - infra: readiness?
    - Ernest: Just gonna start using \[other infra\] to start getting something working, we\'ll throw it away and move to \[infra\] when \[blocker resolved\]. (Update as of Tuesday: blocker is now resolved!)

  - Nicole - only needs to remove warning by the very end

  - Dustin - could finish by early March, even possibly the end of this week

- timing: early March?
  - Mid March feels reasonable at this point. We got a ton of production hardening done last week with memory consumption/perf.-

  - Ernest will unblock himself by using Google \-- needs metrics & monitoring \-- will work with Dustin

  - Depending on DI\'s workload I might work with him to get him running with instrumenting stuff? No pressure, but he\'s in a good spot as far as knowledge of inside bits to help ![:)](/wiki/europython/img/smile.png%20":)")

    - YES PLEASE - di yayayaya! we\'ll schedule offline.

- need Dustin & Ernest to work on docs for this milestone

- Reach out to 3rd party services about new pypi.org domain #2935
  - Sumana will need help on this

- Brainstorming for places we could promote the beta, the launch, and the shutdown [https://docs.google.com/document/d/1uinYN4hjq5Yzz1oWFcGqC5XE45wXF4sh3heqtid6EW8/edit](https://docs.google.com/document/d/1uinYN4hjq5Yzz1oWFcGqC5XE45wXF4sh3heqtid6EW8/edit)

### Ask Donald for 

- \[infra\]

- Review [https://github.com/pypa/packaging/pull/125](https://github.com/pypa/packaging/pull/125)

### Bug triage/double-checking 

- User forgot PyPI password, packaging-problems #122
  - Ernest or Dustin?
    - Ernest: on it.

- Version lookup should take PEP 440 normalization into account #445 [https://github.com/pypa/warehouse/issues/445](https://github.com/pypa/warehouse/issues/445)

  - can we put this off till after launch?
    - Ernest: +1 to Donald\'s note saying we absolutely can.
    - Dustin currently working on version normalization for pypa/packaging so this will be shipped soon

- incremental search indexing #701 [https://github.com/pypa/warehouse/issues/701](https://github.com/pypa/warehouse/issues/701)

  - Need it for the beta or launch? or postpone to post-launch?
    - Nice to have, I\'m -1 to making it a blocker for launch
    - Wasim will take on Elasticsearch issues
    - Someone else left some Elasticsearch comments, Dustin and Sumana will track them down - TODO

- show maintainer\'s name next to avatar on project page #3005 [https://github.com/pypa/warehouse/issues/3005](https://github.com/pypa/warehouse/issues/3005)

  - If Laura doesn\'t fix it with her fix to the very similar #2875 (fixing the project collaboration page), same cool-but-not-urgent milestone?
    - Nicole will review this week

- Improve default browse page order, or remove link #3062 [https://github.com/pypa/warehouse/issues/3062](https://github.com/pypa/warehouse/issues/3062)

  - Need this for launch?
    - Ernest: nah, but not really a huge lift to improve UX here. +1
    - May save users confusion - do earlier?
    - Resolution: insert a temporary fix, then fix more thoroughly later

- 499 client error when uploading #2533 [https://github.com/pypa/warehouse/issues/2533](https://github.com/pypa/warehouse/issues/2533)

  - user has submitted a commit that fails - next steps?
    - Ernest: I\'m leaning towards delay/close until we have better control over our hosting/infra to investigate. Heroku is inscrutable.
    - Dustin: seems like something got stuck in the pipes between the user and PyPI\... hard to debug
    - Ask user for traceroutes, DNS, information about their ISP/network provider? Theory that heroku is blocking them
    - Not a priority to debug remotely \-- will be off Heroku soon

- [https://code.launchpad.net/%7Edustin-ingram/pkginfo/add-new-fields/+merge/330572](https://code.launchpad.net/~dustin-ingram/pkginfo/add-new-fields/+merge/330572) pkg_info update towards Markdown support [https://github.com/pypa/warehouse/issues/869#issuecomment-340928703](https://github.com/pypa/warehouse/issues/869#issuecomment-340928703)

  - need any help? should be good!
    - know what needs done, just need time

  - need anything in readme_renderer? [https://github.com/pypa/readme_renderer/pulls](https://github.com/pypa/readme_renderer/pulls)

    - nope readmerender is good

  - Ernest: Super stoked on Metadata 2.1, also happy to do anything I can help with\... but is this in scope of MOSS grant work? not in scope, so it\'s in my \'extra\' time

  - Will save a headache when people ask about it, nice to have

### TODO 

- add another IRC office hours at 23:00 UTC
  - Laura send calendar invites for IRC office hours -DONE
  - Sumana to update wiki page to reflect Tuesday IRC livechat 2300 UTC / 6pm-7pm EST - DONE
- Dustin and Sumana to find good Elasticsearch comments
