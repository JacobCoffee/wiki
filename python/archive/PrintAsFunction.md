# PrintAsFunction

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

This page discusses the benefits of replacing the current `print`{.backtick} statement with an equivalent builtin. The `write`{.backtick} and `writeln`{.backtick} functions presented below do everything the `print`{.backtick} statement does without requiring any hacking of the grammar, and also make a number of things significantly easier.

Guido has made it clear he wants to get rid of the `print`{.backtick} statement in [Python3.0](../py3/Python3.0). This page considers why we would want to go that way, and how we can actually get there. It should be turned into a PEP eventually.

FYI: Python 3.0 has been released with a print function, and Python 2.6 has `from __future__ import print_function`{.backtick} to enable this on a per-module basis. Further discussion here is therefore quite futile. GvR.

### Benefits of using a function instead of a statement 

- Extended call syntax provides better interaction with sequences

- Keyword argument `sep`{.backtick} allows item separator to be changed easily and obviously

- Keyword argument `linesep`{.backtick} could optionally allow line separator to be changed easily and obviously

- Keyword argument `stream`{.backtick} allows easy and obvious redirection

- The builtin can be replaced for application wide customisation (e.g. per-thread logging)

- Interacts well with PEP 309\'s partial function application, and the rest of Python\'s ability to handle functions
  - *BDFL comments:*

    - don\'t waste your time on sequence printing
    - I\'m not excited about sep and linesep keyword args
    - add to benefits: easier transition to other function/method calls
    - if it were me, I\'d use \'to=\' or \'file=\' rather than \'stream=\' (too long)

### Guido\'s own arguments 

There is a theoretical argument: print is the only application-level functionality that has a statement dedicated to it. Within Python\'s world, syntax is generally used as a last resort, when something *can\'t* be done without help from the compiler. Print doesn\'t qualify for such an exception (quite the opposite actually).

But more important to me are my own experiences exploring the boundaries of print.

- I quite often come to a point in the evolution of a program where I need to change all print statements into logging calls, or calls into some other I/O or UI library. If print were a function, this would be a straightforward string replacement; as it is, finding where to add the parentheses is often a pain (the end isn\'t always on the same line

  as the start). It\'s even worse if there are already \"\>\>stream\" options present. Trailing commas also make this more complicated than it needs to be.

- Having special syntax puts up a much larger barrier for evolution of a feature. For examle, adding printf (or changing print to printf) is a much bigger deal now that print is a statement than if it had been a built-in function: trial implementations are much more work, there are only a few people who know how to modify Python\'s bytecode compiler, etc. (Having printf() be a function and print remain a statement is of course a possibility, but only adds more confusion and makes printf() a second-class citizen, thereby proving my point.)

