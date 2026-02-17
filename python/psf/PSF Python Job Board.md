# PSF Python Job Board

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# PSF Python Job Board 

This page describes the PSF Python Job Board which is run by volunteers to provide the Python community with an important resource to find jobs where they can use Python.

## Job board process 

Job submissions are entered into a web form, the form creates a database record which is then used for review. After approval the Django site will then list the submissions automatically.

1.  Job submitters [log in to the website](https://www.python.org/accounts/login/?next=/jobs/create/) (after having registered for an account)

2.  Submitters [create a job posting record](https://www.python.org/jobs/create/)

3.  Submissions are checked against a list of quality criteria by the reviewers using the [review panel](https://www.python.org/jobs/review/); see the [/Reviewers](./PSF(20)Python(20)Job(20)Board(2f)Reviewers.html) page for details on the review process

4.  Submissions which need refinement are rejected together with a note mentioning the reason for rejection (using the \"review\" button on the review panel).

5.  Good submissions are approved and then automatically listed on the job board page in order of submission date (in most recent first order)

Job postings are automatically unlisted after 90 days. They can also be removed or archived manually using the Django database interface by setting the job listing status setting to *removed*.

Remarks:

- Submissions which have problems could also be refined directly in the system by the submitters, provided they created it while being logged in. The review page doesn\'t show this status, though, so it\'s probably better to go with the rejection procedures for the time being.
- Reviews by multiple persons would need to be coordinated, since the system does not provide this functionality. For the time being, it\'s better to have one person do the review.

## Project organization 

The job board team has decreased a lot due to the long project run time. We will launch with a small team of reviewers:

- [/Reviewers](./PSF(20)Python(20)Job(20)Board(2f)Reviewers.html) - team members who review job postings The review process is also described on the above page.

Issues we find are posted to the [python.org site\'s issue tracker](https://github.com/python/pythondotorg/issues)

- and tagged with \"job board\". The issues are then either worked on by the PSF contractors assigned to the python.org website project, or volunteers who want to help.

The job board team itself will not focus on the development anymore for the time being.

## Mailing list 

The volunteers use a mailing list to coordinate:

- [Python Jobs Mailing List](https://mail.python.org/mailman/listinfo/jobs)

The list gets all email sent to [jobs@python.org](mailto:jobs@python.org). In the previous system, job postings were sent in via email. This is no longer necessary and new submissions should only be done via the [web interface](https://www.python.org/jobs/create/).

The jobs app will send notification about new postings to this list, so that reviewers get notified of new submissions.

If you want to help in the job board team, please write to [jobs@python.org](mailto:jobs@python.org).

Here\'s the mailing list archive:

- [Python Jobs List Archive](https://mail.python.org/mailman/private/jobs/) (requires login)

## Relaunch Project 

In the years before the relaunch, the jobs board was run by single volunteers. Since the load had increased a lo and the last volunteer, Chris Withers, had left the project, the PSF wanted to replace the jobs board with a team of volunteers using a database driven integrated jobs app.

From 2014 to 2015, a team of volunteers worked to relaunch the job board using a jobs app on the new python.org website (which was launched in 2014).

The relaunch project page is still available: [/Relaunch Project](./PSF(20)Python(20)Job(20)Board(2f)Relaunch(20)Project.html)

## Resources 

### Production 

*Note: The jobs app used to run under the temporary URL /newjobs/ during development. This has now been changed back to /jobs/.*

- [Job board jobs listing](http://www.python.org/jobs/) on the production site.

- [Job board review panel](http://www.python.org/jobs/review/) This allows reviewing new job postings.

### Staging 

*Note: The jobs app used to run under the temporary URL /newjobs/ during development. This has now been changed back to /jobs/.*

The staging system can be used to check new developments.

- [Staging system implementation of the new job board](https://staging.python.org/jobs/) This runs a copy of the production database on the master branch of the python.org repository and is updated frequently.

- [Staging system job board review panel](http://staging.python.org/jobs/review/) on the staging site.

### Web site administration 

- [Django admin interface of the python.org site](https://www.python.org/admin/)

- [New site\'s issue trackers](https://github.com/python/pythondotorg/issues) If you find problems with the job app, please open tickets on this tracker.

### Web site code base 

- [Github repository of the new site](https://github.com/python/pythondotorg) (includes the jobs app)

- [Job app code](https://github.com/python/pythondotorg/tree/master/jobs)
