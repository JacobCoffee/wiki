# AlternativePathClass

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

This page describes directory-based path classes, an alternative to [PEP 355](http://www.python.org/dev/peps/pep-0355/) which is string-based.

***Please keep the proposals internally consistent and according to the authors\' intentions.*** You can state objections in the Comment section under each proposal, or in the general topic sections below the proposals.

------------------------------------------------------------------------

# Proposal #1 (Noam Raphael) 

The source can be found in [AlternativePathModule](AlternativePathModule).

## Introduction 

Hello,

I saw the discussion about including the [path type](PathClass) in the standard library. As it turned out, I recently wrote a program which does quite a lot of path manipulation. This caused me to think that the proposed path module:

- Makes path manipulation significantly easier
- Can be improved.

So I tried to write my version of it. You can download it from the page [AlternativePathModule](AlternativePathModule), and say what you think about it.

My basic problem with the current proposed path module is that it\'s a bit\... messy. It contains a lot of methods, collected from various modules, and for me it looks too crowded - there are too many methods and too many details for me to easily learn.

So I tried to organize it all. The following section describes the changes. I think that the result may make file and path manipulation really easier. All these are ideas - I would like to hear what you think about them.

## Major Changes 

### a tuple instead of a string 

The biggest conceptual change is that my path object is a subclass of *tuple* rather than *str*. For example,

    >>> tuple(path('a/b/c'))
    ('a', 'b', 'c')
    >>> tuple(path('/a/b/c'))
    (path.ROOT, 'a', 'b', 'c')

This means that path objects aren\'t the string representation of a path; they are a *logical* representation of a path. Remember why a filesystem path is called a path - because it\'s a way to get from one place on the filesystem to another. Paths can be relative, which means that they don\'t define from where to start the walk, and can be not relative, which means that they do. In the tuple representation, relative paths are simply tuples of strings, and not relative paths are tuples of strings with a first \"root\" element.

The advantage of using a logical representation is that you can forget about the textual one, which can be really complex. You don\'t have to call normpath when you\'re unsure about how a path looks, you don\'t have to search for seps and altseps, and\... you don\'t need to remember a lot of names of functions or methods. To show that, take a look at those methods from the original path class and their equivalent in my path class:

    p.normpath()  -> Isn't needed - done by the constructor
    p.basename()  -> p[-1]
    p.splitpath() -> (p[:-1], p[-1])
    p.splitunc()  -> (p[0], p[1:]) (if isinstance(p[0], path.UNCRoot))
    p.splitall()  -> Isn't needed
    p.parent      -> p[:-1]
    p.name        -> p[-1]
    p.drive       -> p[0] (if isinstance(p[0], path.Drive))
    p.uncshare    -> p[0] (if isinstance(p[0], path.UNCRoot))

    and of course:
    p.join(q) [or anything like it] -> p + q

The only drawback I can see in using a logical representation is that giving a path object to functions which expect a path string won\'t work. The immediate solution is to simply use str(p) instead of p. The long-term solution is to make all related functions accept a path object.

Having a logical representation of a path calls for a bit of term clearing-up. What\'s an absolute path? On POSIX, it\'s very simple: a path starting with a \'/\'. But what about Windows? Is \"\\temp\\file\" an absolute path? I claim that it isn\'t really. The reason is that if you change the current working directory, its meaning changes: It\'s now not \"c:\\temp\\file\", but \"a:\\temp\\file\". The same goes for \"c:temp\\file\". So I decided on these two definitions:

- A *relative path* is a path without a root element, so it can be concatenated to other paths.

- An *absolute path* is a path whose meaning doesn\'t change when the current working directory changes.

This means that paths starting with a drive letter alone (UnrootedDrive instance, in my module) and paths starting with a backslash alone (the CURROOT object, in my module) are not relative and not absolute.

I really think that it\'s a better way to handle paths. If you want an example, compare the current implementation of relpathto and my implementation.

### Easier attributes for stat objects 

The current path objects includes:

- isdir, isfile, islink, and -
- atime, mtime, ctime, size.

The first line does file mode checking, and the second simply gives attributes from the stat object.

I suggest that these should be added to the stat_result object. isdir, isfile and islink are true if a specific bit in st_mode is set, and atime, mtime, ctime and size are simply other names for st_atime, st_mtime, st_ctime and st_size.

It means that instead of using the atime, mtime etc. methods, you will write ` p.stat().atime `, ` p.stat().size `, etc.

This is good, because:

- If you want to make only one system call, it\'s very easy to save the stat object and use it.

- If you have to deal with symbolic links, you can simply use ` p.lstat().mtime `. Yes, symbolic links have a modification time. The alternative is to add three methods with ugly names (latime, lmtime, lctime) or to have an incomplete interface without a good reason.

I think that isfile, isdir should be kept (along with lisfile, lisdir), since I think that doing what they do is quite common, and requires six lines:

    try:
        st = p.stat()
    except OSError:
        return False
    else:
        return st.isdir

I think that still, isdir, isfile and islink should be added to stat_result objects: They turned out pretty useful in writing some of the more complex path methods.

### One Method for Finding Files 

(They\'re actually two, but with exactly the same interface). The original path object has these methods for finding files:

    def listdir(self, pattern = None): ...
    def dirs(self, pattern = None): ...
    def files(self, pattern = None): ...
    def walk(self, pattern = None): ...
    def walkdirs(self, pattern = None): ...
    def walkfiles(self, pattern = None): ...
    def glob(self, pattern):

I suggest one method that replaces all those:

    def glob(self, pattern='*', topdown=True, onlydirs=False, onlyfiles=False): ...

pattern is the good old glob pattern, with one additional extension: \"\*\*\" matches any number of subdirectories, including 0. This means that \'\*\*\' means \"all the files in a directory\", \'\*\*/a\' means \"all the files in a directory called a\", and \'\*\*/a\*/\*\*/b\*\' means \"all the files in a directory whose name starts with \'b\' and the name of one of their parent directories starts with \'a\'\".

onlydirs and onlyfiles filter the results (they can\'t be combined, of course). topdown has the same meaning as in os.walk (it isn\'t supported by the original path class). So, let\'s show how these methods can be replaced:

    p.listdir()   -> p.glob()
    p.dirs()      -> p.glob(onlydirs=1)
    p.files()     -> p.glob(onlyfiles=1)
    p.walk()      -> p.glob('**')
    p.walkdirs()  -> p.glob('**', onlydirs=1)
    p.walkfiles() -> p.glob('**', onlyfiles=1)
    p.glob(patt)  -> p.glob(patt)

Now, for the promised additional method. The current implementation of glob doesn\'t follow symbolic links. In my implementation, there\'s \"lglob\", which does what the current glob does. However, the (default) glob does follow symbolic links. To avoid infinite recursion, it keeps the set of filesystem ids on the current path, and checks each dir to see if it was already encountered. (It does so only if there\'s \'\*\*\' in the pattern, because otherwise a finite number of results is guaranteed.) Note that it doesn\'t keep the ids of all the files traversed, only those on the path from the base node to the current node. This means that as long as there\'re no cycles, everything will go fine - for example, \'a\' and \'b\' pointing at the same dir will just cause the same files to be reported twice, once under \'a\' and once under \'b\'. One last note: On windows there are no file ids, but there are no symbolic links, so everything is fine.

Oh, and it returns an iterator, not a list.

### Separation of Calculations and System Calls 

I like to know when I\'m using system calls and when I don\'t. It turns out that using tuples instead of strings makes it possible to define all operations which do not use system calls as properties or operators, and all operations which do use system calls as methods.

The only exception currently is .match(). What can I do?

### Reduce the Number of Methods 

I think that the number of methods should be reduced. The most obvious example are the copy functions. In the current proposal:

    def copyfile(self, dst): ...
    def copymode(self, dst): ...
    def copystat(self, dst): ...
    def copy(self, dst): ...
    def copy2(self, dst): ...

In my proposal:

    def copy(self, dst, copystat=False): ...

It\'s just that I think that copyfile, copymode and copystat aren\'t usually useful, and there\'s no reason not to unite copy and copy2.

## Other Changes 

Here is a list of the smaller things I\'ve changed in my proposal.

The current normpath removes \'..\' with the name before them. I didn\'t do that, because it doesn\'t return an equivalent path if the path before the \'..\' is a symbolic link.

I removed the methods associated with file extensions. I don\'t recall using them, and since they\'re purely textual and not OS-dependent, I think that you can always do p\[-1\].rsplit(\'.\', 1).

I removed renames. Why not use makedirs, rename, removedirs?

I removed unlink. It\'s an alias to remove, as far as I know.

I removed expand. There\'s no need to use normpath, so it\'s equivalent to .expanduser().expandvars(), and I think that the explicit form is better.

removedirs - I added another argument, basedir, which won\'t be removed even if it\'s empty. I also allowed the first directory to be unempty (I required that it should be a directory). This version is useful for me.

readlinkabs - The current path class returns abspath(readlink). This is meaningless - symbolic links are interpreted relative to the directory they are in, not relative the the current working directory of the program. Instead, I wrote readlinkpath, which returns the correct path object. However, I\'m not sure if it\'s needed - why not use realpath()?

copytree - I removed it. In shutil it\'s documented as being mostly a demonstration, and I\'m not sure if it\'s really useful.

symlink - Instead of a function like copy, with the destination as the second (actually, the only) argument, I wrote \"writelink\", which gets a string and creates a symbolic link with that value. The reason is that symbolic links can be any string, not necessarily a legal path.

I added mknod and mkfifo, which from some reason weren\'t there.

I added chdir, which I don\'t see why shouldn\'t be defined.

relpathto - I used realpath() instead of abspath(). abspath() may be incorrect if some of the dirs are symlinks.

I removed relpath. It doesn\'t seem useful to me, and I think that writing path.cwd().relpathto(p) is easy enough.

join - I decided that p+q should only work if q is a relative path. In my first implementation, it returned q, which is consistent with the current os.path.join(). However, I think that in the spirit of \"explicit is better than implicit\", a code like

    if q.isrel:
        return p + q
    else:
        return q

is pretty easy and pretty clear. I think that many times you want q to be relative, so an exception if it isn\'t would be helpful. I also think that it\'s nice that ` len(p+q) == len(p) + len(q) `.

match - The current implementation matches the base name of the path against a pattern. My implementation matches a relative path against a pattern, which is also a relative path (it\'s of the same form as the pattern of glob - may include \'\*\*\')

matchcase - I removed it. If you see a reason for keeping it, tell me.

## Comparison to the Current Path Class 

Here\'s a comparison of doing things using the current path class and doing things using my proposed path class.

    # Operations on path strings:
    p.cwd()        -> p.cwd()
    p.abspath()    -> p.abspath()
    p.normcase()   -> p.normcase
    Also added p.normcasestr, to normalize path elements.
    p.normpath()   -> Unneeded
    p.realpath()   -> p.realpath()
    p.expanduser() -> p.expanduser()
    p.expandvars() -> p.expandvars()
    p.basename()   -> p[-1]
    p.expand()     -> p.expanduser().expandvars()
    p.splitpath()  -> Unneeded
    p.stripext()   -> p[-1].rsplit('.', 1)[0]
    p.splitunc()   -> Unneeded
    p.splitall()   -> Unneeded
    p.relpath()    -> path.cwd().relpathto(p)
    p.relpathto(dst) -> p.relpathto(dst)

    # Properties about the path:
    p.parent       -> p[:-1]
    p.name         -> p[-1]
    p.ext          -> ''.join(p[-1].rsplit('.', 1)[1:])
    p.drive        -> p[0] if p and isinstance(p[0], path.Drive) else None
    p.namebase     -> p[-1].rsplit('.', 1)[0]
    p.uncshare     -> p[0] if p and isinstance(p[0], path.UNCRoot) else None

    # Operations that return lists of paths:
    p.listdir()    -> p.glob()
    p.listdir(patt)-> p.glob(patt)
    p.dirs()       -> p.glob(onlydirs=1)
    p.dirs(patt)   -> p.glob(patt, onlydirs=1)
    p.files()      -> p.glob(onlyfiles=1)
    p.files(patt)  -> p.glob(patt, onlyfiles=1)
    p.walk()       -> p.glob('**')
    p.walk(patt)   -> p.glob('**/patt')
    p.walkdirs()   -> p.glob('**', onlydirs=1)
    p.walkdirs(patt) -> p.glob('**/patt', onlydirs=1)
    p.walkfiles()  -> p.glob('**', onlyfiles=1)
    p.walkfiles(patt) -> p.glob('**/patt', onlyfiles=1)
    p.match(patt)  -> p[-1:].match(patt)
    (The current match matches the base name. My matches a relative path)
    p.matchcase(patt) -> Removed
    p.glob(patt)   -> p.glob(patt)

    # Methods for retrieving information about the filesystem
    # path:
    p.exists()     -> p.exists()
    Added p.lexists()
    p.isabs()      -> not p.isrel
    (That's the meaning of the current isabs().)
    Added p.isabs
    p.isdir()      -> p.isdir()
    Added p.lisdir()
    p.isfile()     -> p.isfile()
    Added p.lisfile()
    p.islink()     -> p.islink()
    p.ismount()    -> p.ismount()
    p.samefile(other) -> p.samefile(other)
    p.getatime()   -> p.stat().atime
    p.getmtime()   -> p.stat().mtime
    p.getctime()   -> p.stat().ctime
    p.getsize()    -> p.stat().size
    p.access(mode) -> p.access(mode)
    p.stat()       -> p.stat()
    p.lstat()      -> p.lstat()
    p.statvfs()    -> p.statvfs()
    p.pathconf(name) -> p.pathconf(name)

    # Filesystem properties for path.
    atime, mtime, ctime, size - Removed

    # Methods for manipulating information about the filesystem
    # path.
    utime, chmod, chown, rename - unchanged
    p.renames(new)   -> new[:-1].makedirs(); p.rename(new); p[:-1].removedirs()

    # Create/delete operations on directories
    mkdir, makedirs, rmdir, removedirs - unchanged (added an option to removedirs)

    # Modifying operations on files
    touch, remove - unchanged
    unlink - removed

    # Modifying operations on links
    p.link(newpath)   -> p.link(newpath)
    p.symlink(newlink) -> newlink.writelink(p)
    p.readlink()      -> p.readlink()
    p.readlinkabs()   -> p.readlinkpath()

    # High-level functions from shutil
    copyfile, copymode, copystat, copytree - removed
    p.copy(dst)   -> p.copy(dst)
    p.copy2(dst)  -> p.copt(dst, copystat=1)
    move, rmtree - unchanged.

    # Special stuff from os
    chroot, startfile - unchanged.

## Open Issues 

Unicode - I have no idea about unicode paths. My current implementation simply uses str. This should be changed, I guess.

Slash-terminated paths - In my current implementation, paths ending with a slash are normalized to paths without a slash (this is also the behaviour of os.path.normpath). However, they aren\'t really the same: stat() on paths ending with a slash fails if they aren\'t directories, and lstat() treats them as directories even if they are symlinks. Perhaps a final empty string should be allowed.

## Comments on proposal #1 

Please write here comments. Thanks!

------------------------------------------------------------------------

# Proposal #2 (Mike Orr) 

Two classes in os.path: [FilePath](./FilePath.html), [DirectoryPath](./DirectoryPath.html). These are defined in posixpath, ntpath, etc. Inheritance graph:

- posixpath.[FilePath](./FilePath.html) -\> basepath.[FilePath](./FilePath.html) -\> basepath.Path -\> object

  posixpath.[DirectoryPath](./DirectoryPath.html) -\> basepath.[DirectoryPath](./DirectoryPath.html) -\> basepath.[BasePath](./BasePath.html) -\> object

Both describe a path via their attributes, including a tuple of directory components. For [DirectoryPath](./DirectoryPath.html), all components are directories. For [FilePath](./FilePath.html), the final component is a non-directory. The filesystem object described by the path may or may not exist. If a method is called that depends on an existing directory but a file is found instead, or vice versa, raise [DirectoryError](./DirectoryError.html) (subclass of [PathError](./PathError.html)).

Paths are immutable and may be used as dictionary keys. .[str]() returns the string equivalent. The open() builtin should accept Path objects. Paths use unicode internally.

XXX TODO: Split the combined Path below and Noam\'s class above into [FilePath](./FilePath.html) and [DirectoryPath](./DirectoryPath.html).

    class Path(object):     

    Class attributes:
        sep
        extsep
        curdir
        pardir

    Constructors:
        Path(s)           # Create Path from string/unicode.
        Path(s, encoding="latin1", errors="strict")
                          # Same but use non-default encoding.
        Path()            # Same as Path(Path.curdir)
        Path.cwd()        # Same as Path(os.getcwd())
        Path.cwd("c:")    # Get current directory for specified drive.

    Instance attributes:  (immutable, set by constructor)
        root      # "" for relative, "/" for Unix absolute, r"C:\" for
                  # Windows absolute, r"C:" for Windows relative,
                  # r"\\HOST" for Windows UNC share, "http://host/" for
                  # URL.  Actual value may differ from this spec.

        path      # Tuple of directory components.  The last may be a
                  # non-directory.
        name      # Same as path[-1] without extension.
        ext       # Extension without separator; "" if none.
        isabsolute    # Is .root absolute?

    Methods:  same as proposal #1 except...
        p + SEQUENCE  # Similar to os.path.join().  (String incompatible!)

        Replace method .glob with:
        listdir(pattern=None, names_only=False)
                      # List of paths in directory matching 'pattern'.
                      # If 'names_only' is true, same as os.listdir(self).
        files(pattern=None, symlinks=True)
                      # Same but return only regular files.  If 
                      # 'symlinks' is false, do not follow symbolic links.
        dirs(pattern=None, symlinks=True)
                      # Same but return only directories.
        symlinks(pattern=None)
                      # Return only symbolic links.
        # To find other device files, use .listdir().
        walk(pattern=None, symlinks=True, topdown=True, onerror=None)
                      # Recursively yield paths.  XXX What does onerror
                      # do?
        walkfiles(pattern=None, symlinks=True, onerror=None)
        walkdirs(pattern=None, symlinks=True, onerror=None)
        walklinks(pattern=None, onerror=None)

        copy(dst, content=True, mode=True, time=False)

        mkdir() and rmdir() succeed if the operation is already done.

        purge()       # Delete file or directory recursively if exists.

        symlink_to(s)  # Make self a symbolic link to s (Path or string).
                       # Drop method .writelink().

        symlink(p, absolute)     # Make path p a symbolic link to self.
                       # 'absolute' is boolean.  Difficult to determine
                       # number of ".." for relative?

        expand()       # Same as .expanduser().expandvars().

[MutablePath](./MutablePath.html) is a subclass that\'s mutable, so it cannot be used as a dictionary key. The .path attribute is a list.

## Open issues 

Should \*Path subclass str or unicode? Advantages: drop-in replacement for string paths. Disadvantages: str/unicode dichotomy, can\'t use p[-N](./(2d)N.html) to return a derived path with N directories dropped.

Rename [FilePath](./FilePath.html) to Path, and Path to [BasePath](./BasePath.html)?

Should .isdir() etc be Path methods or should one do p.stat().isdir?

Consider using .delete() instead of .remove() or .unlink().

Should Path and [MutablePath](./MutablePath.html) be called [FrozenPath](./FrozenPath.html) and Path? Or frozenpath and path?

## Comments on proposal #2 

None yet.

------------------------------------------------------------------------

# Summary of Python-dev discussion 

Threads:

- [http://mail.python.org/pipermail/python-dev/2006-April/063977.html](http://mail.python.org/pipermail/python-dev/2006-April/063977.html)

- [http://mail.python.org/pipermail/python-dev/2006-May/064745.html](http://mail.python.org/pipermail/python-dev/2006-May/064745.html)

- [http://mail.python.org/pipermail/python-dev/2006-May/064749.html](http://mail.python.org/pipermail/python-dev/2006-May/064749.html)

- [http://mail.python.org/pipermail/python-dev/2006-May/064802.html](http://mail.python.org/pipermail/python-dev/2006-May/064802.html) (proposal #1)

There is general agreement for a new PEP containing one of these proposals.

Guido is not convinced that PEP 355 or these proposals are necessarily better than the existing os.path module. He\'s not following this discussion but will answer short (\<= 20-line) requests for pronouncements cc\'d to both him and python-dev.

Inclusion in Python 2.6 is possible if we agree on an implementation in several months and release it in the Cheeseshop.

Alyssa Coghlan suggests paired walk methods:

       # Do path.walk over this directory, and also return the corresponding
      # information for a destination directory (so the dest dir information
      # probably *won't* match that file system
      for src_info, dest_info in src_path.pairedwalk(dest_path):
          src_dirpath, src_subdirs, src_files = src_info
          dest_dirpath, dest_subdirs, dest_files = dest_info
          # Do something useful

      # Ditto for path.walkdirs
      for src_dirpath, dest_dirpath in src_path.pairedwalkdirs(dest_path):
          # Do something useful

      # Ditto for path.walkfiles
      for src_path, dest_path in src_path.pairedwalkfiles(dest_path):
          src_path.copy_to(dest_path)

What should happen to the os.path functions and other redundancies?

- Leave them alone because they work and existing programs depend on them.
- Discourage their use in the documentation but continue to support them.
- Rewrite them to use their Path counterparts. This is a lot of useless work if we\...
- Remove them in Python 3.0.

Greg Ewing suggested splitting the filename on .extsep. Alyssa Coghlan and Mike Orr pointed out that extensions are merely conventions on some OSes, and the user has to tell us which apparent extensions to consider as extensions. How many extensions does \"foo.2006-02-12.tar.gz\" have? \"foo.2006.02.12.tar.gz\"? And directories normally do \*not\* have extensions (\"cron.daily\", \"modules.autoload.d\").
