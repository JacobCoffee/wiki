# UbuntuInstall

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

**Building Python from source on Ubuntu**

The following packages are required install to get a complete build on Ubuntu.

- libbz2-dev
- libgdbm-dev
- liblzma-dev
- libreadline-dev
- libsqlite3-dev
- libssl-dev
- tcl-dev
- tk-dev
- dpkg-dev (this should solve the \_crypt and nis failures)

zlib1g-dev isn\'t on the list as it gets installed automatically as a dependency of libssl-dev.

------------------------------------------------------------------------

[CategoryFaq](CategoryFaq)
