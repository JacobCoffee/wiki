# Distutils/DiscussionOverview/FilePrefixes

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# Rationale 

It is not possible to retrieve the installation paths of data, or other, files for all installation schemes supported by distutils right now. I propose the inclusion of a PREFIX file within the .egg-info directory that holds information on all prefixes set at installation time and a suitable API within pkgutil.

# Proposal 

## PREFIX 

The RECORD file is a CSV file, composed of records, one line per prefix. The csv module is used to read the file, with these options:

- field delimiter : `,`{.backtick}

- quoting char : `"`{.backtick}

- line terminator : `os.linesep`{.backtick} (so `\r\n`{.backtick} or `\n`{.backtick})

Each record is composed of two elements:

- **prefix identifier**

  - Prefix identifiers differentiate between the various prefixes used within the installation process.

    Valid identifiers must adhere to the regular expression `^[a-z_]+`{.backtick}, i.e any combination of lowercase ASCII characters and the underscore.

- **path**

  - The path for the prefix identifier for this distribution.

    A `/`{.backtick} seperated path will be used regardless of the target system. The path definition can be either absolute or prefixed with one of the identifiers defined below. An absolute path is only used if the installation location is not relative to sys.prefix (\$base) or sys.exec_prefix (\$platbase).

### Identifiers 

The list of standard identifiers comprises:

- `$base`{.backtick} - Base prefix

- `$platbase`{.backtick} - Platform specific base prefix

- `$purelib`{.backtick} - Pure Python distribution

- `$platlib`{.backtick} - Non-pure Python distribution (i.e one with extensions)

- `$scripts`{.backtick} - Executable Python scripts

- `$data`{.backtick} - Data files

### Example 

Standard scheme installation on posix:

    base,/usr
    platbase,/usr
    purelib,$base/lib/pythonX.Y/site-packages
    platlib,$platbase/lib/pythonX.Y/site-packages
    scripts,$base/bin
    data,$base/share

User scheme installation on posix:

    base,/home/sirrobin/.local
    platbase,/home/sirrobin/.local
    purelib,$base/lib/pythonX.Y/site-packages
    platlib,$platbase/lib/pythonX.Y/site-packages
    scripts,$base/bin
    data,share

Custom installation scheme:

    base,/home/sirrobin/.local
    platbase,/home/sirrobin/.local
    purelib,$base/lib/pythonX.Y/site-packages
    platlib,$platbase/lib/pythonX.Y/site-packages
    scripts,/usr/local/bin
    data,/usr/local/share/

### Default values 

Tables summarising the default values on different operating systems:

#### posix

::: {}
  ------------------------ ---------------------------------------------------- ---------------------------------------------------- ------------------------------- --------------------------------
  **Prefix identifier**    **Default value: Standard scheme**                   **Default value: User scheme**                       **Environment variable**        **Command line option**
  `$base`{.backtick}       `sys.prefix`{.backtick}                              `~/.local`{.backtick}                                `$PYDIST_BASE`{.backtick}       `--prefix`{.backtick}
  `$platbase`{.backtick}   `sys.exec_prefix`{.backtick}                         `~/.local`{.backtick}                                `$PYDIST_PLATBASE`{.backtick}   `--exec-prefix`{.backtick}
  `$purelib`{.backtick}    `$base/lib/pythonX.Y/site-packages`{.backtick}       `$base/lib/pythonX.Y/site-packages`{.backtick}       `$PYDIST_PURELIB`{.backtick}    `--install-purelib`{.backtick}
  `$platlib`{.backtick}    `$platbase/lib/pythonX.Y/site-packages`{.backtick}   `$platbase/lib/pythonX.Y/site-packages`{.backtick}   `$PYDIST_PLATLIB`{.backtick}    `--install-platlib`{.backtick}
  `$scripts`{.backtick}    `$base/bin`{.backtick}                               `$base/bin`{.backtick}                               `$PYDIST_SCRIPTS`{.backtick}    `--install-scripts`{.backtick}
  `$data`{.backtick}       `$base/share`{.backtick}                             `$base/share`{.backtick}                             `$PYDIST_DATA`{.backtick}       `--install-data`{.backtick}
  ------------------------ ---------------------------------------------------- ---------------------------------------------------- ------------------------------- --------------------------------
:::

#### nt

::: {}
  ------------------------ ------------------------------------ ------------------------------------------------------ ------------------------------- --------------------------------
  **Prefix identifier**    **Default value: Standard scheme**   **Default value: User scheme**                         **Environment variable**        **Command line option**
  `$base`{.backtick}       `sys.prefix`{.backtick}              `os.environ.get('%APPDATA%')`{.backtick}               `$PYDIST_BASE`{.backtick}       `--prefix`{.backtick}
  `$platbase`{.backtick}   `sys.exec_prefix`{.backtick}         `os.environ.get('%APPDATA%')`{.backtick}               `$PYDIST_PLATBASE`{.backtick}   `--exec-prefix`{.backtick}
  `$purelib`{.backtick}    `$base/Python`{.backtick}            `$base/Python/PythonXY/site-packages`{.backtick}       `$PYDIST_PURELIB`{.backtick}    `--install-purelib`{.backtick}
  `$platlib`{.backtick}    `$platbase/Python`{.backtick}        `$platbase/Python/PythonXY/site-packages`{.backtick}   `$PYDIST_PLATLIB`{.backtick}    `--install-platlib`{.backtick}
  `$scripts`{.backtick}    `$base/Scripts`{.backtick}           `$base/Python/Scripts`{.backtick}                      `$PYDIST_SCRIPTS`{.backtick}    `--install-scripts`{.backtick}
  `$data`{.backtick}       `$base/Data`{.backtick}              `$base/Python/Python26`{.backtick}                     `$PYDIST_DATA`{.backtick}       `--install-data`{.backtick}
  ------------------------ ------------------------------------ ------------------------------------------------------ ------------------------------- --------------------------------
:::

#### mac

#### os2

#### ce

#### java

#### riscos

## API 

The Distribution class will get a new attribute `prefixes`{.backtick} which holds a dictionary mapping prefix identifiers to their absolute paths.

Usage example:

    >>> foo_dist = pkgutil.get_distribution('foo')
    >>> foo_dist.prefixes['$base']
    '/usr'
    >>> foo_dist.prefixes['$data']
    '/usr/share'
    >>> ni_wish = open(os.path.join(foo_dist.prefixes.get('$data'), 'foo', 'shrubbery.jpg'))
    >>> unladen = open(os.path.join(foo_dist.prefixes['$data'], 'foo', 'european.swallow'))
