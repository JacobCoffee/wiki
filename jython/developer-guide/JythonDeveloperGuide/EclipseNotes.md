# JythonDeveloperGuide/EclipseNotes

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# Creating an Eclipse Project for Jython Development 

These notes are based on configuring Eclipse 3.7 on Windows 7 in order to work as a Jython developer. There were lots of little pitfalls.

## Setting up to Develop 

### Tools Assumed 

- Eclipse IDE for Java (SE or EE)
- Mercurial Eclipse plug-in

Command-line versions of

- Ant
- Mercurial

These notes assume the tools are on your path wherever needed.

- A version 1.6 JDK

### Clone the Jython Repository 

It should be possible to direct Eclipse to the on-line Jython repository at hg.python.org/jython but I prefer to do it in two stages. At `C:\hg\jython-clean` I have a clone of the repository created with the command-line `hg` (see [JythonDeveloperGuide#Mercurial)](JythonDeveloperGuide#Mercurial.29) that I use as a local ***mirror repository***.

### Create an Eclipse project 

1.  Open Eclipse and for the sake of simplicity, close any already open projects.

2.  From the **File \>\> New \>\> Project\...** dialogue choose **Mercurial \>\> Clone Existing Mercurial Repository**.

3.  In the Mercurial wizard, choose the **Local\...** button and navigate to the ***mirror repository***

4.  Choose **Checkout as a project in the workspace**.

5.  You can take the default directory name in your Eclipse workspace (parent directory), as you will end up with a project called \"jython-trunk\".

6.  Leave **Last revision** blank.

7.  Press **Next\>**. The clone can take several minutes.

8.  At the next dialogue you may choose the \"branch\". These instructions assume you are developing on the default (tip).

9.  The next operation is equivalent to an `hg update` instruction and will populate the project with files from the repository. It may take a few minutes to execute. (If it fails with a message about the server certificate, follow the advice on Subversion and SSL in [JythonDeveloperGuide](JythonDeveloperGuide).)

10. The wizard will prompt you to import a project called \"jython-trunk\". Accept this.

You should now have a project called \"jython-trunk\" open in your Eclipse workspace. Do not worry that the IDE reports errors. The following steps will put that right, although it gets worse before it gets better.

If you need to, this is the time to rename the project to your liking. (You may have to File \>\> Refresh first.)

### Build it once outside the IDE 

It is easiest to set up the IDE if you have already built Jython once outside the IDE. Start a command prompt in the project home (jython-trunk) directory, and issue the command `ant`. It is normal and harmless to get warnings from ANTLR and the javac tasks, but you should end up with \"BUILD SUCCESSFUL\".

You may as well check it works. If you happen to have an environment variable `JYTHON_HOME`, delete it with `set JYTHON_HOME=`. At the command prompt then, enter

    dist\bin\jython

You will see Jython cache indexes of all the JAR files it can find, then you\'ll get the prompt `>>>`. Try a few well chosen Python commands to prove it works. The command to make it stop is `exit()`.

### Fix-up the class path in the IDE 

The particulars of this section date very quickly as the selection of JAR files and their version numbers change. Enough to say that it is not unusual for the `.classpath` file that Eclipse uses to be out of sync with the actual JAR files in `extlibs`. The IDE build path (checked out by `hg` to file `.classpath`) will need changes like the following (correct around March 2012):

1.  Open **Project \>\> Properties \>\> Java Build Path** and from the **Libraries** tab remove the following:

    - `extlibs/asm-3.1.jar` using **Remove**

    - `extlibs/asm-commons-3.1.jar` using **Remove**

    - `extlibs/guava-r07.jar` using **Remove**

2.  On the **Libraries** tab of the same dialogue, add:

    - `extlibs/guava-11.0.2.jar` to the **Libraries** tab using **Add JARs\...**

    - `build/exposed` to the **Libraries** tab using **Add Class Folder\...**

3.  On the **Order and Export** tab of the same dialogue, find `build/exposed` and move it to the top.

4.  Close it with OK.

5.  Open **Window \>\> Preferences \>\> Java \>\> Build Path \>\> Classpath Variables \>\> New\...** and define the name ANT_HOME to be a **Folder\...**, then navigate to the Eclipse plug-ins directory and the org.apache.ant folder. (For me, ANT_HOME is exactly \"`C:/eclipse/plugins/org.apache.ant_1.8.2.v20110505-1300`\".)

6.  OK your way out, but decline to do a full rebuild, if asked.

### Controlling compilation in the IDE 

The Eclipse IDE will decide to recompile Java source whenever it thinks something has changed. This is frequent (and often useful) but we must make sure it matches what the custom build (`build.xml`) file would have done. The build file specifies a Java 1.6 compiler and runs a stage called \"exposing\".

If you are not already using Java 1.6 compliance globally:

1.  Open **Window \>\> Preferences \>\> Java \>\> Installed JREs** and check that you have a 1.6 standard JDK available to Eclipse. If not, find and add one with **Search\...**. (You do not need to make it the default.)

2.  Open **Project \>\> Properties \>\> Java Compiler** and click **Enable project specific settings** and below it in the drop-down select 1.6.

3.  A bit of advice appears in the dialogue about making sure you use a J2SE-1.6 JRE. Click the link taking you to the Java Build Path dialogue.

4.  Select the JRE System Library and press **Edit\...**. Use that dialogue to choose a 1.6 standard environment.

Configure the IDE build process to use key parts of build.xml as follows:

1.  Open **Project \>\> Properties \>\> Builders** and click **New\...** then choose **Ant Builder**.

2.  Call the configuration something like \"Jython exposer\".

3.  On the **Main** tab, use **Browse Workspace** to select the `build.xml` file.

4.  On the **Refresh** tab select **Refresh Resources**. (Optional: the IDE seems to know when to refresh.)

5.  On the **Targets** tab, in the **After a \"Clean\"** section, remove the default target so the builder is not set to run for this build kind.

6.  On the **Targets** tab, leave the **Manual build** section using the default target (which is a full developer build).

7.  On the **Targets** tab, in the **Auto Build** section, remove the default target and add \"expose\".

8.  On the **Targets** tab, in the **During a \"Clean\"** section, remove the default target and add \"clean\".

9.  On the JRE tab select **Separate JRE** and specify one modern enough to run Ant (e.g. a 1.6 JDK).

You can play with those settings later in the same dialogue using **Edit\...**. For example, on the **Main** tab, is the arguments section where you might add -verbose, if you need to see better what Ant is doing.

### A first run 

Unless you have **Project \>\> Build automatically** turned off, the incremental builder of the Eclipse IDE will have been beavering away in the background, and may even have succeeded in building Jython, or it may have reached a confusing state. Invoke menu **Project \>\> Clean\...**. This will provoke a complete rebuild (if **Build automatically** is on). If necessary, invoke **Project \>\> Build**.

Open **Project \>\> Properties \>\> Run/Debug Settings \>\> New\... \>\> Java Application** and call the launch configuration \"Jython Interactive\". If the IDE hasn\'t already found it, on the **Main** tab use **Search\...** to select the class `org.python.util.jython`. In **VM arguments** enter the following:

    -Dpython.home=dist
    -Dpython.console=org.python.util.InteractiveConsole

OK your way out of the dialogues.

From the Run menu choose **Run configurations\... \>\> Jython Interactive \>\> Run**. Jython should run and produce a lot of messages about cacheing JAR files. Then it gives you an interactive prompt. You should find you have a (semi-)working interactive Jython interpreter running in the console window of the IDE. It will do simple one-liners, but unfortunately interprets /r/n as two lines. (Unsolved problem.)

You can build additional run configurations by copying, and supply them with application arguments, for example to run scripts. JUnit tests also work in the environment of this poroject.

## Things that go wrong 

Here are the symptoms of and solutions for a number of things I did wrong. The instructions above are designed to allow you to avoid them, but you may encounter them as things change, and particularly if you set out to fix bugs in an earlier version (different tip) from the default.

### No project created 

Sometimes the Mercurial wizard seems to import the project but it does not appear in the IDE Navigator. This seems to happen when Windows Explorer is open in the newly-created project folder, preventing a rename. Try again, and this time don\'t peek.

### JYTHON_HOME Defined 

If you have an environment variable `JYTHON_HOME` set, the script at `dist\bin\jython.bat` will use it to locate the installation, which may be your operational installation, not the one you just built.

### IDE Console problems 

You run org.python.util.jython as a Java Application, and maybe it produces the normal messages about cacheing JAR files. It gives you an interactive prompt, but promptly exits as if it had received an end of file from the console.

The JLine console input library Jython uses by default does not interact properly with the IDE Console window. Reading receives the equivalent of an end-of-file. In the run configuration (**Project \>\> Properties \>\> Run/Debug Settings** and the Launch configuration you used, define the VM argument `-Dpython.console=org.python.util.InteractiveConsole`. This isn\'t perfect: the input caret is not positioned where your input will actually appear, but is the best setting I\'ve found.

### Missing packages and objects 

The list of JAR files used in the build and at runtime has been tidied up recently (December 2011) but as you work you may find that the Java editor, or your run configuration, complains it cannot resolve the names of classes. It is not obvious where in the massive class path the class ought to be. There are sites to help such as [http://www.jarfinder.com](http://www.jarfinder.com) can help you guess which of the JAR files has dropped out of your path.

### Missing parser classes 

If the Java editor, or your run configuration, complains it cannot resolve the names of classes related to parsing or lexing, the problem is probably with the classes generated by ANTLR. Either the target `antlr_gen` has not run or `build/gensrc` (which is where the ANTLR output lands) is not on the path. It is possible for the path to be correct for compilation (because it is set in `build.xml`), but wrong as far as the editor is concerned (because it is set in the project properties).

### Bootstrap types 

During the build, particular classes from `build/classes` should be processed by the \"class exposer\" into classes in `build/exposed`. The Ant target `expose` achieves this, and that is why we define the ant builder in the way we do above. At runtime, if java finds the classes it is trying to load in `build/classes` instead of `build/exposed`, as the Jythoon interpreter starts to initialise itself, you will get a message like:

    init: Bootstrap types weren't encountered in bootstrapping:

The problem may be that key classes are missing from `build/exposed`, or more likely that it is not first on the class path.

### End-of-line Encoding 

Jython source uses the Unix standard LF (`\n`) to indicate an end of line. If you are editing on Windows, and you create a completely new source file, Eclipse will give it DOS-style CR-LF line separators. If you are just amending existing source files, Eclipse will conform itself to the prevailing convention in each file.

The output from scripts that generate source code (`make_pydocs.py` or `gderived.py`) can suffer from this problem too.

You can see when this has happened using the configuration dialogue at Window \>\> Preferences \>\> General \>\> Editors \>\> Text Editors, once you check the \"show whitespace\" box. There is a link adjacent that allows you to decide which whitespace characters to show. It might be worth leaving CR, LF and TAB visible.

To prevent the problem (in Eclipse new files) go to Window \>\> Preferences \>\> General \>\> Workspace and set the \"New text file line delimiter\" to \"Other\" and \"Unix\".

To correct files that already have the wrong line endings, open each in Eclipse and use File \>\> Convert Line Delimiters To \>\> Unix.

### Character Encoding 

Jython source adheres to UTF-8 encoding for files. If you are editing on Windows, it comes as a bit of a surprise that Eclipse picks up the default character encoding settings from the DOS environment, even for Java. This will probably not affect you if you are writing 7-bit clean source code, but can catch you out in literal strings where it is necessary to use accented characters.

To prevent the problem (in Eclipse) go to Window \>\> Preferences \>\> General \>\> Workspace and set the \"Text file encoding\" to \"Other\" and \"UTF-8\". This will not correct edits you have already made: you\'ll have to do that by hand (or write a Python script).

### \"version.properties\" not found 

`/org/python/version.properties` is a file generated during the build that labels the version of Jython. It is behind the generation of the banner you see when Jython starts. If you have built targets selectively after a clean, or aborted a build, it may be that the dependency is missing. Building clean should sort it out.

### The access\$ problem 

A subtle problem arises due to incremental builds performed by the IDE in combination with the class exposer. Class files generated in a command-line Ant build use (the JDK?) javac while those generated by the IDE as you edit use its own compiler. These have different strategies for generating the names of methods private to the bytecode. Also, the IDE does not know that particular classes from `build/classes` should be processed by the \"class exposer\" into classes in `build/exposed`. Hence classes in `build/exposed` refer to accessors in `build/classes` by the wrong name. (At least, I think that\'s what\'s happening.)

When the names do not match, the error that results looks like this:

    Exception in thread "main" java.lang.NoSuchMethodError: org.python.core.PyType.access$2(Lorg/python/core/PyType;Ljava/lang/Object;)V
            at org.python.core.PyType$11.onType(PyType.java:1557)
            at org.python.core.PyType.traverse_hierarchy(PyType.java:869)
            at org.python.core.PyType.invalidateMethodCache(PyType.java:1555)

Even if the names matched (which can be achieved by making both builds use the same compiler) there will be problems when classes that should have been passed through the exposer (see file `CoreExposed.includes`) are loaded from build/classes. Run with VM argument `-verbose:classes` to diagnose the problem.

    ...
    [Loaded org.python.core.PyType from file:.../jython-trunk/build/exposed/]
    ...
    [Loaded org.python.core.PyType$11 from file:.../jython-trunk/build/classes/]
    Exception in thread "main" java.lang.NoSuchMethodError: org.python.core.PyType.access$2(Lorg/python/core/PyType;Ljava/lang/Object;)V
            at org.python.core.PyType$11.onType(PyType.java:1557)
            at org.python.core.PyType.traverse_hierarchy(PyType.java:869)
            at org.python.core.PyType.invalidateMethodCache(PyType.java:1555)

The instructions above aim to ensure that each incremental build by the IDE, ends by running the `expose` Ant target.

## Key files 

Files from the repository (lost on revert): not quite right as provided from the repository:

- `.project`

- `.classpath`

Preserved through revert

- `.externalToolsConfig/*.launch`

- `.settings/org.eclipse.jdt.core.prefs`

# Instructions Posted Nov 2009 

The above probably supersededes this but it\'s preserved here for now.

1.  Run the checkout and ant build steps from the regular [JythonDeveloperGuide](JythonDeveloperGuide)

2.  In your Eclipse preferences, go to Java \> Build Path \> Classpath Variables and add a new variable named ANT_HOME that points to your ant install. That directory should have a lib/ant.jar inside of it.

3.  Go to File \> Import \> General \> \"Existing Projects into Workspace\" in Eclipse

4.  Select your Jython checkout directory as the root

This could be made to work entirely in Eclipse with a few more additions to the external builders. For now, it requires running ant in the first step to make the build/gensrc and build/jarjar directories and then every time after a clean.

**Proposed new instructions**

Using Eclipse 3.5 + Subversive:

1.  Open the SVN Repository Exploring perspective and create a new repository for the Jython SVN repository.

2.  Open the new repository, expand trunk, right click on Jython, and select Check Out. (You\'ll be prompted to accept an SSL certificate.)

3.  Once the project is finished checking out, it will show build errors. Right click on the jython-trunk project. Select Build Path \> Configure Build Path.

4.  In the Libraries tab, Add Variable \> Configure Variables, and add a classpath variable for ANT_HOME.

5.  In the Package Explorer, open the build.xml file under jython-trunk.

6.  In the Outline view, find the \"developer build\" target. Right click and Run As \> Ant Build.

7.  In the Package Explorer view, right click on the jython-trunk project, and select Refresh.

8.  The problems view should no longer show any errors.
