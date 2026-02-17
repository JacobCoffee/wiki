# CoreDevHelperTools

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# 1. Core Development Helper Tools 

This wiki page has one simple goal, and will strive with its whole heart to fulfill it. In these weird times, when certain people tend to eat, sleep, hang out with their partners and play football, they want to use the little time they have for development as effective as possible. Sometimes its just simple things that make our hacker life more enjoyable, like setting up your hg identity in one line. Sometimes its a more complex concept that we have to break into pieces, and make it simpler. Hacking should be more enjoyable, we should have more time for whatever we want to do, we should eliminate time-waste on repetitive tasks.

Guiding thought: \"With all the sand and sun on the beaches, should I really be doing this now?\"

Ideas for IDE integration (added by [MichaelFoord](MichaelFoord) who has a particular interest in integration with Wing - but integration with Wing, Vim and Emacs would get most bang for buck):

- Run configure / make
- Run test - from a standard library module run the corresponding test file with regrtest and the current version of Python
- Run reindent.py on current file

Ideas for Roundup extensions:

- Integrate Mercurial and other important DVCSs in Roundup based on roundup-svn
- OAuth-based API
- OpenID authentication support

Tools:

- submit-review-request - A tool to submit diff to rietveld/reviewboard

- grab-tracker-patch - A tool to grab/apply patches attached to a tracker issue

- submit-tracker-patch - A tool to submit patches to a specific tracker issue

- mercurial-simpleshare - A tool for simple sharing of mercurial branches (while [\"hg serve\" or hgwebdir.cgi](http://www.selenic.com/mercurial/wiki/index.cgi/HgWebDirStepByStep#head-746ca383e3a62df34279ec2fca888113497da022) fill this slot, it could be made easier, see below).

## 1.1. Use Cases 

### 1.1.1. mercurial-simpleshare

This would have the advantage of avoiding the need to remember \"hg serve\" details and edit config files, allowing one to share a local branch (locally or in a public server) with the same tool, so network topology doesn\'t make it harder to \"hg serve\".

Examples: \'hg-share rw\' to serve a local branch allowing anyone to push to it. The same tool could be used to share branches in public repositories, read-only or read-write: \'hg-share -s code.python.org\'.

### 1.1.2. Roundup VCS integration 

Daniel is a great hacker, but the only time he has time to hack is when his child is asleep. And his child wakes up every now and then, pretty often actually. So when it starts crying, Daniel commits fix to that silly bug that has been hunting us for ages, but forgets to close down the bug so it stays open. Looking over bug tracker, Jane finds the same bug and starts working on the same bug. Wasted time. Daniel should be able to format commit message in such a way that would automatically close the bug.

------------------------------------------------------------------------

[CategoryTracker](CategoryTracker) [CategoryDevelopmentProcess](CategoryDevelopmentProcess)
