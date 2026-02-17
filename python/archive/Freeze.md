# Freeze

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# Freeze 

Freeze is a \"[pure Python](./pure(20)Python.html)\" utility that ships with Python. You can use Freeze to compile executables for Unix systems.

If you want to write Python, but you don\'t know if your clients have Python installed, use this!

## How to Use 

Create a Python program, \"hello.py\"

:::: 
::: 
``` 
   1 print "Hello, World!"
```
:::
::::

Then find `freeze.py` on your system, and invoke it in a directory that you don\'t mind filling up with `.c` files:

    $ python freeze.py hello.py

With Debian, for example, **dpkg -S freeze.py** yields a current package name, which is, as of the time of writing this, **python2.4-examples**.

On my system, at least, the output is this:

      Name                      File
      ----                      ----
    m BaseHTTPServer            /usr/lib/python2.3/BaseHTTPServer.py
    m FixTk                     /usr/lib/python2.3/lib-tk/FixTk.py
    m SocketServer              /usr/lib/python2.3/SocketServer.py
    m StringIO                  /usr/lib/python2.3/StringIO.py
    m Tkconstants               /usr/lib/python2.3/lib-tk/Tkconstants.py
    m Tkinter                   /usr/lib/python2.3/lib-tk/Tkinter.py
    m UserDict                  /usr/lib/python2.3/UserDict.py
    m __builtin__
    m __main__                  hello.py
    m _codecs
    m _locale                   /usr/lib/python2.3/lib-dynload/_locale.so
    m _random                   /usr/lib/python2.3/lib-dynload/_random.so
    m _socket                   /usr/lib/python2.3/lib-dynload/_socket.so
    m _sre
    m _ssl                      /usr/lib/python2.3/lib-dynload/_ssl.so
    m _tkinter                  /usr/lib/python2.3/lib-dynload/_tkinter.so
    m array                     /usr/lib/python2.3/lib-dynload/array.so
    m atexit                    /usr/lib/python2.3/atexit.py
    m base64                    /usr/lib/python2.3/base64.py
    m binascii                  /usr/lib/python2.3/lib-dynload/binascii.so
    m cStringIO                 /usr/lib/python2.3/lib-dynload/cStringIO.so
    m codecs                    /usr/lib/python2.3/codecs.py
    m copy                      /usr/lib/python2.3/copy.py
    m copy_reg                  /usr/lib/python2.3/copy_reg.py
    m dis                       /usr/lib/python2.3/dis.py
    P distutils                 /usr/lib/python2.3/distutils/__init__.py
    m distutils.dep_util        /usr/lib/python2.3/distutils/dep_util.py
    m distutils.errors          /usr/lib/python2.3/distutils/errors.py
    m distutils.log             /usr/lib/python2.3/distutils/log.py
    m distutils.spawn           /usr/lib/python2.3/distutils/spawn.py
    m distutils.util            /usr/lib/python2.3/distutils/util.py
    m dummy_thread              /usr/lib/python2.3/dummy_thread.py
    P encodings                 /usr/lib/python2.3/encodings/__init__.py
    m encodings.aliases         /usr/lib/python2.3/encodings/aliases.py
    m errno
    m exceptions
    m fcntl                     /usr/lib/python2.3/lib-dynload/fcntl.so
    m fnmatch                   /usr/lib/python2.3/fnmatch.py
    m formatter                 /usr/lib/python2.3/formatter.py
    m ftplib                    /usr/lib/python2.3/ftplib.py
    m getopt                    /usr/lib/python2.3/getopt.py
    m getpass                   /usr/lib/python2.3/getpass.py
    m glob                      /usr/lib/python2.3/glob.py
    m gopherlib                 /usr/lib/python2.3/gopherlib.py
    m htmlentitydefs            /usr/lib/python2.3/htmlentitydefs.py
    m htmllib                   /usr/lib/python2.3/htmllib.py
    m httplib                   /usr/lib/python2.3/httplib.py
    m imp
    m inspect                   /usr/lib/python2.3/inspect.py
    m linecache                 /usr/lib/python2.3/linecache.py
    m locale                    /usr/lib/python2.3/locale.py
    m macpath                   /usr/lib/python2.3/macpath.py
    m macurl2path               /usr/lib/python2.3/macurl2path.py
    m markupbase                /usr/lib/python2.3/markupbase.py
    m marshal
    m math                      /usr/lib/python2.3/lib-dynload/math.so
    m mimetools                 /usr/lib/python2.3/mimetools.py
    m mimetypes                 /usr/lib/python2.3/mimetypes.py
    m ntpath                    /usr/lib/python2.3/ntpath.py
    m nturl2path                /usr/lib/python2.3/nturl2path.py
    m opcode                    /usr/lib/python2.3/opcode.py
    m os                        /usr/lib/python2.3/os.py
    m os2emxpath                /usr/lib/python2.3/os2emxpath.py
    m popen2                    /usr/lib/python2.3/popen2.py
    m posix
    m posixpath                 /usr/lib/python2.3/posixpath.py
    m pwd                       /usr/lib/python2.3/lib-dynload/pwd.so
    m py_compile                /usr/lib/python2.3/py_compile.py
    m pydoc                     /usr/lib/python2.3/pydoc.py
    m quopri                    /usr/lib/python2.3/quopri.py
    m random                    /usr/lib/python2.3/random.py
    m re                        /usr/lib/python2.3/re.py
    m repr                      /usr/lib/python2.3/repr.py
    m rfc822                    /usr/lib/python2.3/rfc822.py
    m select                    /usr/lib/python2.3/lib-dynload/select.so
    m sgmllib                   /usr/lib/python2.3/sgmllib.py
    m site                      /usr/lib/python2.3/site.py
    m socket                    /usr/lib/python2.3/socket.py
    m sre                       /usr/lib/python2.3/sre.py
    m sre_compile               /usr/lib/python2.3/sre_compile.py
    m sre_constants             /usr/lib/python2.3/sre_constants.py
    m sre_parse                 /usr/lib/python2.3/sre_parse.py
    m stat                      /usr/lib/python2.3/stat.py
    m string                    /usr/lib/python2.3/string.py
    m strop                     /usr/lib/python2.3/lib-dynload/strop.so
    m sys
    m tempfile                  /usr/lib/python2.3/tempfile.py
    m termios                   /usr/lib/python2.3/lib-dynload/termios.so
    m thread
    m threading                 /usr/lib/python2.3/threading.py
    m time                      /usr/lib/python2.3/lib-dynload/time.so
    m token                     /usr/lib/python2.3/token.py
    m tokenize                  /usr/lib/python2.3/tokenize.py
    m traceback                 /usr/lib/python2.3/traceback.py
    m tty                       /usr/lib/python2.3/tty.py
    m types                     /usr/lib/python2.3/types.py
    m urllib                    /usr/lib/python2.3/urllib.py
    m urlparse                  /usr/lib/python2.3/urlparse.py
    m uu                        /usr/lib/python2.3/uu.py
    m warnings                  /usr/lib/python2.3/warnings.py
    m webbrowser                /usr/lib/python2.3/webbrowser.py

    Missing modules:
    ? Carbon.File imported from macpath
    ? Carbon.Folder imported from tempfile
    ? Carbon.Folders imported from tempfile
    ? EasyDialogs imported from getpass
    ? MacOS imported from Tkinter, py_compile
    ? SOCKS imported from ftplib
    ? _winreg imported from urllib
    ? ce imported from os
    ? ic imported from pydoc, urllib, webbrowser
    ? mac imported from os
    ? msvcrt imported from getpass
    ? nt imported from ntpath, os
    ? org.python.core imported from copy
    ? os.path imported from os
    ? os2 imported from os
    ? riscos imported from os
    ? riscosenviron imported from os
    ? riscospath imported from os
    ? rourl2path imported from urllib
    ? sitecustomize imported from site

    freezing BaseHTTPServer ...
    freezing FixTk ...
    freezing SocketServer ...
    freezing StringIO ...
    freezing Tkconstants ...
    freezing Tkinter ...
    freezing UserDict ...
    freezing __main__ ...
    freezing atexit ...
    freezing base64 ...
    freezing codecs ...
    freezing copy ...
    freezing copy_reg ...
    freezing dis ...
    freezing distutils ...
    freezing distutils.dep_util ...
    freezing distutils.errors ...
    freezing distutils.log ...
    freezing distutils.spawn ...
    freezing distutils.util ...
    freezing dummy_thread ...
    freezing encodings ...
    freezing encodings.aliases ...
    freezing fnmatch ...
    freezing formatter ...
    freezing ftplib ...
    freezing getopt ...
    freezing getpass ...
    freezing glob ...
    freezing gopherlib ...
    freezing htmlentitydefs ...
    freezing htmllib ...
    freezing httplib ...
    freezing inspect ...
    freezing linecache ...
    freezing locale ...
    freezing macpath ...
    freezing macurl2path ...
    freezing markupbase ...
    freezing mimetools ...
    freezing mimetypes ...
    freezing ntpath ...
    freezing nturl2path ...
    freezing opcode ...
    freezing os ...
    freezing os2emxpath ...
    freezing popen2 ...
    freezing posixpath ...
    freezing py_compile ...
    freezing pydoc ...
    freezing quopri ...
    freezing random ...
    freezing re ...
    freezing repr ...
    freezing rfc822 ...
    freezing sgmllib ...
    freezing site ...
    freezing socket ...
    freezing sre ...
    freezing sre_compile ...
    freezing sre_constants ...
    freezing sre_parse ...
    freezing stat ...
    freezing string ...
    freezing tempfile ...
    freezing threading ...
    freezing token ...
    freezing tokenize ...
    freezing traceback ...
    freezing tty ...
    freezing types ...
    freezing urllib ...
    freezing urlparse ...
    freezing uu ...
    freezing warnings ...
    freezing webbrowser ...
    generating table of frozen modules
    Warning: unknown modules remain: _locale _random _socket _ssl _tkinter array binascii cStringIO fcntl math pwd select strop termios time
    Now run "make" to build the target: hello

