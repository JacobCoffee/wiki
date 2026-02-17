# PackagingBOF

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# 1. Summary 

The following topics came up during the two BoF meetings. Thanks to Jeff Rush for his summary sent to the Distutils-sig mailing list! (This list may be incomplete, please feel free to add to it.)

The BoF drew about 15 people, many of whom were packagers for Red Hat, Ubuntu and such. Everyone had strong expressions of frustration with the status quo and most had tried to resolve their issues but had their patches rejected. I am not taking either side and whether those rejections were justified I cannot say, but the general feeling of their concerns intentionally not being addressed isn\'t healthy. Several had abandoned setuptools, deeming it a failed solution and others called for a fork.

1.  Many felt the existing dependency resolver was not correct. They wanted an intersection of the known restrictions instead of the depth-first, single restriction approach taken now which can result in top-level dependencies not being enforced upon lower levels. One solution would be to make the resolver pluggable.

2.  People want a solution for the handling of documentation. The distutils module has had commented out sections related to this for several years.

3.  A more flexible internal handing of the different types of files is needed. Currently the code, data, lib, etc. files are aggregated at build time and people would like them to be kept separate until install/packaging time so that they can be handled differently.\
    \
    They also want greater flexibility in the kinds of files identified for packaging. There is currently a single plugin entrypoint for file_finding, so people have resorted to abusing the setuptools function find_packages() again and again with different include/exclude args. A solution is to expand the set of entrypoints into finer grained categories. They also want a way to expand the set of categories rather than a fixed set, which can be easily done with entrypoint groups and names.\
    \
    People also want a greater variety of file_finders to be included with setuptools. Instead of just CVS and SVN, they want it to comprehend Mercurial, Bazaar, Git and so forth.

4.  They want an uninstall setuptools command. Adding one to remove a specific egg isn\'t difficult but correctly removing those dependencies that came in with that egg, without breaking later installs can be tricky.\
    \
    This is complicated because there isn\'t a single global package namespace to manage, when you factor in virtualenv and buildout sandboxes and per-user package areas. This differs from how RPMs and .debs are viewed.

5.  There was concern over the .pth mechanism used by setuptools re activation. First, there is a (perceived) performance issue with increasingly adding every ZIP file explicitly onto sys.path. This may or may not be a red herring.\
    \
    The other is the use of a single .pth file to control the list of activated packages. Those who produce distributions would prefer a magic directory into which links to distributions could be dropped, similar to the current best practices for Linux, with /etc/conf.d/, /etc/profile.d/, /etc/xinetd.d/ and so forth.

6.  There is a need for more extensibility hooks. People want places to plug in special handling. For example:
    a.  Setuptools has a \--record option to capture the list of files installed for use by subsequent packaging tools. Some want that list to be available to a setuptools plugin.
    b.  Some want hooks for post-build/post-install actions, instead of the current approach of writing a custom build class that handles it all.

7.  Many wanted an ability to install files anywhere in the install tree and not just under the Python package. Under distutils this was possible but it was removed in setuptools for security reasons. Custom code can still be written to do this explicitly but this is not popular. Neither setuptools nor distutils has the ability to rename files at install time. It would be sufficient if one could write an arbitrary post-install (and pre-uninstall) script that would be automatically executed during installation and uninstallation.

8.  Linux distributions try to ship only one version of a package/egg/module in one release, only shipping more than one version if necessary. eggs (as least as shipped with Debian, Fedora, Ubuntu) are all built using \--single-version-externally-managed.
    a.  import foo should work wether installed as an egg or installed with distutils, and without using pkg_resources.require
    b.  pkg_resources should handle the situation of one egg version installed as \--single-version-externally-managed (default version) and one or more eggs installed not using \--single-version-externally-managed. Currently these additional versions cannot be imported.

9.  It would be useful if setuptools could handle separate build and install steps like most configure/make/make install systems do. Access to external resources should optionally be disabled during a build.

10. The idea was brought up to use a to-be-defined api-version to describe dependencies between eggs. Version numbers are generally used for more than api changes; the idea follows existing practice for shared object names, only changing when the API is changed.

