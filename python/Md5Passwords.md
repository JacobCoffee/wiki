# Md5Passwords

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# MD5 Passwords 

It\'s *very* easy to create MD5 passwords with Python-

You just:

:::: 
::: 
``` 
   1 import hashlib
   2 
   3 key_string = raw_input( "Key to turn into an MD5 password? " )
   4 
   5 print hashlib.md5( key_string ).hexdigest()
```
:::
::::

ex: \"`robots`\" turns into \"`27f5e15b6af3223f1176293cd015771d`\"

The \"hexdigest\" form is the form you frequently find used in databases and in online forums. However, using MD5 for password storage is strongly discouraged. Please see the Security section for more information.

## Salting 

A good idea is to include a \'salt\' with the hash as well, which will prevent people using a dictionary with md5 hashes of common passwords. When you check a password, just add the salt to the front of the password and hash it. The salt can be any random string.

Something like this:

:::: 
::: 
``` 
   1 import hashlib
   2 
   3 key_string = "SecretPassword"
   4 salt = "1Ha7"
   5 
   6 hash = hashlib.md5( salt + key_string ).hexdigest()
   7 print "%s:%s" % (salt, hash) # Store these
```
:::
::::

[AnthonyBriggs](./AnthonyBriggs.html)

## Security 

Use caution when utilizing hashes for passwords. MD5 is no longer considered safe for password storage. Consider instead [scrypt](https://pypi.python.org/pypi/scrypt/), [bcrypt](https://pypi.python.org/pypi/bcrypt/), or [PBDKF2](https://docs.python.org/3/library/hashlib.html#hashlib.pbkdf2_hmac) utilizing 100,000 rounds or more.

Reference: [https://gist.github.com/tqbf/be58d2d39690c3b366ad](https://gist.github.com/tqbf/be58d2d39690c3b366ad)

## See Also 

- [an on-line MD5 generator](http://bfl.rctek.com/tools/?tool=hasher) - create MD5 values from keys, online

# Discussion 
