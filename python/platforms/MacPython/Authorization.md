# MacPython/Authorization

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# Authorization 

- Authorization is a Python wrapper for Apple\'s Authorization API. Basically, it allows you to spawn arbitrary processes as root after successfully authenticating as an administrator. This is useful for installers, twiddling kernel settings (via sysctl or the like), etc.

# status

Authorization is currently at its first public release, 0.1.

# examples

:::: 
::: 
``` 
   1 import os, sys, struct, tempfile
   2 from Authorization import Authorization, kAuthorizationFlagDestroyRights
   3 
   4 AUTHORIZEDTOOL = "#!%s\n%s" % (sys.executable,
   5 r"""
   6 import os
   7 print os.getuid(), os.geteuid()
   8 os.setuid(0)
   9 print "I'm root!"
  10 """)
  11 
  12 def main():
  13     auth = Authorization(destroyflags=(kAuthorizationFlagDestroyRights,))
  14     fd, name = tempfile.mkstemp('.py')
  15     os.write(fd, AUTHORIZEDTOOL)
  16     os.close(fd)
  17     os.chmod(name, 0700)
  18     try:
  19         pipe = auth.executeWithPrivileges(name)
  20         sys.stdout.write(pipe.read())
  21         pipe.close()
  22     finally:
  23         os.unlink(name)
  24 
  25 if __name__=='__main__':
  26     main()
```
:::
::::

## Leopard 

This will not compile directly on Leopard. You will need to change line 14 of Authorization.pxi from \"raise\" to \"raise \_err\".

The following shows a concrete example for using this with Leopard.

    # This has been tested on a Mac OS X 10.5.5 Leopard stock Python installation
    # on October 25, 2008

    # The following is sufficient for using Pyrex, 
    # it doesn't need to be installed
    export PATH=$HOME/Downloads/Pyrex-0.9.8.5:$PATH
    export PYTHONPATH=$HOME/Downloads/Pyrex-0.9.8.5:$PYTHONPATH

    cd $HOME/Downloads/Authorization-0.1

    # Solve "Use __cinit__ instead"
    perl -pi -e  's/__new__/__cinit__/g' ./src/Authorization.pxi

    # Solve "Reraise not inside except clause"
    perl -pi -e 's/raise /#raise /g' ./src/Authorization.pxi

    # Compile, but do not install
    python ./setup.py build_ext --inplace

    # Solve "cannot import name kAuthorizationFlagDestroyRights"
    perl -pi -e  's/, kAuthorizationFlagDestroyRights//g' ./test/test.py
    perl -pi -e  's/destroyflags=\(kAuthorizationFlagDestroyRights,\)//g' ./test/test.py

    # Test
    export PYTHONPATH=./lib/:$PYTHONPATH
    python test/test.py

    # should give:
    # I'm root!

# homepage
