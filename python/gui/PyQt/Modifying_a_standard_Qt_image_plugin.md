# PyQt/Modifying_a_standard_Qt_image_plugin

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# Modifying a standard Qt image plugin 

I created a Qt image format plugin to write CCITT-compressed TIFF files by stripping out everything that wasn\'t needed from the standard TIFF plugin in Qt.

Here\'s a recipe for those of you interested in doing the same thing:

1.  Locate the src/plugins/imageformats/tiff directory in the Qt source package.

2.  Copy it, creating a new directory called tiff_ccitt for the modifications. Make the following modifications to files in that directory.

3.  Apply the [set of patches](attachments/PyQt(2f)Modifying_a_standard_Qt_image_plugin/tiff_ccitt.patches "set of patches") to the files in that directory, typically by entering the directory at the command line and typing

    {{{patch \< tiff_ccitt.patches }}}

Now, you should be able to build the plugin by typing the following commands:
