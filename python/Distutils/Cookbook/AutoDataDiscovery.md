# Distutils/Cookbook/AutoDataDiscovery

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# Problem 

Distutils requires that you manually specify each directory and data-file to be included in the distribution. For packages with large and deep sub-package hierarchies it can be a pain to keep this list in sync with the code, particularly as forgetting an entry is not noticable until a user happens to report that a resource is missing.

# Solution 

Use an automatic scanning mechanism to generate the data_files parameter for setup:

    import os
    import imp

    def non_python_files(path):
        """ Return all non-python-file filenames in path """
        result = []
        all_results = []
        module_suffixes = [info[0] for info in imp.get_suffixes()]
        ignore_dirs = ['cvs']
        for item in os.listdir(path):
            name = os.path.join(path, item)
            if (
                os.path.isfile(name) and
                os.path.splitext(item)[1] not in module_suffixes
                ):
                result.append(name)
            elif os.path.isdir(name) and item.lower() not in ignore_dirs:
                all_results.extend(non_python_files(name))
        if result:
            all_results.append((path, result))
        return all_results

Then call it for the directories which contain data-files you want to include.

    data_files = (
        non_python_files('pytable') +
        non_python_files(os.path.join('pytable', 'doc'))
        )

and pass the result to setup:

    setup (
        name = "pytable",
        version = "0.7.7a",
        data_files = data_files,
        cmdclass = {'install_data':smart_install_data},
        **extra_arguments
        )

(See [DistutilsInstallDataScattered](DistutilsInstallDataScattered) for the smart_install_data command.)

You can see a real-world usage example in the [PyTable setup script](http://cvs.sourceforge.net/viewcvs.py/pytable/table/setup.py?view=markup)

# Discussion 

Again, there should be some way to do this with a distutils template processing call or something, but this direct processing approach works well enough. This approach is very similar to [DistutilsAutoPackageDiscovery](./DistutilsAutoPackageDiscovery.html).

------------------------------------------------------------------------

[CategoryDistutilsCookbook](CategoryDistutilsCookbook)
