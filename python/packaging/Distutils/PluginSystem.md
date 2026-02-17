# Distutils/PluginSystem

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# Example 

This is a generalization of the technique used in setuptools so people can write plugins for commands.

Let\'s take an example: you have a command where you create a list of files to build a file list (a manifest).

You provide a default system to build this list but you know some people will probably provide other strategies to build that list.

So let\'s declare a user option, called \"manifest-makers\", where an ordered list of plugins name can be declared.

We also declare a new attribute called `extensible_options`{.backtick}, to declare the list of options that are used to extend the command.

    class MyCmd(Command):

        user_options = [('manifest-makers', None,
                         'Plugins to build the manifest file')]

        extensible_options = ['manifest-makers']

        def initialize_options(self):
            # this is a regular user option
            self.manifest_makers = ['svn', 'template', 'hg']
            self.files = []

        def finalize_options(self):
            pass

        def run(self):
            # this will build the filelist by running the plugins
            self.run_extension('manifest-makers')

What happened ? In the initialize options, we declared default values for the manifest_makers attribute : three plugins called \'svn\', \'template\' and \'hg\'.

The Command will load these plugins using setuptools entry point called: \"distutils.MyCmd.manifest_makers\". It will load them at the end of the option finalization.

Then, a new API called \"run_extension\" allows MyCmd to run these plugins.

Each plugin receives the command and the name of the option in argument and is free to work over the command and its distribution.

For example, the signature for the svn plugin is :

    def svn(cmd, name):
        # work done here on the command

Read more about how to create plugins with entry points, and what they are, here : [http://lucumr.pocoo.org/2006/7/30/setuptools-plugins](http://lucumr.pocoo.org/2006/7/30/setuptools-plugins)

# Implementation 

- [http://svn.plone.org/svn/collective/collective.releaser/branches/refactor/collective/releaser/commands/extendable.py](http://svn.plone.org/svn/collective/collective.releaser/branches/refactor/collective/releaser/commands/extendable.py)

- [http://svn.plone.org/svn/collective/collective.releaser/branches/refactor/collective/releaser/tests/test_extendable.py](http://svn.plone.org/svn/collective/collective.releaser/branches/refactor/collective/releaser/tests/test_extendable.py)

# Use cases 

Some simple usecase, need solutions with the above design

## Creating a command to build and install documentation 

(by [DavidCournapeau](./DavidCournapeau.html))

A python distribution package foo 1.0 is set-up as follows:

    foo-1.0/setup.py
            foo/__init__.py
            foo/..
            doc/

The documentation is in rest format and can be built by sphinx (e.g. (cd doc && make html)). The author wants to build the documentation automatically, and include it in a sdist-generated tarball. Two commands are needed: build_doc and install_doc.

## Installing a C library meant to be used by other extensions 

(by [DavidCournapeau](./DavidCournapeau.html))

Example: in numpy, some core, portable mathematical routines are built in a pure C library (built through build_clib command). We want to install this library and makes it available to other python packages which are based on numpy. Problems:

- how to install it ? The usual solution is to handle this in the install command. Only build_clib knows where the library is built in the build directory (which is platform dependent and hardcoded in the build_clib command), so the install command has no way to know the location without hacking more into communication between both commands. More fundamentally, it seems very complicated to extend commands to just install one file.
- how to install the corresponding library API declaration (the .h file) in a known location (could be done through install_data, I guess).

## Configuring external dependencies locations 

(by [DavidCournapeau](./DavidCournapeau.html))

Many python packages rely on some external libraries, often written in C/C++. How to detect them if they are installed in a non standard location ? In autoconf, there is a simple mechanism:

    ./configure --with-foo=/some/path 
    (or ./configure --with-foo-include=/some/path/include --with-foo-lib=/some/path/lib)

and the foo header will be looked for in /some/path/include + /some/path/lib for the library. How to add those options to the config command ? How to pass the related information to other commands ?

## Building a ctypes extension 

(by [DavidCournapeau](./DavidCournapeau.html))

A ctypes extension (i.e. a library which can be opened through dlopen/LoadLibrary/etc\...) cannot be built with ctypes in a portable manner ATM. The problem is that some link options are different compared to a python extension (on windows in particular, where the symbols to export through /EXPORT are not the same). The compiler classes are too difficult to use/extend in their current state (they don\'t have the same interface, they sometimes fail for mysterious reasons, in particular the MSVCCompiler class which has not the same interface as the UnixCCompiler class).

How to write a build_ctypes command ?

## Controlling compiler flags 

(by [DavidCournapeau](./DavidCournapeau.html))

Sometimes, it is needed to control compiler flags. For example, gcc offer a very useful variety of warning flags which are not always enabled, or we may want to add option for profiling/debugging/code coverage/etc\... There is also the problem that different source files may need different compilation options.

## Conditionally controlling compiler flags 

(by [FlorisBruynooghe](./FlorisBruynooghe.html))

As above, but only conditionally enable them with a command line option or in a configuration file. This way only a developer can easily enable flags like -Werror while a user won\'t be doing this. (Sorry it wasn\'t clear to me if the above included this or not)
