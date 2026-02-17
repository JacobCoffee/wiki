# PyConPlanning/SoftwareRequirements

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

Collects requirements for the conference software.

## Features 

- Registration for the conference
- Scheduling
- Mapping of attendee locations
- Paper submissions
- Conference feedback

## Users 

- At a minimum, we must have a user\'s e-mail address so that we can contact them.
- Users can have multiple flags set: speaker, volunteer, session chair. (More such flags may be added.)
- Users can optionally supply their geographic location for mapping, paper mailings, and for inclusion on the badges.
- Attendee e-mail addresses can be exported in order to add them to a conference mailing list.

## Paper submission 

- Users can submit proposals.
- Some users have \'reviewer\' status and can look at other people\'s proposals.
- Some users have \'organizer\' status and can mark proposals as \'accepted\' or \'declined\', and can set a scheduled time/location.
- Proposals have: title, summary/abstract, description, category, length (30/45 min), difficulty level (beginner/intermediate/advanced), a list of 3 assigned reviewers, an accepted boolean, a list of reviewer comments, and a list of uploaded documents.
- On being submitted, proposals are assigned 3 reviewers at random. If the author has reviewer status, the author must not be one of the assigned reviewers.
- Reviewers can vote +1, -1, +0, -0, or \'no vote\' on proposals, with a mandatory comment. These comments are not shown to authors until after the selection process is complete.
- Reports: all proposals, all proposals with fewer than 3 votes, all proposals with 3 or more votes grouped by their votes (all positive, all negative, a mixture).
- Reviewers can enter comments that will be e-mailed to the author. Authors can add replies to these comments.
- One-time operation: Authors can be e-mailed the review comments written about their reports.
- One-time operation: Authors are e-mailed the accept/decline decision about their proposal.

## Registration 

- Must able to produce a list of attendees, showing attendee name, T-shirt size, food preferences if any, include in delegate listing Y/N, permission to e-mail about [PyCon](PyCon) Y/N, paid/unpaid Y/N, certain special flags (e.g. speaker/session/chair) so we can hand them the right swag bag and info.

- Can charge the user\'s credit card for the appropriate amount. Or attendees can be marked as \'unpaid\', and they must then mail a cheque to the PSF.

- Must support different prices for students and non-students.

- Keeps or can generate the total revenue for the conference.

- Badge information must be exportable (or maybe we can produce PDF for printing).

- Badges must show: user\'s name, certain flags (speaker, session chair, volunteer).

- Badges can optionally show the attendee\'s organization and home location, at the attendee\'s choice.

- Attendees can register for the conference and optionally for tutorials.

- The software should track the number of attendees for each tutorial, closing registration once the tutorial has filled up.
  - Tutorial money may need to be refunded if a tutorial is cancelled.
  - Tutorial may need to be switched to another if cancelled?
  - Maybe they specify 1, 2, \... preference for am and pm, and we refund only when no preferred tutorial is available? \* Multiple attendees can be registered in one operation and charged to the same credit card. A maximum of 3 attendees is sufficient.

- Registrants can optionally donate an amount to the PSF.

- Admin: add a registrant without charging a credit card. (We still need to count free attendees for T-shirt counts, hotel bookings, etc.)

- Reports: list of all publicly visible registrants, list of all registrants (admin only), list of unregistered speakers.

- Export presentation materials into a directory tree that can be turned into the conference proceedings.

## Mapping 

- Use frapper?: [http://www.frappr.com/django/](http://www.frappr.com/django/)

- google maps integrated

- supports foreign countries

- comment and interest tags per entry

- map \'pin\' locations sent via compliant XML (to work with other google stuff)

- multiple types of \'pins\' (different colors, shapes):
  - Person

  - Sponsor of [PyCon](PyCon)

  - Corporation (employer of engineers with python experience)

  - Python Users Group

  - Zoom Group (see next bullet)

- When zoomed out merge multiple overlapping pins into one Zoom Group \'pin\'

- support search and filter of pins by interest tag and pin type

## Scheduling 

- Produce printable schedules for the entire conference, and for individual rooms for a given day.
- Track session chairs for each session.

## Sponsors 

- Sponsors can fill in a form with contact information that gets stored in a list and also e-mailed to the sponsorship coordinator.
- (Admin) The coordinator can enter sponsors who\'ve committed: contact info, sponsorship level (platinum/gold/silver), invoice number, paid Y/N, web graphic, banner provided Y/N, banner received Y/N, comments on where the banner should be displayed.

## Feedback 

- Forms for the entire conference, and for specific talks and tutorials. (Sprints aren\'t of interest.)
- Report: feedback summary for the conference, summaries for individual talks.
- E-mail authors with the results from their talk\'s feedback.

------------------------------------------------------------------------

[CategoryPyConPlanning](CategoryPyConPlanning)
