# TrackerDevelopmentVirtualEnv

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

This page is derived from [TrackerDevelopment](TrackerDevelopment).

Not only does this cover installing under a virtualenv, but it also covers installing Rietveld. That part is not entirely finished, however.

# Before You Get Started 

## Prerequisites 

1.  Python 2.7 (or 3?)
2.  pip (under same Python)
3.  svn
4.  postgresql 9 server (devel)
5.  openssl (devel)
6.  swig
7.  patch
8.  virtualenvwrapper (pip install virtualenvwrapper)

## Will be Installed 

1.  psycopg2
2.  beautifulsoup
3.  m2crypto

## Environment Variables 

Set them however you like!

    export WORKON_HOME=~/.envs
    export PROJECT_DIR=~/projects
    export MAIL_DOMAIN=spam.eggs
    export TRACKER_HOST=localhost
    export TRACKER_PORT=9999

## virtualenvwrapper Initial Setup 

    echo "export WORKON_HOME=$WORKON_HOME" >> ~/.bashrc
    mkdir -p $WORKON_HOME
    source `which virtualenvwrapper.sh`

# The Main Course 

## Initial Preparation 

    mkvirtualenv tracker  # leaves you in the virtual environment
    pip install psycopg2
    pip install beautifulsoup
    pip install m2crypto  # http://stackoverflow.com/questions/7772965/
    cd $VIRTUAL_ENV/build/m2crypto 
    chmod u+x fedora_setup.sh
    ./fedora_setup.sh build
    ./fedora_setup.sh install
    echo 'export PGDATA=$VIRTUAL_ENV/pg_data' >> $VIRTUAL_ENV/bin/postactivate

## Set Up Postgresql 

    workon tracker
    mkdir $PGDATA
    pg_ctl initdb
    # if needed, fix auth in $VIRTUAL_ENV/pg_data/pg_hba.conf
    pg_ctl start
    psql -c 'create user roundup' postgresql
    psql -c 'alter user roundup with createdb' postgresql

## Install Roundup 

    workon tracker
    cd $PROJECT_DIR
    svn co http://svn.python.org/projects/tracker
    cd tracker/roundup-src
    python setup.py install

## Configure the Python-Dev Instance 

    workon tracker
    cd $PROJECT_DIR/tracker/instances/python-dev
    mkdir db
    echo postgresql > db/backend_name
    cp config.ini.template config.ini # and adjust settings
    sed -i "s/localhost:9999/$TRACKER_HOST:$TRACKER_PORT/" config.ini
    sed -i "s/#domain = NO DEFAULT/domain = $MAIL_DOMAIN/"
    sed -i 's/\(def init(db):.*\)$/\1\n    return/' detectors/rietveldreactor.py
    $VIRTUAL_ENV/bin/roundup-admin -i `pwd` init

## Fire It Up 

    workon tracker
    cd $PROJECT_DIR/tracker/instances/python-dev
    echo "export RU_INSTANCE=`pwd`" >> $VIRTUAL_ENV/bin/postactivate
    echo "export RU_HOST=$TRACKER_HOST" >> $VIRTUAL_ENV/bin/postactivate
    echo "export RU_PORT=$TRACKER_PORT" >> $VIRTUAL_ENV/bin/postactivate
    echo '"alias start-roundup=$VIRTUAL_ENV/bin/roundup-server -n $RU_HOST -p $RU_PORT python-dev=$RU_INSTANCE"' >> $VIRTUAL_ENV/bin/postactivate
    echo '"alias admin-roundup=$VIRTUAL_ENV/bin/roundup-admin -i $RU_INSTANCE"' >> $VIRTUAL_ENV/bin/postactivate
    start-roundup # and point your browser to localhost:9999

## Install Rietveld 

This part isn\'t working all the way, and is likely incorrect/missing pieces.

    workon tracker
    cd $PROJECT_DIR/tracker/instances/python-dev/rietveld
    make all
    cd $PROJECT_DIR/tracker/instances/python-dev/detectors
    ../scripts/initrietveld
