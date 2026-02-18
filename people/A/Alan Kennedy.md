# Alan Kennedy

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

Alan Kennedy is a current jython committer, and has contributed

1.  A [NewSocketModule](../modules/NewSocketModule) with support for

    - Timeout and non-blocking operations
    - UDP / Datagrams
    - Socket Options
    - Client side SSL and certificate verification
    - Internet Protocol V6 (IPV6)
    - Internationalized Domain Names for Applications (IDNA)

2.  A [SelectModule](../modules/SelectModule) with

    - Support for the select function
    - Support for poll objects
    - Dedicated functions for cpython-compatibility

3.  [modjy](http://modjy.xhaus.com), which is a bridge between [WSGI](http://www.python.org/dev/peps/pep-0333/) and java servlets, i.e. it permits any WSGI application to run inside a java servlet container such as [Tomcat](http://tomcat.apache.org).

Alan will address any jython issues relating to these modules, or modules that use them, including the following.

Please consider the cpython 2.5 documentation (linked below under the module names) for these modules to be authoritative for jython 2.5. If jython 2.5 behaviour differs from documented cpython 2.5 behaviour, or if you come across a network-related bug in any of these modules, please [File a bug on the jython tracker](http://bugs.jython.org).

- [socket](http://docs.python.org/release/2.5/lib/module-socket.html)

- [select](http://docs.python.org/release/2.5/lib/module-select.html)

- [asynchat](http://docs.python.org/release/2.5/lib/module-asynchat.html)

- [asyncore](http://docs.python.org/release/2.5/lib/module-asyncore.html)

- [BaseHTTPServer](http://docs.python.org/release/2.5/lib/module-BaseHTTPServer.html)

- [SimpleXMLRPCServer](http://docs.python.org/release/2.5/lib/module-SimpleXMLRPCServer.html)

- [SocketServer](http://docs.python.org/release/2.5/lib/module-SocketServer.html)

- [ftplib](http://docs.python.org/release/2.5/lib/module-ftplib.html)

- [gopherlib](http://docs.python.org/release/2.5/lib/module-gopherlib.html)

- [httplib](http://docs.python.org/release/2.5/lib/module-httplib.html)

- [imaplib](http://docs.python.org/release/2.5/lib/module-imaplib.html)

- [nntplib](http://docs.python.org/release/2.5/lib/module-nntplib.html)

- [poplib](http://docs.python.org/release/2.5/lib/module-poplib.html)

- [smtpd](http://docs.python.org/release/2.5/lib/module-smtpd.html)

- [smtplib](http://docs.python.org/release/2.5/lib/module-smtplib.html)

- [telnetlib](http://docs.python.org/release/2.5/lib/module-telnetlib.html)

- [urllib](http://docs.python.org/release/2.5/lib/module-urllib.html)

- [urllib2](http://docs.python.org/release/2.5/lib/module-urllib2.html)

- [xmlrpclib](http://docs.python.org/release/2.5/lib/module-xmlrpclib.html)

Alan also runs a jython-related blog: [Jython Journeys](http://jython.xhaus.com) and a [Jython Open Source Portal](http://opensource.xhaus.com), where you can find [jyson](http://jyson.xhaus.com), a fast pure-java [JSON](http://json.org) codec for jython.
