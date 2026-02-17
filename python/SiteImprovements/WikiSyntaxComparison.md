# SiteImprovements/WikiSyntaxComparison

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# Wiki Syntax Comparison 

Courtesy of [RadomirDopieralski](http://moinmo.in/RadomirDopieralski "MoinMoin")\... (with editions)

::: {}
  ------------------------------------------------- ------------------------------------------------------------ --------------------------------------------- ---------------------------------------------
  **[MoinMoin](MoinMoin) 1.5 and earlier**   **[MoinMoin](MoinMoin) 1.6 and later**                **Google Code**                               **Trac**
  `WikiName`{.backtick}                             `WikiName`{.backtick}                                        `WikiName`{.backtick}                         `WikiName`{.backtick}
  `http://example.com`{.backtick}                   `http://example.com`{.backtick}                              `http://example.com`{.backtick}               `http://example.com`{.backtick}
  `["page name"]`{.backtick}                        `[[page name]]`{.backtick}                                   -no requests to add-                          wiki:\"page name\"
  `[http://example.com link text]`{.backtick}       `[[http://example.com|link text]]`{.backtick}                `[http://example.com link text]`{.backtick}   `[http://example.com link text]`{.backtick}
  `[:WikiName:link text]`{.backtick}                `[[WikiName|link text]]`{.backtick}                          `[WikiName link text]`{.backtick}             `[wiki:WikiName link text]`{.backtick}
  `[:page name:link text]`{.backtick}               `[[page name|link text]]`{.backtick}                         -no need-                                     -no need-
  `attachment:something.zip`{.backtick}             `[[attachment:something.zip]]`{.backtick}                    -no attachments-                              -full URL-
  `image:something.png`{.backtick}                  `{{attachment:something.png}}`{.backtick}                    -URL ending in .gif, .png, .jpg-              `[[Image(something.png)]]`{.backtick}
                                                    `[[page name|link text|additional parameters]]`{.backtick}                                                 
                                                    `{{page name|link text|additional parameters}}`{.backtick}                                                 
  ------------------------------------------------- ------------------------------------------------------------ --------------------------------------------- ---------------------------------------------
:::

The rationale for the change is that links, apart from those in the `WikiName`{.backtick} and bare URL styles, end up with a uniform syntax, and the embedding of an object in the page is done by modifying the bracketing style. Previously, linking to a page in the same Wiki and using a label instead of the page name involved a relatively arcane syntax; this common case now fits in much better.

The drawback of 1.6 syntax is that you need to type more and press Shift key more than necessary. Links become less readable, because of excessive decoration and lack of whitespace between logical parts. Another big problem with this syntax is that there is no pipe symbol on Russian keyboard layout, and even if don\'t need to switch layouts to copy/paste a link - you definitely need to switch it twice for the pipe to comment it. \-- [techtonik](techtonik) 2010-09-30 13:09:49

- Well, it\'s a shame about the pipe character, but the other arguments about why Moin syntax \"sucks\" aren\'t convincing: you can\'t apparently have non-WikiName links in Google Code or Trac (unless \"no need\" means that Trac figures it out), Trac still uses the baroque `wiki:WikiName`{.backtick} stuff when making a labelled link. And the full URL for attachments? It\'s exactly this kind of stuff which either confuses the Wiki when trying to label links (a problem I\'ve seen with MediaWiki) or just breaks when any aspect of the Wiki configuration changes (a problem that also comes with MediaWiki). You should definitely argue with the Moin folks about that pipe character, though. \-- [PaulBoddie](PaulBoddie) 2010-09-30 14:24:39

  - pipe character alone is enough to keep off a 80% of users. You **can** have non-WikiName links in both Trac and Google Code. What Google Code doesn\'t allow is to name your pages with non-WikiNames. Trac allows arbitrary page name and I\'ve just added Trac syntax for it. Trac supports non-baroque syntax of Google Code, and I specifically added `wiki:WikiName`{.backtick} syntax, becase explicit is better than implicit, especially if you want to illustrate how convenient are Trac namespaces for various links. As for attachments, I don\'t link them so often as to understand the underlying problem. Nor I have time to argue with authors of products I don\'t use (this wiki just forces me to it). \-- [techtonik](techtonik) 2011-01-15 14:25:45
