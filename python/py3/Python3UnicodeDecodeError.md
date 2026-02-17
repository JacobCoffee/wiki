# Python3UnicodeDecodeError

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# PEP: Python3 and UnicodeDecodeError 

This is a PEP describing the behaviour of Python3 on [UnicodeDecodeError](UnicodeDecodeError). It\'s a **draft**, don\'t hesitate to comment it. This document suppose that my patch to allow bytes filenames is accepted which is not the case today.

While I was writing this document I found poential problems in Python3. So here is a TODO list (things to be checked):

- FIXME: When bytearray is accepted or not?
- FIXME: Allow bytes/str mix for shutil.copy\*()? The ignore callback will get bytes or unicode?

Can anyone write a section about bytes encoding in Unicode using escape sequence?

What is the best tool to work on a PEP? I hate email threads, and I would prefer SVN / Mercurial / anything else.

------------------------------------------------------------------------

# Python3 and UnicodeDecodeError for the command line, environment variables and filenames 

## Introduction 

Python3 does its best to give you texts encoded as a valid unicode characters strings. When it hits an invalid bytes sequence (according to the used charset), it has two choices: drops the value or raises an [UnicodeDecodeError](UnicodeDecodeError). This document present the behaviour of Python3 for the command line, environment variables and filenames.

Example of an invalid bytes sequence: ::

    >>> str(b'\xff', 'utf8')
    UnicodeDecodeError: 'utf8' codec can't decode byte 0xff (...)

whereas the same byte sequence is valid in another charset like ISO-8859-1: ::

    >>> str(b'\xff', 'iso-8859-1')
    'ÿ'

## Default encoding 

Python uses \"UTF-8\" as the default Unicode encoding. You can read the default charset using sys.getdefaultencoding(). The \"default encoding\" is used by [PyUnicode](./PyUnicode.html)\_[FromStringAndSize](./FromStringAndSize.html)().

A function sys.setdefaultencoding() exists, but it raises a [ValueError](./ValueError.html) for charset different than UTF-8 since the charset is hardcoded in [PyUnicode](./PyUnicode.html)\_[FromStringAndSize](./FromStringAndSize.html)().

## Command line 

Python creates a nice unicode table for sys.argv using mbstowcs(): ::

    $ ./python -c 'import sys; print(sys.argv)' 'Ho hé !'
    ['-c', 'Ho hé !']

On Linux, mbstowcs() uses LC_CTYPE environement variable to choose the encoding. On an invalid bytes sequence, Python quits directly with an exit code 1. Example with UTF-8 locale:

    $ python3.0 $(echo -e 'invalid:\xff')
    Could not convert argument 1 to string

## Environment variables 

Python uses \"\_wenviron\" on Windows which are contains unicode (UTF-16-LE) strings.  On other OS, it uses \"environ\" variable and the UTF-8 charset. It drops a variable if its key or value is not convertible to unicode. Example:

    env -i HOME=/home/my PATH=$(echo -e "\xff") python
    >>> import os; list(os.environ.items())
    [('HOME', '/home/my')]

Both key and values are unicode strings. Empty key and/or value are allowed.

Python ignores invalid variables, but values still exist in memory. If you run a child process (eg. using os.system()), the \"invalid\" variables will also be copied.

## Filenames 

### Introduction 

Python2 uses byte filenames everywhere, but it was also possible to use unicode filenames. Examples:

- os.getcwd() gives bytes whereas os.getcwdu() always returns unicode

- os.listdir(unicode) creates bytes or unicode filenames (fallback to bytes on [UnicodeDecodeError](UnicodeDecodeError)), os.readlink() has the same behaviour

- glob.glob() converts the unicode pattern to bytes, and so create bytes filenames

- open() supports bytes and unicode

Since listdir() mix bytes and unicode, you are not able to manipulate easily filenames:

    >>> path=u'.'
    >>> for name in os.listdir(path):
    ...  print repr(name)
    ...  print repr(os.path.join(path, name))
    ...
    u'valid'
    u'./valid'
    'invalid\xff'
    Traceback (most recent call last):
    ...
    File "/usr/lib/python2.5/posixpath.py", line 65, in join
        path += '/' + b
    UnicodeDecodeError: 'ascii' codec can't decode byte 0xff (...)

