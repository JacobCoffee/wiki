# CloudPyPI/Proposal

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# Cloud PyPI Proposal 

This is the third revision of the proposal text which was accepted by the PSF board in their December 2010 meeting.

    PSF-Proposal: 100
    Title: Move PyPI static data to the cloud for better availability
    Version: 3
    Last-Modified: 2010-08-16
    Author: mal@lemburg.com (Marc-AndrÃ© Lemburg)
    Discussions-To: catalog-sig@python.org
    Status: Draft
    Type: Informational
    Created: 2010-06-14
    Post-History:


    Proposal: Move PyPI static data to the cloud for better availability
    ========================================================================

    Motivation
    ----------

    PyPI has in recent months seen several outages with the index being
    unavailable to both users using the web GUI interface as well as
    package administration tools such as easy_install from setuptools.

    As more and more Python applications rely on tools such as
    easy_install for direct installation, or zc.buildout to manage the
    complete software configuration cycle, the PyPI infrastructure
    receives more and more attention from the Python community.

    While we just started to have monitoring for PyPI installed and
    the first reports of outtages are now being sent to the catalog-sig 
    mailing list, we don't have reliable numbers available yet. However,
    the number of discussions about PyPI outtages in the mailing lists
    has increased to a point where we cannot simply ignore those 
    complaints anymore.

    In order to maintain its credibility as software repository, to
    support the many different projects relying on the PyPI infrastructure
    and the many users who rely on the simplified installation process
    enabled by PyPI, the PSF needs to take action and move the essential
    parts of PyPI to a more robust infrastructure that provides:

     * scalability
     * 24/7 outsourced system administration management
     * redundant storage
     * geo-localized fast and reliable access


    Current Situation
    -----------------

    PyPI is currently run from a single server hosted in The Netherlands
    (ximinez.python.org).  This server is run by a very small team of sys
    admin.

    PyPI itself has in recent months been mostly maintained by one
    developer: Martin von LÃ¶wis. 

    Projects are underway to enhance PyPI in various ways, including a
    proposal to add external mirroring (PEP 381), but these are still not
    fully finalized and require implementation changes/new features in 
    the existing client tools.

    According to Martin, the server side features of PEP 381, including
    a few undocumented extensions to provide package signatures, are already
    implemented. 

    However, without client tools to make use of them, this is not going
    to change the current situation for existing PyPI users. 

    Furthermore those client tools enhancements would first have to get
    adopted by PyPI users by either replacing their client tools with
    updated versions or switching to new client tools, which is likely
    going to take months to years. Existing client tool users won't 
    see an immediate improvement.


    Usage
    -----

    PyPI provides four different mechanisms for accessing the stored
    information:

     * a web GUI that is meant for use by humans
     * an RPC interface which is mostly used for uploading new
       content
     * a semi-static /simple package listing, used by setuptools
     * a static area /packages for package download files and 
       documentation, used by both the web GUI and setuptools

    The /simple package listing is dump of all packages in PyPI using a
    simple HTML page with links to sub-pages for each package. These
    sub-pages provide links to download files and external references.

    External tools like easy_install only use the /simple package
    listing together with the hosted package download files.

    While the /simple package listing is currently dynamically created
    from the database in real-time, this is not really needed for normal
    operation. A static copy created every 10-20 minutes would provide the
    same level of service in much the same way.


    Moving static data to a CDN
    ---------------------------

    Under the proposal the static information stored in PyPI
    (meta-information as well as package download files and documentation)
    is moved to a content delivery network (CDN).

    For this purpose, the /simple package listing is replaced with a
    static copy that is recreated every 10-20 minutes using a cronjob on
    the PyPI server.

    At the same intervals, another script will scan the package and
    documentation files under /packages for updates and upload any changes
    to the CDN for neartime availability.

    By using a CDN the PSF will enable and provide:

     * high availability of the static PyPI content
     * offload management to the CDN
     * enable geo-localized downloads, i.e. the files are hosted
       on a nearby server
     * faster downloads
     * more reliability and scalability
     * move away from a single point of failure setup

    Note that the proposal does not cover distribution of the dynamic
    parts of PyPI. As a result uploads to PyPI may still fail if the PyPI
    server goes down. However, these dynamic parts are currently not being
    used by the existing package installation tools.


    Choice of CDN: Amazon Cloudfront
    --------------------------------

    To keep the costs low for the PSF, Amazon Cloudfront appears to be
    the bext choice for CDN.

    Cloudfront is supported by a set of Python libraries (e.g. Amazon S3
    lib and boto), upload scripts are readily available and can easily be
    customized.

     http://www.saltycrane.com/blog/2008/12/card-store-project-4-notes-using-amazons-cloudfront/

    Other CDNs, such as Akamai, are either more expensive or require
    custom integration.  Availability of Python-based tools is not always
    given, in fact, accessing such information is difficult for most of
    the proprietary CDNs.


    Cloudfront: quality of service
    ------------------------------

    Amazon Cloudfront uses S3 as basis for the service, S3 has been around
    for years and has a very stable uptime:

     http://www.readwriteweb.com/archives/amazon_s3_exceeds_9999_percent_uptime.php

    Cloudfront itself has been around since Nov 2008. Amazon still uses
    the web 2.0 "beta" marketing term on it.

    You can check their current online status using this panel:

     http://status.aws.amazon.com/

    Apart from the gained availability and outsourced management, we'd
    also get faster downloads in most parts of the world, due to the local
    caching Cloudfront is applying. This caching can be used to further
    increase the availability, since we can control the expiry time of
    those local copies.

    So in summary, we are replacing a single point of failure with an N
    server fail-over system (with N being the number of edge caching
    servers they use).


    How Cloudfront works
    --------------------

    Cloudfront uses Amazon's S3 storage system which is based on
    "buckets".  These can store any number of files in a directory-like
    structure. The only limit is a 5GB per file limit - more than enough
    for any PyPI package file.

    Cloudfront provides a domain for each registered S3 bucket via a
    "distribution" which is then made available through local cache
    servers in various locations around the world. The management of which
    server to use for an incoming request is transparently handled by
    Amazon. Once uploaded to the S3 bucket, the files will be distributed
    to the cache servers on demand and as necessary.

    Each edge server server maintains a cache of requested files and
    refetches the files after an expiry time which can be defined when
    uploading the file to the bucket.

    To simplify things on our side, we'll setup a CNAME DNS alias
    for the Cloudfront domain issued by Amazon to our bucket:

     pypi-static.python.org. IN CNAME d32z1yuk7jeryy.cloudfront.net.

    In the unlikely event of a longer downtime of the whole Amazon
    Cloudfront system, our system administrators could then easily change
    the DNS alias pypi-static.python.org to point back to the PyPI server
    until the Cloudfront problem is rectified.

    For more details, please see the Cloudfront documentation and FAQ:

     http://aws.amazon.com/documentation/cloudfront/
     http://aws.amazon.com/cloudfront/faqs/


    Integration
    -----------

    In order to keep the number of changes to existing client side tools
    and PyPI itself to a minimum, the installation will try to be as
    transparent to both the server and the client side as possible.

    This requires on the server side:

     * few, if any changes to the PyPI code base
     * simple scripts, driven by cronjobs
     * a simple distributed redirection setup to avoid having 
       to change client side tools

    On the client side:

     * no need to change the existing URL http://pypi.python.org/simple
       to access PyPI
     * redirects are already supported by setuptools via urllib2

    Note that we are avoiding creating a lock-in situation by moving the
    data to a CDN, since the needed configuration changes on the server
    side can easily be rolled back to the current setup, without affecting
    the client side.


    Server side: upload cronjobs
    ----------------------------

    Since the /simple index tree is currently being created dynamically,
    we'd need to create static copies of it at regular intervals in order
    to upload the content to the S3 bucket. This can easily be done using
    tools such as wget or curl or using a custom Python script that hooks
    directly into the PyPI database (and reuses the code for generating
    the /simple tree).

    Both the static copy of the /simple tree and the static files uploaded
    to /packages then need to be uploaded or updated in the S3 bucket by a
    cronjob running every 10-20 minutes.

    In a second phase of the project, we could extend PyPI to
    automatically push updates to Cloudfront whenever a new file is
    uploaded or the package data changes.


    Server side: downloads statistics
    ---------------------------------

    The next step would then be to configure access logs:

     http://docs.amazonwebservices.com/AmazonCloudFront/latest/DeveloperGuide/index.html?AccessLogs.html

    and add a cronjob to download them to the PyPI server.

    Since the format is a bit different than the Apache log format used by
    the PyPI software, we'd have two options:

     1. convert the Cloudfront format to Apache format and simply
        append the converted logs to the local log files

     2. write a Cloudfront log file reader and add it to the
        apache_count_dist.py script that updates the download
        counts on the web GUI

    Both options require no more than a few hours to implement and test.


    Server side: redirection setup
    ------------------------------

    Since PyPI wasn't designed to be put on a CDN, it mixes static file
    URL paths with dynamic access ones, e.g.

    dynamic:

     http://pypi.python.org/pypi
     (and a few others)

    static:

     http://pypi.python.org/simple
     http://pypi.python.org/packages

    To move part of the URL path tree to a CDN, which works based on
    domains, we will need to provide a URL redirection setup that
    redirects client side tools to the new location.

    As Martin von Loewis mentioned, this will require distributing the
    redirection setup to more than just one server as well.

    Fortunately, this is not difficult to do: it requires a preconfigured
    lighttpd (*) setup running on N different servers which then all
    provide the necessary redirections (and nothing more):

    dynamic:

     http://pypi.python.org/ -> http://ximinez.python.org/pypi
     http://pypi.python.org/pypi -> http://ximinez.python.org/pypi
     (and possibly a few others)

    static:

     http://pypi.python.org/simple -> http://pypi-static.python.org/simple
     http://pypi.python.org/packages -> http://pypi-static.python.org/packages
     (note: pypi-static.python.org is a CNAME alias for the Cloudfront
      domain issued to the S3 bucket where we upload the data)

    The pypi.python.org domain would then have to be setup to map to
    multiple IP addresses via DNS round-robin, one entry for each
    redirection server, e.g.

     pypi.python.org. IN A 123.123.123.1
     pypi.python.org. IN A 123.123.123.2
     pypi.python.org. IN A 123.123.123.3
     pypi.python.org. IN A 123.123.123.4

    Redirection servers could be run on all PSF server machines, and, to
    increase availability, on PSF partner servers as well.

    It should be noted that current client side PyPI tools do not support
    automatic retry, so there still is a chance that the redirection
    server they pick on first try will fail. The user would then just have
    to retry the download to get a new server address. Automatic retry
    would, of course, create a better user experience, but this requires
    a few small changes in the existing PyPI client tools.


    (*) lighttpd is a lightwheight and fast HTTP server. It's easy to
    setup, doesn't require a lot of resources on the server machine and
    runs stable.


    Long-term changes
    -----------------

    While enabling the above redirection setup, we should also start
    working on changing PyPI and the client tools to use two new domains
    which then cleanly separate the static CDN file access from the
    dynamic PyPI server access:

     pypi.python.org
     pypi-static.python.org

    Such a transition on the client side is expected to take at least a
    few years. After that, the redirection service can be shut down or
    used to distribute and scale the dynamic PyPI service parts.


    Future improvements
    -------------------

    We could replace the cronjob system with a trigger based system
    that uploads changes as soon as the PyPI server receives them.


    Side-effects
    ------------

    Restarts of the PyPI server, network outages, or hardware failures
    would not affect the static copies of the PyPI on the CDN. setuptools,
    easy_install, pip, zc.buildout, etc. would continue to work.

    The S3 bucket would serve as additional backup for the files on PyPI.

    Later integration with Amazon EC2 (their virtual server offering)
    would easily be possible for more scalability and reduced system
    administration load.

    We don't have to worry about issues such as mirror servers having
    out-of-date data. Manipulation of packages, e.g. to introduce trojans,
    is also minimized, since the Cloudfront edge servers get their data
    straight from the S3 bucket.

    By moving from a database query driven /simple index to a static
    file system based one, we increase the responsiveness of the
    PyPI index.

    Additionally, we could easily deliver a database snapshot of the PyPI
    database as SQLite file for client side tools to use for local
    queries, further reducing the need for client-server roundtrips and
    query overhead on the server side.


    Costs
    -----

    Amazon charges for S3 and Cloudfront storage, transfer and access. The
    costs vary depending on location.

     http://aws.amazon.com/cloudfront/#pricing
     http://aws.amazon.com/s3/#pricing

    To get an idea of the costs, we'd have to take a closer look at
    the PyPI web stats:

     http://pypi.python.org/webstats/usage_201005.html

    In May 2010, PyPI transferred 819GB data and had to handle 22mio
    requests.

    Using the AWS monthly calculator this gives roughly (I used 37KB as
    average object size and 35% US, 35% EU, 10% HK, 10% JP as basis): USD
    132 per month, or about USD 1,584 per year for Cloudfront.

    For the S3 storage, the costs amount to roughly USD 30 per month, or
    USD 360 per year (100GB storage, 50GB traffic in, 100GB traffic
    out, 1000 PUT requests, 1mio GET requests).

    Total costs are an estimated USD 1944 per year.


    Refinancing the costs
    ---------------------

    Since PyPI is being used as essential resource by many important
    Python projects (Zope, Plone, Django, etc.), it's fair to ask the
    respective foundations and the general Python community for donations
    to help refinance the administration costs.

    A prominent donation button should go the PyPI page with a text
    explaining how PyPI is being hosted and why donations are necessary.

    We may also be able to directly ask for donations from the above
    foundations. Details of this are currently being evaluated by the PSF
    board (there are some issues related to our non-profit status that
    make this more complicated than it appears at first).

    Unlike other less visible PSF activities, providing and running PyPI
    is a real tangible service to the community, creating more incentive
    for Python users, including companies relying on the PyPI service, to
    donate to the PSF.

    Overall, we should be able to refinance the costs of this improved
    service level, perhaps even generate more donations than needed to
    fund other PSF activities.


    Effort
    ------

    Given that most of the tools are readily available, setting up the
    servers shouldn't take more than 2-3 developer days for developers
    who've worked with Amazon S3 and Cloudfront before, including testing.

    It is expected that we'll find volunteers to implement the necessary
    changes. If not, Marc-Andre Lemburg will start working on implementing
    the necessary changes, as time permits.


    Competing with PEP 381
    ----------------------

    A few PEP 381 developers have stated that this proposal would limit
    the interest in PEP 381 implementations and argue that the proposal
    would compete with their proposed strategy.

    Just to clarify, this proposal does not try to compete with the mirror
    proposal outlined in PEP 381. Instead it focuses on a readily
    available solution that can be implemented in a few days and only
    requires little additional system administration.

    In order to further underline this, the proposal will be presented to
    the board for approval in their August board meeting (currently
    scheduled for August 16), giving the PEP 381 developers more time to
    work and improve their PEP 381 client implementations.

    If the PEP 381 infrastructure gets rolled out, both the external
    mirrors and the cloud mirrors can work side-by-side, so there is no
    conflict.
