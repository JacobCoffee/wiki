# SiteImprovements

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# pydotorg Improvement Ideas 

This page collects suggestions for improving the [PythonWebsite](PythonWebsite), this wiki and related tools.

Discussion of various bits around Python websites takes place on the following mailing lists:

General Web site (architecture, design, integration)

:   [pydotorg-www](http://mail.python.org/mailman/listinfo/pydotorg-www)

Bug tracker

:   [tracker-discuss](http://mail.python.org/mailman/listinfo/tracker-discuss)

Package index

:   [distutils-sig](https://mail.python.org/mailman3/lists/distutils-sig.python.org/)

Development workflow

:   [Core Workflow topic on Discourse](https://discuss.python.org/c/core-workflow)

Please choose the correct list, and try not to cross-post.

## A bigger picture 

Improving a web site is a process of enhancing user experience so that information is found faster and easier. Major things that need improvement can be obvious to many people, but they may seem like tasks of epic proportions, too big for an individual to consider tackling on their own. For example, implementing single sign-on for all Python services, OpenID support, an online editor for docs - these are all non-trivial tasks that require knowledge of the existing site architecture and access to the site code and supporting tools. There are also features that matter to everyone personally, and these are not obvious for everyone else: an automatic subscription to Wiki pages upon editing, various design improvements.

But the process of improvement has to solicit feedback in order to capture ideas about areas of improvement, and this channel for feedback should be easy to reach and visible to others. An example of such a channel is the online manual comments that one sees in the documentation for technologies such as PHP, MySQL [(example)](http://dev.mysql.com/doc/refman/5.0/en/multiple-tablespaces.html) and PostgreSQL.

A lot of information causes frustration: that\'s why people prefer Twitter to Blogger. Too much \"[inventory](Inventory)\" in the room makes it hard to navigate and notice things that are needed. The process of cleanup should involve throwing unused stuff away, leaving relevant and updated information in place. Naturally, the Wiki has accumulated lots of arguably unused and dated pages, but various python.org pages are affected as well. Too much information reduces the \"fun factor\": a separate status page will help people see what\'s going on and let them have more fun by focusing their work and enabling them to work together with others.

## Miscellaneous 

- (done) Fix [webmaster@python.org](mailto:webmaster@python.org) response bug (per [7929](http://bugs.python.org/issue7929 "Issue"))

- (done) Add a link to website repository at [https://github.com/python/pythondotorg](https://github.com/python/pythondotorg) see [this pull request](https://github.com/python/pythondotorg/pull/217).

- (done) Badly need bug tracker for python.org website ([metatracker issue340](http://psf.upfronthosting.co.za/roundup/meta/issue340))

  - I wonder if roundup is better than some hosted solution \-- [techtonik](techtonik) 2010-04-06 14:06:34

    - Now [on GitHub](https://github.com/python/pythondotorg/issues) \-- [SumanaHarihareswara](SumanaHarihareswara) 2019-08-23 10:39:43

## Web Site 

Note: we should probably review these, see which ones are still problems and file them [on GitHub](https://github.com/python/pythondotorg/issues), and then remove this section. \-- [SumanaHarihareswara](SumanaHarihareswara) 2019-08-23 10:39:43

- CSS: Increase interval between list items to be the same as between lines - compare [http://www.python.org/dev/doc/](http://www.python.org/dev/doc/) and [http://www.python.org/dev/pydotorg/](http://www.python.org/dev/pydotorg/)

- (done) Add #pydotorg to [http://python.org/community/irc/](http://python.org/community/irc/)

- (done) Rename \"Internet Relay Chat\" in navigation menu to IRC as it is the preferred name most people look for

- Add paragraph anchors to site generator

- Add an RSS feed and/or mailing list for python security advisories
  - Now that [the security-announce mailing list is on Mailman 3](https://mail.python.org/archives/list/security-announce@python.org/latest), resolving [this HyperKitty issue](https://gitlab.com/mailman/hyperkitty/issues/51) would add a syndication feed \-- [SumanaHarihareswara](SumanaHarihareswara) 2019-08-23 10:39:43

- Add release timer and calendar to [Core Development](http://www.python.org/dev/) page

- Have a **report bug** or **suggest a change** link leading to corresponding bug tracker ([PythonWebsiteCreatingNewTickets](PythonWebsiteCreatingNewTickets) wiki link) (issue [8146](http://bugs.python.org/issue8146 "Issue"))

- (done) [http://www.python.org/download/windows/](http://www.python.org/download/windows/) should indicate latest supported Python for old versions of Microsoft systems (see issue [8146](http://bugs.python.org/issue8146 "Issue")). Note: despite being marked done, don\'t see any indication in this direction; Windows releases currently indicate when they can\'t run on XP or earlier, but nothing says which release could be used on XP. On Jan 14 2020 Windows 7 and Windows Server 2008 R2 go off long-term support, so reminder that the download page will need updating at that point.

- (done) [http://www.python.org/Jobs.html](http://www.python.org/Jobs.html) should be moved to a database with a secure and user-friendly front-end. (Wikis won\'t do it for many people we\'re targeting.)

- Add **core development/source** page with a table of

::: {}
  ---------------- --------------------------------------------------------------------------------------------- --------------------------------------------------------------------------------------------------- ----------------------------------------------------------------------------- --------------- ---------------------------------------------
  Python Version   ViewVC                                                                                        SVN                                                                                                 Snapshot Download                                                             Code Coverage   [BuildBots](./BuildBots.html)
  2.7              [http://svn.python.org/view/python/trunk/](http://svn.python.org/view/python/trunk/)   [http://svn.python.org/projects/python/trunk](http://svn.python.org/projects/python/trunk)   [http://svn.python.org/snapshots/](http://svn.python.org/snapshots/)   ???             ???
  ---------------- --------------------------------------------------------------------------------------------- --------------------------------------------------------------------------------------------------- ----------------------------------------------------------------------------- --------------- ---------------------------------------------
:::

## Wiki Content 

If you find stale pages, please add here, this might be useful work for volunteers

- (done) The first two links at [PythonEditors#Other_Resources](PythonEditors#Other_Resources) are stale

- (done) [MacPython/PythonDistributionsForMac](../platforms/MacPython/PythonDistributionsForMac) does not mention homebrew

- [MacPython](MacPython) has a link for 10.5 Leopard but MacOS has moved on a number of releases from there. There should be something on the mess with Apple\'s buggy tcl/tk, how to not create conflicts with the system version of Python, etc.

- [BeginnerErrorsWithPythonProgramming](BeginnerErrorsWithPythonProgramming) could really stand updating and being made more useful. There are more common beginner problems than this. The page should focus on how to anticipate and not have these be such problems rather than idly speculating on whether the language could change to eliminate these \"problems\".

- (done) BeginnersGuide/Programmers could be improved: some links are probably stale (e.g. the Google course pointed at code.google.com, which is obsolete though usually still redirects correctly). It\'s just a Big Lump of Links, that\'s not very helpful in a beginner picking what to pursue (maybe add some curated mini-reviews?). Not sure - make suggestions!

- Clean up [CategoryJython](CategoryJython)

- Clean up Community/Python Writers page, above all: remove dead links
  - How to scan [DeadLinks](DeadLinks) in Python? \-- [techtonik](techtonik) 2010-03-16 08:36:41

- Shorten URLs - remove /moin/ prefix from [http://wiki.python.org/moin/SiteImprovements#Wiki](SiteImprovements#Wiki)

  - This requires moving Jython wiki from [http://wiki.python.org/jython/](../../jython/) to [http://wiki.jython.org/](http://wiki.jython.org/) and placing a temporary redirect on the previous places. \-- [techtonik](techtonik) 2010-03-16 08:39:34

- Rationalize the natural language coverage (merging the \"new\" language pages with the old ones)

## Wiki Theme 

- Upgrade the Python theme to the one used by [the EuroPython Wiki site](http://wiki.europython.eu/) ![(./)](/wiki/europython/img/checkmark.png "(./)") Added to [InterWikiMap](InterWikiMap) as `Issue`{.backtick}. For example: [7942](http://bugs.python.org/issue7942 "Issue") in the tracker. \-- [PaulBoddie](PaulBoddie) 2010-03-15 15:32:26

  - Even though natural syntax would be more welcomed this is a nice helper. Are there any side effects if the prefix is added lowercased? It seems like it is still not possible for it to show word \"issue\" automatically. \-- [techtonik](techtonik) 2010-03-15 16:47:59

  - I\'m just following the [InterWiki](InterWiki) conventions, really. I\'m sure I should use `PythonIssue:xxx`{.backtick} instead, but I suppose `Issue:xxx`{.backtick} is unlikely to be used by accident. As for the prefix, it\'s only included in the title for the icon, I think. And as for autolinking, I think that would require a parser extension or modification. I\'d personally be comfortable with a macro (like `<<PythonIssue(xxx)>>`{.backtick}), but then people would need to know how to use it, and it wouldn\'t obviously be natural to write. \-- [PaulBoddie](PaulBoddie) 2010-03-15 16:56:18

- Add \"automatically subscribe to pages I edit\" plugin from [http://moinmo.in/MoinMoinPatch/AutomaticSubscriptionOnEditPreference](http://moinmo.in/MoinMoinPatch/AutomaticSubscriptionOnEditPreference) to increase people\'s awareness about changes going on on the wiki.

- **Fix bug** can\'t rename the page (A page with the name \'xxx\' already exists. Try a different name.)

  - Can you give a walk-through of how to reproduce this? \-- [PaulBoddie](PaulBoddie) 2010-03-15 15:44:04

    - Try to rename [http://wiki.python.org/moin/ReStructuredText](./ReStructuredText.html) to [http://wiki.python.org/moin/reStructuredText](reStructuredText) without being superuser

- Remove annoying \"captcha\" for sane users who logged in
  - This just needs the feature to be [configured properly](./HelpOnTextChas.html). Then a system is required to add people to the exempt users list after their intentions have been verified. \-- [PaulBoddie](PaulBoddie) 2010-03-15 15:44:04

  - Is there an automatic group for users with 10 or more successful edits? \-- [techtonik](techtonik) 2010-03-15 17:56:09

  - I think it all has to be done manually. It would be quite easy for spammers to make accounts, perform edits manually and then automate more spamming. The [TextCha](http://moinmo.in/TextCha "MoinMoin") page has plenty of discussion about this, but I agree that it would be nicer to have some kind of workflow in the Wiki itself. \-- [PaulBoddie](PaulBoddie) 2010-03-15 19:21:55

  - It is easier for them to automate [TextCha](./TextCha.html) entry than enter it 10 times manually and in the end have their accounts banned. \-- [techtonik](techtonik) 2010-03-16 08:25:16

- Add improved event calendar support such as that provided by [EventAggregator](http://moinmo.in/MacroMarket/EventAggregator) or another similar extension

- Switch to [TracWiki syntax](http://trac.edgewall.org/wiki/WikiFormatting)

  - Why? Trac\'s syntax, apart from the stuff that\'s identical to [MoinMoin](MoinMoin)\'s syntax, is like the old [MoinMoin](MoinMoin) syntax, and although it\'s better than [MediaWiki](./MediaWiki.html) syntax in various ways (take the [link syntax](http://www.mediawiki.org/wiki/Help:Links) and its inconsistencies), switching to it would be like reverting a number of fixes that [MoinMoin](MoinMoin) applied when its syntax (particularly the [link syntax](http://moinmo.in/LinkPattern "MoinMoin")) was changed in 1.6. I don\'t deny that bits of it can be complicated, but that\'s not usually the basic stuff. \-- [PaulBoddie](PaulBoddie) 2010-03-15 15:32:26

  - Using Trac for various Python (and not only Python) I got used to separate [http://links](./(5b)http(3a2f2f)links(2f).html) with description using space\] - as it is more readable. I can\'t see where \[[LinkPattern](http://moinmo.in/LinkPattern "MoinMoin") link syntax\] will conflict with anything. Anyway it is the last point in this list. \-- [techtonik](techtonik) 2010-03-15 17:27:00

  - I\'ve become accustomed to the newer syntax now, and I think there\'s probably some reason why they moved away from the older syntax, possibly for extensibility reasons where spaces can appear naturally and confuse the process of isolating arguments. I\'ve not been too impressed by the Wiki capabilities of Trac, but that might have something to do with the visually unimpressive styling of Trac for most installations and the lack of [MoinMoin](MoinMoin) conveniences, not the syntax as such. \-- [PaulBoddie](PaulBoddie) 2010-03-15 19:21:55

  - [MoinMoin](MoinMoin) is a general purpose wiki like [MediaWiki](./MediaWiki.html) and it may happen that old syntax created problems with porting content between them. However, for software projects, Trac and [Google Code](http://code.google.com/p/support/wiki/WikiSyntax) were inspired by the old variant of markup and there is [no single ticket](http://code.google.com/p/support/issues/list) to switch to [MediaWiki](./MediaWiki.html). I would really like to see reasoning behind the choice in [MoinMoin](MoinMoin) 1.6, and know if there is a preference to turn on the old markup. \-- [techtonik](techtonik) 2010-03-16 08:20:29

  - A good summary of why the syntax was changed was posted in an IRC conversation on the #moin channel, and I\'ve uploaded it [here](SiteImprovements/WikiSyntaxComparison) \-- [PaulBoddie](PaulBoddie) 2010-04-23 11:36:53

- There should be a \"Logout\" link in the left navigation (Actions)
  - Don\'t you see a \"Logout\" link under \"User\" or are you not using the new (and awesome) default theme? \-- [PaulBoddie](PaulBoddie) 2011-03-25 20:53:00

    - I was using the \"python\" theme, now I changed to \"\<Default\>\" and I can see the \"Logout\", Thanks ! But it would be nice, if we can add a \"Logout\" link for the \"python\" theme. \-- [BaijuMuthukadan](BaijuMuthukadan) 2012-10-22 07:18:08

      - I think the \"python\" theme is unmaintained. There was a suggestion that the new default theme, also known as \"europython\", be renamed to \"python\" and thus appear for everyone who has chosen \"python\" as their theme, but that could be confusing for people. \-- [PaulBoddie](PaulBoddie) 2011-03-25 23:01:36

## Broken Links 

- Link for homepage and download on [http://pypi.python.org/pypi?%3Aaction=search&term=scapy&submit=search](http://pypi.python.org/pypi?:action=search&term=scapy&submit=search)

  - Homepage: [http://www.secdev.org/projects/scapy/](http://www.secdev.org/projects/scapy/)

  - Download: [http://www.secdev.org/projects/scapy/files/scapy-latest.tar.gz](http://www.secdev.org/projects/scapy/files/scapy-latest.tar.gz)

## Core Developer Web Resources 

The [Core Development Helper Tools](CoreDevHelperTools) page discusses enhancements for version control and bug tracking, particularly with regard to integration.

------------------------------------------------------------------------

[CategoryPythonWebsite](CategoryPythonWebsite)
