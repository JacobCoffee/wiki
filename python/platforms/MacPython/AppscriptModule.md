# MacPython/AppscriptModule

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# What is Appscript? 

Appscript is a high-level, user-friendly [MacPython](MacPython)-to-Apple Event Manager bridge that allows you to control scriptable Mac OS X applications using ordinary Python scripts. Appscript makes [MacPython](MacPython) a serious alternative to Apple\'s own [../AppleScript](AppleScript) language for automating your Mac.

For example, to get the value of the first paragraph of the topmost document in [../TextEdit](TextEdit):

    app('TextEdit').documents[1].paragraphs[1].get()

This is equivalent to the [/AppleScript](./MacPython(2f)AppscriptModule(2f)AppleScript.html) statement:

    get paragraph 1 of document 1 of application "TextEdit"

Appscript builds upon lower-level Python packages (aem, osaterminology) to provide:

1.  an Apple event-based *RPC mechanism* for sending commands to applications

2.  a mechanism for converting data between common Python and Apple event types

3.  a simple *embedded query language* for constructing references to an application\'s object model

4.  a mechanism that uses application-defined terminology to present these references in human-readable form

5.  an integrated help system for exploring application terminology information

6.  a clean, *object oriented-like syntax* for ease of use.

See:

- [http://appscript.sourceforge.net/](http://appscript.sourceforge.net/)

# Application scripting notes 

Pages containing additional information on scripting individual applications:

- [../Apple Mail](./MacPython(2f)Apple(20)Mail.html)

- [../Audio Hijack Pro](../../multimedia/MacPython/Audio Hijack Pro)

- [../Camino](Camino)

- [../FileMakerPro](FileMakerPro)

- [../Firefox](Firefox)

- [../Growl](Growl)

- [../Illustrator](./MacPython(2f)Illustrator.html)

- [../InDesign](InDesign)

- [../iCal](iCal)

- [../iPhoto](iPhoto)

- [../iTerm](iTerm)

- [../iTunes](iTunes)

- [../iView MediaPro](./MacPython(2f)iView(20)MediaPro.html)

- [../Microsoft Powerpoint](Microsoft Powerpoint)

- [../Microsoft Word](Microsoft Word)

- [../OmniGraffle](OmniGraffle)

- [../PhotoShop](PhotoShop)

- [../QuarkXPress](QuarkXPress)

- [../Safari](Safari)

- [../SoundtrackPro](SoundtrackPro)

- [../TextEdit](TextEdit)

- [../VoodooPad](VoodooPad)
