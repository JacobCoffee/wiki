# JonathanGardnerPyQtTutorial

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# Jonathan Gardner\'s PyQt Tutorial 

This is a short tutorial to get you up to speed with [PyQt](PyQt). It assumes some knowledge of bash, Python, and Qt.

If you have questions or comments, you can send them to me at [jgardner@jonathangardner.net](mailto:jgardner@jonathangardner.net). You may also make corrections to this page.

A (brazilian) portuguese translation is available at [https://web.archive.org/web/20081017155041/http://www.pythonbrasil.com.br/moin.cgi/TutorialPyQt](https://web.archive.org/web/20081017155041/http://www.pythonbrasil.com.br/moin.cgi/TutorialPyQt) thanks to Rodrigo B. Vieira.

## Abstract 

We will cover:

- Using Qt Designer to generate Qt ui files.
- Using pyuic to generate python programs.
- Using Qt Signals and Slots in Python.
- Creating a simple application to interface with the \'at\' program.

## Requirements 

You will need:

- Red Hat 8.0 with the following configuration:

- qt-devel RPM properly installed

- [PyQt](PyQt)-devel RPM properly installed

[PyQt](PyQt) works on other systems. This tutorial may or may not work as well. However, I cannot provide all the details on how to get them to work on all the systems that can use [PyQt](PyQt). You are responsible for figuring that out.

You should already know:

- How to use a text editor, and how to get that text editor to edit Python code properly.
- How to program in Python.
- Some basic bash commands.
- The basics of Qt programming.

If you haven\'t fulfilled these requirements, you may have some trouble getting the tutorial to work.

## Using Qt Designer 

First things first. We\'ll start where I start. Open up a bash prompt. Start Qt Designer by typing the following command:

- $ designer

You are presented with Qt designer. Depending on which version you are running, it may appear slightly different.

I won\'t assume you are totally inept at using Qt Designer. If you are, you can easily read the documentation.

Create a new widget. Name it \'at_auto\'. Add some stuff to it:

- Add a QLineEdit. Name it \"command\" in the property dialog.

- Add a QPushButton. Name it \"schedule\" in the property dialog. Change its text to \"Schedule\".

- Add a QDateTimeEdit. Name it \"time\" in the property dialog.

Now, rearrange the layout using the Qt layout tools to your heart\'s content. You may need to use some spacers as well.

Save the file in a project directory for this tutorial. If you haven\'t already created one, create one called \"pyqt_tutorial\" or something. Save the file as \"at.ui\".

## Using pyuic 

Go back to your bash prompt, or open up a new one. Go into the project directory, and run these commands.

- $ pyuic at.ui

This command will store the generated python code that comes from the Qt ui file into at_auto.py.

- $ pyuic at.ui -o at_auto.py

Everytime we change the ui file, we need to regenerate the at_auto.py file. Let\'s add this command to a makefile.

![/!\\](/wiki/europython/img/alert.png "/!\") Tabs are important!

- $ cat > Makefile
      at_auto.py : at.ui
              pyuic at.ui -o at_auto.py
      ^D

------------------------------------------------------------------------

Now run the makefile.

- $ make

Notice that it says something about all the files being up to date. Let\'s touch at.ui so it appears newer than at_auto.py, and then run make again.

- $ touch at.ui
      $ make

Now it echos out the commands it runs. You see that it has successfully regenerated at_auto.py.

### Theory 

The idea here is that you want the GUI developer to be able to go and make changes to the GUI interface (like moving stuff around) without affecting the logic behind the GUI. So with your setup right now, all the GUI developer has to do is use Qt Designer to change the at.ui file, and then run make to see his changed take effect.

Your make file will get more complicated as you add more files. Be sure to read more about make so that you make good design decisions early on about how to use make properly.

## Running Your Application 

So we have that at.ui file, and the at_auto.py file. How do we actually run the app?

We have to create at.py. Here is what it will look like.

- from qt import *
      from at_auto import at_auto

      class at(at_auto):
          def __init__(self, parent=None, name=None, fl=0):
              at_auto.__init__(self,parent,name,fl)

      if __name__ == "__main__":
          import sys
          a = QApplication(sys.argv)
          QObject.connect(a,SIGNAL("lastWindowClosed()"),a,SLOT("quit()"))
          w = at()
          a.setMainWidget(w)
          w.show()
          a.exec_loop()

Now, run it.

- $ python at.py

Tada! You have your application.

NOTE: If you are using Qt designer with Qt version 3.3.0 your .ui file contains: \<!DOCTYPE UI\>\<UI version=\"3.3\" stdsetdef=\"1\"\> in the header, and pyuic (3.8.1 at least) complains that the version is too recent and won\'t produce any output.

This is easy to solve; you can create a tiny script which will automatically fix this error, run make and run your new application:

#!/bin/bash

sed -i s/3.3/3.3.0/g at.ui

make

exec python at.py

chmod 700 myscript and you\'re set !

## Setting the Default Date / Time 

Let\'s set a default value for the QDateTimeEdit widget. The QDateTimeEdit widget expects a QDateTime for an argument to the setDateTime method, so we\'ll have to create one. But how to set the time of the QDateTime? Examination of the documentation reveals that the setTime_t method will allow us to set the date with the time in seconds from the Unix epoch. We can get that from the time() function in the built-in time module.

Here\'s the code that does that. We\'ll put this in the `__init__`{.backtick} method so that it gets populated correctly from the beginnin. Remember to import time!

-         # Set the date to now
              now = QDateTime()
              now.setTime_t(time.time()) # Time in seconds since Unix Epoch
              self.time.setDateTime(now)

This code snippet should show how easily python and [PyQt](PyQt) work with each other. It should also demonstrate the thought processes you\'ll have to go through to manipulate Qt\'s widgets.

## Signals and Slots 

Everything you do from here on out is connecting Signals to Slots. It\'s pretty easy, which is why I like [PyQt](PyQt).

Python isn\'t C++. So it has to deal with Signals and Slots in a new way.

First, in Python, anything that is callable is a slot. It can be a bound method, a function, or even a lambda expression. Second, in Python, a signal is just some text that is meaningless.

Let me clarify the distinction between a C++ Signal/Slot and a Python Signal/Slot. It has nothing to do with where the object was created. It has everything to do with where the Signal originated, and where the Slot is located. For instance, a QPushButton has a C++ Signal, \"clicked()\". If you create your own subclass in Python, called \"PyPushButton\", it still has a C++ Signal, \"clicked()\". If you created a new Signal in Python, called \"GobbledyGook()\", then it is a Python Signal, because nothing in C++ even knows of its existence.

When you bind a signal to a slot, you can do one of the following:

- Bind a C++ Signal to a Python slot
  - You\'ll do this all day long. This is done by making the call as follows:

        QObject.connect(some_object, SIGNAL('toggled(bool)'), some_python_callable)

    See here for an example how to simplify this task with decorators (in Python 2.4): [http://www.diotavelli.net/PyQtWiki/SignalDecorator](http://www.diotavelli.net/PyQtWiki/SignalDecorator)
- Bind a C++ Signal to a C++ Signal
  - You won\'t do this very often, but it comes in handy.

        QObject.connect(some_object, SIGNAL('toggled(bool)'), some_object, SLOT('the_slot(bool)'))
- Bind a Python Signal to C++ or Python Slot
  - You won\'t be using Python Signals too often, but this is how to do it. Basically, you imagine up a new signal name. Then you change \"SIGNAL\" above to \"PYSIGNAL\". If you are using a lot of Python signals, it may make some sense to bypass the Qt signalling library and use your own. If you plan on porting the code to C++ one day, that won\'t make any sense at all. I have done this because I found the syntax a bit burdensome, and the debugging difficult.

Our application is going to respond to only one signal: the \"Schedule\" button being pressed. What it will do is run the \"at\" command with appropriate arguments.

Here is the code to initiate the connection:

- self.connect(
          self.schedule, SIGNAL('clicked()'),
          self.schedule_clicked
      )

Notice that we are connecting a C++ Signal to a Python Slot. However, that slot doesn\'t exist yet. Let\'s add it to the \'at\' class.

-     def schedule_clicked(self):
              if not str(self.command.text()):
                  QMessageBox.critical(self,
                      "Invalid event", "You must specify an event",
                      QMessageBox.Ok)
                  return

              t = str(self.time.dateTime().toString('hh:mm MM/dd/yyyy'))
              p = os.popen('at -m "%s"'%t, 'w')
              p.write(str(self.command.text()))
              self.close()

The process here is two fold. First, we check to see if something is specified in the \"command\" QLineEdit widget. If not, we show a QMessageBox with a critical message.

If there is something in the command box, we open up a pipe to the \'at\' command. \'at\' expects the command to be coming in on stdin. We then write to it\'s stdin the command we want to execute. Notice that we don\'t do any error checking here.

Go ahead and run the application now, and use the \'atq\' command to see if the \'at\' job was queued up.

Good? Okay.

Here is the final code for the \'at.py\' file.

- from qt import *
      from at_auto import at_auto
      import time
      import sys
      import os

      class at(at_auto):

          def __init__(self, parent=None, name=None, fl=0):
              at_auto.__init__(self,parent,name,fl)

              # Set the date to now
              now = QDateTime()
              now.setTime_t(time.time()) # Time in seconds since Unix Epoch
              self.time.setDateTime(now)

              self.connect(
                  self.schedule, SIGNAL('clicked()'),
                  self.schedule_clicked
              )

          def schedule_clicked(self):
              if not str(self.command.text()):
                  QMessageBox.critical(self,
                      "Invalid event", "You must specify an event",
                      QMessageBox.Ok)
                  return

              t = str(self.time.dateTime().toString('hh:mm MM/dd/yyyy'))
              p = os.popen('at -m "%s"'%t, 'w')
              p.write(str(self.command.text()))
              self.close()

      if __name__ == "__main__":
          a = QApplication(sys.argv)
          QObject.connect(a,SIGNAL("lastWindowClosed()"),a,SLOT("quit()"))
          w = at()
          a.setMainWidget(w)
          w.show()
          a.exec_loop()

## Homework 

With the time remaining, you may want to add a few extensions.

- Using Qt Designer, add QLabels to describe what each of the inputs do. Notice that you don\'t have to change any code, just edit the \'at.ui\' file and run \'make\'.

- After you schedule the \'at\' job, you may want the application to close. Find an appropriate slot to close the \'at\' widget or the entire application. Question: Why does closing the \'at\' widget shut down the entire application?

- Do some error checking when you schedule the at job . If there are any messages, show them to the user with a QMessageBox.

- Write an application to list the \'at\' queue.

- Add functionality to edit or remove queued \'at\' jobs. Try to reuse as much code as possible. (Hint: the widget that will schedule a new \'at\' job is already finished. Try embedding it in a QDialog.)

## Future Directions 

This application could be part of a suite of Unix command line interfaces. What other commands would you like to implement? I suggest giving things like \"crontab\" and \"ps\" a try. Parsing the output of these commands isn\'t too difficult, and the interface with them is pretty easy.

You may also want to try and combine your new apps with the \'at\' app. If you like, you can sell them as a Unix graphical interface, but you\'ll have to buy the commercial license for both Qt and [PyQt](PyQt) unless you stick with something like the GPL.
