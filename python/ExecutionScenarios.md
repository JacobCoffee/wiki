# ExecutionScenarios

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

Scenes (scenarios, user stories, \...) of program execution with Python.

\<insert hangman picture here\>

Core Subprocess \"features\" to watch for:

- child exception propagation if executing Python script ([http://docs.python.org/2/library/subprocess.html#exceptions](http://docs.python.org/2/library/subprocess.html#exceptions))

- check_call() or check_output() return exception on non-zero exit code (other functions do not)

#### Fire and Forget 

##### Crossplatform shell automation 

I am a user, who tired of writing shell commands by hand, and wants a crossplatform way of executing them on Window/Linux/Mac OS. I don\'t care about security - I am my own evil Pinocchio.

1\. \"i only care that the program is successfully started\"\
Algorithm:

- execute the command
- get the signal that it is successfully started (no \'command not found\' error)
- detach and let the process live its own live

**subprocess way**

    subprocess.Popen(command, shell=True)

Problems:

- type of `command`{.backtick} argument affects crossplatform behavior

  - \[ \] here should be a table of `shell=True`{.backtick}, typeof(command), unix, windows, mac os

- child Python exceptions: affected\|unaffected

#### Libraries on Execution 

- [http://amoffat.github.com/sh/](http://amoffat.github.com/sh/) - avoids suprocess altogether, linux-only for now

#### Notes about bad design in subprocess 

check_call() or check_output() are shortcuts for executing Popen calls (convenience functions), but they modify the error handling behavior, leading to new exceptions when return codes are not the same. There is a also a call() helper that doesn\'t add new exceptions in this case and repeats Popen behaviour. This is what is called \"inconsistent design\" of API.

The check\_\* in the names of the helpers is probably because of those added exceptions, but that\'s not obvious. Names became non-friendly for humans. There might be a good rational user story behind this change, but it is missing in the context of this API, so as a user, I don\'t have a chance to memorize the conditions, when this can be handy. Defining the conditions is the goal of writing this page.
