# Distutils/ManifestPluginSystem

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# Problem 

Right now there are several ways to build the MANIFEST file that comes with a source distribution, besides the scripts.

People tend to use:

- the MANIFEST.in templating system
- a script that scans the (D)VCS structures in order to build the list of files. (setuptools)
- package_data and data_files arguments

Moreover, Distutils will include some elements by default, like README.txt and so one.

There\'s no consensus on what is the good practice yet, but;

- some people don\'t want to use and maintain a MANIFEST.in file. They want an automatic tool.
- you have to combine several techniques when you are dealing with special cases, such as:
- if you use a VCS script, you might want to exclude some files that are listed in your repository. You need to use MANIFEST.in for that.
- if you name explicitely the files in package_data, there are no way to include recursively some directories, and to exclude some files. That is why you also need to use MANIFEST.in
- MANIFEST.in is fine, but doesn\'t provide an automatic way to include elements like a VCS script would.

The problem is that a packager that wants to work with a package might be unable to get the list of files of this package if he doesn\'t work exactly like the author.

Example:

- Bob develops his package using Subversion. He doesn\'t bather about the file list because when he creates his package, it is automatically built using a setuptools script that scans the .svn folder. He works with svn 1.5.
- Bill gets a source distribution, and wants to work on it. He is working with the brand new 1.6 version of Subversion, which is incompatible with the current setuptools VCS script. He is unable to create a source distribution anymore, unless he ask someone else to build the MANIFEST file for him.
- John works with this brand new DVCS, incompatible with Subversion. Unfortunately, no one has written a script in setuptools. Like Bill, he is unable to launch the sdist command because he will probably get a incomplete list of files.

Result :

- Bill and John will have to maintain their own versions of setup.py (and maybe MANIFEST.in) until they merge.

# Proposal 

This proposal does not solve the problem, because it\'s unsolvable. Unless everyone use the same way to list the files, people have to work around. This proposal make Distutils simpler to use, no matter how people build their file list.

Let\'s add in Distutils:

- a generic plugin system in the core
- some plugins to build a file list :
  - a `template`{.backtick} plugin that knows how to build a filelist using the MANIFEST.in templating system

  - a `default`{.backtick} plugin that uses the `template`{.backtick}plugin and do extra things (to provide what Distutils provides today)

  - a `static`{.backtick} plugin, that points to a MANIFEST static file
- a new manifest metadata

## plugin system 

The plugin system is inspired from Setuptools entry points.

Maybe setuptools entry_points code could be added in Distutils, but this section describes the need nevertheless.

Some functions are added in Distutils, in a module called plugins:

- get_plugin(group, name) : returns an object for (group, name)
- register_plugin(group, name, object): register an object, for (group, name)
- unregister_plugin(group, name): removes an object for (group, name)
- list_plugins(group=None, doc=False): returns a list of all objects for the given group.
- list_groups(): return a list of all groups

The filelist module implements a `default`{.backtick} plugin, in the `distutils:filelist`{.backtick} group, that contains the current Distutils algorithm that builds the MANIFEST file:

        >>> register_plugin('distutils:filelist', 'default',
        ...                 distutils.filelist.FileList)

Distutils is refactored in order to use this plugin. For instance the `default`{.backtick} plugin is the `FileList`{.backtick} class. It\'s used by the `sdist`{.backtick} command for example.

The `default`{.backtick} plugin uses another plugin called `template`{.backtick}, that uses the MANIFEST.in templating system:

        >>> register_plugin('distutils:filelist', 'template',
        ...                 distutils.filelist.ManifestTemplate)

Another plugin is also provided, called `static`{.backtick}:

        >>> register_plugin('distutils:filelist', 'static',
                            distutils.filelist.StaticFile)

This plugin allows to provide a path to a simple file that contains the list of file (like a MANIFEST file).

Last, list_plugins(\'distutils:filelist\'), returns a list of all plugins names of a given group:

        >>> list_plugins('distutils:filelist')
        ['default', 'template', 'static']

An optional parameter can be use to get more information:

        >>> list_plugins('distutils:filelist', doc=True)
        [('default', 'Default plugin to get the file list of a package'),
         ('static', 'Returns a file list given a path of a file that contains the list')]

Without parameters, list_plugins() returns all objects.

## How a plugin is called and used ? 

A plugin is called with a in-out argument called `filelist`{.backtick}, an optional `root_path`{.backtick} argument and a list of keywords:

        >>> get_plugin('distutils:filelist', 'default')(filelist, root_path='/somewhere')

If `root_path`{.backtick} is None, the plugin might want to use the current working directory to start his scanning work.

In `sdist`{.backtick}, the plugin is called with the current working directory and all options passed to `sdist`{.backtick}.

## How to choose one or several plugin 

`sdist`{.backtick} will have a new option, called `manifest`{.backtick}, this option is a list of plugin names. If not given, \[\'default\'\] is used by default.

Someone that wants to use another plugin will simply add it in the list:

        >>> setup(name='foo', manifest=['hg'])

He might also want to use several plugins. For instance, build a file list with the `hg`{.backtick} plugin, then exclude some files with the `template`{.backtick} plugin:

        >>> setup(name='foo', manifest=['hg', 'template'])

The `sdist`{.backtick} command will loop over all plugins to build the file list using this simple code::

        >>> def get_filelist():
        ...    filelist = []
        ...    for name in list_plugins('distutils:filelist'):
        ...        plugin = get_plugin(name)
        ...        plugin(filelist)
        ...    return filelist

Each plugin is able to add or remove a file from the file list.

## the manifest metadata 

The manifest metadata already exists in a sense. It\'s not in PKG-INFO itself, but lands into the `.egg-info`{.backtick} directory once it\'s built.

A new display option will allow people to get it without having to call `sdist`{.backtick} or `egg_info`{.backtick}, exactly like `--long-description`{.backtick} provides:

        $ python setup.py --manifest

This will call the `get_filelist()`{.backtick} function and display its result in the standard output.
