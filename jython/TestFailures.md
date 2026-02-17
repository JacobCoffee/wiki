# TestFailures

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# Failing tests on the 2.3 branch 

## Ones with reasons 

test_binascii: exceptions are strings, not classes, so issubclass() raises an exception; a2b_qp not implemented; a2b_uu has a logic error that makes it fail on the UUencoding of an empty string.

test_StringIO: root cause: *.join(\[unicode, str\]) returns str, should be unicode*

test_dumbdbm: with very large strings, the value retrieved is incorrect.

test_format: \'%d\' % \'1\' works, should raise a [TypeError](./TypeError.html).

test_fileinput: patch in SF.
