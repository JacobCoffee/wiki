# Distutils/Proposals/DependencySupport

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# Distutils-based Dependency Support

::: 
### Vision

We want to create a means whereby a package author can create a distutils-based package distribution that can automatically download and install the other distutils-based packages that the author\'s package requires. This mechanism must *not* require that a depended-on package explicitly support it. In other words, a newly created package should be able to depend on any existing distutils-based source distribution. (Being able to use binary distributions to satisfy dependencies is also desirable, but support of all possible binary formats should not be a sprint goal.) The means created should work with Python 2.2, must not require a modified distutils, and must be distributable by the packager so that the end user sees only the standard `setup.py`-based installation process.

Whatever mechanism used to denote and process dependencies should be isolated as a library for reuse by other tool efforts, such as user-friendly package management tools. However, the package management tools themselves aren\'t the sprint goal, because these can be written independently. The \"simplest thing that could possibly work\" here is to give package authors a tool they can use to make their dependencies easy to install.
:::

::: 
### Intended Uses

- break up monolithic systems (PEAK, Zope, Twisted) into smaller package sets with dependencies
- allow dependencies on other systems (e.g. Twisted using PyProtocols, PEAK using zope.publisher, etc.)
- support painless install for end users (single command to download and install \"everything needed\") even at the cost of a little pain for the packager(s).
:::

::: 
### Non-Goals

- This is not an effort to develop an ultimate metadata format, repository, or best way to sign code
- This is not a bitch session about how distutils and PyPI aren\'t CPAN
- PEP 262 should be orthogonal to this effort, since we will be using standard distutils to do installations.
- \"uninstall\" is out of scope
:::

:::::: 
### Implementation Notes

What would be the \"simplest thing that could possibly work\"? We could have a function to download and install a source distribution from a given URL, and `setup.py` could simply call that function once for each dependency.

But that wouldn\'t work very well if someone ran setup.py more than once, and would be wasteful of time and bandwidth if the dependencies were already installed. So, we could have the setup script check if each dependency was already installed, before installing it. That would prevent the redundant installation if the script was re-run, or if the dependencies were already present.

This would not work very well, however, in situations where the user was not installing to the standard location, or indeed using any non-standard options at all. Duplicating the determination of this information wouldn\'t be a good idea. And simply copying `sys.argv` to pass to a subprocess won\'t work either, because the parent script might be being run for say, an \"sdist\" command, which would produce very silly results when applied to a dependency.

So, dependency installation needs to become a part of the distutils command structure, via the custom commands mechanism. Specifically, we could create a `get_dependencies` command, that was added to a custom version of the `build` command. In this way, only during building would we download and install dependencies. We need this to be done before building anything else, because the dependency might contain C header files that the parent package needs in order to compile extensions.

But there\'s still a problem; the `build` command doesn\'t have all of the knowledge that the `install` command would have about the target installation location and so on. So, a `get_dependencies` during `build` could only download, extract, and build the dependencies. It would not be able to install them without manual intervention \-- which means that it would not be able to build the parent package.

Of course, the scenario of depending on C header files probably isn\'t all that common. So, perhaps the simplest thing to do would be to:

1.  explicitly designate build-time dependencies, as distinct from run-time dependencies, and/or
2.  trick the parent package\'s build process to use header files from the `build/` directory of the dependency

Dependencies that are \"build-time\" would then stop the build process of the parent if the dependency is not installed.

So, now it seems we would have at least two custom commands: `build_dependencies` and `install_dependencies`. We might also have `fetch_dependencies` and `extract_dependencies` commands, but it would probably be better to make fetching and extraction be responsibilities of objects representing the dependencies, thereby making it easier to have specialized installation mechanisms. (For example, someone could potentially write a dependency class to install a needed non-Python library or tool.)

Where would dependencies be downloaded? Built? Perhaps we could create a `deps/` subdirectory, similar to the `build/` subdirectory. Dependent packages would be downloaded there, and a subdirectory created for each one. Extraction would take place in that subdirectory. So, if we were building PyProtocols as a dependency, it would be downloaded as `deps/PyProtocols-0.9.2.tar.gz`, and it would be extracted in `deps/PyProtocols-0.9.2`. This would result in a `setup.py` being located at `deps/PyProtocols-0.9.2/PyProtocols-0.9.2/setup.py`. While the double level of directories would be redundant for distutils packages, the extra directory would make the directory structure safe for extracting non-distutils dependencies as well.

So how do we run the subcommands? There\'s a `distutils.core.run_setup()` function that could be used to run the child setup scripts, after first changing to the subdirectory. However, if a dependency expects to import anything special in its setup script (i.e. it depends on `sys.path` including the setup directory), it will not work. This strongly suggests that running dependencies\' setup scripts in a subprocess is the best way to ensure complete compatibility with all existing distributed packages.

So, can we just pass our `sys.argv` to the child process? Tentatively, yes. There are only two ways this could foul up the child\'s configuration:

1.  files or directories were specified on the command line using relative paths
2.  the user edited the parent package\'s setup.cfg to specify options.

Both of these issues could be fixed by regenerating a custom command line from the actual finalized command options for the parent distribution. But it\'s not clear whether that\'s worth it. During the sprint, we may just want to use the parent `sys.argv`, and isolate it in a `get_setup_argv()` method for future enhancement.

::: 
#### What options should be passed to a dependency\'s `setup.py`?

After more review of how distutils options and commands work, it seems that it would be best to pass only a specifically determined subset of options to dependency setup scripts. These would include:

- installation directory options and byte-compiler options for the `install` command
- non-directory options for the `build` command (such as what compiler to use)
- global options for verbose/dry-run (should we download and run the dependencies if it\'s a dry run?)

We can\'t just use the standard `finalize_options()` idiom to get these options from other commands, because of quirks in how the `install` command processes its options. Indeed, it seems the only `install` options we can reasonably support are:

- `prefix`
- `exec-prefix`
- `home`
- `install-base`
- `install-platbase`
- `root`
- `optimize`
- `force`

We can ensure that the ones that specify directories are absolute, and we can get them all in raw form from the `Distribution` object\'s `command_options` dictionary, including any options that were set by editing `setup.cfg`. The same is true for options to `build`, and we can reasonably support:

- `compiler`
- `debug`
- `force`

We should probably track these options for subcommands like `build_lib` and `install_lib`, although I\'m not sure we want to support such fine-grained option settings passing through to dependencies. We do, however, want to abort if any unsupported options are supplied to any of the build/install commands or their subcommands, telling the user to run just the dependency command with appropriate options, or to run a `show_deps` command and manually install the dependencies. (That is, we should abort if there are any dependencies we\'ll need to install to complete a current command.)
:::

::: 
#### Dependency and Distribution Objects

Dependency objects should be able to:

- Check whether they are installed/up-to-date (probably via a function supplied to the constructor, or in the common case some metadata like the name of a module or module contents to import, or perhaps the module location of a version string to check, and the expected version.)

  What about edge cases, where importing a module (particularly an extension) can have gnarly side-effects? Do we build an easy way to spawn a python interpreter and acquire the result of this check, or do we force module authors to fix things such that importing them is safer?

  > This could be handled by regular expression matches or file-size checks against expected filenames relative to `sys.path`. Dealing with binary extensions would be a bit tricky, but still doable.

- Select an appropriate \"distribution\" of the dependency (probably by selecting the first distribution that can be used on this platform)

Distribution objects should be able to:

- Know whether they can be used on the current platform

  (For example, a `win32.exe` distribution should know it can only be used on a Win32 machine, and a `tar.gz` distribution should know it needs a working `zlib` to be extracted. And it should be able to explain *why* it can\'t be used, so that the dependency can explain why it couldn\'t find a suitable distribution if no other distribution suffices.)

- Download themselves to a designated location, optionally verifying size and checksum

- Extract themselves to a designated location

- Install themselves, given some parameters (???)

For convenience\'s sake, it should be possible to make a single call to create a dependency with a single distribution. For example, one might simply provide a list of URLs to the `Depenency` constructor that specify the distribution(s). The dependency would convert any non-distribution objects in the list by looking up file suffixes in a mapping to determine the dependency class to create.

Finally, by subclassing `distutils.core.Distribution` to add a `requires` attribute, we\'ll be able to supply a `requires` keyword to `setup()` in the parent distribution.
:::

::: 
#### Compatibility with other Distutils Extensions

One potentially tricky issue is combining the dependency support with other distutils extensions. For example, PEAK and PyProtocols add extra commands like `test` to install the software and run unit tests, `happy` to run HappyDoc and build an HTML API reference, a modified `install_data` command that installs data in package directories, and so on. Zope 3 uses custom extensions to do a similar `install_data` fakeout, among other tasks.

It may be that what we end up with, or want to end up with, is a `setuptools` mini-package for bundling with distributions that want these features. We could then bundle in some of the more useful commands such as `test` and perhaps an `install_package_data`. And, the package could hack `distutils.command.__path__` to also check the `setuptools` package. Thus, any new commands supplied by `setuptools` would be available without explicitly adding them. Existing commands would have to be explicitly overridden in the `cmdclass` argument to setup, or initialized via `self.cmdclass.setdefault()` in our custom `Distribution` class\'s `__init__`.

(Update: I\'ve begun a draft version of the setuptools package at [http://cvs.eby-sarna.com/PEAK/setuptools/](http://cvs.eby-sarna.com/PEAK/setuptools/) \-- it does the command path extension, and implements installation of package data in a way similar to that used by Zope X3 and ZConfig, but with full distutils integration so that the \"installed files\" list will be accurate. It also adds a `test` command for running unit tests. By the time of the sprint, I will probably also add a draft version of a `get_dependencies` command with some stub classes for dependencies that print \"This is where I would download\" or \"This is where I would install\". \-- PJE)
:::
::::::

::: 
### Sprinting Strategies/Notes

- How can we create tests? What will we test? Unit testing of Dependency, Distribution, et al will probably be easy, but integration testing of the distutils-connected parts may be rather \"interesting\", to say the least.
- We should probably plan ahead what scenarios we\'d like to have working, e.g.:
  - Have PEAK separately download and install PyProtocols and ZConfig, instead of bundling them
  - Tinker with the `mechanize.browser` distribution so it can download and install `ClientCookie`, `ClientForm`, and so on.
  - Something with binary install for win32
:::

::: 
### Committed Participants

- Anthony Baxter
- Fred Drake
- Bob Ippolito
- John Landahl

PJE was unable to secure funds and time off to make it in person, but will continue to help with pre-sprint research, design, and coding. Cory Dodt has also expressed a desire to participate, but also will be unable to attend.
:::

::: 
### Schedule

TBD; Fred suggests Monday/Tuesday (but is somewhat flexible, while trying to juggle too many sprints in just 4 days)
:::
