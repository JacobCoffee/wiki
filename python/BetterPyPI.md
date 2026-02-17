# BetterPyPI

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# stability and high availability 

we went in two directions to improve PyPI :

1\. add the mirroring protocol 2. make the PyPI server more reliable by pushing its storage in a redundant cloud.

## mirroring

The mirroring protocol (PEP 381) is implemented on server-side, I\'ve worked with Martin on this, and we have mirrors now:

Look at [http://pypi.python.org/mirrors](http://pypi.python.org/mirrors)

Also, there\'s a client that anyone can use to set up a mirror: [http://pypi.python.org/pypi/pep381client](http://pypi.python.org/pypi/pep381client)

The idea is that anyone in the community willing to maintain a mirror can do so. We add the mirror in the CND, and make it available for client tools to use. What\'s really missing right now is more integration on client-side.

\- Pip supports the mirroring protocol, and can fall back to a mirror, but I am not 100% sure this is a default behavior. (please correct me if it is now) - Buildout knows how to use \*another server\* than the main PyPI, so can manually switch to a mirror, but I don\'t think it\'s transparent. It should. - Distribute/Setuptools does not do anything for this, and should. - everything is already implemented in packaging/distutils2

The effect of the mirrors is that PyPI being down should not impact the community. This will be true once all tool are transparently using the mirrors.

## better infra 

The current plan is to have two primary load balancer VMs running Nginx acting as both balancer and SSL termination points. These will share a set of floating IPs using Heartbeat. Behind this will be the same Apache configuration currently in use (Apache serving static files and PyPI running as an FCGI script controlled by Apache) running on two VMs, both talking to the same master-slave Postgres 9 replication setup. Package files will initially be handled by a shared DRBD drive, however this may be obsoleted by the project to move file hosting to Cloudfront or another CDN.

A currently open question is how best to provide reliability and security for the SSH-based file upload system currently deployed on ximenez. Most likely we can setup the initial SSH endpoint on the load balancers to run a proxy to one of the main PyPI application servers, however failover would have to be semi-manual (possibly driven by Chef, meaning a chef-client run would have to happen before the tunnel would be updated, or anywhere up to 30 minutes). Given the relatively minimal public knowledge of this service, I think this is acceptable as a first-pass but a future solution involving HAProxy or another TCP load balancer to handle the SSH traffic might be appropriate. Similarly, automated database failover is not planned at this time due to the extra application-side complexity however the process will be well documented and able to be executed by all tier one on-call operations staff if the Postgres master goes offline for some reason.

This will only partially address the current reliability issues as many of the current problems are linked to Apache or mod_fcgid needing to be restarted. In that light I would like to see PyPI and the catalog-sig group investigate moving the codebase to work against mod_wsgi or gunicorn (no real preference between the two) to create a more reliable runtime environment.

# private mirrors 

Having a private mirror makes a lot of sense, when companies need to make sure their build systems are not relying on external services like PyPI or a mirror. It\'s also a good way to dramatically reduce the load for the community servers.

The idea is that a Jenkins server that builds hundreds of Python apps every hour should not hammer PyPI.

We have everything needed these days to set up this kind of system, with zc.buildout or pip good practices.

What we need is a good tutorial or a guide \[\*\]

# private projects 

The part that we do not address in the community is private projects: since we don\'t have any permissions/group/roles system in PyPI, everything is public.

One way to solve this is to have a local repository for private packages, that is looked by tools like pip or easy_install, with the \--find-links option.

What we need is a good tutorial or a guide \[\*\]

# tutorial

\[\*\] If this helps, I am willing to work on a tutorial day for Pycon US, that goes through all of this, to help people set up their dev. environment the best way possible.

The material could then be published at python.org/pypi to help out.

I know Richard has some material already, so maybe this could be a joint tutorial ?
