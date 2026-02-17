# PathClass

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

Björn Lindqvist restarted the discussion about getting Path into the stdlib in January. The PEP and reference implementation is available here: [PEP 355](http://www.python.org/dev/peps/pep-0355), [PathModule](PathModule), [PathModuleTests](PathModuleTests)

There are alternative proposals as well: [AlternativePathClass](AlternativePathClass), [AlternativePathDiscussion](AlternativePathDiscussion), [AlternativePathModuleTests](AlternativePathModuleTests)

# Path class Pre-Pre-PEP 

## Introduction 

The Python Standard Library currently has many modules that allow the developer to interact with the filesystem. Currently this set of modules is:

- os
- os.path
- fnmatch
- glob
- shutil
- stat

This PEP proposes that a new class or module be added to the Python Standard Library that will make all filesystem operations available from one place in a consistent way.

## Reference Implementation 

Reinhold has modified Jason Orendorff\'s original path.py to fit discussions in python-dev and comp.lang.python and has placed it in Python under nondist/sandbox/path: [http://svn.python.org/projects/sandbox/trunk/path/path.py](http://svn.python.org/projects/sandbox/trunk/path/path.py)

Other implementations to look at include the original, path.py and some things that others have mentioned on c.l.p. and python-dev.

Jason Orendorff\'s original path.py can be found here: [http://www.jorendorff.com/articles/python/path/](http://www.jorendorff.com/articles/python/path/)

## Motivation 

The motivation for a single standard class or module to handle filesystem operations is threefold:

- Reduce the number of modules a user must import and refer to to do common operations
- Aesthetics: code written with the reference implementation is more concise, easier to read, and also easier to write
- Consistency: All filesystem operations should be accessed from within the same module.

## Design Principles 

1\. A Path should be a drop-in replacement for a str or unicode as much as possible.

2\. Properties are the interface for actual attributes of a Path. For example, a Path\'s basename will be the same regardless of data on the local filesystem. Accessing a Path property will never result in an IOError.

3\. Methods are the interface for attributes of whatever the Path represents, for example, the last-modified-time or contents of a file. Calling a Path method may result in an IOError if the method accesses the actual filesystem and finds a problem (e.g. the Path refers to a nonexistent file).

4\. \[Done in CVS\] Should be subclassable so third parties can offer richer subclasses. Use `self.__class__()` instead of `Path()` in method bodies. Alternate constructors like `Path.cwd()` should be a class methods rather than static methods. ([MikeOrr](./MikeOrr.html))

## Backwards Compatibility 

If this PEP is accepted, then several of the existing standard modules will become redundant, which violates the [TOOWTDI](TOOWTDI) principle. The following modules will become redundant:

- os.path
- shutils
- fnmatch
- glob
- stat
- parts of os (like mkdir)

It is proposed that Python 2.5 will mark redundant modules as deprecated and issue a warning when they are imported. The functionality that these modules offer should be moved into the path module.

Python 2.6 will remove the redundant modules from the standard library.

## Open Issues 

- What to call this module / class, and where to put it?
- API issues with reference implementation:
  - Remove duplicate functionality:
    - .joinpath / .joinwith

  - Property / method consistency:
    - .parent -\> .dirname (and get rid of .dirname())

    - .name -\> .filename (and get rid of .basename())

    - .namebase -\> .filebase

    - .atime/.mtime/.ctime -\> .atime()/.mtime()/.ctime()

    - .size -\> .filesize()

  - .splitall() -\> .parts()

  - bytes() -\> get_bytes()

  - write_bytes() -\> set_bytes() / append_bytes()

  - text() -\> get_text()

  - write_text() -\> set_text() / append_text()

  - lines() -\> get_lines()

  - write_lines() -\> set_lines() / append_lines()

  - .joinpath(\*args) -\> .subpath(\*args)?

    - This needs consensus, I prefer .joinpath()

  - .listdir() -\> .subpaths() OR .listpaths()

  - drop .getcwd()?
    - default constructor could assign absolute cwd, or \".\"?

  - Should .mtime()/etc. return datetime objects?
    - I vote no, timestamps are fine

## Discussions 

- [http://sourceforge.net/tracker/index.php?func=detail&aid=1226256&group_id=5470&atid=355470](http://sourceforge.net/tracker/index.php?func=detail&aid=1226256&group_id=5470&atid=355470)

- [http://thread.gmane.org/gmane.comp.python.devel/69403](http://thread.gmane.org/gmane.comp.python.devel/69403)

- [http://mail.python.org/pipermail/python-dev/2005-June/054438.html](http://mail.python.org/pipermail/python-dev/2005-June/054438.html)

- [http://groups.google.ca/group/comp.lang.python/msg/822a302350658a01](http://groups.google.ca/group/comp.lang.python/msg/822a302350658a01)
