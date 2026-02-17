# StarshipTransfer

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# Starship Python has Moved! 

On September 1, 2003, the machine that has been hosting Starship Python (courtesy of Zope Corporation) has been shutdown. Consequently, Starship has being transferred to a new machine, kindly provided by Stefan Drees. This page exists as a record for the Starship admins, so they can keep track of what tasks had to be done, for the successful transfer to happen smoothly. We are currently in the everlasting post-transfer phase, where new features and services are enabled. Probably we should list the core and special features of the current machine here\...

If you\'re a Starship admin, feel free to update this page. Otherwise, please email [webmaster@python.net](mailto:webmaster@python.net) if you want to add stuff to our to-do list.

## Tasks for old Starship 

- determine disk usage patterns (ie. which directories use up the most space, and which users are responsible for those directories)

  \
  \[done: gward 2003/08/09\]

- browbeat top disk space users into cleaning up

  \
  \[partly done: gward 2003/08/10; but some of the top users \@python.net addresses bounce\]

- find out which users no longer have a valid \@python.net email address, and then run the

  following loop:\

        for each user with no known forwarding address:
          if (user is "well-known" in the Python community) or
             (user has anything meaningful on starship):
            google to try to find a recent email address
            contact the user and ask:
              do they still need their starship account?
              what's their preferred email forwarding address?
              what's their SSH key (preferably SSHv2)?
          else:
            remove that user's account and all of their files

  \
  \[assigned: gward\]

## Tasks for new Starship 

- upgrade to Debian \'testing\' (sarge)

  \
  \[done: sdrees 2003/08/07\]

- give the machine a proper hostname

  \
  (will have to be in python2.net domain for now; once DNS service is transferred to a new provider, we can give it a python.net name \-- anything but starship.python.net, of course!) Proposed proper hostname: drydock.python2.net ![;)](/wiki/europython/img/smile4.png ";)")\
  \[done: sdrees 2003/08/10\]

- get email services working

  \
  (hmmm: testing this stuff will require have at least one real user on the system. I guess I\'ll create a temporary throwaway account rather than transfer real data over yet.)

  - install Exim 4 packages (**critical path**)\
    (from unstable? or are they in testing yet?)\
    (tismer says: use exim-tls \-- but is that necessary with the new exim4 packages?\
    \[done: gward 2003/08/24; ended up getting 4.22-1 source package from unstable and building custom 4.22-gw1 packages\]

  - configure/test Exim (**critical path**)\
    \[done: gward 2003/08/24\]

  - get elspy working with Debian Exim packages (**critical path**)\
    (recompile necessary? or just fix elspy to work with dlopen() patch?)\
    \[done: gward 2003/08/24\]

  - install Courier (\"semi-critical\" for mwh\--anyone else?)

    \
    (SSL daemon only) (IMAP only? or POP too?)\
    \[assigned: gward\]

  - configure/test Courier

    \
    \[assigned: gward\]

- web services
  - install, configure, and test Apache (**critical path**)\
    (with mod-proxy, mod-rewrite, and mod-ssl, please! Content data is already transfered by greg 2003/08/25)\
    \[done: admins 2003/08/26\]\
    \[.cgi/.spy files enabled for crew, Server Name updated to starship.python.net Jim 2003/08/27\]\
    \[enabled server side includes for .shtml files Jim 2003/08/28\]

  - install, configure, and test Zope (**not** critical path)\
    (Zope 2.7 preferable; (really?) note that Debian testing has Zope 2.6.1 and a working plone on top ![;)](/wiki/europython/img/smile4.png ";)") )\
    \[installed 2.6.1 with plone \-- sdrees 2003/08\]

- install, configure, and test ProFTPd (**critical path**)\
  \[done: sdrees 2003/08/12\]

- install, configure, and test Mailman (**critical path**)\
  (it\'s installed, and seems to be working \-- but list data has not been transferred. I\'m going to let someone else worry about it. \--gward 2003/08/27)\
  \[done: jim 2003/08/27\]

- Install Python and third party modules: \[assigned: tbryan\]
  - Motivation - One of Christian\'s goals in founding the Starship was to give developers a chance to play with the latest and greatest stuff and to show off Python\'s capabilities
  - History - We have built our own local copy of Python, with as many optional modules enabled as possible, since 1999.
  - Implementation - I was downloading the Python source, using Red Hat\'s RPM and our own custom Steup.local to build a custom binary RPM of Python for the starship
  - Third party modules - We have normally installed PIL, HTMLGen, and the mx\* extensions for every Python release; we\'d like to build more third party modules
  - Future - I\'d like to reduce the amount of manual work involved in installing a new Python version. I\'d like to tie in with the platform\'s package management system. I\'d like to see nightly builds from CVS made available to crew members.
  - Plan - Install Python 2.2 and Python 2.3 with our normal third party modules as locally built software in /usr/local/. That will ensure some continuity in the short term when we move to the new Starship. After the move is complete, we can spend some time later to work out how we want to handle our local Python installations on a Debian machine. Then I\'ll remove the hand-built /usr/local/ installs and implement the new strategy.

- compare /etc/{passwd,group,shadow} and friends on both ships, evaluate migration strategy of credential data (**critical path**)\
  user credential transfer will be greatly simplified by starship policy of using ssh keys for authentication. So the (shadowed) passwords will be a local secret \... greg wrote a little script already\
  \[done: gward ![;)](/wiki/europython/img/smile4.png ";)") \]

## Tasks for python.net DNS 

- find/select a good DNS provider (not critical path, but desirable)

  \
  (sdrees uses schlundtechnologies.com and has no complaints about it and has finalized transfer of python2.net to schlundtechnologies.com)\
  (gward uses dyndns.org and has no complaints about it)\
  (alternately, we could run the primary nameserver on starship, and use a commercial provider for the secondary nameserver)

- transfer python.net domain to new DNS provider (not critical path, but desirable)

  \
  (currently the DNS servers are at zope.com/baymountain.com, and Starship admins cannot edit the python.net DNS records)\
  \[assigned: tismer (he owns the domain!)\]

## Detailed transfer plan 

The transfer itself start at 2003-08-27 14:30 UTC.

- disabled logins on old starship

- shut down Exim, Courier-IMAP on old starship

- disabled any other user processes that might update the disk (eg. CGI scripts that write state)

- remounted home read-only on old machine

- rsynced user directories (this assumed the main bulk transfer had already been done)

- ensured ftpd running and working on new machine

- changed canonical name of new machine to starship.python.net (not being able fixing reverse DNS resolution, since hosting provider is not capable \...)

- edit Apache config for name change (drydock -\> starship) and restart\

  - \[done: jim 2003/08/27\]

- edit Exim config for name change and restart

- DNS change so \"starship.python.net\" resolves to the new machine

- start Exim, Courier-IMAP on new machine

- enable user logins on new machine

Transfer completed at 2003-08-28 03:11 UTC.

Thanks to everyone who participated!

------------------------------------------------------------------------

[CategoryPythonWebsite](CategoryPythonWebsite)
