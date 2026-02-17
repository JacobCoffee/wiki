# Admin/Mercurial

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# Mercurial setup 

![/!\\](/wiki/europython/img/alert.png "/!\") *Please note: The administration pages have all been migrated to the new [PSF Systems Wiki](https://psf.projecthut.com/trac/psfsystems/wiki). Please no longer add information to these pages. If you need access to the new wiki, please contact [psf@python.org](mailto:psf@python.org) for details.*

Mercurial services (hg.python.org) are currently hosted on dinsdale.python.org. Everything is under user `hg`{.backtick}\'s home directory in `/data/hg`{.backtick}.

Mercurial itself uses a recent stable build, with a couple of custom patches. The Mercurial tree is in `~hg/mercurial`{.backtick}. The patches are in named branch `local`{.backtick}, which is branched off branch `stable`{.backtick}. This source tree is installed in `~hg/lib/python`{.backtick}, using `make install-home`{.backtick}.

Scripts are in `~hg/bin`{.backtick}, which is versioned using Mercurial:

- `genauth`{.backtick} regenerates the `.ssh/authorized_keys`{.backtick} file using the current committers\' public keys

- `hg-ssh`{.backtick} is used as a shell for remote logins of user `hg`{.backtick}, in order to restrict them to a few safe commands

- `gcrepos`{.backtick} detects \"stale\" repositories in a directory (\"stale\" meaning having received no new changesets since their creation), so as to enable garbage-collecting of unused server-side clones; this still needs wrapping in a cronjob

- `hg`{.backtick} itself is the Mercurial executable installed by `make install-home`{.backtick}

Public repos are in `~hg/repos`{.backtick}. They are served using two mechanisms:

- for the `ssh://...`{.backtick} URLs (which allowing pushing), by the `hg-ssh`{.backtick} script mentioned above

- for the `http://hg.python.org/...`{.backtick} URLs, using WSGI script `~hg/wsgi/python.wsgi`{.backtick} run by a mod_wsgi instance in daemon mode under user `hg`{.backtick}. This script itself uses configuration file `~hg/repos.conf`{.backtick}.

Noteworthy amongsth these repos are:

- `hooks`{.backtick} contains a variety of hooks used for other repos (such as whitespace checking)

- `pymigr`{.backtick} contains scripts and data for the SVN to Mercurial conversion

- `test`{.backtick} is a test repo for committers

------------------------------------------------------------------------

[CategoryPythonWebsite](CategoryPythonWebsite)
