# WebsiteBuilderSetup

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

[CharlieGroves](CharlieGroves), incept: 2006-08-27

Jython uses reStructuredText and a custom writer to build its site. This describes how to set it up.

1.  Download and install [docutils](http://docutils.sourceforge.net/). Grab it from the site and go through the normal \'python setup.py install\' deal. Note that a docutils egg will **NOT** work here (possibly pending some packaging changes to jysite).

2.  Grab the site builder out of svn and install it.
    - svn co https://jython.svn.sourceforge.net/svnroot/jython/trunk/sandbox/wierzbicki/jysite
          cd jysite
          python setup.py install

3.  Check out the actual website code from `https://jython.svn.sourceforge.net/svnroot/jython/trunk/website`{.backtick}

4.  Make sure a Jython trunk checkout is available as `jython`{.backtick} at the same level as `website`{.backtick}.

Now you can build the site using Ant. Change into your checkout directory and run `ant`{.backtick} to build the site. The reStructuredText files that comprise most of the site are in the `Project`{.backtick} directory.

To deploy the site:

1.  Edit `build.xml`{.backtick} to change the `scp.user`{.backtick} property (if your name isn\'t Frank Wierzbicki).

2.  Run `ant copy2sf`{.backtick} to build a tar.bz2 of the site and scp it to sourceforge

3.  `ssh shell.sourceforge.net`{.backtick}

4.  Unpack the site

<!-- -->

    cd /home/groups/j/jy/jython/htdocs
    tar xfj ../website.tar.bz2

You\'ll want to have `umask 002`{.backtick} and `newgrp jython`{.backtick} in your .bash_login so the site is updatable by others as well.
