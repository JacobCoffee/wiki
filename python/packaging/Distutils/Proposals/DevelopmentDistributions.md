# Distutils/Proposals/DevelopmentDistributions

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

## Abstract 

Give Python developers using distutils2 a way to import modules and packages from a source tree without building or installing it.

## Rationale 

People want to import their modules to try them while developing without reinstalling them constantly or mucking with import paths. The code will most of the time come from a version-controlled directory or an unpacked archive.

This proposal does not talk about VCS integration (for example building distributions from branches or tags).

Open issues: how to enable scripts provided by the distribution; how to make the dist-info directory available to pkgutil.

## Detailed Plan 

Provide a command that makes code in an arbitrary directory available for import and use without requiring to rebuild or reinstall it when the files change.

The mechanism for enabling such a devel installation would be as simple as adding a .pth file on the user's site-package directory (overridable with an option).

Since this is a type of installation, the feature should be implemented as an option to the install command. More specifically, since data, headers or scripts are not handled, an option to the install_lib command. This option would imply \--skip-build.

When the code includes C extensions, users will need to run build_ext \--inplace, but they will not have to run install_lib \--link-only again. With pure Python code, there will be no command to run to make the new code available as distribution.

An option to the uninstall command would be used to remove the .pth file.

## References 

1.  [Setuptools' develop command](http://peak.telecommunity.com/DevCenter/setuptools#development-mode)

2.  [Buildutils' use command](http://pypi.python.org/pypi/buildutils/0.3)

3.  [8668](http://bugs.python.org/issue8668 "Issue")

## Copyright and License Terms 

I, [ÉricAraujo](../../../archive/ÉricAraujo), make this document available to anyone for all purposes and intents, including edition and distribution, in the limits allowed by their jurisdictions. (There is no such thing as "placing in the public domain".)
