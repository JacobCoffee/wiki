# TrackerTransition

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# What 

To finally get us off of SF and on to Roundup!

# When 

XXX a reasonable amount of time after Python 2.5.1 is released.

# Who 

- Brett Cannon (PST)
- Erik Forsberg (CEST)

# Where 

XXX IRC or Google Talk/Jabber chat room.

# How 

1.  Put warning into current demo installation that it is not live (**done**)

2.  Set DNS for bugs.python.org to roundup tracker (**done**).

3.  Activate mail sending to python-bugs-list, and activate sending of weekly summaries. (**done**)

4.  Announce upcoming switch on python-dev (and general community through PSF blog and c.l.py.a); encourage people to comment. (**done**)

5.  Wait two weeks. (**done**)

6.  Turn off Roundup tracker and wipe it, put a 503 page online through mod_asis. (**done**)

7.  Put tracker in \"Visible to project members only\" mode; completely hiding it would break the export. Change the \"Submit new item\" and \"browse items\" texts to

    - `<b style="color:red">This tracker is CLOSED</b>. Please use the <a href="http://bugs.python.org/">new tracker</a> instead.`{.backtick}

      [Bugs](http://tinyurl.com/yw53zr) [Patches](http://tinyurl.com/ynw6uq) [Feature Requests](http://tinyurl.com/28lphd)

    (**done**).

8.  Get final data dump. (**done**).

9.  Turn off SF tracker. As this is not supported, just remove it from the project front page. (**done**) (Put tracker in invisible state)

10. Populate Roundup with data dump. (**done**)

11. Remove the warning sign. (**done**)

12. Turn on Roundup tracker.

13. Find all pages in the web that refer to \"5470\" (roughly 200 places) and replace them with the new tracker location. Likewise for the Python documentation itself. (**done**)

14. Hope we didn\'t screw up. =)

------------------------------------------------------------------------

[CategoryTrackerArchive](CategoryTrackerArchive)
