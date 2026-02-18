# PackagingWG/2019-08-02-Warehouse

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

## Bug triage/prioritization call 

August 2, 2019

### Participants 

- Sumana
- Ernest
- Will
- EMi (listening)
- Nicole

### Bugs to prioritize 

- Add collaborators by invitation - WIP PR [https://github.com/pypa/warehouse/pull/6054](https://github.com/pypa/warehouse/pull/6054)

  - is invitation-sending, and displaying whether fellow owner/maintainers have 2FA on, in scope?
    - Sumana says: no. But maybe we can get other funding to do it
    - Ernest: Out of Scope for OTF funding, but yes it is blocking other enhacements

- displaying tokens in project settings [https://github.com/pypa/warehouse/issues/6263](https://github.com/pypa/warehouse/issues/6263)

  - Ernest: Confirmed, out of scope for OTF funding, but a fairly direct carry on as enhancement. Decision is primarily User Experience based.
  - Will: Project scoped Tokens Creation/Revocation will be visible in Audit Logs to Project Owners.
  - Nicole: a good idea - if someone wants to make a PR, Nicole would be happy to help - as a volunteer

- improving error reporting to users re: token permissions [https://github.com/pypa/warehouse/issues/6232](https://github.com/pypa/warehouse/issues/6232)

  - we currently propagate msg to user by checking authz method . permits \.... \[will gives details\]; we\'d have to refactor that to propagate error msg from authz framework. This grinds against how that framework is designed.
  - TODO: Ernest will look at this, this afternoon

- Can we close [https://github.com/pypa/warehouse/issues/996](https://github.com/pypa/warehouse/issues/996) ?

  - let\'s address open question of 2FA for package upload - [https://github.com/pypa/warehouse/issues/5815](https://github.com/pypa/warehouse/issues/5815) but also asked throughout [https://github.com/pypa/warehouse/issues/994](https://github.com/pypa/warehouse/issues/994)

  - Seems reasonable to close #996 and #994 as we aren\'t going to roll back 2FA/API Tokens now ![:)](/wiki/europython/img/smile.png%20":)")

  - Will: diminishing returns to multifactor with scoped tokens \.... if there\'s an upload flow that includes 2FA

  - Ernest: requirement for client support is a big barrier. \... we would be designing in the dark without \[knowing what clients want\]

  - TODO: Sumana to synthesize that into a response, close #996.
    - for desire for the 2FA for upload w/token: what\'s the threat model? And, we\'d need a cross-project effort, funding

- 2FA: unverified-email users get banner linking to nonexistent anchor [https://github.com/pypa/warehouse/issues/6239](https://github.com/pypa/warehouse/issues/6239)

  - Ernest: +1 to getting this done
  - Moved to OTF security work milestone

- add caveats to macaroons for expiration (time) and version [https://github.com/pypa/warehouse/issues/6255](https://github.com/pypa/warehouse/issues/6255)

  - Ernest: Out of Scope for this funding, \"PR welcome!\" territory, but funding would be best given the UX can of worms additional caveats opens.

  - Will: important but out of scope. Time & use scoped macaroons are pinnacle of limited authority. Limit to \"this IP address\"

  - TODO: Will to add that \^ to issue \-- done

- showing token creation UI on confirmation page [https://github.com/pypa/warehouse/issues/6257](https://github.com/pypa/warehouse/issues/6257)

  - Ernest: I still find this confusing, but defer to UXperts ![:)](/wiki/europython/img/smile.png%20":)")

  - TODO: Nicole will check via user tests

- user support ticket system [https://github.com/pypa/warehouse/issues/3231](https://github.com/pypa/warehouse/issues/3231)

  - Ernest: Certainly not in scope for OTF funding\... but omg this remains a thing that would be lovely.
  - Off-the-shelf: No one was willing to donate one to us when we last looked.
  - TODO: Sumana and Ernest to discuss further

- 50x error on non-prefixed tokens [https://github.com/pypa/warehouse/issues/6347](https://github.com/pypa/warehouse/issues/6347)

  - Ernest: can triage, but offhand do not see anything in sentry :\|
  - William: I think this might have been fixed by the latest prefix changes \-- will have been, that is
  - TODO: Sumana to keep up comm on this - re coming fix

- [https://github.com/pypa/warehouse/issues/6345](https://github.com/pypa/warehouse/issues/6345) API tokens: Remove \@token and pypi: cases

  - set a timeline for removing old tokens
  - Ernest\'s concern: let\'s make sure what we change @ to is not a pain
  - TODO: Nicole to look

### Things to user test 

Nicole:

- planning on running a few short-ish user tests for API tokens & audit logs

- discussion of what timing would be better for project management; decided to try to get some API token user tests scheduled for next week, and then do audit log tests later

### Accessibility milesone 

Nicole:

- a11y milestone - would be helpful to get more things to fix
  - TODO: Will: she\'s running out of tickets! send her views to check/fix
  - zooming - 400%, do things still work? some things need to be fixed. Tend to be the same as things in l10n, as that\'s where things get cut off. So that\'s also i18n prep!! yay!
  - TODO: Sumana to coordinate with Nicole re user test audiences \-- especially people using screenreaders

### TODOs 

- Ernest to look at improving error reporting to users re: token permissions [https://github.com/pypa/warehouse/issues/6232](https://github.com/pypa/warehouse/issues/6232) this afternoon

- Ernest and Sumana to discuss options re: user support ticket system [https://github.com/pypa/warehouse/issues/3231](https://github.com/pypa/warehouse/issues/3231)

- Sumana to close [https://github.com/pypa/warehouse/issues/996](https://github.com/pypa/warehouse/issues/996)

- Sumana to keep up communications with community on upcoming fix for 50x error on non-prefixed tokens [https://github.com/pypa/warehouse/issues/6347](https://github.com/pypa/warehouse/issues/6347)

- Sumana and Nicole to coordinate on finding user testers, especially screenreader users, for a11y work

- Nicole to look at [https://github.com/pypa/warehouse/issues/6345](https://github.com/pypa/warehouse/issues/6345) API tokens: Remove \@token and pypi: cases

- Nicole to include assessing showing token creation UI on confirmation page [https://github.com/pypa/warehouse/issues/6257](https://github.com/pypa/warehouse/issues/6257) in user tests

- Will to send Nicole a11y things to fix
