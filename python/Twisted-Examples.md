# Twisted-Examples

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# Python Twisted Examples 

*For current and complete Twisted documentation, please refer to [http://twistedmatrix.com/trac/wiki/Documentation](http://twistedmatrix.com/trac/wiki/Documentation)*

This page maintained by Jacob [Mathai](Mathai).

[http://www.jacobmathai.org](http://www.jacobmathai.org)

- [Twisted](http://twistedmatrix.com/trac/) is an open source network framework written entirely in [Python](http://www.python.org). It allows you to create a SMTP, HTTP, proxy and ssh servers (and more) in [Python](http://www.python.org) with minimal effort. Twisted is **Asynchronous** and event driven and allows applications to respond to different network connection without the use of traditional threading models.

- Be sure to download the **[Twisted 8.2](http://twistedmatrix.com/trac/Downloads)** (main Twisted package), **[PyOpenSSL](http://pyopenssl.sourceforge.net/)**, and **[PyCrypto](http://www.amk.ca/python/code/crypto.html)** (cryptographic libraries and primitives for ssh connections) before running these Python Twisted examples.

- Install the **[ZopeInterface](./ZopeInterface.html)** that is bundled with the Twisted Sumo download before installing Twisted. (cd [ZopeInterface](./ZopeInterface.html)\* && python setup.py install)

- Install **Twisted**. (python setup.py install)

- Install **PyOpenSSL**. (make sure you have base **[openssl](http://www.openssl.org)** installed on the system) If during the PyOpenSSL install, you see any errors about Kerberos header files, try this:

If your OpenSSL ore kerberos header files are not in /usr/include, you may need to supply the -I flag to let the setup script know where to look. The same goes for the libraries of course, use the -L flag. Note that build won\'t accept these flags, so you have t o run first build_ext and then build! Example:

- python setup.py build_ext -I/usr/kerberos/include (or wherever your header files are) python setup.py build python setup.py install

<!-- -->

- Install **Pycrypto**. (python setup.py install)

- Verify that all the package are installed correctly by **import**ing **pyOpenSSL-0.7, twisted, Crypto** from a python shell and we are ready to go.

## Simple HTTP Proxy Server (proxy.py) 

    from twisted.web import proxy, http
    from twisted.internet import reactor
    from twisted.python import log
    import sys
    log.startLogging(sys.stdout)
     
    class ProxyFactory(http.HTTPFactory):
        protocol = proxy.Proxy
     
    reactor.listenTCP(8080, ProxyFactory())
    reactor.run()

- Execute the above Twisted python example script (python proxy.py) You may see a Deprecation Warning that you can ignore for this example.

<!-- -->

    [jacob@tux]$ python proxy.py
    /usr/lib/python2.3/site-packages/twisted/web/proxy.py:22: DeprecationWarning: twisted.protocols.http has moved to twisted.web.http. See http://twistedmatrix.com/projects/web.
      from twisted.protocols import http
    2005/12/06 21:47 EST [-] Log opened.
    2005/12/06 21:47 EST [-] __main__.ProxyFactory starting on 8080
    2005/12/06 21:47 EST [-] Starting factory <__main__.ProxyFactory instance at 0xb73577ac>

- Connect your internet browser to the proxy server you just created **(localhost:8080)** and you have written a **simple proxy server** using Python and Twisted.
