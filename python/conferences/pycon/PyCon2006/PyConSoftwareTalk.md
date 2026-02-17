# PyCon2006/PyConSoftwareTalk

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

This talk will cover the [PyCon2006](PyCon2006) software evolution, lessons learned and what to do next.

When:

- Sunday 2:10-2:55

Where:

- Bent Tree

Who should Attend:

- People interested in the automation of [PyCon](PyCon) via web applications

- People who want to know how we did all those cool things on us.pycon.org

- People who plan on attending the [Conference Software Sprint](http://wiki.python.org/moin/PyCon2006/Sprints/ConferenceSprint).

## Attendees 

- Douglas Napoleone

- Jeff Rush ([jeff@taupro.com](mailto:jeff@taupro.com))

- Martin Thomas ([martin@martinthomas.net](mailto:martin@martinthomas.net))

## Overview 

Each web framework has it\'s stregnths and weaknesses. The collaborative nature of Wiki\'s and the minimal change management provided is essential to organizing the convention. The power of Zope to provide long term change management of conference materials and media is essential. The ability to rapidly develop complex data driven applications with Django has proven invaluable.

How do we get these four drasticly different frameworks to behave together?

Django seems to be unlikely solution.

- Django can be seen as a toolkit in which features can be used independently to glue the rest of the world together.
- Django can access any other python module including Zope modules, Zope DB, and even PHP templates.
- Django can be used to generate php files, or it can use php output as its template input.

The current Django applications written for the convention are integrated into the site using such features.

## Draft Agenda 

We only have 45min so we need to be focused.

- Introductions

- Briefly cover existing applications (\<20 min)

  - PMWiki
  - Zope talks DB w/media
  - roomy (schedule and time table)
  - survey system
  - google map
  - django db layout (live admin interface)

- How django integrates into the site (\<10 min)

  - custom php template loader
  - custom context processor
  - cross app communication
  - potential Zope connection

- The big picture
  - what problems are we trying to solve?
  - what tools best solve those problems?

- Where do we go from here?

------------------------------------------------------------------------

[CategoryPyCon2006](CategoryPyCon2006)
