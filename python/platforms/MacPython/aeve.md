# MacPython/aeve

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

#pragma section-numbers off

# aeve

aeve is a near-complete rewrite of the Apple Event support (gensuitemodule, etc.) for Python. It\'s extremely pythonic and easy to use, but it\'s chattier than doing it \"raw\" and currently does not support any kind of asynchronous mode. This is normally not an issue, but I\'m looking into adding that sort of stuff. The version posted below is a work in progress, your mileage may vary. I\'d like to hear from you if you do anything with it, especially if you have any contributions (bugfixes, example code, etc.), problems or suggestions. Note that it\'s only going to work in Python 2.3 or later.

# status

aeve is currently at its fourth public release, 0.0.3.

# examples

## iChat + Jaguar Mail 

:::: 
::: 
``` 
   1 """
   2 I get an inordinate amount of spam to one of my accounts,
   3 and they get put into spam-definite on my imap server.
   4 The spam-definite mailbox gets flushed on a daily basis to train
   5 spamassasin.
   6 This script changes my status message on iChat to the number of
   7 spams in this mailbox every five minutes.
   8 """
   9 import time
  10 import aeve
  11 i = aeve.talkto('com.apple.iChat')
  12 m = aeve.talkto('com.apple.Mail')
  13 spam = m.rules['Junk'].transfer_message.messages
  14 while True:
  15     i.status_message = '%d spams today' % len(spam)
  16     time.sleep(300.0)
```
:::
::::

## iCal 

:::: 
::: 
``` 
   1 """
   2 This is an example of how to do the make command from aeve to create a new calendar.
   3 It's unfortunately hard at the moment.
   4  
   5 Translated from:
   6 tell application "iCal"
   7     make calendar with properties {title:"newCalendar"}
   8 end tell
   9 """
  10 import aeve
  11 app = aeve.talkto('com.apple.iCal')
  12 from aeve.Applications import iCal
  13 # we have to do this ourselves, aeve doesn't understand property dictionaries
  14 title_code = iCal.iCal_suite._aereg_.iterObjectsForName("title", aekind="property", deep=True).next()
  15 newCalendar = app.make(new=iCal.calendar, with_properties={title_code:"newCalendar"})
```
:::
::::

# homepage

[http://undefined.org/python/#aeve](http://undefined.org/python/#aeve)

# known issues 

Not compatible with:

- Panther mail
- Xcode

Hard to do:

- the make command (with_properties, specifically)

# see also 

- [../AppleScript](./MacPython(2f)AppleScript.html)

- [../AppleScriptNotes](./MacPython(2f)AppleScriptNotes.html)

- [../AeveNewbieDiscussion](./MacPython(2f)AeveNewbieDiscussion.html)
