# Bazaar

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# Using Bazaar to develop Python 

Note: While Python has officially chosen Mercurial for its DVCS, you can still use Bazaar to develop Python. This page describes the current workflow. The migration plan is [PEP 385](http://www.python.org/dev/peps/pep-0385/).

Python\'s source code is maintained under the [Subversion](http://subversion.tigris.org) revision control system. Unofficial [Bazaar](http://bazaar-vcs.org) mirrors of the Subversion repository are maintained on Launchpad and are kept up-to-date automatically.

## What is available? 

We currently have mirrors of the Python 2.6, trunk (2.7), 3.1, and py3k (3.2) branches available to the public. These branches are synchronized in near-real time with the Subversion master. This means that as commits are made to Subversion, they will be available in Bazaar on Launchpad soon thereafter. Of course, there\'s a bit of a lag imposed by the Launchpad puller.

All of the mirrored branches are available [here](https://code.edge.launchpad.net/python).

Code hosting of Bazaar branches is also available on Launchpad. This means you can branch Python locally via Bazaar, do some development, and then push your branch to Launchpad to share with others. Of course because the master branches are in Subversion, you\'ll still have to go through the standard Python development process to get your changes into mainline. But short of that, you can do all your development in a nice, modern DVCS.

There is a pretty good [Bazaar/Subversion bridge](http://wiki.bazaar.canonical.com/BzrForeignBranches/Subversion) which should allow you to commit your Bazaar branch to the Subversion master, but I have not tried it.

## What do I need? 

\* [Bazaar 2.0 or newer](http://bazaar-vcs.org/Download). As of this writing (2010-02-24) Bazaar 2.1 is the most recent release. As Bazaar is written in Python (yay!), it is available for all major platforms, See the Bazaar home page for information about versions for your platform.

\* Python 2.4 or newer. Bazaar requires at least Python 2.4.

\* A Launchpad login if you want to push branches to Launchpad. You do not need a login if all you\'re going to do is pull branches from Launchpad.

## How do I get started? 

There are many ways to use Bazaar. Some like to use it the same way they use Subversion. Others like to take advantage of the disconnected and distributed features, so that they can develop code while off the net. The Bazaar web site outlines all these options. The documentation here will describe just one way of working with it.

You will definitely want to create what Bazaar calls a *shared repository* on your system. Because Bazaar (by default) keeps the entire branch history on the local system, you will want to share this history across all your branches. Having all the history local means you have a fully functional revision control system even when you are not on the \'net, however the first time you grab a branch, it might take a while depending on the speed of your network connection. After that, branching inside your shared repo should be pretty fast.

To create the shared repo, cd to some convenient place and do the following:

    % bzr init-repo python
    % cd python

This `python`{.backtick} directory is your shared repo and you will create all your branches inside of this. It doesn\'t matter which of the four branches you\'re developing; all of your work can go in the same shared repo.

Now, you can grab one of the branches. Let\'s say you want a copy of the Python 3k trunk; do this:

    % bzr branch lp:python/py3k

This will create a working directory called `py3k`{.backtick} in your shared repository directory. Generally, you will want to keep this upstream branch fairly pristine, updating it occasionally, as commits are made to the Subversion master and mirrored to the Launchpad branch. Here\'s how you can pull any new revisions:

    % cd py3k
    % bzr pull

Now let\'s say you want to work on a fix for [bug 1974](http://bugs.python.org/issue1974). Bazaar encourages (but doesn\'t require!) small, frequent branches focused on just the task at hand.

    % cd ..
    % bzr branch py3k bug1974
    % cd bug1974

Now you hack the code. You like your changes and want to commit them. Again, Bazaar encourages but does not require frequent commits. Unlike Subversion though, by default commits in Bazaar are completely local (although there is a style of workflow where commits happen to the remote repository). Here\'s how you could commit your changes:

    % bzr commit

This will pop up an editor, but you could also use the `-m`{.backtick} or `-F`{.backtick} arguments to supply a commit message on the command line. You might also like to give this the `--show-diff`{.backtick} argument to see your changes in the commit buffer.

You can keep iterating on the hack-commit cycle as much as you want, until you are ready to share your code with someone. To do this, push your branch like so, substituting your Launchpad user name for `barry`{.backtick} of course.

    % bzr push py:~barry/python/bug1974

The last path component can be anything that doesn\'t already exist.

Now everyone (not just core developers) will be able to view, branch, and merge your branch, say to do a code review. You can even create a diff of your branch against the trunk, say to generate a patch for the [Python bug tracker](http://bugs.python.org).

You can attach your branch URL to the issue in the Python bug tracker, and it will be much easier for a core developer to review and apply your changes.

## Loggerhead 

[Loggerhead](https://launchpad.net/loggerhead) is the [ViewVC](http://www.viewvc.org/) of Bazaar. It\'s a web interface that lets you explore Python\'s bzr branches, view history, etc. Loggerhead is available for all the Python branches. E.g. the trunk is visible [here](http://bazaar.launchpad.net/~python-dev/python/trunk/files). Other branches can be viewed by clicking on the appropriate series as listed [here](https://code.edge.launchpad.net/python).

## Anything else? 

You want to create or edit your `~/.bazaar/bazaar.conf`{.backtick} file to set a few things up. Unlike Subversion, Bazaar commits happen locally, so you have control over the email address that gets associated with your changes. You should use an email address that is identifiably you in the Python community. You may also decide to [GPG](http://www.gnupg.org) sign your commits, though this is not required. Here for example is my `bazaar.conf`{.backtick} [file::](file::)

    [DEFAULT]
    email=Barry Warsaw <barry@python.org>
    create_signatures=always
    smtp_server = mail.example.com
    [ALIASES]
    last = log -r-10..-1 --line
    commit = commit --strict

See the Bazaar documentation for more options on [configuring Bazaar](http://bazaar-vcs.org/ConfiguringBzr).

If you are running on Ubuntu, you should have a new enough Bazaar if you are running Karmic (9.10) or newer. Lucid (10.04) will ship with Bazaar 2.1.

Christian Heimes points out the following instructions for getting the latest bzr on older versions of Ubuntu:

    sudo vi /etc/apt/sources.list.d/bzr.list
    --- add ---
    deb http://ppa.launchpad.net/bzr/ubuntu gutsy main
    deb-src http://ppa.launchpad.net/bzr/ubuntu gutsy main
    --- eof ---

    sudo apt-get update

    #  --force-yes because the packages aren't signed yet
    sudo apt-get --force-yes -y install bzr bzr-gtk bzrtools

Also read [https://launchpad.net/\~bzr/+archive](https://launchpad.net/~bzr/+archive) and [http://bazaar-vcs.org/DistroDownloads](http://bazaar-vcs.org/DistroDownloads)

## Where do I get help? 

Start by reading the [Bazaar documentation](http://bazaar-vcs.org/Documentation). There are many ways to use Bazaar and many options, commands and plugins (such as [looms](https://edge.launchpad.net/bzr-loom) which rock) which are not described above. Explore!

Ask your questions on the [python-dev@python.org](mailto:python-dev@python.org) mailing list. We\'ll keep an eye on things and try to help as much as possible.

Log onto [irc.freenode.net](http://freenode.net/) and ask around on the `#python`{.backtick}, `#python-dev`{.backtick}, or `#bzr`{.backtick} channels. The former two are better for specific questions about Python\'s Bazaar branches, while the latter is better for more general Bazaar questions.

Keep refreshing this page! We\'ll try to keep it updated with new information and examples, based on your feedback.
