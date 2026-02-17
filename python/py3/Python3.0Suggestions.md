# Python3.0Suggestions

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

Other syntax ideas and feature ideas for [Python3.0](Python3.0) .

## declaring parameter and variable types 

It may be easier, reduce bugs, offers intelli-sense like in Microsoft Visual Studio. All of that could reduce development-time.

## script to translate python source from one version to one other 

does any script (will) exists, to translate code, form python 2.3 to python 2.4 or from python 2.3 to 2.4?

## Different regular expressions modules for bytes and unicode text 

I do not allways understand whether `re` module is designed for text or binary? The struct module for interfacing with binary files, or network datagrams might be improved by adding some of the regular expressions facilities, such as split.

Two modules like `re` might be a good thing, one binary oriented, and the other unicode oriented: \* one for binary data, with some of the `re` and `struct` facilities adapted to bytes. \... with eventually stuff like reading a two bytes encoded size, then a buffer from the previous size \... \* one for unicode/text regular expression should be in some way text/unicode oriented\.... like ICU portable one.

For example, the ICU one provide the following patterns:

- \\N{UNICODE CHARACTER NAME} Correspond au caractère nommé

- \\p{UNICODE PROPERTY NAME} Correspond au carctère doté de la propriété Unicode spécifiée.

- \\P{UNICODE PROPERTY NAME} Correspond au carctère non doté de la propriété Unicode spécifiée.

- \\s Correspond à un caractère séparateur. un séparateur est définit comme \[\\t\\n\\f\\r\\p{Z}\].

- \\uhhhh Correspond à un caractère dont la valeur hexa est hhhh.

- \\Uhhhhhhhh Correspond à un caractère dont la valeur hexa est hhhhhhhh. Exactement huit chiffres héxa doivent être fournis, même si le code point unicode le plus grand est \\U0010ffff.

- the portable library \"International Components for Unicode\" might be used. It might be largely available as it is existing in debian distribution.

- [Unicode](Unicode)

related pep:

