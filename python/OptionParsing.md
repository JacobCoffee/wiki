# OptionParsing

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

## 1. Builtin Tools 

Overview of Python modules for option parsing

- [getopt](http://docs.python.org/2/library/getopt.html) - procedural interface in stdlib for refugees from the C camp

- [optparse](OptParse) - stdlib name for Optik, a revolutionary API for option parsing in Python 2.x

- [argparse](http://docs.python.org/3/library/argparse.html) - `optparse`{.backtick} pumped up for Python 3.x (and included in Python 2.7)

## 2. External tools 

::: {}
+--------------------------------------------------------------------------------+----------------------------------------------------------------------------+---------------------+-----------------------------------------------------------------------------------------------+
| **Name**                                                                       | **[365 Day Ranking](https://hugovk.github.io/top-pypi-packages/)** | **Latest Release**  | **Description**                                                                               |
+--------------------------------------------------------------------------------+----------------------------------------------------------------------------+---------------------+-----------------------------------------------------------------------------------------------+
| [Abseil Python Common Libraries](https://github.com/abseil/abseil-py)\ | 103                                                                        | 0.11.0 (2020-10-27) | gflags merged into this                                                                       |
| (pypi: [absl-py](https://pypi.org/project/absl-py/))                   |                                                                            |                     |                                                                                               |
+--------------------------------------------------------------------------------+----------------------------------------------------------------------------+---------------------+-----------------------------------------------------------------------------------------------+
| [Click](https://palletsprojects.com/p/click/)\                         | 34                                                                         | 7.1.2 (2020-04-27)  | create beautiful command line interfaces in a composable way with as little code as necessary |
| (pypi: [click](https://pypi.org/project/click/))                       |                                                                            |                     |                                                                                               |
+--------------------------------------------------------------------------------+----------------------------------------------------------------------------+---------------------+-----------------------------------------------------------------------------------------------+
| [Typer](https://typer.tiangolo.com/)\                                  | 2321                                                                       | 0.3.2 (2020-08-16)  | build great CLIs. Easy to code. Based on Python type hints.                                   |
| (pypi: [typer](https://pypi.org/project/typer/))                       |                                                                            |                     |                                                                                               |
+--------------------------------------------------------------------------------+----------------------------------------------------------------------------+---------------------+-----------------------------------------------------------------------------------------------+
:::

More:

- [cmdopts](http://code.google.com/p/py-command-line-options) - \...

- [docopt](http://docopt.org/) - no API calls needed, it\'s awesome!

## 3. The goal of option parsing 

The option parsing goal can be split in two parts:

1.  identifying the command user needs to execute
2.  changing configuration for the program

For the first part, it will be good if option parsing library could handle \'subcommands\'. It is known that \'argparse\' can do this and \'optparse\' cannot. \'docopt\' probably handles this transparently.

For the second thing there should be some strategy to choose how (and which) options are merged into configuration to make the process of program configuration easy for the user and occasional patch contributors.

## 4. See Also 

- [ConfigParser](ConfigParser)

- [CommandlineTools](CommandlineTools)
