# Distutils/Proposals/SplitAndCompoundDistributions

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

## Abstract 

Make the source-to-distribution mapping more flexible to allow people to build multiple distributions from one project, and to bundle multiple distributions into one distribution.

## Rationale 

When extracting reusable parts from a codebase, one must move the files and write a dedicated setup script (or setup config file, when PEP 390 is implemented). OS packagers sometimes also distribute Python packages from one distribution as separate OS packages (e.g. Debian has python-setuptools and python-pkg-resources). I think that Distutils2 could handle these use cases.

Conversely, some people would like to provide their users with source and built meta-distribution bundling their project alongside with their build dependencies (including testing package) and runtime dependencies ([MoinMoin](MoinMoin) does that), without the need for virtualenv or network access. A new kind of distribution would meet this use case.

## Requirements/Ideas 

Building multiple distributions out of one directory will require either an extension to the setup.cfg file or a new file. We could take good ideas from other build systems. For example, Debian's debhelper toolchain builds everything and then moves files to build binay packages using manifests.

Meta-distributions may or may not require an extension to the setup.cfg file. I need to think about this more.

## References 

1.  Add link to another Distutils page where building multiple packages was suggested

2.  [Debian Developers Reference](http://www.debian.org/doc/developers-reference/best-pkging-practices.html#multiple-binary) (scarce)

3.  [HOWTO Split a Package](http://wiki.debian.org/PkgSplit) on the Debian wiki: Example of manifests

4.  [Python bug #8371](http://bugs.python.org/issue8371), where I propose a command that would serve to download dependencies for normal and compound distributions.

5.  IRC discussion on #distutils on 2010-04-11 (edited):

<!-- -->

    <ronny> and well, another tricky issue is generating bundles
    <ronny> (i.e. distributing a app + its deps in a nice single file way)
    <merwok> Bundling everything in one blob is not something I like.
    <ronny> moinmoin ships all its dependencies to endusers on various platforms
    <merwok> That being said, I can’t see why there couldn’t be a third-party distutils command to do that.
    <ronny> it will be unnecessary hard in distutils
    <merwok> Distutils2 and PyPI and virtualenv can remove the need for that.
    <merwok> (There has been recent talk about including virtualenv-like support in core Python)
    <ronny> the moinmoin issue is not deploymen/packaging
    <ronny> its about having a easy shipment to endusers
    <ronny> one thing i want to manage is putting stuff like py.test + its dependencies into a sdist as single script
    <ronny> so i can ship the test tools as single file instead of needing to pull off crap
    <ronny> in sdists, so people can just test what they got
    <merwok> what about a command that gets dependencies?
    <merwok> I mean one command that downloads dependencies if necessary, and another one that builds a “fat” sdist?
    <ronny> that should work, i want both, slim and fat sdists

## Copyright and License Terms 

I, [ÉricAraujo](./(c389)ricAraujo.html), make this document available to anyone for all purposes and intents, including edition and distribution, in the limits allowed by their jurisdictions. (There is no such thing as "placing in the public domain".)
