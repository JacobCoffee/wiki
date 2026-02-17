# PackageScanning

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

## What is Package Scanning 

Java\'s builtin libraries provide no way to determine what packages are available to a running JVM until they\'ve been loaded. You can ask the JVM to find a class for you with a call to `Class.forName`{.backtick}, but there\'s no equivalent `Package.forName`{.backtick}. To allow code to import packages directly and have functions like dir work on them, Jython scans all the jar files it can find at startup to build the package and class structure available to the JVM.

## How do I control which jars are scanned 

Jython looks at two properties in its registry to try to find jars: `python.packages.paths`{.backtick} and `python.packages.directories`{.backtick}. Each of these should be a comma separated list of further registry entries that actually contain the values the scanner will use to build its listing.

First the `python.packages.paths`{.backtick} registry entry is processed. It defaults to `java.class.path,sun.boot.class.path`{.backtick}. That means that the scanner looks up `java.class.path`{.backtick} then `sun.boot.class.path`{.backtick} in the registry in turn. Each of these \"classpath\" entries is treated like something passed to Java\'s -cp option: it\'s split on the platform\'s path separator and each resulting value is scanned for packages if it ends with \".jar\" or \".zip\".

Then `python.packages.directories`{.backtick} is handled. It defaults to `java.ext.dirs`{.backtick}. Each second-level registry value is treated as a \"directory\" entry. The scanner lists the files in each one, and if a file ends in \".jar\" or \".zip\", it\'s scanned.

To control the jars that are scanned, you need to set the values for those properties in the registry. The registry properties can be controlled by calling `PyInterpreter.initialize(Properties preProperties, Properties postProperties, String[] argv)`{.backtick} with your own `postProperties`{.backtick} object before creating a `PythonInterpreter`{.backtick}. `preProperties`{.backtick} is `System.getProperties()`{.backtick} by default, so it\'s a good idea to pass that in as `preProperties`{.backtick} here too.

## How do I skip scanning jars 

If you only use full class imports, you can skip the package scanning altogether. Set the system property `python.cachedir.skip`{.backtick} to `true`{.backtick} or(again) pass in your own `postProperties`{.backtick} to turn it off.
