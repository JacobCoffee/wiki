# Distribute/Functionality

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# Functionality 

setuptools does many things. Breaking that down into different areas will allow people to contribute to a smaller chunk that they feel familiar with and excited about.

::: {}
  --------------------------------------------------------------------------------------
  Note! This is the early stages of this. Feel free to brainstorm or organize at will.
  --------------------------------------------------------------------------------------
:::

## metadata

This is the metadata about the package that\'s stored in the egg

### Ideas 

- Enhance metadata with an API/ABI version (ABI would mean, changes to file formats and such)
- Storage of metadata and data with the same API is not great as there\'s different storage requirements for each.
- API for extracting the metadata?
- Script interface to do the same

## egg format 

This is the format of metadata + code + data that is zipped up into an egg.

## pkg_resources: Library Dependency Manager 

This is the functionality that loads libraries of certain versions and runs them,

### Ideas 

- Be able to both control version choices programmatically and have a default version
- Properly handle overlapping dependencies

## pkg_resources: Resource Manager 

Allow code to import data from an unknown and variable location on the disk.

[http://peak.telecommunity.com/DevCenter/PkgResources#resourcemanager-api](http://peak.telecommunity.com/DevCenter/PkgResources#resourcemanager-api)

### Ideas 

- Ability to retrieve data from outside of the Module ([EggTranslations](./EggTranslations.html))

- General data store

- Ability to access data in different locations per platform and install method

## easy_install

Tool that downloads and installs all the dependencies of a package

## build

Tool that makes building and installing from source easier

### Ideas 

- Able to install to FHS locations or build eggs as desired
- bdist\_\* and install should all be terminal targets. bdist\_\*, for instance, should not depend on install having been run first.
