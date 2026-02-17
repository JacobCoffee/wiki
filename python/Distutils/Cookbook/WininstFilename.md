# Distutils/Cookbook/WininstFilename

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# Problem 

Windows binary installers often have dependencies on other binary libraries which one would like to include in the filename for the installer such as PyOpenGL-2.0.1-Numpy23.exe

# Solution 

Subclass bdist_wininst to introduce a customisation point for acquiring the filename.

    import sys, os, string, struct
    from distutils.command.bdist_wininst import bdist_wininst

    class BdistWinInstaller(bdist_wininst):
        """Version of bdist_wininst with customization point for filename

        This class should operate identically to the built-in
        class, it exists solely to provide the customization point.
        """
        def get_installer_filename(self, directory, fullname, target_version= None):
            """Calculate the final installer filename"""
            if target_version:
                return os.path.join(
                    directory,
                    "%s.win32-py%s.exe" % (
                        fullname,
                        target_version
                    )
                )
            else:
                return os.path.join(
                    directory,
                    "%s.win32.exe" % fullname
                )
        def create_exe (self, arcname, fullname, bitmap=None):
            """Do the actual creation of the executable file

            The base command, unfortunately, does not break down
            this command into sub-commands, so this method is
            almost entirely a duplication of the base-class method,
            with the only noticeable difference being the
            call to get_installer_filename(...) instead of
            calculating the filename inline.
            """
            import struct

            self.mkpath(self.dist_dir)

            cfgdata = self.get_inidata()
            installer_name = self.get_installer_filename(
                self.dist_dir,
                fullname,
                self.target_version,
            )
            self.announce("creating %s" % installer_name)

            if bitmap:
                bitmapdata = open(bitmap, "rb").read()
                bitmaplen = len(bitmapdata)
            else:
                bitmaplen = 0

            file = open(installer_name, "wb")
            file.write(self.get_exe_bytes())
            if bitmap:
                file.write(bitmapdata)

            file.write(cfgdata)
            header = struct.pack("<iii",
                                 0x1234567A,       # tag
                                 len(cfgdata),     # length
                                 bitmaplen,        # number of bytes in bitmap
                                 )
            file.write(header)
            file.write(open(arcname, "rb").read())

# Discussion 

This might be better introduced as part of the core rather than as a seperate recipe, as the customisation point doesn\'t alter the base operation, just provides a hook for the customisation.

------------------------------------------------------------------------

[CategoryDistutilsCookbook](CategoryDistutilsCookbook)
