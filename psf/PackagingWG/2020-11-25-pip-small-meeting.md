# PackagingWG/2020-11-25-pip-small-meeting

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

Sunday 25 Nov

Pradyun-Sumana meeting

- On Big Sur support - updated [https://github.com/pypa/pip/issues/8936](https://github.com/pypa/pip/issues/8936)

  - TODO: Sumana to mark in release announcement

- to triage \-- updated several issues, such as #9143, #9020, and #9139

- Releasing a beta for 20.3 right now.
  - add attention admonition on top:
    - Major and minor releases of pip also include changes listed within prior beta releases

    - PR opened: [https://github.com/pypa/pip/pull/9173](https://github.com/pypa/pip/pull/9173)

- Add \"no-deps\" suggestion to user guide - migration
  - change step 4 to \"Troubleshoot and try these workarounds\"
    - use `--no-deps`{.backtick} when you are sure you don\'t want pip to actually resolve dependencies, because you are using a set of packages that work together in reality even though their metadata says that they conflict \[this is a workaround \-- see [https://pip.pypa.io/en/latest/user_guide/#fixing-conflicting-dependencies](https://pip.pypa.io/en/latest/user_guide/#fixing-conflicting-dependencies) re longterm solution\]

    - read [https://pip.pypa.io/en/latest/user_guide/#dependency-resolution-backtracking](https://pip.pypa.io/en/latest/user_guide/#dependency-resolution-backtracking) for ways to reduce the time pip spends backtracking

    - use the old resolver \[reuse existing language\]

  - change pointers to resolver testing survey to GitHub issue?

    - no. Pradyun will look frequently

Major changes in this release:

1.  DISRUPTION: Switch to the new dependency resolver by default. (#9019) Watch out for changes in handling editable installs, constraints files, and more: [https://pip.pypa.io/en/latest/user_guide/#changes-to-the-pip-dependency-resolver-in-20-3-2020](https://pip.pypa.io/en/latest/user_guide/#changes-to-the-pip-dependency-resolver-in-20-3-2020)

2.  DEPRECATION: Deprecate support for Python 3.5 (to be removed in pip 21.0) (#8181)

3.  DEPRECATION ANNOUNCEMENT: pip freeze will stop filtering the pip, setuptools, distribute and wheel packages from pip freeze output in a future version. To keep the previous behavior, users should use the new \--exclude option. (#4256)

4.  Substantial improvements in new resolver for performance, output and error messages, avoiding infinite loops, and support for constraints files.

5.  Support for PEP 600: Future 'manylinux' Platform Tags for Portable Linux Built Distributions. (#9077)

6.  Documentation improvements: Resolver migration guide, quickstart guide, and new documentation theme.

7.  Add support for MacOS Big Sur compatibility tags. (#9138)
