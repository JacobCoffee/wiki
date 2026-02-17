# SSL

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

SSL stands for **Secure Sockets Layer** and is designed to create secure connection between client and server. Secure means that connection is encrypted and therefore protected from eavesdropping. It also allows to validate server identity.

### SSL support status 

- **ssl** module (internal for Python 2.6+, external for Python 2.5 - [http://pypi.python.org/pypi/ssl](http://pypi.python.org/pypi/ssl)). Unfortunately, there are no external binaries for Python 2.5 on Windows (and that makes [AppEngine](AppEngine) uploads insecure).

  - **ssl** doesn\'t validate server identity and hence vulnerable to MITM attack by default (read below).

- **pyOpenSSL**, external module for Python 2.3+, doesn\'t validate server identity, vulnerable to MITM attack by default.

There is a serious security issue with **ssl** and **pyOpenSSL** libraries that provide SSL support. They may require valid certificate from server, but do not check it actually belongs to this server. This allows successful Man-in-the-middle attack using valid certificate from other site - [http://bugs.python.org/issue1589](http://bugs.python.org/issue1589) Libraries validate that certificate is correct and correctly signed by root certificate, but it does not check that site name matches the name specified in certificate.

### Validating server identity with ssl module 

Client need to connect to server over SSL, fetch its certificate, check that the certificate is valid (signed properly) and belongs to this server (server name).

Let\'s illustrate **ssl** vulnerability in Python 2.x versions. The following snippet should fail - it replaces HOST \"www.google.com\" to connect to with its IP address. If you try to use this IP in Chrome like [https://74.125.232.50](https://74.125.232.50) - it will show an error, but **ssl** library will not.

    import socket
    import ssl

    HOST = "www.google.com"
    PORT = 443

    # replace HOST name with IP, this should fail connection attempt,
    # but it doesn't in Python 2.x
    HOST = socket.getaddrinfo(HOST, PORT)[0][4][0]
    print(HOST)

    # create socket and connect to server
    # server address is specified later in connect() method
    sock = socket.socket()
    sock.connect((HOST, PORT))

    # wrap socket to add SSL support
    sock = ssl.wrap_socket(sock,
      # flag that certificate from the other side of connection is required
      # and should be validated when wrapping 
      cert_reqs=ssl.CERT_REQUIRED,
      # file with root certificates
      ca_certs="cacerts.txt"
    )

You will need \"cacerts.txt\" file that contains root certificates placed alongside the script - feel free to use the one attached to this page or see below how to get an updated list. To check that certificate validation works - use [https://www.debian-administration.org/](https://www.debian-administration.org/) in HOST name. This site\'s certificate is not signed by any root certificates from \"cacerts.txt\", so you will get an error.

To validate that a certificate matches requested site, you need to check *commonName* field in the *subject* of the certificate. This information can be accessed with *getpeercert()* method of wrapped socket.

    import socket
    import ssl

    HOST = "www.google.com"
    PORT = 443

    # replace HOST name with IP, this should fail connection attempt
    HOST = socket.getaddrinfo(HOST, PORT)[0][4][0]
    print(HOST)

    # create socket and connect to server
    # server address is specified later in connect() method
    sock = socket.socket()
    sock.connect((HOST, PORT))

    # wrap socket to add SSL support
    sock = ssl.wrap_socket(sock,
      # flag that certificate from the other side of connection is required
      # and should be validated when wrapping 
      cert_reqs=ssl.CERT_REQUIRED,
      # file with root certificates
      ca_certs="cacerts.txt"
    )

    # security hole here - there should be an error about mismatched host name
    # manual check of hostname
    cert = sock.getpeercert()
    for field in cert['subject']:
      if field[0][0] == 'commonName':
        certhost = field[0][1]
        if certhost != HOST:
          raise ssl.SSLError("Host name '%s' doesn't match certificate host '%s'"
                             % (HOST, certhost))

That\'s it.

### Validating server certificate with pyOpenSSL module 

    import socket
    from OpenSSL import SSL

    HOST = "www.google.com"
    PORT = 443

    # replace HOST name with IP, this should fail connection attempt,
    # but it doesn't by default
    HOST = socket.getaddrinfo(HOST, PORT)[0][4][0]
    print(HOST)

    # uses HOST
    def verify_cb(conn, x509, errno, errdepth, retcode):
      """
      callback for certificate validation
      should return true if verification passes and false otherwise
      """
      if errno == 0:
        if errdepth != 0:
          # don't validate names of root certificates
          return True
        else:
          if x509.get_subject().commonName != HOST:
            return False
      else:
        return False

    context = SSL.Context(SSL.SSLv23_METHOD)
    context.set_verify(SSL.VERIFY_PEER | SSL.VERIFY_FAIL_IF_NO_PEER_CERT, verify_cb)
    context.load_verify_locations("cacerts.txt")

    # create socket and connect to server
    sock = socket.socket()
    sock = SSL.Connection(context, sock)
    sock.connect((HOST, PORT))
    sock.do_handshake()

### Validate certificate expiration 

Needs to be researched if Python SSL libraries validate certificate expiration times correctly. Entrypoint: certificate fields *notBefore* and *notAfter*.

### Get updated list of root certificates 

You will need the latest version of certificate data from [http://hg.mozilla.org/mozilla-central/file/tip/security/nss/lib/ckfw/builtins/certdata.txt](http://hg.mozilla.org/mozilla-central/file/tip/security/nss/lib/ckfw/builtins/certdata.txt) and convert it to PEM format by any of available tools.

Or just grab the latest version from [http://curl.haxx.se/ca/cacert.pem](http://curl.haxx.se/ca/cacert.pem)
