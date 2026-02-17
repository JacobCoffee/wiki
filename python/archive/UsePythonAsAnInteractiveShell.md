# UsePythonAsAnInteractiveShell

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

The idea: using the Python interpreter as an [InteractiveShell](./InteractiveShell.html).

# Command execution 

Use short method names:

:::: 
::: 
``` 
   1 def S(arg):
   2   """returns string of executed command arg"""
   3   return os.popen(arg).read()
   4 
   5 def SN(arg):
   6   """returns list of executed command arg"""
   7   return os.popen(arg).read().split('\n')
   8 
   9 def SP(arg):
  10   """prints string of executed command arg"""
  11   print S(arg)
  12 
  13 def SNP(arg):
  14   """prints with lines list executed command arg"""
  15   for i in SN(arg):
  16     print i
```
:::
::::

Command execution is the one thing an [InteractiveShell](./InteractiveShell.html) has to be good at. Typing S(\"\<command\>\") is too much overhead for command execution. Still, a mixture of bash style command execution and shell programming with Python would be great.

------------------------------------------------------------------------

I\'d want the simple style of command execution from bash available:

    cd /foo/bar

But also the Python style for more complex commands:

    os.setcwd('/foo/bar')

Some ways to execute the bash-style command:

- Use os.popen(\<command\>).

- Map all commands to Python functions: cd(), less(), all taking a list of strings as arguments.

- Completely separate bash-style commands from Python commands, executing it with bash.

\-- [JohannesGijsbers](JohannesGijsbers) 2002-12-07 03:34:05

There is a project that attempts to acheive this. Quasi ([http://quasi-shell.sourceforge.net/](http://quasi-shell.sourceforge.net/)) provides a shell within which Python can be freely mixed with OS (and certain database) commands. \-- [BenLast](./BenLast.html)

- This sounds a lot like [lwickjr/Modules](./lwickjr(2f)Modules.html)/Alias.py when coupled with a module of shell-command functions. See [lwickjr/Modules](./lwickjr(2f)Modules.html) for further information.

  - \--[lwickjr](lwickjr)

# Path manipulation 

The os.path module provides a good set of functions for path manipulation, but you might also want to split the path at the root:

:::: 
::: 
``` 
   1 import re
   2 def splitroot(s):
   3   if "/" not in s:
   4     return '',s
   5   if s[0] == '/':
   6     s = s[1:]
   7   m = re.match("(.*?)/(.*)$",s)
   8   return m.groups()
```
:::
::::

# awk comparables 

Simply use the re module. It\'s a fuller set of regular expressions. Create a wrapper function for a utility for this if you want call it inlinegrep.

# Limitations 

The killall function was rejected by the [BDFL](BDFL). As far as I can see from the previous version of this page, Guido rejected it because it isn\'t in POSIX. I couldn\'t find any references on this in the mailing list archives. Anyone?

See also:

- [The Perl Shell](http://www.gregorpurdy.com/gregor/psh/)
