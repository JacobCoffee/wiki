# JythonDeveloperGuide/IntellijNotes

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

## Intellij project creation notes 

Jython is an Ant project. This makes it a bit difficult to import into Intellij IDEA. This step by step guide should help you to get started.

### Prequisites 

#### Software packages (outside Intellij) 

- ant

- mercurial

- Java JDK

- Python 2.7

- Intellij IDEA 12 ([http://www.jetbrains.com/idea/](http://www.jetbrains.com/idea/))

There is a free \"Community Edition\" of Intellij that might work (I\'m only unsure about the Python integration). However as I ([SvenDehmlow](./SvenDehmlow.html)) use the Ultimate Edition, this tutorial is tested with this edition.

Intellij offers free IDEA licenses for Open Source projects. Perhaps it might be a good idea to apply for them.

#### Intellij Plugins 

- Ant Support (Bundled)
- Eclipse Integration (Bundled)
- hg4idea (Bundled)
- Python (Custom, i.e. must be installed from Intellij plugin repository)

Of course there are many other useful plugins, but these four are essential for importing Jython into Intellij IDEA.

### Steps 

#### Make a clean checkout 

:::: 
::: 
``` 
   1 hg clone http://bitbucket.org/jython/jython jython
```
:::
::::

#### Remove Intellij files from jython 

Unfortunately the Intellij project files in the jython source directory don\'t work (anymore?). We\'ll delete them. Later Intellij IDEA will create new ones for us.

Change into the jython directory:

:::: 
::: 
``` 
   1 cd jython
```
:::
::::

Remove files:

:::: 
::: 
``` 
   1 rm -rf .idea/
   2 rm Jython27.iml
```
:::
::::

#### Run ant 

Run this in the jython source directory (if you made the previous step, you\'re already there):

:::: 
::: 
``` 
   1 ant
```
:::
::::

#### Import jython as Eclipse-Project in Intellij IDEA 

Start Intellij IDEA. Close the last open project (if there\'s any), to get to the start screen.

Choose *Import Project*:

![WelcomeToIntellijIdea.png](attachments/JythonDeveloperGuide(2f)IntellijNotes/WelcomeToIntellijIdea.png "WelcomeToIntellijIdea.png")

Select jython source directory:

![SelectFileOrDirectoryToImport.png](attachments/JythonDeveloperGuide(2f)IntellijNotes/SelectFileOrDirectoryToImport.png "SelectFileOrDirectoryToImport.png")

*Import project from external model* \--\> *Eclipse*:

![ImportProject.png](attachments/JythonDeveloperGuide(2f)IntellijNotes/ImportProject.png "ImportProject.png")

Check *Link created Intellij IDEA modules to Eclipse project files*. For other fields the defaults should be sufficient.

![ImportProject2.png](attachments/JythonDeveloperGuide(2f)IntellijNotes/ImportProject2.png "ImportProject2.png")

*Finish*:

![ImportProject3.png](attachments/JythonDeveloperGuide(2f)IntellijNotes/ImportProject3.png "ImportProject3.png")

Drag and drop the ant build.xml from the project window to the ant window. This will make Intellij aware of the ant project.

![DragAndDropAnt.png](attachments/JythonDeveloperGuide(2f)IntellijNotes/DragAndDropAnt.png "DragAndDropAnt.png")

#### Configure SDKs 

If you\'ve configured more than one SDK for Python oder Java in Intellij IDEA, you should open the *Project Structure* (Shortcut: Strg + Alt + Shift + s) and check that the right SDKs are used for Jython.

I think a JDK \>= 6 and CPython corresponting to the current Jython version (2.7) are good guesses.

![ProjectStructureFacetPython.jpg](attachments/JythonDeveloperGuide(2f)IntellijNotes/ProjectStructureFacetPython.jpg "ProjectStructureFacetPython.jpg")

![ProjectStructureProjectSDK.jpg](attachments/JythonDeveloperGuide(2f)IntellijNotes/ProjectStructureProjectSDK.jpg "ProjectStructureProjectSDK.jpg")

#### InformixDataHandler and OracleDataHandler 

The classes [InformixDataHandler](./InformixDataHandler.html) and [OracleDataHandler](./OracleDataHandler.html) depend on proprietary Jars. Downloading the Oracle odbc.jar for example requires a reqistration at Oracles Website.

If you just want to get your project running, delete both classes ([InformixDataHandler](./InformixDataHandler.html) and [OracleDataHandler](./OracleDataHandler.html)). Thats it. ![:)](/wiki/modernized/img/smile.png%20":)")

If you\'re going to work in the area of JDBC data handlers, figure from build.xml out which jars you\'ll need (one for Infromix and one for Oracle), download them and put them into the extlibs directory.

#### Make 

Build the project to see, if everything went well. For this either use *Build* \--\> *Make Project* in the menu or the shortcut Ctrl + F9.

### What did we? 

Speaking in Intellij jargon, we adopted the whole *Project Structure* (classpath, source and test directories, libaries) from the Eclipse project files. We could have done this manually, but this way was much easier and less error-prone.

It\'s a good idea to take a look at the *Project Structure* (Shortcut: Ctrl + Alt + Shift + s) as e.g. the classpath might change with the next update.
