# PyQt/IOSlavesTutorial

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# An IOSlave Tutorial 

## Note 

This document needs to be revised. I am working on [an updated tutorial](http://www.boddie.org.uk/david/Projects/Python/KDE/Docs/kioslaves-tutorial.html) based on a kioslave in the [kioslaves package](http://www.boddie.org.uk/david/Projects/Python/KDE/).

## Introduction 

The ADFS IOSlave presents the contents of ADFS floppy disk images to the user by inspecting the ADFS filesystem stored within each image and using the KIOSlave API to return this information to client applications. Although the underlying Python module was written with a command line interface in mind, it provides an interface which can be used by an IOSlave without too much of an overhead.

This document outlines the source code and structure of the ADFS IOSlave and aims to be a useful guide to those wishing to write IOSlaves, either in Python or C++.

## Annotated code 

It is convenient to examine the source code as it is written in the *kio_adfs.py* file. However, we can at least group some of the methods in order to provide an overview of the IOSlave and separate out the details of the initialisation.

### Initialisation 

Various classes and namespaces are required in order to communicate with the KIOSlave framework. These are drawn from the `qt`{.backtick}, `kio`{.backtick} and `kdecore`{.backtick} modules:

    from qt import QByteArray
    from kio import KIO
    from kdecore import KURL

The `os`{.backtick} and `time`{.backtick} modules provide functions which are relevant to the operation of the IOSlave; the `sys`{.backtick} and `traceback`{.backtick} modules are useful for debugging the IOSlave:

    import os, sys, traceback, time

The `ADFSlib`{.backtick} module is imported. This provides the functionality required to read disk images:

    import ADFSlib

We omit the debugging code to keep this tutorial fairly brief. This can be examined in the distributed source code.

### The slave class 

We define a class which will be used to create instances of this IOSlave. The class must be derived from the `KIO.SlaveBase`{.backtick} class so that it can communicate with clients via the DCOP mechanism. Various operations are supported if the appropriate method (represented as virtual functions in C++) are reimplemented in our subclass.

Note that the name of the class is also declared in the *details.py* file so that the library which launches the Python interpreter knows which class to instantiate.

    class SlaveClass(KIO.SlaveBase):

        """SlaveClass(KIO.SlaveBase)
        
        See kdelibs/kio/kio/slavebase.h for virtual functions to override.
        """

An initialisation method, or constructor, is written which calls the base class and initialises some useful attributes, or instance variables. Note that the name of the IOSlave is passed to the base class\'s `__init__`{.backtick} method:

        def __init__(self, pool, app):
        
            # We must call the initialisation method of the base class.
            
            KIO.SlaveBase.__init__(self, "adfs", pool, app)
            
            # Initialise various instance variables.
            
            self.host = ""
            self.disc_image = None
            self.adfsdisc = None

We create a method to parse any URLs passed to the IOSlave and return a path into a disk image. This initially extracts the path from the `KURL`{.backtick} object passed as an argument and converts it to a unicode string:

        def parse_url(self, url):
        
            file_path = unicode(url.path())

The presence of a colon character is determined. If one is present then it will simply be discarded along with any preceding text; the remaining text is assumed to be a path to a local file.

            at = file_path.find(u":")
            
            if at != -1:
            
                file_path = file_path[at+1:]

Since we are implementing a read-only IOSlave, we can implement a simple caching system for operations within a single disk image. If we have cached a URL for a disk image then we check whether the URL passed refers to an item beneath it. This implies that the cached URL is a substring of the one given.

If the disk image has been cached then return the path within the image:

            if self.disc_image and file_path.find(self.disc_image) == 0:
            
                # Return the path within the image.
                return file_path[len(self.disc_image):]

An uncached URL must be examined element by element, as far as possible, comparing the path with the local filesystem. Since a valid path will contain at least one slash character then we can immediately discard any paths which do not contain one, returning `None`{.backtick} to the caller:

            elements = file_path.split(u"/")
            
            if len(elements) < 2:
            
                return None

Starting from the root directory, we apply each new path element to the constructed path, testing for the presence of the objects it refers to. If no object can be found at the path given then `None`{.backtick} is returned to the caller to indicate that the URL was invalid. If a file is found then it is assumed that an ADFS disk image has been located; a check could be performed to verify this. Finally, if all the path elements are added to the root directory, and the object referred to is itself a directory, then the URL is treated as invalid; it should have referred to a file.

            path_elements, elements = elements[:1], elements[1:]
            
            while elements != []:
            
                path_elements.append(elements.pop(0))
                
                path = u"/".join(path_elements)
                
                if os.path.isfile(path):
                
                    break
                
                elif elements == [] and os.path.isdir(path):
                
                    return None
                
                elif not os.path.exists(path):
                
                    return None

At this point, it is assumed that a suitable image has been found at the constructed path. The characters following this path correspond to the path within the image file. We record the path to the image and construct the path within the image:

            self.disc_image = path
            
            image_path = u"/".join(elements)

If not already open, it is necessary to open the image file, returning `None`{.backtick} if the file cannot be found. (Its presence was detected earlier but it is better to catch any exceptions.)

            try:
            
                adf = open(self.disc_image, "rb")
            
            except IOError:
            
                return None

We attempt to open the disk image using a class from the support module. This will read and catalogue the files within the image, storing them in an internal structure. However, if a problem is found with the image, then an exception will be raised. We tidy up and return `None`{.backtick} to signal failure in such a case, but otherwise return the path within the image:

            try:
            
                self.adfsdisc = ADFSlib.ADFSdisc(adf)
            
            except ADFSlib.ADFS_exception:
            
                adf.close()
                return None
            
            return image_path

### The get file operation 

Various fundamental operations are required if the IOSlave is going to perform a useful function. The first of these is provided by the `get`{.backtick} method which reads files in the disk image and sends their contents to the client. The first thing this method does is check the URL supplied using the previously defined `parse_url`{.backtick} method, reporting an error if the URL is unusable:

        def get(self, url):
        
            path = self.parse_url(url)
            
            if path is None:
            
                self.error(KIO.ERR_DOES_NOT_EXIST, url.path())
                return

Having established that the disk image referred to is valid, we now have a path which is supposed to refer to a file within the image. It is now necessary to attempt to find this file. This is achieved by the use of the as yet undeclared `find_file_within_image`{.backtick} method which will return `None`{.backtick} if a suitable file cannot be found:

            adfs_object = self.find_file_within_image(path)
            
            if not adfs_object:
            
                self.error(KIO.ERR_DOES_NOT_EXIST, path)
                return

Since, at this point, an object of some sort was located within the image, we need to check whether it is a directory and return an error if so.

The details of the object returned by the above method is in the form of a tuple which contains the name, the file data and some other metadata.

If the second element in the tuple is a list then the object found is a directory:

            if type(adfs_object[1]) == type([]):
            
                self.error(KIO.ERR_IS_DIRECTORY, path)
                return

For files, the second element of the tuple contains a string. In this method, we are only interested in the file data. Using the base class\'s `data`{.backtick} method, which we can access through the current instance, we send a `QByteArray`{.backtick} to the client:

            self.data(QByteArray(adfs_object[1]))

The end of the data string is indicated by an empty `QByteArray`{.backtick} before we indicate completion of the operation by calling the base class\'s `finished`{.backtick} method:

            self.data(QByteArray())
            
            self.finished()

### The stat operation 

The `stat`{.backtick} method returns information about files and directories within the disk image. It is very important that this method works properly as, otherwise, the IOSlave will not work as expected and may appear to be behaving in an unpredictable manner. For example, clients such as Konqueror often use the `stat`{.backtick} method to find out information about objects before calling `get`{.backtick}, so failure to read a file may actually be the result of a misbehaving `stat`{.backtick} operation.

As for the `get`{.backtick} method, the `stat`{.backtick} method initially verifies that the URL supplied is referring to a valid disk image, and that there is a path within the image to use. Unlike the `get`{.backtick} method, it will redirect the client to the path contained within the URL if the `parse_url`{.backtick} fails to handle it. This allows the user to use URL autocompletion on ordinary filesystems while searching for images to read.

        def stat(self, url):
        
            path = self.parse_url(url)
            
            if path is None:
            
                # Try redirecting to the protocol contained in the path.
                redir_url = KURL(url.path())
                self.redirection(redir_url)
                self.finished()
                #self.error(KIO.ERR_DOES_NOT_EXIST, url.path())
                return

As before, non-existant objects within the image cause errors to be reported:

            adfs_object = self.find_file_within_image(path)
            
            if not adfs_object:
            
                self.error(KIO.ERR_DOES_NOT_EXIST, path)
                return

In the tuple containing the object\'s details the second item may be in the form of a list. This would indicate that a directory has been found which we must deal with appropriately. However, for ordinary files we simply generate a suitable description of the file to return to the client:

            if type(adfs_object[1]) != type([]):
            
                entry = self.build_entry(adfs_object)

If the object was not a file then we must ensure that the path given contains a reference to a directory. If, on the other hand, the path is either empty or does not end in a manner expected for a directory then it is useful to redirect the client to an appropriate URL:

            elif path != u"" and path[-1] != u"/":
            
                # Directory referenced, but URL does not end in a slash.
                
                url.setPath(unicode(url.path()) + u"/")
                self.redirection(url)
                self.finished()
                return

If the URL referred to a directory then a description can be returned to the client in a suitable form:

            else:
            
                entry = self.build_entry(adfs_object)

After a description of the object found has been constructed, it only remains for us to return the description (or entry in the filesystem) to the client by submitting it to the KIOSlave framework. This is performed by the following operation to the `statEntry`{.backtick} method, and is followed by a `finished`{.backtick} call to indicate that there are no more entries to process:

            if entry != []:
            
                self.statEntry(entry)
                
                self.finished()
            
            else:
            
                self.error(KIO.ERR_DOES_NOT_EXIST, path)

### The mimetype operation 

In many virtual filesystems, the `mimetype`{.backtick} operation would require a certain amount of work to determine MIME types of files, or sufficient planning to ensure that data is returned in a format in line with a predetermined MIME type. Since its use is optional, we do not define a method to determine the MIME types of any files within our virtual filesystem. The client will have to inspect the contents of such files in order to determine their MIME types.

### The listDir operation 

The contents of a directory on our virtual filesystem are returned by the `listDir`{.backtick} method. This works like the `stat`{.backtick} method, but returns information on multiple objects within a directory.

As for the previous methods the validity of the URL is checked. If no suitable directory found within the disk image, the path component of the original URL is extracted and the client redirected to this location. Note that the `url`{.backtick} argument is a `kdecore.KURL`{.backtick} object.

        def listDir(self, url):
        
            path = self.parse_url(url)
            
            if path is None:
            
                redir_url = KURL(url.path())
                
                self.redirection(redir_url)
                self.finished()
                return

Having established that the path refers to a valid disk image, we try to find the specified object within the image, returning an error if nothing suitable is found:

            adfs_object = self.find_file_within_image(path)
            
            if not adfs_object:
            
                self.error(KIO.ERR_DOES_NOT_EXIST, path)
                return

If the path does not end in a slash then redirect the client to a URL which does. This ensures that either a directory will be retrieved or an error will be returned to the client:

            elif path != u"" and path[-1] != u"/":
            
                url.setPath(unicode(url.path()) + u"/")
                self.redirection(url)
                self.finished()
                return

If a file is referenced then an error is returned to the client because we can only list the contents of a directory:

            elif type(adfs_object[1]) != type([]):
            
                self.error(KIO.ERR_IS_FILE, path)
                return

A list of files is kept in the second item of the object returned from the support module. For each of these files, we must construct an entry which is understandable to the KIOSlave infrastructure in a manner similar to that used in the method for the `stat`{.backtick} operation.

            # Obtain a list of files.
            files = adfs_object[1]
            
            # Return the objects in the list to the application.
            
            for this_file in files:
            
                entry = self.build_entry(this_file)
                
                if entry != []:
                
                    self.listEntry(entry, 0)
                    
                    # For old style disk images, return a .inf file, too.
                    if self.adfsdisc.disc_type.find("adE") == -1:
                    
                        this_inf = self.find_file_within_image(
                            path + "/" + this_file[0] + ".inf"
                            )
                        
                        if this_inf is not None:
                        
                            entry = self.build_entry(this_inf)
                            
                            if entry != []:
                            
                                self.listEntry(entry, 0)
            
            # We have finished listing the contents of a directory.
            self.listEntry([], 1)
            
            self.finished()

### The dispatch loop 

Although not entirely necessary, we implement a `dispatchLoop`{.backtick} method which simply calls the corresponding method of the base class:

        def dispatchLoop(self):
        
            KIO.SlaveBase.dispatchLoop(self)

## Utility methods 

We define some methods which, although necessary for this IOSlave to work, are not standard virtual methods to be reimplemented. However, they do contain code which might be usefully reused in other IOSlaves.

### Building file system entries 

We create a method to assist in building filesystem entries to return to the client via the KIOSlave infrastructure. For this example, some basic details of each file or directory in the disk image is derived from information contained within and stored within standard `KIO.UDSAtom`{.backtick} instances.

        def build_entry(self, obj):
        
            entry = []

We check the type of object passed to the method in order to determine the nature of the information returned. For files we do not provide a predetermined MIME type, leaving the client to determine this from data retrieved from the disk image.

            if type(obj[1]) != type([]):
            
                # [name, data, load, exec, length]
                name = self.encode_name_from_object(obj)
                length = obj[4]

Files stored in old disk images require accompanying *.inf* files to describe their original attributes. The following code provides details of these files which are not actually present in the disk image, but are generated automatically by this IOSlave:

                if self.adfsdisc.disc_type.find("adE") == -1 and \\
                    obj[0][-4:] == ".inf":
                
                    # For .inf files, use a MIME type of text/plain.
                    mimetype = "text/plain"
                
                else:
                
                    # Let the client discover the MIME type by reading
                    # the file.
                    mimetype = None
            
            else:
            
                name = self.encode_name_from_object(obj)
                length = 0
                mimetype = "inode/directory"

Having determined the MIME type we now declare all the relevant attributes of the object and return these to the caller:

            atom = KIO.UDSAtom()
            atom.m_uds = KIO.UDS_NAME
            atom.m_str = name
            
            entry.append(atom)
            
            atom = KIO.UDSAtom()
            atom.m_uds = KIO.UDS_SIZE
            atom.m_long = length
            
            entry.append(atom)
            
            atom = KIO.UDSAtom()
            atom.m_uds = KIO.UDS_MODIFICATION_TIME
            # Number of seconds since the epoch.
            atom.m_long = int(time.time())
            
            entry.append(atom)
            
            atom = KIO.UDSAtom()
            atom.m_uds = KIO.UDS_ACCESS
            # The usual octal permission information (rw-r--r-- in this case).
            atom.m_long = 0644
            
            entry.append(atom)
            
            # If the stat method is implemented then entries _must_ include
            # the UDE_FILE_TYPE atom or the whole system may not work at all.
            
            atom = KIO.UDSAtom()
            atom.m_uds = KIO.UDS_FILE_TYPE
            
            if mimetype != "inode/directory":
            
                atom.m_long = os.path.stat.S_IFREG
            
            else:
            
                atom.m_long = os.path.stat.S_IFDIR
            
            entry.append(atom)
            
            if mimetype:
            
                atom = KIO.UDSAtom()
                atom.m_uds = KIO.UDS_MIME_TYPE
                atom.m_str = mimetype
                
                entry.append(atom)
            
            return entry

### Encoding filenames 

The following two internal methods deal with the translation of paths and filenames within the disk image to and from canonical URL style paths. These are only of interest to those familiar with ADFS style paths.

        def encode_name_from_object(self, obj):
        
            name = obj[0]
            
            # If the name contains a slash then replace it with a dot.
            new_name = u".".join(name.split(u"/"))
            
            if self.adfsdisc.disc_type.find("adE") == 0:
            
                if type(obj[1]) != type([]) and u"." not in new_name:
                
                    # Construct a suffix from the object's load address/filetype.
                    suffix = u"%03x" % ((obj[2] >> 8) & 0xfff)
                    new_name = new_name + "." + suffix
            
            return unicode(KURL.encode_string_no_slash(new_name))
        
        def decode_name(self, name):
        
            return unicode(KURL.decode_string(name))

### Locating objects within a disk image 

A key element in the construction of an IOSlave is the method used to map between the URLs given by client applications and the conventions of the virtual filesystems represented by the IOSlave. In this instance, the disk image contains a working snapshot of an ADFS filesystem which must be navigated in order to extract objects referenced by the client.

Since the `ADFSlib`{.backtick} support module provides objects to contain the directory structure contained within the disk image, only a minimal amount of work is required to locate objects, and this mainly involves a recursive examination of a tree structure. However, there are a few special cases which are worth mentioning.

In this method, the `path`{.backtick} argument contains the path component of the URL supplied by the client in the standard form used in URLs.

        def find_file_within_image(self, path, objs = None):

A convention we have adopted is the use of a default value of `None`{.backtick} for the final argument of this method. Omission of this argument indicates that we are starting a search from the root directory of the disk image. As we descend into the directory structure, recursive calls to this method will supply suitable values for this argument but, for now, a reasonable value needs to be substituted for `None`{.backtick}; this is a structure containing the entire filesystem:

            if objs is None:
            
                objs = self.adfsdisc.files

If an empty path was supplied then it is assumed that an object corresponding to the root directory was being referred to. In such a case a slash character is given as the name of the object, and the list of objects supplied is given as the contents of the root directory:

            if path == u"":
            
                # Special case for root directory.
                return [u"/", objs, 0, 0, 0]

For non-trivial paths, we split the path string into elements corresponding to the names of files and directories expected as we descend into the filesystem\'s hierarchy of objects, then we remove any empty elements:

            elements = path.split(u"/")
            
            elements = filter(lambda x: x != u"", elements)

For each object found in the current directory, we examine each object and compare its name to the next path element expected.

            for this_obj in objs:
            
                if type(this_obj[1]) != type([]):
                
                    # A file is found. 

If a file is found in the filesystem, we translate its name so that we can compare it with the next path element expected:

                    obj_name = self.encode_name_from_object(this_obj)
                    
                    if obj_name == elements[0]:
                    
                        # A match between names.

For files, we perform the simple test that the current path element is the final one in the list, and return the corresponding object if this is the case. If this is not the case then the URL is likely to be invalid:

                        if len(elements) == 1:
                        
                            # This is the last path element; we have found the
                            # required file.
                            return this_obj
                        
                        else:
                        
                            # There are more elements to satisfy but we can
                            # descend no further.
                            return None

If a direct match between names is not possible then, for old-style disk images, it is possible that the path is referring to a *.inf* file; we check for this possibility, applying the same check on the remaining path elements as before:

                    elif self.adfsdisc.disc_type.find("adE") == -1 and \\
                         elements[0] == obj_name + u".inf":

If successfully matched, a *.inf* file is created and returned, otherwise a `None`{.backtick} value is returned to indicate failure:

                        if len(elements) == 1:
                        
                            file_data = "%s\t%X\t%X\t%X\n" % \\
                                tuple(this_obj[:1] + this_obj[2:])
                            
                            new_obj = \\
                            (
                                this_obj[0] + ".inf", file_data,
                                0, 0, len(file_data)
                            )
                            
                            return new_obj
                        
                        else:
                        
                            # There are more elements to satisfy but we can
                            # descend no further.
                            return None
                
                else:
                
                    # A directory is found.

As for files, the names of directories found in the filesystem are translated for comparison with the next path element expected:

                    obj_name = self.encode_name_from_object(this_obj)
                    
                    if obj_name == elements[0]:
                    
                        # A match between names.

Unlike files, directories can occur at any point in the descent into the filesystem. Therefore, we either return the object corresponding to the last path element or descend into the directory found:

                        if len(elements) == 1:
                        
                            # This is the last path element; we have found the
                            # required file.
                            return this_obj
                        
                        else:
                        
                            # More path elements need to be satisfied; descend
                            # further.
                            return self.find_file_within_image(
                                u"/".join(elements[1:]), this_obj[1]
                                )

At this point, no matching objects were found, therefore we return `None`{.backtick} to indicate failure:

            return None
