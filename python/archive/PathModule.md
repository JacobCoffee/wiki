# PathModule

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

:::: 
::: 
``` 
   1 # -*- coding: iso-8859-1 -*-
   2 """ path.py - An object representing a path to a file or directory.
   3 
   4 Example:
   5 
   6 from path import path
   7 d = path('/home/guido/bin')
   8 for f in d.files('*.py'):
   9     f.chmod(0755)
  10 
  11 This module requires Python 2.2 or later.
  12 
  13 
  14 URL:     http://www.jorendorff.com/articles/python/path
  15 Author:  Jason Orendorff <jason@jorendorff.com> (and others - see the url!)
  16 Date:    7 Mar 2004
  17 
  18 Adapted for stdlib by: Reinhold Birkenfeld, July 2005
  19 Modified by Björn Lindqvist <bjourne@gmail.com>, January 2006
  20 """
  21 
  22 # TODO
  23 #   - Better error message in listdir() when self isn't a
  24 #     directory. (On Windows, the error message really sucks.)
  25 #   - Make sure everything has a good docstring.
  26 #   - Add methods for regex find and replace.
  27 #   - Perhaps support arguments to touch().
  28 #   - Could add split() and join() methods that generate warnings.
  29 #   - Note:  __add__() technically has a bug, I think, where
  30 #     it doesn't play nice with other types that implement
  31 #     __radd__().  Test this.
  32 
  33 import fnmatch
  34 import glob
  35 import os
  36 import shutil
  37 import sys
  38 
  39 __all__ = ['path']
  40 __version__ = '2.0.4'
  41 
  42 # Universal newline support
  43 _textmode = 'r'
  44 if hasattr(file, 'newlines'):
  45     _textmode = 'U'
  46 
  47 # Use unicode strings if possible
  48 _base = str
  49 if os.path.supports_unicode_filenames:
  50     _base = unicode
  51 
  52 
  53 class path(_base):
  54     """ Represents a filesystem path.
  55 
  56     For documentation on individual methods, consult their
  57     counterparts in os.path.
  58     """
  59 
  60     # --- Special Python methods.
  61     def __new__(typ, *args):
  62         """
  63         Creates a new path object concatenating the *args.  *args
  64         may only contain Path objects or strings.  If *args is
  65         empty, Path(os.curdir) is created.
  66         """
  67         if not args:
  68             return typ(os.curdir)
  69         for arg in args:
  70             if not isinstance(arg, basestring):
  71                 raise ValueError("%s() arguments must be Path, str or "
  72                                  "unicode" % typ.__name__)
  73         if len(args) == 1:
  74             return _base.__new__(typ, *args)
  75         return typ(os.path.join(*args))
  76         
  77     def __repr__(self):
  78         return '%s(%r)' % (self.__class__.__name__, _base(self))
  79 
  80     # Adding a path and a string yields a path.
  81     def __add__(self, more):
  82         return self.__class__(_base(self) + more)
  83 
  84     def __radd__(self, other):
  85         return self.__class__(other + _base(self))
  86 
  87     @classmethod
  88     def cwd(cls):
  89         """ Return the current working directory as a path object. """
  90         return path(os.getcwd())
  91 
  92     # --- Operations on path strings.
  93 
  94     def abspath(self):
  95         return self.__class__(os.path.abspath(self))
  96     
  97     def normcase(self):
  98         return self.__class__(os.path.normcase(self))
  99     
 100     def normpath(self):
 101         return self.__class__(os.path.normpath(self))
 102     
 103     def realpath(self):
 104         return self.__class__(os.path.realpath(self))
 105     
 106     def expanduser(self):
 107         return self.__class__(os.path.expanduser(self))
 108     
 109     def expandvars(self):
 110         return self.__class__(os.path.expandvars(self))
 111     
 112     def expand(self):
 113         """ Clean up a filename by calling expandvars(),
 114         expanduser(), and normpath() on it.
 115 
 116         This is commonly everything needed to clean up a filename
 117         read from a configuration file, for example.
 118         """
 119         return self.expandvars().expanduser().normpath()
 120 
 121     def _get_namebase(self):
 122         base, ext = os.path.splitext(self.name)
 123         return base
 124 
 125     def _get_ext(self):
 126         f, ext = os.path.splitext(_base(self))
 127         return ext
 128 
 129     def _get_drive(self):
 130         drive, r = os.path.splitdrive(self)
 131         return self.__class__(drive)
 132 
 133     def _get_dirname(self):
 134         return self.__class__(os.path.dirname(self))
 135     
 136     parent = property(
 137         _get_dirname, None, None,
 138         """ This path's parent directory, as a new path object.
 139 
 140         For example, path('/usr/local/lib/libpython.so').parent == path('/usr/local/lib')
 141         """)
 142 
 143     name = property(
 144         os.path.basename, None, None,
 145         """ The name of this file or directory without the full path.
 146 
 147         For example, path('/usr/local/lib/libpython.so').name == 'libpython.so'
 148         """)
 149 
 150     namebase = property(
 151         _get_namebase, None, None,
 152         """ The same as path.name, but with one file extension stripped off.
 153 
 154         For example, path('/home/guido/python.tar.gz').name     == 'python.tar.gz',
 155         but          path('/home/guido/python.tar.gz').namebase == 'python.tar'
 156         """)
 157 
 158     ext = property(
 159         _get_ext, None, None,
 160         """ The file extension, for example '.py'. """)
 161 
 162     drive = property(
 163         _get_drive, None, None,
 164         """ The drive specifier, for example 'C:'.
 165         This is always empty on systems that don't use drive specifiers.
 166         """)
 167 
 168     def splitpath(self):
 169         """ p.splitpath() -> Return (p.parent, p.name). """
 170         parent, child = os.path.split(self)
 171         return self.__class__(parent), child
 172 
 173     def stripext(self):
 174         """ p.stripext() -> Remove one file extension from the path.
 175 
 176         For example, path('/home/guido/python.tar.gz').stripext()
 177         returns path('/home/guido/python.tar').
 178         """
 179         return path(os.path.splitext(self)[0])
 180 
 181     if hasattr(os.path, 'splitunc'):
 182         def splitunc(self):
 183             unc, rest = os.path.splitunc(self)
 184             return self.__class__(unc), rest
 185 
 186         def _get_uncshare(self):
 187             unc, r = os.path.splitunc(self)
 188             return self.__class__(unc)
 189 
 190         uncshare = property(
 191             _get_uncshare, None, None,
 192             """ The UNC mount point for this path.
 193             This is empty for paths on local drives. """)
 194 
 195     def splitall(self):
 196         """ Return a list of the path components in this path.
 197 
 198         The first item in the list will be a path.  Its value will be
 199         either os.curdir, os.pardir, empty, or the root directory of
 200         this path (for example, '/' or 'C:\\').  The other items in
 201         the list will be strings.
 202 
 203         path.path(*result) will yield the original path.
 204         """
 205         parts = []
 206         loc = self
 207         while loc != os.curdir and loc != os.pardir:
 208             prev = loc
 209             loc, child = prev.splitpath()
 210             loc = self.__class__(loc)
 211             if loc == prev:
 212                 break
 213             parts.append(child)
 214         parts.append(loc)
 215         parts.reverse()
 216         return parts
 217 
 218     def relpath(self):
 219         """ Return this path as a relative path,
 220         based from the current working directory.
 221         """
 222         return self.__class__.cwd().relpathto(self)
 223 
 224     def relpathto(self, dest):
 225         """ Return a relative path from self to dest.
 226 
 227         If there is no relative path from self to dest, for example if
 228         they reside on different drives in Windows, then this returns
 229         dest.abspath().
 230         """
 231         origin = self.abspath()
 232         dest = self.__class__(dest).abspath()
 233 
 234         orig_list = origin.normcase().splitall()
 235         # Don't normcase dest!  We want to preserve the case.
 236         dest_list = dest.splitall()
 237 
 238         if orig_list[0] != os.path.normcase(dest_list[0]):
 239             # Can't get here from there.
 240             return dest
 241 
 242         # Find the location where the two paths start to differ.
 243         i = 0
 244         for start_seg, dest_seg in zip(orig_list, dest_list):
 245             if start_seg != os.path.normcase(dest_seg):
 246                 break
 247             i += 1
 248 
 249         # Now i is the point where the two paths diverge.
 250         # Need a certain number of "os.pardir"s to work up
 251         # from the origin to the point of divergence.
 252         segments = [os.pardir] * (len(orig_list) - i)
 253         # Need to add the diverging part of dest_list.
 254         segments += dest_list[i:]
 255         if len(segments) == 0:
 256             # If they happen to be identical, use os.curdir.
 257             return self.__class__(os.curdir)
 258         else:
 259             return self.__class__(os.path.join(*segments))
 260 
 261 
 262     # --- Listing, searching, walking, and matching
 263 
 264     def listdir(self, pattern=None):
 265         """ D.listdir() -> List of items in this directory.
 266 
 267         Use D.files() or D.dirs() instead if you want a listing
 268         of just files or just subdirectories.
 269 
 270         The elements of the list are path objects.
 271 
 272         With the optional 'pattern' argument, this only lists
 273         items whose names match the given pattern.
 274         """
 275         names = os.listdir(self)
 276         if pattern is not None:
 277             names = fnmatch.filter(names, pattern)
 278         return [path(self, child) for child in names]
 279 
 280     def dirs(self, pattern=None):
 281         """ D.dirs() -> List of this directory's subdirectories.
 282 
 283         The elements of the list are path objects.
 284         This does not walk recursively into subdirectories
 285         (but see path.walkdirs).
 286 
 287         With the optional 'pattern' argument, this only lists
 288         directories whose names match the given pattern.  For
 289         example, d.dirs('build-*').
 290         """
 291         return [p for p in self.listdir(pattern) if p.isdir()]
 292 
 293     def files(self, pattern=None):
 294         """ D.files() -> List of the files in this directory.
 295 
 296         The elements of the list are path objects.
 297         This does not walk into subdirectories (see path.walkfiles).
 298 
 299         With the optional 'pattern' argument, this only lists files
 300         whose names match the given pattern.  For example,
 301         d.files('*.pyc').
 302         """
 303         
 304         return [p for p in self.listdir(pattern) if p.isfile()]
 305 
 306     def walk(self, pattern=None):
 307         """ D.walk() -> iterator over files and subdirs, recursively.
 308 
 309         The iterator yields path objects naming each child item of
 310         this directory and its descendants.  This requires that
 311         D.isdir().
 312 
 313         This performs a depth-first traversal of the directory tree.
 314         Each directory is returned just before all its children.
 315         """
 316         for child in self.listdir():
 317             if pattern is None or child.match(pattern):
 318                 yield child
 319             if child.isdir():
 320                 for item in child.walk(pattern):
 321                     yield item
 322 
 323     def walkdirs(self, pattern=None):
 324         """ D.walkdirs() -> iterator over subdirs, recursively.
 325 
 326         With the optional 'pattern' argument, this yields only
 327         directories whose names match the given pattern.  For
 328         example, mydir.walkdirs('*test') yields only directories
 329         with names ending in 'test'.
 330         """
 331         for child in self.dirs():
 332             if pattern is None or child.match(pattern):
 333                 yield child
 334             for subsubdir in child.walkdirs(pattern):
 335                 yield subsubdir
 336 
 337     def walkfiles(self, pattern=None):
 338         """ D.walkfiles() -> iterator over files in D, recursively.
 339 
 340         The optional argument, pattern, limits the results to files
 341         with names that match the pattern.  For example,
 342         mydir.walkfiles('*.tmp') yields only files with the .tmp
 343         extension.
 344         """
 345         for child in self.listdir():
 346             if child.isfile():
 347                 if pattern is None or child.match(pattern):
 348                     yield child
 349             elif child.isdir():
 350                 for f in child.walkfiles(pattern):
 351                     yield f
 352 
 353     def match(self, pattern):
 354         """ Return True if self.name matches the given pattern.
 355 
 356         pattern - A filename pattern with wildcards,
 357             for example '*.py'.
 358         """
 359         return fnmatch.fnmatch(self.name, pattern)
 360 
 361     def matchcase(self, pattern):
 362         """ Test whether the path matches pattern, returning true or
 363         false; the comparison is always case-sensitive.
 364         """
 365         return fnmatch.fnmatchcase(self.name, pattern)
 366 
 367     def glob(self, pattern):
 368         """ Return a list of path objects that match the pattern.
 369 
 370         pattern - a path relative to this directory, with wildcards.
 371 
 372         For example, path('/users').glob('*/bin/*') returns a list
 373         of all the files users have in their bin directories.
 374         """
 375         return map(path, glob.glob(_base(path(self, pattern))))
 376 
 377     # --- Methods for querying the filesystem.
 378 
 379     exists = os.path.exists
 380     isabs = os.path.isabs
 381     isdir = os.path.isdir
 382     isfile = os.path.isfile
 383     islink = os.path.islink
 384     ismount = os.path.ismount
 385 
 386     if hasattr(os.path, 'samefile'):
 387         samefile = os.path.samefile
 388 
 389     def atime(self):
 390         """Last access time of the file."""
 391         return os.path.getatime(self)
 392 
 393     def mtime(self):
 394         """Last-modified time of the file."""
 395         return os.path.getmtime(self)
 396 
 397     def ctime(self):
 398         """
 399         Return the system's ctime which, on some systems (like Unix)
 400         is the time of the last change, and, on others (like Windows),
 401         is the creation time for path.
 402 
 403         The return value is a number giving the number of seconds
 404         since the epoch (see the time module). Raise os.error if the
 405         file does not exist or is inaccessible.
 406         """
 407         return os.path.getctime(self)
 408 
 409     def size(self):
 410         """Size of the file, in bytes."""
 411         return os.path.getsize(self)
 412 
 413     if hasattr(os, 'access'):
 414         def access(self, mode):
 415             """ Return true if current user has access to this path.
 416 
 417             mode - One of the constants os.F_OK, os.R_OK, os.W_OK, os.X_OK
 418             """
 419             return os.access(self, mode)
 420 
 421     def stat(self):
 422         """ Perform a stat() system call on this path. """
 423         return os.stat(self)
 424 
 425     def lstat(self):
 426         """ Like path.stat(), but do not follow symbolic links. """
 427         return os.lstat(self)
 428 
 429     if hasattr(os, 'statvfs'):
 430         def statvfs(self):
 431             """ Perform a statvfs() system call on this path. """
 432             return os.statvfs(self)
 433 
 434     if hasattr(os, 'pathconf'):
 435         def pathconf(self, name):
 436             return os.pathconf(self, name)
 437 
 438 
 439     # --- Modifying operations on files and directories
 440 
 441     def utime(self, times):
 442         """ Set the access and modified times of this file. """
 443         os.utime(self, times)
 444 
 445     def chmod(self, mode):
 446         os.chmod(self, mode)
 447 
 448     if hasattr(os, 'chown'):
 449         def chown(self, uid, gid):
 450             os.chown(self, uid, gid)
 451 
 452     def rename(self, new):
 453         os.rename(self, new)
 454 
 455     def renames(self, new):
 456         os.renames(self, new)
 457 
 458 
 459     # --- Create/delete operations on directories
 460 
 461     def mkdir(self, mode=0777):
 462         os.mkdir(self, mode)
 463 
 464     def makedirs(self, mode=0777):
 465         os.makedirs(self, mode)
 466 
 467     def rmdir(self):
 468         os.rmdir(self)
 469 
 470     def removedirs(self):
 471         os.removedirs(self)
 472 
 473 
 474     # --- Modifying operations on files
 475 
 476     def touch(self):
 477         """ Set the access/modified times of this file to the current time.
 478         Create the file if it does not exist.
 479         """
 480         fd = os.open(self, os.O_WRONLY | os.O_CREAT, 0666)
 481         os.close(fd)
 482         os.utime(self, None)
 483 
 484     def remove(self):
 485         os.remove(self)
 486 
 487     def unlink(self):
 488         os.unlink(self)
 489 
 490 
 491     # --- Links
 492 
 493     if hasattr(os, 'link'):
 494         def link(self, newpath):
 495             """ Create a hard link at 'newpath', pointing to this file. """
 496             os.link(self, newpath)
 497 
 498     if hasattr(os, 'symlink'):
 499         def symlink(self, newlink):
 500             """ Create a symbolic link at 'newlink', pointing here. """
 501             os.symlink(self, newlink)
 502 
 503     if hasattr(os, 'readlink'):
 504         def readlink(self):
 505             """ Return the path to which this symbolic link points.
 506 
 507             The result may be an absolute or a relative path.
 508             """
 509             return self.__class__(os.readlink(self))
 510 
 511         def readlinkabs(self):
 512             """ Return the path to which this symbolic link points.
 513 
 514             The result is always an absolute path.
 515             """
 516             p = self.readlink()
 517             if p.isabs():
 518                 return p
 519             else:
 520                 return self.__class__(self.parent, p).abspath()
 521 
 522 
 523     # --- High-level functions from shutil
 524 
 525     copyfile = shutil.copyfile
 526     copymode = shutil.copymode
 527     copystat = shutil.copystat
 528     copy = shutil.copy
 529     copy2 = shutil.copy2
 530     copytree = shutil.copytree
 531     if hasattr(shutil, 'move'):
 532         move = shutil.move
 533     rmtree = shutil.rmtree
 534 
 535 
 536     # --- Special stuff from os
 537 
 538     if hasattr(os, 'chroot'):
 539         def chroot(self):
 540             os.chroot(self)
```
:::
::::