As you can see, even a simple Python program will require several dozen modules because these are necessary simply for Python itself to start --- yes, Python uses its own Standard Library to help run the language!

Next, run make:

    $ make
    gcc -pthread -DNDEBUG -g -O3 -Wall -Wstrict-prototypes -I/usr/include/python2.3
    -I/usr/include/python2.3 -c config.c
    gcc -pthread -DNDEBUG -g -O3 -Wall -Wstrict-prototypes -I/usr/include/python2.3
    -I/usr/include/python2.3 -c frozen.c
    gcc -pthread -DNDEBUG -g -O3 -Wall -Wstrict-prototypes -I/usr/include/python2.3
    -I/usr/include/python2.3 -c M_BaseHTTPServer.c
    gcc -pthread -DNDEBUG -g -O3 -Wall -Wstrict-prototypes -I/usr/include/python2.3
    -I/usr/include/python2.3 -c M_FixTk.c
    gcc -pthread -DNDEBUG -g -O3 -Wall -Wstrict-prototypes -I/usr/include/python2.3
    -I/usr/include/python2.3 -c M_SocketServer.c
    gcc -pthread -DNDEBUG -g -O3 -Wall -Wstrict-prototypes -I/usr/include/python2.3
    -I/usr/include/python2.3 -c M_StringIO.c
    gcc -pthread -DNDEBUG -g -O3 -Wall -Wstrict-prototypes -I/usr/include/python2.3
    -I/usr/include/python2.3 -c M_Tkconstants.c
    gcc -pthread -DNDEBUG -g -O3 -Wall -Wstrict-prototypes -I/usr/include/python2.3
    -I/usr/include/python2.3 -c M_Tkinter.c
    gcc -pthread -DNDEBUG -g -O3 -Wall -Wstrict-prototypes -I/usr/include/python2.3
    -I/usr/include/python2.3 -c M_UserDict.c
    gcc -pthread -DNDEBUG -g -O3 -Wall -Wstrict-prototypes -I/usr/include/python2.3
    -I/usr/include/python2.3 -c M___main__.c
    gcc -pthread -DNDEBUG -g -O3 -Wall -Wstrict-prototypes -I/usr/include/python2.3
    -I/usr/include/python2.3 -c M_atexit.c
    gcc -pthread -DNDEBUG -g -O3 -Wall -Wstrict-prototypes -I/usr/include/python2.3
    -I/usr/include/python2.3 -c M_base64.c
    gcc -pthread -DNDEBUG -g -O3 -Wall -Wstrict-prototypes -I/usr/include/python2.3
    -I/usr/include/python2.3 -c M_codecs.c
    gcc -pthread -DNDEBUG -g -O3 -Wall -Wstrict-prototypes -I/usr/include/python2.3
    -I/usr/include/python2.3 -c M_copy.c
    gcc -pthread -DNDEBUG -g -O3 -Wall -Wstrict-prototypes -I/usr/include/python2.3
    -I/usr/include/python2.3 -c M_copy_reg.c
    gcc -pthread -DNDEBUG -g -O3 -Wall -Wstrict-prototypes -I/usr/include/python2.3
    -I/usr/include/python2.3 -c M_dis.c
    gcc -pthread -DNDEBUG -g -O3 -Wall -Wstrict-prototypes -I/usr/include/python2.3
    -I/usr/include/python2.3 -c M_distutils.c
    gcc -pthread -DNDEBUG -g -O3 -Wall -Wstrict-prototypes -I/usr/include/python2.3
    -I/usr/include/python2.3 -c M_distutils__dep_util.c
    gcc -pthread -DNDEBUG -g -O3 -Wall -Wstrict-prototypes -I/usr/include/python2.3
    -I/usr/include/python2.3 -c M_distutils__errors.c
    gcc -pthread -DNDEBUG -g -O3 -Wall -Wstrict-prototypes -I/usr/include/python2.3
    -I/usr/include/python2.3 -c M_distutils__log.c
    gcc -pthread -DNDEBUG -g -O3 -Wall -Wstrict-prototypes -I/usr/include/python2.3
    -I/usr/include/python2.3 -c M_distutils__spawn.c
    gcc -pthread -DNDEBUG -g -O3 -Wall -Wstrict-prototypes -I/usr/include/python2.3
    -I/usr/include/python2.3 -c M_distutils__util.c
    gcc -pthread -DNDEBUG -g -O3 -Wall -Wstrict-prototypes -I/usr/include/python2.3
    -I/usr/include/python2.3 -c M_dummy_thread.c
    gcc -pthread -DNDEBUG -g -O3 -Wall -Wstrict-prototypes -I/usr/include/python2.3
    -I/usr/include/python2.3 -c M_encodings.c
    gcc -pthread -DNDEBUG -g -O3 -Wall -Wstrict-prototypes -I/usr/include/python2.3
    -I/usr/include/python2.3 -c M_encodings__aliases.c
    gcc -pthread -DNDEBUG -g -O3 -Wall -Wstrict-prototypes -I/usr/include/python2.3
    -I/usr/include/python2.3 -c M_fnmatch.c
    gcc -pthread -DNDEBUG -g -O3 -Wall -Wstrict-prototypes -I/usr/include/python2.3
    -I/usr/include/python2.3 -c M_formatter.c
    gcc -pthread -DNDEBUG -g -O3 -Wall -Wstrict-prototypes -I/usr/include/python2.3
    -I/usr/include/python2.3 -c M_ftplib.c
    gcc -pthread -DNDEBUG -g -O3 -Wall -Wstrict-prototypes -I/usr/include/python2.3
    -I/usr/include/python2.3 -c M_getopt.c
    gcc -pthread -DNDEBUG -g -O3 -Wall -Wstrict-prototypes -I/usr/include/python2.3
    -I/usr/include/python2.3 -c M_getpass.c
    gcc -pthread -DNDEBUG -g -O3 -Wall -Wstrict-prototypes -I/usr/include/python2.3
    -I/usr/include/python2.3 -c M_glob.c
    gcc -pthread -DNDEBUG -g -O3 -Wall -Wstrict-prototypes -I/usr/include/python2.3
    -I/usr/include/python2.3 -c M_gopherlib.c
    gcc -pthread -DNDEBUG -g -O3 -Wall -Wstrict-prototypes -I/usr/include/python2.3
    -I/usr/include/python2.3 -c M_htmlentitydefs.c
    gcc -pthread -DNDEBUG -g -O3 -Wall -Wstrict-prototypes -I/usr/include/python2.3
    -I/usr/include/python2.3 -c M_htmllib.c
    gcc -pthread -DNDEBUG -g -O3 -Wall -Wstrict-prototypes -I/usr/include/python2.3
    -I/usr/include/python2.3 -c M_httplib.c
    gcc -pthread -DNDEBUG -g -O3 -Wall -Wstrict-prototypes -I/usr/include/python2.3
    -I/usr/include/python2.3 -c M_inspect.c
    gcc -pthread -DNDEBUG -g -O3 -Wall -Wstrict-prototypes -I/usr/include/python2.3
    -I/usr/include/python2.3 -c M_linecache.c
    gcc -pthread -DNDEBUG -g -O3 -Wall -Wstrict-prototypes -I/usr/include/python2.3
    -I/usr/include/python2.3 -c M_locale.c
    gcc -pthread -DNDEBUG -g -O3 -Wall -Wstrict-prototypes -I/usr/include/python2.3
    -I/usr/include/python2.3 -c M_macpath.c
    gcc -pthread -DNDEBUG -g -O3 -Wall -Wstrict-prototypes -I/usr/include/python2.3
    -I/usr/include/python2.3 -c M_macurl2path.c
    gcc -pthread -DNDEBUG -g -O3 -Wall -Wstrict-prototypes -I/usr/include/python2.3
    -I/usr/include/python2.3 -c M_markupbase.c
    gcc -pthread -DNDEBUG -g -O3 -Wall -Wstrict-prototypes -I/usr/include/python2.3
    -I/usr/include/python2.3 -c M_mimetools.c
    gcc -pthread -DNDEBUG -g -O3 -Wall -Wstrict-prototypes -I/usr/include/python2.3
    -I/usr/include/python2.3 -c M_mimetypes.c
    gcc -pthread -DNDEBUG -g -O3 -Wall -Wstrict-prototypes -I/usr/include/python2.3
    -I/usr/include/python2.3 -c M_ntpath.c
    gcc -pthread -DNDEBUG -g -O3 -Wall -Wstrict-prototypes -I/usr/include/python2.3
    -I/usr/include/python2.3 -c M_nturl2path.c
    gcc -pthread -DNDEBUG -g -O3 -Wall -Wstrict-prototypes -I/usr/include/python2.3
    -I/usr/include/python2.3 -c M_opcode.c
    gcc -pthread -DNDEBUG -g -O3 -Wall -Wstrict-prototypes -I/usr/include/python2.3
    -I/usr/include/python2.3 -c M_os.c
    gcc -pthread -DNDEBUG -g -O3 -Wall -Wstrict-prototypes -I/usr/include/python2.3
    -I/usr/include/python2.3 -c M_os2emxpath.c
    gcc -pthread -DNDEBUG -g -O3 -Wall -Wstrict-prototypes -I/usr/include/python2.3
    -I/usr/include/python2.3 -c M_popen2.c
    gcc -pthread -DNDEBUG -g -O3 -Wall -Wstrict-prototypes -I/usr/include/python2.3
    -I/usr/include/python2.3 -c M_posixpath.c
    gcc -pthread -DNDEBUG -g -O3 -Wall -Wstrict-prototypes -I/usr/include/python2.3
    -I/usr/include/python2.3 -c M_py_compile.c
    gcc -pthread -DNDEBUG -g -O3 -Wall -Wstrict-prototypes -I/usr/include/python2.3
    -I/usr/include/python2.3 -c M_pydoc.c
    gcc -pthread -DNDEBUG -g -O3 -Wall -Wstrict-prototypes -I/usr/include/python2.3
    -I/usr/include/python2.3 -c M_quopri.c
    gcc -pthread -DNDEBUG -g -O3 -Wall -Wstrict-prototypes -I/usr/include/python2.3
    -I/usr/include/python2.3 -c M_random.c
    gcc -pthread -DNDEBUG -g -O3 -Wall -Wstrict-prototypes -I/usr/include/python2.3
    -I/usr/include/python2.3 -c M_re.c
    gcc -pthread -DNDEBUG -g -O3 -Wall -Wstrict-prototypes -I/usr/include/python2.3
    -I/usr/include/python2.3 -c M_repr.c
    gcc -pthread -DNDEBUG -g -O3 -Wall -Wstrict-prototypes -I/usr/include/python2.3
    -I/usr/include/python2.3 -c M_rfc822.c
    gcc -pthread -DNDEBUG -g -O3 -Wall -Wstrict-prototypes -I/usr/include/python2.3
    -I/usr/include/python2.3 -c M_sgmllib.c
    gcc -pthread -DNDEBUG -g -O3 -Wall -Wstrict-prototypes -I/usr/include/python2.3
    -I/usr/include/python2.3 -c M_site.c
    gcc -pthread -DNDEBUG -g -O3 -Wall -Wstrict-prototypes -I/usr/include/python2.3
    -I/usr/include/python2.3 -c M_socket.c
    gcc -pthread -DNDEBUG -g -O3 -Wall -Wstrict-prototypes -I/usr/include/python2.3
    -I/usr/include/python2.3 -c M_sre.c
    gcc -pthread -DNDEBUG -g -O3 -Wall -Wstrict-prototypes -I/usr/include/python2.3
    -I/usr/include/python2.3 -c M_sre_compile.c
    gcc -pthread -DNDEBUG -g -O3 -Wall -Wstrict-prototypes -I/usr/include/python2.3
    -I/usr/include/python2.3 -c M_sre_constants.c
    gcc -pthread -DNDEBUG -g -O3 -Wall -Wstrict-prototypes -I/usr/include/python2.3
    -I/usr/include/python2.3 -c M_sre_parse.c
    gcc -pthread -DNDEBUG -g -O3 -Wall -Wstrict-prototypes -I/usr/include/python2.3
    -I/usr/include/python2.3 -c M_stat.c
    gcc -pthread -DNDEBUG -g -O3 -Wall -Wstrict-prototypes -I/usr/include/python2.3
    -I/usr/include/python2.3 -c M_string.c
    gcc -pthread -DNDEBUG -g -O3 -Wall -Wstrict-prototypes -I/usr/include/python2.3
    -I/usr/include/python2.3 -c M_tempfile.c
    gcc -pthread -DNDEBUG -g -O3 -Wall -Wstrict-prototypes -I/usr/include/python2.3
    -I/usr/include/python2.3 -c M_threading.c
    gcc -pthread -DNDEBUG -g -O3 -Wall -Wstrict-prototypes -I/usr/include/python2.3
    -I/usr/include/python2.3 -c M_token.c
    gcc -pthread -DNDEBUG -g -O3 -Wall -Wstrict-prototypes -I/usr/include/python2.3
    -I/usr/include/python2.3 -c M_tokenize.c
    gcc -pthread -DNDEBUG -g -O3 -Wall -Wstrict-prototypes -I/usr/include/python2.3
    -I/usr/include/python2.3 -c M_traceback.c
    gcc -pthread -DNDEBUG -g -O3 -Wall -Wstrict-prototypes -I/usr/include/python2.3
    -I/usr/include/python2.3 -c M_tty.c
    gcc -pthread -DNDEBUG -g -O3 -Wall -Wstrict-prototypes -I/usr/include/python2.3
    -I/usr/include/python2.3 -c M_types.c
    gcc -pthread -DNDEBUG -g -O3 -Wall -Wstrict-prototypes -I/usr/include/python2.3
    -I/usr/include/python2.3 -c M_urllib.c
    gcc -pthread -DNDEBUG -g -O3 -Wall -Wstrict-prototypes -I/usr/include/python2.3
    -I/usr/include/python2.3 -c M_urlparse.c
    gcc -pthread -DNDEBUG -g -O3 -Wall -Wstrict-prototypes -I/usr/include/python2.3
    -I/usr/include/python2.3 -c M_uu.c
    gcc -pthread -DNDEBUG -g -O3 -Wall -Wstrict-prototypes -I/usr/include/python2.3
    -I/usr/include/python2.3 -c M_warnings.c
    gcc -pthread -DNDEBUG -g -O3 -Wall -Wstrict-prototypes -I/usr/include/python2.3
    -I/usr/include/python2.3 -c M_webbrowser.c
    c++ -pthread  -Xlinker -export-dynamic config.o frozen.o M_BaseHTTPServer.o M_FixTk.o M_SocketServer.o M_StringIO.o M_Tkconstants.o M_Tkinter.o M_UserDict.o M___main__.o M_atexit.o M_base64.o M_codecs.o M_copy.o M_copy_reg.o M_dis.o M_distutils.o M_distutils__dep_util.o M_distutils__errors.o M_distutils__log.o M_distutils__spawn.o M_distutils__util.o M_dummy_thread.o M_encodings.o M_encodings__aliases.o M_fnmatch.o M_formatter.o M_ftplib.o M_getopt.o M_getpass.o M_glob.o M_gopherlib.o M_htmlentitydefs.o M_htmllib.o M_httplib.o M_inspect.o M_linecache.o M_locale.o M_macpath.o M_macurl2path.o M_markupbase.o M_mimetools.o M_mimetypes.o M_ntpath.o M_nturl2path.o M_opcode.o M_os.o M_os2emxpath.o M_popen2.o M_posixpath.o M_py_compile.o M_pydoc.o M_quopri.o M_random.o M_re.o M_repr.o M_rfc822.o M_sgmllib.o M_site.o M_socket.o M_sre.o M_sre_compile.o M_sre_constants.o M_sre_parse.o M_stat.o M_string.o M_tempfile.o M_threading.o M_token.o M_tokenize.o M_traceback.o M_tty.o M_types.o M_urllib.o M_urlparse.o M_uu.o M_warnings.o M_webbrowser.o /usr/lib/python2.3/config/libpython2.3.a   -lpthread -ldl  -lutil -lm  -o hello
    /usr/lib/python2.3/config/libpython2.3.a(posixmodule.o)(.text+0x3908): In function `posix_tmpnam':
    : the use of `tmpnam_r' is dangerous, better use `mkstemp'
    /usr/lib/python2.3/config/libpython2.3.a(posixmodule.o)(.text+0x387a): In function `posix_tempnam':
    : the use of `tempnam' is dangerous, better use `mkstemp'

