# PythonCdDownload

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# General hints 

![/!\\](/wiki/europython/img/alert.png "/!\") Currently the [PythonCd](PythonCd) is at an early stage. Although it is basically usable, it still needs some polishing, testing and bug fixing. So at this time, these download sources are intended for its developers and testers only, not for educational purposes and beginners. We will remove this comment as soon as it is ready for prime time.

If anybody downloads and tests the [PythonCd](PythonCd), please give some feedback here in the wiki. I expect some feedback before releasing the next version of it to make it better fit your expectations.

# Where you can get the PythonCd on the internet 

- [ftp://ftp.uni-erlangen.de/pub/Linux/LOCAL/PythonCD/](ftp://ftp.uni-erlangen.de/pub/Linux/LOCAL/PythonCD/) (Germany, primary site)

- [ftp://ftp.uni-stuttgart.de/pub/mirror/ftp.uni-erlangen.de/pub/Linux/PythonCD/](ftp://ftp.uni-stuttgart.de/pub/mirror/ftp.uni-erlangen.de/pub/Linux/PythonCD/) (Germany)

- (please make some additional mirrors in other parts of the world)

You will find a README there with some words about what you will get by downloading the `*.iso`{.backtick} file and a `*.iso.md5`{.backtick} file which is used for checking if your download was successful. If there are multiple `*.iso`{.backtick} files, you only need to get the latest release, there is a `yyyy-mm-dd`{.backtick} timestamp in the file name.

# Checking integrity of the ISO image 

After downloading `pythoncd-xxxx-xx-xx.iso`{.backtick} and `pythoncd-xxxx-xx-xx.iso.md5`{.backtick} use this Linux command to check if the download is OK:

    md5sum -c pythoncd-xxxx-xx-xx.iso.md5
    # if it doesn't complain, everything is ok

`xxxx-xx-xx`{.backtick} has to be replaced by the real date in the file name, e.g. `2004-07-02`{.backtick}, of course.

# Burning the CD 

The `*.iso`{.backtick} ISO-image file must be burned on a CDR/CDRW media of appropriate size (currently 700MB). Better use CDRW media to be able to overwrite them again when a new version is released.

Make sure you choose the right option of your CD burning software which makes a CD from an ISO image.

![/!\\](/wiki/europython/img/alert.png "/!\") Do not master a fresh data CD containing the ISO file as a regular data file, this is wrong and won\'t boot nor work as intended in any other way.

# Booting from the CD 

![/!\\](/wiki/europython/img/alert.png "/!\") You maybe have to enter your PC\'s BIOS and change **Boot sequence** to **CDROM,C,A** (or something similar) to make your PC boot from a bootable CD before trying to boot from hard disk.

Then you should get the boot prompt from the [PythonCd](PythonCd).

Just enter one of these boot options and hit \<ENTER\>:

::: {}
  ------ ------------------------------------------------------------
  en24   english and kernel 2.4
  en26   english and kernel 2.6 (default if you just hit \<ENTER\>)
  de24   german and kernel 2.4
  de26   german and kernel 2.6
  ------ ------------------------------------------------------------
:::

The function keys F2 and F3 also show some other options. Use `desktop=fluxbox`{.backtick} in any case (there is no KDE).

The [PythonCd](PythonCd) then should boot and show a fluxbox windowmanager (try right mouse button!) and a mozilla browser to you. Have fun!
