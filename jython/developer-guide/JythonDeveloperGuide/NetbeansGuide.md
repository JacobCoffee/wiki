# JythonDeveloperGuide/NetbeansGuide

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

## Building Jython with Netbeans 

- *Submitted by Josh Juneau on 6/10/2006*

This is a step-by-step guide to show how you may set up a Jython build using Netbeans. I used [NetBeans](./NetBeans.html) 5.5 (beta) for this tutorial.

Since this is a guide which is specific to [NetBeans](./NetBeans.html), I will only briefly touch upon the procedures for obtaining the code and all of the required JAR files.

- **OBTAIN NECESSARY CODE AND JAR LIBRARIES**

- Obtain the code:
  - \- If you do not have Subversion, you will need to download it and then check out the codebase. See the [JythonDeveloperGuide](JythonDeveloperGuide)

    - for complete details.

- Obtain required JAR files:
  - \- You will need to obtain the following five JAR files to successfully build Jython:
    - Apache Ant - ant.jar Oracle JDBC - classes12.jar Java Readline- libreadline-java-0.8.0.jar
      - *easiest to obtain by extracting from another application*

      <!-- -->

      - **Find a listing of applications: [http://java-readline.sourceforge.net/](http://java-readline.sourceforge.net/)**

      Informix JDBC- ifxjdbc.jar
      - *You will need to sign up for an IBM account (free) to obtain*

      Java EE or J2EE javaee.jar
      - or j2ee.jar

- **NOW YOU ARE READY TO BUILD JYTHON IN NETBEANS**

- Create a new project within Netbeans and name it Jython.

  - \- Be sure to uncheck the *Create Main Class* box upon creation.

- Copy all code which resides within the Jython code you\'ve obtained using Subversion. Copy this code into your project: *Jython-\>src*

  - directory.

- Copy all required JARs within that same directory. You will now have all of the source appearing within Netbeans.

- Add all appropriate JARs into your classpath via the Libraries option within the project properties and set the source level you will use to run Jython. Set Main Class to *org.python.util.jython* within the **Run** category.

- Build Jython and begin to develop. It may be helpful to set up a shortcut (or batch script in Windows) to your jython build:
  - Example:

<!-- -->

            REM File: JythonBuild.bat
            REM ** Executable for desktop **
            java -jar "<<path to codebase>>\Jython\dist\Jython.jar"

- You should see something that looks like this:

<!-- -->

    init:
    deps-clean:
    Deleting directory C:\j2ee_dev\Jython\build
    Deleting directory C:\j2ee_dev\Jython\dist
    clean:
    init:
    deps-jar:
    Created dir: C:\j2ee_dev\Jython\build\classes
    Compiling 357 source files to C:\j2ee_dev\Jython\build\classes
    Note: * uses or overrides a deprecated API.
    Note: Recompile with -Xlint:deprecation for details.
    Copying 11 files to C:\j2ee_dev\Jython\build\classes
    compile:
    Created dir: C:\j2ee_dev\Jython\dist
    Building jar: C:\j2ee_dev\Jython\dist\Jython.jar
    To run this application from the command line without Ant, try:
    java -jar "C:\j2ee_dev\Jython\dist\Jython.jar"
    jar:
    BUILD SUCCESSFUL (total time: 2 minutes 23 seconds)
