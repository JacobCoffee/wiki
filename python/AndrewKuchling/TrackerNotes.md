# AndrewKuchling/TrackerNotes

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

I\'m using this page to record notes and reminders while assessing trackers. Please do not edit these notes. (Feel free to add a comment at the bottom of a section if there\'s something you want to respond to; just don\'t edit my text.)

# 09/16 weekend tasks 

Get more information on the Launchpad e-mail interface problems, and try to give Henstridge et.al. some debugging info.

Start thinking about ranking the trackers. Draw up a list of criteria and assign scores?

# Trac 

\'View Active Tickets\' query only returns a single spam query, but the bugs \*\*are\*\* in the tracker. Not sure why \'View Active\' isn\'t working like I expect.

Provides a wiki. This could be either a positive (easy to write little documents) or a negative (yet another spam target). The wiki doesn\'t seem to be very featureful compared to [MoinMoin](MoinMoin).

Couldn\'t figure out how to log in.

You can assign bugs to anonymous \-- probably a bug from our perspective.

Saving queries is non-trivial; you need to write a wiki invocation, but can\'t save them directly.

Couldn\'t attach an image, but only because the file limit was too low; attaching files is straightforward. (It even displays patches specially!)

Grouping by priority produces multiple groups for the same priority \-- not sure how the result list is being sorted.

Speed is reasonably quick, even for large lists of results.

Notifications are clear. There\'s an e-mail interface for adding comments, but it\'s completely undocumented. I guess it uses the subject line for the bug #, and the contents are then added as a comment.

Tripped a Python traceback (query: all new/assigned/reopened, component is Documentation; group by Owner):

    Traceback (most recent call last):
      File "/usr/lib/python2.4/site-packages/trac/web/main.py", line 335, in dispatch_request
        dispatcher.dispatch(req)
      File "/usr/lib/python2.4/site-packages/trac/web/main.py", line 220, in dispatch
        resp = chosen_handler.process_request(req)
      File "/usr/lib/python2.4/site-packages/trac/ticket/query.py", line 443, in process_request
        self.display_html(req, query)
      File "/usr/lib/python2.4/site-packages/trac/ticket/query.py", line 608, in display_html
        req.hdf['query.num_matches_group'] = num_matches_group
      File "/usr/lib/python2.4/site-packages/trac/web/clearsilver.py", line 195, in __setitem__
        self.set_value(name, value, True)
      File "/usr/lib/python2.4/site-packages/trac/web/clearsilver.py", line 243, in set_value
        add_value(name, value)
      File "/usr/lib/python2.4/site-packages/trac/web/clearsilver.py", line 235, in add_value
        add_value('%s.%s' % (prefix, k), value[k])
      File "/usr/lib/python2.4/site-packages/trac/web/clearsilver.py", line 242, in add_value
        set_str(prefix, value)
      File "/usr/lib/python2.4/site-packages/trac/web/clearsilver.py", line 213, in set_str
        self.hdf.setValue(prefix.encode('utf-8'), str(value))
    Error: Traceback (innermost last):
      File "neo_hdf.c", line 805, in hdf_set_value()
      File "neo_hdf.c", line 795, in _set_value()
    AssertError: Unable to set Empty component query.num_matches_group.Fred L. Drake, Jr.

# Roundup 

Slightly unclear how to sort to see most recent bugs (sort by descending activity, it turns out).

Interface feels pretty zippy. Also pleasantly simple compared to Jira.

Can\'t search based on attachments.

Can\'t sort users by ID, AFAICT.

Not receiving e-mails about my changes \-- maybe I\'ll only receive messages when other people edit my issues.

Didn\'t try e-mail interface yet.

# Jira 

No anonymous bug submissions, at least as currently configured.

Interface is very dense \-- many links, graphs \-- though not as bad as Bugzilla. Might be off-putting to random users.

On the other hand, that summary information is useful: who has the most assigned bugs, which subsystems have the most bugs, etc.

Interface feels kind of slow \-- it\'s not clear if this is because the server is slow, the database is so large, or because the HTML takes a while to render in my browser.

The home page is customizable, so you can remove displays you don\'t care about and add query displays for custom things. It lets you shrink the page a bit.

Version list in search seems to be unsorted.

Fancy filtering interface.

Has RSS feeds, which is kind of neat.

I didn\'t receive any e-mails; not sure if they\'re disabled in this installation, or if I need to do something to enable mail. There doesn\'t seem to be any way to add comments or close bugs via e-mail.

# Launchpad 

Filing a bug seems straightforward. All the other use cases are feasible.

Has extraneous features \-- translations, bzr branches, specifications \-- that might confuse bug reporters. Perhaps we\'d use them, or perhaps we\'d need to disable them.

Minor oddity: searching for bugs with patches lists a bug with three patches three times.

The ability to give a nickname for a bug is a neat idea.

Clicking on \'Python (upstream)\' to change the status is not immediately obvious.

I couldn\'t decrypt the OpenPGP message Launchpad sent me (complains of a CRC error), so I couldn\'t confirm my key and try the e-mail interface.

The ability to cross-link Python bugs with bugs filed on other projects might be a really useful tool for getting more bug reports, and for introducing more people to Python maintenance.

# Notes / Comments 

- On Roundup ([DavidLinke](DavidLinke)):

  - Your speculation was correct: Roundup will not send an email to the message submitter. [RichardJones](RichardJones): This is configurable.

  - Search interface: More search fields can be easiliy added (also submitter, actor or user id, attachment yes/no, attachment type). It is just not active in the demo. Also you can store your personal searches under a name which gets added to the sidebar. Searches can be public or private so that some searches like \"recently submitted\" can be made available for all.

  - Attachment search: Do you even plan to search for something in the attachment? Roundup uses the powerful Xapian search engine and this would make even searching in attachments possible. Text files are already indexed in current version of roundup. I don\'t know if Xapian is installed for the roundup demo tracker.

------------------------------------------------------------------------

[CategoryTracker](CategoryTracker)
