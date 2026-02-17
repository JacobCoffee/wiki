# DeveloperFAQ

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# Developer\'s FAQ

::: 
Table of Contents

- [1   General Information](#general-information)
  - [1.1   What is SourceForge?](#what-is-sourceforge)
  - [1.2   Where can I find Jython on SourceForge?](#where-can-i-find-jython-on-sourceforge)
  - [1.3   Who is who?](#who-is-who)
  - [1.4   How can I become a developer?](#how-can-i-become-a-developer)
- [2   Subversion (svn)](#subversion-svn)
  - [2.1   Where can I learn about Subversion (svn)?](#where-can-i-learn-about-subversion-svn)
  - [2.2   What do I need to use Subversion?](#what-do-i-need-to-use-subversion)
    - [2.2.1   UNIX Command line](#unix-command-line)
    - [2.2.2   Windows](#windows)
  - [2.3   How do I get a checkout of the repository?](#how-do-i-get-a-checkout-of-the-repository)
  - [2.4   How do I update my working copy to be in sync with the repository?](#how-do-i-update-my-working-copy-to-be-in-sync-with-the-repository)
  - [2.5   How do I browse the source code through a web browser?](#how-do-i-browse-the-source-code-through-a-web-browser)
  - [2.6   How do I add a file or directory to the repository?](#how-do-i-add-a-file-or-directory-to-the-repository)
  - [2.7   How do I commit a change to a file?](#how-do-i-commit-a-change-to-a-file)
  - [2.8   How do I delete a file or directory in the repository?](#how-do-i-delete-a-file-or-directory-in-the-repository)
  - [2.9   What files are modified locally in my working copy?](#what-files-are-modified-locally-in-my-working-copy)
  - [2.10   How do I find out what Subversions properties are set for a file or directory?](#how-do-i-find-out-what-subversions-properties-are-set-for-a-file-or-directory)
  - [2.11   How do I revert a file I have modified back to the version in the respository?](#how-do-i-revert-a-file-i-have-modified-back-to-the-version-in-the-respository)
  - [2.12   How do I find out who edited or what revision changed a line last?](#how-do-i-find-out-who-edited-or-what-revision-changed-a-line-last)
  - [2.13   How can I see a list of log messages for a file or specific revision?](#how-can-i-see-a-list-of-log-messages-for-a-file-or-specific-revision)
  - [2.14   How do I get a diff between the repository and my working copy for a file?](#how-do-i-get-a-diff-between-the-repository-and-my-working-copy-for-a-file)
  - [2.15   How do I undo the changes made in a recent committal?](#how-do-i-undo-the-changes-made-in-a-recent-committal)
- [3   Patches](#patches)
  - [3.1   How to make a patch?](#how-to-make-a-patch)
  - [3.2   How do I apply a patch?](#how-do-i-apply-a-patch)
  - [3.3   How do I undo an applied patch?](#how-do-i-undo-an-applied-patch)
  - [3.4   How to submit a patch?](#how-to-submit-a-patch)
  - [3.5   How to test a patch?](#how-to-test-a-patch)
:::

::::::: 
### [1   General Information](#id1)

::: 
#### [1.1   What is SourceForge?](#id2)

SourceForge is a free hosting service for open source projects. The main website is found at [http://sourceforge.net](http://sourceforge.net).
:::

::: 
#### [1.2   Where can I find Jython on SourceForge?](#id3)

The Jython project page can be found at [http://sourceforge.net/projects/jython](http://sourceforge.net/projects/jython).
:::

::: 
#### [1.3   Who is who?](#id4)

The list of developers with commit access is here: [http://sourceforge.net/project/memberlist.php?group_id=12867](http://sourceforge.net/project/memberlist.php?group_id=12867)

This presents a list of developers, giving their names and SourceForge IDs.
:::

::: 
#### [1.4   How can I become a developer?](#id5)

Submit patches that fix bugs or implement features, especially features that exist in CPython but are not yet implemented in Jython.
:::
:::::::

:::::::::::::::::::: 
### [2   Subversion (svn)](#id6)

::: 
#### [2.1   Where can I learn about Subversion (svn)?](#id7)

Subversion has its official web site at [http://subversion.tigris.org/](http://subversion.tigris.org/) (it is also known as svn thanks to that being the name of the executable of Subversion itself). A book on Subversion published by O\'Reilly Media, Version Control with Subversion, is available for free online.

With Subversion installed, you can run the help tool that comes with Subversion to get help:

svn help

This will give you the needed information to use the tool. The man page for svn is rather scant and thus not worth reading.
:::

::::: 
#### [2.2   What do I need to use Subversion?](#id8)

::: 
##### [2.2.1   UNIX Command line](#id9)

First, you need to download Subversion. Most UNIX-based operating systems have binary packages available for Subversion. Also, most package systems also have Subversion available.
:::

::: 
##### [2.2.2   Windows](#id10)

You have several options on Windows. One is to download Subversion itself which will give you a command-line version. Another option is to download TortoiseSVN which integrates with Windows Explorer.
:::
:::::

::: 
#### [2.3   How do I get a checkout of the repository?](#id11)

The basic command is:

svn checkout \<URL\> \[PATH\]

\<URL\> is the specified location of the project within the repository that you would like to check out (those paths are discussed later). The optional \[PATH\] argument specifies the local directory to put the checkout into. If left out then the tail part of \<URL\> is used for the directory name.

The format of \<URL\> is:

[https://jython.svn.sourceforge.net/svnroot/jython](https://jython.svn.sourceforge.net/svnroot/jython)/\<path\>

with \<path\> representing the path to the project.

The Subversion repository has many projects under it. Most people are probably interested in one of these four projects:

> - the trunk or HEAD (the current version under development)
> - the experimental Jython 2.5 (ASM) branch
> - the latest release (plus bug fixes) of Jython
> - the website source

The projects above can be checked out using the following \<URL\> paths, respectively:

> - [https://jython.svn.sourceforge.net/svnroot/jython/trunk/](https://jython.svn.sourceforge.net/svnroot/jython/trunk/)
> - [https://jython.svn.sourceforge.net/svnroot/jython/branches/asm/](https://jython.svn.sourceforge.net/svnroot/jython/branches/asm/)
> - [https://jython.svn.sourceforge.net/svnroot/jython/branches/Release_2_2maint/](https://jython.svn.sourceforge.net/svnroot/jython/branches/Release_2_2maint/)
> - [https://jython.svn.sourceforge.net/svnroot/jython/trunk/website/](https://jython.svn.sourceforge.net/svnroot/jython/trunk/website/)
:::

::: 
#### [2.4   How do I update my working copy to be in sync with the repository?](#id12)

Run:

svn update

from the directory you wish to update (and all subdirectories).
:::

::: 
#### [2.5   How do I browse the source code through a web browser?](#id13)

Visit [http://fisheye3.cenqua.com/browse/jython](http://fisheye3.cenqua.com/browse/jython) to browse the Subversion repository.
:::

::: 
#### [2.6   How do I add a file or directory to the repository?](#id14)

Simply specify the path to the file or directory to add and run:

svn add PATH

Subversion will skip any directories it already knows about. But if you want new files that exist in any directories specified in PATH, specify \--force and Subversion will check all directories for new files.

You will then need to run svn commit. See the next section.
:::

::: 
#### [2.7   How do I commit a change to a file?](#id15)

To have any changes to a file (which include adding a new file or deleting an existing one), you use the command:

svn commit \[PATH\]

Although \[PATH\] is optional, if PATH is omitted all changes in your local copy will be committed to the repository. DO NOT USE THIS!!! You should specify the specific files to be committed unless you are absolutely positive that all outstanding modifications are meant to go in this commit.

To abort a commit that you are in the middle of, perform a commit with no message (i.e., close the text editor without adding any text for the message). Subversion will ask if you want to abort the commit or not at that point.

If you do not like the default text editor Subversion uses for entering commmit messages, you may specify a different editor in your Subversion config file with the editor-cmd option in the \[helpers\] section.
:::

::: 
#### [2.8   How do I delete a file or directory in the repository?](#id16)

Specify the path to be removed with:

svn delete PATH

Any modified files or files that are not checked in will not be deleted in the working copy on your machine.
:::

::: 
#### [2.9   What files are modified locally in my working copy?](#id17)

Running:

svn status \[PATH\]

will list any differences between your working copy and the repository. Some key indicators that can appear in the first column of output are:

> - A Scheduled to be added
> - D Scheduled to be deleted
> - M Modified locally
> - ? Not under version control
:::

::: 
#### [2.10   How do I find out what Subversions properties are set for a file or directory?](#id18)

svn proplist PATH
:::

::: 
#### [2.11   How do I revert a file I have modified back to the version in the respository?](#id19)

Running:

svn revert PATH

will change PATH to match the version in the repository, throwing away any changes you made locally. If you run:

svn revert -R

from the root of your local repository it will recursively restore everything to match up with the main server.
:::

::: 
#### [2.12   How do I find out who edited or what revision changed a line last?](#id20)

You want:

svn blame PATH

This will output to stdout every line of the file along with what revision number last touched that line and who committed that revision. Since it is printed to stdout, you probably want to pipe the output to a pager:

svn blame PATH \| less
:::

::: 
#### [2.13   How can I see a list of log messages for a file or specific revision?](#id21)

To see the log messages for a specific file, run:

svn log PATH

That will list all messages that pertain to the file specified in PATH.

If you want to view the log message for a specific revision, run:

svn log \--verbose -r REV

With REV substituted with the revision number. The \--verbose flag should be used to get a listing of all files modified in that revision.
:::

::: 
#### [2.14   How do I get a diff between the repository and my working copy for a file?](#id22)

The diff between your working copy and what is in the repository can be had with:

svn diff PATH

This will work off the current revision in the repository. To diff your working copy with a specific revision, do:

svn diff -r REV PATH

Finally, to generate a diff between two specific revisions, use:

svn diff -r REV1:REV2 PATH

Notice the : between REV1 and REV2.
:::

::: 
#### [2.15   How do I undo the changes made in a recent committal?](#id23)

Assuming your bad revision is NEW and OLD is the equivalent of NEW - 1, then run:

svn merge -r NEW:OLD PATH

This will revert all files back to their state in revision OLD. The reason that OLD is just NEW - 1 is you do not want files to be accidentally reverted to a state older than your changes, just to the point prior.

Note: PATH here refers to the top of the checked out repository, not the full pathname to a file. PATH can refer to a different branch when merging from the head, but it must still be the top and not an individual file or subdirectory.
:::
::::::::::::::::::::

::::::::: 
### [3   Patches](#id24)

::: 
#### [3.1   How to make a patch?](#id25)

If you are using subversion (anonymous or developer) you can use subversion to make the patches for you. Just edit your local copy and enter the following command:

svn diff \| tee \~/name_of_the_patch.diff

Else you can use the diff util which comes with most operating systems (a Windows version is available as part of the cygwin tools).
:::

::: 
#### [3.2   How do I apply a patch?](#id26)

For the general case, to apply a patch go to the directory that the patch was created from (usually /dist/src/) and run:

patch -p0 \< name_of_the_patch.diff

The -p option specifies the number of directory separators (\"/\" in the case of UNIX) to remove from the paths of the files in the patch. -p0 leaves the paths alone.
:::

::: 
#### [3.3   How do I undo an applied patch?](#id27)

Undoing a patch differs from applying one by only a command-line option:

patch -R -p0 \< name_of_the_patch.diff

Another option is to have \'patch\' create backups of all files by using the -b command-line option. See the man page for \'patch\' on the details of use.
:::

::: 
#### [3.4   How to submit a patch?](#id28)

Please consult the patch submission guidelines at [http://www.python.org/patches/](http://www.python.org/patches/).

Submit the patch to the Jython bug tracker at [http://bugs.jython.org/](http://bugs.jython.org/).
:::

:::: 
#### [3.5   How to test a patch?](#id29)

Start by testing on your own system. Jython comes with an extensive regression test suite by running the Lib/test/regrtest.py script.

Also run the tests in trunk/bugtests/ directions are in a README file there.

::: 
Note

This FAQ was adapted from the Python developers FAQ at [http://www.python.org/dev/faq/](http://www.python.org/dev/faq/)
:::
::::
:::::::::
