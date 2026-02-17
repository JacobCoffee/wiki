# CiviCRMImport

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

AMK\'s test setup: [http://psf.amk.ca/drupal-6.20/civicrm/dashboard](http://psf.amk.ca/drupal-6.20/civicrm/dashboard) User: psfdemo PW: zaytinya

Kurt\'s setup: Drupal 6, CiviCRM 3.3.

- [http://psfmember.org/d/](http://psfmember.org/d/) \-- Drupal

- [http://psfmember.org/d/user/login](http://psfmember.org/d/user/login) to login

- [http://psfmember.org/d/admin](http://psfmember.org/d/admin) for Drupal admin & configuration.

- [http://psfmember.org/d/civicrm/dashboard](http://psfmember.org/d/civicrm/dashboard) for CiviCRM dashboard.

# Fields for Individual import 

    birth date
    City
    Country
    Do not Email
    Do not Mail
    email
    first name
    middle name
    last name
    prefix
    suffix
    nickname
    phone
    postal code
    street address
    supplemental address 1,2
    url

# Fields for Company Membership import 

    Contact ID
    Contact e-mail
    Contact External identifier
    Is Pay Later
    Member Since
    Membership expiration date
    Membership start date
    Membership status
    Membership type
    Organization name
    Source
    Status Override 
    Test

# Fields for CiviCRM\'s membership import 

    Membership Type
    Membership Start Date
    E-mail (to match to the contact)

Discussion of importing in CRM docs: [http://en.flossmanuals.net/CiviCRM/ContactsAddingAndImporting](http://en.flossmanuals.net/CiviCRM/ContactsAddingAndImporting)

# Tasks 

## CiviCRM configuration 

- Go to Administer \> Global Settings \> Localization. Under \"Available Countries\", leave the right-hand side blank. Under \"Available States and Provinces\", add Canada, the US, the UK, Germany, New Zealand, and Argentina.

## Conversion process 

- Import individual records (nominated members, and then non-members).
  - Edit file: South Korea -\> \"Korea, Republic of\".

  - Import into CRM. Maxx\'s date format is mm/dd/yyyy. Ignore the phone field.
- Membership data:
  - Create \'nominated\' membership. Emeritus members will be created as \'nominated\' and then cancelled.
  - Does Pat have data for the initial start date?
- Import company records.
  - Export sponsor members from [MatrixMaxx](./MatrixMaxx.html).

  - Edit file: \"Corporate Member\" -\> \"Sponsor\"; \"Active\" -\> \"Current\" (watch for [ActiveState](./ActiveState.html)\'s record!)

  - Edit file: fix \@hitmeister.de e-mail, [res@opsware.com](mailto:res@opsware.com) e-mail

  - Import into CRM. Maxx\'s date format is mm/dd/yyyy.

Exports must be in CSV format, UTF-8 encoding. Maxx\'s exports are in Latin-1.

CiviCRM doesn\'t support committees; should check that the committee rosters are up-to-date on the wiki or somewhere.

Perhaps Groups could be used for this? \--KBK

# Process 

Target numbers: Companies: 37 total, 27 corporate members, 10 non-members.

Target numbers: Individuals: 138 nominated members, 23 non-members.

Should I bother converting the [MatrixMaxx](./MatrixMaxx.html) applications, for either companies or individuals? Probably not.
