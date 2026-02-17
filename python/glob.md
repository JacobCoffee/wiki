# glob

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

------------------------------------------------------------------------

    r""" hitlist.py

    The glob module lists names in folders that match Unix shell patterns.

    If the elemental function emulating Unix bash `echo *` really is missing
    from the 2.5 Python batteries included, then here's a brief clear way of
    adding that function to Python.

    Mind you, to date I've never written an elemental function for Python that
    I haven't eventually found well-buried somewhere, e.g., os.urandom.

    See also: http://wiki.python.org/moin/glob
    See also: http://wiki.python.org/moin/PathClass
    """

    import glob

    def hitlist(patterns, quiet = ''):

            """
            Choose files and folders like Unix bash ls and rm -f do.

            That is, visit each pattern. Substitute the sorted list of files
            and folder that match if any files or folders do match. Leave
            patterns that match no files or folders in place unchanged
            ordinarily, but delete those patterns if asked to be quiet.

            See glob in: Unix man bash | col -b
            """

            results = []

            for pattern in patterns:
                    matches = glob.glob(pattern)
                    if matches:
                            matches.sort()
                            results += matches
                    elif not quiet:
                            results += [pattern]

            return results

    if __name__ == '__main__':

            import sys
            args = sys.argv[1:]

            if not len(args):
                    print "Usage: python hitlist.py [-f] 'pattern'"
            else:

                    quiet = args[0]
                    patterns = args[1:]
                    if quiet != '-f':
                            quiet = ''
                            patterns = args
                    print quiet, patterns

                    hits = hitlist(patterns, quiet)
                    for hit in hits:
                            print hit

------------------------------------------------------------------------

------------------------------------------------------------------------

[CategoryFaq](CategoryFaq)
