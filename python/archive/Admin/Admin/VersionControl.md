# Admin/VersionControl

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# Configuration File Version Control 

![/!\\](/wiki/europython/img/alert.png "/!\") *Please note: The administration pages have all been migrated to the new [PSF Systems Wiki](https://psf.projecthut.com/trac/psfsystems/wiki). Please no longer add information to these pages. If you need access to the new wiki, please contact [psf@python.org](mailto:psf@python.org) for details.*

## Bazaar Overview 

We are using Bazaar to track files in `/etc`{.backtick} on python.org machines. Bazaar, also known as BZR, is a version-control system written in Python.

The home page for Bazaar is at [http://bazaar-vcs.org/](http://bazaar-vcs.org/).

Send questions about the use of Bazaar on python.org to \<amk at python.org\>.

## Directories tracked 

On dinsdale:

    /etc/  -- various directories tracked
    /data/ -- initialized but nothing tracked yet

On ximinez:

    /etc/  -- various directories tracked
    /data/ -- MoinMoin configuration

On bag:

    /etc/  -- various directories tracked

## Bazaar cheatsheet 

The command-line interface resembles that of CVS, but the executable is named `bzr`{.backtick}.

A more detailed introduction to Bazaar\'s basic features is part of the docs: [http://doc.bazaar-vcs.org/bzr.dev/tutorial.htm](http://doc.bazaar-vcs.org/bzr.dev/tutorial.htm)

To get a list of available subcommands, run `bzr help`{.backtick}.

To get more details about one particular subcommand, run `bzr help <command-name>`{.backtick}.

### Setting your ID 

Bazaar remembers your ID and uses this ID when committing changes. If you\'re doing stuff as root, this means we won\'t know who made a particular change.

`/usr/bin/bzr`{.backtick} is a wrapper script that checks that the ID has been set, reporting an error and stopping when it hasn\'t been.

To set your ID, set the BZREMAIL environment variable:

    export BZREMAIL=admin-person@python.org

### Making changes 

To commit a change: `bzr commit -m "Add new virtual host" /etc`

If you omit the path name, committing will search the entire repository containing the current directory, so you don\'t need to supply the path if you\'re currently in `/etc`{.backtick}. It\'s OK to commit only a portion of the tree; if you\'re in `/etc/apache2`{.backtick} and do a commit specifying the current directory (`bzr commit .`), you\'ll only commit changes in `/etc/apache2`{.backtick} and its subdirectories.

To back out an uncommitted change: `bzr revert /etc/database.conf` restores the last committed version of the file.

The `revert`{.backtick} subcommand works recursively on directories, so `bzr revert /etc`{.backtick} will undo all the changes you\'ve made to the configuration files.

### What have I changed? 

`bzr status`{.backtick} lists the names of files that are different from the last committed version:

    root@matterhorn:/etc# bzr status
    removed:
      nanorc
    added:
      vnc.conf
    modified:
      syslog.conf
    root@matterhorn:/etc#

To get a diff-style display of changes, use `bzr diff`{.backtick}:

    root@matterhorn:/etc# bzr diff |less
    === removed file 'nanorc'
    --- nanorc
    +++ /dev/null
    @@ -1,314 +0,0 @@
    -## Sample initialization file for GNU nano
     ...
    === modified file 'syslog.conf'
    --- syslog.conf
    +++ syslog.conf
    @@ -56,16 +56,3 @@
     #      *.=debug;*.=info;\
     #      *.=notice;*.=warn       /dev/tty8

    -# The named pipe /dev/xconsole is for the `xconsole' utility.  To use it,
    -# you must invoke `xconsole' with the `-file' option:
    -#
    -#    $ xconsole -file /dev/xconsole [...]
    -#
    -#
    -daemon.*;mail.*;\
    -       news.crit;news.err;news.notice;\
    -       *.=debug;*.=info;\
    -       *.=notice;*.=warn       |/dev/xconsole
    -

The `--diff-options`{.backtick} switch can be used to change the output of the underlying `diff`{.backtick} program.

### Adding/removing files 

To begin tracking a new configuration file, it must be added to the repository and then committed:

    bzr add /etc/database.conf
    bzr commit -m "Add database config" /etc/

If you delete a tracked file using `rm`{.backtick}, Bazaar will notice it\'s gone and remove it from the repository when you commit:

    root@matterhorn:/etc# rm database.conf
    root@matterhorn:/etc# bzr status
    removed:
      database.conf
    root@matterhorn:/etc# bzr commit -m "Remove file"
    missing database.conf
    deleted database.conf
    Committed revision 9.
    root@matterhorn:/etc#

The `bzr rm`{.backtick} subcommand stops tracking a file, but does \*\*not\*\* remove the working copy in `/etc`{.backtick}.

## Viewing history 

`bzr log`{.backtick} displays all changes that have been made to the tracked files:

    root@bag:/etc# bzr log |less
    ------------------------------------------------------------                   
    revno: 3
    committer: XXX@python.org
    branch nick: etc
    timestamp: Sat 2007-03-03 04:14:44 +0100
    message:
      Add Apache files
    ------------------------------------------------------------
    revno: 2
    committer: XXX@python.org
    branch nick: etc
    timestamp: Sat 2007-03-03 00:16:43 +0100
    message:
      Add a bunch of postfix config files.

    ...

## Initializing a new machine 

Here\'s how to set up the version control on a new system.

1\. Initialize the `/etc`{.backtick} directory as a Bazaar repository.

    bzr init /etc

This will create a directory called `/etc/.bzr/`{.backtick} that stores the history of changes.

2\. Make the \'add\' and \'status\' subcommands ignore all files by default.

    bzr ignore '*'

This prevents a stray `bzr add`{.backtick} lacking arguments from adding lots and lots of files.

3\. Manually add the files you want to track:

    bzr add /etc/network/interfaces
    bzr add /etc/apache2/httpd.conf
     ...

4\. Commit for the first time:

    cd /etc
    bzr commit -m "Record configuration files"
