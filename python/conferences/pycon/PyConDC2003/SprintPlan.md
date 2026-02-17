# PyConDC2003/SprintPlan

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

## PyConDC Sprint plan 

What is a sprint?

A sprint is a two or three day focused development session, in which developers pair in a room and focus on building a particular subsystem. A sprint is organized with a coach leading the session. The coach sets the agenda, tracks activities, and keeps the development moving. The developers work in pairs using XP\'s pair programming approach.

The sprint approach works best when the first few hours are spent getting oriented \-- presenting a tutorial for the development material, laying out the stories to tackle for the day, getting everyone a CVS checkout to work with.

See also the section \"Sprinting Explained\" at the bottom of this page: [http://dev.zope.org/Wikis/DevSite/Projects/ComponentArchitecture/SprintSchedule](http://dev.zope.org/Wikis/DevSite/Projects/ComponentArchitecture/SprintSchedule)

### Sprints being planned 

- [TwistedSprint](TwistedSprint) - Come hack with the Twisted development team on Twisted or other closely-related projects.

- [I18n/l10n/Zope 3 sprint](http://dev.zope.org/Wikis/DevSite/Projects/ComponentArchitecture/PyConSprint) - The focus of this sprint will be I18n/L10n for Zope and other Python applications. See [JimsPyconSprintMessage](JimsPyconSprintMessage) and [PyconZ3SprintQuestions](PyconZ3SprintQuestions).

- [WebwareSprint](WebwareSprint) - We can\'t let the Zopatistas and Twistinis have all the fun, now, can we?

- [PyCoreSprint](PyCoreSprint) - 4 Pythonlabs folks are showing up to sprint on\... something. Add suggestions to the wiki page.

### Proposed sprint topics 

- Here are several topics that have been proposed but not accepted. If you think this would be a good sprint topic, add a comment in the wiki or send a comment to [jeremy@alum.mit.edu](mailto:jeremy@alum.mit.edu). In some cases, the topic has been assigned but the coach hasn\'t. Feel free to volunteer to coach those sprints.

- Complete the implementation of Generator Expressions

- Add a module of statistical and reduction functions: stddev, average, nlargest, nsmallest, product, etc.

- Examine two optimizations proposed by Neal Norwitz:
  - \+ Add gotos from opcodes that set \"why\" since their jump target is known in advance + Add 2 custom op-codes for CALL_FUNCTION where the number of arguments is known in advance

- Add \'diff3\' and \'patch\' to difflib

- Unify doctest\'s two approaches to finding test cases.

- Documentation sprint
  - \+ People liked the examples in the docs for unittest, sets, and itertools. Apply that model to other parts of the docs. For instance, the email and logging packages would be a lot easier to use if there were a semi-comprehensive example section in the docs.

- Python bug fixing sprint

- PythonASTSprint \-- finish the new compiler on the ast-branch \-- this should be a top priority because the project has been open for so long.

- Reduce python\'s start-up time.

- Jython sprint \-- work on some of the \"Jython should be fixed\" items from the [Jython website](http://www.jython.org/docs/differences.html)

- Improve the byte code optimizer. Several new transformations can be added after checking for basic blocks and if the jump targets can be fixed up when the total number of bytes changes. Also, the line numbering has to be kept intact during the transformations.

- Speedup list comprehensions by pre-allocating blocks of 100 list elements, writing using `PyList_SET_ITEM`{.backtick}, and adjusting the total size at the end of the comprehension.

- Update, pare-down, and clean-up Demo and Tools/Scripts

  I you want to attend the sprints, but don\'t know what topic to sprint on, you can add your name to the [ListOfInterestedSprinters](ListOfInterestedSprinters).

### Logistics 

- We are trying to minimize the cost and admin burden of hosting the sprints. We will not provide food, because there is a cafeteria a few floors down the people can use. I expect we won\'t have enough space for every possible sprint topic or sprinter. I would like to accept proposals from sprint coaches and then coordinate with the coaches to figure out how many people we can accomodate. A sprint attendee should plan to attend a single sprint. Given limited space, we might have a slight bias towards sprint topics related to the Python code, but any significant Python project would be welcome. Location: Room 307 (holds 48 people). Time: 9am till 7pm. Date: Monday 3/24, Tuesday 3/25. These figures assume two sprinters per 6-foot table. I don\'t know if this is the preferred configuration. We will need to keep the venue advsied of our requirements.

### Other information 

Here\'s some information from Guido that will at least give those interested some kind of orientation and set appropriate expectations. A summary: it\'s fine to express interest, and to record it here along with topic suggestions, but don\'t expect too much to happen until maybe a month before the conference.

- We can do this in several ways. If we make the sprinters pay extra for use of facilities during the sprint, we can basically handle as many people as sign up. If we pay for the sprint facilities out of conference surplus, we have to be more selective.

  Sprints for pure newbies (no Python experience) probably won\'t work well, although there are some local folks in DC who have some experience. (George Paci \<[george@rightinternet.com](mailto:george@rightinternet.com)\> should know more; you should ask him if he wants to run one.) Sprints for people with Python experience but no experience on a particular code base (e.g. Zope) can work if there\'s an introductory talk at the beginning. This is how Jim Fulton does most Zope3 sprints. But that takes time away from sprinting (his intro was almost a full day at the recent sprint in Rotterdam). Sprints need focused projects that have been selected by more experienced developers ahead of time; you can\'t just get together without a plan and expect much to happen.

  I suggest that we shouldn\'t try to plan the sprints just yet. But maybe someone can transfer some of this to the Wiki so there\'s info for people interested in sprints. \-- *guido, December 18, 2002*

The conference will pay for the room reservations of the sprints. Sprinters will have to take care of their own meals; there\'s a student cafeteria two floors down, plenty of restaurants nearby. You can also pool to order pizza.

------------------------------------------------------------------------

[CategoryPyCon](CategoryPyCon)