\...and you should end up with the executable, `hello`!

    $ ./hello
    Hello, world!

ta da!

## See Also 

- [Py2Exe](Py2Exe) \-- like Freeze, but makes Windows executables

- [PythonInstalledByDefault](PythonInstalledByDefault) \-- OS/desktop distributions that come with Python installed

- README \-- the README file for the \"freeze\" utility that comes with Python

# Discussion 

I may be doing something wrong; I don\'t think it should be including just about every module under the sun.

\-- [LionKimbro](LionKimbro) 2004-08-30 04:06:38

The \"problem\" is pydoc. It includes Tkinter and some internet related modules for its gui. Just excluding pydoc with

    python freeze.py -X pydoc hello.py

reduces the list of frozen modules for me to this:

    freezing UserDict ...
    freezing __main__ ...
    freezing codecs ...
    freezing copy ...
    freezing copy_reg ...
    freezing distutils ...
    freezing distutils.dep_util ...
    freezing distutils.errors ...
    freezing distutils.log ...
    freezing distutils.spawn ...
    freezing distutils.util ...
    freezing dummy_thread ...
    freezing encodings ...
    freezing encodings.aliases ...
    freezing linecache ...
    freezing locale ...
    freezing macpath ...
    freezing ntpath ...
    freezing os ...
    freezing os2emxpath ...
    freezing popen2 ...
    freezing posixpath ...
    freezing py_compile ...
    freezing random ...
    freezing re ...
    freezing repr ...
    freezing site ...
    freezing sre ...
    freezing sre_compile ...
    freezing sre_constants ...
    freezing sre_parse ...
    freezing stat ...
    freezing string ...
    freezing tempfile ...
    freezing traceback ...
    freezing types ...
    freezing warnings ...
    generating table of frozen modules
    Warning: unknown modules remain: _locale _random array binascii fcntl itertools math pwd strop time

