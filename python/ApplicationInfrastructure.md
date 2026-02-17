# ApplicationInfrastructure

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# Reusable application infrastructure 

A quick overview of components needed for a reusable application infrastructure. *Reusable* means that external projects can easily reuse the basic building blocks to implement their project-specific (i.e. coupled to that particular project) application/plugin stores. *Application* is used in more or less equivalent sense to a Python package.

This is a proposal for the API, not for particular tools.

Installing an application consists of:

1.  fetching the app descriptor from a configurable location (currently PyPI, there should be no default in the API)

2.  parse the app descriptor to a Python app descriptor object

3.  parse the dependencies listed in the descriptor

4.  check if dependencies are installed, if not, install each of them by going to step 1 (recursively)

5.  download the app package from the URL given in the descriptor

6.  verify the app package with the digest given in the descriptor

7.  unpack the app package to a temporary location

8.  run any required sanity checks on the unpacked source

9.  move the source to a configurable location to install it (currently `site-packages`{.backtick}, but apps may have different needs, e.g. Google App Engine frameworks need a plain directory as the target location)

10. optionally move documentation and tests to specific locations as well

Specifics:

- writing a tool that can be told to install an application (pip, easy_install, project-specific enhanced tool) should be entirely trivial with the API
  - it should be easy for frameworks to implement e.g. `trac-admin install pluginname [pluginversion]`{.backtick} or `django-admin.py install reusableapp [appversion]`{.backtick} with the API

- it\'s possible to specify the location where applications are installed (to cater for virtualenv and \"lump all libs into `/some/where/lib/`{.backtick} and `sys.path.insert('/some/where/lib/')`{.backtick}\" workflows)

- it\'s possible to specify the package index URL, to facilitate PyPI mirrors, framework-specific \"PyPI\"s etc

- there will be rigid guidelines for app versioning (see below) for sensible version parsing and ordering

