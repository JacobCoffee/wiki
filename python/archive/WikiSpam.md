# WikiSpam

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

Occasionally the Wiki is hit by spammers trying to increase Google\'s ranking for their sites by adding links to them. These spammers may replace a page\'s content with dozens of links, or they may insert links into the existing text.

# Fixing the Changes 

To fix changes, follow the little \'i\' icon next to the page\'s [RecentChanges](RecentChanges) entry, or select `Info`{.backtick} on the page itself (which may be an \'i\' icon depending on which theme you are using). You\'ll find a history of all versions and a revert button for each of them. Usually you can just revert to the previous version. You can also select a version and then on the page (possibly depending on the theme) choose `Revert to this revision`{.backtick} from the actions menu.

# Preventing Future Attacks 

Generally, the TextCHA support should help prevent attacks and reduce the likelihood of recurrence. Previously, the following advice was much more important.

Edit the [LocalBadContent](LocalBadContent) page. This page records a bunch of regular expression patterns that are applied to all of the links in a page; if a matching link is found when the page content is saved, the save will be disallowed and an error will be reported.

Remember that this page lists regular expressions, not strings, so the \'.\' character will match any character. If you\'re matching a domain such as foo.com, add `foo\.com`{.backtick} to the page.

See [AntiSpamGlobalSolution](http://moinmo.in/AntiSpamGlobalSolution "MoinMoin") for more details.
