# ReplaceJythonc

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

jythonc doesn\'t handle generators and is difficult to debug and improve. The current thinking is to add capabilites to jython itself to generate bytecode from py files and run those statically compiled items rather than jythonc\'s approach of making Java classes that work like the base Python code. The current thinking runs as follows:

- Turn Python classes into Java classes without a Java interface or class using function annotations to specify the static Java type information
- statically compile proxy classes for Python classes that extend Java classes
- remove code from core that is only there to support jythonc

The annotation goes on any method in a Python class that needs to be visible from Java and `__init__`{.backtick} for the constructor. Given the following annotated Python class

:::: 
::: 
``` 
class Simple(object):
  @java
  def __init__(self):

  @java(String, String)
  def firstWord(self, param):
    return param.split(' ')[0]
```
:::
::::

Java bytecode corresponding to

:::: 
::: 
``` 
public abstract class Simple {

    public Simple(){}

    public abstract String firstWord(String);

}
```
:::
::::

is generated. This is starting to be implemented in [The clamp project](https://github.com/jythontools/clamp/) .

\[wwolff - Nov 08\] An important use-case for jythonc is for generating Java Applets that can run in Web Browsers. The approach described here sounds excellent because it would mean less special Jython related code. A big problem with jythonc 2.2.1 is a Jython applet needs to have a special policy file to allow it to run in a browser. That defeats the main point of an applet\--automatically running without any installation.

\[adiroiban - Oct 10\] You can use \'jython -m compileall path/to/your/jython/files\' to create \$py.class

\[pakin - Nov 23\] How can I run the result of \'jython -m compileall\'? No matter what I try, java gives me a \'Could not find the main class\' error.
