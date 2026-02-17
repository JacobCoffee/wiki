# MacPython/Growl/Terminology

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

*([GrowlHelperApp](./GrowlHelperApp.html).app terminology, generated from /Library/PreferencePanes/Growl.prefPane/Contents/Resources/GrowlHelperApp.app)*

::: {}
  -------------- -----------------------------------------------------------------------------------------------------------------------------------------
  **Suites**     [Growl](./MacPython(2f)Growl(2f)Terminology.html#suite_Growl)
  **Commands**   [notify](./MacPython(2f)Growl(2f)Terminology.html#command_notify) [register](./MacPython(2f)Growl(2f)Terminology.html#command_register)
  **Classes**    [Image](./MacPython(2f)Growl(2f)Terminology.html#class_Image) [Picture](./MacPython(2f)Growl(2f)Terminology.html#class_Picture)
  -------------- -----------------------------------------------------------------------------------------------------------------------------------------
:::

## Growl 

[AppleScript](./AppleScript.html) for the Growl Notification System

### Commands 

- **application.notify(\...)** \-- Post a notification to be displayed via Growl\

  - **with_name**=*Text* \-- name of the notification to display\
    **title**=*Text* \-- title of the notification to display\
    **description**=*Text* \-- full text of the notification to display\
    **application_name**=*Text* \-- name of the application posting the notification.\
    \[**image_from_location**=*[InsertionLoc](./InsertionLoc.html)*\] \-- Location of the image file to use for this notification. Accepts aliases, paths and [file:///](file:///) URLs.\
    \[**icon_of_file**=*[InsertionLoc](./InsertionLoc.html)*\] \-- Location of the file whose icon should be used as the image for this notification. Accepts aliases, paths and [file:///](file:///) URLs. e.g. \'[file:///Applications\'.\<\<BR\>\>](file:///Applications'.%3C%3CBR%3E%3E) \[**icon_of_application**=*Text*\] \-- Name of the application whose icon should be used for this notification. For example, \'Mail.app\'.\
    \[**image**=*k.Image*\] \-- TIFF Image to be used for the notification.\
    \[**pictImage**=*k.Picture*\] \-- PICT Image to be used for the notification.\
    \[**sticky**=*Boolean*\] \-- whether or not the notification displayed should time out. Defaults to \'no\'.\
    \[**priority**=*SInt32*\] \-- The priority of the notification, from -2 (low) to 0 (normal) to 2 (emergency).\
    Result: *None*

  **application.register(\...)** \-- Register an application with Growl\

  - **as_application**=*Text* \-- name of the application as which to register.\
    **all_notifications**=*list of Text* \-- list of all notifications to register.\
    **default_notifications**=*list of Text* \-- list of default notifications to register.\
    \[**icon_of_application**=*Text*\] \-- Name of the application whose icon should be used for this notification. For example, \'Mail.app\'.\
    Result: *None*

### Classes 

- **Picture**

  **Image**
