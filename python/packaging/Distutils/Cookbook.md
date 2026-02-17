# Distutils/Cookbook

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

## Introduction 

The Distutils Cookbook collects various useful recipes and tips for using the Distutils.

When creating new recipes, use the [RecipeTemplate](RecipeTemplate).

## Recipes 

- [/InstallDataScattered](Cookbook/InstallDataScattered) \-- make resource data-files get installed in the same directory tree as the Python files that depend on them

- [/AutoDataDiscovery](Cookbook/AutoDataDiscovery) \-- specify data-files to install with smart_install_data recursively by specifying only a top-level directory

- [/AutoPackageDiscovery](Cookbook/AutoPackageDiscovery) \-- specify packages to install recursively by specifying only the top-level package

- [/WininstFilename](Cookbook/WininstFilename) \-- provide customisation point for altering the filename of bdist_wininst installer (such as to include numpy version information)