- [: Python Unicode Integration](http://www.python.org/peps/pep-0100.html)

- [: Allow str() to return unicode strings](http://www.python.org/peps/pep-0349.html)

- [: Byte vectors and String/Unicode Unification](http://www.python.org/peps/pep-0332.html)

- [: Adding a bytes Object Type](http://www.python.org/peps/pep-0296.html)

## New binary operator symbols d e \` 

these operators d e \` should be added to the language having the following meaning:

- \<= \>= !=

this should improve readibility (and make language more accessible to beginners).

This should be an evolution similar to the digraphe and trigraph (digramme et trigramme) from C and C++ languages. In C, \"\<%\" or \"??\<\" mean \"{\" such as.

gcc -trigraphs a.c

    ??=include <stdio.h>

    int main(int argc, char *argv ??( ??) )
            ??<
            printf ("hello world\n");
            ??>

See also: \* The \<\> operator: use != instead [http://www.python.org/peps/pep-3000.html#id54](http://www.python.org/peps/pep-3000.html#id54)

------------------------------------------------------------------------

From an aesthetic point of view, I would *very much* prefer not to see the \<\> operator go away. At least on U.S. keyboards, you could make the case that \<\> is easier to type than !=, but really I just dislike the exclamation point as an operator. GIven that Python is not intended to look like C and other languages that use C-like syntax, is this really necessary? We already use \"not\" for logical negation rather than \"!\", so the argument that \"!\" means negation doesn\'t hold.

\-- [MichaelFromberger](./MichaelFromberger.html)

------------------------------------------------------------------------

Most US people will be unable to easily type ≤, ≥ or ≠ on their keyboards. I believe also that Guido has decreed ASCII as the character set with the exception of perhaps in comments and strings. Finally, what do digraphs and trigraphs have to do with your proposal? I don\'t think most people believe them to have been a success.

\-- [SkipMontanaro](SkipMontanaro)

------------------------------------------------------------------------

For keyboard, I distinguish two issues: one is writing text (input), the other one is reading it (output/display). Most used modern systems (linux and windows) and most used modern editors (vim for example) can display unicode characters (even if some old browsers can break unicode text). For writing python, a special editor is needed due to indentations issues; such an editor might have some feature for input of some unicode characters. When not, the old system of writing a comparison with two ASCII characters \'\<=\' is not incompatible with the use of one single unicode character ( parse can accept both). Might be the use of non ASCII (in fact, extended ASCII) characters in the source is an issue. I do not have skill for python parser. But might be nice for the long term (python 4.0?). For digraphs, I simply consider \'\<=\' as a digraph, because the same concept can be represented with a single characer, instead of two.

Finally, some microsoft compilers are friends with extended ASCII variable names, and I believe that chinese people (those who promote international internet names) will use such programming language before 2016\... \--

## Optional Static Typing / Adaptation 

- [Adding Optional Static Typing to Python](http://www.artima.com/forums/flat.jsp?forum=106&thread=85551) - article by Guido with responses

- [\"Optional Static Typing\" thread](http://groups-beta.google.com/group/comp.lang.python/messages/a7960bedeffdf36b,9ff25b65c3523b32,ea183c14193161d8,b0f5feee912db455,4888ee248493142e,f96c9f8f1d65b439,dc16b1ac3c356751,7f95e63c5f791a07,c6afe85be43223db,b0de4d002834507d?thread_id=8ed8632b8c5a551a&mode=thread&noheader=1&q=optional+static+typing#doc_a7960bedeffdf36b)

- [\"Adding static typing to Python\" thread](http://groups-beta.google.com/group/comp.lang.python/messages/03553183983059e9,b505ef98e0436d24,dad1a48eee3248a4,7fac43f511f6bb21,ee614add572c34b1,7030280781fef1dc,6a852f4133c86be5,3a695733220ba136,4bec8d2fefbc0ce6,45b123013d82a365?thread_id=ff4df85e58d128bc&mode=thread&noheader=1&q=optional+static+typing#doc_03553183983059e9)

## Lambda / Anonymous Methods / Closures 

- [AlternateLambdaSyntax](AlternateLambdaSyntax)

- Anonymous Methods / Closures

- [\"Securing a future for anonymous functions in Python\" thread](http://groups-beta.google.com/group/comp.lang.python/browse_frm/thread/81e17b1d3ccba538/41713ae1c0d7385a#41713ae1c0d7385a)

- [http://boo.codehaus.org/Closures](http://boo.codehaus.org/Closures)

- [http://logix.livelogix.com/tutorial/5-Standard-Logix.html#5.8](http://logix.livelogix.com/tutorial/5-Standard-Logix.html#5.8) (uses same syntax as above except no multi-line support)

## Print as builtin instead of a statement 

- [PrintAsFunction](PrintAsFunction)

## \"..\" Sequences, Custom Infix Operators 

- [http://www.livelogix.net/logix/](http://www.livelogix.net/logix/)

- [\"Other notes\" thread](http://groups-beta.google.com/group/comp.lang.python/browse_frm/thread/6fb45278f4a24648/93ce3e9a08f5e4c7#93ce3e9a08f5e4c7)

## Improved default value logic for Dictionaries 

- The setdefault() method is badly named and poorly designed. In a typical call, `d.setdefault.(k, []).append(v)`, the list may be unnecessarily instantiated and discarded on every call. At a minimum, default value should be a new empty list instead of None: ` d.setdefault(k).append(v) `.

- A more versatile idea is to realize that defaults generalize to the whole dictionary instead of an individual lookup. A call to setdefault would then change the whole dictionary\'s behavior when a key is not found:

<!-- -->

        counts = {}
        counts.setdefault(value=0)
        for elem in data:
            counts[elem] += 1

        index = {}
        index.setdefault(function=list)
        for pageno, page in enumerate(pages):
            for line in page:
                for word in line.split():
                     index[word].append(line)

Note that it\'s not really necessary that setdefault() take \*args and \*\*kwargs arguments to be passed to the function; PEP 309 allows a reasonable solution to this problem:

:::: 
::: 
``` 
   1 from functional import partial
   2 d.setdefault(function=partial(list, [0]))
   3 d.setdefault(function=partial(dict, a=0, b=1))
```
:::
::::

## Better boolean logic 

The and/or operators should only return boolean values. This makes their use less error-prone, less prone to abuse, and more closely match other languages. Also, it will simplify the underlying bytecode which currently inserts many `POP_TOP` instructions to complete conditionals. The need to insert these instructions also results in extra code paths and jump instructions. Overall, the language will become more intuitive, more reliable, simpler, and faster.

- *While I agree with your points. I would find \"Better boolean logic\" counter-productive in many instances. I personally prefer the former of these examples as the latter slows me down and, in my case, invites errors. {{{return a() or \'b\'*

#\-\--

temp = a() if temp:

- return temp

else:

- return \'b\'

}}}The latter structure always makes me shudder. I\'ve never encountered a good use for non-boolean output from \"and\" (in Python. Other languages are a different story.) but using \"or\" in the first example is both quicker and more intuitive for many people not to mention reducing code complexity.\-- [StephanSokolow](./StephanSokolow.html)

*Unnecessary if:else: statements to take the place of the current \"or\" behavior make my soul hurt. I use \"and\" sometimes, typically like `bar = foo and foo.get('bar')` when `foo` might be None or a dictionary. \-- [IanBicking](IanBicking)*

Agreed, only comparison operators (`==`, `>`, `<`) should return True/False, leave and/or as is *(Note: the comparison operators do \*not\* return only True/False; they can return any value, as used by Numeric and SQLObject)*

::: some new true boolean operators should be added. The binary/boolean `and` should be represented by one of the following: `+`, `&&`, `'`. The binary/boolean `and` should be represented by one of the following: `*`, `||`, `(`.

The +, \* are by mathematical analogy with addition and multiplication, within mathematical ‚ .

The && and \|\| comes from the ugly c/java notation, I mean languages from an other century\...

`'`. `(`. comes from unicode representation for boolean operations. They might be completed by three others boolean operators, xor, nand and nor: `» ¼½` `'`. `(` are for boolean what `)*` are for set. (similar notation, similar meaning).

They also have a curly notation: `ÎÏ`.

    a + b # a or b. should return True, when a and b are true (instead of 2) 
    a * b #should return a logic_and b for boolean

    a && b #should return a logic_and b for boolean
    a || b #should return a logic_or b for boolean

    a ' b #should return a logic_and b 
    a ( b #should return a logic_or b 

    should return True or False

## Disallow calling class methods from instances 

Calling with a instance is almost never what you want. When it is done, the results are not especially readable, and the code suggests that it is doing something that it isn\'t:

    {'a'=1}.fromkeys('poof') # what happened to 'a'? 

I disagree to this. Although calling class methods on the instance from the outside will usually be rubbish, it will very often be useful and intended behavour inside instances. For example:

    class mydict(dict):
      def key_copy(self):
        return self.fromkeys(self)    

This will assert that whatever subclass of mydict is created and not some other class. One could argue though that this could be achieved by the more cluttersome `self.__class__.fromkeys()`.

## Simplify the syntax for raising exceptions 

- Eliminate string exceptions entirely.

- Alway require instantation. IOW, prefer `raise ValueError(dat)` to `raise ValueError, dat`.

- Require that all exceptions subclass from *Exception*.

- Have *Exception* be a new-style class

Include docstrings when printing user-defined exceptions such as implemented by [http://soiland.no/software/doc_exception.py](http://soiland.no/software/doc_exception.py):

    >>> class IdiotError(Exception):
    ...    """Some idiot occured"""
    ...
    >>> raise IdiotError
    Traceback (most recent call last):
      File "<stdin>", line 1, in ?
    __main__.IdiotError: Some idiot occured

This could simply be implemented in `Exception.__str__` when `args` is empty.

## Fix implementation of in-place operators 

The current implementation will call `__iadd__()`, allowing it to do the in-place change, but then require that the method return the new value and then store it again. Ideally, all the responsibility for the update should lie with the `__iadd__()` method and it should return None. This simplifies the bytecode and eliminates some annoying behavior (such as `a[0]+=1` succeeding **and** raising an error when `a=([0],)`.

## Remove the distinction between data and non-data decriptors 

Having the distinction provides a tiny benefit but incurs a large cost in terms of implementation complexity and increasing the learning curve for descriptors. Using the presence or absence of a setter to distinquish the two is somewhat hackish and confuses the heck out of anyone first trying to master descriptors. Even after using descriptors for a while, that nuance remains an annoying distraction.

*Note that descriptors are a somewhat advanced feature, not really expected to be used by beginners or on a day to day basis, so the extra flexibilty given by by the data/non-data descriptors distinction may still be worth the small extra complexity it adds to the protocol* .

## Reconsider the inclusion of \_\_slots\_\_ or re-evaluate its implementation 

Guido has expressed that this is a highly popular, but badly misunderstood tool that is often used incorrectly.

- If `__slots__ `is misspelled, there is no visible indication of failure.

- The purpose of the tool is **not** to make it more difficult to assign attributes.

- `__slots__` do not inherit.

- `__slots__` complicates and slows the implementation of new-style classes.

*I have never see `__slots__` misused, or used much at all, so maybe in typical real projects misuse isn\'t much of an issue? \-- [IanBicking](IanBicking)*

## Extra operators for strings and lists 

[Operators as `- & | ^` should be used for strings and lists directly in place of first making a `set` data type (see [PEP 218 - Adding a Built-In Set Object Type](http://www.python.org/peps/pep-0218.html)).]

The operators `/`, `*` and `%` could also be used to split and stitch strings and lists:

:::: 
::: 
``` 
   1 # split:
   2 'spameggsham' / 'a' == 'spameggsham'.split('a') == ['sp', 'meggsh', 'm']
   3 # remainder:
   4 'spameggsham' % 'a' == 'aa'
   5 # stitch:
   6 ['sp', 'meggsh', 'm'] * 'a' == 'spameggsham'
   7 
   8 # split list:
   9 [1, 2, 3, 4, 5] / [2, 3] == [[1], [4, 5]]
```
:::
::::

- *`'spameggsham' % 'a' == 'aa'` is sort of unclear, and .count(\'a\') works just as well. The others sound fine.\-- [ChrisRebert](./ChrisRebert.html)*

## Move rarely-used builtins to the library 

pow() to the math module!

## Don\'t remove callable() 

Please don\'t. There are times where you want to know if an object is callable without calling it. For instance if you create a metaclass and need to wrap defined methods passed to `__new__`, and don\'t want to wrap class variables.

- *Why use callable() then? Isn\'t this what inspect.ismethod(), .isfunction() etc. are for? \--[StevenBethard](StevenBethard)*

In addition, using exceptions for normal control flow is not good code style.

- *Using exceptions in normal control flow is very typical in Python code, so not everyone agrees \-- [IanBicking](IanBicking)*

## Make API of set, list, dict more consistent 

No need for copy function. A clear function for all of them.

## Make copy and deepcopy built-ins, replace copy methods by \_\_copy\_\_ 

It would clarify how copy should be done.

- *Some people will argue that copy is hard, and deepcopy nearly impossible, to do \"right\" for a typical program, and so you shouldn\'t encourage these to be used generally. For specific data types \-- like dictionaries and lists \-- there are simple idioms for copies. \-- [IanBicking](IanBicking)*

## Don\'t remove cmp() and \_\_cmp\_\_ 

Even if it looks as if \"there\'s more than one way to do it\" applies, it makes implementing comparison so easy that it must be kept. If the rule \"there\'s only one way to do it\" is important, maybe only keep [cmp]?

:::: 
::: 
``` 
   1    def __cmp__(self, other):
   2       return cmp(self.member1, other.member1) or cmp(self.member2, other.member2)
```
:::
::::

Are rich comparisons really that much more complex?

:::: 
::: 
``` 
   1    def __lt__(self, other):
   2       return (self.member1, other.member1) < (self.member2, other.member2)
```
:::
::::

## Builtin Literal for sets 

Make a set literal:

:::: 
::: 
``` 
   1    # Use "< >"
   2    s = <'a', 'b', 'c'>
   3    
   4    # Or use "| |"
   5    s = |'a', 'b', 'c'|
```
:::
::::

- Why not using the mathematical notation?

:::: 
::: 
``` 
   1    # Use "{ }"
   2    s = {'a', 'b', 'c'}
```
:::
::::

- Curly braces are already used for dictionaries. Even if there is no ambiguity to the parser, I think it is confusing to the programmer\'s eye to have both meanings. I\'d prefer using pairs of braces, because it makes sets look different than dicts at first sight and still resembles mathematical notation. \--[RobertoBonvallet](./RobertoBonvallet.html)

:::: 
::: 
``` 
   1    # Use "{{ }}"
   2    s = {{'a', 'b', 'c'}}
```
:::
::::

## Make extended function call syntax more iterator friendly 

Extended function call syntax currently does not play well with iterators because it produces a tuple to be passed in to the function. This means API developers face a tough choice - either accept an iterator and make the function clumsier for use with a short sequence of specific variables (as the user of the API has to create a throwaway list or tuple), or use positional arguments and make the API iterator unfriendly (as an iterator passed via extended function call syntax gets unraveled and stuffed into a tuple).

If the extended function call syntax was able to avoid forcing the creation of the tuple, then the choice would be easy - always use the positional argument support.

- There are some serious compatibility problems with this idea, and Guido has said \"Never gonna happen\" on [python-dev](http://mail.python.org/pipermail/python-dev/2005-September/056113.html)

## Require \_\_iter\_\_() for DictMixin instead of keys() 

Currently, [UserDict](./UserDict.html).[DictMixin](./DictMixin.html) requires the methods `__getitem__()`, `__setitem__()`, `__delitem__()`, and `keys()` to supply the appropriate other methods of the dict interface. I would prefer that it require `__iter__()` instead of `keys()`. [As I understand it](http://mail.python.org/pipermail/python-list/2005-January/258569.html), the fact that it uses `keys()` instead of `__iter__()` is mainly due to the order of introduction of `keys()` and `__iter__()`. Since `keys()` can easily be defined in terms of `__iter__()`, in Python 3.0, I\'d like to see `__iter__()` be the required method instead. \-- [StevenBethard](StevenBethard)

- The default `__iter__` implementation could potentially check if `self.keys` is also the default implementation, and if not then it calls that method. `keys` in turn calls `list(self)` always. \-- [IanBicking](IanBicking)

## Raise the level of os module functions 

Many/most functions in the `os` module are thin wrappers around their underlying POSIX namesakes. This can lead to some surprises. For example, `os.rename` won\'t rename a file across partitions. It may not (I don\'t know for sure) work on Windows if another program has the file open. \-- [SkipMontanaro](SkipMontanaro)

## Parameterize functions that hardcode stdout or stderr 

Some modules hardcode the target of their output, typically as stdout or stderr. One example is the dis module. The functions/methods in such modules should be updated to accept an optional stream argument. \-- [SkipMontanaro](SkipMontanaro)

## Module interface 

- Modules should support cleaning up after themselves on unloading, just like objects do. This is especially interesting for extension modules.

## Stronger Distinction between Tuples & Lists 

Guido has often indicated he thinks of tuples as something more akin to Pascal records or C structs than to arrays or lists. Still, people continue to treat them as immutable lists. There has been a fair amount of talk recently about creating \"frozen\" versions of mutable objects. That would allow them to be used as dictionary keys and remove a significant reason to treat tuples and lists (nearly) the same. For example:

        d = {}
        d[freeze([1,2,3])] = "happy"

If you no longer need tuples to masquerade as frozen lists, why not consider making the two types more distinct? Get rid of the sequence API for tuples (`len(some_tuple)` would raise an exception, no index or slice notation) and give them attributes. How about:

        color = (red=255, blue=17, green=0xcc)
        print color.blue * 3                     # prints 51
        another_color = tuple(favorite_color, green=0)
        print another_color == color             # prints False
        bad = tuple([1,2,3])                     # raises TypeError exception

Storagewise they\'d be much like current tuples (that is, cheaper than dicts) and they\'d also be immutable. Field access would be via attribute.

What is the point? As long as you are calling it a structure, you might as well define it, so how is this different from

        class color(object):
            __slots__=("red", "blue", "green")
            def __init__(self, red=None, blue=None, green=None):
                self.red=red
                self.blue=blue
                self.green=green

And yes, I know that [slots] is not supposed to be used for limiting attributes, but it does work, and is still more flexible than using a tuple. And yes, I know that [slots] is awkward, but that is another issue. \-- JimJJewett

## Unifying generators 

:::: 
::: 
``` 
   1    # A generator:
   2    g = (x ** 2 for x in numbers)
   3    
   4    # A list:
   5    list(x ** 2 for x in numbers) == [x ** 2 for x in numbers]
   6    
   7    # A dict:
   8    dict((x, x ** 2) for x in numbers) == {x: x ** 2 for x in numbers}
   9    
  10    # A set:
  11    set(x ** 2 for x in numbers) == <x ** 2 for x in numbers>
```
:::
::::

## Replace Integer Masks with Sets 

(This idea was mentioned on c.l.py by Bryan Olson. I\'m just recording it, though I agree it seems like a good idea. \-- [SkipMontanaro](SkipMontanaro))

In places where Python usage currently uses a bitmask to specify a set of options it would be more Pythonic to instead use a set. For example, `re.compile()` accepts two args, a pattern and an optional set flags. Those flags are specified as integers bitwise-or-ed together:

        pat = re.compile("some pattern", re.I|re.S|re.X)

It seems it would be more Pythonic to use a set:

        pat = re.compile("some pattern", set(re.I, re.S, re.X))

The elements of the set wouldn\'t even need to be integers.

## Replace abs() with \| \| 

Use `| |` (like in mathematics) to get absolute value in place of the `abs()`-function:

:::: 
::: 
``` 
   1    abs(-1) == |-1| == 1
```
:::
::::

## Require Parens for Tuple Definition 

This is a fairly common mistake:

       x = 1,

and results in x referring to a one-element tuple. I think Python 3.0 should require parens for all tuple literals. \-- [SkipMontanaro](SkipMontanaro)

- Would that disallow `a, b == func()` ? That would make me very sad. \-- [IanBicking](IanBicking)

  Yes. You\'d have to write `(a, b) == func()` \-- Skip

## Remove \[\<listcomp\>\] syntax in favor of list(\<genexp\>) syntax 

Since Python 3.0 will retain generator expressions and therefore *must* support the `list(...)` syntax, I think the redundant `[...]` list comprehension syntax should be removed.

The main reasons to keep the `[...]` syntax:

- it saves four characters of typing
- it looks like list literals, so you\'ll know it\'s a list

The main reasons to remove it:

- it does not provide any substantially different semantic support:
  - both expressions produce lists by iterating over some iterable(s)

- it does not provide any substantially different syntactic support:
  - the allowed forms of `<listcomp>` and `<genexp>` expressions are identical

  - both the `[...]` and `list(...)` forms use parentheses/brackets, so the inner expression can be broken across lines in exactly the same ways

- it doesn\'t look like other similar operations in Python, e.g. `set(...)`, `collections.deque(...)`, `sorted(...)`, `min(...)`, etc.

- it looks like list literals, so you may not immediately realize the differences, e.g. that it\'s iterating over some iterable

I think the arguments for removing the redundant `[...]` form outweigh the arguments for retaining it. \--[StevenBethard](StevenBethard)

## Move builtins to be methods on the types they apply to: 

        [1,2,3].len() == 3
        [1,2,3].max() == 3

Instead of:

        len([1,2,3]) == 3
        max([1,2,3]) == 3

It seems inconsistent to have certain functions (like hex, round, raw_input, pow!?) as builtins when they can\'t be applied to every type of object.

## Default to assign class object rather than class reference 

Consider the following:

       havarti = Cheese
       havarti.spices = "carraway"
       gouda = havarti
       gouda.spices = ""
       # havarti.spices is ""!

How useful is it to assign a reference by default? You force everyone who wants to assign class objects to create a method for each class they want to copy that copies all values of the class to the new class variable.

On the other hand, you should be able to assign references. It\'s never required, but sometimes useful. Perhaps a standard method or a new keyword could be used to assign the reference rather than the value.

The main issue with copying references is that it is somewhat inconsistent. Basic datatypes don\'t suffer from this issue; complex datatypes do.

The other large issue with this is that it\'s not covered anywhere in the tutorials.

The third large issue is that the common usage is the one you have to do the most work for.

So why is this a feature?

\--Chris W

Python does not have a prototype-based object model. If you want to implement this it\'s easy enough:

        class Cheese:
            def __init__(self):
                ...

            def copy(self):
                variant = Cheese()
                variant.__dict__.update(self.__dict__)
                return variant

        havarti = Cheese()
        havarti.spices = "carraway"
        gouda = havarti.copy()
        gouda.spices = ""
        print havarti.spices

\-- [SkipMontanaro](SkipMontanaro)

Ah, okay. Thanks. Then I would suggest updating the documentation instead.

\-- Chris W

## Unicode identifier 

If Perl, dot Net, [StarBasic](./StarBasic.html) and Java have unicode ientifier support, will python one day have it?

## Remove support for complex numbers 

Complex numbers are almost never used by casual programmers and integration into python core provide only one tiny syntaxic sugar:

:::: 
::: 
``` 
   1 # you can write a complex number
   2 x = 10+5j
   3 # instead of
   4 x = 10+5*j
   5 # or
   6 x = complex(10,5)
```
:::
::::

So I suggest to move complex data type and cmath module to an external library ([SciPy](SciPy) for sample).

## Reserve some keywords for futur extensions 

Some PEPs which are not ready for Python 3.0 will need new keywords. Reserving them in Python 3.0 will provide better backward compatibility in Python 3.x. Of curse, this should only be done for PEPs wich have good chances to be accepted.

This reserved keywords could be: switch, case, make \...

## Simplify the filename search when importing 

When Python executes \'import os\' (for example) it looks for

    os.so
    osmodule.so
    os.py
    os.pyc

Is the `osmodule.so` really needed when you already have `os.so`, or is the \'module\' suffix just an historical relic which can be removed? It seems unnecessary, a bit like adding \'string\' onto the end of all your string variables.

## Increment operator 

Although python have other means for iterate between stuff, increments are very common, it would be nice to have operators to increment/decrement a variable.

eg:

    foo++
    foo--
    ++foo
    --foo
