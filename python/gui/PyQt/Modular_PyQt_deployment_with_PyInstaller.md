# PyQt/Modular_PyQt_deployment_with_PyInstaller

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# How to distribute only the qt4 dlls and pyqt libraries that your application really needs 

If you want to finetune the size of a [PyQt](PyQt) application, the best way is to recompile Qt/PyQt to use a consolidated module. Basically:

1.  Compile Qt statically (`configure --static`). It will build static libraries (.lib) instead of dlls.

2.  Compile [PyQt](PyQt) with `--consolidate` (but \*without\* `--static`, since you still want a dynamic .pyd module). Add `--enable` for the modules you need and `--plugin` for the plugins you need. This will give you a big \_qt.pyd with everything inside (no external dependencies), plus small Qt\*.pyd wrappers to make your existing code work. You will save space twice because:

    - it will just include the parts you need
    - it will compress \*tons\* better (because there are no relocations symbols, more stuff is inlined, etc.).

3.  Give that to [PyInstaller](PyInstaller) trunk with latest UPX (with LZMA support) and its\'s done.

Then, you might want to see the output of ArchiveViewer.py run over the final executable, so that you will see the list of all modules that have been brought in. If there\'s something that [PyInstaller](PyInstaller) thought you might need but you actually don\'t use, you can hand-edit the `excludes=[]` list in the .spec file to avoid bringing them in.
