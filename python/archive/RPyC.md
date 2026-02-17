# RPyC

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

**RPyC** (pronounced like *are-pie-see*), or **Remote Python Call**, is a transparent and symmetrical python library for remote procedure calls, clustering and distributed-computing. RPyC makes use of object-proxying, a technique that employs python\'s dynamic nature, to overcome the physical boundaries between processes and computers, so that remote objects can be manipulated as if they were local.

## Features 

- Transparent access to remote objects; program remotely as if working locally
- Symmetric protocol, where both the client and server can serve requests (which allows, for instance, to use callbacks)
- Synchronous and asynchronous invocation
- Platform-agnostic: 32/64 bit, little/big endian, Windows/Linux/Solaris/Mac... access objects across different architectures.
- Capability based security model
- Integration with TLS/SSL and inetd

## Use cases 

- Excels in testing environments
- Control multiple hardware or software platforms from a centralized point
- Access remote physical (hardware) resources transparently
- Distribute workload among multiple machines with ease
- Implement remote services (like SOAP or RMI) quickly and concisely (without the overhead and limitations of these technologies)

## Homepage 

[http://rpyc.wikidot.com](http://rpyc.wikidot.com)
