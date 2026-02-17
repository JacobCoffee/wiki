# SvnToHgMigration

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

::: 
### Svn to Hg Migration

The main Jython repo is hosted at:

[http://hg.python.org/jython](http://hg.python.org/jython)

The checkins mailing list has also moved from SF.net to python.org:

[http://mail.python.org/mailman/listinfo/jython-checkins](http://mail.python.org/mailman/listinfo/jython-checkins)

You should read the CPython devguide, we\'ll for the most part follow their mercurial workflow:

[http://docs.python.org/devguide/](http://docs.python.org/devguide/)

We have a bitbucket mirror setup at [http://bitbucket.org/jython](http://bitbucket.org/jython) to ease forks (and pull requests).

TODO: We\'ll probably want to grant all Jython committers access to the bitbucket account so they can publish personal repos (and branches) under this account. That way we can keep feature branches out of the main repo but still easily follow all committers\' work.
:::

::: 
### Where\'d my feature branch go?

Another read-only repo includes all unmerged feature branches from subversion, located at:

[http://hg.python.org/jython-fullhistory](http://hg.python.org/jython-fullhistory)

These branches are stored in the fullhistory repository as Mercurial bookmarks:

    $ hg incoming -B http://hg.python.org/jython-fullhistory
    comparing with http://hg.python.org/jython-fullhistory
    searching for changed bookmarks
    2.0                       80ec4a2935cf
    advanced                  83b99db43823
    antlr                     9421b912c882
    asm_compiler              b728b1f57041
    august-boulder-sprint     fb5e5b753ac3
    ctypes-via-rawffi         7824236e7d68
    customizable-proxymaker   a6f4fbd0dde7
    indy                      f5a16157033d
    jy26                      01bccefd742d
    jy3k                      401eab15f3a3
    jythonc                   f7d4ba23e11e
    newstr                    e236b28ee585
    py25                      2ec5f236a1a6
    unicodedata               a7d458092892
    unlabeled-1.1.2           1099b851db45

(Note that many of these branches are abandoned or very old)

If you wanted to e.g. continue work on the old newstr feature branch, you\'d do the following:

    # First get the main repo
    hg clone http://hg.python.org/jython
    # Pull in the newstr bookmark from the archive. You could preface this command with: hg incoming -r newstr
    hg pull -B newstr http://hg.python.org/jython-fullhistory
    # optionally bookmark the current tip so you can easily get back to it later
    hg book my-tip
    hg up newstr # and go to work
    # then when you're done
    hg up my-tip

TODO: mention merge -P and the log equivalent for a log of the old branch

TODO: mention how to merge from default to aid in later merges ( [http://codespeak.net/svn/pypy/extradoc/planning/hg-migration/active-branches-howto.txt](http://codespeak.net/svn/pypy/extradoc/planning/hg-migration/active-branches-howto.txt) )
:::

::: 
### Issues

1.  The svn:externals were converted to \[svn\] subrepos. Beware there\'s a bug with this feature that affects our repo when switching to revisions with different externals, more info (with the workaround) here: http://mercurial.selenic.com/bts/issue2752
2.  Beware the svn:externals checkout can also appear to lockup mercurial if your subversion config lacks the python.org SSL certificate: http://mercurial.selenic.com/bts/issue2759
:::

::: 
### Svn to Hg Map

[svnmap.txt](attachments/SvnToHgMigration/jython-svnmap.txt) contains a mapping of original svn revision (and its original subversion branch name) to its hg revision.

This data can also be gathered from the hg repo itself, the original subversion revision and location information is contained the Mercurial extras field (hg log \--template {extras})
:::

::: 
### Migration Details

The conversion was basically done via:

fix-svn.sh & convert-jython.sh

from: [http://bitbucket.org/pjenvey/pymigr](http://bitbucket.org/pjenvey/pymigr)

These need to be ran with a modified version of hgsubversion, from here (with all three mq patches applied):

[http://bitbucket.org/pjenvey/hgsubversion-jython-conv](http://bitbucket.org/pjenvey/hgsubversion-jython-conv)

After the conversion is complete a couple other things are done:

1.  Create a jython-svnmap.txt (maps svn revisions/branch names to hg ids) via jython-svnmap.py
2.  Create bookmarks for the fullhistory repo with jython-old-branches.txt jython-svnmap.txt and jython-bmarks2hg.py (believe the final output still needs some fixing to create \'hg book\' commands)
3.  Finally, dummy merge up the stable branches
:::

::: 
### TODO

1.  More testing/feedback/ssh keys from committers\*
2.  Go live\*
3.  Ask bitbucket for a mirror\*
4.  Modify pom.xml scm location\*
5.  Fix the buildbot repo location (buildbot currently broken anyway)
6.  build.xml may need some fixes (references many svn things likely for release management)

Additionally:

1.  Convert installer and website repos
:::
