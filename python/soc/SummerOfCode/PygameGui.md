# SummerOfCode/PygameGui

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# A Pygame GUI Toolkit. 

**On second thoughts, this sort of project probably isn\'t needed, for many different reasons.** - [SimonWittber](SimonWittber)

------------------------------------------------------------------------

Build a minimal object oriented GUI toolkit, aimed at use with touchscreens, which uses pygame for display. It should use something like a command dispatch pattern, and make sure to take advantage of the late binding abilities of python.

The minimum widgets needed are:

- Labels
- Tool Tips
- Text Entry (with possible optional virtual keyboard)
- Buttons
- Heirarchial Pie Menu System
- Spacer
- Dialogs with Customisable buttons

It should also provide customisable layout managers for widget layout. Grid, Horizontal and Vertical Row etc.

------------------------------------------------------------------------

## Some reasons why this proposal isn\'t needed: 

- PGU is good enough for most people who want a Pygame GUI.
- Most games / multimedia applications use custom GUI code.
- IMO, the only part of a GUI toolkit which can be successfully genericised for these sorts of applications is the event loop and dispatch mechanism.
