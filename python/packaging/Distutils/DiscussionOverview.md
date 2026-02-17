# Distutils/DiscussionOverview

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

### Python packaging discussion 

The way packaging in Python works is currently undergoing big changes. This page tries to summarise the discussion, proposals and ideas that might be incorporated into the PEPs listed below.

If you have an idea, or a use case that is not (sufficiently) supported right now, we would like to know about it and encourage you to add it to the [Ideas & Use cases](./Distutils(2f)DiscussionOverview.html#ideas) section of this page. See also the older [proposals](./Distutils(2f)Proposals.html).

### PEPS 

List of packaging related PEPs that are under consideration:

- [PEP 345 - Metadata for Python Software Packages 1.2](http://www.python.org/dev/peps/pep-0345/)

- [PEP 376 - Changing the .egg-info structure](http://www.python.org/dev/peps/pep-0376/)

- [PEP 382 - Namespace Packages](http://www.python.org/dev/peps/pep-0382/)

- [PEP 386 - Changing the version comparison module in Distutils](http://www.python.org/dev/peps/pep-0386/)

- [PEP 390 - Static metadata for Distutils](http://www.python.org/dev/peps/pep-0390/) Obsoleted by acceptance of PEP 345 which provides field names and format. A concrete syntax proposal is being worked on. See also [StaticMetadata](./StaticMetadata.html) (not yet up to date with respect to the syntax proposal).

### Proposals 

## Accepted 

## Under consideration 

- [Prefix handling for installed files](./Distutils(2f)DiscussionOverview.html#fileprefixes)

- [Prefix classes](./Distutils(2f)DiscussionOverview.html#prefixclasses)

- [Change default installation scheme](./Distutils(2f)DiscussionOverview.html#defaultscheme)

- [User defined prefixes](./Distutils(2f)DiscussionOverview.html#userprefixes)

### Ideas & Use cases 

## Data file installation paths 

It is not possible to retrieve the installation paths of data, or other, files for all installation schemes supported by distutils right now. I propose the inclusion of a PREFIX file within the .egg-info directory that holds information on all prefixes set at installation time and a suitable API within pkgutil.

**Discussion**: [Distutils/DiscussionOverview/FilePrefixes](./Distutils(2f)DiscussionOverview(2f)FilePrefixes.html)

**Status**: Under Consideration

**Affected PEPs**: 376

## Data file prefix classes/placeholders 

Data files shipped within a distribution are not further classified. This makes it impossible to define default installation paths for certain file types that are typically shipped with a distribution like configuration files, examples, shared data files, \...

**Discussion**: [Distutils/DiscussionOverview/PrefixClasses](./Distutils(2f)DiscussionOverview(2f)PrefixClasses.html)

**Status**: Under Consideration

**Affected PEPs**: 376

## Change the default installation scheme 

Distribute packaged distributions get installed into paths that are typically under the aegis of the system\'s package manager. I propose to change the default installation scheme to the (PEP 370) `--user`{.backtick} one.

**Discussion**: [Distutils/DiscussionOverview/DefaultInstallScheme](./Distutils(2f)DiscussionOverview(2f)DefaultInstallScheme.html)

**Status**: Under Consideration

**Affected PEPs**: None

## User defined prefix identifiers 

It could be advantageous to provide a method to define arbitrary installation prefixes. This would enable users to split a package into `foo`{.backtick} and `foo-plugin`{.backtick} while still being able to install the data files shipped with `foo-plugin`{.backtick} into the correct location.

**Discussion**: [Distutils/DiscussionOverview/UserPrefixes](./Distutils(2f)DiscussionOverview(2f)UserPrefixes.html)

**Status**: Under Consideration

**Affected PEPs**: 376

## User story: Package management 

As a user I want to list installed python packages, install and uninstall from command line. I also would like to search for them, list files that they contain. I also want to see if there are updates to them. I want to have an option to see diffs for updates (like directory diffs and content diffs) and changelogs when deciding whenever to update or not. I also want an ability to create my own isolated virtual environment with chosen packages and update it separately.

**Discussion**: unknown

**Status**: unknown

**Affected PEPs**: unknown
