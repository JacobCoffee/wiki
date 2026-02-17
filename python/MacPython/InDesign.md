# MacPython/InDesign

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

Only some snippets from a simple [InDesign](./InDesign.html) automator\...

     inD = app('Adobe InDesign CS2')
     inD.script_preferences.user_interaction_level = k.never_interact
     finder = app('Finder')
     doc = inD.open(mactypes.Alias(u'/Users/user/Documents/test.indd'))

     if doc.pages[page].side() == k.right_hand:
         print "page %d is on the righthand side" % page

How to place a text file and delete the first 2 lines:

     story = doc.place(macpath, on=doc.pages[page], showing_options=False)
     story.lines[1:2].delete()

Fix the size of the new text frame:

     rect = [76, 12, 284, 65]
     # left, top, height, width in default unit (e.g. mm)
     frame = story.text_frames[1].get()
     frame.geometric_bounds.set(rect)
     if frame.overflows():
         # too much text -> increase size
