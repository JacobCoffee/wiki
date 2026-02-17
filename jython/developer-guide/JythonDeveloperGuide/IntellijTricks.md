# JythonDeveloperGuide/IntellijTricks

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# Intellij IDEA Tricks 

This page describes useful tricks for Intellij IDEA users. If you haven\'t created an Intellij project for Jython yet, see [JythonDeveloperGuide/IntellijNotes](IntellijNotes).

## Eclipse Code Formatter 

Configuring the [CodingStandards](CodingStandards) by hand is an annoying task. Fortunately there is a plugin to import Eclipse code formatting rules into Intellij IDEA: Eclipse Code Formatter. It is available in the plugin repository.

The Eclipse Code Styles file is attached to the [CodingStandards](CodingStandards) page.

Eclipse Code Formatter can be configured under *Settings* (shortcut: ctrl + alt + s) \--\> *Eclipse Code Formatter*

## Running Jython and JUnit tests inside IDEA 

General *Run/Debug Configurations* settings:

::: {}
  --------------------- ---------------------------------------------------------------------------------------------------------------------
  Parameter Name        Value
  VM options            *-Dpython.home=dist -Dpython.console=org.python.util.[InteractiveConsole](./InteractiveConsole.html)*
  Working directory     project basedir
  Classpath of module   *jython-trunk*
  --------------------- ---------------------------------------------------------------------------------------------------------------------
:::

### Jython 

Configuration Type: **Application**

Additional parameters:

::: {}
  ------------------------------ ----------------------------------------------------------
  Parameter Name                 Value
  Main class                     *org.python.util.jython*
  Program arguments (optional)   Parameters for Jython, e.g. the python module to execute
  ------------------------------ ----------------------------------------------------------
:::

#### Example: Regression Tests 

Running the regression tests in IDEA is interesting for at least two reasons:

1.  Code Coverage
2.  Debugger

![JythonRegressionTestConfiguration.jpg](attachments/JythonDeveloperGuide(2f)IntellijTricks/JythonRegressionTestConfiguration.jpg "JythonRegressionTestConfiguration.jpg")

See *regrtest.py* for detailed information about additional program arguments.

### JUnit tests 

Configuration Type: **JUnit**

Additional parameters:

::: {}
  ------------------------------ ----------------------------------------------------------
  Parameter Name                 Value
  Main class                     *org.python.util.jython*
  Program arguments (optional)   Parameters for Jython, e.g. the python module to execute
  ------------------------------ ----------------------------------------------------------
:::

#### Example: \_ioTest 

![JythonJUnitConfiguration.jpg](attachments/JythonDeveloperGuide(2f)IntellijTricks/JythonJUnitConfiguration.jpg "JythonJUnitConfiguration.jpg")
