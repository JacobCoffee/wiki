# ReadlineSetup

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

**Contents**

### Configure Readline for Jython 2.5 

Jython now supports readline functionality of out the box, as of 2.5.0, by bundling JLine. In addition, 2.5.2 beta 2 adds completion support. See the [tracking issue](http://bugs.jython.org/issue1133).

You can also try [Jython Console](http://code.google.com/p/jythonconsole/), which is implemented on Swing. It features code completion and has been updated to work with Jython 2.5.

### Configuring Readline for Jython 2.1 

(This content will moved to another page shortly and is probably of historical interest only at this point.)

Jython can support line editing and history via the [Java-Readline](http://java-readline.sourceforge.net/) library on unix systems. Java-Readline wraps [GNU Readline](http://directory.fsf.org/readline.html) with a JNI interface to provide advanced editing support to Java console programs. However, Java-Readline is not bundled with the standard Jython distribution. This note describes how to configure Readline support into an existing Jython install. It is not necessary to rebuild Jython from source, but you will need to build/install Java-Readline if a prebuilt version doesn\'t exist for your platform/OS distribution (which is likely the case).

These instructions were tested on a Fedora linux system, with Jython-2.1, Sun JDK1.5 (note GCJ does not work at this time), and GCC. It as assumed that Jython has already been installed.

1\. [Checkout Java-Readline](http://sourceforge.net/cvs/?group_id=48669), uncomment the correct OS_FLAVOR line in java-readline/Makefile and follow the included build instructions. This will require both java and C compilers. If the necessary compilers can be found in your path, building should be as simple as:

    $ cvs -d:pserver:anonymous@java-readline.cvs.sourceforge.net:/cvsroot/java-readline login 
    $ cvs -z3 -d:pserver:anonymous@java-readline.cvs.sourceforge.net:/cvsroot/java-readline co -P java-readline
    $ cd java-readline
    $ vi Makefile#or whatever editor you prefer to fix OS_FLAVOR
    $ make

The build results in the creation of following two files:

- libreadline-java.jar
- libJavaReadline.so on most systems or libJavaReadline.jnilib on Mac

These can be copied to a convient location, but the rest of these instructions assume they remain in /home/myname/java-readline.

2\. Jython needs to be configured to use the Java-Readline library. Edit the jython [registry](http://www.jython.org/archive/21/docs/registry.html) file, setting the following two lines:

    python.console=org.python.util.ReadlineConsole
    python.console.readlinelib=GnuReadline

3\. Jython also needs to have libreadline-java.jar in its CLASSPATH, and the shared library needs to be available to the OS\'s dynamic linker when loading Jython. Both of these can be done through setting environment variables as follows on most systems:

    export LD_LIBRARY_PATH=/home/myname/java-readline
    export CLASSPATH=/home/myname/java-readline/libreadline-java.jar:$CLASSPATH

You can put these directly into the shell script that invokes jython (created by the installer), or into one of your environment\'s startup scripts.

On Mac you should add the jar to the CLASSPATH as above, but instead of adding the java-readline dir to LD_LIBRARAY_PATH copy libJavaReadline.jnilib to the \~/Library/Java/Extensions directory(go ahead and create it if it doesn\'t exist).

That\'s it. You should now be able to invoke jython\'s interactive console, with readline powered command line editing enabled.

### Common Error Messages 

Its not uncommon to trip up on one of the configuration steps. Here\'s some of the possible errors that may be encountered and some clues on what they mean and where to look for a fix.

If you see no error\'s on Jython startup, and when at the interactive console you press cursor up and just see junk like:

    >>> ^[[A

Then readline simply isn\'t enabled. You should investigate if the setting **python.console** is correctly specified in the registry, and ensure the registry file you\'ve edited is somewhere where Jython will find it on startup. You can check the registry Jython is actually using from within the interpreter by executing:

:::: 
::: 
``` 
>>>import sys
>>>print sys.registry
```
:::
::::

If Jython throws an exception on startup like:

    Exception in thread "main" java.lang.UnsatisfiedLinkError: no JavaEditline in java.library.path

followed by a backtrace, then a possible cause is that **python.console** is set but **python.console.readlinelib** is not (it defaults to JavaEditline). Again check your registry settings.

If Jython throws an exception on startup such as:

    Exception in thread "main" java.lang.NoClassDefFoundError: org/gnu/readline/ReadlineLibrary

Then libreadline-java.jar isn\'t in your classpath. Check that your CLASSPATH environment variable includes this jar file.

If on startup you see:

    Exception in thread "main" java.lang.UnsatisfiedLinkError: no JavaReadline in java.library.path

Then its possible the shared library libJavaReadline.so isn\'t being found by the linker. Make sure LD_LIBRARY_PATH includes the location of this shared library.

### Enhancements 

A [patch](http://sourceforge.net/tracker/index.php?func=detail&aid=795831&group_id=12867&atid=312867) on the jython patch-tracker implements TAB support for indentation in ReadlineConsole. However, it has not yet been accepted into Jython.

### Readline Alternatives 

While these instructions are for Java-Readline compiled against GNU Readline, Java-Readline can also be backed by the BSD licensed EditLine libary as well as a simple line editor called GetLine. One or the other may be preferable depending on your platform and license requirements. Setup is similar, you need to select the appropriate backing lib when building Java-Readline, and set **python.console.readlinelib=Editline** or **python.console.readlinelib=Getline** as appropriate (TODO: test & confirm).

Other alternatives include programs that function as console wrappers and provide history & command-editing without requiring any changes to the Jython other than the way you invoke the application itself. Examples include:

- [rlwrap](http://utopia.knoware.nl/~hlub/uck/rlwrap/) which also wraps GNU Readline, but can be used by invoking jython with:

<!-- -->

    rlwrap jython

This provides command line history and editing, but does not support the readline API (for application controlled TAB completion, etc).

- [jline](http://jline.sourceforge.net/) is a java console command editor distributed in the form of a jar file. It can be used as a wrapper by putting the jline jar file in the CLASSPATH, and changing jython invokation to:

<!-- -->

    java.exe -Dpython.home="C:\jython2.2" -cp "jython.jar;jline-0_9_5.jar" jline.ConsoleRunner org.python.util.jython

Note that this will not work from under a cygwin shell \-- it must be a native windows console.

For Unix:

    java -Dpython.home="${HOME}/jython2.2" -cp "jython.jar:jline-0.9.91.jar" jline.ConsoleRunner org.python.util.jython

Note that jline can also be used programically to provide an alternative jython console, as in [JLineConsole](http://thread.gmane.org/gmane.comp.lang.jython.devel/713).

There are several Jython swing console\'s in various states of completion that provide command editing features in a cross-platform way. The simplest is the demo console bundled with jython in the [Demo/swing/Console.py](http://cvs.sourceforge.net/viewcvs.py/jython/jython/Demo/swing/Console.py?rev=1.1&view=auto) subdir which provides a command history via the cursor-up and cursor-down keys. Others GUI console\'s include:

- [Jython Console](http://don.freeshell.org/jython/) featuring code completion.

- The interstingly named [YaTiSeWoBe](http://www-iis.unil.ch/~jiglesia/apps/yatisewobe/doc/html/sec-cons.html) has a Jython console.

- [jydle](http://cvs.sourceforge.net/viewcvs.py/jydle/Jydle/Console/) is an attempt at an IDLE-like environment for Jython, and includes an interactive console.

- [jyleo](http://webpages.charter.net/edreamleo/front.html) contains JythonShell. This appears to be actively developed but requires the alpha jython 2.2 release.

### References 

The Java-Readline library includes [contributed instructions](http://cvs.sourceforge.net/viewcvs.py/java-readline/java-readline/contrib/jpython/jython-install.txt?rev=1.1&view=markup) on building Jython with Readline support that have been very useful in sorting the process out. Many thanks to the author SteveC.

Charlie Moad [summarizes](http://article.gmane.org/gmane.comp.lang.jython.user/4018) setup instructions on ubuntu using a pre-built Java-Readline package, as well as mentioning the CLASSPATH perils of invoking Jython using `java -jar`.

The Readline wrapper rlwrap was recommended by [Dave Kuhlman](http://article.gmane.org/gmane.comp.lang.jython.user/4245).

The use of JLine and the JLineConsole implementation itself are due to [Robert Andre](http://thread.gmane.org/gmane.comp.lang.jython.devel/713).

Don Coleman introduced his Jython Console with [this](http://thread.gmane.org/gmane.comp.lang.jython.user/779) post to the jython-user mailing list.

[YaTiSeWoBe](./YaTiSeWoBe.html) is due to [Javier Iglesias](http://article.gmane.org/gmane.comp.lang.jython.user/2787).

Jydle owes its development to [Michel Pelletier](http://article.gmane.org/gmane.comp.lang.jython.user/1001).

JythonShell was [introduced](http://thread.gmane.org/gmane.comp.lang.jython.user/4177) by the enigmatic \"Leo User\".
