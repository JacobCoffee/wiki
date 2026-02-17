# JythonFaq/DistributingJythonScripts

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# Distributing Jython Scripts 

return to [JythonFaq](JythonFaq)

------------------------------------------------------------------------

## How can others use scripts/applications I\'ve developed? 

Initial creation date: Aug 2007 last updated: Aug 6, 2009

### Using Maven 

The easiest way to distribute a standalone jar is by using the **[jython compilation maven plugin](http://mavenjython.sourceforge.net/compile/)**. It allows you to deploy a standalone project that includes jython with libraries.

For demonstration of this plugin, see the [demo project](http://mavenjython.sourceforge.net/compile/demo/) and its [source code](https://sourceforge.net/p/mavenjython/code/ci/HEAD/tree/jython-compile-maven-plugin-test/). It shows how to

- **launch a python console** \-- look at [AbstractInitJython and InitJython](https://sourceforge.net/p/mavenjython/code/ci/HEAD/tree/jython-compile-maven-plugin-test/src/main/java/net/sf/mavenjython/) on how to launch a python/jython console, how to execute python code snippets, and how to run a python script.

- **include python libraries** \-- the plugin also downloads and bundles python libraries (using easy_install) in the package phase, and adds them to the jar. The resulting jar can have all the libraries of the project, all pom dependencies and all the python libraries requested. The demo project shows this with the \"nose\" python library (see the pom file).

For testing python / jython code, the [python test maven plugin](http:/mavenjython.sourceforge.net/test/) allows you to run your python tests alongside the normal junit tests. The [demo project](http:/mavenjython.sourceforge.net/test/demo/) (look at the source at [source code](https://sourceforge.net/p/mavenjython/code/ci/HEAD/tree/python-test-maven-plugin-test/)) shows the use of standard python unit tests (with nose) and BDD (behaviour testing) with the lettuce-clone freshen.

The sourceforge umbrella project is [http://mavenjython.sourceforge.net/](http://mavenjython.sourceforge.net/)

### Manually 

**NOTE:** This contains advanced concepts that require knowledge of Java development. Specifically, if you do not know what a classpath is, the difference between a class and a .class file and how they are created or don\'t know what a jar file contains or what it really is, then I would suggest learning these **Java** concepts and once you understand them, come back and continue on. Here are a couple of links that may help you: [Java Tutorial](http://java.sun.com/docs/books/tutorial/java/TOC.html) and [About Java Technology](http://java.sun.com/docs/books/tutorial/getStarted/intro/index.html) but I would not stop with these two links. Use your favorite search engine and search for the terms above. [LearningJython](LearningJython) is also good reading.

------------------------------------------------------------------------

- There are several ways to accomplish this, but the following text will only cover distributing code you\'ve written so others with out a Jython installation can use them without having to use jythonc. If someone wants to cover deployment to a web app server or embedded deployment, please do! These are beyond the scope of this text and more importantly my personal knowledge.

There are really two main ways to accomplish distributing your code and, like most things Jython, they are pretty easy.

## Requirements 

For your script to run on another PC there isn\'t much in the way of requirements really only two that I can think of.

- You need a reasonably current JVM installed on the target machine, I\'ve used every thing from Java 1.4.2 through Java 1.6.
- You need the standalone Jython Jar from Jython 2.2 or greater.

What I did is install Jython twice. Once as a regular installation (not standalone) and then once as standalone. Then I renamed the standalone Jython jar file to jythonStandalone.jar, moved it into my original Jython2.2 directory, and deleted the other one.\
[*Note:*] *you don\'t have to call it \'jythonStandalone\' it is simply the name I chose you can use any name you like as long as it ends in .jar.*

## Using the Class Path 

Just set up the classpath with all the jars needed and pass that to java with the \"-cp\" command-line option. That\'s a pretty standard thing for command line Java tools to do and isn\'t specific to Jython. If you\'re going to do that, you can\'t use -jar though. Just add the Jython jar to the things you\'ve added to the classpath and give Jython\'s main class, org.python.util.jython, explicitly. Optionally you can add a script as a parameter which would run as usual. This does not use jythonc in any way.

So this boils down to:

- having your scripts (\*.py) outside the standalone jython.jar
- having all the .jars you need on the classpath (including standalone jython.jar)
- starting java with the appropriate -cp (-classpath) option and package name.

for example:

- (Linux / Unix) java -cp /path/to/jython2.2/jython.jar:\$CLASSPATH org.python.util.jython \[file.py\]
- (windows) java -cp \"c:\\jython2.2\\jython.jar;%CLASSPATH%\" org.python.util.jython \[file.py\]

## Using the Jar Method 

This is my favorite method of distribution. It\'s less hassle for you, the developer, with fewer files to keep track of and easier for your end users to use. This also does not use jythonc in any way.

If you are not using any 3rd party jar files, the very simplest way is to add them to the standalone jython.jar, in the /Lib folder.

If you ARE using 3rd party jars, such as dom4j or maybe Apache Commons jars, what worked very well for me is to explode the jar files, delete the meta_inf directory since you won\'t need it, and copy the the org or com directory into the standalone Jython jar file into the root directory. If you do that, you don\'t have to mess with python.path and the like. Imports should just work. For example, the dom4j directory extracts into a directory structure that starts org/dom4j/\*. The entire org directory structure should be copied into the standalone Jython jar file into the root directory so that the jar now contains /org/python and /org/dom4j.

So this boils down to:

- having your scripts (\*.py) inside standalone jython.jar in the /lib directory
- having all the classes (\*.class) in the /org or /com directory
- having all the .jars you need on the classpath (including standalone jython.jar)
- start java with the -jar option.

for example:

    $ java -jar jython.jar {optional .py file}

you can manipulate .jar files with tools like:

- jar \-- jar is a command line program that is distributed as part of the Java jdk/sdk.

- (on Linux) midnight commander

- (on Windows) servant salamander or total commander
  - total commander: [http://www.ghisler.com/index.htm](http://www.ghisler.com/index.htm)

  - servant salamander: [http://www.altap.cz/download.html#sal25](http://www.altap.cz/download.html#sal25)

- zip and unzip \-- Command line tools available from [http://www.info-zip.org/](http://www.info-zip.org/). A jar, after all, is a special kind of zip file.

Obviously, the tools listed are just examples, [not endorsements(!)]. You should use what ever works best for you. I\'ve tried using winzip but had difficulty with it. Maybe ant would be another way to do this. If someone wants to post an ant script, that would be wonderful because I\'m hardly an ant expert.

For additional info I would strongly suggest you review Oti\'s notes at [http://jython.extreme.st/talk/talk.html](http://jython.extreme.st/talk/talk.html) (search for Script Deployment).

For me personally I found the jar method worked best for me. I had the supporting jars and scripts in the standalone Jython jar and then the primary script separately. So I had 2 files that I distributed: one .jar and one .py. Because the support files were pretty stable and didn\'t change this allowed me to easily improve and fix bugs in the main .py file.

I could have only distributed a single jar file by renaming my main .py file to `__run__.py` and putting it into the root directory of the jar file. **But** note that you will have to remove the `if __name__ == '__main__'`{.backtick} check from `__run__.py`{.backtick}, since the `__name__`{.backtick} is set to the jar file name. So, for example, if your original main script looks like:

    import foo
    if __name__ == "__main__":
        foo.do_something()

Then `__run__.py`{.backtick} will look like this:

    import foo
    foo.do_something()

Then, after packaging `__run__.py`{.backtick} inside the JAR file, the command simply becomes:

    $ java org.python.util.jython -jar myapp.jar

If you use this method, you may have to add your jar file (myapp.jar in the above example command line) to your CLASSPATH environment variable.

## Building jars - some samples 

The following examples assume that you want to build and run your Jython application from a jar file in a way that is **not** dependent on files in your Jython installation. This will enable your users to run your Jython application (packaged in a jar file) without installing Jython. They will, of course, need Java installed on their machines.

The following example scripts were developed on Linux (and the bash shell), but with minor modifications, you should be able to do the same thing in an MS DOS box on MS Windows.

### Add Jython install stuff to our jar 

To build our jar, we first make a copy of jython.jar, then add the contents of the Lib/ directory to it:

    $ cd $JYTHON_HOME
    $ cp jython.jar jythonlib.jar
    $ zip -r jythonlib.jar Lib

### Add modules and paths to the jar file 

Then we copy this expanded jar file, and add modules that are specific to our application. I\'m also going to add a path to an additional jar file to the manifest:

    $ cd $MY_APP_DIRECTORY
    $ cp $JYTHON_HOME/jythonlib.jar myapp.jar
    $ zip myapp.jar Lib/showobjs.py
    # Add path to additional jar file.
    $ jar ufm myapp.jar othermanifest.mf

Where, othermanifest.mf contains the following:

    Class-Path: ./otherjar.jar

### Run the script/jar 

Now I have a self-contained jar file that I can run by executing the following:

    $ java -jar myapp.jar testmyapp.py

The file `testmyapp.py` imports modules that I have added to `myapp.jar` and `otherjar.jar`, then starts my application.

### A more self-contained jar file 

Now suppose you want to package your \"start-up\" script in the (main) jar itself. In order to do so, follow the above instructions plus:

- Rename (or copy) your start-up script to `__run__.py` (but removing the `if __name__ == '__main__'`{.backtick} check, as described above). Add it to the (main) jar file at the root. (On Linux/UNIX you could also do this by using the `ln -s` command to create a symbolic link.) For example, you might do something like this:

      $ zip myapp.jar __run__.py

- Add the path to your jar to your CLASSPATH environment variable.

Now you can run your application with the following:

    $ java org.python.util.jython -jar myapp.jar

Notice how, when we start the application, we specify the jython class (`org.python.util.jython`) on the command line. That starts the Jython interpreter, which looks for and runs our `__run__.py` script.

Alternatively, instead of adding your standalone jar to the `CLASSPATH` environment variable, you can use the `-cp` or `-classpath` command line options:

    $ java -cp myapp.jar org.python.util.jython -jar myapp.jar

This works because Java and Jython both *have `-jar` options. The first `-jar` tells Java to run Jython, and the second `-jar` tells Jython to run the `__run__.py` in the jar file.*

## A summary 

Create the basic jar:

    $ cd $JYTHON_HOME
    $ cp jython.jar jythonlib.jar
    $ zip -r jythonlib.jar Lib

Add other modules to the jar:

    $ cd $MY_APP_DIRECTORY
    $ cp $JYTHON_HOME/jythonlib.jar myapp.jar
    $ zip myapp.jar Lib/showobjs.py
    # Add path to additional jar file.
    $ jar ufm myapp.jar othermanifest.mf

For a more self-contained jar, add the `__run__.py` module:

    # Copy or rename your start-up script, removing the "__name__  == '__main__'" check.
    $ cp mymainscript.py __run__.py
    # Add your start-up script (__run__.py) ot the jar.
    $ zip myapp.jar __run__.py
    # Add path to main jar to the CLASSPATH environment variable.
    $ export CLASSPATH=/path/to/my/app/myapp.jar:$CLASSPATH

On MS Windows, that last line, setting the `CLASSPATH` environment variable, would look something like this:

    set CLASSPATH=C:\path\to\my\app\myapp.jar;%CLASSPATH%

Or, again on MS Windows, use the Control Panel and the System properties to set the CLASSPATH environment variable.

Run the application:

    $ java -jar myapp.jar mymainscript.py arg1 arg2

Or, if you have added your start-up script to the jar, use one of the following:

    $ java org.python.util.jython -jar myapp.jar arg1 arg2
    $ java -cp myapp.jar org.python.util.jython -jar myapp.jar arg1 arg2
    $ java -jar myapp.jar -jar myapp.jar arg1 arg2

**NOTE:** Wildcard imports, e.g. `from javax.swing import *` that may work when invoking using jython directly `jython myapp.py`, or `java -jar jython.jar myapp.py` fail when the application is packaged as a single jar file. To avoid this problem, always use explicit imports for Java packages, e.g. `from javax.swing import JFrame`.

## A note about webstart 

Ok maybe one mention of webstart: check out these postings to the mailing list (all from aug 2007):

- [http://article.gmane.org/gmane.comp.lang.jython.user/5821](http://article.gmane.org/gmane.comp.lang.jython.user/5821)

- [http://article.gmane.org/gmane.comp.lang.jython.user/5820](http://article.gmane.org/gmane.comp.lang.jython.user/5820)

- and David Huebel recommends [http://seanmcgrath.blogspot.com/JythonWebAppTutorial.html](http://seanmcgrath.blogspot.com/JythonWebAppTutorial.html) the first part looks pretty good.

## \"What\'s a really easy way to distribute my app as a single jar?\" 

Start with a fresh working directory. Paste the following code into the file `Main.java`:

:::: 
::: 
``` 
   1 import java.io.FileInputStream;
   2 import java.lang.System;
   3 import java.util.Properties;
   4 
   5 import org.python.core.Py;
   6 import org.python.core.PyException;
   7 import org.python.core.PyFile;
   8 import org.python.core.PySystemState;
   9 import org.python.util.JLineConsole;
  10 import org.python.util.InteractiveConsole;
  11 import org.python.util.InteractiveInterpreter;
  12 
  13 public class Main {
  14     private static InteractiveConsole newInterpreter(boolean interactiveStdin) {
  15         if (!interactiveStdin) {
  16             return new InteractiveConsole();
  17         }
  18 
  19         String interpClass = PySystemState.registry.getProperty(
  20         "python.console", "");
  21         if (interpClass.length() > 0) {
  22             try {
  23                 return (InteractiveConsole)Class.forName(
  24             interpClass).newInstance();
  25             } catch (Throwable t) {
  26                 // fall through
  27             }
  28         }
  29         return new JLineConsole();
  30     }
  31 
  32     public static void main(String[] args) throws PyException {
  33         PySystemState.initialize(
  34             PySystemState.getBaseProperties(), 
  35             new Properties(), args);
  36 
  37         PySystemState systemState = Py.getSystemState();
  38         // Decide if stdin is interactive
  39         boolean interactive = ((PyFile)Py.defaultSystemState.stdin).isatty();
  40         if (!interactive) {
  41             systemState.ps1 = systemState.ps2 = Py.EmptyString;
  42         }
  43 
  44         // Now create an interpreter
  45         InteractiveConsole interp = newInterpreter(interactive);
  46         systemState.__setattr__("_jy_interpreter", Py.java2py(interp));
  47         interp.exec("try:\n import entrypoint\n entrypoint.main()\nexcept SystemExit: pass");
  48     }
  49 }
```
:::
::::

Then, in the working directory, execute the following commands

    $ mkdir Package
    $ cd Package
    $ cp -r JYTHONROOT/Lib .
    $ unzip JYTHONROOT/jython.jar
    $ # add your modules to Lib
    $ javac ../Main.java -d .
    $ cp ../entrypoint.py .
    $ jar -cfe output.jar Main *

The entrypoint.py mentioned above must be provided by you. It is a python script with a parameterless function main(), e.g.,

    from my_prog import main

With all this, `java -jar output.jar`{.backtick} should run your code.

**NOTE**: Please email charlieATcharliedyson.net if this does or does not work for you, I\'ve only just come up with it as I wanted a single jar that could be executed without any arguments. The Main.java code above was hacked to support readline (if possible) by msdemleiATari uni-heidelberg.de, so if that bugs you, don\'t bother Charlie, ask Markus. Also, an ant build as well as a sample project that implements this method is available [here](https://github.com/jsbruneau/jython-selfcontained-jar).

## Resources and acknowledgements 

Finally, as in all things [YMMV](http://en.wiktionary.org/wiki/your_mileage_may_vary). If you have different experences or just think I\'m crazy then don\'t just sit there and complain, contribute to the wiki!

I\'d like to thank Oti H., Charlie G., Frank W., and all the others that have helped along the way.

If you have questions about the FAQ please post them on the jython-users mailing list at [http://sourceforge.net/mail/?group_id=12867](http://sourceforge.net/mail/?group_id=12867)

By: [GregMoore](GregMoore) & [DaveKuhlman](DaveKuhlman)\
Help from: The members of the Jython-users and Jython-dev mailing lists

------------------------------------------------------------------------

Return to [JythonFaq](JythonFaq)
