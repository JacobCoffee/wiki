# AlternativePathModule

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

:::: 
::: 
``` 
   1 """ path.py - An object representing a path to a file or a directory.
   2 
   3 Based on the path module by Jason Orendorff
   4 (http://www.jorendorff.com/articles/python/path)
   5 
   6 Written by Noam Raphael to show the idea of using a tuple instead of
   7 a string, and to reduce the number of methods.
   8 
   9 Currently only implements posix and nt paths - more can be added.
  10 
  11 """
  12 
  13 import os
  14 import stat
  15 import itertools
  16 import fnmatch
  17 import re
  18 import string
  19 
  20 class StatWrapper(object):
  21     """ A wrapper around stat_result objects which gives additional properties.
  22     
  23     This object is a wrapper around a stat_result object. It allows access
  24     to all the original object's attributes, and adds a few convinient
  25     properties, by using the stat module.
  26     
  27     This object should have been a subclass posix.stat_result - it simply
  28     isn't possible currently. This functionality may also be integrated into
  29     the original type.
  30     """
  31     
  32     __slots__ = ['_stat']
  33     
  34     def __init__(self, stat):
  35         self._stat = stat
  36         
  37     def __getattribute__(self, attr, *default):
  38         try:
  39             return object.__getattribute__(self, attr, *default)
  40         except AttributeError:
  41             return getattr(self._stat, attr, *default)
  42 
  43     # Mode properties
  44     
  45     @property
  46     def isdir(self):
  47         return stat.S_ISDIR(self.st_mode)
  48     @property
  49     def isfile(self):
  50         return stat.S_ISREG(self.st_mode)
  51     @property
  52     def islink(self):
  53         return stat.S_ISLNK(self.st_mode)
  54     
  55     # Easier names properties
  56 
  57     @property
  58     def size(self):
  59         return self.st_size
  60     @property
  61     def mtime(self):
  62         return self.st_mtime
  63     @property
  64     def atime(self):
  65         return self.st_atime
  66     @property
  67     def ctime(self):
  68         return self.st_ctime
  69 
  70 
  71 class BasePath(tuple):
  72     """ The base, abstract, path type.
  73     
  74     The OS-specific path types inherit from it.
  75     """
  76 
  77     # ----------------------------------------------------------------
  78     # We start with methods which don't use system calls - they just
  79     # manipulate paths.
  80 
  81     class _BaseRoot(object):
  82         """ Represents a start location for a path.
  83         
  84         A Root is an object which may be the first element of a path tuple,
  85         and represents from where to start the path.
  86         
  87         On posix, there's only one: ROOT (singleton).
  88         On nt, there are a few:
  89           CURROOT - the root of the current drive (singleton)
  90           Drive(letter) - the root of a specific drive
  91           UnrootedDrive(letter) - the current working directory on a specific
  92                                   drive
  93           UNCRoot(host, mountpoint) - a UNC mount point
  94 
  95         The class for each OS has its own root classes, which should inherit
  96         from _OSBaseRoot.
  97 
  98         str(root) should return the string name of the root. The string should
  99         identify the root: two root elements with the same string should have
 100         the same meaning. To allow meaningful sorting of path objects, root
 101         objects can be compared to strings and other root objects. They are
 102         smaller than all strings, and are compared with other root objects
 103         according to their string name.
 104 
 105         Every Root object should contain the "isabs" attribute, which is True
 106         if changes in the current working directory won't change the meaning
 107         of the root and False otherwise. (CURROOT and UnrootedDrive aren't
 108         absolute)
 109         If isabs is True, it should also implement the abspath() method, which
 110         should return an absolute path object, equivalent to the root when the
 111         call was made.
 112         """
 113         isabs = None
 114 
 115         def abspath(self):
 116             if self.abspath:
 117                 raise NotImplementedError, 'This root is already absolute'
 118             else:
 119                 raise NotImplementedError, 'abspath is abstract'
 120 
 121         def __str__(self):
 122             raise NotImplementedError, '__str__ is abstract'
 123 
 124         def __cmp__(self, other):
 125             if isinstance(other, str):
 126                 return -1
 127             elif isinstance(other, BasePath._BaseRoot):
 128                 return cmp(str(self), str(other))
 129             else:
 130                 raise TypeError, 'Comparison not defined'
 131 
 132         def __hash__(self):
 133             # This allows path objects to be hashable
 134             return hash(str(self))
 135 
 136     # _OSBaseRoot should be the base of the OS-specific root classes, which
 137     # should inherit from _BaseRoot
 138     _OSBaseRoot = None
 139 
 140     # These string constants should be filled by subclasses - they are real
 141     # directory names
 142     curdir = None
 143     pardir = None
 144 
 145     # These string constants are used by default implementations of methods,
 146     # but are not part of the interface - the whole idea is for the interface
 147     # to hide those details.
 148     _sep = None
 149     _altsep = None
 150 
 151     @staticmethod
 152     def _parse_str(pathstr):
 153         # Concrete path classes should implement _parse_str to get a path
 154         # string and return an iterable over path elements.
 155         raise NotImplementedError, '_parse_str is abstract'
 156 
 157     @staticmethod
 158     def normcasestr(string):
 159         """ Normalize the case of one path element.
 160         
 161         This default implementation returns string unchanged. On
 162         case-insensitive platforms, it returns the normalized string.
 163         """
 164         return string
 165 
 166     # We make this method a property, to show that it doesn't use any
 167     # system calls.
 168     # Case-sensitive subclasses can redefine it to return self.
 169     @property
 170     def normcase(self):
 171         """ Return an equivalent path with case-normalized elements. """
 172         if self.isrel:
 173             return self.__class__(self.normcasestr(element)
 174                                   for element in self)
 175         else:
 176             def gen():
 177                 it = iter(self)
 178                 yield it.next()
 179                 for element in it:
 180                     yield self.normcasestr(element)
 181             return self.__class__(gen())
 182 
 183     @classmethod
 184     def _normalize_elements(cls, elements):
 185         # This method gets an iterable over path elements.
 186         # It should return an iterator over normalized path elements -
 187         # that is, curdir elements should be ignored.
 188         
 189         for i, element in enumerate(elements):
 190             if isinstance(element, str):
 191                 if element != cls.curdir:
 192                     if (not element or
 193                         cls._sep in element or
 194                         (cls._altsep and cls._altsep in element)):
 195                         # Those elements will cause path(str(x)) != x
 196                         raise ValueError, "Element %r is invalid" % element
 197                     yield element
 198             elif i == 0 and isinstance(element, cls._OSBaseRoot):
 199                 yield element
 200             else:
 201                 raise TypeError, "Element %r is of a wrong type" % element
 202 
 203     def __new__(cls, arg=None):
 204         """ Create a new path object.
 205         
 206         If arg isn't given, an empty path, which represents the current
 207         working directory, is returned.
 208         If arg is a string, it is parsed into a logical path.
 209         If arg is an iterable over path elements, a new path is created from
 210         them.
 211         """
 212         if arg is None:
 213             return tuple.__new__(cls)
 214         elif type(arg) is cls:
 215             return arg
 216         elif isinstance(arg, str):
 217             return tuple.__new__(cls, cls._parse_str(arg))
 218         else:
 219             return tuple.__new__(cls, cls._normalize_elements(arg))
 220 
 221     def __init__(self, arg=None):
 222         # Since paths are immutable, we can cache the string representation
 223         self._cached_str = None
 224 
 225     def _build_str(self):
 226         # Return a string representation of self.
 227         # 
 228         # This is a default implementation, which may be overriden by
 229         # subclasses (form example, MacPath)
 230         if not self:
 231             return self.curdir
 232         elif isinstance(self[0], self._OSBaseRoot):
 233             return str(self[0]) + self._sep.join(self[1:])
 234         else:
 235             return self._sep.join(self)
 236 
 237     def __str__(self):
 238         """ Return a string representation of self. """
 239         if self._cached_str is None:
 240             self._cached_str = self._build_str()
 241         return self._cached_str
 242 
 243     def __repr__(self):
 244         # We want path, not the real class name.
 245         return 'path(%r)' % str(self)
 246 
 247     @property
 248     def isabs(self):
 249         """ Return whether this path represent an absolute path.
 250 
 251         An absolute path is a path whose meaning doesn't change when the
 252         the current working directory changes.
 253         
 254         (Note that this is not the same as "not self.isrelative")
 255         """
 256         return len(self) > 0 and \
 257                isinstance(self[0], self._OSBaseRoot) and \
 258                self[0].isabs
 259 
 260     @property
 261     def isrel(self):
 262         """ Return whether this path represents a relative path.
 263 
 264         A relative path is a path without a root element, so it can be
 265         concatenated to other paths.
 266 
 267         (Note that this is not the same as "not self.isabs")
 268         """
 269         return len(self) == 0 or \
 270                not isinstance(self[0], self._OSBaseRoot)
 271 
 272     # Wrap a few tuple methods to return path objects
 273 
 274     def __add__(self, other):
 275         other = self.__class__(other)
 276         if not other.isrel:
 277             raise ValueError, "Right operand should be a relative path"
 278         return self.__class__(itertools.chain(self, other))
 279 
 280     def __radd__(self, other):
 281         if not self.isrel:
 282             raise ValueError, "Right operand should be a relative path"
 283         other = self.__class__(other)
 284         return self.__class__(itertools.chain(other, self))
 285 
 286     def __getslice__(self, *args):
 287         return self.__class__(tuple.__getslice__(self, *args))
 288 
 289     def __mul__(self, *args):
 290         if not self.isrel:
 291             raise ValueError, "Only relative paths can be multiplied"
 292         return self.__class__(tuple.__mul__(self, *args))
 293 
 294     def __rmul__(self, *args):
 295         if not self.isrel:
 296             raise ValueError, "Only relative paths can be multiplied"
 297         return self.__class__(tuple.__rmul__(self, *args))
 298 
 299     def __eq__(self, other):
 300         return tuple.__eq__(self, self.__class__(other))
 301     def __ge__(self, other):
 302         return tuple.__ge__(self, self.__class__(other))
 303     def __gt__(self, other):
 304         return tuple.__gt__(self, self.__class__(other))
 305     def __le__(self, other):
 306         return tuple.__le__(self, self.__class__(other))
 307     def __lt__(self, other):
 308         return tuple.__lt__(self, self.__class__(other))
 309     def __ne__(self, other):
 310         return tuple.__ne__(self, self.__class__(other))
 311         
 312 
 313     # ----------------------------------------------------------------
 314     # Now come the methods which use system calls.
 315 
 316     # --- Path transformation which use system calls
 317 
 318     @classmethod
 319     def cwd(cls):
 320         return cls(os.getcwd())
 321 
 322     def chdir(self):
 323         return os.chdir(str(self))
 324 
 325     def abspath(self):
 326         if not self:
 327             return self.cwd()
 328         if isinstance(self[0], self._OSBaseRoot):
 329             if self[0].isabs:
 330                 return self
 331             else:
 332                 return self[0].abspath() + self[1:]
 333         else:
 334             return self.cwd() + self
 335 
 336     def realpath(self):
 337         return self.__class__(os.path.realpath(str(self)))
 338 
 339     def relpathto(self, dst):
 340         """ Return a relative path from self to dest.
 341 
 342         This method examines self.realpath() and dest.realpath(). If
 343         they have the same root element, a path in the form
 344         path([path.pardir, path.pardir, ..., dir1, dir2, ...])
 345         is returned. If they have different root elements,
 346         dest.realpath() is returned.
 347         """
 348         src = self.realpath()
 349         dst = self.__class__(dst).realpath()
 350 
 351         if src[0] == dst[0]:
 352             # They have the same root
 353             
 354             # find the length of the equal prefix
 355             i = 1
 356             while i < len(src) and i < len(dst) and \
 357                   self.normcasestr(src[i]) == self.normcasestr(dst[i]):
 358                 i += 1
 359 
 360             return [self.pardir] * (len(src) - i) + dst[i:]
 361 
 362         else:
 363             # They don't have the same root
 364             return dst
 365             
 366 
 367     
 368 
 369     # --- Expand
 370 
 371     def expanduser(self):
 372         return path(os.path.expanduser(str(self)))
 373 
 374     def expandvars(self):
 375         return path(os.path.expandvars(str(self)))
 376     
 377 
 378     # --- Info about the path
 379 
 380     def stat(self):
 381         return StatWrapper(os.stat(str(self)))
 382     
 383     def exists(self):
 384         try:
 385             self.stat()
 386         except OSError:
 387             return False
 388         else:
 389             return True
 390 
 391     def isdir(self):
 392         try:
 393             return self.stat().isdir
 394         except OSError:
 395             return False
 396 
 397     def isfile(self):
 398         try:
 399             return self.stat().isfile
 400         except OSError:
 401             return False
 402         
 403     def lstat(self):
 404         return StatWrapper(os.lstat(str(self)))
 405 
 406     def lexists(self):
 407         try:
 408             self.lstat()
 409         except OSError:
 410             return False
 411         else:
 412             return True
 413 
 414     def lisdir(self):
 415         try:
 416             return self.stat().lisdir
 417         except OSError:
 418             return False
 419 
 420     def lisfile(self):
 421         try:
 422             return self.stat().lisfile
 423         except OSError:
 424             return False
 425 
 426     def islink(self):
 427         try:
 428             return self.lstat().islink
 429         except OSError:
 430             return False
 431         
 432     def ismount(self):
 433         return os.path.ismount(str(self))
 434 
 435     def access(self, mode):
 436         """ Return true if current user has access to this path.
 437 
 438         mode - One of the constants os.F_OK, os.R_OK, os.W_OK, os.X_OK
 439         """
 440         return os.access(str(self), mode)
 441 
 442     # Additional methods in subclasses:
 443     # statvfs (PosixPath)
 444     # pathconf (PosixPath, XXX MacPath)
 445     # samefile (PosixPath, XXX MacPath)
 446 
 447 
 448     # --- Modifying operations on files and directories
 449 
 450     def utime(self, times):
 451         """ Set the access and modified times of this file. """
 452         os.utime(str(self), times)
 453 
 454     def chmod(self, mode):
 455         os.chmod(str(self), mode)
 456 
 457     def rename(self, new):
 458         os.rename(str(self), str(new))
 459 
 460     # Additional methods in subclasses:
 461     # chown (PosixPath, XXX MacPath)
 462     # lchown (PosixPath, XXX MacPath)
 463 
 464 
 465     # --- Create/delete operations on directories
 466 
 467     def mkdir(self, mode=0777):
 468         os.mkdir(str(self), mode)
 469 
 470     def makedirs(self, mode=0777):
 471         os.makedirs(str(self), mode)
 472 
 473     def rmdir(self):
 474         os.rmdir(str(self))
 475 
 476     def removedirs(self, base=None):
 477         """ Remove empty directories recursively.
 478         
 479         If the directory is empty, remove it. If the parent directory becomes
 480         empty, remove it too. Continue until a directory can't be removed,
 481         because it's not empty or for other reasons.
 482         If base is given, it should be a prefix of self. base won't be removed
 483         even if it becomes empty.
 484         Note: only directories explicitly listed in the path will be removed.
 485         This means that if self is a relative path, predecesors of the
 486         current working directory won't be removed.
 487         """
 488         if not self.stat().isdir:
 489             raise OSError, 'removedirs only works on directories.'
 490         base = self.__class__(base)
 491         if base:
 492             if not self[:len(base)] == base:
 493                 raise ValueError, 'base should be a prefix of self.'
 494             stopat = len(base)
 495         else:
 496             stopat = 0
 497         for i in xrange(len(self), stopat, -1):
 498             try:
 499                 self[:i].rmdir()
 500             except OSError:
 501                 break
 502 
 503     def rmtree(self, *args):
 504         return shutil.rmtree(str(self), *args)
 505 
 506 
 507     # --- Modifying operations on files
 508 
 509     def touch(self):
 510         """ Set the access/modified times of this file to the current time.
 511         Create the file if it does not exist.
 512         """
 513         fd = os.open(str(self), os.O_WRONLY | os.O_CREAT, 0666)
 514         os.close(fd)
 515         os.utime(str(self), None)
 516 
 517     def remove(self):
 518         os.remove(str(self))
 519 
 520     def copy(self, dst, copystat=False):
 521         """ Copy file from self to dst.
 522 
 523         If copystat is False, copy data and mode bits ("cp self dst").
 524         If copystat is True, copy data and all stat info ("cp -p self dst").
 525 
 526         The destination may be a directory. If so, a file with the same base
 527         name as self will be created in that directory.
 528         """
 529         dst = self.__class__(dst)
 530         if dst.stat().isdir:
 531             dst += self[-1]
 532         shutil.copyfile(str(self), str(dst))
 533         if copystat:
 534             shutil.copystat(str(self), str(dst))
 535         else:
 536             shutil.copymode(str(self), str(dst))
 537 
 538     def move(self, dst):
 539         dst = self.__class__(dst)
 540         return shutil.move(str(self), str(dst))
 541         
 542 
 543     # --- Links
 544 
 545     # In subclasses:
 546     # link (PosixPath, XXX MacPath)
 547     # writelink (PosixPath) - what about MacPath?
 548     # readlink (PosixPath, XXX MacPath)
 549     # readlinkpath (PosixPath, XXXMacPath)
 550 
 551 
 552     # --- Extra
 553 
 554     # In subclasses:
 555     # mkfifo (PosixPath, XXX MacPath)
 556     # mknod (PosixPath, XXX MacPath)
 557     # chroot (PosixPath, XXX MacPath)
 558     #
 559     # startfile (NTPath)
 560 
 561 
 562     # --- Globbing
 563 
 564     # If the OS supports it, _id should be a function that gets a stat object
 565     # and returns a unique id of a file.
 566     # It the OS doesn't support it, it should be None.
 567     _id = None
 568 
 569     @staticmethod
 570     def _match_element(comp_element, element):
 571         # Does a filename match a compiled pattern element?
 572         # The filename should be normcased.
 573         if comp_element is None:
 574             return True
 575         elif isinstance(comp_element, str):
 576             return comp_element == element
 577         else:
 578             return comp_element.match(element)
 579 
 580     def _glob(cls, pth, comp_pattern, topdown, onlydirs, onlyfiles,
 581               positions, on_path, stat):
 582         """ The recursive function used by glob.
 583 
 584         This version treats symbolic links as files. Broken symlinks won't be
 585         listed.
 586 
 587         pth is a dir in which we search.
 588         
 589         comp_pattern is the compiled pattern. It's a sequence which should
 590         consist of three kinds of elements:
 591         * None - matches any number of subdirectories, including 0.
 592         * a string - a normalized name, when exactly one name can be matched.
 593         * a regexp - for testing if normalized names match.
 594 
 595         positions is a sequence of positions on comp_pattern that children of
 596         path may match. On the first call, if will be [0].
 597 
 598         on_path is a set of inode identifiers on path, or None if circles
 599         shouldn't be checked.
 600 
 601         stat is the appropriate stat function - cls.stat or cls.lstat.
 602         """
 603 
 604         if len(positions) == 1 and isinstance(comp_pattern[positions[0]], str):
 605             # We don't have to listdir if exactly one file name can match.
 606             # Since we always stat the files, it's ok if the file doesn't exist.
 607             listdir = [comp_pattern[positions[0]]]
 608         else:
 609             listdir = os.listdir(str(pth))
 610             listdir.sort()
 611 
 612         for subfile in listdir:
 613             newpth = pth + subfile
 614             # We don't strictly need to stat a file if we don't follow symlinks
 615             # AND positions == [len(comp_pattern)-1] AND
 616             # not isinstance(comp_pattern[-1], str), but do me a favour...
 617             try:
 618                 st = stat(newpth)
 619             except OSError:
 620                 continue
 621             newpositions = []
 622             subfilenorm = cls.normcasestr(subfile)
 623             
 624             if topdown:
 625                 # If not topdown, it happens after we handle subdirs
 626                 if positions[-1] == len(comp_pattern) - 1:
 627                     if cls._match_element(comp_pattern[-1], subfilenorm):
 628                         if not ((onlydirs and not st.isdir) or
 629                                 (onlyfiles and not st.isfile)):
 630                             yield newpth
 631 
 632             for pos in reversed(positions):
 633                 if st.isdir:
 634                     comp_element = comp_pattern[pos]
 635                     if pos + 1 < len(comp_pattern):
 636                         if cls._match_element(comp_element, subfilenorm):
 637                             newpositions.append(pos + 1)
 638                             if comp_pattern[pos + 1] is None:
 639                                 # We should stop at '..'
 640                                 break
 641                     if comp_element is None:
 642                         newpositions.append(pos)
 643                         # We don't have to break - there are not supposed
 644                         # to be any positions before '..'.
 645 
 646             if newpositions:
 647                 newpositions.reverse()
 648 
 649                 if on_path is not None:
 650                     newpath_id = cls._id(st)
 651                     if newpath_id in on_path:
 652                         raise OSError, "Circular path encountered"
 653                     on_path.add(newpath_id)
 654 
 655                 for x in cls._glob(newpth,
 656                                    comp_pattern, topdown, onlydirs, onlyfiles,
 657                                    newpositions, on_path, stat):
 658                     yield x
 659 
 660                 if on_path is not None:
 661                     on_path.remove(newpath_id)
 662 
 663             if not topdown:
 664                 # If topdown, it happens after we handle subdirs
 665                 if positions[-1] == len(comp_pattern) - 1:
 666                     if cls._match_element(comp_pattern[-1], subfilenorm):
 667                         if not ((onlydirs and not st.isdir) or
 668                                 (onlyfiles and not st.isfile)):
 669                             yield newpth
 670 
 671     _magic_check = re.compile('[*?[]')
 672 
 673     @classmethod
 674     def _has_magic(cls, s):
 675         return cls._magic_check.search(s) is not None
 676 
 677     _cache = {}
 678 
 679     @classmethod
 680     def _compile_pattern(cls, pattern):
 681         # Get a pattern, return the list of compiled pattern elements
 682         # and the list of initial positions.
 683         pattern = cls(pattern)
 684         if not pattern.isrel:
 685             raise ValueError, "pattern should be a relative path."
 686 
 687         comp_pattern = []
 688         last_was_none = False
 689         for element in pattern:
 690             element = cls.normcasestr(element)
 691             if element == '**':
 692                 if not last_was_none:
 693                     comp_pattern.append(None)
 694             else:
 695                 last_was_none = False
 696                 if not cls._has_magic(element):
 697                     comp_pattern.append(element)
 698                 else:
 699                     try:
 700                         r = cls._cache[element]
 701                     except KeyError:
 702                         r = re.compile(fnmatch.translate(element))
 703                         cls._cache[element] = r
 704                     comp_pattern.append(r)
 705 
 706         if comp_pattern[0] is None and len(comp_pattern) > 1:
 707             positions = [0, 1]
 708         else:
 709             positions = [0]
 710 
 711         return comp_pattern, positions
 712 
 713     def match(self, pattern):
 714         """ Return whether self matches the given pattern.
 715 
 716         pattern has the same meaning as in the glob method.
 717         self should be relative.
 718 
 719         This method doesn't use any system calls.
 720         """
 721         if not self.isrel:
 722             raise ValueError, "self must be a relative path"
 723         comp_pattern, positions = self._compile_pattern(pattern)
 724 
 725         for element in self.normcase:
 726             newpositions = []
 727             for pos in reversed(positions):
 728                 if pos == len(comp_pattern):
 729                     # We matched the pattern but the path isn't finished -
 730                     # too bad
 731                     continue
 732                 comp_element = comp_pattern[pos]
 733                 if self._match_element(comp_element, element):
 734                     newpositions.append(pos + 1)
 735                 if comp_element is None:
 736                     newpositions.append(pos)
 737                     # No need to continue after a '**'
 738                     break
 739             newpositions.reverse()
 740             positions = newpositions
 741             if not positions:
 742                 # No point in carrying on
 743                 break
 744 
 745         return (len(comp_pattern) in positions)
 746 
 747     def glob(self, pattern='*', topdown=True, onlydirs=False, onlyfiles=False):
 748         """ Return an iterator over all files in self matching pattern.
 749 
 750         pattern should be a relative path, which may include wildcards.
 751         In addition to the regular shell wildcards, you can use '**', which
 752         matches any number of directories, including 0.
 753 
 754         If topdown is True (the default), a directory is yielded before its
 755         descendents. If it's False, a directory is yielded after its
 756         descendents.
 757 
 758         If onlydirs is True, only directories will be yielded. If onlyfiles
 759         is True, only regular files will be yielded.
 760 
 761         This method treats symbolic links as regular files. Broken symlinks
 762         won't be yielded.
 763         """
 764 
 765         if onlydirs and onlyfiles:
 766             raise ValueError, \
 767                   "Only one of onlydirs and onlyfiles can be specified."
 768 
 769         comp_pattern, positions = self._compile_pattern(pattern)
 770 
 771         if self._id is not None and None in comp_pattern:
 772             on_path = set([self._id(self.stat())])
 773         else:
 774             on_path = None
 775             
 776         for x in self._glob(self, comp_pattern, topdown, onlydirs, onlyfiles,
 777                             positions, on_path, self.__class__.stat):
 778             yield x
 779         
 780     def lglob(self, pattern='*', topdown=True, onlydirs=False, onlyfiles=False):
 781         """ Return an iterator over all files in self matching pattern.
 782 
 783         pattern should be a relative path, which may include wildcards.
 784         In addition to the regular shell wildcards, you can use '**', which
 785         matches any number of directories, including 0.
 786 
 787         If topdown is True (the default), a directory is yielded before its
 788         descendents. If it's False, a directory is yielded after its
 789         descendents.
 790 
 791         If onlydirs is True, only directories will be yielded. If onlyfiles
 792         is True, only regular files will be yielded.
 793 
 794         This method treats symbolic links as special files - they won't be
 795         followed, and they will be yielded even if they're broken.
 796         """
 797 
 798         if onlydirs and onlyfiles:
 799             raise ValueError, \
 800                   "Only one of onlydirs and onlyfiles can be specified."
 801 
 802         comp_pattern, positions = self._compile_pattern(pattern)
 803             
 804         for x in self._glob(self, comp_pattern, topdown, onlydirs, onlyfiles,
 805                             positions, None, self.__class__.lstat):
 806             yield x
 807 
 808 
 809 class PosixPath(BasePath):
 810     """ Represents POSIX paths. """
 811     
 812     class _PosixRoot(BasePath._BaseRoot):
 813         """ Represents the filesystem root (/).
 814         
 815         There's only one root on posix systems, so this is a singleton.
 816         """
 817         instance = None
 818         def __new__(cls):
 819             if cls.instance is None:
 820                 instance = object.__new__(cls)
 821                 cls.instance = instance
 822             return cls.instance
 823         
 824         def __str__(self):
 825             return '/'
 826 
 827         def __repr__(self):
 828             return 'path.ROOT'
 829 
 830         isabs = True
 831 
 832     _OSBaseRoot = _PosixRoot
 833 
 834     ROOT = _PosixRoot()
 835 
 836     # Public constants
 837     curdir = '.'
 838     pardir = '..'
 839 
 840     # Private constants
 841     _sep = '/'
 842     _altsep = None
 843 
 844     @classmethod
 845     def _parse_str(cls, pathstr):
 846         # get a path string and return an iterable over path elements.
 847         if pathstr.startswith('/'):
 848             if pathstr.startswith('//') and not pathstr.startswith('///'):
 849                 # Two initial slashes have application-specific meaning
 850                 # in POSIX, and it's not supported currently.
 851                 raise NotImplementedError, \
 852                       "Paths with two leading slashes aren't supported."
 853             yield cls.ROOT
 854         for element in pathstr.split('/'):
 855             if element == '' or element == cls.curdir:
 856                 continue
 857             # '..' aren't specially treated, since popping the last
 858             # element isn't correct if the last element was a symbolic
 859             # link.
 860             yield element
 861 
 862 
 863     # POSIX-specific methods
 864     
 865 
 866     # --- Info about the path
 867 
 868     def statvfs(self):
 869         """ Perform a statvfs() system call on this path. """
 870         return os.statvfs(str(self))
 871 
 872     def pathconf(self, name):
 873         return os.pathconf(str(self), name)
 874 
 875     def samefile(self, other):
 876         other = self.__class__(other)
 877         s1 = self.stat()
 878         s2 = other.stat()
 879         return s1.st_ino == s2.st_ino and \
 880                s1.st_dev == s2.st_dev
 881 
 882 
 883     # --- Modifying operations on files and directories
 884 
 885     def chown(self, uid=None, gid=None):
 886         if uid is None:
 887             uid = -1
 888         if gid is None:
 889             gid = -1
 890         return os.chown(str(self), uid, gid)
 891     
 892     def lchown(self, uid=None, gid=None):
 893         if uid is None:
 894             uid = -1
 895         if gid is None:
 896             gid = -1
 897         return os.lchown(str(self), uid, gid)
 898 
 899 
 900     # --- Links
 901 
 902     def link(self, newpath):
 903         """ Create a hard link at 'newpath', pointing to this file. """
 904         os.link(str(self), str(newpath))
 905 
 906     def writelink(self, src):
 907         """ Create a symbolic link at self, pointing to src.
 908 
 909         src may be any string. Note that if it's a relative path, it
 910         will be interpreted relative to self, not relative to the current
 911         working directory.
 912         """
 913         os.symlink(str(src), str(self))
 914 
 915     def readlink(self):
 916         """ Return the path to which this symbolic link points.
 917 
 918         The result is a string, which may be an absolute path, a
 919         relative path (which should be interpreted relative to self[:-1]),
 920         or any arbitrary string.
 921         """
 922         return os.readlink(str(self))
 923 
 924     def readlinkpath(self):
 925         """ Return the path to which this symbolic link points. """
 926         linkpath = self.__class__(self.readlink())
 927         if linkpath.isrel:
 928             return self + linkpath
 929         else:
 930             return linkpath
 931 
 932 
 933     # --- Extra
 934 
 935     def mkfifo(self, *args):
 936         return os.mkfifo(str(self), *args)
 937 
 938     def mknod(self, *args):
 939         return os.mknod(str(self), *args)
 940 
 941     def chroot(self):
 942         return os.chroot(str(self))
 943 
 944 
 945     # --- Globbing
 946 
 947     @staticmethod
 948     def _id(stat):
 949         return (stat.st_ino, stat.st_dev)
 950 
 951 
 952 class NTPath(BasePath):
 953     """ Represents paths on Windows operating systems. """
 954 
 955     class _NTBaseRoot(BasePath._BaseRoot):
 956         """ The base class of all Windows root classes. """
 957         pass
 958 
 959     _OSBaseRoot = _NTBaseRoot
 960 
 961     class _CurRootType(_NTBaseRoot):
 962         """ Represents the root of the current working drive.
 963         
 964         This class is a singleton. It represents the root of the current
 965         working drive - paths starting with '\'.
 966         """
 967         instance = None
 968         def __new__(cls):
 969             if cls.instance is None:
 970                 instance = object.__new__(cls)
 971                 cls.instance = instance
 972             return cls.instance
 973         
 974         def __str__(self):
 975             return '\\'
 976 
 977         def __repr__(self):
 978             return 'path.CURROOT'
 979 
 980         isabs = False
 981 
 982         def abspath(self):
 983             from nt import _getfullpathname
 984             return NTPath(_getfullpathname(str(self)))
 985 
 986     CURROOT = _CurRootType()
 987 
 988     class Drive(_NTBaseRoot):
 989         """ Represents the root of a specific drive. """
 990         def __init__(self, letter):
 991             # Drive letter is normalized - we don't lose any information
 992             if len(letter) != 1 or letter not in string.letters:
 993                 raise ValueError, 'Should get one letter'
 994             self._letter = letter.lower()
 995 
 996         @property
 997         def letter(self):
 998             # We use a property because we want the object to be immutable.
 999             return self._letter
1000 
1001         def __str__(self):
1002             return '%s:\\' % self.letter
1003 
1004         def __repr__(self):
1005             return 'path.Drive(%r)' % self.letter
1006 
1007         isabs = True
1008 
1009     class UnrootedDrive(_NTBaseRoot):
1010         """ Represents the current working directory on a specific drive. """
1011         def __init__(self, letter):
1012             # Drive letter is normalized - we don't lose any information
1013             if len(letter) != 1 or letter not in string.letters:
1014                 raise ValueError, 'Should get one letter'
1015             self._letter = letter.lower()
1016 
1017         @property
1018         def letter(self):
1019             # We use a property because we want the object to be immutable.
1020             return self._letter
1021 
1022         def __str__(self):
1023             return '%s:' % self.letter
1024 
1025         def __repr__(self):
1026             return 'path.UnrootedDrive(%r)' % self.letter
1027 
1028         isabs = False
1029 
1030         def abspath(self):
1031             from nt import _getfullpathname
1032             return NTPath(_getfullpathname(str(self)))
1033 
1034     class UNCRoot(_NTBaseRoot):
1035         """ Represents a UNC mount point. """
1036         def __init__(self, host, mountpoint):
1037             # Host and mountpoint are normalized - we don't lose any information
1038             self._host = host.lower()
1039             self._mountpoint = mountpoint.lower()
1040 
1041         @property
1042         def host(self):
1043             # We use a property because we want the object to be immutable.
1044             return self._host
1045 
1046         @property
1047         def mountpoint(self):
1048             # We use a property because we want the object to be immutable.
1049             return self._mountpoint
1050 
1051         def __str__(self):
1052             return '\\\\%s\\%s\\' % (self.host, self.mountpoint)
1053 
1054         def __repr__(self):
1055             return 'path.UNCRoot(%r, %r)' % (self.host, self.mountpoint)
1056 
1057         isabs = True
1058             
1059             
1060     # Public constants
1061     curdir = '.'
1062     pardir = '..'
1063 
1064     # Private constants
1065     _sep = '\\'
1066     _altsep = '/'
1067 
1068     @staticmethod
1069     def normcasestr(string):
1070         """ Normalize the case of one path element.
1071         
1072         On Windows, this returns string.lower()
1073         """
1074         return string.lower()
1075 
1076     @classmethod
1077     def _parse_str(cls, pathstr):
1078         # get a path string and return an iterable over path elements.
1079 
1080         # First, replace all backslashes with slashes.
1081         # I know that it should have been the other way round, but I can't
1082         # stand all those escapes.
1083         
1084         pathstr = pathstr.replace('\\', '/')
1085 
1086         # Handle the root element
1087         
1088         if pathstr.startswith('/'):
1089             if pathstr.startswith('//'):
1090                 # UNC Path
1091                 if pathstr.startswith('///'):
1092                     raise ValueError, \
1093                           "Paths can't start with more than two slashes"
1094                 index = pathstr.find('/', 2)
1095                 if index == -1:
1096                     raise ValueError, \
1097                           "UNC host name should end with a slash"
1098                 index2 = index+1
1099                 while pathstr[index2:index2+1] == '/':
1100                     index2 += 1
1101                 if index2 == len(pathstr):
1102                     raise ValueError, \
1103                           "UNC mount point is empty"
1104                 index3 = pathstr.find('/', index2)
1105                 if index3 == -1:
1106                     index3 = len(pathstr)
1107                 yield cls.UNCRoot(pathstr[2:index], pathstr[index2:index3])
1108                 pathstr = pathstr[index3:]
1109             else:
1110                 # CURROOT
1111                 yield cls.CURROOT
1112         else:
1113             if pathstr[1:2] == ':':
1114                 if pathstr[2:3] == '/':
1115                     # Rooted drive
1116                     yield cls.Drive(pathstr[0])
1117                     pathstr = pathstr[3:]
1118                 else:
1119                     # Unrooted drive
1120                     yield cls.UnrootedDrive(pathstr[0])
1121                     pathstr = pathstr[2:]
1122 
1123         # Handle all other elements
1124         
1125         for element in pathstr.split('/'):
1126             if element == '' or element == cls.curdir:
1127                 continue
1128             # We don't treat pardir specially, since in the presence of
1129             # links there's nothing to do about them.
1130             # Windows doesn't have links, but why not keep path handling
1131             # similiar?
1132             yield element
1133 
1134 
1135     # NT-specific methods
1136 
1137     # --- Extra
1138 
1139     def startfile(self):
1140         return os.startfile(str(self))
1141 
1142 if os.name == 'posix':
1143     path = PosixPath
1144 elif os.name == 'nt':
1145     path = NTPath
1146 else:
1147     raise NotImplementedError, \
1148           "The path object is currently not implemented for OS %r" % os.name
```
:::
::::