The minimal set of excludes which produces a still working executable, while excluding everything unnecessary is:

    python freeze.py -X codecs -X copy -X distutils -X encodings -X locale -X macpath -X ntpath -X os2emxpath -X popen2 -X pydoc -X re -X warnings hello.py

The resulting list is

    freezing UserDict ...
    freezing __main__ ...
    freezing copy_reg ...
    freezing os ...
    freezing posixpath ...
    freezing site ...
    freezing stat ...
    freezing types ...
    generating table of frozen modules
    Warning: unknown modules remain: pwd

Quite a difference\... The sizes of the resulting binaries are:

::: {}
  -------------- ---------- -------------------
  **excluded**    **size**  **size stripped**
  nothing         6041313   2267304
  pydoc           5169213   1416840
  maximum         4666109   1076264
  -------------- ---------- -------------------
:::

\-- [MarcChr](MarcChr) 2005-02-03 16:42:03

I have errors trying to freeze a wxPython script:

    ricardo@yuggoth:~/Python$ ./hello2
    Traceback (most recent call last):
      File "hello2.py", line 1, in ?
        from wxPython.wx import *
      File "/usr/lib/python2.4/site-packages/wx-2.5.3-gtk2-unicode/wxPython/__init__.py", line 10, in ?
        import _wx
      File "/usr/lib/python2.4/site-packages/wx-2.5.3-gtk2-unicode/wxPython/_wx.py", line 3, in ?
        from _core import *
      File "/usr/lib/python2.4/site-packages/wx-2.5.3-gtk2-unicode/wxPython/_core.py", line 15, in ?
        import wx._core
      File "/usr/lib/python2.4/site-packages/wx-2.5.3-gtk2-unicode/wx/__init__.py", line 42, in ?
        from wx._core import *
      File "/usr/lib/python2.4/site-packages/wx-2.5.3-gtk2-unicode/wx/_core.py", line 4, in ?
        import _core_
    ImportError: No module named _core_

