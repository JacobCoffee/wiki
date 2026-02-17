# PythonBugDay

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

**(!) Next Python Bug Day: November 3rd**

Time: all Saturday

Join us for an effort at closing some Python bugs and patches. Get quick feedback on your patches and bugfixes, or learn how to submit and examine patches.

To get all set up, the [Developer\'s Guide](http://docs.python.org/devguide) contains all the information you need.

There are usually a few core developers around at any time. Here are the nicknames of developers who will be present for sure:

- merwok --- Éric Araujo --- American East Coast timezone
- 

# Participating at Your User Group 

The Montréal-Python user group will meet up in person to participate in the bug day. Some Python user groups will meet up in person during the weekend.

Is your local user group participating?

# Participating Online 

Participants will meet in the #python-dev IRC channel on irc.freenode.net. To learn more about IRC and to find links to IRC clients for various platforms, see [http://www.irchelp.org](http://www.irchelp.org/).

# Finding Bugs 

Using [the bug tracker](http://bugs.python.org/), you can perform various searches to look for candidate issues:

- [Bugs classified as \'easy\'](http://bugs.python.org/issue?@search_text=&title=&@columns=title&id=&@columns=id&creation=&creator=&activity=&@columns=activity&@sort=activity&actor=&nosy=&type=&components=&versions=&severity=&dependencies=&assignee=&keywords=6&priority=&@group=priority&status=1&@columns=status&resolution=&@pagesize=50&@startwith=0&@queryname=&@old-queryname=&@action=search)

- [Documentation bugs](http://bugs.python.org/issue?@search_text=&title=&@columns=title&id=&@columns=id&creation=&creator=&activity=&@columns=activity&@sort=activity&actor=&nosy=&type=&components=4&versions=&severity=&dependencies=&assignee=&keywords=&priority=&@group=priority&status=1&@columns=status&resolution=&@pagesize=50&@startwith=0&@queryname=&@old-queryname=&@action=search)

- [Random issue](http://bugs.python.org/issue?@action=random) (you can use the link in the left sidebar of the bug tracker to go through random issues until you find one that you like

# Procedures 

The goal of the bug day is to process bug reports in [the Python bug tracker](http://bugs.python.org/), trying to fix and close issues.

What to do:

- Grab a copy of the Python codebase from Mercurial, following instructions in the [Developer\'s Guide](http://docs.python.org/devguide), and compile it.

- If you have a problem that isn\'t in the bug tracker, announce it to the IRC channel, and if it\'s more than five minutes\' work, create a bug report for it. See the [bug reporting instructions](http://docs.python.org/dev/bugs.html) to learn how to write bug reports.

- When you choose a bug to work on, announce it to the IRC channel (e.g. \"I\'m working on #123456.\") or on the bug report itself. This avoids accidentally duplicating work.

- Consider providing a patch that fixes the problem, or at least a simple test case that demonstrates the bug. Please see the patch submission guidelines in the Developer\'s Guide before submitting a patch.

- Does the bug appear to be gone in the Python development version (the Mercurial branch \"default\", that will become 3.4), but not the 3.2, 3.3 or 2.7 maintenance branchs? Report that, too.

- If someone else has supplied a fix, see if this fix works for² you, and add your results to the bug.

- Read the text of proposed patches and assess them for correctness and code quality. This is usually the most time-consuming step in the bug fixing process, so reading patches is very useful.

- If there\'s a working fix, feel free to add a note asking for the fix to get committed. The bug tracker has a lot of items in it, and it\'s easy for bugs to be overlooked.

- Feature requests should be classified as type \'feature request\' in the bug tracker.

# Questions? 

If you have questions about the bug day, please add them to this section.

# Previous bug days 

::: {}
  ----------------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  Date              Accomplishments
  2004-06-05        44 bugs
  2004-07-10        18 bugs, 21 patches
  2004-08-07        19 bugs, 12 patches
  2004-11-07        12 bugs, 10 patches
  2005-06-25        10 bugs, 7 patches
  2005-12-04        11 bugs+patches
  2006-03-31        19 bugs, 9 patches
  2008-01-19        37 bugs+patches
  2008-02-23        48 bugs+patches
  2008-05-10 & 11   34 bugs+patches
  2009-04-25        [39 bugs](http://bugs.python.org/issue?@columns=title&@columns=id&activity=from+2009-04-25+to+2009-04-%20%2026&@columns=activity&@sort=activity&@group=priority&status=2&@columns=status&@pagesize=50&@startwith=0&@action=search)
  2010-11-20 & 21   [55 bugs](http://bugs.python.org/issue?@columns=title&@columns=id&activity=from+2010-11-20+to+2010-11-22&@columns=activity&@sort=activity&@group=priority&status=2&@columns=status&@pagesize=100&@startwith=0&@action=search)
  2012-11-03        [17 bugs](http://bugs.python.org/issue?@columns=title&@columns=id&activity=from+2012-11-03+to+2012-11-04&@columns=activity&@sort=activity&@group=priority&status=2&@columns=status&@pagesize=100&@startwith=0&@action=search)
  ----------------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
:::

# Preparatory Tasks 

- Need to set up log of python-dev channel
- Send announcements (python-announce, python-dev, PSF weblog, personal web log. python-list?)
