# JiraTracker

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

Some experiences with Jira:

- SF conversions seems to work fine.
- needs login for every user, even for read.
  - This is just a configuration issue. [The Apache JIRA](http://issues.apache.org/jira/) has public read enabled.
- can do convenient mass edits, for example, I could assign all issues currently assigned to \"loewis\" to \"mloewis\".

## Questions 

Bignose:

- According to the [licensing and pricing](http://www.atlassian.com/software/jira/pricing.jsp) page for Jira, it is non-free software. We can\'t examine, improve, or commission others to do these things to it. Why are we considering a non-free tracker for Python?

  The [word on the street](http://sayspy.blogspot.com/2006/06/request-for-test-trackers-to-get.html): \"We want the best solution possible without being political.\" Sounds like a minor [BitKeeper](./BitKeeper.html) incident in the making, but then [SourceForge](SourceForge) isn\'t entirely run on open source software, either. \-- [PaulBoddie](PaulBoddie)