Anyone knows why?

freeze doesn\'t handle modules written in C/C++ like py2exe does - you have to manually copy all the .so files that you want to use into the LD_LIBRARY_PATH of the output program. However, I did this and now my application segfaults.

I \'m facing the simular problem what gives `"ImportError: No module named wxc"`. but when I put the right wxc.so in the app folder(No need freeze the program again), It just run ok. you can try it.

I tried this and I am still segfaulting - is there any solution to it?

\-\--

I tried using freeze, and got the following error: c++: /System/Library/Frameworks/Python.framework/Versions/2.3/lib/python2.3/config/libpython2.3.a: No such file or directory

Anyone know what\'s going on?

On MacOS, try using [py2app](./MacPython(2f)py2app.html), it does a nice job and works perfectly well for MacOS systems.

Try manually specifying your python source tree with -p?

------------------------------------------------------------------------

When I tried make after using freeze I get the error: powerpc-apple-darwin8-gcc-4.0.1: Python.framework/Versions/2.5/Python: No such file or directory i686-apple-darwin8-gcc-4.0.1: Python.framework/Versions/2.5/Python: No such file or directory lipo: can\'t figure out the architecture type of: /var/tmp//ccG5Z3m2.out

Thoughts for a newb?

------------------------------------------------------------------------

