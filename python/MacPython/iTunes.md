# MacPython/iTunes

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

Does anyone know how to add a track to a playlist using appscript?

Maybe something like this:

def add to playlist(a, t, pl ):

- a.duplicate( t, to=pl )

Find a connected ipod making no assumptions about the name of the ipod:

------------------------------------------------------------------------

from appscript import \*

def find_ipod( a ):

- for src in a.sources.get():
  - if src.kind.get() == k.iPod:
    - return src

ipod = find_ipod( app(\'Itunes\') )

------------------------------------------------------------------------

Find the library making no assumptions about the name of the library (e.g. for non-english versions of itunes it\'s not \"Library\"):

------------------------------------------------------------------------

from appscript import \*

def find_library( a ):

- for src in a.sources.get():
  - if src.kind.get() == k.library:
    - return src

library = find_library( app(\'Itunes\') )

------------------------------------------------------------------------

Create a new playlist on a certain source (i.e. either the library or an ipod, as returned from one of the functions above).

------------------------------------------------------------------------

src.make( new=k.user_playlist, with_properties={k.name: \'My new playlist\'} )

------------------------------------------------------------------------
