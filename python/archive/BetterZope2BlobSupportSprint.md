# BetterZope2BlobSupportSprint

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

## Better Zope 2 Blob Support Sprint 

At [PyCon](PyCon) 2004, we came up with an interface that made it possible to quickly and efficiently return read-only filelike data (\"blobs\") to viewers of Zope websites. I\'d like continue this work, attempting to come up with a sane API which would allow us to persist pointers to bloblike objects into the ZODB and treat them like files for both read and write operations (particularly while maintaining transactional integrity for write operations).

\*\*NOTE\*\* This sprint is subsumed by the [ZodbSprint](ZodbSprint).
