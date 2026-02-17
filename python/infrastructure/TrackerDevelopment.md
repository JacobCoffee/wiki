# TrackerDevelopment

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

::: caution
**Roundup tracker has been retired in favour of [GitHub](./GitHub.html) issues.** See [https://github.com/psf/gh-migration](https://github.com/psf/gh-migration)
:::

This page is dedicated to development of Python bug tracker instance at [http://bugs.python.org/](http://bugs.python.org/)\
We have a [meta tracker](http://psf.upfronthosting.co.za/roundup/meta/) for current issues and [DesiredTrackerFeatures](DesiredTrackerFeatures) page for recording ideas. See also [TrackerDevelopmentPlanning](TrackerDevelopmentPlanning).

# Docker 

The simplest way to work with the tracker is by using Docker.

Clone [the docker-bpo repo](https://github.com/python/docker-bpo) and follow the README.

If you want to install the tracker manually follow the instructions below.

# Requirements 

This configuration is deployed on production server, so it is good to stick it for development as well:

- Roundup 1.4.20+ (patched version)

- PostgreSQL (as a backend database)

- psycopg2 (bindings for the above)

- pyoidc (OpenID Connect library from [https://github.com/rohe/pyoidc](https://github.com/rohe/pyoidc))

[http://bugs.python.org/](http://bugs.python.org/) (`python-dev`{.backtick} tracker instance or configuration) is running PostgreSQL on backed, because it has the best performance for large installations. Besides, there is at least one place in the `python-dev`{.backtick} config with hardcoded dependency on the SQL-based backed.

## Getting the source 

Get patched version of [Roundup tracker](http://www.roundup-tracker.org/) from here:

- [http://hg.python.org/tracker/roundup/](http://hg.python.org/tracker/roundup/) (the changes are in the `bugs.python.org`{.backtick} branch)

Tracker configuration for [http://bugs.python.org/](http://bugs.python.org/) (called \'tracker home\', \'instance\' or \`environment) is here:

- Official: [http://hg.python.org/tracker/python-dev/](http://hg.python.org/tracker/python-dev/)

- Mirror: [https://bitbucket.org/rirror/bugs.python.org](https://bitbucket.org/rirror/bugs.python.org)

## Other tracker configurations 

There are several Roundup trackers used for Python development. Configuration for them is maintained in [http://hg.python.org/tracker/](http://hg.python.org/tracker/) repositories:

- **roundup**: a clone of the original Roundup with our modifications;

- **python-dev**: the instance used on bugs.python.org;

- **meta**: the instance used for the meta tracker;

- **jython**: the instance used for the jython tracker;

- **setuptools**: the instance used for the setuptools tracker;

- **rietveld**: a clone of Rietveld used to do reviews on the bug tracker;

- **django-gae2django**: a clone of django-gae2django necessary for rietveld;

# Setup bugs.python.org instance 

## Install patched Roundup 

Clone code and switch to `bugs.python.org`{.backtick} branch before installing. Here it is installed to hardcoded system-wide location at `/opt/tracker-roundup/`{.backtick}.

- Read-only clone

      hg clone http://hg.python.org/tracker/roundup

- Read/Write clone (if you have write access to the repository)

      hg clone ssh://hg@hg.python.org/tracker/roundup

<!-- -->

    cd roundup
    hg up bugs.python.org
    sudo python setup.py install --prefix /opt/tracker-roundup/

## Checkout the python-dev instance 

- Read-only clone

      hg clone http://hg.python.org/tracker/python-dev

- Read/Write clone (if you have write access to the repository)

      hg clone ssh://hg@hg.python.org/tracker/python-dev

## Checkout the Rietveld integration (optional) 

If you want to work on Rietveld code review tool, check out the django-gae2django and rietveld clones in the python-dev/ directory:

- Read-only clone

      cd python-dev
      hg clone http://hg.python.org/tracker/django-gae2django/
      hg clone http://hg.python.org/tracker/rietveld/

- Read/Write clone (if you have write access to the repository)

      cd python-dev
      hg clone ssh://hg@hg.python.org/tracker/django-gae2django/
      hg clone ssh://hg@hg.python.org/tracker/rietveld/

After getting the clones **remember to update the branches to bugs.python.org**:

    cd django-gae2django
    hg up bugs.python.org
    cd ..
    cd rietveld
    hg up bugs.python.org

In addition, Django needs to be installed; e.g. the Django 1.2 or 1.3 Debian packages work fine.

## Install psycopg2 (PostgreSQL access library for Python) 

For Debian/Ubuntu:

    sudo apt-get install python-psycopg2

For other systems, follow instructions from [psycopg2 site](http://initd.org/psycopg/install/).

## Install and configure PostgreSQL 

Other backends may work, but it is recommended to keep development environment close to production.

It has been reported that 8.2, 8.3, 8.4, and 9.1 work well. See [UpgradingPostgreSQL](UpgradingPostgreSQL) if you need to upgrade version.

Access control in PostgreSQL is tricky. You need to know Unix user, under which you run Roundup, setup access for him to PostgreSQL database, and add PostgreSQL user that you\'ve configured in Roundup\'s configuration.

For a development environment the easiest way is to allow any user from localhost to connect as any database user. This can be accomplished by editing pg_hba.conf (usually found in /etc/postgresql/9.x/main/ in Linux or /Library/PostgreSQL/9.x/data/ in Mac OS X \-- you might need privileges to edit it). The end of the file should look like this (the four changed lines are preceded by ##):

    # Database administrative login by UNIX sockets
    ##local   all         postgres                          ident
    local   all         postgres                          trust

    # TYPE  DATABASE    USER        CIDR-ADDRESS          METHOD

    # "local" is for Unix domain socket connections only
    ##local   all         all                               ident
    local   all         all                               trust
    # IPv4 local connections:
    ##host    all         all         127.0.0.1/32          md5
    host    all         all         127.0.0.1/32          trust
    # IPv6 local connections:
    ##host    all         all         ::1/128               md5
    host    all         all         ::1/128               trust

**PLEASE NOTE**: This is not a secure configuration on a multi-user machine.

After the change in pg_hba.conf, reload your postgreSQL database to make sure it knows about your new access configuration. Something similar to

    sudo /etc/init.d/postgresql reload

should do the trick on Unix-like platforms.

On Mac OS X, do `sudo su - postgres`. Then use pg_ctl to restart the server:

    /Library/PostgreSQL/9.x/bin/pg_ctl restart -D /Library/PostgreSQL/9.x/data

Create a database user that is allowed to create databases. This user will be used when roundup connects to the database.

    $ psql -U postgres
    postgres=# create user roundup;
    postgres=# alter user roundup with createdb;

## Configure your Development Roundup Instance 

Now enter the python-dev directory, and create the \'db\' directory, as well as the db/backend_name file which decides which backend (i.e. database type) to use:

    cd python-dev
    mkdir db
    echo postgresql > db/backend_name

Note: the db dir contains all the messages and files attached to issues, and it\'s removed and recreated every time you run `roundup-admin init`.

Copy `python-dev/config.ini.template` into `config.ini` and `detectors/config.ini.template` into `detectors/config.ini`:

    cp config.ini.template config.ini
    cp detectors/config.ini.template detectors/config.ini

The former will let you configure your roundup instance; the latter, detectors such as **irker**, **busybody**, or **tellteam**.

In config.ini pay special attention to settings marked with *NO DEFAULT*.

`config.ini.template` already contains some useful default values for a development enviroment, for example

    debug = debugmail.txt

at the end of the `[mail]` section saves outgoing mails on a local file; and

    debug = on

at the end of the `[web]` section shows tracebacks in the browser instead of having them sent by email.

Initialize your roundup instance:

    /opt/tracker-roundup/bin/roundup-admin -i <your python-dev directory> init

Provide a password for the \'admin\' user when asked for.

**Note**: you have to provide the full path to your python-dev directory, otherwise the command will fail.

If you are getting the error:

- \"`roundup.hyperdb.DatabaseError: FATAL:  password authentication failed for user "roundup"`\" check again pg_hba.conf;

- \"`roundup.configuration.OptionUnsetError: MAIL_DOMAIN is not set and has no default`\" set the option in python-dev/config.ini, \[mail\] section, domain;

Start your roundup instance:

    /opt/tracker-roundup/bin/roundup-server -p 9999 python-dev=<your python-dev directory>

You will have to use this command every time you (re)start roundup, so it\'s easier to create an alias for it with:

    alias start-roundup='/opt/tracker-roundup/bin/roundup-server -p 9999 python-dev=<your python-dev directory>'

It might be a good idea to create another alias for roundup admin too:

    alias admin-roundup='/opt/tracker-roundup/bin/roundup-admin -i <your python-dev directory>'

then add them to your `.bashrc` (or `~/.profile` in Mac OS X)

You should now be able to browse [http://localhost:9999/python-dev/](http://localhost:9999/python-dev/) and get a roundup instance that looks just like [http://bugs.python.org](http://bugs.python.org), except for some missing new values for fields like Stages and Keywords. It\'s possible to replace **initial_data.py** with an [updated version](./TrackerDevelopment(3f)action(3d)AttachFile(26)do(3d)view(26)target(3d)initial_data_updated(2e)py.html) so that your fields will have values that match those currently present in the Python Tracker.

The IDs for values in a given field might be different from those in the Python Tracker. This should only be a problem if you try to import CSV files from one tracker into the other.

Create an user from User-\>register in the left sidebar. Note that if you have set `debug = debugmail.txt` as suggested above, you will have to open the file and copy the URL in the browser (make sure to replace `=3D` with `=` in the URL and to remove the trailing `=` where the url is broken at the end of the line). You can then use roundup-admin to set developer privileges for it:

    /opt/tracker-roundup/bin/roundup-admin -i <your python-dev directory>
    Roundup 1.5.0 ready for input.
    Type "help" for help.
    roundup> display user3
    ...
    roundup> set user3 roles=User,Developer,Coordinator
    roundup> commit
    roundup>

You can find your user id clicking on \"Your Details\" in the left sidebar and then looking at the address bar (it should show something similar to [http://localhost:9999/python-dev/user3](http://localhost:9999/python-dev/user3)).

## Rietveld Setup 

The Roundup and Rietveld data are stored in the same Postgres database. After the Roundup tables have been created, add to python-dev/config.ini:

    [django]
    secret_key = <the_secret_key>

To generate the secret key you can use an online django secret key generator, or just put an arbitrary string.

Before continuing make sure to check with \"hg branch\" that the branch is \"bugs.python.org\" on both the rietveld and the django-gae2django clones.

    cd rietveld
    python manage.py syncdb
    cd ..
    PYTHONPATH=detectors/:/opt/tracker-roundup/lib/python2.7/site-packages/ python scripts/initrietveld

If you are upgrading from an older installation, review the revision history of rietveld/migration.

To run the Rietveld code, do

    python manage.py runserver

This will run Rietveld by default on port 8000. Alternatively to the development server, you can also configure your web server to run rietveld.wsgi under the /review URL.

Rietveld patchset creation is an offline activity. If you have new patches in your tracker instance, run

    scripts/addpatchsets

If you get errors like:

    django.db.utils.DatabaseError: column codereview_repository.guid does not exist
    LINE 1: ...itory"."url", "codereview_repository"."owner_id", "coderevie...

you can try to remove the table(s) from the database and re-run syncdb and initrietveld:

    $ psql -U roundup
    psql (9.1.4)
    Type "help" for help.

    roundup=> \d codereview_repository
         Table "public.codereview_repository"
    ... check here if some column is missing and if it is drop the table ...
    roundup=> drop table codereview_repository cascade;
    NOTICE:  drop cascades to constraint codereview_branch_repo_id_fkey on table codereview_branch
    DROP TABLE
    roundup=> \q

    $ cd rietveld
    $ python manage.py syncdb
    Creating tables ...
    Creating table codereview_repository
    Installing custom SQL ...
    Installing indexes ...
    No fixtures found.
    $ cd ..
    $ PYTHONPATH=detectors/:/opt/tracker-roundup/lib/python2.7/site-packages/ python scripts/initrietveld

## irker setup 

irkerd is a daemon that sends notification on IRC whenever a message is added or an issue is created, and replaces the CIA.vc service.

You will need:

\* irker: [http://www.catb.org/esr/irker/](http://www.catb.org/esr/irker/)

\* the irc package: [http://pypi.python.org/pypi/irc/](http://pypi.python.org/pypi/irc/)

To install them you can use:

    wget http://pypi.python.org/packages/source/i/irc/irc-5.0.1.zip
    unzip irc-5.0.1.zip
    cd irc-5.0.1/
    sudo python setup.py install
    cd ..

    wget http://www.catb.org/~esr/irker/irker-1.17.tar.gz
    tar -zxvf irker-1.17.tar.gz

If you get the error `ImportError: No module named hgtools.plugins` during the `sudo python setup.py install`, you can try the command again and it should automagically work.

Make sure that you have listed the address of the channels that should receive the messages in `detectors/config.ini`, e.g.:

    [irker]
    channels = irc://chat.freenode.net/python-dev

To start irker use:

    cd irker-1.17/
    ./irkerd &

You can also use `./irkerd -d3` to see debugging messages.

# Resources for Tracker Development 

## Getting Help 

Subscribe to and ask your question on the tracker-discuss mailing list. See [http://mail.python.org/mailman/listinfo/tracker-discuss](http://mail.python.org/mailman/listinfo/tracker-discuss)

Since the Python Tracker is a slightly modified version of [Roundup](http://www.roundup-tracker.org), both Roundup\'s [Documentation](http://www.roundup-tracker.org/docs.html) and [issue tracker](http://issues.roundup-tracker.org/) contain relevant information about how the Python Tracker works and problems one might find working with its code.

## Using roundup-admin 

To start roundup-admin interactively use:

    /opt/tracker-roundup/bin/roundup-admin -i <your python-dev directory>

To get the list of users, issues, msgs, files, etc:

    roundup> list user

To see info about a specific user, issue, msg, file, etc:

    roundup> display userXXX

To change the role of an user:

    roundup> set userXXX roles=User,Developer
    roundup> commit

Users have limited privileges and can edit just some of the fields in the issue page. Developers can edit all the fields and remove msgs and files. Coordinators can also mark/unmark messages as spam and change some of the settings of other users (e.g. if they submitted the contributor agreement).

To add back a message deleted accidentally:

    roundup> set issueXXX messages=+YYY
    roundup> commit

The message will be added back in the right position. (This should be equivalent to b.p.o/issueXXX?@action=edit&@add@messages=YYY, but this doesn\'t seem to work.)

## The Meta Tracker 

A [Meta Tracker](http://psf.upfronthosting.co.za/roundup/meta/) is available for handling bugs and features requests for the [Python Tracker](http://bugs.python.org/).

## Setting Up an Instance in a VirtualEnv 

See [TrackerDevelopmentVirtualEnv](TrackerDevelopmentVirtualEnv).

## The Test Tracker 

Public test instance of the Python tracker: [http://bot.bio.br/python-dev/](http://bot.bio.br/python-dev/) (currently offine)

Instance that attempts to match the code used in [http://bugs.python.org](http://bugs.python.org) to allow testing, reproducing and verifying fixes for tracker bugs. Can also be used as a sandbox by users interested in learning about Developer, Coordinator or Admin tasks and features. Testing new content (e.g. Components or Statuses) is OK, but new features show be tested in the Experimental Tracker instead.

Currently the email system is disabled (redirected to file), so people interested in having an account there to test new features should email [tracker-discuss](http://mail.python.org/mailman/listinfo/tracker-discuss) to get one. Maintained by [DanielDiniz](DanielDiniz).

## The Experimental Tracker 

Modified version of the Python tracker: [http://bot.bio.br/python-dev-exp/](http://bot.bio.br/python-dev-exp/) (currently offline)

It\'s an instance to showcase and test new features.

New features (2009-04-18):

- [Issue tags](http://mail.python.org/pipermail/tracker-discuss/2009-April/002099.html)

- [Quiet properties](http://psf.upfronthosting.co.za/roundup/meta/issue249)

- [Restore removed messages and files](http://psf.upfronthosting.co.za/roundup/meta/issue267)

- [Claim (\'assign to self\') and add/remove self as nosy buttons](http://psf.upfronthosting.co.za/roundup/meta/issue258)

- [Don\'t close issues with open dependencies](http://psf.upfronthosting.co.za/roundup/meta/issue266)

- [Auto-add nosy users based on Components](http://psf.upfronthosting.co.za/roundup/meta/issue258)

- [\"Email me\" buttons for messages and issues, \"Reply by email\"](http://psf.upfronthosting.co.za/roundup/meta/issue245)

- [RSS feeds (per issue and global)](http://psf.upfronthosting.co.za/roundup/meta/issue155)

- [Display selected issues in the index view](http://psf.upfronthosting.co.za/roundup/meta/issue246)

- [Mass-update/batch-editing support](http://psf.upfronthosting.co.za/roundup/meta/issue248)

Currently the email system is disabled (redirected to file), so people interested in having an account there to test new features should email [tracker-discuss](http://mail.python.org/mailman/listinfo/tracker-discuss) to get one. Maintained by [DanielDiniz](DanielDiniz).

There is also a list of additional [DesiredTrackerFeatures](DesiredTrackerFeatures) for which no patches yet exist.

# Getting Your Own Jython Tracker 

To set up a local Jython tracker, please follow instructions for python-dev tracker with following exceptions:

- There is no **CIA.vc** detector

- The repository for Jython tracker can be cloned with:

<!-- -->

    hg clone http://hg.python.org/tracker/jython/

------------------------------------------------------------------------

[CategoryTracker](CategoryTracker) [CategoryDevelopmentProcess](CategoryDevelopmentProcess)
