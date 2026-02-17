# InstallationDetails

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

**Contents**

## Installation 

To start the installation, please proceed as follows:

- download the installer .jar file and save it locally ([Download](http://www.jython.org/Project/download.html))

- double-click this .jar file , or type: `java -jar jython_installer-2.2.jar`{.backtick}

This will bring up the GUI installer (BROKEN LINK [A bit older Screen shots, reflecting 2.2](http://homepage.sunrise.ch/mysunrise/ohumbel/HEAD/install-HEAD.html)).

On true headless systems, the installer will automatically switch to console mode. You can force console mode using the `--console`{.backtick} switch:

- `java -jar jython_installer-2.2.jar --console`{.backtick}

For command line aficionados, there is also a silent mode, which requires at least the target directory:

- `java -jar jython_installer-2.2.jar -s -d /usr/lib/jython-22`{.backtick}

## Generation of start scripts 

On Windows, the installer creates a `jython.bat`{.backtick} and a `jythonc.bat`{.backtick} file. On all other platforms, it creates a `jython`{.backtick} and `jythonc`{.backtick} file, which are unix like shell scripts. If you have installed a shell on Windows (like cygwin, for example), the installer in addition will create unix like shell scripts.

These scripts have been tested on a wide range of platforms. Please let us know if you need different scripts on a specific platform.

## Troubleshooting 

If one of the GUI steps should appear empty, or with no text visible: Please try to press **Previous** and then **Next** again.

The GUI which appears when pressing the **Browse** button in selecting the target directory might be a bit confusing. Some tips and tricks:

- It uses the standard `javax.swing.JFileChooser`

- Open / select of a directory: There are different L&F\'s on different platforms - just play a little to get used to yours

- The icon for creation of a new directory is sometimes greyed out, although java would have the rights to create one. If this happens, select the parent directory and then try to type in the name of the new directory in the input field. The installer then will create the new directory, if possible

If all else fails, try using silent or console mode.

## A list of all the options 

    $ java -jar jython_installer-2.2.jar --help
    usage:
           java -jar jython_installer-2.2.jar [-c | -s | -A] [-d dir] [-t type] [-i
           part(s)] [-e part(s)] [-j dir] [-v] [-h | -?]

    No option at all will start the interactive GUI installer, except:
    Options respected in GUI mode are 'directory' and 'jre', which serve as
    default values in the wizard.
    In non-GUI mode the following options are available:
    .
     -c,--console             console based installation (user interaction)
                              any other options will be ignored (except 'verbose')
     -s,--silent              silent installation (without user interaction)
     -A,--autotest            automatic stress tests for the installer
                              most of the other options are ignored
                              allowed additional options: 'verbose', 'jre'
     -d,--directory <dir>     target directory to install to
                              (required in silent mode,
                              used as default in GUI mode)
     -t,--type <type>         installation type
                              one of the following types is possible
                              (see also include/exclude parts):
                              - all: everything (including src)
                              - standard: core, mod, demo, doc,
                              standard is the default
                              - minimum: core
                              - standalone: install a single, executable .jar,
                              containing all the modules
     -i,--include <part(s)>   finer control over parts to install
                              more than one of the following is possible:
                              - mod: library modules
                              - demo: demos and examples
                              - doc: documentation
                              - src: java source code
     -e,--exclude <part(s)>   finer control over parts not to install
                              more than one of the following is possible:
                              - mod: library modules
                              - demo: demos and examples
                              - doc: documentation
                              - src: java source code
                              (excludes override includes)
     -j,--jre <dir>           home directory of the runtime jre or jdk
                              (executables are assumed in the /bin subdirectory)
                              select this if you want to run Jython with a
                              different java version than the installation
     -v,--verbose             print more output during the installation
                              (also valid in GUI and autotest mode)
     -h,--help                print this help (overrides any other options)
     -?                       print this help (overrides any other options)

    example of a GUI installation:
            java -jar jython_installer-2.2.jar

    example of a console installation:
            java -jar jython_installer-2.2.jar -c

    example of a silent installation:
            java -jar jython_installer-2.2.jar -s -d targetDirectory

    examples of a silent installation with more options:
            java -jar jython_installer-2.2.jar -s -d targetDirectory -t minimum -i src -j javaHome
            java -jar jython_installer-2.2.jar -s -d targetDirectory -t standard -e demo doc
                     -i src -j javaHome -v

    example of an autotest installation into temporary directories:
            java -jar jython_installer-2.2.jar -A
            (make sure you do NOT touch mouse NOR keyboard after hitting enter/return!)

    example of an autotest installation, using a different jre for the start scripts:
            java -jar jython_installer-2.2.jar -A -j javaHome -v
            (make sure you do NOT touch mouse NOR keyboard after hitting enter/return!)
