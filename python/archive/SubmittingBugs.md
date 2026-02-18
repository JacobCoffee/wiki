# SubmittingBugs

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

**NOTE**: For updated instructions please refer to the [devguide](http://docs.python.org/devguide/tracker.html).

# Reporting Bugs in Python 

Python is a mature programming language which has established a reputation for stability. In order to maintain this reputation, the developers would like to know of any deficiencies you find in Python.

Bug reports should be submitted via the Python Bug Tracker [http://bugs.python.org/](http://bugs.python.org/). The bug tracker offers a Web form which allows pertinent information to be entered and submitted to the developers.

## Filing a Report 

The first step in filing a report is to determine whether the problem has already been reported. The advantage in doing so, aside from saving the developers time, is that you learn what has been done to fix it; it may be that the problem has already been fixed for the next release, or additional information is needed (in which case you are welcome to provide it if you can!). To do this, search the bug database using the **search tracker** box on the top of the page.

### Log In 

If the problem you\'re reporting is not already in the bug tracker, go back to the Python Bug Tracker. If you don\'t already have a tracker account, select the **Register** link in the sidebar and undergo the registration procedure. If you have an account already, enter your credentials and select **Login**. It is not possible to submit a bug report anonymously.

Once you\'re logged in, you can submit a bug.

### Create an Issue 

Select the **Create New** link in the sidebar to open the bug reporting form.

The submission form has a number of fields.

- *Title*: enter a \*very\* short description of the problem; fewer than ten words is good.

- *Type*: select the type of your problem (note: rfe stands for Request for Enhancement).

- *Component* and *Versions*: select all appropriate to this bug.

- *Change Note*: describe the problem in detail, including what you

expected to happen and what did happen. Be sure to include whether any extension modules were involved, and what hardware and software platform you were using (including version information as appropriate).

Click **submit**

Some pointers to keep in mind:

- Small code examples that don\'t depend on external code are a great way to help confirming and fixing the bug you report (providing them as [unittests](http://www.python.org/dev/workflow/#unit-test-needed) is ideal, but not required).

- Precise details about the version(s) and environment in which you have found the problem make it easier for developers to confirm your report.

- If you find a bug in previous Python releases, confirming it in the latest versions helps getting it fixed.

- Checking whether the issue was previously reported is good, but duplicates will eventually be merged by triagers.

- If you find out the issue you submitted is invalid (or a duplicate), you can close it yourself (or triagers will get to it).

- For non-conforming behavior bugs, citing the relevant RFCs and standards is a plus.

- An objective appraisal of potential or realized harm from the bug helps developers in prioritizing issues.

Understanding the usual [Issue Workflow](http://www.python.org/dev/workflow/) also helps in creating good bug reports, raising the chances of your bug report (or feature request) being resolved efficiently.

### What happens next 

See [Issue Workflow](http://www.python.org/dev/workflow/) and [general Roundup guidelines](http://www.python.org/dev/intro/#general-roundup-guidelines) for detailed descriptions of how bugs get fixed.

Each bug report will ultimately be assigned to a core developer who will determine what needs to be done to correct the problem or take the necessary steps to include a provided fix or patch into the Python source. You will receive an email update each time action is taken on the bug (it\'s possible to opt-out). Further editing and new messages can be done by the web form. You can also post to issues by replying to an email that you receive, file uploads can be done via attachments in this case.

Contributions in the form of tests, docs and patches are very welcome. The [Developer Documentation](http://www.python.org/dev/) is your main guide to the procedures and [tools of the trade](http://www.python.org/dev/tools). The [PythonBugDay](../archive/PythonBugDay) volunteer docs offers an overview focused at newcomer developers.

#### see also: 

*How to Report Bugs Effectively* [http://www-mice.cs.ucl.ac.uk/multimedia/software/documentation/ReportingBugs.html](http://www-mice.cs.ucl.ac.uk/multimedia/software/documentation/ReportingBugs.html)

- This article goes into some detail about how to create a useful bug report. It describes what kind of information is useful and why it is useful.

*Bug Writing Guidelines* [http://www.mozilla.org/quality/bug-writing-guidelines.html](http://www.mozilla.org/quality/bug-writing-guidelines.html)

- Information about writing a good bug report. Some of this is specific to the Mozilla project, but describes general good practices.
