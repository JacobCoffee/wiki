# Distutils/Cookbook/InstallDataScattered

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# Problem 

Distutils standard install_data doesn\'t automatically store resource-files in the same location as Python source-code files. This tends to break the assumptions of packages which expect to find their resource files in the same relative location to their source-code files. Since most data-files being packaged with a Python package really are resources on which code depends (not mere data-files) this can be a pain.

To see the effect, try installing a library that specifies data-files while specifying \--install_lib=somewhere. The data-files will still be installed to site-packages while the Python files show up in \"somewhere\".

# Solution for Python 2.3 

Sub-class install_data and tell it to use the install_lib directory as its root install directory.

    from distutils.command.install_data import install_data
    class smart_install_data(install_data):
        def run(self):
            #need to change self.install_dir to the library dir
            install_cmd = self.get_finalized_command('install')
            self.install_dir = getattr(install_cmd, 'install_lib')
            return install_data.run(self)

then specify that the command class for \'install_data\' is to be smart_install_data:

    setup (
        name = "pytable",
        version = "0.7.7a",
    ...
        cmdclass = {'install_data':smart_install_data},
        **extraArguments
    )

This code was created by Pete Shinners (of [PyGame](PyGame) fame).

You can see a real-world usage example in the [PyTable setup script](http://cvs.sourceforge.net/viewcvs.py/pytable/table/setup.py?view=markup)

Note that in Python 2.4 and newer, you\'ll be able to use the \'package_data\' keyword to the \'setup\' function to install data in packages without having to clobber the normal install_data command.

# Solution for Python 2.1 and 2.2 

For some obscure reason, the solution above does not work with Python 2.2 (or 2.1), even if the distutils code of Python 2.3 is used with Python 2.2. To make things worse, Python 2.1 and 2.2 will install data_files to /usr/package instead of /usr/lib/python2.x/package.

See [this posting](http://groups.google.de/groups?as_umsgid=f70e3538.0404141327.6cea58ca@posting.google.com) for a solution that will work with every Python version.

# Discussion 

If you want to be able to use resources reliably even in the presence of Py2exe or similar packaging schemes (which aren\'t helped by this recipe), you might want to try [ResourcePackage](./ResourcePackage.html). [ResourcePackage](./ResourcePackage.html) automatically embeds resources in Python packages/modules so that they are treated as Python code by the various packaging mechanisms.

------------------------------------------------------------------------

[CategoryDistutilsCookbook](CategoryDistutilsCookbook)
