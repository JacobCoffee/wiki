# MacPython/Growl/AppleScriptSupport

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

Translated examples from Growl\'s [AppleScript](./MacPython(2f)AppleScript.html) Support page:

- **Basics**

  - :::: 
    ::: 
    ``` 
       1 #!/usr/bin/pythonw
       2 from appscript import *
       3 
       4 # connect to Growl
       5 growl = app('GrowlHelperApp')
       6 
       7 # Make a list of all the notification types 
       8 # that this script will ever send:
       9 allNotificationsList = ['Test Notification', 'Another Test Notification']
      10 
      11 # Make a list of the notifications 
      12 # that will be enabled by default.      
      13 # Those not enabled by default can be enabled later 
      14 # in the 'Applications' tab of the growl prefpane.
      15 enabledNotificationsList = ['Test Notification']
      16 
      17 # Register our script with growl.
      18 # You can optionally (as here) set a default icon 
      19 # for this script's notifications.
      20 growl.register(
      21     as_application='Growl Appscript Sample', 
      22     all_notifications=allNotificationsList, 
      23     default_notifications=enabledNotificationsList, 
      24     icon_of_application='PythonIDE')
      25 
      26 # Send a Notification...
      27 growl.notify(
      28     with_name='Test Notification', 
      29     title='Test Notification', 
      30     description='This is a test Appscript notification.', 
      31     application_name='Growl Appscript Sample')
      32 
      33 # Another one...
      34 growl.notify(
      35     with_name='Another Test Notification', 
      36     title='Another Test Notification :) ', 
      37     description='Alas - you won\'t see me until you enable me...', 
      38     application_name='Growl Appscript Sample')
    ```
    :::
    ::::

- **Notifications using Images**

  - Application Icons
    - :::: 
      ::: 
      ``` 
         1 growl.notify( 
         2     with_name="Some Notification",
         3     title="This is a Notification with an App Icon",
         4     description="We are using an Application Icon...",
         5     application_name="Growl /AppleScript Sample",
         6     icon_of_application="Script Editor.app")
      ```
      :::
      ::::
  - File Icons
    - :::: 
      ::: 
      ``` 
         1 growl.notify(
         2     with_name="Some Notification",
         3     title="This is a Notification with an File Icon",
         4     description="We are using a File's Icon...",
         5     application_name="Growl /AppleScript Sample",
         6     icon_of_file="file:///Users/someone/Growl")
      ```
      :::
      ::::
  - Image Files
    - :::: 
      ::: 
      ``` 
         1 growl.notify(
         2     with_name "Some Notification",
         3     title="This is a Notification with an Image File",
         4     description="We are using an Image File...",
         5     application_name="Growl /AppleScript Sample",
         6     image_from_location="file:///Users/someone/pictures/stopWatch.png")
      ```
      :::
      ::::
  - Image Data
    - *(not done yet\...)*
