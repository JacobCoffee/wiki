# Distutils/Cookbook/AutoPackageDiscovery

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# Problem 

Distutils requires that you manually specify each package to be included in the distribution. For packages with large and deep sub-package hierarchies it can be a pain to keep this list in sync with the code, particularly as forgetting an entry is not noticable until a user happens to report that an entire sub-package is missing.

# Solution 

Use an automatic sub-package scanning mechanism to generate the package_dir and packages parameters for setup:

    import os

    def is_package(path):
        return (
            os.path.isdir(path) and
            os.path.isfile(os.path.join(path, '__init__.py'))
            )

    def find_packages(path, base="" ):
        """ Find all packages in path """
        packages = {}
        for item in os.listdir(path):
            dir = os.path.join(path, item)
            if is_package( dir ):
                if base:
                    module_name = "%(base)s.%(item)s" % vars()
                else:
                    module_name = item
                packages[module_name] = dir
                packages.update(find_packages(dir, module_name))
        return packages

Then call `find_packages` to get the set of packages to be included (note that this call assumes that the packages are sub-directories of the directory where setup.py resides).

    packages = find_packages(".")

Then use `packages` as the source within your call to setup:

    setup (
        name = "pytable",
        package_dir = packages,
    #...
        packages = packages.keys(),
        **extra_arguments
        )

You can see a real-world usage example in the [PyTable setup script](http://pytable.cvs.sourceforge.net/pytable/table/setup.py?view=markup)

# Discussion 

There should be some way to do this with distutils own machinery, I just don\'t know what it would be.

Idea: Giving "packages=\[\'egg\', \'ham\'\]" should be enough for Distutils2 to include the egg and ham packages and their subpackages, using a function similar to Setuptools/Distribute find_package (or the one written here). merwok

------------------------------------------------------------------------

[CategoryDistutilsCookbook](CategoryDistutilsCookbook)
