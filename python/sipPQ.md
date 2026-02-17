# sipPQ

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# sipPQ 

sipPQ is an interface to PostgreSQL\'s libpq. It is written using [SIP](SIP), and is being used in a production environment. The original author is Jonathan Gardner.

sipPQ only tries to interface directly with libpq. A more useable interface can be written in python that runs on top of it.

sipPQ demonstrates that [SIP](SIP) can also handle C libraries, and quite well at that. Beyond learning how to write a sip script, not much effort was required to create a finished product.
