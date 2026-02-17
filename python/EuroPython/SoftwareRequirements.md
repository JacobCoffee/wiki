# EuroPython/SoftwareRequirements

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# EuroPython Conference Software Requirements 

This page is derived from [PyConPlanning/SoftwareRequirements](./PyConPlanning(2f)SoftwareRequirements.html) but focuses on things that have proven more relevant to [EuroPython](EuroPython). The requirements here do not directly address general conference Web site issues, such as [http://www.europython.org/](http://www.europython.org/) which focuses on the publishing of general information about the conference.

------------------------------------------------------------------------

## Existing Software 

There are a few solutions people are using for conference management, including the following:

- [Indico](http://cdsware.cern.ch/indico/) - used for [EuroPython](EuroPython) 2006 and 2007

- [Zookeepr](http://www.zookeepr.org/) - developed for linux.conf.au

- [PyCon-Tech](https://pycon.coderanger.net/) The [PyCon](PyCon) submissions and schedule system - developed for [PyCon](PyCon) and being developed further for [PyCon](PyCon) UK

- [EuroPython Software](https://github.com/pythonitalia) - This was specifically written for [EuroPython](EuroPython) by the Python Italia user group as Django application and is open-source (only the design files are not open-source). It was used for [EuroPython](EuroPython) 2011-2013 and is the official conference software for [EuroPython](EuroPython) conferences.

------------------------------------------------------------------------

## Essentials 

These are things which have been central to the organisation of [EuroPython](EuroPython) and which have already been managed using conference software:

- Account management
- Registration
- Paper/talk submissions
- Scheduling

## Extras 

These are things which could have been managed using conference software or which could have been made easier using such software:

- Feedback
- Sponsor management

## Luxuries 

These are things which people seem to find interesting but which haven\'t been the focus of the [EuroPython](EuroPython) organisers:

- Mapping of attendee locations

------------------------------------------------------------------------

## Account Management 

It is not generally a good idea to allow unauthenticated users to register for a conference - this tends to attract speculative registrations from people who seem not to be serious about attending. However, a few use-cases need to be supported for people logging in to\...

- Register themselves
- Register other people
- Submit/edit/withdraw materials created by themselves or collaborators
- Review paper/talk submissions
- Manage aspects of the conference

One limitation of the Indico instance hosted at CERN was the insistence that registrants must have their own account. Creative workarounds include using distinct e-mail aliases belonging to one person.

## Registration 

This combines some of the [PyCon](PyCon) requirements for \"users\" with more general requirements:

- Support the following information:
  - Name

  - E-mail address

  - Registrant status: participant, speaker, volunteer, session chair

  - Registrant class: student, normal

  - Payment class: paid, unpaid

  - Geographic information (this is more relevant for [EuroPython](EuroPython) given the number of countries involved)

  - Organisation

  - Other contact details

  - Privacy preferences (would (not) like name published in delegate listing, would (not) like e-mail notifications)

  - T-shirt size (if appropriate)

  - Food preferences (if any)
- Export/reports of registrant information
- Badges must be able to show name, class/status, organisation, origin and must obviously be exportable (as PDF, for example)
- Payment:
  - Support e-payment and later payment (bank transfer being the norm in Europe)
  - Support non-paying registrants (guests, invitees)
  - Must support different prices for students, non-students (and other classes of registrant)
- Keeps or can generate the total revenue for the conference
- Support tutorial registration and extra events
- Support capacity limits for tutorials and extra events
- Optional donations and/or extra items
- Support editing and cancellation of registrations by both users (for their own registrations) and by administrators

## Paper/Talk Submissions 

See \"Account Management\" for some relevant criteria.

- Reviewers can look at other people\'s proposals

- Organisers can mark proposals as \'accepted\' or \'declined\', and can set a scheduled time/location

- Proposals have: title, summary/abstract, description, category, length (30/45 min), difficulty level (beginner/intermediate/advanced), a list of 3 assigned reviewers, an accepted boolean, a list of reviewer comments, and a list of uploaded documents

- A mechanism must exist for reviewers to choose or be assigned submissions; [PyCon](PyCon) requirements involve assigning 3 reviewers at random (excluding the author)

- Reviewer voting or the mechanisms to form a consensus

- Exports/reports showing the status of submissions and their scores

- Reviewers and users can comment, but some reviewer comments can be withheld from the user until a decision is made

- Notifications via e-mail about comments and decisions

- Export conference materials for proceedings

## Scheduling 

- Produce online schedules with talk information, track/theme membership for each room
- Produce printable schedules for the entire conference, and for individual rooms for a given day
- Track session chairs for each session
- It can be nice to be able to edit the schedule interactively
- Room management: desirable to be able to switch or rename rooms globally

## Sponsors 

- Sponsors can fill in a form with contact information that gets stored in a list and also e-mailed to the sponsorship coordinator
- Support the following information:
  - Contact information
  - Sponsorship level (platinum/gold/silver)
  - Invoice number
  - Paid (Y/N)
  - Web graphic, banner provided (Y/N)
  - Banner received (Y/N)
  - Comments on where the banner should be displayed

## Feedback 

- Forms for the entire conference, and for specific talks and tutorials (but not sprints since they\'re separate things)
- Report: feedback summary for the conference, summaries for individual talks
- E-mail authors with the results from their talk\'s feedback

------------------------------------------------------------------------

## Experiences with Indico 

[Indico](http://cdsware.cern.ch/indico/) has been used to manage [EuroPython](EuroPython) 2007. Here\'s how it fares in the above criteria:

::: {}
+:---------------------------------------------:+:------------------------------------------------------:+
| **Account Management**                                                                                 |
+-----------------------------------------------+--------------------------------------------------------+
| **Register yourself**                         | *Yes*                                                  |
+-----------------------------------------------+--------------------------------------------------------+
| **Register others**                           | *Not at CERN*                                          |
+-----------------------------------------------+--------------------------------------------------------+
| **Submit/edit/withdraw your own materials**   | *Yes*                                                  |
+-----------------------------------------------+--------------------------------------------------------+
| **Submit/edit/withdraw materials for others** | *Only as administrator*                                |
+-----------------------------------------------+--------------------------------------------------------+
| **Review materials**                          | *Yes*                                                  |
+-----------------------------------------------+--------------------------------------------------------+
| **Administer conference**                     | *Yes*                                                  |
+-----------------------------------------------+--------------------------------------------------------+
| **Registration**                                                                                       |
+-----------------------------------------------+--------------------------------------------------------+
| **Registrant information**                    | *Supported - can add arbitrary fields*                 |
+-----------------------------------------------+--------------------------------------------------------+
| **Export/reports of registrant information**  | *Yes (PDF, CSV)*                                       |
+-----------------------------------------------+--------------------------------------------------------+
| **Badges**                                    | *Supported - interactive editor and PDF export*        |
+-----------------------------------------------+--------------------------------------------------------+
| **e-payment**                                 | *Yes*                                                  |
+-----------------------------------------------+--------------------------------------------------------+
| **Pay later**                                 | *Yes*                                                  |
+-----------------------------------------------+--------------------------------------------------------+
| **Non-paying registrants**                    | *Yes (1)*                                              |
+-----------------------------------------------+--------------------------------------------------------+
| **Different prices/rates**                    | *Yes*                                                  |
+-----------------------------------------------+--------------------------------------------------------+
| **Can generate total revenue**                | *No - would need to include non-registration revenues* |
+-----------------------------------------------+--------------------------------------------------------+
| **Tutorials and extra events**                | *Yes (2)*                                              |
+-----------------------------------------------+--------------------------------------------------------+
| **Capacity limits on events**                 | *Yes*                                                  |
+-----------------------------------------------+--------------------------------------------------------+
| **Optional donations/extra items**            | *Yes (2)*                                              |
+-----------------------------------------------+--------------------------------------------------------+
| **Edit registrations yourself**               | *Yes*                                                  |
+-----------------------------------------------+--------------------------------------------------------+
| **Edit other registrations**                  | *Only as administrator*                                |
+-----------------------------------------------+--------------------------------------------------------+
| **Cancel registrations yourself**             | *No*                                                   |
+-----------------------------------------------+--------------------------------------------------------+
| **Cancel other registrations**                | *Only as administrator*                                |
+-----------------------------------------------+--------------------------------------------------------+
| **Paper/Talk Submissions**                                                                             |
+-----------------------------------------------+--------------------------------------------------------+
| **Reviewer role**                             | *Yes*                                                  |
+-----------------------------------------------+--------------------------------------------------------+
| **Organiser role**                            | *Yes*                                                  |
+-----------------------------------------------+--------------------------------------------------------+
| **Submission information**                    | *Supported*                                            |
+-----------------------------------------------+--------------------------------------------------------+
| **Reviewer assignment**                       | *Done manually*                                        |
+-----------------------------------------------+--------------------------------------------------------+
| **Reviewer voting/consensus forming**         | *Yes*                                                  |
+-----------------------------------------------+--------------------------------------------------------+
| **Export/reports showing submission status**  | *Yes - filtering and export possible (XML, PDF)*       |
+-----------------------------------------------+--------------------------------------------------------+
| **Reviewer comments (public and hidden**      | *Yes*                                                  |
+-----------------------------------------------+--------------------------------------------------------+
| **User comments**                             | *Yes*                                                  |
+-----------------------------------------------+--------------------------------------------------------+
| **E-mail notifications**                      | *Yes*                                                  |
+-----------------------------------------------+--------------------------------------------------------+
| **Export as proceedings**                     | *Yes*                                                  |
+-----------------------------------------------+--------------------------------------------------------+
:::

1.  An \"invitation code\" feature would let people register without manual validation of non-paying registrants afterwards. Generally, some kind of validation mechanism would be required, anyway.
2.  Add chargeable items to the form for extra events and items.
