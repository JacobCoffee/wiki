# WikiName

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# Wiki Name 

A WikiName is a word that contains a group of words with spaces removed (and with starting letters of the words capitalized), e.g. [SystemInfo](SystemInfo). WikiNames automatically become hyperlinks to the WikiName\'s page. Uppercase and lowercase letters are determined by the configuration of the wiki software. The default configuration should work for UTF-8 characters (digits are treated as lowercase characters).

When you click on the highlighted page title (i.e. WikiName on this page), you will see a list of all pages that link to the current page. This even works on pages that have not been created yet.

A question mark (?) before a link or a link in gray means that the page has not yet been created. Clicking on the question mark (?) or page\'s name will send you to the default creation page where you can create that page (e.g. [NoSuchPageForReal](./NoSuchPageForReal.html)). A list of all pages that have not yet been created but are referred to on another page is located at [WantedPages](WantedPages).

*Escaping* a WikiName, i.e. if you want to write the word WikiName without linking it, can be done in one of three ways:

- An exclamation mark before the WikiName, like this: `!WikiName`.

- An \"empty\" formatting sequence (except ones which accidentally subsequence other sequences, like 4-quotes for italics interpreted as 3 quotes for bold and single quote) inside the WikiName: `Wiki''''''Name`, ``` Wiki``Name ```, `Wiki~++~Name`.

- Using of [macro](HelpOnMacros) `Verbatim`{.backtick}: `<<Verbatim(HelpOnMacros)>>`{.backtick}.

Note that last two methods disable searching or highlighting escaped WikiName.

To learn more, see [HelpOnEditing](HelpOnEditing) and [HelpOnLinking](HelpOnLinking).