- There is a distinct non-linearity in print\'s ease of use once you decide that you don\'t want to have spaces between items; you either have to switch to using sys.stdout.write(), or you have to collect all items in a string. This is not a simple transformation, consider what it takes to get rid of the spaces before the commas in this simple example:

  - `print "x =", x, ", y =", y, ", z =", z`

  If it was a built-in function, having a built-in companion function that did a similar thing without inserting spaces and adding a newline would be the logical thing to do (or adding keyword parameters to control that behavior; but I prefer a second function); but with only print as it currently stands, you\'d have to switch to something like

  - `print "x = " + str(x) + ", y = " + str(x) + ", z = " + str(z)`

  or

  - `print "x = %s, y = %s, z = %s" % (x, y, z)`

  neither of which is very attractive. (And don\'t tell me that the

  spaces are no big deal \-- they aren\'t in *this* example, but they are in other situations.)

- If it were a function, it would be much easier to replace it within

  one module (just `def print(*args):...`) or even throughout a program (e.g. by putting a different function in `__builtin__.print`). As it is, you can do this by writing a class with a write() method and assigning that to sys.stdout \-- that\'s not bad, but definitely a much larger conceptual leap, and it works at a different level than print.

Summarizing, my main problems with print as a statement are the transformations \-- when print doesn\'t cut it, you have to switch to something entirely different. If it were a function the switch would feel much smoother. I find that important: things that are conceptually related should be syntactically related (within the realm of common sense, as always).

### Getting there from here 

The example implementation below shows that creating a function with the desired behaviour is quite straightforward. However, calling the builtin `print`{.backtick} is a problem due to the fact that `print`{.backtick} is a reserved word in Python 2.x. Since the `print`{.backtick} statement will be around until Py3K allows us to break backwards compatibility, devising a transition plan that lets programmers \'get ready early\' for the Py3K transition becomes a significant challenge.

If, on the other hand, the builtin has a different name, it is quite feasible to introduce it during the 2.x series. In [PEP 3000](http://www.python.org/peps/pep-3000.html), it is suggested that the `print`{.backtick} statement be replaced by two builtins: `write`{.backtick} and `writeln`{.backtick}. These names are used in the example below. By using alternative names, and providing the builtins in the 2.x series, it is possible to \'future-proof\' code against the removal of the `print`{.backtick} statement in Py3k.

This technique of having two printing operations is not uncommon - Java has both `print`{.backtick} and `println`{.backtick} methods, and C# has `Write`{.backtick} and `WriteLine`{.backtick}. The main problem with the approach is that the `writeln`{.backtick} form will actually be more commonly used, but has the longer, less obvious name of the two proposed functions. This perception of relative use is based on a comparison of relative usage levels of the two current forms of the `print`{.backtick} statement (i.e., with and without the trailing comma) by some of the developers on python-dev.

- [\[lwickjr](./(5b)lwickjr.html): Why TWO functions? Why can\'t we specify `printFunc(....,"\n")`?\]

Some other names for the builtins which have been suggested are:

- `print`{.backtick} - excellent name, but causes transition problems as described above

- `println`{.backtick} - avoids the transition problems, reflects default behaviour of adding a line, matches Java method name

- `printline`{.backtick} - alternative to `println`{.backtick}, that avoids the somewhat cryptic abbreviation

- `writeline`{.backtick} - alternative to `writeln`{.backtick} that avoids the somewhat cryptic abbreviation

- `say`{.backtick} - short alternative to `println`{.backtick} invented in Perl 6 (which uses `print`{.backtick} for no-newline output)

- `out`{.backtick} - not a verb, and converting to it may be problematic due to shadowing by variable names

- `output`{.backtick} - nice symmetry with input, but using the term as a verb is not typical

- `prnt`{.backtick} - easily edited into `print`{.backtick} later on

- `write`{.backtick} - decent name, but confusing when compared to write() method

- `display`{.backtick} - Can be a verb or not. Idea from Scheme.

  - Maybe file-objects should have `write()`{.backtick}- and `writeln()`{.backtick}-methods similar to the built-in functions? *\-- TS*

  [\[lwickjr](./(5b)lwickjr.html): don\'t they already have something similar?\]

### Sample implementation 

This is a Python 2.4 compatible sample implementation of the approach currently in [PEP 3000](http://www.python.org/peps/pep-3000.html). This version of `writeln`{.backtick} doesn\'t provide a `linesep`{.backtick} keyword argument in order to keep things simple. Some other variations are covered further down this Wiki page.

:::: 
::: 
``` 
   1 def write(*args, **kwds):
   2     """Functional replacement for the print statement
   3 
   4     This function does NOT automatically append a line separator (use writeln for that)
   5     """
   6 
   7     # Nothing to do if no positional arguments
   8     if not args:
   9         return
  10 
  11     def parse_kwds(sep=" ", stream=sys.stdout):
  12         """ Helper function to parse keyword arguments """
  13         return sep, stream
  14     sep, stream = parse_kwds(**kwds)
  15 
  16     # Perform the print operation without building the whole string
  17     stream.write(str(args[0]))
  18     for arg in args[1:]:
  19         stream.write(sep)
  20         stream.write(str(arg))
  21         
  22 def writeln(*args, **kwds):
  23     """Functional replacement for the print statement
  24 
  25     >>> writeln(1, 2, 3)
  26     1 2 3
  27     >>> writeln(1, 2, 3, sep='')
  28     123
  29     >>> writeln(1, 2, 3, sep=', ')
  30     1, 2, 3
  31     >>> import sys
  32     >>> writeln(1, 2, 3, stream=sys.stderr)
  33     1 2 3
  34     >>> writeln(*range(10))
  35     0 1 2 3 4 5 6 7 8 9
  36     >>> writeln(*(x*x for x in range(10)))
  37     0 1 4 9 16 25 36 49 64 81
  38     """
  39     # Perform the print operation without building the whole string
  40     write(*args, **kwds)
  41     write("\n", **kwds)
```
:::
::::

### Code comparisons 

These are some comparisons of current `print`{.backtick} statements with the equivalent code using the builtins `write`{.backtick} and `writeln`{.backtick}.

:::: 
::: 
``` 
   1 # Standard printing
   2 print 1, 2, 3
   3 writeln(1, 2, 3)
   4 
   5 # Printing without any spaces
   6 print "%d%d%d" % (1, 2, 3)
   7 writeln(1, 2, 3, sep='')
   8 
   9 # Print as comma separated list
  10 print "%d, %d, %d" % (1, 2, 3)
  11 writeln(1, 2, 3, sep=', ')
  12 
  13 # Print without a trailing newline
  14 print 1, 2, 3,
  15 write(1, 2, 3)
  16 
  17 # Print to a different stream
  18 print >> sys.stderr, 1, 2, 3
  19 writeln(1, 2, 3, stream=sys.stderr)
  20 
  21 # Print a simple sequence
  22 print " ".join(map(str, range(10)))
  23 writeln(*range(10))
  24 
  25 # Print a generator expression
  26 print " ".join(str(x*x) for x in range(10))
  27 writeln(*(x*x for x in range(10)))
```
:::
::::

### Newline / No-newline 

Another possibility to deal with the newline / no-newline cases would be to have a single function which would take an extra keyword argument \"linesep\" or \"end\" (or perhaps some slight magic: an empty string as the last argument), so to print without newline, you would do

:::: 
::: 
``` 
   1 # Print without a trailing newline
   2 print 1, 2, 3,
   3 writeln(1, 2, 3, end='')
   4 # or (shorthand)
   5 writeln(1, 2, 3, '')
```
:::
::::

The default case should be to insert a newline.

- I quite like the single function idea (early versions of this Wiki page used only a single function), but giving it a good name is challenging. The version without the keyword argument is a definite non-starter, though, as there is far too much risk of quirky behaviour when printing a string variable which just happens to contain the empty string. - *Alyssa Coghlan*

  - *BDFL comments:* I definitely am not keen on the single function with keyword args. IMO all you need is a companion function that inserts no separator and no newline; the desired separators are then easily given explicitly. Oh, and you will never get away with using the final empty string to mean \"no newline\". This would be very confusing for someone who printed a variable like so: `print("The value is:", x)` when the variable happens to be empty.

<!-- -->

- [\[lwickjr](./(5b)lwickjr.html): I quite agree. Ugly, but explicit is better than implicit. Function with NO seperator and NO newline: +5 How about `def printFunc(*args): print "".join(map(str, args))`\]

### Iterating Iterables 

Another potentially interesting improvement could be for the function to iterate all iterables, in order to be able to use generator expressions without having to use the star syntax and to avoid the creation of a temporary sequence. This would allow:

:::: 
::: 
``` 
   1 # Print a generator expression
   2 print " ".join(str(x*x) for x in range(10))
   3 writeln(x*x for x in range(10))
   4 # Or optionally
   5 writeln((x*x for x in range(10)), iter=1)
```
:::
::::

This behaviour could be optionally triggered by a keyword argument \"iter\". Another possibility would be to always do the iteration and to force the caller to str() the generator if he wants to print it without iteration (happens rarely).

- Nailing down this kind of behaviour is trickier than one might think. The python-dev discussion of the Python 2.5 candidate library function [itertools.walk](http://mail.python.org/pipermail/python-dev/2005-March/052215.html) goes over some of the potential problems. We\'ve survived without fancy iterator handling in the print statement - let\'s avoid adding anything we don\'t have a demonstrated need for (the extended call syntax stuff comes \'for free\' with the conversion to using a function). - *Alyssa Coghlan*

  - *BDFL comments:* bah. implicitly exhausting iterables has side effects, which is a bad idea for a print function. It would not be a good idea if commenting out a print() call changes the behavior of the program.

<!-- -->

- [\[lwickjr](./(5b)lwickjr.html): How about this? Define `repr(iterator)` to return `"<iteratorData>"` and `str(iterator)}} to return something like {{{" ".join([i for i in iterator])`? -5\]

### Another Strawman 

Here\'s my own strawman implementation of `write()` and `writef()` using semantics I think are pretty useful. I\'ll post to python-dev about the details. - *Barry Warsaw*

:::: 
::: 
``` 
   1 import sys
   2 from string import Template
   3 
   4 class Separator:
   5     def __init__(self, sep):
   6         self.sep = sep
   7 
   8 SPACE = Separator(' ')
   9 EMPTY = Separator('')
  10 
  11 
  12 def writef(fmt, *args, **kws):
  13     if 'to' in kws:
  14         to = kws.get('to')
  15         del kws['to']
  16     else:
  17         to = sys.stdout
  18     if 'nl' in kws:
  19         nl = kws.get('nl')
  20         del kws['nl']
  21         if nl is True:
  22             nl = '\n'
  23         elif nl is False:
  24             nl = ''
  25     else:
  26         nl = '\n'
  27     if isinstance(fmt, Template):
  28         if args:
  29             raise TypeError('invalid positional arguments')
  30         s = fmt.substitute(kws)
  31     else:
  32         if kws:
  33             raise TypeError('invalid keyword arguments')
  34         s = fmt % args
  35     to.write(s)
  36     to.write(nl)
  37 
  38 
  39 def write(*args, **kws):
  40     if 'to' in kws:
  41         to = kws.get('to')
  42         del kws['to']
  43     else:
  44         to = sys.stdout
  45     if 'nl' in kws:
  46         nl = kws.get('nl')
  47         del kws['nl']
  48         if nl is True:
  49             nl = '\n'
  50         elif nl is False:
  51             nl = ''
  52     else:
  53         nl = '\n'
  54     if 'sep' in kws:
  55         sep = kws.get('sep')
  56         del kws['sep']
  57     else:
  58         sep = ' '
  59     if kws:
  60         raise TypeError('invalid keyword arguments')
  61     it = iter(args)
  62     # Suppress leading separator, but consume all Separator instances
  63     for s in it:
  64         if isinstance(s, Separator):
  65             sep = args[0].sep # Should this be s.sep?
  66         else:
  67             # Don't write a leading separator
  68             to.write(str(s))
  69             break
  70     for s in it:
  71         if isinstance(s, Separator):
  72             sep = s.sep
  73         else:
  74             to.write(sep)
  75             to.write(str(s))
  76     to.write(nl)
  77 
  78 
  79 obj = object()
  80 refs = sys.getrefcount(obj)
  81 
  82 write('obj:', obj, 'refs:', refs)
  83 write(Separator(': '), 'obj', obj,
  84       Separator(', '), 'refs',
  85       Separator(': '), refs,
  86       nl=False)
  87 write()
  88 
  89 writef('obj: %s, refs: %s', obj, refs)
  90 writef(Template('obj: $obj, refs: $refs, obj: $obj'),
  91        obj=obj, refs=refs,
  92        to=sys.stderr,
  93        nl=False)
  94 write()
```
:::
::::

- For the code comparisons shown earlier, simply put `write`{.backtick} where `writeln`{.backtick} is currently used, and add the keyword argument `nl=False`{.backtick} for the no trailing newline case. I quite like this approach. - *Alyssa Coghlan*

  - *BDFL comments:* I like the write/writef parallel; would like it even more if it was print/printf. But please drop the Separator thing. The use case isn\'t common enough to burden people with the possibility. Also, we need to spend more time researching the formatting language. (See a post in python-dev by Steven Bethard: \"string formatting options and removing `basestring.__mod__`\".

<!-- -->

- [\[lwickjr](./(5b)lwickjr.html): `def printf(format, *args): print(format(format, *args))`? This definition will actually work with `print` either a statement or function. Further, formatting and printing are seperate concepts and should not be tightly coupled.\]

### Another variant - \`format\` builtin 

Barry\'s `writef`{.backtick} builtin cuts down a little on the typing, but is somewhat inflexible in that it only supports `string %`{.backtick} or `string.Template`{.backtick} formatting when printing directly to a stream. It also causes problems by preventing the use of `to`{.backtick} or `nl`{.backtick} as keywords in the format string. A separate `format`{.backtick} builtin would deal with both of those problems, at the expense of some extra typing when using it. Such a builtin would also help with avoiding some of the tuple related quirks of the string mod operator, as well as making it easy to write code that supports both types of string formatting. The version below is based on Barry\'s, but eliminates the `Separator`{.backtick} concept, and replaces `writef`{.backtick} with `format`{.backtick} - *Alyssa Coghlan*

:::: 
::: 
``` 
   1 import sys
   2 from string import Template
   3 
   4 # Real implementation would avoid blocking use of 'fmt'
   5 # as an element of the formatting string
   6 def format(fmt, *args, **kws):
   7     if isinstance(fmt, Template):
   8         if args:
   9             raise TypeError('invalid positional arguments')
  10         s = fmt.substitute(kws)
  11     else:
  12         if kws:
  13             s = fmt % kws
  14         else:
  15             s = fmt % args
  16     return s
  17 
  18 
  19 def write(*args, **kws):
  20     if 'to' in kws:
  21         to = kws.get('to')
  22         del kws['to']
  23     else:
  24         to = sys.stdout
  25     if 'nl' in kws:
  26         nl = kws.get('nl')
  27         del kws['nl']
  28         if nl is True:
  29             nl = '\n'
  30         elif nl is False:
  31             nl = ''
  32     else:
  33         nl = '\n'
  34     if 'sep' in kws:
  35         sep = kws.get('sep')
  36         del kws['sep']
  37     else:
  38         sep = ' '
  39     if kws:
  40         raise TypeError('invalid keyword arguments')
  41     for s in args[:1]:
  42         to.write(str(s))
  43     for s in args[1:]:
  44         to.write(sep)
  45         to.write(str(s))
  46     to.write(nl)
  47 
  48 
  49 obj = object()
  50 refs = sys.getrefcount(obj)
  51 
  52 write('obj:', obj, 'refs:', refs)
  53 write('obj:', obj, 'refs:', refs, sep=', ', nl=False)
  54 write()
  55 
  56 write(format('obj: %s, refs: %s', obj, refs))
  57 write(format('obj: %(obj)s, refs: %(refs)s', obj=obj, refs=refs))
  58 write(format(Template('obj: $obj, refs: $refs, obj: $obj'),
  59               obj=obj, refs=refs),
  60        to=sys.stderr,
  61        nl=False)
  62 write()
```
:::
::::

### Displaying iterators 

I\'m looking into an approach which adds explicit support for displaying iterators into the string mod operator. The intent is that `"%''j" % (my_seq,)`{.backtick} will become roughly equivalent to `''.join(map(str, my_seq))`{.backtick}. - *Alyssa Coghlan*

[SF Patch #1281573](http://sourceforge.net/tracker/?func=detail&aid=1281573&group_id=5470&atid=305470) for anyone who wants to play with it. Only strings are supported so far (no Unicode), but it illustrates the concept quite well.

:::: 
::: 
``` 
   1 # Print a simple sequence
   2 print " ".join(map(str, range(10)))
   3 print "%' 'j" % range(10)
   4 
   5 # Print a generator expression
   6 print " ".join(str(x*x) for x in range(10))
   7 print "%' 'j" % (x*x for x in range(10))
```
:::
::::

- *BDFL comments:* again, please don\'t do this.

<!-- -->

- [\[lwickjr](./(5b)lwickjr.html): I prefer that `repr()` and `str()` be the Official Pythonic Way to decide which representation gets written. How about `def printFunc(*args): print "".join(map(str, args))` and `def writeFunc(*args): print "".join(map(repr, args))`?\]

### Scrap C-Style Formatting 

What\'s one more strawman, right? ![:)](/wiki/europython/img/smile.png ":)") My approach is tailor-made for gettext (although I\'m no expert in gettext usage). Keywords become the default and positionals disappear completely.

`>>> print('x = {x}, y = {y}, z = {z}', x=x, y=y, z=z)`

There\'s some redundancy in the the keyword arguments (unfortunately), but it helps insulate the format string from the code that uses it. It removes the problems of separator vs no separator It allows it to be self-documenting for the gettext translators, with no problems in reordering or reformatting. You could even give extra arguments that aren\'t always used (but they wouldn\'t be self-documenting I suppose).

Further options are using locals():

`>>> print('x = {x}, y = {y}, z = {z}', **locals())`

but only if you don\'t mind exposing them (debatable). If you need something besides %s (the default) then go as follows:

`>>> print('x = {r:x}, y = {f9.8:y}, z = {i:z}', x=x, y=y, z=z)`

Or maybe even something that allows arbitrary arguments to be passed to the formatter. - *Adam Olsen*

### Another idea 

String formatting with %\* is a bad idea, imho. Since python is anyway dynamic by nature, why not add built-in string evaluation, as in boo [http://boo.codehaus.org](http://boo.codehaus.org). for example:

    x = "lucy"
    write("i love ${x}")

or

    x = 7
    write("the answer is ${x * 2}")

if strings (or a special flavor of string, say one marked with backticks\*) allowed evaluation of expressions, code will never look like

    print "x = ", x, "y = ", y

but rather

    write("x = ${x}, y = ${y}")

which is much more readable and easier to maintain. imagine working with 20 \'%s\' in a single string! it\'s a disaster. even using the silly %(name) is bad, since you then have to fill a huge dict after your string.

(\*) backticks: yes, backticks mean repr(), but did anyone ever hear of them? [\[lwickjr](./(5b)lwickjr.html): I use them regularly.\] i think they are depricated anyway. [\[lwickjr](./(5b)lwickjr.html): Why?\] adding a new built-in type, evalstr (\"evaluating string\"), marked by backticks, is very simple and almost completely backwards compatible. and it works not only in the context of printing output.

    write(`hello ${os.getuid()}, the time now is ${time.asctime()}, and you are running on ${os.name}`)

true, it doesnt solve the write/writeln \"problem\", and i must admit that print as a statement is a pretty useful feature (no parenthesis hassle), but adding evalstrings will make long format string possible and maintainable. plus, it gets us rid of the ugly writef or printf proposals.

### Yet Another Formatting Alternative 

There\'s a few goals for any formatting scheme

1.  Inline naming (not off to the right somewhere)

2.  Expression arguments (`obj.attr`{.backtick} is common)

3.  Gettext swapout

4.  No repetition of names

5.  No explicit call to `locals()`{.backtick}

Our existing % formatting can do 2,3,4,5, but if you want 1 you instead get 1,3,4. My previous suggestion handles 1, but fails 4 miserably, as well as 5. My new suggestion handles all 5 goals simultaneously.

The full syntax is:

    $"filler {name:expr formatter arguments} filler"

Most of that is optional. The most common way to use it would be:

    $"filler {x} filler"
    # Equivalent to...
    $"filler {x:x str} filler"
    # Equivalent to...
    FormatString("filler {x str} filler", {'x': x})

A `FormatString`{.backtick} instance does not immediately evaluate. Instead, it waits until its `__str__`{.backtick} method is called, at which point the above example becomes:

    "filler %s filler" % (str(fs.args['x']),)

Because of the lazy evaluation it is possible to use it for gettext.

    def _(fs):
        return FormatString(localizedstrings(fs.format), fs.args)

Further options:

    $"x = {:3}, y = {:42}"  # Names are ommited so numbers (positions) will be generated for them
    $"f = {:1/3 float 10.5}"  # "f = %10.5f" % (1/3)
    $foo  # Parse error!  $ is a string prefix, NOT an operator

Looking this over, the weakest link seems to be in the formatter aspects. It needs a way to specify an expression that happens after the initial evaluation, but after gettext has had a chance to replace the format string. Unfortunately I\'m out of ideas so I\'ll leave it be.

\- *Adam Olsen*

### Extend String.Template? 

The basic idea would be to incorporate the functionality of the existing `string.Template` module as a built-in. The format prefix characters are stolen directly from Perl, which makes them both lightweight and familiar.

However, the current API is too cumbersome for \"hello world\" use. So we need to streamline it a bit.

The first part is getting rid of the need to explictly instantiate the String.Template() object. I suggest a new \"string decorator\", similar to \"r\" and \"u\", which indicates that the string is a template string. Lets assume that the prefix is \"t\" for \"template\" for now:

    print t"Hello, $user!".substitute( user="Tim" )

The \'t\' prefix should be usable in conjunction with the \'r\', \'u\', triple-quote and other string variations.

However, its still too wordy. We need to get rid of the `.substitute()`. One thought (which may not be workable) is to detect when the template is being coerced into a string by overloading `__str__`, which then automagically calls substitude using the local scope as the dictionary. (The hard part is getting the scope - because the coercion to string might be happening inside the print function. Perhaps the string can capture the scope pointer upon construction.)

Ideally, what we would then have is something similar to the Perl syntax:

    print t"Hello, $user!"

\- *Talin*
