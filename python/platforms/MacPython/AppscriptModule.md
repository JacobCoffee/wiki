# MacPython/AppscriptModule

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# What is Appscript? 

Appscript is a high-level, user-friendly [MacPython](MacPython)-to-Apple Event Manager bridge that allows you to control scriptable Mac OS X applications using ordinary Python scripts. Appscript makes [MacPython](MacPython) a serious alternative to Apple\'s own [../AppleScript](./MacPython(2f)AppleScript.html) language for automating your Mac.

For example, to get the value of the first paragraph of the topmost document in [../TextEdit](./MacPython(2f)TextEdit.html):

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

- [../Audio Hijack Pro](./MacPython(2f)Audio(20)Hijack(20)Pro.html)

- [../Camino](./MacPython(2f)Camino.html)

- [../FileMakerPro](./MacPython(2f)FileMakerPro.html)

- [../Firefox](./MacPython(2f)Firefox.html)

- [../Growl](./MacPython(2f)Growl.html)

- [../Illustrator](./MacPython(2f)Illustrator.html)

- [../InDesign](./MacPython(2f)InDesign.html)

- [../iCal](./MacPython(2f)iCal.html)

- [../iPhoto](./MacPython(2f)iPhoto.html)

- [../iTerm](./MacPython(2f)iTerm.html)

- [../iTunes](./MacPython(2f)iTunes.html)

- [../iView MediaPro](./MacPython(2f)iView(20)MediaPro.html)

- [../Microsoft Powerpoint](./MacPython(2f)Microsoft(20)Powerpoint.html)

- [../Microsoft Word](./MacPython(2f)Microsoft(20)Word.html)

- [../OmniGraffle](./MacPython(2f)OmniGraffle.html)

- [../PhotoShop](./MacPython(2f)PhotoShop.html)

- [../QuarkXPress](./MacPython(2f)QuarkXPress.html)

- [../Safari](./MacPython(2f)Safari.html)

- [../SoundtrackPro](./MacPython(2f)SoundtrackPro.html)

- [../TextEdit](./MacPython(2f)TextEdit.html)

- [../VoodooPad](./MacPython(2f)VoodooPad.html)
