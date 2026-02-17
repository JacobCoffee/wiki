# GitSvnOld

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

::: caution
Python is now hosted in a Mercurial repository. This page is currently outdated.
:::

# Checking out the Python Source Code with Git 

Note that the Python source is eventually going to be moved from Subversion of Mercurial. When that happens, the Git repositories will likely stop being updated.

Also note that these instructions should not be considered a good introduction to typical Git usage. They are necessarily complex because they try to be efficient in network bandwidth while still working with the existing Subversion infrastructure.

## Introduction 

Python\'s source code currently maintained under the [Subversion](http://subversion.tigris.org) revision control system. This document describes how to checkout the source as a [Git](http://git-scm.com/) repository. Some advantages of using git are:

\* The entire history is available locally so you easily work without network access.

\* Git has some nice tools for dealing with local branches (rebasing them, for example).

\* Operations like `git diff`{.backtick} and `git log`{.backtick} are much faster than the Subversion equivalents.

## Doing the initial checkout 

Git\'s pack format is efficient but the entire VC history of Python still consumes a lot of space (currently around 90 MB). You could use `git-svn`{.backtick} to create a local repository (please don\'t do that) but it\'s much faster to use the native git protocol. To allow that, there are Git repositories on svn.python.org that are updated every hour. Changes since that time can be pulled using `git-svn`{.backtick}.

Ensure that you have a recent Git (at least version 1.5.1). The following commands will initialize an empty repository::

        mkdir trunk.git
        cd trunk.git
        git init

Tell git-svn where the Subversion repository is located (so you can use git-svn to push and pull changes to the SVN server). If you have read-write access use::

        git svn init svn+ssh://pythondev@svn.python.org/python/trunk

Tell Git where the data can be fetched using the Git protocol. This is more efficient than using the Subversion protocol, especially if you are far behind the head::

        git remote add git-svn git://code.python.org/python/trunk
        git config remote.git-svn.fetch refs/heads/master:refs/remotes/git-svn

The following command populates the local repository (this will download approximately 90 MB of data from code.python.org). Note that you can use the `git clone`{.backtick} command to efficiently make local copies of the repository. To fetch that data into the local `git-svn`{.backtick} branch::

        git fetch git-svn

We don\'t do our development on the git-svn branch since that follows the head of the public Subversion repository. Our main development branch is called \'master\', athough we can create as many others as we like. Merge the changes from the `git-svn`{.backtick} branch into our development branch (normally you would first rebase your changes in master on top of git-svn but right now we don\'t have any)::

         git pull git-svn master

The local branch `master`{.backtick} and the remote branch `git-svn`{.backtick} now contain identical trees. Use `git-svn`{.backtick} to get up to the minute changes from the SVN server::

        git svn fetch

This should complete quickly because nearly all the data is already local and the `git-svn`{.backtick} command will merely go through the logs and extract the Subversion revision numbers.

## Keeping up-to-date 

Using the `git svn fetch`{.backtick} command closely matches the behavior of the `svn update`{.backtick} command. It will fetch new versions from the Subversion repository and then rebase your local changes on top of them::

        git svn fetch

Note that this can be slow if your repository is far behind the Subversion repository. The most efficient method to update your local respository is to use the Git protocol before using `git svn`{.backtick}. To fetch new commits, run::

        git fetch git-svn

If you have no local changes, you can do a fast-forward merge of upstream commits into your current development branch::

        git merge git-svn

However, if you have local changes then you probably want to use `rebase`{.backtick} as it more closely matches the behavior of `svn up`{.backtick}. This will essentially extract your changes as a series of patches and reapply them to the git-svn (i.e. most recent) version of the tree::

        git rebase git-svn

## Sharing work 

Please refer to the [Git SVN tutorial](http://git.or.cz/course/svn.html) for general instructions on how to interact with a Subversion repository. The `git format-patch`{.backtick}, `git am`{.backtick} and `git apply`{.backtick} commands are very useful when dealing with patches.

If you have write access to the SVN repository then you can use `git svn dcommit`{.backtick} to push your local commits directly into the public SVN repository. Take extra care before using `dcommit`{.backtick}. It\'s a good idea to use `git log`{.backtick} or `gitk`{.backtick} to check what will be sent before actually running `dcommit`{.backtick}. Also note that your local copy must be up-to-date (e.g. via `git svn rebase`{.backtick}) for `dcommit`{.backtick} to work.

## Python 3 branch 

There is also a Git repository for the py3k branch. The following commands assume read-write access to the SVN repository and will create a local repository (the important difference is with the SVN and Git URLs)::

        mkdir py3k.git
        cd py3k.git
        git init
        git svn init svn+ssh://pythondev@svn.python.org/python/branches/py3k
        git remote add git-svn git://code.python.org/python/branches/py3k
        git config remote.git-svn.fetch refs/heads/master:refs/remotes/git-svn
        git fetch git-svn
        git pull git-svn master
