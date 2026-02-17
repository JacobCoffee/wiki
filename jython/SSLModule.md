# SSLModule

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

Jython 2.7 fully supports the ssl module including as of 2.7.1 beta 2, most of ssl.SSLContext. The one major exception is server sockets that support STARTTLS protocols (FTP over SSL, \...) that negotiate from plain text to SSL-secured text, due to a limitation of Netty 4.
