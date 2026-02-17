# AlternativePathDiscussion

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

This page describes parts of the Path class design which are in discussion. It is meant to show the current state of the discussion, so when we reach a consensus, we can delete all the discussion details and just write the decision. Please write your opinions below in the appropriate section, or start a new section. Also indicate what you agree with, so we know how close to consensus we are.

This discussion will be used to write a PEP (an alternative to PEP 355) and reference implementation.

# Work coordination 

Mike (2006/08/20): I\'ll be working on a reference implementation and a PEP soon. Anybody else feel inclined? We should get working now if we want this in Python 2.6.

# Constructor 

**agreed:** {{{Path(\"/a/b\") =\> a Path object for \"/a/b\". Path() =\> same as Path(os.curdir). Path.cwd() =\> same as Path(os.getcwd()). Path(\[\"a\", \"b\"\]) =\> same as Path(\'a/b\') - since a path is a sequence of items, it should be initializable from an iterable of items.}}}

# Representation 

**agreed:** A logical representation is better than a string representation. `p[:]` should behave like a tuple of path components (directories and the final filename). `p[n1:n2` should return a new Path containing only the sliced components. `p1 + p2` should join paths. This eliminates the need for several properties/methods: .parent, .name, .join(), .split(), etc. `str(p)` should return a platform-specific string representing the entire path.

# Joining absolute paths 

Mike: ` p1 + p2 ` should return p2 if it isn\'t relative.

Noam: ` p1 + p2 ` should raise an exception if p2 isn\'t relative. Rationale:

- Explicit is better than implicit.

- It makes len(p1 + p2) == len(p1) + len(p2), which is nice.

- It\'s pretty easy to write ` p1 + p2 if p2.isrel else p2 `

Mike: My proposal matches existing os.path.join() behavior. We shouldn\'t contradict it without a good reason. The most common use case is `Path.cwd() + Path(sys.argv[1])`. However, I\'m not personally opposed to Noam\'s proposal if there\'s consensus for it. Why does the length of the combined path matter?

Noam: About the length: I feel it\'s nice that addition preserves this property, that\'s all. About cwd() + something: the abspath method does that.

# Path + string 

What should `Path("/a/b") + "c"` do? Alternatives:

1.  Join paths. Same as `Path("/a/b/c")`.

2.  Append to the filename (useful for extensions). Same as `Path("/a/bc")`.

3.  Raise an exception because `tuple + string` and `list + string` are illegal in Python.

Noam: I know that tuple + string are illegal, but I think that since there\'s an obvious way to treat the string as a path, it\'s ok.

Mike: Maybe. But Guido rejected `/` for joining; he may also reject `+`. Its obviousness is debatable. If we do use `+` for joining, we\'ll need APIs to modify the filename and extension without having to split/rejoin. *Note: discussion of a filename/extension API is in the Filename/Extensions section below.*

Noam: Another point against automatic conversion: it doesn\'t preserve the property that (a + b) + c == a + (b + c). But it is convinient\...

## One sequence or several parts? 

**agreed:** The filename or leaf directory should be the final component of the sequence, with extensions treated as part of the filename.

Should the root and drive be encoded as the first component of the sequence, or as attributes? On POSIX there is one root: \"/\". On Windows, each drive has its own root and current directory: r\"C:\\\", r\"D:\\\". There is an implied default drive, subject to .chdir. r\"C:foo\" is relative to drive C:\'s current directory. Should we encode all this info in the first Path component, or as .isabs/.isabsolute and .root attributes? What about Windows UNC paths (r\"\\\\a\\b\\c\")?

Noam: Keep it all in the sequence. Sequence slicing is simple and intuitive. Attributes storing data not found in the sequence is complicating matters. The root element stores all the data of \"where to start from\". UNCRoot stores host and share name.

Mike: Encoding absolute/relative and drive in the sequence may be too obscure and magical.

Noam: I don\'t think so - it\'s just an attribute of the root element, \"isabs\".

Mike: Note that slicing off the front of an absolute path makes a relative path. `Path("/a/b/c")[:1] => Path("b/c")`

Noam: which is great.

## A seperate class for files and directories? 

**agreed:** The same class will represent a file, directory, or symbolic link. (Reasons can be found in the wiki history)

## Inheritance from str to allow easy use in other functions 

Noam, Mike: This won\'t work. Strings must slice by character, and this is incompatible with slicing by directory component.

## Inheritance from tuple 

Noam: I think it works well. Guido said that he didn\'t like it, but I don\'t understand why. If all the data is stored in the sequence, I think a sequence interface should be provided. As far as I can see, the tuple interface is just that: an interface for an immutable sequence. This means that it doesn\'t cause any unwanted restrictions, so I don\'t see why not to inherit from it.

Jason: I suggest making it look like a sequence without actually subclassing tuple. It is rather strange to be subclassing tuple this way.

Noam: I guess this may be left to Guido\'s decision. I feel that subclassing from tuple is fine, but I don\'t really care.

Mike: the top level can emulate tuple slicing/addition to return a new Path object. It doesn\'t have to \*subclass\* tuple.

Noam: Can you please elaborate about why not to subclass from tuple?

Mike: Containment is better than inheritance. Never subclass if you can reasonably put the value in an attribute; it leads to all sorts of potential conflicts and bugs. Subclass only if the object really *is* a type of the superclass, and/or if the user will be calling a lot of the superclass\'s methods directly.

Noam: You can always use containment - you never really need to subclass. I think that if it\'s agreed that all the data is stored in the sequence, inheritence from tuple is ok, since we really behave like an immutable sequence, and add some operations about the sequence.

## Immutability 

Noam, Jason, Mike: I think that immutable paths are somewhat easier to implement, and allow usage as dictionary keys. I think that if we have managed to live so far without mutable strings, we will manage to live without mutable paths. I don\'t see this as a major issue, but immutable paths can be somewhat more efficient: you can hash the string representation, and you can make sure you have a path by writing things like ` dst=path(dst) `, and if dst is already a path, no new object will be created.

# In which module(s)? 

Mike: A new \'basepath\' module would contain the common base class. The platform modules (posixpath, ntpath, etc) already exist and are the logical place for these Path classes.

Noam: I think that all path OS subclasses fit nicely into one module. Most of the logic is in the base class, anyway, and it makes it easier to see what are the differences between each platform.

Mike: Putting code for disparate architectures in one module is asking for trouble. What if one architecture needs to import modules which aren\'t needed or can\'t be built on other architectures, especially C modules? Plus the module would become very large due to the need to accommodate Windows\'s intricaies (e.g., r\"C:foo\", r\"\\\\uncpath\").

Noam: Ok. It\'s basically an implementation detail, so we can decide on it after we implement the full class.

# Filenames 

Mike: If we use `+` for path joining, we need a way to create a derived path from a modified filename. Example: \"I want to add a prefix or suffix to the filename portion of \"/a/b/filename\". Splitting/rejoining the path is messy, especially if you have to modify the base name but preserve the extensions. No specific API proposal yet.

# Extensions 

**agreed:** extensions are critical, so the class must make it easy to query/modify them without splitting/rejoining the Path. Like directories, extensions have a platform-specific separator. Unlike directories, extensions are conventions rather than OS-enforced rules: not every apparent extension should be treated as such. The user must tell us when to recognize extensions, defined as N number of filename suffixes beginning with the platform\'s extension separator (.extsep). For instance, most users consider \"filename.2005-05-13.tar.gz\" and \"filename.2006.05.13.tar.gz\" as having two extensions each (\".tar.gz\"), even though the number of apparent extensions is larger.

We can put attributes/methods on the Path object, or on a special str/unicode subclass used for the filename (or for each directory component).

Noam: How should we distinguish between a file with an empty extension (\"a.\") and a file without an extension (\"a\")?

Mike: The legacy os.path.splitext() returns \".ext\", so it presumably returns \".\" for an empty extension. We could stick with this. That prevents the ability of treating extensions platform-independently though. I doubt \"a.\" is important enough to support though, have you ever seen it?

Mike: subclassing str is impractical due to the string/unicode duality. Why not path properties: p.ext, p.name (name without extension). The full filename is p\[-1\] so it doesn\'t need a property.

Noam: Why does the string/unicode duability makes subclassing str impractical? On Windows we can have unicode subclasses, and on POSIX we can have str subclasses. Having extension-related methods added to elements is nice because:

- Extension is an attribute of a path element, not of the sequence of path elements. (dirs can have extensions just as well)
- It reduces the number of methods of the path type and makes it easier to distinguish between different kinds of methods.

What should be the interface? Mike said that adding and removing extensions is important. How should it be done?

Mike: There must be a convenient way to add/delete extensions. How about `p.add_ext(*exts_without_separator)` and `p.del_ext(n=1)`, each returning new Paths. The only other operations then are querying N extensions or splitting the filename into name + N extensions. (Note: if the extsep is attached, an empty string in the result would mean \"there are not that many extensions\".)

Noam:

Ok. Here\'s a suggestion. It\'s simple, and I think that it gives you all that you need.

Path elements will be subclasses of str/unicode, with two additional properties:

element.ext will return the string from the last dot, including the dot. If there\'s no dot, it will return the empty string.

element.withoutext will return the string up to the last dot, not including the dot. It there\'s no dot, it will return the complete string.

element.ext will return str/unicode. element.withoutext will return an instance of the same subclass as element, so that you\'ll be able to write element.withoutext.withoutext to strip off two extensions.

So, to add extension to a path, you\'ll write ` p[:-1] + (p[-1]+'.py') `. To remove extension, you\'ll write ` p[:-1] + p[-1].withoutext `. To replace an extension, you\'ll write ` p[:-1] + (p[-1].withoutext + '.py') `.

I\'ve checked, and even in macpath.py, extsep is \'.\'. So I don\'t see a real problem of platform incompatibility with that scheme.

Another possible name can be \"stripext\" instead of \"withoutext\". It\'s shorter, but perhaps less descriptive.

Mike: OK on .ext and .withoutext. Concerned about using subclasses, but maybe it\'ll be OK.

Noam: Excellent!

# Stat 

**agreed:** p.stat() and p.lstat() should return an enhanced version of Python\'s os.stat() object, with attributes like `p.stat().mtime` for all information traditionally provided by stat. Include Noam\'s additional properties from [http://wiki.python.org/moin/AlternativePathModule](http://wiki.python.org/moin/AlternativePathModule). Do not have Path methods duplicating stat attributes.

Mike: Unlike os.stat(), do not support ugly attributes like .st_mtime or tuple indexing.

Noam: I think that it would be best if os.stat(pathstr) would return the same type of object as pathobj.stat() - in other words, add the easy attributes to os.stat() too. In that case, I guess that the ugly \"st\_\" names will have to stay until Python 3.

Mike: No, this is supposed to be an improvement and an API we\'ll want permanently. Nobody using legacy stat objects will get caught up because they\'ll never call Path.stat().

Noam: I don\'t really mind - we can take this to python-dev / guido decision.

Mike: I formerly proposed moving all stat attributes into Path methods, because the distinction between \"stat attribute\" and \"other file info\" was arbitrarily defined by Unix tradition, but withdrew this because it\'s not critical. Having .stat() does let the user cache the result, and having .lstat() avoids the need for a parallel set of methods that don\'t follow symlinks.

# Finding files 

Jason Orendorff\'s path module has three methods returning a non-recursive list of paths: listdir, files, dirs; and three methods returning a recursive iteration of paths: walk, walkfiles, walkdirs. Noam proposed combining all these plus filename globbing into one method: glob, with a special pattern \"\*\*\" meaning \"any subdirectory or recursive path of subdirectories\".

Nick: Swiss army methods are even more evil than wide APIs. And I consider the term \'glob\' itself to be a Unixism - I\'ve found the technique to be far more commonly known as wildcard matching in the Windows world.

Noam: Can you give examples why this proposed method is evil? I think that the basic pattern idea is well defined. It gets three arguments. topdown is, I think, well defined and may be useful. onlyfiles and onlydirs are well defined and are only a convinience. I don\'t really mind ommitting them.

About the name \"glob\": I have nothing against glob, but if you find another name for the method, I might have nothing against it either.

Jason: Hard-won knowledge here: d.files(\'\*.html\') is just right. This is the common use case. glob() overgeneralizes it, forcing me to write d.glob(\'\*.html\', filesonly=True). Yuck.

Guido strongly prefers multiple APIs for distinct use cases, as opposed to a single API that serves all the use cases by providing boolean flags that toggle various aspects of its behavior.

Noam:

I see what you mean. How about \"glob\" doing what it does in the current proposal, without the \"onlyfiles\" and \"onlydirs\" arguments, and \"files\" and \"dirs\" getting exactly the same arguments but yielding only files and directories, respectively?

About the \"l\" versions: Having glob, files, dirs, lglob, lfiles, ldirs seems ugly. Perhaps this *should* go in as a flag, say, \"follow_symlinks=True\"? (I would put it after pattern, because remembering the string \"topdown\" is easier. I don\'t think of any better name than \"follow_symlinks\". I also tend to think that it is more useful.)

Mike: Non-recursive lists: listdir, files, dirs, symlinks. Recursive iterators: walk, walkfiles, walkdirs, walklinks. All except \*links should take a \'symlinks\' argument, default True, meaning follow symlinks. If false, never return a symlink. The user can call \*links to get the symlinks separately if desired. listdir should have a \'names_only\' argument, default False, meaning return the same as os.listdir(). Doesn\'t a \'pattern\' argument eliminate the need for .glob()?

Noam: Can you explain why you think that \"listdir, files, dirs, walk, walkfiles, walkdirs\" is bettern than \"glob, files, dirs\"? I prefer three over six. About \"links\" methods - Do you have examples of when they are useful? Thinking about it, it seems that dirs+files should cover all the files in the directory, when symlinks are considered directories if they point to directories in the follow_symlinks mode. About the names_only: I don\'t like an attribute which changes the type of the result. You can always do x\[-1\] to get the base name.

Mike: Combining the recursive and non-recursive methods is acceptable. They would all have to be generators in that case. .glob() is not the best name: it sounds like something else to Unix people and incomprehensible to non-Unix people. The \*links() methods are useful when you want to treat symlinks specially; they eliminate an if-stanza in the main for loop. No reason to shove disparate things into the same loop. If symlinks=True, we do follow the links and inspect the actual directory/file, so we\'re in agreement. We can drop names_only if we add listdir(). Sometimes you just want the names, and it\'s a pain (and inefficient) to unpack temporary Path objects made from those same names.

Noam: About glob: Can you suggest a better name? I\'m happy with glob but have nothing agains a better name.

About listdir: I prefer to omit that method. From my experience, you always want to add the base name to the dir name (what would you do with it otherwise?) I can live with the slight inefficiency and small pain of making a path and taking only the last element on the rare cases in which it\'s needed. I prefer the \"one way to do it\" approach here.

About symlinks: I see what you mean. I prefer one iteration with an if stanza, since I then iterate over the contents of a directory only once, but it seems like a reasonable friend of \"dirs\" and \"files\". The name \"link\" is ok, but we should make sure that all symlinks are referred to as \"links\" in the method names - I don\'t want to remember when it\'s a link and when it\'s a symlink. If so, the \"link\" method should be renamed \"hardlink\".

But \"lfiles\", \"ldirs\" are so ugly\...

Mike: `p.listdir() => os.listdir(str(p))` is small, simple, and unobtrusive; it won\'t bother anybody except purists. Say you need the filenames for a GUI list box or a menu. It\'s hard to find a name that means \".dirs plus .files\"; maybe `.walk(recursive=False)` is OK. That will surprise existing users of walk functions, but we haven\'t found a better name. I agree we should be consistent about .(sym)links methods; maybe we should rename .link to .hardlink because it\'s so rarely used. \'follow_symlinks\' as an argument is also acceptable; it\'s wordy but perhaps better self-explanatory than \'symlinks\'. Down with the \'l\' versions!

Noam: To get all the files, you simply write ` p.glob() `, which is the same as ` p.glob('*') `.

Here\'s a suggestion. The two basic functions for finding files will be glob and lglob. They will have the same interface:

    def glob(self, pattern='*', topdown=True)
    def lglob(self, pattern='*', topdown=True)

In addition, you\'ll have two simple convinience methods:

    def files(self, pattern='*', topdown=True):
        for subpath in self.glob(pattern, topdown):
            if subpath.isfile():
                yield subpath
    def dirs(self, pattern='*', topdown=True):
        for subpath in self.glob(pattern, topdown):
            if subpath.isdir():
                yield subpath

We will ommit \"lfiles\", \"ldirs\" and \"links\" because:

- They are less useful
- They have ugly names
- They can be replaced by two lines of code.

Mike: There will be significant opposition to \"one method to rule them all\", so let\'s have a main proposal and an alternate proposal. I think mine more closely matches the expectations of the majority of Pythoneers who favor a Path object, especially those who have used Orendorff\'s/interim/PEP 355. We can code your .glob() in the reference implementation (perhaps as .glob2()), and then mention that some methods will be dropped in the final.

Noam: We can have two alternatives in the PEP.

Mike: But the #1 thing is, .glob() should not call glob.glob() unless it has to. So pattern=\'\*\' should bypass glob and call os.listdir() directly.

Noam: It does.

# isfile

Noam: It currently returns True if a file is a regular file. Perhaps it would be better if it returned whether a file is not a link or a dir? The rationale is that block device files and FIFO files can mostly be treated as regular files - you can write to and read from them, if permissions allow you. It simplifies things: paths can only be:

1.  Nonexisting
2.  Symlinks to nonexisting paths
3.  Symlinks to dirs (perhaps with a few \"jumps\")
4.  Symlinks to files (perhaps with a few \"jumps\")
5.  Dirs
6.  Files

Each of the methods exists, isdir, isfile, lexists, lisdir, lisfile, islink returns True on a different subset of these: exists - 3,4,5,6. isdir - 3,5. isfile - 4,6. lexists - 2,3,4,5,6. lisdir - 5. lisfile - 6. islink - 2,3,4.

Mike: In other words, Noam is proposing that .isfile return True for all non-directories, whereas os.path.isfile(F) returns True only for regular files (not special files). This parallels the other methods (.files()). However, it does make it harder for the user to treat special files separately. Normally if not os.path.isfile(foo) and not os.path.isdir(foo), the file is a device. Since we\'re removing functionality, let\'s add .isspecial() to bring it back \-- even better than os.path does! This returns True if any of the stat.S\_\* functions would return True.

Mike: There are no methods to check for a special file type (ischr, isblk, isfifo, issock, isdoor). Instead you have to do stat.S_ISBLK( Path(\"FOO\").stat().mode ). I\'m tempted to say we should add the methods, although they\'re rarely used.

Noam: Great! We can add them to the stat object - no need to make them methods of Path. \"isfile\" is a method of path because it\'s quite common to write \"if p.exists() and p.stat().isfile\". But we don\'t have to add those shortcuts for rarely-used tests.

Mike: Note that .isfile() and .isspecial() follow symbolic links, so they refer to the pointed-to file. They both return False if the link is dead, because these methods should never return True when .exists() would return False). But .lisfile() and .isspecial() return False and True respectively for a symbolic link, regardless of what the link points to.

Noam: About .isspecial(), I think that it ought to be left as an attribute of stat, as I wrote. About lisfile(): It should return True if p.lexists() and p.stat().isfile - it should return True only for files, not for symlinks and dirs.

# Access Permissions 

Noam: I think that the \"access\" method should be replaced by three straightforward methods, which don\'t require the use of a constant from somewhere: p.isreadable(), p.iswriteable(), p.isexecutable().

Mike: .canread(), .canwrite(), .canexecute(). The access() function is cumbersome and was probably added to conform to the Unix API.

Noam: These are indeed better names.

# Expand 

Noam: I removed expand. There\'s no need to use normpath, so it\'s equivalent to .expanduser().expandvars(), and I think that the explicit form is better.

Mike: Expand is useful though, so you don\'t forget one or the other.

Noam: I wouldn\'t want to call expandvars() by default - I think that expanding environment variables is something that should be done with care, as it may expose info about the environment which should be kept private. Anyway, I think that p.expanduser().expandvars() shows exactly what is being done and isn\'t a lot longer, so I prefer it.

# copytree

Mike: Er, not sure I\'ve used it, but it seems useful. Why force people to reinvent the wheel with their own recursive loops that they may get wrong?

Nick:

Because the handling of exceptional cases is almost always going to be application specific. Note that even os.walk provides a callback hook for if the call to os.listdir() fails when attempting to descend into a directory.

For copytree, the issues to be considered are significantly worse:

- what to do if listdir fails in the source tree?
- what to do if reading a file fails in the source tree?
- what to do if a directory doesn\'t exist in the target tree?
- what to do if a directory already exists in the target tree?
- what to do if a file already exists in the target tree?
- what to do if writing a file fails in the target tree?
- should the file contents/mode/time be copied to the target tree?
- what to do with symlinks in the source tree?

Now, what might potentially be genuinely useful is paired walk methods that allowed the following:

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

Jason: I think Python needs high-level APIs to do stuff like copytree(). The current state of affairs is just awful. On Unix I can do os.system(\'cp \' + \...), but it\'s not portable.

I haven\'t tried pairedwalkfiles(), so no opinion.

Mike: .pairedwalk() and friends may be useful. The user wants to know which files/directories to create, update, and delete. So it\'s essentially a diff report.

Noam: I\'m not sure about pairedwalk() - it may be a bit complicated, I\'m afraid. However, perhaps copytree() isn\'t such a big deal if it works only when the source is a directory and the destination doesn\'t exist. Then, exceptions aren\'t expected, so if they happen they can simply be propagated.

Mike: I\'m now thinking about a class with methods to handle each of the exceptional cases, and boolean attributes for the alternative behaviors. Then we\'d define one or more default behaviors as `copytree = CopyTree.__call__`.

# Copy 

Nick:

OK, this is one case where a swiss army method may make sense. Specifically, something like:

- def copy_to(self, dest, copymode=True, copytime=False)

\*\[Mike removed the \'copyfile\' argument, aka \'content\'. If you want to copy just the mode or time or create an empty file, without copying the file content, use other methods.\]\*

Whether or not to copy the permission settings and the last access and modification time are then all independently selectable.

The different method name also makes the direction of the copying clear (with a bare \'copy\', it\'s slightly ambiguous as the \'cp src dest\' parallel isn\'t as strong as it is with a function).

Noam: I think the different name and arguments are a good idea.

Jason: Definitely agree with Nick.

Noam: What about copyto? It\'s easier to write, I think that it\'s not hard to understand, and perhaps it focuses less attention on the \"to\", making it look like a special kind of copy.

Mike: src.copy(dest, mode=False, time=False). .copy_to is OK, .copyto is bad. Almost everybody expects .copy to mean .copy_to and not .copy_from.

Noam: About copymode vs. mode: I prefer copymode. \"mode\" seems like a mode specification (like in mkdir), not like a boolean.

# Unicode 

Noam: Someone with experience with unicode filenames, please help!

Jason: I have some experience, not a ton.

In the Win32 API, paths are Unicode strings. To produce a path-string you\'ll have to decode any non-Unicode strings in your tuple; Python\'s default encoding is one option, but the operating system\'s default encoding is another option; I think the latter is what the os functions do on Windows.

In the POSIX API, paths are char strings, which means 8-bit strings on every platform I\'m familiar with. The character set varies from system to system. Some use UTF-8.

It\'s kind of squirrely if you allow both 8-bit strings and Unicode strings in your tuple. I suggest using only Unicode within the tuple and converting to 8-bit only as needed to talk to POSIX.

Noam:

Thanks for the explanation. I agree about not mixing different kinds of strings. Is there a good way to convert unicode strings into file names on POSIX? How do you know the right encoding?

Mike: At first I thought about forcing everything to Unicode on input and adding \'encoding\' and \'onerror\' arguments to the constructor. That doesn\'t solve the problem of chosing the charset to encode on output. But now I\'m wondering if we should just preserve whatever type(s) the user inputs.

Noam: I don\'t think that preserving the type of the user input will work: You\'ll still have to decode it to str on POSIX. It seems to me that the only solution is to use the native \"alphabet\" of the system: Unicode chars on Windows, and byte chars on POSIX. To put it more clearly: All elements on Windows will be unicode, all elements on POSIX will be str.

Noam: I checked, and it seems that on Windows, file-related functions work well with byte strings. I guess it\'s because there\'s a clearly defined system encoding. So why not use only byte strings, and convert from unicode if needed by using the system encoding?

Noam: Here\'s another suggestion. I think it\'s good. It\'s based on the behaviour of functions like listdir, which return a list of unicode strings when they get a unicode argument, and a list of byte strings if they get a str argument.

Path objects will be homogeneous containers of either str or unicode items. This will be determined upon construction: if they are constructor from a unicode string, or from a sequence containing a unicode string, all elements will be unicode strings. Furthermore, all methods returning strings will return strings of that type, and all methods returning paths will return paths containing strings of that kind.

# Obsoleting other modules 

Nick:

I don\'t believe it\'s a given that a nice path object will obsolete the low level operations. When translating a shell script to Python (or vice versa), having access to the comparable low level operations would be of benefit.

At most, I would expect provision of an OO path API to result in a comment in the documentation of various modules (os.path, shutil, fnmatch, glob) saying that \"pathlib.Path\" (or whatever it ends up being called) is generally a more convenient API.

Noam: I don\'t mind obsoleting os.path, shutil, fnmatch, glob, as I see them as high-level operations. I don\'t mind not obsoleting them either - it may keep the code more organized if different operations are in differnt modules. I agree that most of the functions in the os module shouldn\'t be obsoleted - these are really low-level operating system operations, and you shouldn\'t need to use a complex path object in order to call them.

Jason: The new API should be the one high-level API for this type of stuff. All the other high-level APIs should be obsoleted.

Mike: We cannot deprecate the existing functions in Python 2.x; too many existing programs would break. But we can discourage them in the documentation.

# Additional methods/attributes 

## .purge() 

Mike: Delete \"it\" recursively if it exists, whatever it is. This is convenient when you don\'t care whether it\'s a file or directory, you just want to overwrite it, and you don\'t want to take six lines of code to do it.

Noam: Why six lines of code? I count four:

    if p.isfile():
        p.remove()
    elif p.isdir():
        p.rmtree()

We can have rmtree work also for files, and even for non-existing paths, but I\'m not sure it\'s a good idea.

Mike: .rmtree would go away if .purge is added. So we\'d have to inline its implementation. The main reason for .purge is .rmtree raises exceptions if (A) the Path is a file, or (B) the Path doesn\'t exist, and you don\'t want to clutter your code for all those cases when you just want to write or remove \"it\".

Noam: I feel fine with the four lines above, but I can live with another method. We can bring this to python-dev decision.

Mike: Adding the two capabilities to .rmtree would be functionally the same. I think .purge is a better name though.

Noam: I want to keep the number of methods and their complexity small enough. I\'m against adding capabilities to .rmtree(). I prefer not having a method which can be clearly defined in four lines and I personally have never used, but it can be taken to python-dev.

Mike: The purpose of this module (or any Python module) is to make the calling code elegant, so it describes the level of detail that matches the conceptual operation, and is not cluttered with unnecessary details (if-stanzas) simply because the module owner refused to include commonly-used convenience functions. That forces every developer to write the same stanzas again and again, or to each write their own function encapsulating it.

Noam: Ok, let\'s leave this to python-dev / Guido\'s decision.

# mkdir/rmdir 

Mike: These should succeed silently if the operation is already done. Otherwise the user has to write an unnecessary \"if p.exists():\" around it. If the user really cares whether the item exists, he can explicity write the if-stanza. If not, he shouldn\'t be forced to clutter his code, especially since that obscures whether it does matter or not that the item existed.

Noam: Simply use makedirs() and removedirs().

Mike: Those methods should go away. Their names are kludgey, and their behavior can be done with a \'parents=False\' argument.

Noam: I don\'t agree. In this case, I like to leave the basic OS calls do what they do, and keep the API of the complex methods simple (avoid the parents=False option.)

Mike: This is supposed to be an improved API. Programs are more readable if the methods reflect the operations the user really wants to do. If the user calls .mkdir it means they want to create the directory, no ifs ands or buts. The shell commands have a \--parents option so why can\'t we? If we must have .makedirs it should be called .mkdirs.

Noam: I\'m not sure about the name. makedirs/removedirs is more verbose but not too verbose, and keeps \"name compatibility\" with the os module. On the other hand, mkdirs/rmdirs looks more like mkdir/rmdir. We can leave this to python-dev/Guido decision.

Jason wrote that Guido prefers separate functions for different cases, and in this case, I prefer it too. I think that a simple API is generally better than a complex API. I think that in this case, separate functions are simpler than one function with another option.
