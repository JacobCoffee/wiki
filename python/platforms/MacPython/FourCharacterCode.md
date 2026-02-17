# MacPython/FourCharacterCode

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

By convention, Apple uses four character codes in place of integer enumerations in almost all of its software, protocols, and file formats.

Notes:

- Four character codes are literally four [../MacRoman](MacRoman) characters (including `\x00`, but usually four 7-bit ASCII safe characters).

- When \"packed\" as an integer, they are almost always stored in big endian format as a 32bit signed integer (e.g. `strnAsInteger = struct.unpack(">i", 'strn')`).

- You may see crazy stuff like © or ™ in four character codes (or maybe just garbage, depending on the text editor). The text encoding used is always [MacRoman](./MacRoman.html). Fortunately, the general case is the 7-bit subset of [../MacRoman](MacRoman) that overlaps with ASCII.

- Four character codes are supposed to be globally unique in context, but not in general.

- Apple maintains a registry of application signatures via Developer Technical Support. This list is not publically available.

- Apple maintains exclusive \"ownership\" of all lowercase four character codes for their software and APIs.

Examples:

- `'hook'` - the application signature for iTunes (notice that it is an Apple product and is therefore lowercase)

- `'8BIM'` - the application signature for Adobe Photoshop.

- `'shor'` - the [../AEDesc](AEDesc) type code for a 16bit signed integer, also known as `typeSInt16`, `typeSMInt`, or `typeShortInteger`

In Python, four character codes are passed around as four character `str` (primarily for introspection purposes). Some Python code will automatically interchange four character codes with `str`, `unicode`, `int`, or `long` but that will not be the general case until Python 2.4 at the earliest. [../bgen](./MacPython(2f)bgen.html) may output constants that look like `FOUR_CHAR_CODE('shor')`, however `FOUR_CHAR_CODE` is (currently) a no-op and just returns the input string unchanged.

In C, four character codes are interchangable with 32 bit integer types and will usually be defined in an enumerator:

    /*  
        This is how you will see them in Universal Interfaces format 
    */
    enum {
        MyConstant = FOUR_CHAR_CODE('MooV'),
        MyOtherConstant = FOUR_CHAR_CODE('©xxx')
    }

    /*  
        This is the "new way" that you will see in OS X frameworks
    */
    enum {
        MyConstant = 'MooV',
        MyOtherConstant = (long)0xA9787878 /* so that the source isn't tainted with high ascii */
    }

See also:

- [../AppleEvents](AppleEvents)

- [../AppleScript](AppleScript)
