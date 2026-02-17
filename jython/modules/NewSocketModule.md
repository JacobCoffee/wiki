# NewSocketModule

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# New Socket Module 

## Introduction 

This page descibes the socket module for jython 2.5, which now has support for [asynchronous or non-blocking operations](http://en.wikipedia.org/wiki/Non-blocking_I/O). This support makes possible the use of event-based server frameworks on jython. Examples of cpython event-based frameworks are [Twisted](http://twistedmatrix.com/), [Zope](http://www.zope.org/) and [Medusa](http://www.amk.ca/python/code/medusa.html). It is considered by some that Asynchronous IO is the only way to address [The C10K problem](http://www.kegel.com/c10k.html)

The socket module is pretty much feature complete. It is written to use java.nio apis as much as possible, i.e. all reads and writes are carried out through the sockets java.nio.channel based interface. However, there are some circumstances, specifically timeout operations, where the java.net.socket interfaces must be used.

The socket module is quite stable; a [number of bugs in the functionality have been found and fixed](http://bugs.jython.org/issue?@search_text=&title=&@columns=title&id=&@columns=id&creation=&creator=&activity=&@columns=activity&@sort=activity&actor=&nosy=&type=&components=&versions=&severity=&dependencies=&assignee=amak&keywords=&priority=&@group=priority&status=&@columns=status&resolution=&@pagesize=50&@startwith=0&@action=search).

There are necessarily some differences between the behaviour of the cpython and jython socket modules, because jython is implemented on the java socket model, which is more restrictive than the C language socket interface that cpython is based on. It is the purpose of this document to describe those differences. If you find a difference in behaviour between cpython and jython that is not documented here, and where jython is behaving differently to the cpython socket documentation, then [that should be considered a bug and reported, please](http://bugs.jython.org/).

## Requirements 

Non-blocking support

- JVM version with [java.nio](http://java.sun.com/j2se/1.4.2/docs/guide/nio/) support, i.e. \>= version 1.4

- Any jython version \>= 2.5

SSL support

- JVM version: any version on which jython runs.

- Any jython version \>= 2.5

## Cpython compatibility 

The new socket module has been written to comply as closely as possible with the cpython 2.5 API for non-blocking sockets, therefore you should use the cpython socket documentation as your reference when writing code.

[http://www.python.org/doc/2.5/lib/module-socket.html](http://www.python.org/doc/2.5/lib/module-socket.html)

If the jython module exhibits behaviour that differs from that described in the cpython documentation, then that should be considered a bug and reported as such, except for certain unavoidable differences, desribed below.

## SSL Support 

The module includes an implementation of client side SSL support, which is compatible with the cpython SSL API. The client side ssl example from the cpython documentation should just work.

[http://docs.python.org/lib/socket-example.html](http://docs.python.org/lib/socket-example.html)

However, the cpython SSL API is extremely basic, and essentially only permits the formation of SSL wrapped sockets. It does NOT include support for any of the following

- Management of Certificates, i.e. loading, storing, manipulating certificates.
- Verification of Certificates, i.e. verifying the chain of trust.
- Non-blocking SSL support.
- Server side SSL support.

All of the above are possible, but since no other python version includes that support in the base distribution, I\'m not going to do it for jython either; trying to design an API would be complex enough; implementing would be a lot of work beyond that.

If you have serious SSL or crypto requirements, then I **strongly** recommend using the java crypto libraries, or one of the excellent third-party crypto libraries for java, such as that from the [Legion of the Bouncy Castle](http://www.bouncycastle.org).

### Certificate Checking 

By default, the cpython socket library does not carry out certificate checking, which means that it will accept expired certificates, etc. This is acceptable when the validity of the remote certificate is not important, such as in testing.

In Java, by default, certificate checking is **enabled**. This means that the jython ssl routines **will** verify the validity of the remote certificate, and refuse to form the connection if it is not valid. If this is a problem for you, then you can get around it as described here. I have also written a blog post about this: [Installing an all trusting security provider on java and jython](http://jython.xhaus.com/installing-an-all-trusting-security-provider-on-java-and-jython/)

There is also a pure Jython implementation of this same thing here: [Trusting All Certificates in Jython](http://tech.pedersen-live.com/2010/10/trusting-all-certificates-in-jython/)

#### By configuring your JVM 

If you are using self-generated certificates for testing, then you can import those certificates into the JVM running your jython scripts, and the certificate will then be recognised. See this article from Sun on [how to install certificates on a JVM](http://java.sun.com/j2ee/1.4/docs/tutorial/doc/Security6.html).

#### By installing your own Security Provider 

The following technique has been adapted from the ZXTM [KnowledgeHub](./KnowledgeHub.html) article [Using the Control API with Java](http://knowledgehub.zeus.com/articles/2006/01/03/using_the_control_api_with_java).

**WARNING**: Installing this all-trusting security provider means that **all** certificates will be accepted, regardless of validity! **Do not use this technique if you need to verify the trustworthiness of an SSL certificate!**

In order to accept all certificates, valid or not, you can install your own security provider. Here is a sample Security Provider, written in java, which trusts all certificates. This code should be saved in a file called **MyProvider.java**, compiled and the resulting **MyProvider.class** file placed in the class path.

    import java.security.Security;
    import java.security.KeyStore;
    import java.security.Provider;
    import java.security.cert.X509Certificate;
    import javax.net.ssl.ManagerFactoryParameters;
    import javax.net.ssl.TrustManager;
    import javax.net.ssl.TrustManagerFactorySpi;
    import javax.net.ssl.X509TrustManager;

    public class MyProvider extends Provider
    {
      public MyProvider()
      {
        super("MyProvider", 1.0, "Trust certificates");
        put("TrustManagerFactory.TrustAllCertificates", MyTrustManagerFactory.class.getName());
      }

      protected static class MyTrustManagerFactory extends TrustManagerFactorySpi
      {
        public MyTrustManagerFactory()
          {}
        protected void engineInit( KeyStore keystore )
          {}
        protected void engineInit(ManagerFactoryParameters mgrparams )
          {}
        protected TrustManager[] engineGetTrustManagers()
        {
          return new TrustManager[] {new MyX509TrustManager()};
        }
      }

      protected static class MyX509TrustManager implements X509TrustManager
      {
        public void checkClientTrusted(X509Certificate[] chain, String authType)
          {}
        public void checkServerTrusted(X509Certificate[] chain, String authType)
          {}
        public X509Certificate[] getAcceptedIssuers()
          { return null; }
      }

    }

To install this custom Security Provider from jython, execute the following code

    import java
    import MyProvider
    # Install the all-trusting trust manager
    java.security.Security.addProvider(MyProvider())
    java.security.Security.setProperty("ssl.TrustManagerFactory.algorithm", "TrustAllCertificates")

All code which creates SSL socket connections should now accept all certicates, whether they are valid or not.

## Cpython versions 

It is the intention that these modules be fully API compatible with cpython, as far as is possible or sensible. This means that any cpython socket code that is syntax compatible with your selected jython version should produce identical behaviour to the same code running on cpython.

The unit-tests provided with these modules should also run on all versions of cpython. See below under unit-tests for more details.

## Other I/O 

The design of the cpython non-blocking API is derived from the UNIX C api, which deals with FILE DESCRIPTORS. Since file descriptors can describe any type of I/O channel on unix OSes, cpython can deal with selecting and polling on multiple channel types, such non-blocking files, pipes and named-pipes, fifos, etc.

The java model for selecting on channels is much more restrictive. There is a java abstract class, java.nio.channels.[SelectableChannel](./SelectableChannel.html), which other channel classes must subclass if they are to be multiplexed. On 1.4 JVMs, only the following classes subclass [SelectableChannel](http://java.sun.com/j2se/1.4.2/docs/api/java/nio/channels/SelectableChannel.html).

- [Socket channels](http://java.sun.com/j2se/1.4.2/docs/api/java/nio/channels/SocketChannel.html)

- Pipe [source](http://java.sun.com/j2se/1.4.2/docs/api/java/nio/channels/Pipe.SourceChannel.html) and [sink](http://java.sun.com/j2se/1.4.2/docs/api/java/nio/channels/Pipe.SinkChannel.html) channels

Specifically, [FileChannel\'s](http://java.sun.com/j2se/1.4.2/docs/api/java/nio/channels/FileChannel.html) do not subclass [SelectableChannel](http://java.sun.com/j2se/1.4.2/docs/api/java/nio/channels/SelectableChannel.html), and thus it is not possible to include files in non-blocking multiplex operations on Java platforms.

Of the two channel types listed above, these modules only support socket channels. This is because it was necessary to rewrite all of the socket creation calls to return [SelectableChannels](./SelectableChannels.html). To do so for Pipes, which are used for communication with sub-processes, it would be necessary to rewrite the jython sub-process creation modules, i.e. popen, etc, to create [SelectableChannels](./SelectableChannels.html). Although it should be reasonably straightforward to implement this, I have no plans to do this work.

## Socket options 

The following socket options are supported on jython

For TCP client sockets

- SO_ERROR
- SO_KEEPALIVE
- SO_LINGER
- SO_OOBINLINE
- SO_RCVBUF
- SO_REUSEADDR
- SO_SNDBUF
- SO_TIMEOUT
- SO_TYPE
- TCP_NODELAY

For TCP server sockets

- SO_ACCEPTCONN
- SO_ERROR
- SO_RCVBUF
- SO_REUSEADDR
- SO_TIMEOUT
- SO_TYPE

The following TCP client socket options can be set on TCP Server sockets, but will have no effect on them. Instead, they will be propagated to **accept**ed client sockets. For more details, read [#1309 - Server sockets do not support client options and propagate them to \'accept\'ed client sockets](http://bugs.jython.org/issue1309)

- SO_KEEPALIVE
- SO_LINGER
- SO_OOBINLINE
- SO_SNDBUF
- TCP_NODELAY

For UDP sockets

- SO_BROADCAST
- SO_ERROR
- SO_RCVBUF
- SO_REUSEADDR
- SO_SNDBUF
- SO_TIMEOUT
- SO_TYPE

If an option is not explicitly listed above, it is explicitly not supported, i.e. jython cannot because java does not support the option.

Note that the **level** at which all but one of the options above are get and set is **socket.SOL_SOCKET**. The exception is **TCP_NODELAY**, which is at level **socket.IPPROTO_TCP**.

All but one of the above take either a single boolean/integer or a single integer as a parameter, so they might be called like so

    mysock.setsockopt(socket.SOL_SOCKET, socket.SO_OOBINLINE, 1)
    mysock.setsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF, 32768)
    mysock.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)

The exception is SO_LINGER, which (thanks to cpython\'s C heritage) takes a packed struct containing two values, the first is the flag to enable or disable SO_LINGER, the second specifies the linger time. The return value from getting the option is similarly packed. Here is a code snippet

    import struct
    linger_enabled = 1
    linger_time = 10
    linger_struct = struct.pack('ii', linger_enabled, linger_time)
    mysock.setsockopt(socket.SOL_SOCKET, socket.SO_LINGER, linger_struct)
    linger_status = mysock.getsockopt(socket.SOL_SOCKET, socket.SO_LINGER)
    linger_enabled, linger_time = struct.unpack('ii', linger_status)

## Differences between cpython and jython 

### socket.fileno() does not return an integer 

Cpython, as is appropriate for its C language heritage, returns an integer from the **socket.fileno()** method. However, the concept of having an integer handle on I/O channels is a C language specific idiom: C maintains an internal of array of FILE\* structures, and the integer \"file descriptor\" is an index into that array.

In java, there is no concept of a file descriptor table. Instead, java deals with objects, java.nio.channel objects in the case of sockets.

Also, the only reason why one might need the return value from the **socket.fileno()** method is to pass it to one of the functions in the [select module](SelectModule). However, the portable way to do this, i.e. the way to write code that works portably across cpython and jython (and other pythons such as ironpython, pypy, etc) is to **pass the socket object directly to the select call**. This is approved by Guido, the python BDFL, as you can see from this email discussion on python-dev: [python-dev: return value of socket.fileno()](http://mail.python.org/pipermail/python-dev/2007-May/073409.html).

The **socket.fileno()** method has been added to jython purely for code compatibility, i.e. to prevent exceptions from code that was not written to be portable (we try hard to be good citizens in jython-land {{/wiki/modernized/img/smile4.png\|;-) )

For a much more detailed discussion of this subject, see this email discussion: [fileno support is not in jython. Reason?](http://comments.gmane.org/gmane.comp.lang.jython.devel/3994)

### Socket shutdown 

On sockets, the **shutdown** method is closely related to the **close** method, in that it terminates network communication on the socket. However, there are differences, because **close** relates to the file descriptor connected to the socket, whereas the **shutdown** method relates to the socket itself. But java doesn\'t have file descriptors, and doesn\'t have the shutdown method for sockets in general; only TCP client sockets have shutdown methods; for TCP server sockets and UDP sockets, the method to shutdown a socket is the **close** method. For a detailed discussion of these issues, see this blog post: [Socket shutdown versus socket close on cpython, jython and java](http://jython.xhaus.com/socket-shutdown-versus-socket-close-on-cpython-jython-and-java/). On jython, the socket method is implemented as follows, for each type of socket

1.  **TCP Client sockets**. When **shutdown** is called on TCP client sockets, the **how** parameter determines how the read and write streams of the socket are treated. This is standard cpython behaviour, and follows the cpython documentation.

2.  **TCP Server sockets**. When **shutdown** is called on TCP server sockets, the effect should be to close the listening socket, and discard all incoming connections in the listen queue. However, in java there is no **shutdown** method for server sockets (see [ServerSocket](http://java.sun.com/j2se/1.5/docs/api/java/net/ServerSocket.html) and [ServerSocketChannel](http://java.sun.com/j2se/1.5/docs/api/java/nio/channels/ServerSocketChannel.html)), there is only a **close** method. So in jython, the **shutdown** method on TCP server sockets is a no-op, i.e. it **does nothing**. If you want to stop accepting incoming requests, then you should call the **close()** method on the socket.

3.  **UDP sockets**. When **shutdown** is called on an UDP socket, as with TCP server sockets, the effect should be to stop accepting incoming packets. However, in java there is no **shutdown** method on udp sockets (see [DatagramSocket](http://java.sun.com/j2se/1.5/docs/api/java/net/DatagramSocket.html) and [DatagramChannel](http://java.sun.com/j2se/1.5/docs/api/java/nio/channels/DatagramChannel.html)), there is only a **close** method. So in jython, the **shutdown** method on UDP sockets is a no-op, i.e. it **does nothing**. If you want to stop accepting incoming packets, then you should call the **close()** method on the socket.

### Error handling 

These modules have been coded so that the error handling is as close to the error handling of cpython as possible. So, ideally, cpython socket and select code run on jython should exhibit identical behaviour to cpython, in terms of exception types raised, error numbers returned, etc.

However, due to the different semantics of java and C, there will be differences in the error handling, which will be documented here as they are discovered.

### Differences in the treatment of zero timeout values 

On cpython, when you specify a zero (i.e. 0 or 0.0) timeout value, the socket should behave the same as if the socket had been placed in non-blocking mode. See the [cpython socket object documentation](http://www.python.org/doc/lib/socket-objects.html) for details.

However, [Java interprets a zero timeout value as an infinite timeout](http://java.sun.com/j2se/1.4.2/docs/api/java/net/Socket.html#setSoTimeout(int)), i.e. the socket is placed in blocking mode.

To solve this conflict, I decided that the best thing to do with zero timeouts is to adjust them to the smallest possible timeout in java, which is 1 millisecond. So if you do socket.settimeout(0) with the new jython socket module, what you will really get is equivalent to the cpython call socket.settimeout(0.001).

This means that you may get differing exception signatures when using zero timeouts under cpython and jython.

1.  Cpython: socket operations with zero timeouts that fail will raise socket.error exceptions. This is equivalent to a -1 return from the C socket.recv call, with errno set to EAGAIN, meaning \"The socket is marked non-blocking and the receive operation would block, or a receive timeout had been set and the timeout expired before data was received.\"
2.  Jython: socket operations with zero timeouts that fail will generate socket.timeout exceptions.

### Deferred socket creation on jython 

Java has different objects for Client (java.net.Socket+java.nio.channels.[SocketChannel](./SocketChannel.html)) and Server (java.net.[ServerSocket](./ServerSocket.html)+java.nio.channels.[ServerSocketChannel](./ServerSocketChannel.html)) sockets. Jython cannot know whether to create a client or server socket until some client or server specific behaviour is observed. For clients, this is a **connect()** call, and for servers, this is a **listen()** call.

When a **connect()** call is made, jython then knows that this is a client socket, and to create a java.net.Socket+java.nio.channels.[SocketChannel](./SocketChannel.html) to implement the socket.

Similarly, when a **listen()** call is made, jython then knows that this is a server socket, and to create a java.net.[ServerSocket](./ServerSocket.html)+java.nio.channels.[ServerSocketChannel](./ServerSocketChannel.html) to implement the socket.

Any attempt to get information about a socket before either a connect() or listen() call is made, i.e. before the implementation socket is created, may fail, although attempts are made to return already set configuration values, if possible.

For example, consider the following code

    >>> import socket
    >>> s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    >>> s.bind( ("localhost", 8888) )
    >>> print s.getsockname()
    (u'127.0.0.1', 8888)
    >>> s.listen(5)
    >>> print s.getsockname()
    (u'127.0.0.1', 8888)

The value for port number, 8888, that is returned after the bind() call, is **not** the port number retrieved from the underlying socket itself, because the socket does not yet exist. Instead, you are being returned the requested configuration value, the value you passed in. Only after the listen() call does the socket exist, so only then is the port number retrieved from the actual underlying socket.

This may seem a trivial concern, since the correct port is always returned. But there is one situation where it does make a difference. If you request a port number of **0**, then that is a request to the operating system to pick an **ephemeral** port number for you, one that is guaranteed to be free. Consider this code

    >>> import socket
    >>> s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    >>> s.bind( ("localhost", 0) )
    >>> print s.getsockname()
    (u'127.0.0.1', 0)
    >>> s.listen(5)
    >>> print s.getsockname()
    (u'127.0.0.1', 3357)

In this scenario, if you relied on the port number returned after the bind call but before the listen call, e.g. handing it to clients, then your clients would fail, because 0 is an invalid port number.

Similarly, the actual underlying implementation socket for client sockets does not exist until you have called one of the **connect()** methods.

## Known issues and workarounds 

### Null address returned from UDP socket.recvfrom() in timeout mode 

This bug is reported on the jython bug tracker: [UDP recvfrom fails to get the remote address](http://bugs.jython.org/issue1018).

#### Description 

When an UDP socket is in timeout mode, the address returned from socket.recvfrom() is always (None, -1).

This only happens in timeout mode, because that code path uses java.net.[DatagramSocket](./DatagramSocket.html).receive() to receive packets. For some reason, [DatagramPackets](./DatagramPackets.html) receive()d in this way either

- Return null from the [DatagramPacket](./DatagramPacket.html).getAddress() method, thus preventing us from obtaining the source address

- Cause an exception when [DatagramPacket](./DatagramPacket.html).getSocketAddress() is called.

This bug has been reported to Sun, but is not yet public on the Java bug database.

#### Workaround 

1.  Until the java bug is fixed, only use sockets in either blocking or non-blocking mode; the problem will not occur in this case.

2.  If you need timeouts, then until the java bug is fixed, you should probably create your own [DatagramSockets](./DatagramSockets.html), directly through the java.net APIs.

### IPV6 address support 

#### Description 

On some versions of the JVM, there are problems with bind\'ing and connect\'ing sockets using IPV6 addresses, even though the OS platform ostensibly supports IPV6. See this bug on the Java bug database: [NIO channels with IPv6 on Windows](http://bugs.sun.com/view_bug.do?bug_id=6230761)

There have also been reports of [IPV6 problems with java.nio on Windows 7 64 bit](http://bugs.jython.org/issue1711), so these instructions also apply to that platform, since the jython socket module uses java.nio extensively. Further information: the reporter of that bug has found that the problem appears on JDK 1.6, and **goes away when he uses a release of JDK 1.7**, which is still in pre-release.

The most appropriate mechanism for retrieving IP addresses is the **getaddrinfo()** function, to which you pass parameters to specify the kind of addresses you\'re interested in. The function returns a 5-tuple, the last element of which is a tuple of (ip-address, port), which you then use to bind or connect your socket. For example

    >>> import socket
    >>> socket.getaddrinfo("localhost", 80, socket.AF_INET, socket.SOCK_STREAM)[0][4]
    ('127.0.0.1', 80)

If you want to retrieve IPV4 addresses only, you pass the **family** parameter **AF_INET**, as in the example above.

If you want to retrieve IPV6 addresses only, you pass the **family** parameter **AF_INET6**, like this.

    >>> import socket
    >>> socket.getaddrinfo("localhost", 80, socket.AF_INET6, socket.SOCK_STREAM)[0][4]
    ('0:0:0:0:0:0:0:1', 80)

If you don\'t care whether you receive IPV4 or IPV6 addresses, specify the **family** parameter as **AF_UNSPEC**, and you will be returned a mix of addresses, if your system supports IPV6, like this

    >>> import socket
    >>> for a in socket.getaddrinfo("localhost", 80, socket.AF_UNSPEC, socket.SOCK_STREAM)
    ...     print a[4]
    ...
    ('127.0.0.1', 80)
    ('0:0:0:0:0:0:0:1', 80)

A problem arises because of incomplete IPV6 support in the JVM, particularly on older JVMs, such as the bugs mentioned above. So, on some systems, if you try to use IPV6 addresses, you will get a **java.net.[SocketException](./SocketException.html)**.

This is problematic in jython, because there are multiple modules, such as telnetlib, httplib, smtplib, etc, that use the socket library to retrieve addresses, **but which use the AF_UNSPEC parameter to getaddrinfo()**. This means that those modules may be returned IPV6 addresses, which they will try to **bind** or **connect**, and possibly fail, for the reasons discussed above. Which would mean you get failures from those modules.

So to prevent those failures, we\'ve put a workaround in place.

#### Workaround 

The workaround is a jython-specific function which instructs the **getaddrinfo()** function to **only** return IPV4 addresses. Although this function is in the socket module, it affects all modules that use the **getaddrinfo()** function.

It is used like this

    >>> import socket
    >>> socket._use_ipv4_addresses_only(True)
    >>> for a in socket.getaddrinfo("localhost", 80, socket.AF_UNSPEC, socket.SOCK_STREAM)
    ...     print a[4]
    ...
    ('127.0.0.1', 80)

Note that this function should be called before any other modules attempt to use the socket module, like so

    import httplib
    import socket
    socket._use_ipv4_addresses_only(True)
    py_dot_org = httplib.HTTPConnection('www.python.org')

To restore normal behaviour of the **AF_UNSPEC** family, pass a **False** value to **socket.\_use_ipv4_addresses_only()**

**NB**: This workaround **only** affects the **getaddrinfo()** function. If you pass traditional (hostname, port) tuples containing IPV6 addresses to socket functions, e.g. (\"::1\", 80), you will **not** be able to avail of this workaround.

### Internationalized Domain Name support 

[Internationalized Domain Names for Applications](http://en.wikipedia.org/wiki/Internationalized_domain_name) (IDNA) is a mechanism whereby characters from outside the [US-ASCII character set](http://en.wikipedia.org/wiki/ASCII) may be used in domain names. IDNA is specified in [RFC 3490](http://tools.ietf.org/html/rfc3490).

Before IDNA, it was not possible to include non-ASCII characters in domain names, e.g. accented characters such as á, é, í, ó, ú, etc, or characters from non-Roman alphabets, such Japanese, Chinese, Korean, Hebrew, Arabic, etc. In May 2010, based on widespread support for IDNA, ICANN permitted the [first non-ASCII TLDs to be made available](http://blog.icann.org/2010/05/idn-cctlds/).

Therefore, in order to access the entire internet, including non-ASCII domain names, IDNA support is required.

#### Description 

When you pass a non-ASCII hostname to the cpython or jython socket module, it attempts to automatically map that name to its IDNA equivalent. This applies to all functions that take hostnames, e.g. getaddrinfo(), bind(), connect(), etc, as in these examples from cpython

    Python 2.5.4 (r254:67916, Dec 23 2008, 15:10:54) [MSC v.1310 32 bit (Intel)] on win32
    Type "help", "copyright", "credits" or "license" for more information.
    >>> import socket
    >>> socket.getaddrinfo(u"alán.com", 80)
    [(2, 0, 0, '', ('207.234.185.84', 80))]
    >>>

The problem is that [jython\'s IDNA support is currently broken](http://bugs.jython.org/issue1153). This means that any attempt to use socket module functions to access domain names that contain non-ASCII characters will break.

    Jython 2.5.0 (Release_2_5_0:6476, Jun 16 2009, 13:33:26)
    [Java HotSpot(TM) Client VM (Sun Microsystems Inc.)] on java1.5.0_18
    Type "help", "copyright", "credits" or "license" for more information.
    >>> import socket
    >>> socket.getaddrinfo(u"alán.com", 80)
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
      File "C:\jython250\Lib\socket.py", line 593, in getaddrinfo
        raise _map_exception(jlx)
    socket.gaierror: (20001, 'getaddrinfo failed')
    >>>

#### Workaround 1 for Java 6 JVMs 

There is builtin [IDNA support in Java 6](http://java.sun.com/developer/technicalArticles/javase/i18n_enhance/#idn). This support has been used in the jython socket module, but **only when jython is run on a Java 6 JVM**. This support was first made available in jython 2.5.2rc4. See this example from the latest jython

    Jython 2.5.2rc3 (trunk, Feb 1 2011, 21:42:10)
    [Java HotSpot(TM) Client VM (Sun Microsystems Inc.)] on java1.6.0_13
    Type "help", "copyright", "credits" or "license" for more information.
    >>> import socket
    >>> socket.getaddrinfo(u"alán.com", 80)
    [(2, None, 0, 'xhaus.com', ('207.234.185.84', 80))]
    >>>

This IDNA support **will not work on Java 5 JVMs**: You must use a Java 6 JVM for it to work.

#### Workaround 1 for Java 5 JVMs 

If you are unable to upgrade the JVM on which you run jython to Java 6, then there is another potential workaround.

There is a [GNU library for IDNA support](http://www.gnu.org/software/libidn/), which includes [Java support for IDNA](http://www.gnu.org/software/libidn/javadoc/).

If you want to have IDNA support in jython on Java 5, then you download the GNU library, put libidn.jar on your classpath, and use it as follows

    >>> import gnu.inet.encoding.IDNA
    >>> domain = u"alán.com"
    >>> idna_domain = gnu.inet.encoding.IDNA.toASCII(domain)
    >>> idna_domain
    u'xn--aln-fla.com'
    >>> import socket
    >>> socket.getaddrinfo(idna_domain, 80)
    [(2, None, 0, 'xhaus.com', ('207.234.185.84', 80))]

This same technique will also work on socket-dependent modules, such as httplib, urllib/2, ftplib, telnetlib, [SocketServer](./SocketServer.html), etc.