- there will be rigid guidelines for app directory layout to help Linux distribution packagers to put docs and tests to system-specific locations (e.g. \'/usr/share/docs` and `{.backtick}/usr/something/python/site-packages/tests\`)

What is not covered:

- eggs or any other binary packaging formats, assume source packages - this tool can be used for creating them (including Linux distribution-specific formats like .deb or .rpm) \-- generally needs more thinking

Lets assume that the API is called `appinfra`{.backtick}.

## Application descriptors 

Application descriptors are instances of `App`{.backtick} class. The latter is a struct-like container class for all application meta-data. See [http://docs.python.org/distutils/setupscript.html#additional-meta-data](http://docs.python.org/distutils/setupscript.html#additional-meta-data) for the main fields, also [http://peak.telecommunity.com/DevCenter/PkgResources](http://peak.telecommunity.com/DevCenter/PkgResources).

The propsed API uses the following fields that are described below: `version`{.backtick}, `depends`{.backtick}, `python_versions`{.backtick}, `download_url`{.backtick}, `platforms`{.backtick}.

## A sample main() that uses the API 

This illustrates a high-level use case for the API, both system-level tools and framework-specific tools would be implemented in similar manner:

    import sys
    import appinfra

    from myframework.conf import settings
    from myframework import run_sanity_checks, move_app_to_expected_location
    from myframework import move_tests_to_expected_location, move_docs_to_expected_location

    def install_app(appname, appversion):
        app = appinfra.fetch.fetch_descriptor(settings.APPSTORE_URL, appaname, appversion)
        if not appinfra.verify.python_version_supported(app.python_versions):
            raise RuntimeError("Unsupported Python version.")
        if not appinfra.verify.platform_supported(app.platforms):
            raise RuntimeError("Unsupported platform.")

        for dep in app.dependencies:
            if not appinfra.deps.is_installed(dep.name, dep.versions, ['/my/framework/libs']):
                best_version = appinfra.deps.best_version(dep.versions)
                install_app(dep.name, best_version)

        app_package = appinfra.fetch.fetch_package(app.download_url)
        if not appinfra.verify.package_is_valid(app.digest, app_package):
            raise RuntimeError("Digest does not match package file.")

        package_dir = appinfra.package.unpack(app_package)
        if not appinfra.package.dir_has_expected_structure(package_dir):
            raise RuntimeError("Package directory does not have the required structure")

        if app.needs_compiling():
            appinfra.package.compile_package(app, package_dir)

        run_sanity_checks(app, package_dir) # e.g. CheeseCake http://pycheesecake.org/

        move_app_to_expected_location(app, package_dir)
        move_tests_to_expected_location(app, package_dir)
        move_docs_to_expected_location(app, package_dir)

        run_any_additional_hooks(app) # e.g. update settings, register in a package registry etc

        appinfra.package.cleanup(app_package, package_dir)

    def main():
        appname, appversion = sys.argv[1:]
        install_app(appname, appversion)

## Fetch API 

The `fetch`{.backtick} or `download`{.backtick} module contains the following functions:

    fetch_descriptor(base_url, appname, appversion=None) -> App instance

Downloads the app descriptor for central app descriptor store and converts it to an App instance. Note that the `base_url`{.backtick} concept makes it possible to create app stores that support **namespaces**, e.g. `http://foo.com/apps/`{.backtick} - the base index, `http://foo.com/django/apps/`{.backtick} - only apps coupled to Django, `http://foo.com/zope/apps/`{.backtick} - only apps coupled to Zope etc.

Behaviour:

- urljoin `appname`{.backtick} to `base_url`{.backtick}; if `appversion`{.backtick} is not None, add it as a query parameter, resulting in e.g. `http://foo.com/appstore/appname/?version=1.2`{.backtick}

- urlopen the resulting URL, retrieve contents. The contents represent the App object in JSON.

- decode the result with the json module, resulting in a dict with metadata fields.

- construct an App object with the dict, return it.

<!-- -->

    fetch_package(download_url) -> path to filename

Downloads the packaged application to local filesystem.

Behaviour:

- downloads the application package from `download_url`{.backtick} to system temporary directory, returns the full path to the resulting file

## Verification API 

The `verify`{.backtick} module contains the following functions:

    python_version_supported(python_versions) -> True, False

Verifies if the running Python version is in `python_versions`{.backtick}, a list of strings.

    platform_supported(platforms) -> True, False

Verifies if the string representation of current platform is in `platforms`{.backtick}, a list of strings.

    package_is_valid(digest, package_file) -> True, False

Verifies if the digest matches the package file\'s digest. Digest is in the form `algoname:digest_value_in_base64`{.backtick}.

## Dependency API 

The `deps`{.backtick} module contains the following functions:

    is_installed(app_name, app_versions, additional_paths=None) -> True, False

Checks whether a prerequisite application is installed.

Behaviour:

- `app_versions`{.backtick} is a list of strings in the format `comparison_operator version_string`{.backtick}. Comparison operator can be any of `<|<=|!=|==|>=|>`{.backtick} and version string has to be in supported format for the `version`{.backtick} module (see below).

- if `additonal_paths`{.backtick} is given, inserts (or appends?) them into `sys.path`{.backtick}

- tries to `__import__(app_name)`{.backtick}, if that fails, returns `False`{.backtick}

- if import is successful, compares the installed app\'s version against the required versions with the specified comparison operator

- if the version matches any of the required versions, returns `True`{.backtick}, else `False`{.backtick}

<!-- -->

    best_version(supported_versions) -> version string

Selects the \"best\" version from `supported_version`{.backtick}, a list of strings. \"Best\" version is the highest released version (this may need more thought).

## Package API 

The `package`{.backtick} module contains the following functions:

    unpack(package_file) -> package_dir

Unpacks the package to a temporary location and returns the full path to the resulting directory.

    dir_has_expected_structure(package_dir) -> True, False

Verifies if the unpacked package directory has expected structure. There will be **strict, defined requirements** on how the directory should be laid out (e.g. tests in \'tests\', documentation in \'docs\' etc).

    compile(app, package_directory)

Compiles the C/C++/whatnot sources to binaries.

## Version API 

Version format will be strictly defined (both the string representation and capabilities of the `Version`{.backtick} class) according to best practices.

The responsibilities of the `Version`{.backtick} class will be to provide canonical string representation of `Version`{.backtick} objects, parser version strings and create corresponding `Version`{.backtick} objects, and consistent and intuitive ordering of versions. Strict version format makes dependency handling easy and contributes to general correctness and order.

Possible specification:

`appinfra`{.backtick}-confirming packages MUST use the `appinfra.version.Version`{.backtick} objects to declare their versions.

Version strings are in \"major.minor\[.patch\] \[sub\]\" format. The major number is 0 for initial, experimental releases of software. It is incremented for releases that represent major milestones in a package. The minor number is incremented when important new features are added to the package. The patch number increments when bug-fix releases are made.

Additional trailing version information is used to indicate sub-releases. These are \"alpha 1, alpha 2, \..., alpha N\" for alpha releases, where functionality and API may change, \"beta 1, beta 2, \..., beta N\" for beta releases, which only fix bugs and \"pre 1, pre 2, \..., pre N\" for final pre-release release testing. The \"pre-alpha\" sub-release is special, marking a version that is currently in development and not yet in release stage. As such it cannot have a sub-release version number. A release without sub-release information is considered final.

Packages have to utilise the `Version`{.backtick} class below for specifying their versions, e.g.:

    from appinfra import version

    VERSION = version.Version(0, 1)
    # or
    VERSION = version.Version(0, 1, 2)
    # or
    VERSION = version.Version(1, 0, 3, version.PRE_ALPHA)
    # or
    VERSION = version.Version(1, 0, version.ALPHA, 1)

## Example implementation 

### Version handling 

`appinfra.version`{.backtick} module (tested, working code):

    import re

    from appinfra.exceptions import VersionError

    PRE_ALPHA, ALPHA, BETA, PRERELEASE, FINAL = range(5)

    SUBRELEASE_DICT = {
        PRE_ALPHA:  'pre-alpha',
        ALPHA:      'alpha',
        BETA:       'beta',
        PRERELEASE: 'prerelease',
    }

    SUBRELEASE_DICT_REVERSE = dict((value, key) for key, value in
        SUBRELEASE_DICT.items())


    def SubreleaseError():
        """
        A factory function for creating a particularly complex yet informative
        VersionError instance.
        """
        return VersionError("Subrelease has to be one of %s." %
                ", ".join("%s (%s)" %
                    (SUBRELEASE_DICT[key], key)
                    for key in sorted(SUBRELEASE_DICT.keys())))

    class Version(object):
        """
        Class for representing package versions.

        `Version` objects have human-readable string representation and defined
        ordering. When comparing versions, non-release versions (i.e. versions
        that *have subrelease numbers*) have less priority than release versions,
        e.g.::

        >>> v = Version(1, 2, 3, BETA, 1)
        >>> v2 = Version(0, 1)
        >>> v2 > v
        True
        >>> v3 = Version(1, 2, 3)
        >>> v3 > v2
        True

        Usage::

        >>> v = Version(0, 1)
        >>> v
        Version(major=0, minor=1)
        >>> print v
        0.1
        >>> print Version(0, 1, subrelease=0)
        0.1 pre-alpha
        >>> print Version(0, 1, subrelease=1, subrellevel=1)
        0.1 alpha 1

        >>> Version(1, 2, 3, 0)
        Version(major=1, minor=2, patch=3, subrelease=0)
        >>> Version(1, 2, 3, PRE_ALPHA)
        Version(major=1, minor=2, patch=3, subrelease=0)

        >>> v = Version(1, 2, 3, BETA, 1)
        >>> v
        Version(major=1, minor=2, patch=3, subrelease=2, subrellevel=1)
        >>> print v
        1.2.3 beta 1
        """
        def __init__(self, major, minor, patch=None, subrelease=None,
                subrellevel=None):
            self.major = _to_int(major, "Major number")
            self.minor = _to_int(minor, "Minor number")
            self.patch = _to_int_or_none(patch, "Patch number")
            self.subrelease = _to_int_or_none(subrelease, "Subrelease number")
            if (self.subrelease is not None and
                    self.subrelease not in SUBRELEASE_DICT):
                raise SubreleaseError()
            if self.subrelease == PRE_ALPHA and subrellevel is not None:
                raise VersionError("Pre-alpha release can have no subrelease "
                        "level number.")
            self.subrellevel = _to_int_or_none(subrellevel,
                    "Subrelease level number")

        def __str__(self):
            format = '%(major)s.%(minor)s'
            params = self.__dict__.copy()
            if self.patch is not None:
                format += '.%(patch)s'
            if self.subrelease is not None:
                format += ' %(subrelease)s'
                params['subrelease'] = SUBRELEASE_DICT[self.subrelease]
            if self.subrellevel is not None:
                format += ' %(subrellevel)s'
            return format % params

        def as_tuple(self):
            return (self.major, self.minor, self.patch, self.subrelease,
                self.subrellevel)

        def __repr__(self):
            return 'Version(%s)' % ', '.join(['%s=%s' %
                (label, getattr(self, label))
                for label in sorted(self.__dict__.keys())
                if getattr(self, label) is not None])

        def __lt__(self, other):
            # non-release versions are always lower priority
            if self.subrelease is not None and other.subrelease is None:
                return True
            if other.subrelease is not None and self.subrelease is None:
                return False

            return self.as_tuple() < other.as_tuple()

        def __gt__(self, other):
            return other < self

        def __le__(self, other):
            return not (other < self)

        def __ge__(self, other):
            return not (self < other)

        def __eq__(self, other):
            return self.as_tuple() == other.as_tuple()

        def __ne__(self, other):
            return not (self == other)

        def __hash__(self):
            return hash(self.as_tuple())


    VERSION_RE = re.compile(r'^(?P<major>\d+)\.(?P<minor>\d+)(\.(?P<patch>\d+))?'
            r'( (?P<subrelease>[-a-z]+)( (?P<subrellevel>\d+))?)?$')
    def from_string(version_string):
        """
        Factory function that creates `Version` objects from version strings.

        To specify strings in right format, create a `Version` object and convert
        it to string to get the canonical representation.

        Usage:

        >>> from_string('1.2.1 beta 5')
        Version(major=1, minor=2, patch=1, subrelease=2, subrellevel=5)
        >>> from_string('1.2')
        Version(major=1, minor=2)

        :param version_string: the string that specifies the version
        :return: a Version object
        """
        match = VERSION_RE.match(version_string)
        if not match:
            raise VersionError("Incorrect version string. Please generate it in "
                    "the manner of 'str(Version(1, 2, 0, ALPHA, 1))'.")
        result = match.groupdict()
        if result['subrelease'] is not None:
            if result['subrelease'] not in SUBRELEASE_DICT_REVERSE:
                raise SubreleaseError()
            result['subrelease'] = SUBRELEASE_DICT_REVERSE[result['subrelease']]
        return Version(**result)

    def _to_int(value, label):
        try:
            return int(value)
        except (TypeError, ValueError):
            raise VersionError("%s has to be an integer." % label)

    def _to_int_or_none(value, label):
        if value is None:
            return value
        return _to_int(value, label)

Samples of version ordering:

    def test_ordering():
        v0 = Version(0,1)
        v1 = Version(1,2)
        v2 = Version(1,2,1)
        v3 = Version(1,2,1,2,2)
        v4 = Version(1,2,1,2,3)
        v5 = Version(major=1, patch=1, minor=2, subrellevel=2, subrelease=2)

        assert v1 > v0
        assert v1 >= v0
        assert v0 < v1
        assert v0 <= v1
        assert v2 > v1
        assert v0 > v3
        assert v4 > v3

        assert v1 != v2
        assert v3 == v5

### Dependency handling 

`deps`{.backtick} module (untested code, may break horribly):

    import re, sys, operator

    from plugit import version, install

    CMP_OP_MAP = {
        '<':  operator.lt,
        '<=': operator.le,
        '==': operator.eq,
        '!=': operator.ne,
        '>=': operator.ge,
        '>':  operator.gt,
    }
    # ",?\s*(?=%s)" % "|".join(CMP_OP_MAP.keys())
    DEP_SPLIT_RE = re.compile(r',?\s*(?=<|<=|!=|==|>=|>)')
    VER_DEP_RE = re.compile(r'(?P<cmp><|<=|!=|==|>=|>)\s*(?P<ver>[-a-z0-9. ]+)')

    def _parse(ver_deps):
        chunks = DEP_SPLIT_RE.split(ver_deps)
        return [VER_DEP_RE.match(chunk).groupdict() for chunk in chunks]

    def is_installed(appname, ver_deps, additional_paths=None):
        if additional_paths:
            for path in additional_paths:
                sys.path.insert(0, path)
        try:
            __import__(appname)
            app = sys.modules[appname]
        except ImportError:
            return False

        for ver in _parse(ver_deps):
            if CMP_OP_MAP[ver['cmp']](app.__version__,
                    version.from_string(ver['ver'])):
                return True

        return False

## Copyright 

This document is in public domain. Created by Mart Sõmermaa, mrts.pydev at gmail dot com.
