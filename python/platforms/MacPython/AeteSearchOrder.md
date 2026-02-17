# MacPython/AeteSearchOrder

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

(These are by watching `AEDebugSends` and `AEDebugReceives` and looking at ktrace output of osacompile)

iTunes

- Reads `Info.plist` (probably sees `NSAppleScriptEnabled = True`)

- Reads `Resources/iTunes.rsrc`

- Reads `Resources/English.lproj/Localized.rsrc`

Finder

- Reads `Info.plist` (probably sees `NSAppleScriptEnabled = True`)

- Reads `Resources/Finder.rsrc`

- Reads `Resources/English.lproj/Localized.rsrc`

Mail

- Reads `Info.plist` (probably sees `NSAppleScriptEnabled = True`)

- Reads `Resources/Mail.rsrc`

- Finds nothing in `Resources/English.lproj`

iChat

- Reads `Info.plist` (probably sees `NSAppleScriptEnabled = True`)

- Looks in `Resources` and `English.lproj`, finds nothing

- Looks in the iChat executable and its resource fork, finds nothing

- ascr/gdte, answers with aete

Terminal

- Reads `Info.plist` (probably sees `NSAppleScriptEnabled = True`)

- Reads `Resources/Terminal.rsrc`

- Finds nothing in `Resources/English.lproj`
