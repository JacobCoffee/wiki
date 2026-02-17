# PackagingWG/2019-06-07-Warehouse

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

7 June 2019

**Attendees:**

- William
- Dustin
- Nicole
- Ernest
- Sumana

**TODOs**:

- William to confirm with his internal PM that it\'s ok to switch tasks now and do the initial a11y audit right away

- Nicole to reach out to some users to get direct UX feedback. Maybe Duo could help facilitate/participate

- Ernest or Dustin to talk with Filippo re Golang experience

- Sumana will schedule weekly 15 min triage, to ask \"how urgent is this\" & make delegating to volunteers easier

- Sumana to start planning coordinating volunteer effort on the finding & labelling of currently-hardcoded strings

- Sumana to ask Duo for recovery code work

- Sumana to ask Duo to offer their eyes on the existing PR \-- point out things they like/don\'t like about how William is using their library

- Sumana to ask the NYU crew for opinions on threat model/needs discussion/how much security do we need here? [GitHub](./GitHub.html) issues

- Sumana to ask Mattias to become part of this miniteam! ask re availability! Help with PR review would be great!

- Sumana to start WebAuthn rollout prep, \"how to test this\" documentation

**Agenda**:

1.  **making the most of William\'s limited time**

    1.  \[limited\] remaining in Milestone 1 (API keys & audit log)

    2.  getting reviews faster
        1.  a thumbs-up from Dustin or Ernest is sufficient to approve. They are the accepting parties.

        2.  during Eastern business hours, please \"blow \[Ernest\] up\" - if you\'re waiting for a review, ping but not via [GitHub](./GitHub.html) notifications. IRC or Slack.

    3.  tight scope of work
        1.  Sumana trying to get volunteers to do stuff that is more ancillary

        2.  TODO: Sumana will schedule weekly 15 min triage, to ask \"how urgent is this\" & make delegating to volunteers easier

2.  **availability**, especially Nicole\'s schedule for the next few months (discussion redacted for privacy)

3.  **first a11y and i18n steps**

    1.  Accessibility (estimate: 2 weeks for Trail of Bits; ? for Nicole):
        1.  Nicole: who has volunteered to help?
            1.  just Matthias.

        2.  Can we get the audit now so we can parallelize/speed Nicole\'s work?
            1.  There\'s a case for Nicole to get started. Works well for William.
            2.  If we\'re talking about running an audit, need to do that across codebase, split up front/back. Nicole could set up time with the relevant person to \.... who will it be? William?
                1.  TODO - William to confirm with his internal PM that it\'s ok to switch tasks now and do the initial a11y audit right away

        3.  some existing research on finding issues & adding a11y checks to CI: [https://github.com/SolutionGuidance/psm/issues/415](https://github.com/SolutionGuidance/psm/issues/415)
    2.  Localization/internationalisation (estimate: 3 weeks for Trail of Bits, ? for Nicole):
        1.  changing hardcoded strings to localizable: bunch of tedious labelling work. Who can/wants to do it?
            1.  Nicole could do some on templates while ToB does on views\.... could split it up

            2.  William has experience localizing C programs. Prework: ID and build tables of strings that need parameterizing. ID where they are. Makes job easier.

            3.  Nicole: has experience with this on dayjob. We ID strings that need localizing & provide context. A small description of string that needs translating. Useful to ensure quality of translation. The verb \"complete\" - could be a status or action! In French, that\'s different verb vs adjective. \"this is a COMPLETE BUTTON and when you press it, foo happens.\" In some translation software, you can add screenshots, which is also useful.

                1.  TODO: Sumana to start planning coordinating volunteer effort on this

4.  **making the most of volunteer help** (Duo, Mathias, TUF crew at NYU)

    1.  Duo & py_webauthn.

        1.  Testing?
        2.  TODO: Sumana to ask them for recovery code work!!!
        3.  TODO: Sumana to ask them to offer their eyes on the existing PR \-- point out things they like/don\'t like about how William is using their library
        4.  user testing, possible documentation\....
            1.  TODO: Nicole to reach out to some users to get direct UX feedback. Maybe they could help facilitate/participate

    2.  Mattias \[address\] [https://github.com/JazzBrotha](https://github.com/JazzBrotha) is a front end developer working at axesslab.com \<[http://axesslab.com\>](http://axesslab.com%3E). Axesslab pay their employees to work on any open source project for up to 10 hours per month, and Mattias is interested in using that time to help us! ![:D](/wiki/europython/img/biggrin.png ":D") (as of a year ago.) Already did a light audit: [https://wiki.python.org/psf/PackagingWG?action=AttachFile&do=get&target=May-2018-Warehouse-accessibility-audit-Mattias-JazzBrotha](https://wiki.python.org/psf/PackagingWG?action=AttachFile&do=get&target=May-2018-Warehouse-accessibility-audit-Mattias-JazzBrotha) [May2018WarehouseaccessibilityauditMattiasJazzBrotha.pdf](attachments/PackagingWG(2f)2019(2d)06(2d)07(2d)Warehouse/May2018WarehouseaccessibilityauditMattiasJazzBrotha.pdf) which Nicole turned into [https://github.com/pypa/warehouse/labels/accessibility](https://github.com/pypa/warehouse/labels/accessibility)

        1.  Ask for more auditing and recommendation work?
            1.  TODO: Sumana to ask Mattias to become part of this miniteam! ask re availability! Help with PR review would be great!

    3.  Trishank, Justin, Lukas Puehringer\... (multi-factor auth & TUF)

        1.  create architectural plan? prework for the upcoming Facebook-funded work????
            1.  BUT some of this will come down to the results of the RFP process.

        2.  TODO: Ernest or Dustin to talk with Filippo re Golang experience

        3.  TODO: Sumana to ask them for opinions on threat model/needs discussion/how much security do we need here? [GitHub](./GitHub.html) issues

**Any other general updates?**

- Ernest: burn rate?
  - number of invoices Ernest\'s received \.... needs updates

- Sumana: adding issues to milestones [https://github.com/pypa/warehouse/milestones?direction=asc&sort=count&state=open](https://github.com/pypa/warehouse/milestones?direction=asc&sort=count&state=open)

- Everyone: invoices!

- How close are we to merging WebAuthn?

  - very close. Maybe next week?
  - TODO: Sumana to start rollout prep, \"how to test this\" documentation

Unavailability between now & end of August: \[availability details redacted\]
