# Sprint Accomplishments

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

This is a list of all the accomplishments from the [PyCon](PyCon) 2008 Sprints.

# 03/17/2008 

- Bitten continuous build tool now supports figleaf for code coverage

- Got about 20 unassigned/unclassified issues triaged.

- Python: fixed about 8 issues. Backported new buffer protocol and rest of PEP 3127 to 2.6. Converted more tests to unittest or doctest.

- Ported [Watermelons](http://www.imitationpickles.org/melons/) to the OLPC while creating a [tutorial](http://wiki.laptop.org/go/Porting_pygame_games_to_the_XO) to port pygame games to the OLPC.

- Introduced Liam to using the issue tracker and triaging bugs.

- Made TG2\'s template engine configurable

- Preliminary support for Pylons in DBMechanic

# 03/18/2008 

- Zope Interfaces now running on Jython

- Trac source browser now supports keyboard navigation

- Repoze WSGI pluggable auth middleware now does RADIUS authentication

- Python: Got around 30 unassigned/unclassified issues triaged and one code change committed.

- Python: PEP 361 written, setting the Python 2.6 schedule.

- Implemented simple encap/stow style package manager in 54 lines

- Ported [Elephants](http://www.imitationpickles.org/elephant/) to the OLPC.

- Released Graphviz plugin for Trac 0.11 and updated the release for Trac 0.10

- Made it so that shutil.move() will do os.rename() instead of a copy when moving a file to a directory. Huge speed improvement for moving files on the same file-system.

- OLPC sprint: XO-Core localization at 100% in [Khmer](https://dev.laptop.org/translate/km/) for Cambodia.

- Got a new C function-based extension type API working, after several months simmering in development.

- Made [TurboGears](TurboGears) testutil.DBTest work with SQLAlchemy (lmacken)

# 03/19/2008 

- [TracForge](./TracForge.html) now support basic web-based project creation.

- 152 broken tests corrected for SQLAlchemy\'s Oracle module

- flex-pypy proof of concept: A Flash game written in RPython\... [Pummel the chimp!](http://www.taniquetil.com.ar/py/chimp/chimp.html)

- Triaged another 40 issues, closed around six of them.

- OLPC sprint: completed main engine for original OLPC game \"Tramp Steamer Captain\"

- Got a bzr mirror of the Python SVN repository up so developers can start experimenting with it.

- Created a [WebTest](./WebTest.html)-based WSGI unit-testing framework for TG (lmacken)

- Fixed a bug that would cause smtplib SSL readlines to hang on EOF.

# 03/20/2008 

- Display code coverage in Trac browser for Bitten builds

- Ported Pygame Tutorial example code to Sugar/OLPC

- Back-ported a change from 2.6 to 2.5 which fixes a syntax problem in the generator statements.

- Got the unassigned/unprioritized issue list down under a page long. Closed 4 or 5 issues.

- Python: [Experimental Bazaar branches](http://www.python.org/dev/bazaar/) set up.

# finished 03/22/2008 

- Patch submitted for pydoc to display \'inherited\' documentation.

# Jython 

From [Frank Wierzbicki](http://fwierzbicki.blogspot.com/2008/03/pycon-2008-and-jython.html):

- Start of Twisted on Jython

- New compiler/New parser work

- Better threading support for Jython

- Collaboration with SQLAlchemy to get JDBC support

- Work on writing decimal.py as a wrapper around Java\'s [BigDecimal](./BigDecimal.html)

- Work on porting mmap to jython

- Work on 2.5 new style class exceptions

# SchoolTool Sprint 

- Removed breadcrumbs.

- Moved navigation menu to top.

- Made actions menu row of buttons.

- Yearly calendar view displays term information (Filip).

- Made [SchoolTool](SchoolTool) more beautiful (Andrew).

- Creation of a manage tab, centralizing management screens.

- Fixes to timetabling management UI (William).

- Fixed score system bug in add activities view (Paul).

- Added a home view for persons (William).

- Removed use of deprecated zapi (Alan).

- Refactored calendar portlet to be viewlet based (Filip).

- Significantly improved weekly calendar view with timetable integration (Chris).

- Improved [SchoolTool](SchoolTool) resource booking view (Andrew).

# Orbited Sprint 

- Pylons demo fixed and updated to orbited 0.3.2, thanks to Wes Devauld
- New modpython tutorial, thanks to Roy Han
- Daemonization of 0.3.2 thanks to Wes Devauld
- Great new real-time RSS Feed reader, by Jared and Phillip
- Revolved Publish/subscribe in 0.4.0 branch, thanks to Marcus Cavanaugh
- rel 0.1.12 fixes threading and memory leak issues for Orbited, thanks to Mario Balibrera
- CSP protocol redisign, thanks to Michael Carter and Marcus Cavanaugh
- dez/WSGI fixes and Pylons integration for 0.4.0 thanks to Matthew Desmaris
- Turbogears integration thanks to Toshio Kuratomi
- Long running download progress bar demo, thanks to Will (tutorial to come)
- All transports ported to Orbited 0.4.0, thanks to Marcus Cavanaugh

------------------------------------------------------------------------

[CategoryPyCon2008](CategoryPyCon2008)
