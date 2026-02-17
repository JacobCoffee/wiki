# ClarkUpdike/RemoteJythonDebugging

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

The following describes how to set up a remote debugging session with a running jython application (or any java application for that matter).

Basically, you just:

- Modify the java command line that starts jython
- Set up your ide to attach to the debugging session

## Java Command Line To Startup The App 

Here\'s what mine looks like to run from the jar:

    C:\apps\j2sdk1.4.2\jre\bin\java.exe -Xnoagent -Djava.compiler=NONE -Xdebug -Xrunjdwp:server=y,transport=dt_socket,address=8000 -Dpython.home=C:\\workspace\\JythonTip\\jython\\dist -jar c:\workspace\JythonTip\jython\dist\jython.jar

or to run from the class directories:

    C:\apps\j2sdk1.4.2\jre\bin\java.exe -Xnoagent -Djava.compiler=NONE -Xdebug -Xrunjdwp:server=y,transport=dt_socket,address=8000 -classpath <very long classpath> org.python.util.jython

[Eclipse hint: external java command \"snarfing\" tip](./ClarkUpdike(2f)RemoteJythonDebugging.html#commandlinesnarf)

And here\'s what the options mean:

::: {}
  ----------------------------------- ------------------------------------------------------------------------------
  **Command Line Option**             **Meaning**
  `-Xnoagent`{.backtick}              Disables the old sun.tools.debug agent
  `-Djava.compiler=NONE`{.backtick}   Turn off JIT compilation (required in order to use the \"classic\" debugger)
  `-XDebug`{.backtick}                Enable debugging
  `-Xrunjdwp:<options>`{.backtick}    Enable the Java Debug Wire Protocol
  ----------------------------------- ------------------------------------------------------------------------------
:::

And here\'s the `<options>`{.backtick}:

::: {}
  ---------------------------------- ------------------------------------------------------------
  **JDWP Option**                    **Meaning**
  `server=y`{.backtick}              Tell the app to listen for debugging connections
  `transport=dt_socket`{.backtick}   We\'re going to use a socket (see below for other options)
  `address=8000`{.backtick}          The socket to listen on
  ---------------------------------- ------------------------------------------------------------
:::

Note: Once you hit enter, the app may not respond like it normally does. For the jython interpreter, it seems to \"hang\". But once you attach your debugger to it (below), it will respond with the familiar propmt\--kind of like \"lazy initialization\".

See below for further references\...

## IDE Settings 

For Eclipse:

- Navigate into your source and set your break points.

- Select `Run`{.backtick}\|`Debug`{.backtick}.

- Look for the `Remote Java Application`{.backtick} run configuration type on the `Debug`{.backtick} dialog.

- Select your jython project.

- The `Connection Type`{.backtick}: should be `Standard(Socket Attach)`{.backtick}. I imagine in the future there may be other options, like shared memory (if your running locally on windows).

- Enter `8000`{.backtick} for the port number (or whatever port number you configure your app to listen on).

- Click `Debug`{.backtick}

This will take you into the app at the first breakpoint.

For NetBeans:\
\[\^[http://debuggercore.netbeans.org/docs/VM-options.html](http://debuggercore.netbeans.org/docs/VM-options.html) netbeans vm options for debugging\]

I have used this technique also for debugging a development Tomcat server remotely (see article below). Keep in mind that in a multithreaded environment, **all** threads will get stopped at your breakpoint, so be warned if this is not a private workspace.

## References 

- \[\^[http://java.sun.com/j2se/1.4.2/docs/guide/jpda/conninv.html](http://java.sun.com/j2se/1.4.2/docs/guide/jpda/conninv.html) jdpa 1.4.2 connection and invocation details\]

- \[\^[http://java.sun.com/j2se/1.4.2/docs/guide/jpda/architecture.html](http://java.sun.com/j2se/1.4.2/docs/guide/jpda/architecture.html) 1.4.2 jdpa architecture (high level)\]

- \[\^[http://www.ftponline.com/javapro/2003_06/online/debugging_kjones_06_23_03](http://www.ftponline.com/javapro/2003_06/online/debugging_kjones_06_23_03) javapro article on debugging servlets (login required)\] ![:\\](/wiki/modernized/img/ohwell.png ":\")

------------------------------------------------------------------------

#### Eclipse External Command \"Snarfing\" Tip 

If you have an app that you run inside eclipse and you want to run it standalone (in a shell), you can get at the launch command that Eclipse uses:

- Go into the Eclipse debug perspective.

- If you don\'t already have a debug session showing for the app (live or terminated), start it up.

- Click on the `+`{.backtick} to expand the debug session (if needed).

- You should see a line like this:
  - \<path to javaw.exe\>\\javaw.exe (\<timestamp\>)

  - Mine is: `C:\apps\j2sdk1.4.2\jre\bin\javaw.exe (Mar 1, 2005 4:24:02 PM)`{.backtick}

- Right-click on this line and select properties.

- You can then swipe/copy the `Command Line`{.backtick} info.

- You can then paste this into your shell. You\'ll typically want to convert the `javaw.exe`{.backtick} to a `java.exe`{.backtick} to receive output to the shell.