When I execute the makefile I get: `make: execvp: config.o: Permission denied`

I then changed the permission on the file to be executable and get the following error: `./config.o: ./config.o: cannot execute binary file`

The program is a simple print helloworld app. Any ideas?

You shouldn\'t have made it executable, instead try chown USERNAME config.o

------------------------------------------------------------------------

This doesn\'t seem to work right:

Two systems:

- A redhat9 system with python 2.5.2 compiled and installed.
- A normal Ubuntu 8.10 box.

<!-- -->

    redhat9: (echo "import os, sys, time" ; echo "print repr(time)") > test.py
    redhat9: python freeze/freeze.py test.py
    ...
    generating table of frozen modules
    Warning: unknown modules remain: _bisect _heapq _locale _random _socket _ssl _struct _tkinter array binascii cStringIO collections fcntl itertools math operator readline select strop termios time
    Now run "make" to build the target: test
    redhat9: make
    redhat9: scp test ubuntu8:/tmp/test
    ubuntu8: /tmp/test
    Traceback (most recent call last):
      File "test.py", line 2, in <module>
    ImportError: No module named time

It\'s as if the dynload libraries aren\'t frozen. ![:-(](/wiki/europython/img/sad.png ":-(")

\...

Reply to self: That \*is\* the case. The Warning is saying that those modules will not be in the binary! (Shouldn\'t that be an error?)

The fix is to rebuild it [using static modules](http://groups.google.com/group/comp.lang.python/browse_frm/thread/9407982ad24b62ec/5018f9abebaa285a?lnk=st&q=build+python+static&rnum=3&hl=en#5018f9abebaa285a). See `Modules/Setup` for docs. The short fix is to run this before you run `./configure` to build python:

    perl -pi -e 's!(^#\*shared\*)!*static*\n$1!' Modules/Setup.dist

------------------------------------------------------------------------

I got the following Error:

    Error: needed directory /usr/lib/python2.7/config not found
    Use ``/usr/share/doc/python2.7/examples/Tools/freeze/freeze.py -h'' for help

How can I fix it?

------------------------------------------------------------------------

You probably need to install the `python-dev`{.backtick} or `python-devel`{.backtick} package for your system. For example, on Debian the [python2.7-dev](http://packages.debian.org/wheezy/python2.7-dev) package provides the `/usr/lib/python2.7/config`{.backtick} directory (amongst [other things](http://packages.debian.org/wheezy/i386/python2.7-dev/filelist)), and will itself be installed if you install the `python-dev`{.backtick} package in this case. \-- [PaulBoddie](PaulBoddie) 2013-12-01 23:13:20
