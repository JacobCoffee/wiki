# Asking for Help/Why don't my list and generator comprehensions work?

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# Asking for Help: Why don\'t my list and generator comprehensions work? 

[lwickjr](lwickjr): \[2008-Jul-09\]

    Python 2.5.2 (r252:60911, Feb 21 2008, 13:11:45) [MSC v.1310 32 bit (Intel)] on win32
    Type "copyright", "credits" or "license()" for more information.

        ****************************************************************
        Personal firewall software may warn about the connection IDLE
        makes to its subprocess using this computer's internal loopback
        interface.  This connection is not visible on any external
        interface and no data is sent to or received from the Internet.
        ****************************************************************

    IDLE 1.2.2      ==== No Subprocess ====
    >>> import os
    >>> dir()
    ['__builtins__', '__doc__', '__file__', '__name__', 'idlelib', 'os']
    >>> Source = ('all', 'F:\\Documents\\Pictures\\New\\06')
    >>> [[os.path.join(S, t) for t in os.listdir(S)] for S in Source[1:]]
    [['F:\\Documents\\Pictures\\New\\06\\Thumbs.db',
      'F:\\Documents\\Pictures\\New\\06\\style[1].css',
      'F:\\Documents\\Pictures\\New\\06\\index.html',
      'F:\\Documents\\Pictures\\New\\06\\desktop.ini']]
    >>> dir()
    ['S', 'Source', '__builtins__', '__doc__', '__file__', '__name__', 'idlelib', 'os', 't']
    >>> del S, t
    >>> [(os.path.join(S, t) for t in os.listdir(S)) for S in Source[1:]]
    [<generator object at 0x010B5AA8>]
    >>> dir()
    ['S', 'Source', '__builtins__', '__doc__', '__file__', '__name__', 'idlelib', 'os']
    >>> del S
    >>> dir()
    ['Source', '__builtins__', '__doc__', '__file__', '__name__', 'idlelib', 'os']
    >>> [os.path.join(S, t) for t in os.listdir(S) for S in Source[1:]]
    Traceback (most recent call last):
      File "<pyshell#10>", line 1, in <module>
        [os.path.join(S, t) for t in os.listdir(S) for S in Source[1:]]
    NameError: name 'S' is not defined
    >>> 

The first example generates nested lists, one sublist per directory in Source.

The second example generates a list of generator objects, one per directory in Source.

The third example generates an undefined variable error.

What is wrong with the third example? If I pre-define `S = Source[1]`, it works correctly, generating a flat list, while if I predefine S equal to something else, it uses that value in violation of the semantics of list comprehensions as I understand them. Is something wrong with my list comprehension, with Python 2.5.2 itself, or with my understanding of the relavent semantics?

My answer: In case someone reads this, the third example has got \"for\" loops in the wrong order. The first for loop runs first, and therefore it should be written as `[os.path.join(S, t) for S in Source[1:] for t in os.listdir(S)].`

Answer from [PaulBoddie](PaulBoddie):

- In the second example, you get generator objects because that is what a generator comprehension produces, and these generators must then be \"materialised\" (or consumed by something like `list`{.backtick} in order to get a list of objects).

- In the third example, you have to remember that the loops read from left to right, starting with the outermost loop and ending at the innermost. The way to think about this is to move the expression from the beginning to the end and then write the loops out as you normally would:

  :::: 
  ::: 
  ``` 
     1  os.path.join(S, t) for t in os.listdir(S) for S in Source[1:]
     2 
     3  # becomes...
     4  for t in os.listdir(S) for S in Source[1:] ... os.path.join(S, t)
     5 
     6  # then...
     7  for t in os.listdir(S):
     8      for S in Source[1:] ... os.path.join(S, t)
     9 
    10  # and finally...
    11  for t in os.listdir(S):
    12      for S in Source[1:]:
    13          ... os.path.join(S, t)
  ```
  :::
  ::::

  Here, `...`{.backtick} refers to the operation which yields the results of the comprehension. Now, it should be obvious why `S`{.backtick} is not defined.

------------------------------------------------------------------------

[CategoryAskingForHelp](CategoryAskingForHelp) [CategoryAskingForHelpAnswered](CategoryAskingForHelpAnswered)
