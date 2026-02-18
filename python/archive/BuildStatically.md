# BuildStatically

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# Building Python Statically 

This page describes the steps required to build Python statically, derived from [this thread](http://groups.google.com/group/comp.lang.python/browse_thread/thread/eba7c323a0221b97?hl=en#3314cbe8234de6c5). It presently covers Linux, but many of the same steps apply to other OSs. The goal is to get `ldd`{.backtick} to say:

    $ ldd /path/to/python
    not a dynamic executable

Building the python binary is fairly straightforward:

    $ ./configure LDFLAGS="-static" --disable-shared
    $ make LDFLAGS="-static" LINKFORSHARED=" "

`LINKFORSHARED=" "`{.backtick} prevents passing `-export-dynamic`{.backtick} to the linker, which will cause the binary to be built as a dynamically linked executable. You may need additional flags to build successfully.

This will build a static python binary, without any of the libraries normally provided by dynamically loaded modules. To add these modules, edit Modules/Setup.local, and add

    *static*

followed by any of the modules that you want to build into your python binary. Any line in Modules/Setup.local with an \"=\" will be interpreted as a Makefile variable definition rather than a module. For instance, if you wanted to build in the math library, add

    math mathmodule.c _math.c # -lm # math library functions, e.g. sin()

Note that the line is not commented (unlike the corresponding line in Modules/Setup). See Modules/Setup for guides on enabling other libraries, further examples and documentation.

## See also 

- [http://stackoverflow.com/questions/1150373/compile-the-python-interpreter-statically](http://stackoverflow.com/questions/1150373/compile-the-python-interpreter-statically)

- [http://mdqinc.com/blog/2011/08/statically-linking-python-with-cython-generated-modules-and-packages/](http://mdqinc.com/blog/2011/08/statically-linking-python-with-cython-generated-modules-and-packages/)
