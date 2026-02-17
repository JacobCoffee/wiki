# PyQt/Multimedia_Resources/MPlayerWidget

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# MPlayerWidget 

MPlayerWidget is a widget wrapper around MPlayer. Unlike other solutions that use the XEmbed protocol to embed an MPlayer window in a user interface, this solution passes the X handle of an existing QLabel widget to MPlayer so that it can render its output directly onto it.

Henning Schröder posted a link to his PyQt (Qt 3) MPlayer wrapper widget in [a message](http://www.riverbankcomputing.com/pipermail/pyqt/2007-June/016277.html) to [the mailing list](./PyQt(2f)TheMailingList.html). He has kindly donated the code to the community, and it can also be obtained from this page.
