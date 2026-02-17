# Distutils2/Contributing

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# How to contribute to distutils2/packaging 

This document describes a simple workflow that makes it easy to work on a new feature for distutils2, or to track a difficult bug. It requires a basic understanding of Mercurial: clone, update, diff, commit, merge.

The distutils2 codebase is developed as part of CPython 3.3, where it is named "packaging". It is backported for Python 2.4-2.7 and 3.1-3.2 in the [distutils2](http://hg.python.org/distutils2) repository, from which standalone releases are made and uploaded to PyPI. Contributors should work with the 3.3 version, but patches based on the distutils2 repo are also welcomed: some bugs only show up with Python 2, or it can be hard to install a compiler toolchain to work with CPython 3.3.

If you're looking for a bug to work on, have a look at [Distutils2 easy bugs](http://bugs.python.org/issue?%40search_text=&ignore=file%3Acontent&title=&%40columns=title&id=&%40columns=id&stage=&creation=&creator=&activity=&%40columns=activity&%40sort=activity&actor=&nosy=&type=&components=25&versions=&dependencies=&assignee=&keywords=6&priority=&%40group=priority&status=1&%40columns=status&resolution=&nosy_count=&message_count=&%40pagesize=50&%40startwith=0&%40queryname=&%40old-queryname=&%40action=search) or [Distutils easy bugs](http://bugs.python.org/issue?%40search_text=&ignore=file%3Acontent&title=&%40columns=title&id=&%40columns=id&stage=&creation=&creator=&activity=&%40columns=activity&%40sort=activity&actor=&nosy=&type=&components=3&versions=&dependencies=&assignee=&keywords=6&priority=&%40group=priority&status=1&%40columns=status&resolution=&nosy_count=&message_count=&%40pagesize=50&%40startwith=0&%40queryname=&%40old-queryname=&%40action=search) (most of the distutils bugs also apply to distutils2). If you need help and don't feel comfortable asking for it publicly on a bug page, the [core-mentorship](http://mail.python.org/mailman/listinfo/core-mentorship) mailing list is a friendly space where all questions are welcome.

If you've found a new bug or would like to propose a new feature, you should look for an existing report on [http://bugs.python.org/](http://bugs.python.org/) and open one if you find nothing. The bug tracker is used to let developers coordinate (i.e. not duplicate work) and review patches before they are integrated. The field named Component should be set to [Distutils2](http://bugs.python.org/issue?@columns=title,id,activity,status&@sort=activity&@group=priority&@filter=components,status&@pagesize=50&@startwith=0&status=1&components=25&@dispname=distutils2), to let the maintainers be automatically notified of the report, and Version to 3.3. Some bugs only use the [Distutils](http://bugs.python.org/issue?@columns=title,id,activity,status&@sort=activity&@group=priority&@filter=components,status&@pagesize=150&@startwith=0&status=1&components=3&@dispname=distutils) component.

distutils1 should be considered a maintenance branch of distutils2; even for bugs originally reported against distutils1, patches should be developed against distutils2, unless the bug is reproducible with distutils1 only or targets code removed in distutils2. There are more tests and more useful support code in distutils2, so it's easier to work on tests for distutils2 and let its developers will take care of the backport to distutils1.

This page was written with the help of an old version of the [Python developers' guide](http://docs.python.org/devguide/), thanks to its authors. See also [http://mercurial.aragost.com/kick-start/en/tasks/](http://mercurial.aragost.com/kick-start/en/tasks/) for another tutorial describing the same workflow, with pictures but without packaging-specific parts, and the Mercurial wiki: [http://mercurial.selenic.com/wiki/NamedBranches](http://mercurial.selenic.com/wiki/NamedBranches)

## Getting the codebase 

Start by creating a directory for your work and clone the Python 3.x repository:

    $ mkdir cpython && cd cpython
    $ hg clone http://hg.python.org/cpython#default py3k
    $ cd py3k
    $ ./configure --with-pydebug && make -s

You have a working Python, let's start hacking!

## Starting a branch 

Start a new named branch with this command:

    $ hg branch mywork
    $ # wait until you have some changes or commit immediately to register the branch
    $ hg commit

Now you can edit files, run tests and commit your changes. Using a named branch instead of unnamed branches gives you a name, mywork, that you can use with commands such as hg diff and hg log. It doesn't matter how many unclean commits you make in your branch; `hg diff -r default` will always show you the result of the changes in your branch compared to the default branch, in other words your local work compared to the main repository.

Having this name makes it easy to work on various things (one branch per patch), merge regularly with upstream, generate diffs, fix mistakes, port some changes upstream directly, etc. You can make mistakes and fix them; in the end, you will get one clean diff to apply.

If you have many named branches to work on many bugs in parallel, you can push all of them to the same repository to let other people see your changes and let the bug tracker create a patch (more on that later).

A variation of this workflow uses multiple clones. I tend to work on more than one bug at a time, and often have uncommitted changes for a work in progress, so switching between named branches in the same clone would not work. (I also fear that `make` could think that all files are new and recompile everything needlessly.) So to start working on a patch, I first make a copy of my local clone (`hg clone py3k add-magic`) and then create a branch for easy patch tracking as described above.

## Hacking 

You can work on your feature or bug and commit as needed. The distutils2 code lives in Lib/packaging and its documentation in Doc/packaging, Doc/install and Doc/library/packaging.\* Some bugs also require editing modules like site or sysconfig, or their documentation. Ideally, the first step is to write a test that fails, thus demonstrating the bug, and then change the code to make the test pass.

The [Python developers' guide](http://docs.python.org/devguide/) contains good advice that applies to distutils2 as well. For example, it tells you about the `make patchcheck` command (`./python Tools/scripts/patchcheck.py` on Windows), to run from the root of a clone before committing to perform some checks for common mistakes.

For distutils2, each bug fix should have a test, and each new feature should have good tests and documentation. Don't hesitate to ask for assistance or advice on the bug report or on mailing lists:

- [distutils2 development list](http://groups.google.com/group/the-fellowship-of-the-packaging/)

- [Python mentors](http://mail.python.org/mailman/listinfo/core-mentorship)

## Staying in sync 

To make sure that your branch does not get out of sync, which means that the final diff could not be applied, remember to pull and merge new changesets regularly:

    $ cd cpython/py3k
    $ hg pull

(If you use many clones like I do, you would run `hg pull` in the add-magic clone after that; it will not download again from hg.python.org but look for the changesets in the py3k clone, saving you bandwidth and time. To avoid changing directory all the time, you can give a path as argument to the hg command: `hg pull -R ../add-magic`, or write a shell function to automate pulling in all clones.)

The next step is the merge itself::

    $ hg branch
    mywork
    $ hg merge default

Using `hg branch` or `hg id` is a good way to make sure your working copy is a checkout of the right branch. `hg merge default` is the command that lets you incorporate changes from upstream into your local copy. If nobody edited the same files on the same lines, Mercurial will merge everything automatically; otherwise, you will have to resolve the conflicts with the merge tool that you configured and that Mercurial launches for you.

## Sharing your work 

If you don't have a favorite Mercurial hosting yet, the easiest is to use Bitbucket. Log in and visit [http://bitbucket.org/python_mirrors/cpython/fork](http://bitbucket.org/python_mirrors/cpython/fork) to create a server-side clone; select "default" in the dropdown menu labeled "fork at" before submitting, otherwise you will get the Python 2.7 branch, which you don't need. Then you can push the changesets from your named branch:

    $ cd cpython/py3k
    $ hg branch
    mywork
    $ hg push . --new-branch ssh://hg@bitbucket.org/<username>/cpython

Protip: To make Mercurial remember the URI of the repo to use for push, edit the file located at py3k/.hg/hgrc to make it look like this::

    [paths]
    default = http://hg.python.org/cpython#default
    default-push = ssh://hg@bitbucket.org/yourname/cpython

Now `hg push` without arguments will push new changesets to your Bitbucket clone, and `hg pull` will still pull from the official repo.

(If you're using a separate clone, the default pull path would be `../py3k`.)

After you've pushed, another developer can clone your repo to work with you on your branch, or you can automatically add a patch to the Python bug tracker. Let's try this one.

## Mercurial-Roundup integration 

On each bug page, there is a [field](http://docs.python.org/devguide/triaging#mercurial-repository) called "Remote hg repo"; add the HTTP URI of your clone on Bitbucket, with the branch name after a `#` sign, like `http://bitbucket.org/yourname/cpython#mywork`. After this, simply pushing the "Create Patch" button will generate a diff between the default branch of the official repo and the head of your named branch. Anyone with a Roundup account can now follow the link labeled "review" to see the patch and make comments. You can then address this comments with a new commit in your repo, push to your public clone, and "Create Patch" again.

Don't be worried about the review: Even experienced core developers have their patches sent back to them for changes. Getting a review is a sign that your work is noticed and that progress is made towards including it in the official repository. Reply to feedback about the changes, update your patch, ping the maintainers (automatically subscribed to distutils and distutils2 bugs) as needed.

## The end 

When your patch is in a good shape, a Python core developer can take the patch, apply it in the default branch of a cpython clone and push it. You can now use `hg commit --close-branch` to hide your branch. If you were using a second clone, you can delete it to save some disk space.

If the issue was about a bug also present in old-school distutils, you can adapt your fix from Lib/packaging to Lib/distutils and propose this patch. It's okay if you don't want to, the backport will be done by a distutils maintainer.

It is also possible that your patch is rejected, because the issue is judged invalid or because the approach taken in the patch is not accepted. Please do not take it personally; there are a number of constraints on accepting patches, and your work is appreciated regardless of the outcome.
