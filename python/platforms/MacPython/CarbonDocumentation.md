# MacPython/CarbonDocumentation

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# General Tips 

Try some or all:

- Read Apple Carbon documentation

- Use `dir()`{.backtick} and `help()`{.backtick}

- Look into [MacPython](MacPython) IDE code, or in the few Mac Python modules like `macostools`{.backtick}, `findertools`{.backtick} or other modules in `plat-mac`{.backtick}

- Look into the C modules that implement the glue between Python and Carbon.

- Ask the good people at `#macpython`{.backtick} in `irc.freenode.org`{.backtick}

# Recipes 

## Getting file and folder information 

You want to know the file type or creator of a file.

    >>> from Carbon import File
    >>> info = File.FSSpec('Todo').FSpGetFInfo()     
    >>> info.Type
    '****'
    >>> info.Creator
    'Hdra'
    >>> 

Note that FSSpecs have some issues, see [http://developer.apple.com/technotes/tn2002/tn2078.html](http://developer.apple.com/technotes/tn2002/tn2078.html)

Here is another simpler way (from [MacPython](MacPython) IDE):

    >>>import MacOS
    >>> MacOS.GetCreatorAndType('Todo')
    ('Hdra', '****')

# Carbon Reference 

Python 2.3 Carbon Modules:

- [../AE](./MacPython(2f)AE.html)

- [../AH](./MacPython(2f)AH.html)

- [../Aliases](./MacPython(2f)Aliases.html)

- [../App](./MacPython(2f)App.html)

- [../Appearance](./MacPython(2f)Appearance.html)

- [../AppleEvents](AppleEvents)

- [../AppleHelp](./MacPython(2f)AppleHelp.html)

- [../CF](./MacPython(2f)CF.html)

- [../CG](./MacPython(2f)CG.html)

- [../CarbonEvents](./MacPython(2f)CarbonEvents.html)

- [../CarbonEvt](./MacPython(2f)CarbonEvt.html)

- [../Cm](./MacPython(2f)Cm.html)

- [../Components](./MacPython(2f)Components.html)

- [../ControlAccessor](./MacPython(2f)ControlAccessor.html)

- [../Controls](./MacPython(2f)Controls.html)

- [../CoreFoundation](./MacPython(2f)CoreFoundation.html)

- [../CoreGraphics](./MacPython(2f)CoreGraphics.html)

- [../Ctl](./MacPython(2f)Ctl.html)

- [../Dialogs](./MacPython(2f)Dialogs.html)

- [../Dlg](./MacPython(2f)Dlg.html)

- [../Drag](./MacPython(2f)Drag.html)

- [../Dragconst](./MacPython(2f)Dragconst.html)

- [../Events](./MacPython(2f)Events.html)

- [../Evt](./MacPython(2f)Evt.html)

- [../File](./MacPython(2f)File.html)

- [../Files](./MacPython(2f)Files.html)

- [../Fm](./MacPython(2f)Fm.html)

- [../Folder](./MacPython(2f)Folder.html)

- [../Folders](./MacPython(2f)Folders.html)

- [../Fonts](./MacPython(2f)Fonts.html)

- [../Help](./MacPython(2f)Help.html)

- [../IBCarbon](./MacPython(2f)IBCarbon.html)

- [../IBCarbonRuntime](./MacPython(2f)IBCarbonRuntime.html)

- [../Icn](./MacPython(2f)Icn.html)

- [../Icons](./MacPython(2f)Icons.html)

- [../List](./MacPython(2f)List.html)

- [../Lists](./MacPython(2f)Lists.html)

- [../MacHelp](./MacPython(2f)MacHelp.html)

- [../MacTextEditor](./MacPython(2f)MacTextEditor.html)

- [../MediaDescr](./MacPython(2f)MediaDescr.html)

- [../Menu](./MacPython(2f)Menu.html)

- [../Menus](./MacPython(2f)Menus.html)

- [../Mlte](./MacPython(2f)Mlte.html)

- [../QDOffscreen](./MacPython(2f)QDOffscreen.html)

- [../Qd](./MacPython(2f)Qd.html)

- [../Qdoffs](./MacPython(2f)Qdoffs.html)

- [../Qt](./MacPython(2f)Qt.html)

- [../QuickDraw](./MacPython(2f)QuickDraw.html)

- [../QuickTime](./MacPython(2f)QuickTime.html)

- [../Res](./MacPython(2f)Res.html)

- [../Resources](./MacPython(2f)Resources.html)

- [../Scrap](./MacPython(2f)Scrap.html)

- [../Snd](./MacPython(2f)Snd.html)

- [../Sound](./MacPython(2f)Sound.html)

- [../TE](./MacPython(2f)TE.html)

- [../TextEdit](TextEdit)

- [../WASTEconst](./MacPython(2f)WASTEconst.html)

- [../Win](./MacPython(2f)Win.html)

- [../Windows](./MacPython(2f)Windows.html)
