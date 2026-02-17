# BuildBot

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

This page contains general information about the Python BuildBot setup and issues.

**[Here are the current BuildBot results](http://buildbot.python.org/all/#/console/)**.

We need to add more platforms (and compilers!) to the BuildBot farm. If you have one of these machines you are willing to run BuildBot on, please contact [python-buildbots@python.org](mailto:python-buildbots@python.org):

- Windows

- AIX

- HP-UX

- FreeBSD, NetBSD, OpenBSD

- OS X

- Solaris / OpenSolaris / OpenIndiana / Illumos

It might also be beneficial to run on older versions of operating systems or others not mentioned above. Feel free to contact us if you would like to offer another type of system.

To add a new buildbot or change the configuration of your existing one, send a pull request to the build master config found at [https://github.com/python/buildmaster-config/blob/master/master/master.cfg](https://github.com/python/buildmaster-config/blob/master/master/master.cfg).

## Installing a buildbot worker 

You need to install a recent version of [Buildbot](http://buildbot.net/). If your OS has a packaging system (e.g. under Linux), it is probably available from the standard repositories. Otherwise, you\'ll have to build it from source (in which case you\'ll have to install Python and Twisted first).

A buildbot worker also needs the git client and it needs to be able to build Python and some of its extension modules. It means you should have the standard development tools installed (compiler, linker), and the development headers for a couple of third-party libraries (such as zlib and OpenSSL).

Once all this is done, create a new user \"buildbot\" if it doesn\'t exist (your package manager might have done it for you). Then:

     % su - buildbot
     % mkdir buildarea
     % buildbot-worker create-worker buildarea buildbot.python.org:9020 workername workerpasswd

You\'ll need to get someone to create the workername/workerpasswd on buildbot.python.org before doing this. Ask on [python-buildbots@python.org](mailto:python-buildbots@python.org) once you\'re ready.

Then edit buildarea/info/admin and buildarea/info/host to set them appropriately.

Use \"crontab -e\" (still under the \'buildbot\' user) to ensure that the buildbot automatically starts on reboot (we must use restart instead of start, as start will fail if the server was shutdown abruptly, leaving the twistd.pid file on disk):

     @reboot buildbot-worker restart /home/buildbot/buildarea

Finally, start buildbot (still under the \'buildbot\' user) with:

     % buildbot-worker start ~/buildarea

Once the buildbot is running, don\'t forget to monitor the [build results](http://www.python.org/dev/buildbot/) and solve any setup issues causing test failures.

## Required ports 

In order for the buildbot to operate properly, it needs access to various TCP ports on the internet. Below is a list of known ports and hosts; this list is not exhaustive and may evolve as new tests get written.

::: {}
  ---------- ------------------------------- -------------------------------------
  **Port**   **Host**                        **Description**
  20, 21     ftp.kernel.org, ftp.mirror.nl   test_urllib2net
  53         your DNS server                 test_socket (and others implicitly)
  80         python.org                      (several tests)
  119        news.gmane.org                  test_nntplib
  443        (various)                       test_ssl
  465        smtp.gmail.com                  test_smtpnet
  9020       python.org                      Buildbot connection
  ---------- ------------------------------- -------------------------------------
:::

Many tests will also create local TCP sockets and connect to them (usually through \"localhost\" or \"127.0.0.1\"), so make sure this capability hasn\'t been disabled.

## Required Resources 

Based on \[2\]\_, the recommended resource allocations for a Python buildbot are at least:

- 2 CPUs
- 512 MB RAM
- 30 GB free disk space

Note: the bigmem tests won\'t run in this configuration, since they require substantially more memory. However, these resources should be sufficient to ensure Python compiles correctly on the platform and can run the rest of test suite.

.. \[2\]: [http://mail.python.org/pipermail/python-dev/2012-March/117978.html](http://mail.python.org/pipermail/python-dev/2012-March/117978.html)

## Buildbot Workers and Security 

Here are some important points of which you should be aware when running a buildbot worker \[1\]\_:

1\. Anyone setting up a buildbot worker should take care to invoke the build

- in an environment where an out-of-control buildbot worker, potentially executing arbitrarily horrible and/or malicious code, should not damage anything. Builders should always be isolated from valuable resources, although the specific mechanism of isolation may differ. A virtual machine is a good default, but may not be sufficient; other tools for cutting of the builder from the outside world would be chroot jails, solaris zones, etc.

2\. Code runs differently as privileged vs. unprivileged users.

- Therefore builders should be set up in both configurations, running the full test suite, to ensure that all code runs as expected in both configurations. Some tests, as the start of \`this thread

  \<[http://mail.python.org/pipermail/python-dev/2011-October/113935.html\>\`\_](http://mail.python.org/pipermail/python-dev/2011-October/113935.html%3E%60_) indicates, must have some special logic to make sure they do or do not run, or run differently, in privileged vs. unprivileged configurations, but generally speaking most things should work in both places.

3\. Access to root may provide access to slightly surprising resources,

- even within a VM (such as the ability to send spoofed IP packets, change the MAC address of even virtual ethernet cards, etc), and administrators should be aware that this is the case when configuring the host environment for a run-as-root builder. You don\'t want to end up with a compromised test VM that can snoop on your network.

The information above is a summary of a discussion that happened on python-dev regarding Buildbot security. No consensus came about, but the information is still helpful as a point of reference.

.. \[1\] See the related `python-dev thread <http://mail.python.org/pipermail/python-dev/2011-October/113935.html>`{.backtick}\_.
