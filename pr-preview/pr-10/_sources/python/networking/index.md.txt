# Networking

A small collection of pages on network programming topics in Python. Most of Python's networking story lives elsewhere -- in the web development section, in the standard library docs, in Twisted's own documentation. What's here covers CORBA bindings, IRC resources, SSL, XML-RPC, and the "Need for Speed" sprint that focused on Python performance improvements.

## Protocols and Standards

- [CorbaPython](CorbaPython) -- CORBA IDL language mapping for Python, with links to implementations like omniORBpy and Fnorb
- [SSL](SSL) -- notes on SSL/TLS support in Python, including the `ssl` module's history and its security limitations
- [XmlRpc](XmlRpc) -- XML-RPC in Python, a lightweight protocol for remote procedure calls that transports native data structures
- [IRC](IRC) -- Python IRC channels (mostly on Freenode) and IRC-related Python libraries

## Sprints

- [NeedForSpeed subpages](NeedForSpeed/index) -- the "Need for Speed" sprint, focused on improving CPython performance (includes IRC logs)

```{toctree}
:hidden:
:maxdepth: 1

NeedForSpeed/index
CorbaPython
IRC
SSL
XmlRpc
```
