# TrackerDevelopmentPlanning

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

This page outlines a plan to improve the Bug Tracker at [http://bugs.python.org](http://bugs.python.org).

See also the [TrackerDevelopment](TrackerDevelopment) page and the [DesiredTrackerFeatures](DesiredTrackerFeatures) pages.

::::::: 
### [Git/GitHub integration](#id1)

While migrating to Git/GitHub, the following things need to be done:

::: 
#### [Converting patches to Pull Requests](#id2)

A new detector that converts patches to pull requests should be written. The tracker will probably require:

- a local git clone of cpython where to commit patches;
- a github account used to post pull requests;
- a github clone of cpython;

This is an outline of its possible functioning:

1.  a new patch is submitted and triggers the detector;
2.  the detector commits the patch on its local clone;
3.  the detector pushes the patch on its github clone;
4.  the detector sends a pull request to the official CPython clone;
5.  the detector adds a link to the newly created PR on the issue page;

Issues:

- should the detector create a separate branch for every issue/patch?
- is it possible to use the correct author/committer on step 2?
- is it possible to skip step 3 and send the PR from the local clone?
- are there better approaches?
:::

::: 
#### [Pull Request List](#id3)

A new list for PRs should be added after the attachments list:

+-------------------+-------------------+-------------------+---------------------+-------------------+
| PR                | Author            | Status            | Comment             | Edit              |
+===================+===================+===================+=====================+===================+
| PR 123            | ezio.melotti      | Merged            | Fix issue #12345    | \[edit\]          |
+-------------------+-------------------+-------------------+---------------------+-------------------+
| PR 125            | ezio.melotti      | Open              | Improve docs        | \[edit\]          |
+-------------------+-------------------+-------------------+---------------------+-------------------+
| PR \[\_\_\_\] \[Add New Pull Request\]                                                              |
+-----------------------------------------------------------------------------------------------------+

The list is updated when:

- a patch is uploaded and a PR is automatically created;
- the user enters a PR number in the specific field at the bottom;

The list might also be updated when:

- through an API call (if/when the REST API is added to Roundup it should work out of the box);
- a PR number is mentioned in a message
  - pro: mentioning the PR num in the message is enough \-- no need to write it in the field;
  - pro: useful for bots that can\'t edit fields and only send messages via email;
  - cons: if the PR of a related issue is mentioned it will be included too;
:::

::: 
#### [Other Roundup/GitHub integrations](#id4)

- a \"GitHub account name\" field for users;
- auto-nosy to the issue for users that submit a PR;
- conditional auto-closing of issues when PR is merged;
- an API to check the CLA from GitHub;
:::

::: 
#### [Auto-generated Links](#id5)

The [extension that generates links](https://hg.python.org/tracker/python-dev/file/tip/extensions/local_replace.py), also needs to be updated:

- update cs ids links to point to [https://hg.python.org/lookup/](https://hg.python.org/lookup/) (see [this message](https://mail.python.org/pipermail/python-committers/2016-January/003691.html)).
- update path links to point to GitHub;
- add links to pull requests on GitHub when \"PR num\" or \"pull request num\" are used in messages;
:::
:::::::

::: 
### [Workflow](#id6)

Certain things in the UI may trigger depending on how the user is classified. The current roundup \'Developer\' role is modified into the following sub-roles:

> - Triage
> - Committer
> - Release Manager

Change possible \'resolved\' states to the following:

> - fixed
> - won\'t fix
> - duplicate
> - postponed
> - not a bug
> - third party

These 6 states are already present, but there are 5 additional ones that should be removed: later, out of date, rejected, remind, works for me.

Replace both \'components\' and \'keywords\' by a more comprehensive tagging system. Initially at least these will all be \'official\' tags, listed in the developer\'s guide and settable via autocomplete in a text field. The list of values should be every category currently in the experts list, plus:

> - resource usage
> - performance
> - security issue
> - segfault/abort
> - stuck
> - buildbot
> - bite sized
> - release blocker (for each active release)
> - deferred blocker (for each active release)

Change Types to:

> - documentation
> - bug
> - enhancement

Change \'assigned to\' so that it can be any valid user, and it is automatically reset to \'no one\' after N days or an issue state change.

New \'state\' field will eventually replace both \'stage\' and \'status\' (see [http://imgur.com/a/UgJBJ](http://imgur.com/a/UgJBJ) for a diagram).

> - new
> - information needed
> - decision needed
> - patch needed
> - review needed
> - patch update needed
> - commit review needed
> - resolved (with one of the resolved states)

Priority:

> - high
> - normal
> - low
:::

:::: 
### [Other features](#id7)

::: 
#### [Patch-related improvements](#id8)

When a file is submitted the tracker should be able to:

- Determine if the file is a patch or not
- Determine what files are affected by the patch (and possibly add the module/package names as tags)
- Determine if the patch contains tests, docs, Misc/NEWS entry, Misc/ACKS, What\'s New (etc?)
- Determine if the patch contains trailing whitespace or PEP 8 violations
- Determine on which branches the patches apply on without conflicts (with a way to re-check it on demand or periodically)

Somewhat controversial: a set of checkboxes for the items from the above that are required for this particular issue\'s patch.
:::
::::

:::: 
### [User Interface](#id9)

- Have only title/message/state in the default user view, with a sticky (either per-user or per-browser (via cookies)) setting to also show the other fields. (No \'state\' in the \'new issue\' view).
- Show the role of users (normal user, developer/triager, committer) with an icon or tooltip
- **DONE** Show a \"clip\" icon in the issue list page for issues with a patch (see [http://psf.upfronthosting.co.za/roundup/meta/issue550](http://psf.upfronthosting.co.za/roundup/meta/issue550))

::: 
#### [Dashboard(s)](#id10)

Add a dashboard page similar to [https://dashboard.djangoproject.com/](https://dashboard.djangoproject.com/) (global + per user?).

Experiment with a dashboard that actually lists the top messages in each state, arranged in the order of interest to the user based on their role (user, triager, committer).

\'stuck\' issues are sorted to bottom of queue.

\'information needed\' queue should list only issues that have been in that state for longer than N days.

------------------------------------------------------------------------

[CategoryTracker](CategoryTracker)
:::
::::
