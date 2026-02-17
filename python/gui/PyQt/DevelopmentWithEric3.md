# PyQt/DevelopmentWithEric3

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

Add your tips on eric3 here!

------------------------------------------------------------------------

This is a little tutorial that is a bit outdated (the sample source has to be changed in some points, but I don\'t remember them, sorry): [http://www.pycs.net/lateral/stories/16.html](http://www.pycs.net/lateral/stories/16.html)

------------------------------------------------------------------------

OK, here is the 5-minute introduction. I\'ve just installed eric3 and pyQt on debian; the command

      apt-get install eric eric-api-files pyqt-tools

will do the trick.

On Ubuntu, \"apt-get install eric\" is sufficient. Just to be sure, you can try

      apt-get install eric python-kde3 qt3-assistant qt3-designer qt3-linguist qt3-doc pyqt-tools python-xml

which will install eric and all the optional packages that it requires.

Then, a very important thing to do is to set up QTDIR correctly in Settings-\>Preferences-\>Qt or else a lot of problems will crop out later. I\'ve mine set to /usr/share/qt3

Restart eric and everything (hopefully) will work as explained below\...

## Create_Project 

First, select **Project-\>New** to create a new project. Name it \'Hello\', ensure that the **UI Type is QT**, and press **OK**.

## Create_Dialog 

Run Qt Designer (**Extras-\>Tools-\>Designer**) and create a new form using **File-\>New\...** and selecting **Dialog** from the wizard.

Set the name of the dialog form **hello_form** and change the caption to \'hello\' (or whatever). Add a **[PushButton](./PushButton.html)** to the form and the change the text to \'Close\' (or, again, whatever).

Hit **F3** or the **Connect Signals/Slots** button. Create a connection from the **[PushButton](./PushButton.html) pressed** signal to the **hello_form \'close()\' slot**.

Save the form as **hello_form.ui** and exit Qt designer.

## Add Dialog To Project 

The project Browser is the tabbed or notebook widget in on the upper left of the Eric3 IDE. It has a tab with a snake, a (drawing) compass, a fish, a piece of paper saying IDL, and a blank piece of paper; these represent the project Sources, Forms, Translations, Interfaces, and Others.

Go to the Forms tab in the Project Browser. **Right-click on the tab** to get the Forms context menu ; **select \'New Form\', then \'Dialog\'** . When the file dialog comes up, select \'hello_form.ui\' and press OK.

The \'hello_form.ui\' file will appear in the Forms tab. **Right-click on it and select \'Compile Form\'** . This will create \'hello_form.py\' and add it to the Sources tab in the Project Browser.

## Generate Subclass For Form 

**Right-click on \'hello_form.ui\'** in the Forms tab of the Project Browser and **choose \'Generate Subclass\'** . When prompted for a name, enter \'hello_form_impl\'.

This will open an untitled python script window with the subclass implementation in it. **Save the script as \'hello_form_impl.py\'** .

Go to the Sources tab of the Project Browser and right-click on the background. **Choose \'Add source file\...\' and select \'hello_form_impl.py\'** in the file dialog, then press OK.

## Create A Main Script 

Open a new python script. Enter the following code:

:::: 
::: 
``` 
   1 #!/usr/bin/env python
   2 
   3 import sys
   4 from qt import *
   5 from hello_form_impl import hello_form_Impl
   6 
   7 # create Qt application
   8 app = QApplication(sys.argv)
   9 
  10 # create and show Qt form
  11 form = hello_form_Impl()
  12 form.show()
  13 
  14 # enter Qt event-handling loop
  15 app.exec_loop()
```
:::
::::

Save the script as \'hello_main.py\'

Go to Project-\>Properties

Set the \'Main script\' property to \'hello_main.py\' and press OK; this will add \'hello_main.py\' to the Sources tab of the Project Browser.

## Wrapping It Up 

Use **Debug-\>Run Project** to run the scripts and show the dialog.
