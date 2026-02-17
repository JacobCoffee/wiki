# OriginalCallForTrackers

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# Results 

![/!\\](/wiki/europython/img/alert.png "/!\") **The infrastructure commitee made a recommendation on Oct 3rd, 2006. See [python-dev posting](http://mail.python.org/pipermail/python-dev/2006-October/069139.html) for more (selected: Jira & Roundup).**

Four trackers were set up by the deadline of August 7 2006; see below for the list. A committee of four people is now looking at the submitted trackers, and will recommend one for use as the new Python bug tracker. The committee will make its recommendation in the fall, perhaps in October.

Once a tracker has been selected, a new installation will be set up and the [SourceForge](SourceForge) bug data will be converted once more. That conversion may be more carefully done than the conversion for the demo trackers.

# Participating Trackers 

::: {}
+--------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------+:-----------------:+:--------------------------------------------------------------------------------:+
| **Tracker wiki page**                                                          | **Test Tracker URL**                                                                                         | **Contact Person** (name & email)                                                                    |
+--------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------+-------------------+----------------------------------------------------------------------------------+
| [TracTracker](TracTracker)                                              | [http://python-trac.swapoff.org](http://python-trac.swapoff.org)                                      | Alec Thomas       | [alec@swapoff.org](mailto:alec@swapoff.org)                             |
+--------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------+-------------------+----------------------------------------------------------------------------------+
| [Roundup](http://www.mechanicalcat.net/tech/roundup/wiki/PythonTracker) | [http://efod.se/python-tracker/](http://efod.se/python-tracker/)                                      | Stefan Seefeld    | [seefeld@sympatico.ca](mailto:seefeld@sympatico.ca)                     |
+--------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------+-------------------+----------------------------------------------------------------------------------+
| [JiraTracker](JiraTracker)                                              | [http://jira.python.atlassian.com](http://jira.python.atlassian.com)                                  | Jonathan Nolen    | [jonathan@atlassian.com](mailto:jonathan@atlassian.com)                 |
+--------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------+-------------------+----------------------------------------------------------------------------------+
| [LaunchpadTracker](LaunchpadTracker)                                    | [https://demo.launchpad.net/products/python/+bugs](https://demo.launchpad.net/products/python/+bugs) | James Henstridge  | [james.henstridge@canonical.com](mailto:james.henstridge@canonical.com) |
+--------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------+-------------------+----------------------------------------------------------------------------------+
:::

![/!\\](/wiki/europython/img/alert.png "/!\") No new trackers are being accepted for consideration. ![/!\\](/wiki/europython/img/alert.png "/!\")

To learn what the committee liked about various trackers participating, see [GoodTrackerFeatures](./GoodTrackerFeatures.html) (to be edited by committee members only!).

# The Announcement 

The Python Software Foundation\'s Infrastructure committee has been charged with finding a new tracker system to be used by the Python development team as a replacement for [SourceForge](SourceForge). The development team is currently unhappy with SF for several reasons which include:

- Bad interface
  - Most obvious example is the \"Check to Upload\" button
- Lack of reliability
  - SF has been known to go down during the day unexpectedly and stay down for hours
- Lack of workflow controls
  - For instance, you cannot delete a category once created

For these reasons and others, we are requesting the Python community help us find a new tracker to use. We are asking for test trackers to be set up to allow us to test them to see which tracker we want to move the Python development team to. This is in order to allow the Infrastructure committee to evaluate the various trackers to see which one meets our tracker needs the best.

Because we are not sure exactly what are requirements for a tracker are we do not have a comprehensive requirements document. But we do have a short list of bare minimum needs:

- Can import SF data
  - [http://effbot.org/zone/sandbox-sourceforge.htm](http://effbot.org/zone/sandbox-sourceforge.htm) contains instructions on how to access the data dump and work with the support tools (graciously developed by Fredrik Lundh)
- Can export data
  - To prevent the need to develop our own tools to get our data out of the next tracker, there must be a way to get a dump of the data (formatted or raw) that includes \*all\* information
- Has an email interface
  - To facilitate participation in tracker item discussions, an email interface is required to lower the barrier to add comments, files, etc.

If there is a tracker you wish to propose for Python development team use, these are the steps you must follow:

- Install a test tracker
  - If you do not have the server resources needed, you may contact the Infrastructure committee at infrastructure at python.org, but our resources are limited by both machine and manpower, so \*please\* do what you can to use your own servers; we do not expect you to provide hosting for the final installation of the tracker for use by python-dev, though, if your tracker is chosen

- Import the SF data dump
  - [http://effbot.org/zone/sandbox-sourceforge.htm](http://effbot.org/zone/sandbox-sourceforge.htm)

- Make the Infrastructure committee members administrators of the tracker
  - A list of the committee members can be found at [http://wiki.python.org/moin/PythonSoftwareFoundationCommittees#infrastructure-committee-ic](http://wiki.python.org/moin/PythonSoftwareFoundationCommittees#infrastructure-committee-ic)

- Add your tracker to the wiki page at [http://wiki.python.org/moin/CallForTrackers](http://wiki.python.org/moin/CallForTrackers)

  - This includes specifying the contact information for a \*single\* lead person to contact for any questions about the tracker; this is to keep communication simple and prevent us from having competing installations of the same tracker software

- Email the Infrastructure committee that your test tracker is up and ready to be viewed

We will accept new trackers for up to a maximum of two months starting 2006-06-05 (and thus will end 2006-08-07). If trackers cease to be suggested, we will close acceptance one month after the last tracker proposed (this means the maximum timeframe for all of this is three months which ends 2006-09-04). This allows us to not have this process carry on for three months if there is no need for it to thanks to people getting trackers up quickly.

For those that are working to provide a test tracker, please subscribe to the various wiki pages that are maintained by the Infrastructure committee. We will use these wiki pages as the primary way to communicate with all tracker maintainers.

If you have any questions, feel free to email infrastructure at python.org .

\- Brett Cannon

- Chairman, Python Software Foundation Infrastructure committee

------------------------------------------------------------------------

[CategoryTrackerArchive](CategoryTrackerArchive)
