# Distutils/Extensions/SpecFileManipulation

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

This extension of the `bdist_rpm`{.backtick} command shows how to modify the SPEC file before it is passed to the `RPM`{.backtick} shell command. It makes the Python version used to call \"setup.py\" known within the spec file, and also sets another prefix for the install step.

Note that you can use `pre_install`{.backtick} and `post_install`{.backtick} in your \"setup.cfg\" to add customized `%pre`{.backtick} and `%post`{.backtick} sections (those settings contain the names of files that are then appended to the SPEC file).

:::: 
::: 
``` 
   1 class bdist_rpm_ext(bdist_rpm):
   2     """ Überladung von bdist_rpm, um das SPEC-File etwas zu erweitern.
   3     """
   4 
   5     def _make_spec_file(self):
   6         spec_file = bdist_rpm._make_spec_file(self)
   7         spec_file[0:0] = [
   8             '%define pyversion ' + sys.version[:3],
   9         ]
  10 
  11         install = spec_file.index('%install')
  12         spec_file[install+1] = spec_file[install+1].replace(
  13             'setup.py install',
  14             'setup.py install --prefix /opt/%{name}/%{version}')
  15 
  16         return spec_file
```
:::
::::
