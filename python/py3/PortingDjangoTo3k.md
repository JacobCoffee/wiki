# PortingDjangoTo3k

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

I started porting Django to Python 3 at [PyCon2008](PyCon2008). The current patch allows me to get through the tutorial, but there are certainly large parts of the code base that I haven\'t touched, so more issues are likely to show up.

The current version of the patch is available on [http://bitbucket.org/loewis/django-3k/](http://bitbucket.org/loewis/django-3k/)

Note: an update of the port, which features a single codebase for 2.x and 3.x, and which passes the regression tests on Python 2.5, 2.6, 2.7 and 3.2, is available at [https://bitbucket.org/vinay.sajip/django/](https://bitbucket.org/vinay.sajip/django/) (default branch).

For general tips on porting to Python 3, see [PortingPythonToPy3k](PortingPythonToPy3k) (ideally, much of the non-Django-specific information from the porting Django page should be included on the general porting page).

# Porting Strategy 

This port attempts to maintain compatibility with older Python versions from a single code base; the goal is to support all versions that Django supports, plus 3.1.

To simplify porting, and to allow running Django from a single code base, I changed distutils to allow invocation of the 2to3 tool as part of the build_py step, if setup.py is invoked from python3.0. To add that support, I first made 2to3 a standard library (named lib2to3).

This approach mostly works, and has the following flaws:

- conversion is rather slow (takes 6min on my machine)

# Changes 

The changes can be roughly grouped into the following categories

## Naming Changes 

A number of modules that django uses have been removed, or renamed:

- all modules in the email package got renamed to lower-case. I haven\'t actually tested whether any of the email functionality in Django still works (I don\'t even know what that functionality could be).

- in gettext, the u\* methods have disappeared.

- cStringIO is no longer; Django should use io.BytesIO instead.

- the .next method of iterators got renamed to `__next__`{.backtick}. A builtin `next()`{.backtick} was added, but is not available in 2.x; I added an emulation of it in the py3 utility module.

In addition, a few functions and attributes got renamed:

- to test whether something is a function, don\'t look at `func_code`{.backtick} anymore; use `__code__`{.backtick} instead.

## Bytes vs. Strings 

Python 3 separates byte strings and character strings clearly, and defines that string literals are character strings, unless prefixed as bytes. Character strings are always represented as sequence of Unicode characters.

2to3 will change all occurrences of the unicode identifier to str, but leave all occurrences of str alone. It will also change all Unicode string literals to regular string literals, but leave the existing string literals alone.

As a consequence, it produces code like this one:

      class EscapeString(str, EscapeData): pass
      class EscapeUnicode(str, EscapeDate): pass

These types were meant to be separate, but became identical after 2to3.

To fix these problems, I made the following changes:

- introduce django.utils.py3.bytes, which is the bytes type in 3.x, but an alias for str in 2.x. Use that in all places where str is used as a type.

- introduce django.utils.py3.b, which is a function that converts its argument to an ASCII-encoded byte string. In 2.x, it is another alias for str; in 3.x, it leaves byte strings alone, and encodes regular (unicode) strings as ASCII. This function is used in all places where string literals are meant as bytes, plus all cases where str() was used to invoke the default conversion of 2.x.

- Django encourages users to define `__unicode__`{.backtick} methods in models; 2to3 leaves them alone. Rather than changing them to str, I kept the Django approach of calling them explicitly. In some cases, they were called implicitly (through unicode()); these calls had to be converted.

- md5.hexdigest returns a (unicode) string in 3.x; Django assumes the digest is a byte sequence.

- When Django reads a file, it typically uses the pattern

  - ` open(name).read().decode(encoding)... `

  This breaks, as .read() now returns a (unicode) string, which is already decoded. This can be fixed by adding `'rb'` as a parameter to open().

- Django builds keyword dictionaries to be passed as \*\* arguments into functions, and puts str() objects into them. As now all str() objects consistently become byte strings, calling the function fails. 3.x will require Unicode strings here. However, using Unicode strings would break on 2.x, so this gets special-cased based on sys.version_info.

- urllib.quote currently doesn\'t work on bytes; I think it should. To work around, I convert the argument into a Unicode string.

## New-style classes 

- Django uses types.[ClassType](./ClassType.html) to create new classes at run-time. Change that to use type in 3.x, through a test for sys.version_info.

- Django defines a [metaclass] [ModelBase](./ModelBase.html), and uses it in Model. As the syntax for metaclass declarations has changed, I needed to change the code; this should be done by 2to3, though (#2366)

- Django relies on clearing the dictionary of the class called Meta in a Model. This a) doesn\'t work anymore, as the dictionary proxy is immutable,

  and b) leaves over a number of attributes in the class that are new in 3.x (`__weakref__`{.backtick} and `__dict__`{.backtick}). I copy the dict, then clear it. I don\'t understand why it is important to clear the dict, other than checking that all attributes have been processed completely, so I hope this change is correct.

- [cmp] cannot be used anymore for comparison; classes need to implement [lt], etc.

## Other changes 

- the hex codec does not exist anymore, use binhex.unhexlify

- list.sort doesn\'t support the sort function anymore. In the specific case, rewriting it to use a key= function was straight-forward.

- In [AdminLogNode](./AdminLogNode.html), limit shows up as a string, not as an int, and slice() will complain. I\'m not sure why that works in 2.x.

# Open Issues 

- I have worked with sqlite3 and psycopg2 only; all the other databases have not been tested.

- The manage module has an \"import settings\", this gets fixed to \"from . import settings\" by 2to3. When manage.py is then run as the main script, Python complains that the relative import is incorrect. However, that \*would\* be correct if the script is imported as \<site\>.manage

- checks for `im_func`{.backtick} need to be replaced with checks for `__func__`{.backtick}.

- \... (many more things; this just barely works)

#### Tags 

Python 3k. Python 3.0. Python 3000. Py3K. Django.
