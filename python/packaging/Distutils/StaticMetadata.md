# Distutils/StaticMetadata

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

This page discuss the way to separate the metadata in a static PKG-INFO like file.

- use the distutils.dist.[DistutilsMetadata](DistutilsMetadata) as a basis to think about a read/write API [an example](http://bugs.python.org/file12746/get_metadata.diff)

  - \- implemented in distutils2.metadata.[DistributionMetadata](./DistributionMetadata.html)

- think about the dynamic metadata issue (can we provide something for that ?)

- write a best practice guide for people to separate their metadata in a separate file, and use it in their setup.py
  - \- progress about that tracked in [http://bugs.python.org/issue8252](http://bugs.python.org/issue8252)

## TresSeaver\'s notes 

Matthias Klose and I worked on this a bit. We settled on the idea of reusing the \'setup.cfg\' file, by relaxing the \"one section per command\" rule to allow spelling more arbitrary metadata.

I commented to reflect work happening in distutils2 --ÉA (Éric Araujo)

In particular, we proposed the following changes:

- Document use of extra sections, not directly connected to a command.
  - \- work in progress (ÉA)

- Allow expansion of values using \'\${key:value}\' semantics from other sections.
  - Alternative: When passing arguments to commands, pass the whole

    \'[ConfigParser](ConfigParser)\' (to allow pulling in config from other commands / sections. This is more general, so maybe a \"better\" choice, but might break backward-compatibility with out-of-core commands.

- Add new distutils commands, each with their own sections in \'setup.cfg\' (these sections would break out files currently labeled only as \'data\' into categories more useful to downstream packageers).
  - \'install_docs\'

  - \'install_i18n\' / \'install_locales\'. See the Ubuntu extension which alread does this stuff: \'python-distutils-extra\', maintained by Sebastian Heinlein.

  - \'install_tests\'?

  - Alternative: add one or more new sections, not based on a command, which captures the extra stuff.

    See [http://hg.python.org/distutils2/file/tip/docs/design/wiki.rst](http://hg.python.org/distutils2/file/tip/docs/design/wiki.rst) ---ÉA

- Add a distutils command which generates [ConfigParser](ConfigParser) section text (on \'sys.stdout\') based on values passed to \'setup()\'. This command would provide a migration path for existing distributions, who would capture the output to a file, review it, and then concatenate it onto their \'setup.cfg\'.

- Eventually, the only thing in \'setup.py\' for the majority of packages would be:
  - try:

    - from setuptools import setup

    except [ImportError](./ImportError.html):

    - from distutils import setup

    setup() \# use the data in setup.cfg

- The only reason to include \'setup.py\' at all would be for compatibility with existing docs, etc. The \"normal\" installation dance might be something like:
  - \$ python -m distutils.commands.install

  or a generated script which did the same thing.
