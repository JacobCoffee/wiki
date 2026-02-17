# MacPython/MacModelPerformance

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

This page collects some pystone numbers for various Mac models. As bad as the pystone benchmark is as a useful figure of merit, my intent is as much to compare various Mac models as it is to compare different Python versions and implementations. (I\'m in the market for a new laptop.) If you have some numbers for various Macs, please add row(s) to this table. Please at least use /usr/bin/python to run pystone, something like this:

    /usr/bin/python /usr/lib/python2.3/test/pystone.py

(`python2.3` will change according to version of Python shipped with your Mac. Run the command three times while your computer is otherwise idle then insert the largest pystone number in the table (rounded to the nearest pystone). `/usr/lib/python2.3/test/pystone.py` should work for all Python 2.x versions. If you report numbers for Python 3.0 you will have to use the pystone.py which comes with it.

::: {}
  --------------------------------------------- ---------------- ---------- ------------------ ----------------------------------------------- ---------- -------------------------------------------------------
  Model                                         CPU              Speed      Mac OS X Version   Python version                                  Pystones   Reporter
  PowerBook                                     G4               800MHz     10.4.11            /usr/bin/python (2.3.5)                         11905      [SkipMontanaro](SkipMontanaro)
  PowerBook                                     G4               800MHz     10.4.11            python from source (2.2.3+)                     10776      [SkipMontanaro](SkipMontanaro)
  PowerBook                                     G4               800MHz     10.4.11            python from source (2.4.4)                      14663      [SkipMontanaro](SkipMontanaro)
  PowerBook                                     G4               800MHz     10.4.11            python from source (2.5.2a0)                    15625      [SkipMontanaro](SkipMontanaro)
  PowerBook                                     G4               800MHz     10.4.11            python from source (2.6a0)                      15384      [SkipMontanaro](SkipMontanaro)
  PowerBook                                     G4               800MHz     10.4.11            python from source (3.0a2)                      11338      [SkipMontanaro](SkipMontanaro)
  Power Mac                                     2xG5             2GHz       10.4.11            /usr/bin/python (2.3.5)                         28410      [SkipMontanaro](SkipMontanaro)
  Power Mac                                     2xG5             2GHz       10.4.11            python from source (2.6a0, 32-bit)              35461      [SkipMontanaro](SkipMontanaro)
  Power Mac                                     2xG5             2GHz       10.4.11            python from source (2.6a0, 64-bit)              37313      [SkipMontanaro](SkipMontanaro)
  Power Mac                                     2xG5             2GHz       10.5.6             /usr/bin/python (2.5.1 r251:54863)              30307.4    [SkipMontanaro](SkipMontanaro)
  MacBook Pro                                   Core 2 Duo       2.2GHz     10.4.11            /usr/bin/python (2.3.5)                         38462      [GaryBernhardt](GaryBernhardt)
  MacBook Pro                                   Core 2 Duo       2.2GHZ     10.4.11            universal mac build (2.5.1)                     49505      [GaryBernhardt](GaryBernhardt)
  MacBook Pro                                   Core 2 Duo       2.2GHz     10.5.1             /usr/bin/python (Python 2.5.1 (r251:54863))     46453.6    [ThomasJuntunen](./ThomasJuntunen.html)
  MacBook Pro                                   Core 2 Duo       2.2GHz     10.5.6             /usr/bin/python (Python 2.5.1 (r251:54863))     46776.1    [SkipMontanaro](SkipMontanaro)
  MacBook Pro                                   Core 2 Duo       2.2GHz     10.5.6             Python 2.6.1+ (release26-maint:70232)           51437.2    [SkipMontanaro](SkipMontanaro)
  MacBook Pro                                   Core 2 Duo       2.33GHz    10.5.1             /usr/bin/python (Python 2.5.2a0)                52083      [RonaldOussoren](RonaldOussoren)
  MacBook Pro                                   Core 2 Duo       2.33GHz    10.5.1             /usr/bin/python (Python 2.5.2a0, 64-bit)        60871      [RonaldOussoren](RonaldOussoren)
  MacBook Pro                                   Core 2 Duo       2.4GHz     10.5.1             /usr/bin/python (Leopard version)               49958      [DavidReed](./DavidReed.html)
  MacBook Pro                                   Core 2 Duo       2.4GHz     10.5.1             /usr/local/bin/python2.5 (python.org version)   54945      [DavidReed](./DavidReed.html)
  iMac                                          Core 2 Duo       2.4GHz     10.5.1             /usr/bin/python (2.5.1)                         50613      [KevinHorton](./KevinHorton.html)
  iMac                                          Core 2 Duo       2.4GHz     10.5.1             /sw/bin/python (2.5.1 from Fink Project)        55254      [KevinHorton](./KevinHorton.html)
  iMac                                          Core 2 Duo       2.4GHz     10.5.1             universal mac build (2.5.1)                     56180      [CharlesMoad](./CharlesMoad.html)
  iMac                                          Core 2 Duo       2.8GHz     10.5.1             /usr/bin/python (2.5.1)                         59101.5    [NicholasRiley](./NicholasRiley.html)
  Mac Mini                                      Core Duo         1.66GHz    10.4.11            universal mac build (2.5.1)                     37878.8    [BlakeWinton](./BlakeWinton.html)
  MacBook                                       Core 2 Duo       2Ghz       10.5.1             /usr/bin/python (2.5.1)                         41593.7    [JackJansen](JackJansen)
  Mac Pro                                       Quad-core Dual   3.0GHz     10.5.11            universal mac build (2.5.1)                     63019.7    [DanielLord](./DanielLord.html)
  Mac Pro                                       Quad-core        2.66Ghz    10.5.1             /usr/bin/python (2.5.1)                         62578.2    [JackJansen](JackJansen)
  Mac Pro                                       Quad-core        2.66Ghz    10.4.11            universal mac build (2.5.1)                     63291.1    [NicholasRiley](./NicholasRiley.html)
  Mac Book                                      Dual             2.16 GHz   10.5.1             universal 2.5.1                                 44578.2    [BrianRay](BrianRay)
  MacBook Pro                                   Core 2 Duo       2.33 GHz   10.4.11            Python 2.4.4 (build 5341)                       40650.4    [EricLewin](EricLewin)
  [MacBook](./MacBook.html) Pro   Core 2 Duo       2.2 GHz    10.6.2             Python 2.6.1 (r261:67515)                       58225      [JoaoRodrigues](./JoaoRodrigues.html)
  --------------------------------------------- ---------------- ---------- ------------------ ----------------------------------------------- ---------- -------------------------------------------------------
:::

Here\'s a table for iPhone and iPod Touch devices. If you have a device which was jailbroken it\'s likely that Python is available for it.

::: {}
  --------------- ----- ----------- ---------------------------- --------------------------- --------- ---------------------------------------
  iPod Touch 1G   ARM   412MHz(?)   iPhone OS (Firmware 2.2.1)   Python 2.5.1 (r251:54863)   1192.75   [SkipMontanaro](SkipMontanaro)
  --------------- ----- ----------- ---------------------------- --------------------------- --------- ---------------------------------------
:::

::: {}
  --------------- --------------- -------- ---------------------------- -------------- ------ -----------------------------------------------------
  iPod Touch 3G   ARM Cortex A8   600MHz   iPhone OS (Firmware 3.1.2)   Python 2.5.1   4717   [JoaoRodrigues](./JoaoRodrigues.html)
  --------------- --------------- -------- ---------------------------- -------------- ------ -----------------------------------------------------
:::
