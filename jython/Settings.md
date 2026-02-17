# Settings

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# Methods of specifying Jython settings 

- `preProperties`{.backtick}, typically Java system properties specified with `-D`{.backtick} **before** class/jar specification on Java command line

- Registry: property files `registry`{.backtick} in Jython root and `.jython`{.backtick} in `user.home`{.backtick}; if both are present, the latter replaces the former completely. If either is present, the Java system properties are replaced entirely. (This is likely a bug in `PySystemState.addRegistryFile`{.backtick}.) See [Finding the Registry File](http://www.jython.org/Project/userguide.html#finding-the-registry-file) for more information.

- `postProperties`{.backtick}, typically Jython properties specified with `-D`{.backtick} **after** class/jar specification on Java command line (these overwrite Java system properties, too.)

For `preProperties`{.backtick} and `postProperties`{.backtick}, alternate properties may be passed to `PySystemState.initialize`{.backtick} or `PythonInterpreter.initialize`{.backtick} by programmatic users of Jython.

The runtime registry (`PySystemState.registry`{.backtick} from Java, or `sys.registry`{.backtick} from Python) is created from the above three sources.

Other command-line arguments are written directly into Options static variables without going through the properties system; the overlapping properties are `python.divisionWarning`{.backtick}, `python.options.Qnew`{.backtick} and `python.verbose`{.backtick}. In these overlapping cases, the above three sources always take precedence over the command-line equivalents. (This precedence should likely be reversed.)

## Documentation 

- The options whose destinations are static variables in the `Options`{.backtick} class are well-documented [there](https://jython.svn.sourceforge.net/svnroot/jython/branches/asm/src/org/python/core/Options.java).

- The [default registry file](https://jython.svn.sourceforge.net/svnroot/jython/branches/asm/registry) is severely bitrotted and needs redoing.

- The [Jython user guide](http://www.jython.org/Project/userguide.html#the-jython-registry) refers to a subset of these properties.

::: {}
  --------------------------------------------------------------------------------------- ---------------------------------------------------------------------------- -----------------------------------------------------------------------------------
  Source                                                                                  Destination                                                                  Default
  install.root                                                                                                                                                         
  python.cachedir                                                                         [PySystemState](./PySystemState.html).cachedir = File(\...)    \"cachedir\"
  python.cachedir.skip                                                                    [PySystemState](./PySystemState.html).cachedir = null          true if standalone, else false
  python.collections                                                                      [PyInstance](./PyInstance.html).initializeIterators            \"\"
  python.console                                                                          jython.main                                                                  \"org.python.util.[InteractiveConsole](./InteractiveConsole.html)\"
  python.console.encoding                                                                 [CompilerFlags](./CompilerFlags.html).encoding                 
  python.console.readlinelib                                                                                                                                           
  python.deprecated.keywordMangling                                                       Options.deprecatedKeywordMangling                                            false
  python.divisionWarning                                                                  Options.divisionWarning                                                      
  python.executable                                                                       [PySystemState](./PySystemState.html).\[default\]Executable    set by launcher script, else null
  python.home                                                                             [PySystemState](./PySystemState.html).\[exec\_\]prefix         set by launcher script, else \".\"
  python.modules.builtin                                                                  [PySystemState](./PySystemState.html).builtin_module_names     \"\"; appended to Setup.builtinModules
  python.options.Qnew                                                                     Options.Qnew                                                                 false
  python.options.caseok                                                                   Options.caseok                                                               false
  python.options.compileClass                                                             *unused; in default registry file*                                           false (in registry file)
  python.options.includeJavaStackInExceptions                                             Options.includeJavaStackInExceptions                                         true
  python.options.internalTablesImpl                                                       [InternalTables](./InternalTables.html).createInternalTables   null
  python.options.proxyDebugDirectory                                                      Options.proxyDebugDirectory                                                  null
  python.options.showJavaExceptions                                                       Options.showJavaExceptions                                                   false
  python.options.showPythonProxyExceptions                                                Options.showPythonProxyExceptions                                            false
  python.os                                                                               os.\_name                                                                    \"posix\"
  python.packages.directories                                                             [SysPackageManager](SysPackageManager).findAllPackages                \"java.ext.dirs\" (see [PackageScanning](PackageScanning))
  python.packages.fakepath                                                                [SysPackageManager](SysPackageManager).findAllPackages                null
  python.packages.paths                                                                   [SysPackageManager](SysPackageManager).findAllPackages                \"java.class.path,sun.boot.class.path\"
  python.path ![{X}](/wiki/modernized/img/icon-error.png "{X}")   end of path after JYTHON_JAR/Lib                                             \"\"
  python.prepath (python.path in r5043+)                                                  beginning of path after current dir                                          \"\"
  python.security.respectJavaAccessibility                                                Options.respectJavaAccessibility                                             true
  python.verbose                                                                          Options.verbose                                                              Py.MESSAGE = 1
  python.xml.sax.parser                                                                   xml.sax.default_parser_list (split)                                          PY_SAX_PARSER, else xml.sax.drivers2.drv_javasax
  --------------------------------------------------------------------------------------- ---------------------------------------------------------------------------- -----------------------------------------------------------------------------------
:::

![{X}](/wiki/modernized/img/icon-error.png "{X}") gone in Jython 2.5 or later