A fair question is whether it is the job of setuptools (or any Python packaging solution) to cover all these bases. The risk of not doing the job is that some of those in attendance were rolling their own solutions which do not play well with packages installed using other means, not seeing them. Distutils has intentionally tried to -not- be a general replacement packaging solution, with its support of the \"bdist\" command for various platform-specific distribution formats. We should continue not trying to replace platform-specific packaging technologies but perhaps improve our control of their creation.

As mentioned, some of these concerns can be resolved by adding customization-pressure-release entrypoints to setuptools, and some can be handled with much better documentation of use cases and what to do. And some of it is confusion over packaging libraries versus applications, where setuptools focuses on the former and zc.buildout focuses on the latter. But buildout is very young, maintains isolation from the system Python and was not known to many of the packaging BoF attendees.

# 2. Other Enthought Notes 

- When different eggs require the same project but with different version requirements, setuptools/easy_install doesn\'t attempt to merge the requirements or inform you that there is no way to simultaneously satisfy both requirements. Instead, it installs the best match for the first requirement and then chokes on the second if its \'best match\' for the first doesn\'t work for the second. We propose a change where all \*known\* requirements are tracked and intersected before a download of a dependency is made. This way an application egg, which is usually what a user would request and thus is likely to be the first processed, can explicitly identify library versions and the install tool would always intersect these with any library dependency versions.

- When running easy_install, output about the installation progress for a project doesn\'t include any information about which project(s) required that project. Instead, it just says something like \"Searching for foo \> X, \< Y\". If there is an error in any dependency spec, you have no clue which project that spec came from.

- There is no tool/feature to uninstall a project.

- There is no ability to declare a preference for a release of a project. For example, I\'d like to say my project requires \"a release of enthought.traits \>= 2.0, \<3.0\". I\'d then like easy_install/setuptools to only pick releases (no qualifiers of any kind alpha, beta, dev, etc.) of 2.0, 2.1, 2.2, 2.3, 2.4, \.... As a further example, it should totally ignore \'2.5a1\' and \'2.6_r15669\'. This is driven by a common error which is to write something like \"enthought.traits \>= 2.0.1, \<3.0\" instead of \"enthought.traits \>= 2.0.1, \<3.0a\". In the former, the first efforts at developing enthought.traits-3.0 get installed instead of the latest release of 2.x.

- When an egg contains extension code, the egg names aren\'t specific enough to allow hosting of multiple platforms in the same repository. For example, we can\'t host an egg built for RHEL 3 in the same directory as one for Ubuntu 7.10 because they both have a name like \"enthought.traits-3.0-py2.5-linux-i686.egg\" even though the binary build is not compatible between the two platforms.

- Documents and examples can\'t be useful included in an egg because access to them is not somewhere where users would normally look. It would be nice if documents and examples got copied to a specified directory (platform standard perhaps?) when the egg was installed \-- somewhat how like scripts are generated in the single scripts dir during egg installation. It would be gravy if they got removed when the egg was uninstalled.

- It would be nice if we could have 2 eggs of the same version, one binary built with debug support and without it, in a egg repository. And then we\'d need some way to pick which to install.

# 3. Other Debian/Ubuntu Notes 

- Standardize version numbers such that no heuristics are needed for version comparisions. See [http://www.us.debian.org/doc/debian-policy/ch-controlfields.html#s-f-Version](http://www.us.debian.org/doc/debian-policy/ch-controlfields.html#s-f-Version) for a format addressing errors in version handling (epochs) and handling prerelease and release candidate versions. The paragraph about debian revisions does not apply.

- Archive maintainance in Debian/Ubuntu is expensive and requires manual interaction when a binary package enters the distribution or leaves the distribution; this is the main reason for modules and extensions packaged in unversioned packages. Such a package can be used for more than one python version. Think about it as a \"fat package\" like Darwin binaries which could be built for more than one architecture, but here for more than one python version. It would be nice to have some support for such a layout such as having non-conflicting file names for .so and .pyc files.

# 4. Invitation Text 

Enthought is currently using eggs and several extensions to eggs in order to package and ship the Enthought Python Distribution. In doing this, we have encountered multiple opportunities for improving the current approach to packaging and distribution using eggs that we would like to discuss with anyone else in the Python community interested in these issues.

Some of our ideas are well-developed and others are more ephemeral. We would like to spend an hour or two discussing these ideas and comparing notes with anyone else interested in packaging and distributing python modules.
