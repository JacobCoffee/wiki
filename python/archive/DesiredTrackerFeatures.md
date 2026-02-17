# DesiredTrackerFeatures

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# Desired Tracker Features

::: 
### Patch and Test Tracking

Instead of the \'needs test\' and \'needs patch\' stages, it would be better to have a checkbox grid something like this:

                NA      needs patch     has patch
    docs       ( )          ( )           ( )
    tests      ( )          ( )           ( )
    code       ( )          ( )           ( )

We could then have a \'patch incomplete\' stage instead of the \'needs\' stages, where the checkboxes would make clear what things were missing.

Instead of radio boxes we could have three drop-down inputs like:

    docs   [____________[▼]
    tests  [____________[▼]
    code   [____________[▼]

With \"not needed\", \"needed\", \"provided\", \"committed\" as possible values.

> This is probably unnecessary and adds too much clutter to the interface. It would also take 6 clicks to open the 3 dropdowns and select \"provided\". Moving the stage from \"patch review\" to \"commit review\" should be enough to indicate that the patch is complete and has docs/tests/code.

The stages could be something like \"discussing\" (when no patch has been provided yet), \"in progress\" (when there is some patch), \"committed\" (when all the patches have been committed). The stage field could also be removed altogether and replaced by these 3 fields; the additional details can be provided by the \'status\' and \'resolution\' fields.

In the meanwhile the stages could be changed to \"needs unit test\", \"needs patch\", \"needs review\", \"resolved\".

> See also some notes on [python-dev](http://mail.python.org/pipermail/python-dev/2011-March/109877.html)
:::

::: 
### Python Version Tracking

Instead of a multi-selection list for python versions, perhaps we could have a list of versions like this:

            confirmed   will apply  committed
    3.3        ( )         ( )      [      ]
    3.2        ( )         ( )      [      ]
    3.1        ( )         ( )      [      ]
    3.0        ( )         ( )      [      ]
    2.7        ( )         ( )      [      ]
         ...

This would allow the tracker to record which versions a bug is present in, even if it doesn\'t get fixed in that version, and also allow us to track the progress when more than one version needs to be patched. We might perhaps want to add a stage \'committing\' when a patch has been committed to one branch but not all. (Note: for feature requests \'confirmed\' would be left blank). \'will apply\' would be checked when someone determines that the patch, whether it exists or not, should be applied to the given branch. \'committed\' would be the revision in which the patch was committed. Ideally this would be auto-filled by the change management system based on tags in the commit message.

If the above is deemed too complex, then we should at least have a way to mark issues as accepted regardless of whether or not they have a complete patch. This is to differentiate between issues that just need work, and issues where we haven\'t even decided that we are going to accept it.

> The above is too complex and probably unnecessary. Recording the version is useful, but the roundup/hg script + the highlight on the message should already be enough. Differentiate between issues that need work and ones where we have to decide might be useful sometimes, but it\'s not so common, so it might not be worth adding another field.

Another alternative is using drop-downs, e.g.:

    3.1  [____________[▼]
    3.2  [____________[▼]
    3.3  [____________[▼]

With values like \'unaffected\', \'affected\', \'committed\', \'to be ported\'.

> Dropdowns require too many clicks, and this is probably unnecessary too.
>
> Using checkboxes instead of multi-value select elements is a huge usability win.(No references handy, just memory.) ---merwok
>
> > Checkboxes are better from an usability point of view but might make the interface more cluttered. Hiding somehow the values that are not selected might make the situation better, but previous experiments with this weren\'t too successful. Using a lower opacity for unchecked fields and restore it on hover might work. For some experiments with checkboxes see [http://psf.upfronthosting.co.za/roundup/meta/issue384](http://psf.upfronthosting.co.za/roundup/meta/issue384)
> >
> > Checkboxes could be used for versions, like:
> >
> >     [ ] 2.5   [ ] 2.6   [ ] 2.7
> >     [ ] 3.1   [ ] 3.2   [ ] 3.3
> >
> > or:
> >
> >     [ ] 2.5   [ ] 3.1
> >     [ ] 2.6   [ ] 3.2
> >     [ ] 2.7   [ ] 3.3
> >
> > the \'3rd party\' value could IMHO be removed, since there are only 3 issues opened that use it.
:::

::: 
### New Field for Module/Package

When I want to find all bugs related to one module or package, I have to use the plain text search, which could give false positives and leave out valid results. For some packages I can use a component, e.g. Distutils, but not for all. I suggest a new field that would allow selecting what module(s)/package(s) a bug apply to. This would provide reliable and discoverable URIs for people who want to monitor particular modules or packages.

> 
>
> This has been suggested and rejected a number of times on python-dev. \--RDM
>
> :   
>
>     This information is not useful. Can you list the arguments? \-- techtonik
>
>     :   
>
>         No, but it would be great if you would search the archives and post links to the threads here. \--RDM
>
>         :   
>
>             I tried with no luck. It would be useful to find the threads for future reference, but your memory is enough for me to withdraw my feature request. --merwok
>
>             :   
>
>                 Found this: [http://psf.upfronthosting.co.za/roundup/meta/issue78](http://psf.upfronthosting.co.za/roundup/meta/issue78) ---merwok
>
>                 :   
>
>                     Nice catch. But that\'s not python-dev requests RDM is referring to. -techtonik
>                     :   [http://psf.upfronthosting.co.za/roundup/meta/issue373](http://psf.upfronthosting.co.za/roundup/meta/issue373)
:::

::: 
### Easier Monitoring

(merwok)

Provide Atom feeds for saved queries to make keeping up with a particular area or component easier. (See [http://psf.upfronthosting.co.za/roundup/meta/issue155](http://psf.upfronthosting.co.za/roundup/meta/issue155), which however uses one of the legacy RSS formats.)

Add OpenSearch support to allow browsers to get search suggestions (completion) and scripts to get search results as easily-parsable feeds (see [Wikipedia's OpenSearch file](http://fr.wikipedia.org/w/opensearch_desc.php) for an example). It means adding one simple XML file, and returning search results as Atom feeds with some OpenSearch elements.

Allow any user to set her/himself as auto-nosy for some criteria. Allow any user with developer status to set her/himself as auto-assignee for some for some criteria.

> For the record, these can be done by \"Coordinators\" from the \"component\" page. Making the form editable by any user is not an option, so this would require a separate page if it\'s implemented.

Add a stats page that shows stats and graphs similar to the ones included in the weekly summary reports.
:::

::: 
### Files

(merwok)

Warn the user if they send an inappropriate file (zipfile, .exe, Microsoft office formats).

Attach files to emails sent to nosy if they have a sane mime type and size (possibly with a user option).
:   This can be already enabled in Roundup, but the sanity check should probably be implemented separately.
:::

::: 
### Misc

There could be a short (one line) description that depending on the stage of the issue says what should be done next (triaging, adding tests, a patch, review it, commit it), with a link to the respective section of the devguide.

> This could be implemented as a \"progress/stage bar\" at the top of the page that would list the stages from left to right. The current state would be highlighted somehow. The bar should probably be read-only and just provide information about the current stage of the issue and what\'s next.

The template for a new issue could include a short introduction that links to the devguide and suggests to check if a similar issue already exists before reporting a new one.

When an issue is closed stage should be automatically set to \'resolved\'. \[Done in [#595](http://psf.upfronthosting.co.za/roundup/meta/issue595)\]

There should be a field in which you can enter an issue number of an issue of which this issue is a duplicate, and submitting it should

> 1.  merge the nosy list from this issue into the specified issue
> 2.  set the resolution to duplicate
> 3.  close the issue (setting stage to resolved per above)

When a user adds a file there should be a note among the messages (or even inside the message) with a link to the added file. This would avoid confusion if the user says \"This patch \...\" and there are several files attached.

Emails can contain useful links like \"remove me from nosy\" and also link directly to the message using an anchor (i.e. \.../issue1234#msg12345).

> Removing someone from nosy via a link, IOW modifying state with a GET request, is a proved bad idea. Ok for a link that would open a page with a form that sends a POST request to remove oneself from nosy. ---merwok

Assignment should be open to anyone with an account. Assignment suggests responsibility. Many issues may be worth fixing, but not interesting enough to someone with tracker privileges to fix.

> There might be an \'assigned to\' field open to everyone is working or wants to work on the issue and a \'reviewer/committer\' field for a core developer that can review and commit the patch once it\'s ready.

Mails for \"unimportant\" changes (e.g. nosy changes, files/msgs removed) could be avoided. These changes could still be included in the next message or when enough unimportant changes are collected, making sure that it\'s clear who changed what. The only problem is that if there\'s no \"next message\" the change will pass unnoticed. This is a problem especially for messages that gets removed accidentally. See [#279](http://psf.upfronthosting.co.za/roundup/meta/issue279).

Links to msgs (e.g. msg12345) should use anchors (i.e. issue1234#msg12345).

Ability to make groups of related issues, i.e. issue7833, issue8870 and issue8871 are independent, but related and will be interesting for developer of any of them. \-- techtonik

Ability to link/track status of issues from external trackers. \-- techtonik

Consider Trac 0.12 as an alternative to Roundup [http://trac.edgewall.org/wiki/TracWorkflow](http://trac.edgewall.org/wiki/TracWorkflow) \-- techtonik

------------------------------------------------------------------------

CategoryTracker
:::
