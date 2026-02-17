# PSF Python Job Board/Drafters

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# PSF Python Job Board Drafters 

## Team members 

These are team members who help porting existing job postings from the old job board page and new postings to the jobs mailing list into the database:

- *Please add your name here.*

- [GilesThomas](GilesThomas)

- [FrancoRobles](FrancoRobles)

- [MarcAndreLemburg](MarcAndreLemburg)

- [GregBack](./GregBack.html)

- [MelanieJutras](./MelanieJutras.html)

- [SteveBarnes](SteveBarnes)

- [SimonHayward](./SimonHayward.html)

## Tasks 

- add existing job postings from the [single page version of the job board](http://legacy.python.org/community/jobs/) to the database as approved entries

  *This is done.*

- add job postings sent to the [jobs list since mid-January](https://mail.python.org/mailman/private/jobs/) to the database as draft entries

  *This is done.*

- add new postings sent to the [jobs list since March 11](https://mail.python.org/mailman/private/jobs/) to the database as draft entries

  *This is an ongoing, until we switch on the form submission process.* Please also email back to the job submitters that the job board is undergoing changes and that their submission was added to our database.

## Resources 

- [Jobs table in the Django admin interface](https://www.python.org/admin/jobs/job/)

**FAQs regarding using the Job Board django admin interface :**

*category* : Since the admin system doesn\'t currently let you choose one, you must determine the number of the category. You can do this by clicking on the search icon next to the category box then hovering over the item. You will see the number in the url at the bottom (for example, software engineer is 2)

*job type* : Choose some if they match, Make a note if you have ideas for new types that you didn\'t see on the list

*region* : do your best or duplicate the city name if you don\'t know the region since this is a required field

*start date* : today

*end date* : today plus 3months

*status* : review (this will indicate the posting is ready for review by a Job Board member)

*agencies* checked means \"ok for agencies to contact\"
