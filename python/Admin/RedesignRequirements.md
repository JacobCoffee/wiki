# Admin/RedesignRequirements

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# Goals for 2007 redesign 

- Rebuilding needs to be faster.
  - Global rebuilds could be very fast.
  - Or, a fast rebuild of a subtree or page needs to be easy.
- Must not require a massive restructuring of the current build/data tree. (We may or may not use nav.yml and the other files, but a new tool mustn\'t require some enormous transition process.)
- Continue supporting reST and hand-written HTML; we\'ll continue working on killing off the HTML, but don\'t want to make it dependent on that.
- Should be possible to include Wiki pages.
- Easier to build: e.g. use the current best-of-practice YAML parser, whatever that may be, instead of a custom wrapper.
- Should include a redirect list inside the pydotorg SVN, so that it doesn\'t require editing the Apache configs to move a page.
- Should use some 3rd-party Python library for templating.
- Should be usable as the back-end for generating pages on the fly in case python.org becomes fully dynamic. So generating a single page should be reasonably quick and not require any expensive operations.

## Tasks 

- Write conversion tool: YAML info to the navigation format.
- Fix encoding problems.
- Write redirection config. tool.

## Pyramid usage 

    amk@matterhorn:~/source/p/pyramid-trunk$ pyramid/pyramid --help
    usage: pyramid [options]

    options:
      -h, --help            show this help message and exit
      -d DATA, --data=DATA  directory in which the fragment data is stored
      -o OUT, --out=OUT     directory in which to save output (will be emptied)
      -r RESOURCES, --resources=RESOURCES
                            comma separated list of resource directories to copy
      -v, --verbose         print status messages to stdout
      -V, --veryverbose     print all data to stdout
      -W, --veryveryverbose
                            print all data to stdout
      -R REBUILDDIRS, --rebuilddirs=REBUILDDIRS
                            only rebuild below these comma separated directories
      -C, --createcache     recreate the cache files
      -c CONSTANTS, --constants=CONSTANTS
                            pass in the names constants (e.g.
                            PDO=/root/pdo,PSF=/psf
      -k, --keepgoing       keep going past errors if possible
      -U, --update          NOT WORKING DO NOT USE try to build only those pages
                            that have changed
      -n, --relativeurls    Converts urls from absolute to relative
      -P, --prettify        Prettify output - not used on live site
    amk@matterhorn:~/source/p/pyramid-trunk$