Python3 supports both types, bytes and unicode, but disallow mixing them. If you ask for unicode, you will always get unicode or an exception is raised.

You should only use unicode filenames, except if you are writing a program fixing file system encoding, a backup tool or you users are unable to fix their broken system.

## Windows 

Microsoft Windows since Windows 95 only uses Unicode (UTF-16-LE) filenames. So you should only use unicode filenames.

### Non Windows (POSIX) 

POSIX OS like Linux uses bytes for historical reasons. In the best case, all filenames will be encoded as valid UTF-8 strings and Python creates valid unicode strings. But since system calls uses bytes, the file system may returns an invalid filename, or a program can creates a file with an invalid filename.

An invalid filename is a string which can not be decoded to unicode using the default file system encoding (which is UTF-8 most of the time).

A robust program will have to use only the bytes type to make sure that it can open / copy / remove any file or directory.

### Filename encoding 

Python use:

- \"mbcs\" on Windows
- or \"utf-8\" on Mac OS X
- or nl_langinfo(CODESET) on OS supporting this function
- or UTF-8 by default

\"mbcs\" is not a valid charset name, it\'s an internal charset saying that Python will use the function [MultiByteToWideChar](./MultiByteToWideChar.html)() to decode bytes to unicode. This function uses the current codepage to decode bytes string.

You can read the charset using sys.getfilesystemencoding(). The function may returns None if Python is unable to determine the default encoding.

[PyUnicode](./PyUnicode.html)\_DecodeFSDefaultAndSize() uses the default file system encoding, or UTF-8 if it is not set.

On UNIX (and other operating systems), it\'s possible to mount different file systems using different charsets. sys.getdefaultencoding() will be the same for the different file systems since this encoding is only used between Python and the Linux kernel, not between the kernel and the file system which may uses a different charset.

### Display a filename 

Example of a function formatting a filename to display it to human eyes: ::

    from sys import getfilesystemencoding
    def format_filename(filename):
        return str(filename, getfilesystemencoding(), 'replace')

Example: format_filename(\'r\\xffport.doc\') gives \'r�port.doc\' with the UTF-8 encoding.

### Functions producing filenames 

Policy: for unicode arguments: drop invalid bytes filenames; for bytes arguments: return bytes

- os.listdir()
- glob.glob()

This behaviour (drop silently invalid filenames) is motivated by the fact to if a directory of 1000 files only contains one invalid file, listdir() fails for the whole directory. Or if your directory contains 1000 python scripts (.py) and just one another document with an invalid filename (eg. r�port.doc), glob.glob(\'\*.py\') fails whereas all .py scripts have valid filename.

Policy: for an unicode argument: raise an [UnicodeDecodeError](UnicodeDecodeError) on invalid filename; for an bytes argument: return bytes

- os.readlink()

Policy: create unicode directory or raise an [UnicodeDecodeError](UnicodeDecodeError)

- os.getcwd()

Policy: always returns bytes

- os.getcwdb()

### Functions for filename manipulation 

Policy: raise [TypeError](TypeError) on bytes/str mix

- os.path.\*(), eg. os.path.join()
- fnmatch.\*()

### Functions accessing files 

Policy: accept both bytes and str

- io.open()
- os.open()
- os.chdir()
- os.stat(), os.lstat()
- os.rename()
- os.unlink()
- shutil.\*()

os.rename(), shutil.copy\*(), shutil.move() allow to use bytes for an argment, and unicode for the other argument

### bytearray

In most cases, bytearray() can be used as bytes for a filename.

## Unicode normalisation 

Unicode characters can be normalized in 4 forms: NFC, NFD, NFKC or NFKD. Python does never normalize strings (nor filenames). No operating system does normalize filenames. So the users using different norms will be unable to retrieve their file. Don\'t panic! All users use the same norm.

Use unicodedata.normalize() to normalize an unicode string.
