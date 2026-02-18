# DubiousPython

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

This page follows a [suggestion](http://groups.google.ca/groups?hl=en&lr=&selm=mailman.8378.1103832808.5135.python-list%40python.org&prev=/groups%3Fq%3Ddubious%2BFernando%26hl%3Den%26lr%3D%26group%3Dcomp.lang.python.*%26selm%3Dmailman.8378.1103832808.5135.python-list%2540python.org%26rnum%3D2) of [FernadoPerez](./FernadoPerez.html) on comp.lang.python that there should be a collection of bad python practices together with an explanation of the badness and a preferred alternative.

## String Concatenation 

String concatenation is building up a relatively lengthy string from a collection of strings.

### Dubious Way 

Newcomers to Python often try to build strings up like this:

:::: 
::: 
``` 
   1 >>> string_list = ['one', 'big', 'string', 'in', 'pieces']
   2 >>> new_string = "" 
   3 >>> for s in string_list: 
   4         new_string = new_string + s
   5 >>> print new_string 
   6 onebigstringinpieces 
   7 >>>
```
:::
::::

### The Problem 

This is slow and resource heavy. Each time through the `for` loop, a new string is built and the old one is discarded. That might not matter so much for such a small case, but as the number of elements to be joined creeps up, so too does the inefficiency.

*The above code is perfectly fine. Its readible, and it works. Worrying about speed/performance when it is not an issue is one of the worst programming practices. \"Premature Optimization is the Root of All Evil\" \-- see [PrematureOptimization](http://c2.com/cgi/wiki?PrematureOptimization "Wiki")*

*Training yourself to NEVER use some possibly-tempting idiom that is NEVER right is not premature: JUST SAY NO, learn to see this way to build up strings as ugly and always wrong, and live happily ever after!*

If we are going to quote Knuth: *The conventional wisdom shared by many of today\'s software engineers calls for ignoring efficiency in the small; but I believe this is simply an overreaction to the abuses they see being practiced by pennywise-and-pound-foolish programmers, who can\'t debug or maintain their \"optimized\" programs. In established engineering disciplines a 12 % improvement, easily obtained, is never considered marginal; and I believe the same viewpoint should prevail in software engineering.*

From the same paper (Structured Programming with go to Statements) that he stated: *We should forget about small efficiencies, say about 97% of the time: premature optimization is the root of all evil.*

Yet we should not pass up our opportunities in that critical 3 %. A good programmer will not be lulled into complacency by such reasoning, he will be wise to look carefully at the critical code;

### Preferred Alternatives 

#### String Formatting 

For short cases where the number of strings to be joined is known, you can use string formatting as follows:

:::: 
::: 
``` 
   1 >>> print '%s%s%s%s%s' % tuple(string_list)
   2 onebigstringinpieces
```
:::
::::

This is much more efficient, but is also rather more limited in the range of circumstances to which it applies. It could be made more general by constructing the formatting string as a function of `len(string_list)`{.backtick}, but this would be a bit dubious, too. It\'s also less readible, less maintainible. A better alternative is found in the next section.

#### The join method of strings 

The join method of the string type lets you perform the concatenation as follows:

:::: 
::: 
``` 
   1 >>> print "".join(string_list)
   2 onebigstringinpieces
```
:::
::::

This is quite efficient and perfectly general as it applies to any arbitrary list of strings. (You don\'t need to know the list length in advance.)

The major thing to puzzle the newcomer here is why `"".join(some_list)`{.backtick} rather than `some_list.join()`{.backtick}. The way to think of this is that you are using the string \"\" to join the elements of some_list. Hence,

:::: 
::: 
``` 
   1 >>> print 'JOINT'.join(string_list)
   2 oneJOINTbigJOINTstringJOINTinJOINTpieces
```
:::
::::

That said, some do consider this aspect of the join method of strings odd enough to count as a [PythonWart](./PythonWart.html).

If the `''.join(some_list)`{.backtick} syntax really bothers you, one option is to bind the method to a different name, e.g.

:::: 
::: 
``` 
   1 >>> join = ''.join
   2 >>> print join(string_list)
   3 onebigstringinpieces
   4 >>> 
   5 >>> underscore_join = '_'.join
   6 >>> print underscore_join(string_list)
   7 one_big_string_in_pieces
```
:::
::::

*The audience should be an expert in the idioms of a language when considering readability.* The join is simple to this crowd.

## Overly Verbose Conditionals 

Among the most common tasks in programming is to test if a condition obtains and act accordingly. It is common for newcomers to Python to adopt an all-together overly verbose idiom for this.

### Dubious Way 

:::: 
::: 
``` 
   1 if (count > 10) == True:
   2     # do something
```
:::
::::

:::: 
::: 
``` 
   1 def count_tester(count):
   2     if count > 10:
   3         return True
   4     else:
   5         return False
```
:::
::::

:::: 
::: 
``` 
   1 if len(somecontainer) > 0:
   2     # do something
```
:::
::::

### The Problem 

There is a slight speed of execution inefficiency in these examples. The first example has the overhead of an extra method lookup (`bool.__eq__`{.backtick}) and an extra name lookup (`True`{.backtick}). The second example has the overhead of an extra branch statement. The third example has the overhead of two extra method lookups (`somecontainer.__len__`{.backtick} and `int.__cmp__`{.backtick}).

But much more important is the speed of entry and understanding inefficiency. All other things being equal, extra typing is evil. And, unless some substantial gain in clarity is purchased by the extra characters, the more characters in the code, the longer that code will take to understand. (The programming time you save could well be your own!)

### Preferred Alternatives 

:::: 
::: 
``` 
   1 if count > 10:
   2     # do something
```
:::
::::

:::: 
::: 
``` 
   1 def count_tester(count):
   2     return count > 10
```
:::
::::

Most non-empty containers evaluate to True in a boolean context, so no test on len() is generally necessary:

:::: 
::: 
``` 
   1 if somecontainer:
   2     # do something
```
:::
::::

Some containers (e.g. numarray.array) do not evaluate this way. In these cases, the preferred idiom is:

:::: 
::: 
``` 
   1 if len(somecontainer):
   2     # do something
```
:::
::::

## Overuse of lambda 

Lambda forms allow anonymous functions to be created and used as part of an expression. However, when a function is already named, wrapping this function in a lambda can decrease readability and affect program efficiency.

### Dubious Way 

:::: 
::: 
``` 
   1 dict(a=lambda x: str(x),
   2      b=lambda x: some_dict.get(x))
```
:::
::::

### The Problem 

Using a lambda when a function is already named incurs the extra overhead of one function call, which is generally undesirable as function calls are relatively expensive in Python. Even setting execution efficiency aside, the lambda-less versions are preferred because they are generally more concise and easier to read.

### Preferred Alternatives 

:::: 
::: 
``` 
   1 dict(a=str,
   2      b=some_dict.get)
```
:::
::::

## Inappropriate use of Lambda 

There are situations where the usage of Lambda is completely inappropriate. The most inappropriate usage is where a lambda is used to create a named function. Especially when that named function uses recursion.

### Dubious Way 

:::: 
::: 
``` 
   1 bstr = lambda n, l=16: n<0 and binarystr((2L<<l)+n) or n and bstr(n>>1).lstrip('0')+str(n&1) or '0'
```
:::
::::

### The Problem 

This code was presented on comp.lang.python as a solution to \"How do I turn a number into a string of 1\'s and 0\'s. The person who posted it copied it verbatim out of the python cookbook, and didn\'t realise there were significant problems with it.

The code is compressed to the level that it is practically impossible at a first glance to realise if there is anything wrong with it at all. Lets break it down to see the errors. Rewritten as a real function.

:::: 
::: 
``` 
   1 def bstr(n, length=16):
   2     if n == 0:
   3         return '0'
   4     if n<0:
   5         return binarystr((long(2)<<length)+n)
   6     return bstr(n>>1).lstrip('0') + str(n&1)
```
:::
::::

The code calls itself by the wrong name in the if n\<0 branch! It calls \'binarystr\' recursively instead of \'bstr\'.

### Preferred Alternatives 

Don\'t give a lambda a name, even if it only has localised and limited usage. If it needs to be given a name, it has a right to be a normal function. Use \'def\' and make a named function.

Don\'t write lambdas that use \'and\' and \'or\' with shortcut evaluation in order to return the correct value. The example presented is a good indication of why that can lead to subtly buggy code. Instead, use if statements, and your code will be more readable, and you will be able to spot bugs far more easily.

## Overuse of Regular Expressions 

Regular Expressions provde a powerful tool for doing complicated string searches. However, for simple string searches, regular expressions are often overkill.

(Note that such overuse of regular expressions is often the result of converting Perl code to Python code.)

### Dubious Way 

:::: 
::: 
``` 
   1 matcher = re.compile(r'defg')
   2 if matcher.search(s):
   3     do_something()
```
:::
::::

:::: 
::: 
``` 
   1 matcher = re.compile(r'(\S+)')
   2 words = matcher.findall(s)
```
:::
::::

### The Problem 

For simple tasks, using a regular expression can add unnecessary overhead from compiling the regular expression and using the match object to search. When applicable, using string methods can often be faster and more concise.

### Preferred Alternatives 

:::: 
::: 
``` 
   1 if 'defg' in s:
   2     do_something()
```
:::
::::

Note that in pre-2.3 Pythons \'in\' only worked with single character strings. In Python 2.3 and above, \'in\' works with multi-character substrings as above.

:::: 
::: 
``` 
   1 words = s.split()
```
:::
::::

## Counting Items without Enumerate 

It is often useful to keep track of the index of an item in an iterable, for example, for reporting the line number of a string in a file. As of Python 2.3 the preferred way to do this is using the builtin enumerate instead of a manually updated count variable. In versions of Python before 2.3, this is actually not all that dubious\... ![;-)](/wiki/europython/img/smile4.png%20";-)")

### Dubious Way 

:::: 
::: 
``` 
   1 count = 0
   2 for item in iterable:
   3     try:
   4         do_something(item)
   5     except Exception:
   6         raise Exception('error on item %r' % count)
   7     count += 1
```
:::
::::

### The Problem 

While timings are comparable, manual update is more verbose and has a greater risk of programming error if the programmer forgets to update the count variable.

### Preferred Alternatives 

[UsingEnumerate](UsingEnumerate):

:::: 
::: 
``` 
   1 for count, item in enumerate(iterable):
   2     try:
   3         do_something(item)
   4     except Exception:
   5         raise Exception('error on item %r' % count)
```
:::
::::

## Premature Optimization 

*Note that this is at the bottom not because it is less significant than any of the other problems but because, unlike the above idioms, is not a problem specific to Python, but a general programming problem.*

Premature Optimization is spending effort on execution efficiency before determining which parts of the code are actually significant to the program efficiency.

### Dubious Way 

This occurs in a variety of contexts, all of which involve spending extra time making code run faster before first writing a simple, concise implementation that produces the correct results.

Example of over-optimizing attribute accesses:

:::: 
::: 
``` 
   1 app = lst.append
   2 for item in iterable:
   3     app(func(item))
```
:::
::::

### The Problem 

While a correctly applied optimization can indeed speed up code, optimizing code that is only seldom used can waste significant development time, and can make code harder to read. Optimizations should only be sought when a programmer has isolated (using a profiler, etc.) a significant bottleneck in program efficiency. Write correct code first, then make it fast (if necessary).

### Preferred Way 

Don\'t optimize until necessary.

Example of non-optimized but more readable attribute access:

:::: 
::: 
``` 
   1 for item in iterable:
   2     lst.append(func(item))
```
:::
::::

*The above examles look equally readable to me. In fact, the binding of a function to an object*

    app = lst.append

enhances readiblity and maintainability if used more than once:

    app("a")
    app("b")

is preferred over

    lst.append("a")
    lst.append("b")

since the binding of lst and append happens twice - copy and paste.
