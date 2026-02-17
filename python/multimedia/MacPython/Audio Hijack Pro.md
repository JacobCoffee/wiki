# MacPython/Audio Hijack Pro

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

Print a formatted, plain text list of all scheduled timers with the dates and times for which they are scheduled. A description can be found [here](http://www.leancrew.com/all-this/2007/07/python_appscript_for_audio_hij.html)

:::: 
::: 
``` 
   1 #!/usr/bin/env python
   2 
   3 from appscript import *
   4 import datetime
   5 
   6 # Get a list of all the sessions.
   7 allsessions = app('Audio Hijack Pro').sessions.get()
   8 
   9 # Make a list with the sessions that have scheduled timers.
  10 timersessions = []
  11 for s in allsessions:
  12     for t in s.timers.get():
  13         if t.scheduled():
  14           timersessions.append(s)
  15           break # go to next session after finding a scheduled timer
  16 
  17 # Get the length of the longest name of a timersession.
  18 longest = max(len(s.name()) for s in timersessions)
  19 
  20 # Make a 7-character string with the days that the timer runs.
  21 def timerdays(t):
  22   daylist = ['-'] * 7
  23   if t.runs_Sunday():
  24     daylist[0] = 'S'
  25   if t.runs_Monday():
  26     daylist[1] = 'M'
  27   if t.runs_Tuesday():
  28     daylist[2] = 'T'
  29   if t.runs_Wednesday():
  30     daylist[3] = 'W'
  31   if t.runs_Thursday():
  32     daylist[4] = 'T'
  33   if t.runs_Friday():
  34     daylist[5] = 'F'
  35   if t.runs_Saturday():
  36     daylist[6] = 'S'
  37   return ''.join(daylist)
  38 
  39 # Print the info for all the sessions with enabled timers.
  40 for s in timersessions:
  41   for t in s.timers.get():
  42     if t.scheduled():
  43       dur = t.duration()
  44       durstr = '(%d min)' % (dur/60)
  45       st = t.start_time()
  46       et = st + datetime.timedelta(seconds = dur)
  47       dow = timerdays(t)
  48       ststr = st.strftime("%l:%M %p")
  49       etstr = et.strftime("%l:%M %p")
  50       fmtstr = "%" + str(longest) + "s: %s from %s to %s %s"
  51       print fmtstr % (s.name(), dow, ststr, etstr, durstr.rjust(9))
```
:::
::::
