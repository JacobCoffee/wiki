# PythonEventsCalendar

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# Python Events Calendar 

## Introduction 

The *Python events calendar* is a combination of Google calendars maintained by the Python Calendar Team and published on the following sites:

- [http://www.python.org/](http://www.python.org/) (in the events box on the front page and on the [events calendar](https://www.python.org/events/) pages)

- [http://www.pycon.org/](http://www.pycon.org/) (calendar widget under the conference listing)

- [https://twitter.com/PythonEvents](https://twitter.com/PythonEvents) (@[PythonEvents](PythonEvents))

- [http://legacy.python.org/](http://legacy.python.org/) (in the side bar on the left of all pages)

As of January 2020, we have more then 520 events listed and the calendars are proving to be a really useful resource for the Python community.

The events are also listed on a map mashup created by Luis Miguel Morillas:

- [http://lmorillas.github.io/python_events/](http://lmorillas.github.io/python_events/)

Here\'s a snapshot showing all events from Jan 2012 - March 2016:

![width=200](attachments/PythonEventsCalendar/Python-Events-Jan-2012-March-2016.jpg "width=200")

------------------------------------------------------------------------

------------------------------------------------------------------------

## Submitting an Event 

If you would like to get new events listed on these calendars, please write to [events@python.org](mailto:events@python.org) using the following email template:

    Please add the following event:

     * name of the event: 
     * type of event: 
     * focus on Python: 
     * approximate number of attendees: 
     * location (incl. country): 
     * dates/times/recurrence (incl. time zone): 
     * HTML link using the format <a href="http://url/">name of the event</a>: 

Please mention:

- the name of the event (including the user group name for user group events)

- type of event (conference, bar camp, sprint, user group meeting, etc.)

- focus on Python and approximate size (number of attendees)

- the location (venue address, including city and *country*)

- the dates/times (including the time zone)

- a link with more details for the event (using HTML format \"`<a href="http://url/">name of the event</a>`\"); URL shorteners are *not permitted*.

For recurring events, please also include the recurrence information, e.g. \"monthly, every second Thursday\".

*Notes:*

- For online events, please use \"Online Event\" as location.

- For *training sessions, courses, webinars and similar type of events*, please post your event on the [PythonTraining](PythonTraining) page. We currently do not have a calendar for these.

- ![/!\\](/wiki/europython/img/alert.png "/!\") **Please leave at least 4 weeks notice** when submitting events. The calendar team is volunteer driven. While we try to add new events swiftly, we cannot guarantee response times.

## Bulk Submission of Events 

In some cases, the email format may not be suitable, e.g. if you want to submit several larger events in one go. For those cases, please list the events in the email sent to [events@python.org](mailto:events@python.org), including the following details:

- the name of the event (including the user group name for user group events)
- type of event (conference, bar camp, sprint, user group meeting, etc.)
- focus on Python and approximate size (number of attendees)
- optional: a link with more details for the event

for each event, or as summary, so that we can tell which type of event you want entered and whether they are suitable for our calendars.

Please attach the event data as iCal file `events.ics` using the following entry format:

- *title:* `name of the event`

- *start and end dates:* start day and end day of the event, entered as \"all day events\" for larger events, or as start and end date and time in the local timezone for smaller single day events

- *location:* `city, [state,] country`

- *description:* `<a href="http://url/">name of the event</a>`

The same notes as above apply to bulk submissions.

## Available Calendars 

- [Python Events Calendar](https://www.google.com/calendar/embed?src=j7gov1cmnqr9tvg14k621j7t5c@group.calendar.google.com&ctz=Europe/London) - mostly meant for conferences and larger local events Calendar ID: [j7gov1cmnqr9tvg14k621j7t5c@group.calendar.google.com](mailto:j7gov1cmnqr9tvg14k621j7t5c@group.calendar.google.com)

- [Python User Group Calendar](https://www.google.com/calendar/embed?src=3haig2m9msslkpf2tn1h56nn9g@group.calendar.google.com&ctz=Europe/London) - meant for user group events and other smaller local events Calendar ID: [3haig2m9msslkpf2tn1h56nn9g@group.calendar.google.com](mailto:3haig2m9msslkpf2tn1h56nn9g@group.calendar.google.com)

- [Both calendars combined](https://www.google.com/calendar/htmlembed?showTitle=0&showCalendars=0&height=600&wkst=2&bgcolor=%23FFFFFF&src=j7gov1cmnqr9tvg14k621j7t5c%40group.calendar.google.com&color=%23125A12&src=3haig2m9msslkpf2tn1h56nn9g%40group.calendar.google.com&color=%232F6309&ctz=GMT) - in a single calendar widget

## iCal Downloads 

- [Python Events Calendar](https://www.google.com/calendar/ical/j7gov1cmnqr9tvg14k621j7t5c@group.calendar.google.com/public/basic.ics)

- [Python User Group Calendar](https://www.google.com/calendar/ical/3haig2m9msslkpf2tn1h56nn9g@group.calendar.google.com/public/basic.ics)

## RSS Feeds 

*Note: Google has [switched off calendar RSS feeds](https://support.google.com/calendar/answer/6285065?p=xml_deprecation&rd=1) on Nov 18 2015, so these links no longer work.*

- [Python Events Calendar](https://www.google.com/calendar/feeds/j7gov1cmnqr9tvg14k621j7t5c@group.calendar.google.com/public/basic?orderby=starttime&sortorder=ascending&futureevents=true)

- [Python User Group Calendar](https://www.google.com/calendar/feeds/3haig2m9msslkpf2tn1h56nn9g@group.calendar.google.com/public/basic?orderby=starttime&sortorder=ascending&futureevents=true)

## Twitter Feed 

- [\@PythonEvents](https://twitter.com/PythonEvents)

  This Twitter account automatically gets all new entries from both calendars as tweets. The triggering is setup using [IFTTT](https://ifttt.com/). Note that changes to the calendar entries are not reported on the Twitter feed. This appears to be a limitation of the IFTTT trigger.

## Embedding Calendars 

If you\'d like to embed the calendar into your site, please ping us at [events@python.org](mailto:events@python.org) before doing so. We\'d like to keep a list of sites where the calendars are displayed.

You can find the embedding code further below on this page.

### Known sites embedding the calendars 

- [https://www.python.org/](https://www.python.org/) (in the events box on the front page and on the [events calendar](https://www.python.org/events/) pages)

- [http://www.pycon.org/](http://www.pycon.org/) (calendar widget under the conference listing)

- [http://legacy.python.org/](http://legacy.python.org/) (in the side bar on the left of all pages)

- [https://pythonz.net/events](https://pythonz.net/events) (a Russian site)

## Python Calendar Team 

The following people are team members with admin rights to the calendars:

- Marc-Andre Lemburg

These are our team members with editing rights:

- Helio Loureiro
- Abdur-Rahmaan Janhangeer
- Olivia Sauls

If you want to join the team, please sign up to the python-events ML and send a short intro about yourself together with a Google compatible email address to the list. Thanks.

The following people are inactive team members:

- Mayank Pathak
- Giri Prasath Dinakaran
- Sergey Sokolov
- Anton Caceres
- Marcelo Elizeche Landó
- Richard Jones
- Mike Müller
- Tarek Ziade
- Tetsuya Morimoto
- Skip Montanaro
- Tim Golden
- Mats Wichmann
- Laura Creighton
- Carol Willing
- Oier Etxaniz

### Mailing List 

The team uses the python-events mailing list for discussion and to process events. The [events@python.org](mailto:events@python.org) address is an alias for the python-events mailing list.

- [https://mail.python.org/mailman/listinfo/python-events](https://mail.python.org/mailman/listinfo/python-events)

![/!\\](/wiki/europython/img/alert.png "/!\") As team member, it is vital for you to subscribe to this list, otherwise you won\'t get the incoming event notifications.

### Guidelines for entries 

In order to make the decision of whether to add an event and where to add it easier, we\'ve setup a few guidelines:

#### General Requirements 

- Events have to have some focus on Python: The event should either target Python, a project written in Python, or showcase Python in some form.

  Examples are Python conferences, conferences which have a Python track or tutorial, conferences at which Python is presented in some form. The same goes for conferences which target a project written mostly in Python (e.g. Plone, Django, [OpenStack](./OpenStack.html), etc.) and for other events such as sprints.

- The calendars should only list the events themselves. CFP deadlines, registration openings or similar announcements should not be listed in the calendars.

- For online events, such as [PyWeek](PyWeek) game jams, only a reasonably short events (no longer than two weeks) should be added as single event. For longer events, it\'s better to just add the start and end date as separate events to the calendar, or even just the start date and then mention the end in the description. The same criteria for calendars apply to online events as well. Please add these using `Online` or `Online Event` as location. For hybrid events (both in-person and virtual), mentioning `and Online` after the in-person location is possible as well.

- Training events, conferences which don\'t have a strong Python focus or offer a decent sized Python track, should not be listed on the calendars.

#### Calendar Choice 

- Python Events Calendar: This calendar should only receive entries for conferences of at least around 100 attendees, which at least around a 3rd non-local attendees. Smaller events with at least around 30 attendees such as sprints, barcamps, [PyDays](./PyDays.html) or smaller unconferences may also be added to this calendar if they are scheduled as separate event, will have a significant impact and reach out to larger regions. Examples: [PyCon](PyCon) conferences, OSCON, Django conferences, Plone conference, Need-for-speed sprints, Python BarCamps/Unconferences/etc.

- Python User Group Calendar: This calendar is meant for user group activities which are open to Python people from outside the group (new prospective members and visitors from out of town). It is not meant for user group internal events. Examples: monthly local user group meetings, project sprints that are open for non-group members, workshops organized by user groups, Django Girls events.

#### Notes regarding calendar entries 

Some notes regarding entries for the admins:

- Please add the conference/event year to the title, if available. For user group meetings or other events that occur more often that\'s probably not necessary.

- For conference events please use \"All day\" entries (even for one day events), for user group events please add the start time and end time, if known. Full day user group events can also be added as \"All day\" event to give them a little more attention in the calendar. We use this for e.g. Django Girls workshops or similar full day events.

- Please include the location as \"City, Country\", not with the full address, since this can often be inaccurate and confused the Google maps mashup. For online events, please use \"Online\" or \"Online from City, Country\" (not sure whether this will work with mapping tool, but worth a try).

- Please add a link to the event as description. We have standardized on using HTML links for this, e.g. `<a href="http://www.pycon.fr/2012/>PyCon FR 2012</a>`. Note that the Google calendar UI was changed some time ago to no longer accept HTML as input. Instead, you have to paste the HTML link directly into the description box. Calendar interfaces using iCal typically require adding the full HTML.

- Please test the provided link and make sure that it\'s not a URL shortener URL or one which redirects to an unrelated website. We have had situations where the added events later linked to unrelated or spam pages.

- For familiar sounding event names, please check whether the requests are genuine. In case of naming collisions, try to get the organizers to talk to each other and sort out the issue.

- Please don\'t add more than the link to the description. If an event does not have a website, it\'s fine to add a one line text description. Background: The entries should not be used as advertisement text for events, only as reference.

- Please don\'t select an event color. People who subscribe to the calendars will have their own color preferences, so it\'s better to leave the default color set for all events.

- Reminders should not be setup for the events. They can be annoying for users subscribing to the calendars.

- We\'ve always used \"Show me as: Available\" for new entries. No idea whether that matters or not.

- Please select \"Privacy: Default\" for new entries. This makes the entries public, since that\'s the default setting.

All calendar admins can invite more people as calendar admins. When doing so, please add the new admins to the above list and ping the team by writing to [events@python.org](mailto:events@python.org) and also to get their email address added to the python-events mailing list.

### Calendar embedding code 

This iframe code is used on pycon.org to display the calendar:

- <iframe src="https://www.google.com/calendar/embed?showTitle=0&amp;showCalendars=0&amp;height=400&amp;wkst=2&amp;bgcolor=%23FFFFFF&amp;src=j7gov1cmnqr9tvg14k621j7t5c%40group.calendar.google.com&amp;color=%23125A12&amp;src=3haig2m9msslkpf2tn1h56nn9g%40group.calendar.google.com&amp;color=%232F6309&amp;ctz=Europe%2FLondon" style=" border-width:0 " width="800" height="450" frameborder="0" scrolling="no">
        <a href="https://www.google.com/calendar/ical/j7gov1cmnqr9tvg14k621j7t5c%40group.calendar.google.com/public/basic.ics">Python Events iCal Calendar</a><br/>
        <a href="https://www.google.com/calendar/ical/3haig2m9msslkpf2tn1h56nn9g%40group.calendar.google.com/public/basic.ics">Python User Group iCal Calendar</a>
      </iframe>

### Resources 

- [Google Calendar API v2 Atom Reference](https://developers.google.com/google-apps/calendar/v2/reference). This describes the available RSS feed options available on the Google calendar feed links.
