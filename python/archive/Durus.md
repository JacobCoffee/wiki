# Durus

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

## Masthead 

URL

:   [https://pypi.python.org/pypi/libdurus/4.0.0](https://pypi.python.org/pypi/libdurus/4.0.0)

License
:   MIT

Platforms

:   Python 2.7, PyPy 5.9, Python 3.5

Version
:   4.0.0

Maintainer
:   The current libdurus port maintainer may be contacted at tkadm30\[dot\]yandex.ru

## DB API 2.0 Drivers 

Not applicable. Durus is an object database, similar in approach to ZODB.

#### Comments 

Durus is a persistent object system for applications written in the Python programming language. Durus offers an easy way to use and maintain a consistent collection of object instances used by one or more processes. Access and change of a persistent instances is managed through a cached Connection instance which includes commit() and abort() methods so that changes are transactional.

#### Programming Model 

The programming interface is nearly the same as ZODB (Durus is heavily influenced by the ZODB design). Durus aggressively caches data and does not do locking. As a result it performs very well for applications do mostly reading and only a little writing. See the [FAQ](http://www.mems-exchange.org/software/durus/doc/FAQ.html)

#### Comments 

## Supported Python applications 

- [Schevo](Schevo)

## Pros 

- Supports epoll through the python-epoll extension.

## Cons 
