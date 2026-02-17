# Asking for Help/How can i fetch system generated value from database after inserting a row using cursor.execute() function?

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# Asking for Help: How can I fetch a system-generated value from a database after inserting a row using the cursor.execute() function? 

The API is described in [PEP 249](http://www.python.org/dev/peps/pep-249 "PEP"). Unfortunately, the return value of `cursor.execute`{.backtick} is not defined in the specification, however, but it may be the case that your database adapter may provide a meaningful return value. When issuing `insert`{.backtick} statements in SQL, sometimes the number of rows inserted may be returned (which is probably what you\'re referring to), but even in systems like PostgreSQL where this can be observed, there can be situations where a result of 0 is given instead of the actual number of inserted rows. I seem to recall that table partitions, for instance, don\'t (or didn\'t) support non-zero results from `insert`{.backtick} when statements were issued in the SQL client. \-- [PaulBoddie](PaulBoddie) 2012-05-31 12:03:22

------------------------------------------------------------------------

[CategoryAskingForHelp](CategoryAskingForHelp) [CategoryAskingForHelpAnswered](CategoryAskingForHelpAnswered)
