# ClarkUpdike

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

[/ScrapBook](ClarkUpdike/ScrapBook) My page for temporary content

# Wiki Tidbits 

## Deleting wiki pages 

These are the directions I use for deleting pages on an intranet moinmoin wiki I administer. These directions assume you have a login on the host machine, allowing you to temporarily turn on a flag in a config file that let\'s you delete a page and then turn it off (making it safe since it\'s only temporarily enabled). I\'ve tried to adapt them for this (jython) wiki.

First of all, if you aren\'t in the [MoinPagesEditorGroup](MoinPagesEditorGroup), you\'ll need to contact an admin, and remind them to follow the directions on this page.

To delete a wiki page:

- make sure that MoinMoin acl is activated in moin_config.py (it should be left on)

- turn on the DeletePage action in moin_config.py (look for the \'security critical actions\' section towards the bottom of the file and set the \"if 0:\" to \"if 1:\" )

- put an acl entry on the page:

<!-- -->

    #acl MoinPagesEditorGroup:read,delete

- edit the page and look for the DeletPage action at the very bottom

- follow the steps to delete the page

- turn off the DeletePage action in moin_config.py

Note: moin_config.py is probably here, `<wiki home>/moin/<wiki name>`{.backtick}

## Misc 

- Create an anchor.

<!-- -->

    [[Anchor(myAnchorLabel)]]

\*Linking to anchors on another page
:   you must use an \"interwiki\" style link.

<!-- -->

    [wiki:Self:SomePage/SomeSubPage#someBookmark bookmarkDisplayText]

- Footnotes macro^[1](#fnref-1151ad7600a53a0620d4755d42af8e668e1ed7a5)^

<!-- -->

    [[FootNote(This is a sample footnote [look for it at the bottom of the page].)]]
    Must be separated from the prior word by a space.

- Force a new page (aka arbitrary page name).\

<!-- -->

    ["/mynewpage"]

- Link to a subpage (there several ways to do [this](./HelpOnEditing(2f)SubPages.html))\

[Eclipse notes](../developer-guide/JythonDeveloperGuide/EclipseNotes)\
[JythonDeveloperGuide/EclipseNotes](../developer-guide/JythonDeveloperGuide/EclipseNotes)

    [wiki:Self:JythonDeveloperGuide/EclipseNotes Eclipse notes] <- link on arbitrary text
    JythonDeveloperGuide/EclipseNotes                           <- wiki style link

- Prevent a new page with and without code font.\

::: {}
  ------------------- ---------------------------- ---------------------------
  with code font      `PySystemState`{.backtick}   `` `PySystemState` ``
  without code font   PySystemState                ``` Py``System``State ```
  ------------------- ---------------------------- ---------------------------
:::

- Embedding python (one way\--there\'s [others](HelpOnFormatting#codeDisplay)).\

<!-- -->

    {{{
    #!python
    print "jython rocks!"                
    } } } <-- don't include these spaces (it's just to escape them)

- Or ticks for `print "jython rocks!"`{.backtick}.\

<!-- -->

    `print "jython rocks!"`

- Inserting \"new lines\" into a paragraph.\

<!-- -->

    [[BR]]

::: footnotes
1.  []This is a sample footnote \[look for it at the bottom of the page\]. ([1](#fndef-1151ad7600a53a0620d4755d42af8e668e1ed7a5-0))
:::
