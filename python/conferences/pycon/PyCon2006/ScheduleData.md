# PyCon2006/ScheduleData

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

A tool for parsing the wiki source for the [PyCon2006/FinalSchedule](./PyCon2006(2f)FinalSchedule.html) page is available in the Python SVN repository\'s sandbox from the `sandbox/pycon`{.backtick} directory. The script is called `parse-sched.py`{.backtick}.

- [Subversion view](http://svn.python.org/view/sandbox/trunk/pycon/)

- [Download link for parse-sched.py](http://svn.python.org/view/*checkout*/sandbox/trunk/pycon/parse-sched.py)

Run the `get.sh`{.backtick} to fetch the current wiki source for the [PyCon2006/FinalSchedule](./PyCon2006(2f)FinalSchedule.html); the script will save it as `FinalSchedule`{.backtick} in the current directory.

`parse-sched.py`{.backtick} takes this file on standard input, and can generate several different output formats, chosen by the `--format=<whatever>`{.backtick} switch. The available formats are:

- print: a pretty-printed version. This is the most human-readable version.
- python: a Python module containing a data structure for the schedule.
- pickle: a pickled version of the same data structure as produced by the \'python\' format.
- html: a set of HTML tables describing the schedule.

Please feel free to submit patches that add new output formats. If you have commit privileges, feel free to just check in changes that add new formats.

Additional formats I would like to see:

- iCal
- XML
- RDF Calendar

Example invocation:

    ./parse-sched.py --format=html <FinalSchedule >schedule.html

------------------------------------------------------------------------

[CategoryPyCon2006](CategoryPyCon2006)
