# ArrayInterface

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

This pre-PEP proposes enhancing the buffer protocol in Python 3000 to implement the array interface (protocol).

This Wiki will serve as a place to develop the PEP until it is assigned a number and committed to the Python development tree.

# Abstract 

This PEP proposes re-designing the buffer API (PyBufferProcs function pointers) to improve the way Python allows memory sharing in Python 3.0

In particular, it is proposed that the multiple-segment and character buffer portions of the buffer API are eliminated and additional function pointers are provided to allow sharing any multi-dimensional nature of the memory and what data-format the memory contains.

# Rationale 

The buffer protocol allows different Python types to exchange a pointer to a sequence of internal buffers. This functionality is **extremely** useful for sharing large segments of memory between different high-level objects, but it\'s too limited and has issues.

1.  There is the little (never?) used \"sequence-of-segments\" option (bf_getsegcount)

2.  There is the apparently redundant character-buffer option (bf_getcharbuffer)

3.  There is no way for a consumer to tell the buffer-API-exporting object it is \"finished\" with its view of the memory and therefore no way for the exporting object to be sure that it is safe to reallocate the pointer to the memory that it owns (the array object reallocating its memory after sharing it with the buffer object which held the original pointer led to the infamous buffer-object problem).

4.  Memory is just a pointer with a length. There is no way to describe what\'s \"in\" the memory (float, int, C-structure, etc.)

5.  There is no shape information provided for the memory. But, several array-like Python types could make use of a standard way to describe the shape-interpretation of the memory (!wxPython, GTK, pyQT, CVXOPT, PyVox, Audio and Video Libraries, ctypes, NumPy)

# General Proposal 

1.  Get rid of the char-buffer and multiple-segment sections of the buffer-protocol.
2.  Unify the read/write versions of getting the buffer.
3.  Add a new function to the protocol that should be called when the consumer object is \"done\" with the view.
4.  Add a new function to allow the protocol to describe what is in memory (unifying what is currently done now in struct and array)
5.  Add a new function to allow the protocol to share shape information

# Specification 

Change the [PyBufferProcs](./PyBufferProcs.html) structure to

    typedef struct {
         getbufferproc bf_getbuffer
         releasebufferproc bf_releasebuffer
         formatbufferproc bf_getbufferformat
         shapebufferproc bf_getbuffershape 
    }

The signatures and purposes of these function pointers are provided here:

    typedef Py_ssize_t (*getbufferproc)(PyObject *obj, void **buf, int  *writeable)

A pointer to the memory is returned in buf and the length of that memory buffer is the function return value. If the returned value of writeable is 1, then the buffer can be written to, otherwise it must only be read-from (writeable can be NULL). A -1 is returned if an error occurs.

    typedef int (*releasebufferproc)(PyObject *obj)

This function is called when a view of memory previously acquired from the object is no longer needed. It is up to the exporter of the API to make sure all views have been released before eliminating a reference to a previously returned pointer. It is up to consumers of the API to call this function on the object whose view is obtained when it is no longer needed. A -1 is returned on error and 0 on success.

    typedef char *(*formatbufferproc)(PyObject *obj)

Get the format-string of the memory using the struct-module string syntax (see below for proposed additions to that syntax). Also, there is never an alignment assumption in this string\-\--the full byte-layout is always required. If the implied size of this string is smaller than the length of the buffer then it is assumed that the string is repeated.

    typedef PyObject *(*shapebufferproc)(PyObject *obj)

Return a 3-tuple of lists containing shape information: (shape, strides, offsets). The strides and offsets objects can be None if the memory is C-style contiguous with 0 offsets in each dimension).

All of these routines are optional for a type object (but the last three make no sense unless the first one is implemented).

Some C-API calls should also be made available:

- PyObject\_[GetBuffer](./GetBuffer.html)()

- PyObject\_[ReleaseBuffer](./ReleaseBuffer.html)()

- PyObject\_[GetBufferFormat](./GetBufferFormat.html)()

- PyObject\_[GetBufferShape](./GetBufferShape.html)()

# Additions to the struct string-syntax 

::: {}
  --------------------- ---------------------------------------------------------------
  Character             Description
  \'1\'                 bit (number before states how many bits)
  \'?\'                 platform \_Bool type
  \'g\'                 long double
  \'F\'                 complex float
  \'D\'                 complex double
  \'G\'                 complex long double
  \'c\'                 ucs-1 (latin-1) encoding
  \'u\'                 ucs-2
  \'w\'                 ucs-4
  \'O\'                 pointer to Python Object
  \'T{}\'               structure (detailed layout inside {})
  \'(k1,k2,\...,kn)\'   multi-dimensional array of whatever follows
  \':name:\'            optional name of the preceeding element
  \'&\'                 specific pointer (prefix before another charater)
  \'X{}\'               pointer to a function (optional function signature inside {})
  --------------------- ---------------------------------------------------------------
:::

Endian-specification is also allowed inside the string so that it can change if needed.

According to the struct-module, a number can preceed a character code to specify how many of that type there are. The (k1,k2,\...,kn) extension also allows specifying if the data is supposed to be viewed as a multi-dimensional array of a particular format.

It would be nice if there were functions in ctypes to create a ctypes object from a struct description, and add long-double, and ucs-2 to ctypes.

Perhaps, the struct module should be incorporated into the ctypes module which would also grow a C-API.

# Code to be affected 

- buffer object
- bytes object
- string object
- array module
- struct module
- mmap module

anything else using the buffer API

# Issues 

The proposed locking mechanism relies entirely on the objects implementing the buffer interface to do their own thing. Ideally an object that implements the buffer interface should keep at least a number indicating how many releases are extant.

Currently the struct module does not allow specification of nested structures. It seems like specifying a nested structure should be specified as several ways of viewing memory areas (ctypes and [NumPy](NumPy)) already allow this.
