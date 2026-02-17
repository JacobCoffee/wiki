# CvsToSvn

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

The Python development team recently switched from using CVS hosted at [SourceForge](SourceForge) to Subversion hosted at svn.python.org. There are many similarities between the two, but there are some differences as well. This page provides general tips. More details about using Subversion as it relates specifically to Python development are available in the [Python developer\'s FAQ](http://www.python.org/dev/devfaq.html#subversion-svn).

(Most of the initial content came from a python-dev post by Tim Peters.)

# Update vs. Status 

CVS uses `update` for all sorts of things. SVN has different commands for several of the use cases CVS\'s update conflates:

- Updating to the current server state. `svn update` does that, and SVN\'s update isn\'t useful for anything other than that.

- Finding out what\'s changed in your sandbox. Use `svn status` for that. Bonus: in return for creating zillions of admin files, `svn status` is a local operation (no network access required). Do `svn status -u` (which **does** require network access) to get a listing of files that **would** change if you were to do `svn update`.

- Merging. Use `svn merge` for that. This includes the case of reverting a checkin, in which case just reverse the revision numbers:

      svn merge URL -rNEW:OLD

  NEW is the revision number of the checkin you want to revert, and OLD is typically NEW-1. Very nice:

  this reverts **all** changes made in revision NEW, no matter how many files were involved.

# Checkins 

Revision numbers apply to the entire repository, not just to single files. Every checkin conceptually creates a new version of the entire repository, uniquely identified by its revision number. This is very powerful, but subtle, and CVS has nothing like it. A glimpse of its power was given just above, talking about the ease of reverting an entire checkin in one easy gulp.

# Branching 

You\'re working on a trunk sandbox and discover it\'s going to take longer than you hoped. Now you wish you had created a branch. This is actually dead easy: create a new branch of the trunk. `svn switch` your sandbox to that new branch; this leaves your local change alone, which is key. `svn commit` \-- you\'re done! There\'s now a branch on the server matching your fiddled local state.

    svn cp -m "Create new branch from rev xxx." svn+ssh://pythondev@svn.python.org/python/trunk \
        svn+ssh://pythondev@svn.python.org/python/branches/my-branch
    svn switch svn+ssh://pythondev@svn.python.org/python/branches/my-branch
    svn ci -m "Commit first modifications on my branch."

Making a branch or tag goes very fast under SVN. Because branches and tags are just conventionally-named directories, you can delete them (like any other directory) when you\'re done with them. These conspire to make simple applications of branches much more pleasant than under CVS.

# File Modes 

CVS uses text mode for files by default. SVN uses binary mode. The latter is safer, but creates endless low-level snags for x-platform development. I encourage Python developers to include this gibberish in their SVN config file:

    [auto-props]
    # Setting eol-style to native on all files is a trick:  if svn
    # believes a new file is binary, it won't honor the eol-style
    # auto-prop.  However, svn considers the request to set eol-style
    # to be an error then, and if adding multiple files with one
    # svn "add" cmd, svn will stop adding files after the first
    # such error.  A future release of svn will probably consider
    # this to be a warning instead (and continue adding files).
    * = svn:eol-style=native
    *.c = svn:keywords=Id
    *.h = svn:keywords=Id
    *.py = svn:keywords=Id

Then SVN will set the necessary `svn:eol-style` property to \"native\" on new text files you commit. I\'ve never yet seen it tag a file inappropriately using this trick, but it\'s guaranteed to screw up \_all\_ text files without something like this (unless you have the patience and discipline to manually set eol-style=native on all new text files you add).

For the above to work you will also have to make sure the `enable-auto-props` configuration key is set to \"yes\".
