# PSF Python Job Board/Relaunch Project

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# PSF Python Job Board: Relaunch Project 

The jobs board relaunch project was started early in 2014 and completed early in 2015, taking much longer than expected due to issues we found with the jobs app implementation in the new python.org website, which was launched in 2014.

This page was used to run the project.

------------------------------------------------------------------------

The Python job board was run by single volunteers for many years. Since the job board activities have significantly increased in recent years, and the last Chris Withers, who ran the board in the years 2010-2013, left the project, the PSF would like to relaunch the project using a team of volunteers.

At the same time, we\'d like to move the job board from the legacy site to the new relaunched [http://www.python.org/](http://www.python.org/) Django based site.

## Old job board process 

*Please note that this description may not be completely correct. It just describes the process based on the how-to document.*

Job submissions were processed using email, a ReST template and a page in a subversion repository.

1.  Job submitters created a job posting based on the template listed on the [Job board how-to page](http://legacy.python.org/community/jobs/howto/)

2.  Submissions were checked against a list of quality criteria

3.  Submissions which needed refinement were sent back with a notice of what to fix

4.  Good submissions were added to the job page in order of submission date (in most recent first order)

Page cleanup:

- entries older than three months were regularly removed
- filled positions were removed upon request by the job submitter

## New job board process 

*Please note that this process is just a sketch. It may well change and get more refinements in coming weeks.*

Job submissions are entered into a web form, the form creates a database record which is then used for review. After approval the Django site will then list the submissions automatically.

1.  Job submitters log in to the website (after having registered for an account)
2.  Submitters create a job posting record
3.  Submissions are checked against a list of quality criteria by the reviewers
4.  Submissions which needed refinement are flagged and an email is sent back to the job submitter asking for changes
5.  Good submissions are approved and then automatically listed on the job board page in order of submission date (in most recent first order)

Questions:

- How to inform the job submitters of problems with their submissions ?
- Should we have 1 person or 2 person reviews ?

Possible solutions for questions:

- The submission could be like a blog post, that way, the submitter could edit the submission while it\'s not published and leaving the team members to comment on the submission (alerting the submitter of any comments) regarding problems with the submission.
- The submitter could also tick a checkbox to delete his submission.

To be clarified:

- Exact status workflow of job submission records
- Classification of job submissions (there are multiple categories available)
- Quality criteria
- Team member assignments to the review process (e.g. by category)
- Porting the existing job board submissions into the new site\'s database

What we need:

- team members who can help refine the job board Django app (good Django skills are necessary)
- team members who regularly log in and review postings
- team members who can help interface to the Django site maintainers, e.g.review and process pull requests, issue tickets in case of problems with the site
- team members who lead the groups and signal problems to the PSF board, should any arise

## Jobs app design 

The jobs Django app is already available, but not yet complete.

To get it to a usable state, we\'ll have to work some more on the code and the templates. Here\'s what we need to do:

- review the existing app
- come up with user stories to define the workflows and UI
- distill these into feature requests
- open tickets and implement the changes necessary to make those user stories work

Please run reviews of the existing app and post them on the review page:

- [../Jobs App Reviews](Jobs App Reviews)

We collect user stories on this page:

- [../Jobs App User Stories](Jobs App User Stories)

These will then be distilled into feature requests / implementation phases on this page:

- [../Jobs App Feature Requests](Jobs App Feature Requests)

### Job Model Reference 

Notes on how various field in the database should be updated:

- **Region**: If not applicable, set to the same thing as \"Country\", until this is no longer a required field. ([GitHub Issue](https://github.com/python/pythondotorg/issues/271))

- **Job Start Date**: Date of the posting

- **Job End Date**: 3 months after \"Job start date\" (by default)

- **Status**: The first person to migrate it should mark it as \"review\". Someone else should double-check and mark as \"approved\". Ones submitted by external users should be \"draft\" if no one has looked at it yet.

## Project organization 

### Roles 

We have so far identified these roles in the team:

- [../Drafters](Drafters) - team members who help with getting existing job board listings and the mailing list backlog entered into the database

- [../Reviewers](Reviewers) - team members who review job postings and help giving usability feedback to the developers

- [../Developers](Developers) - team members with Django skills to help with improving the Django app

We will also need leaders of both groups and possibly an overall project lead to coordinate the work of the groups and provide an interface to the PSF board.

Once established, we should transfer the project into a regular PSF work group.

### Mailing list 

The project is run using a mailing list dedicated for the team:

- [Python Jobs Mailing List](https://mail.python.org/mailman/listinfo/jobs)

The list gets all email sent to [jobs@python.org](mailto:jobs@python.org). The old process used this email address for job submissions. The new process will use a web form based approach instead.

If you want to help in the job board team, please write to [jobs@python.org](mailto:jobs@python.org).

Here\'s the mailing list archive with our current job submission backlog:

- [Python Jobs List Archive](https://mail.python.org/mailman/private/jobs/) (requires login)

The last processed job submission is dated 12-Feb-2014.

### Issue tracker 

- [python.org site\'s issue tracker](https://github.com/python/pythondotorg/issues)

Please open tickets for any problems you find with the jobs app. The tickets should be labeled as \"job board\", if possible (github restricts using labels). If not possible, please prefix the ticket title with \"JB:\" or use \"job board\" in the title. We can then add labels after ticket creation.

## Resources 

### New job board 

- [Job board temporary installation](http://www.python.org/newjobs/) on the production site. This is a temporary location of the new Python job board, run using Django and backed by a database.

  ![/!\\](/wiki/europython/img/alert.png "/!\") Please note that the database used by this temporary installation is the production one, so any changes to the database contents should be done with care!

- [Staging system implementation of the new job board](https://staging.python.org/newjobs/) This runs a copy of the production database on the staging branch of the python.org repository.

- [New job board](http://www.python.org/jobs/) This will be the production location of the Python job board.

  **Note: At the moment this still redirects to the legacy single page job board.**

*Deprecated:*

The project\'s fork of the main python.org site repo is no longer used and just listed here as reference, since it still has some tickets open which need to be merged to the upstream python.org repo tracker:

- [Python Jobs Board Github Repository](https://github.com/python-jobs-board/pythondotorg) We were using this for the jobs app development. It\'s a fork of the main python.org repo.

- [Python Jobs Board Issue Tracker](https://github.com/python-jobs-board/pythondotorg/issues?state=open) This is the tracker we were using for the jobs app development. Development has now (2015) moved back to the main python.org repository.

### Old job board 

- [Job board listing ported from the legacy site](http://www.python.org/community/jobs/) This is a single page which has to be manually maintained via the Django admin interface.

- [Legacy job board site](http://legacy.python.org/community/jobs/) This page was manually maintained through the Subversion repository which runs the legacy website.

- [Job board how-to explaining the process that was used for the legacy site](http://legacy.python.org/community/jobs/howto/)

### Web site administration 

- [Django admin interface of the new site](https://www.python.org/admin/)

- [New site\'s issue trackers](https://github.com/python/pythondotorg/issues) If you find problems with the job app, please open tickets on this tracker.

### Web site code base 

- [Github repository of the new site](https://github.com/python/pythondotorg)

- [Job app code](https://github.com/python/pythondotorg/tree/master/jobs)
