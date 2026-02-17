# ExecutableModules

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

Python 2.4 added the `-m`{.backtick} option to execute modules as scripts ([Python documentation](https://docs.python.org/3/using/cmdline.html#cmdoption-m)). [PEP 338](https://www.python.org/dev/peps/pep-0338/), adopted in Python 2.5, adds the ability to execute modules in the search path.

# Executable Standard Library Modules 

The following standard library modules work as command-line tools:

- `python3 -m http.server`{.backtick} - Start a web server, serving files from the current directory ([full docs](https://docs.python.org/3/library/http.server.html#http.server.SimpleHTTPRequestHandler)).

- `python -m json.tool path/to/data.json`{.backtick} - Validate and pretty-print JSON. Omitting the path will read from standard input ([full docs](https://docs.python.org/3/library/json.html#module-json.tool)).

- `python -m pdb script.py`{.backtick} - Run a script in the debugger, starting post-mortem debugging on unhandled exceptions ([full docs](https://docs.python.org/3/library/pdb.htm)).

- `python -m timeit -s 'import string' '"x" in string.lowercase'`{.backtick} - Run some setup code (`import string`{.backtick}), and then run test code many (1,000,000 times) to time execution of the code. ([full docs](https://docs.python.org/3/library/timeit.html))

# Writing Executable Modules 

Here\'s a sample executable Python script:

    def main():
        import sys

        for pos, arg in enumerate(sys.argv):
            print('Argument %d: %s' % (pos, arg))


    if __name__ == '__main__':
        main()

If this file is importable as mylib.script, then running `python -m mylib.script foo bar`{.backtick} will output:

    Argument 0: /full/path/to/mylib/script.py
    Argument 1: foo
    Argument 2: bar

The starting line `#!/usr/bin/env python`{.backtick} is used in UNIX-like shells. If the script is given execute permissions, then it can also be executed directly. `python`{.backtick} may still point to Python 2.x on some systems, and in this case `python3`{.backtick} can disambiguate.

A fully-featured script should use a library to parse the command line, such as [argparse](https://docs.python.org/3/library/argparse.html). See the [source for json.tool](https://github.com/python/cpython/blob/master/Lib/json/tool.py) for a fuller example.
