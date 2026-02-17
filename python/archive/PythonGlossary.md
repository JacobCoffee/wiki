# PythonGlossary

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# Python Glossary 

If you know a term you\'d like defined, simply enter it with `???`{.backtick} for the definition, then subscribe to updates to this page (you\'ll need to set up a profile on the [UserPreferences](./UserPreferences.html) page). Someone will come along and complete it and you\'ll be reminded to check back when you are notified of changes to this page.

A [symbol glossary](attachments/PythonGlossary/PySymbols.html "symbol glossary") is also available.

------------------------------------------------------------------------

## A-M 

- **Attribute** - Values associated with an individual object. Attributes are accessed using the \'dot syntax\': *a.x* means fetch the x attribute from the \'a\' object.

- **BDFL** - Acronym for \"Benevolent Dictator For Life\" - a.k.a. [Guido van Rossum](http://www.python.org/~guido/), Python\'s primary creator, figurehead and decision-maker.

- **byte code** - The internal representation of a Python program in the interpreter. The byte code is also cached in .pyc and .pyo files so that executing the same file is faster the second time (the step of compilation from source to byte code can be saved). This \"intermediate language\" is said to run on a \"virtual machine\" that calls the subroutines corresponding to each bytecode.

- **class** - A template for creating user-defined objects. Class definitions normally contain method definitions that operate on instances of the class.

- **coercion** - The implicit conversion of an instance of one type to another during an operation which involves two arguments of the same type. For example, `int(3.15)`{.backtick} converts the floating point number to the integer, 3, but in `3 + 4.5`{.backtick}, each argument is of a different type (one int, one float), and both must be converted to the same type before they can be added or it will raise a TypeError. Coercion between two operands can be implicitly invoked with the coerce builtin function; thus, `3 + 4.5`{.backtick} is equivalent to `operator.add(*coerce(3, 4.5)`{.backtick}) and results in `operator.add(3.0, 4.5)`{.backtick} which is of course 7.5. Without coercion, all arguments of even compatible types would have to be normalized to the same value by the programmer, e.g., `float(3) + 4.5`{.backtick} rather than just `3 + 4.5`{.backtick}.

- **complex number** - An extension of the familiar real number system in which all numbers are expressed as a sum of a real part and an imagary part. Imaginary numbers are real multiples of the imaginary unit, often written `i`{.backtick} in mathematics or `j`{.backtick} in engineering. Python has builtin support for complex numbers, which are written with this latter notation; the imaginary part is written with a `j`{.backtick} suffix, e.g., `3+1j`{.backtick}. To get access to complex equivalents of the `math`{.backtick} module, use `cmath`{.backtick}. Use of complex numbers is a fairy advanced mathematical feature; if you\'re not aware of a need for complex numbers, it\'s almost certain you can safely ignore them.

- **conversion** - The invocation of a well-defined mechanism from of transforming an instance of one type of object to an instance of another; for example, `int('3')`{.backtick} will convert a string (\'3\') to an int (3).

- **decorator** - A function that modifies another function or method. Its return value is typically a callable object, possibly the original function, but most often another function that modifies the original function\'s behavior in some fashion.

- **descriptor** - Any object that defines the methods `__get__()`{.backtick}, `__set__()`{.backtick}, or `__delete__()`{.backtick}. When a class attribute is a descriptor, its special binding behavior is triggered upon attribute lookup. Normally, writing `a.b`{.backtick} looks up the object `b`{.backtick} in the class dictionary for `a`{.backtick}, but if `b`{.backtick} is a descriptor, the defined method gets called. Understanding descriptors is a key to a deep understanding of Python because they are the basis for many features including functions, methods,properties, class methods, static methods, and reference to super classes.

- **dictionary** - A built-in Python data type composed of arbitrary keys and values; sometimes called a \"hash\" or a \"hash map\" in other languages, although this is technically a misnomer (hashing is one way to implement an associative array but not the only way). The use of `dict`{.backtick} much resembles that for `list`{.backtick}, but the keys can be any object with a `__hash__`{.backtick} function, not just integers starting from zero. Examples: `d = {'A':65, 'B':66}`{.backtick}, `d = dict([('A', 65), ('B', 66)])`{.backtick}, `d['C'] = 67`{.backtick}

<!-- -->

- **docstring** - A string that appears as the lexically first expression in a module, class definition or function/method definition is assigned as the `__doc__` attribute of the object where it is available to documentation tools or the `help()` builtin function.

- **duck typing** - From the \"If it walks, talks, and looks like a duck, then it\'s a duck\" principle. Python uses duck typing in that if an object of some user-defined type exhibits all of the expected interfaces of some type (say the string type), then the object can be treated as if it really were of that type.

- **dynamic typing** - A style of typing of variables where the type of objects to which variables are assigned can be changed merely by reassigning the variables. Python is dynamically typed. Thus, unlike as in a statically typed language such as C, a variable can first be assigned a string, then an integer, and later a list, just by making the appropriate assignment statements. This frees the programmer from managing many details, but does come at a performance cost.

- **EAFP** - Acronym for the saying it\'s \"Easier to Ask for Forgiveness than Permission\". This common Python coding style assumes the existence of valid keys or attributes and catches exceptions if the assumption proves false. This clean and fast style is characterized by the presence of many `try`{.backtick} and `except`{.backtick} statements. The technique contrasts with the **LBYL** style that is common in many other languages such as C.

- **EIBTI** - Acronym for \"Explicit Is Better Than Implicit\", one of Python\'s design principles, included in the **Zen of Python**.

- **exception** ???

- **first-class object** A first class object in a programming language is a language object that can be created dynamically, stored in a variable, passed as a parameter to a function and returned as a result by a function (from [http://www.cs.unm.edu/\~crowley/phdExams/1997xfall/pl.html](http://www.cs.unm.edu/~crowley/phdExams/1997xfall/pl.html)). In Python, practically all objects are first-class, including functions, types, and classes.

- **function** - A block of code that is invoked by a \"calling\" program, best used to provide an autonomous service or calculation.

- **generator function** - A function that returns a **generator** **iterator**. Its definition looks like a normal function definition except that it uses the keyword `yield`{.backtick}. Generator functions often contain one or more `for`{.backtick} or `while`{.backtick} loops that `yield`{.backtick} elements. The function execution is stopped at the `yield`{.backtick} keyword (returning the result) and its resumed there when the next element is requested (e.g., by the builtin function `next()`{.backtick}). For details see PEP 0255 and PEP 0342.

- **generator** - The common name for a generator **iterator**. The type of iterator returned by a generator function or a generator expression.

- **global interpreter lock** or **GIL** - the lock used by Python threads to assure that only one thread can be run at a time. This simplifies Python by assuring that no two processes can access the same memory at the same time. Locking the entire interpreter makes it easier for the interpreter to be multi-threaded, at the expense of some parallelism on multi-processor machines. Efforts have been made in the past to create a \"free-threaded\" interpreter (one which locks shared data at a much finer granularity), but performance suffered in the common single-processor case. See [GlobalInterpreterLock](GlobalInterpreterLock).

- **greedy regular expressions** - Regular expressions which match the longest string possible. The `*`, `+` and `?` operators are all greedy. Their counterparts `*?`, `+?` and `??` are all non-greedy (match the shortest string possible).

- **hash** - A number used to correspond to objects, usually used for \'hashing\' keys for storage in a hash table. Hashing in Python is done with the builtin *hash* function

- **hash table** - An object that maps more-or-less arbitrary keys to values. Dictionaries are the most visible and widely used objects that exhibit this behavior.

- **hashable** - An object is hashable if it is immutable (ints, floats, tuples, strings, etc) or user-defined classes that define a `__hash__` method.

- **id** - `id` is a built-in function which returns a number identifying the object, referred to as the object\'s id. It will be unique during the lifetime of the object, but is very often reused after the object is deleted.

- **IDLE** - an Integrated Development Environment for Python. IDLE is a basic editor and intepreter environment that ships with the standard distribution of Python. Good for beginners and those on a budget, it also serves as clear example code for those wanting to implement a moderately sophisticated, multi-platform GUI application.

- **immutable** - An object with fixed value. Immutable objects include numbers, strings and tuples. Such an object cannot be altered. A new object has to be created if a different value has to be stored. They play an important role in places where a constant hash value is needed such as the keys of a **dictionary**.

- **integer division** - Mathematical division discarding any remainder, for example 3 // 2 returns 1, in contrast to the 1.5 returned by float division. Also called \"floor division\". When dividing two integers the outcome will always be another integer (having the floor function applied to it). However, if one of the operands is another numeric type (such as a float), the result will be coerced (see coercion) to a common type. For example, an integer divided by a float will result in a float value. Integer division can be carried out by using the \'//\' operator instead of the \'/\' operator (used for \"true division\").

- **interactive** - Python has an interactive interpreter which means that you can try out things and directly see its result. To use it, launch `python3`{.backtick} with no arguments. A very powerful way to test out new ideas, inspect libraries (remember `x.__doc__`{.backtick} and `help(x)`{.backtick}) and improve programming skills.

- **interpreted** - Python is an interpreted language (like Perl), as opposed to a compiled one (like C). This means that the source files can be run directly without first creating an executable which is then run. Interpreted languages typicaly have a shorter development/debug cycle than compiled ones, though their programs generally also run more slowly. See also **interactive**.

- **iterable** - A container object capable of returning its members one at a time. Examples of iterables include all sequence types (`list`{.backtick}, `str`{.backtick}, `tuple`{.backtick}, etc.) and some non-sequence types like `dict`{.backtick} and `file`{.backtick} and objects of any classes you define with an `__iter__`{.backtick} or `__getitem__`{.backtick} method. Iterables can be used in a `for`{.backtick} loop and in many other places where a sequence is needed (zip(), map(), \...). When an **iterable** object is passed as an argument to the builtin function `iter()`{.backtick}, it returns an **iterator** for the object. This iterator is good for one pass over the set of values. When using iterables, it is usually not necessary to call `iter()`{.backtick} or deal with iterator objects yourself - the `for`{.backtick} statement does that automatically for you, creating a temporary unnamed variable to hold the iterator for the duration of the loop. See also **iterator**, **sequence**, **generator** and **reiterable**.

- **iterator** - An object representing a stream of data. Repeated calls to the iterator\'s `next()`{.backtick} method return successive items in the stream. When no more data is available a `StopIteration`{.backtick} exception is raised instead. At this point the iterator object is exhausted and any further calls to its `next()`{.backtick} method just raise `StopIteration`{.backtick} again. Iterators are required to have an `__iter__()`{.backtick} method that returns the iterator object itself so every **iterator** is also **iterable** and may be used in most places where other iterables are accepted. One notable exception is code that attempts multiple iteration passes. A container object (e.g. a `list`{.backtick}) produces a fresh new iterator each time you pass it to the `iter()`{.backtick} function or use it in a `for`{.backtick} loop. Attempting this with an iterator will just return the same exhausted iterator object from the second iteration pass and on, making it appear like an empty container.

- **LBYL** - Look before you leap. This coding style explicitly tests for pre-conditions before making calls or lookups. This style contrasts with the **EAFP** approach and is characterized the presence of many `if`{.backtick} statements.

- **list** - A built-in Python datatype, which is a **mutable** sorted **sequence** of values. Note that only sequence itself is mutable; it can contain **immutable** values like strings and numbers. Any Python **first-class object** can be placed in a tuple as a *value*.

- **list comprehension** - A neat syntactical way to process elements in a sequence and return a list with the results. `result = ["0x%02x" % x for x in range(256) if x % 2 == 0]`{.backtick} generates a list of strings containing hex numbers (0x..) that are even and in the range from 0 to 255. The `if`{.backtick} part is optional\' all elements are processed when it is omitted.

- **mapping** - A container object (such as `dict`{.backtick}) that supports arbitrary key lookups using `__getitem__`{.backtick}.

- **metaclass** - The class of a class. Class definitions create a class name, a class dictionary, and a list of base classes. The metaclass is responsible for taking those three arguments and creating the class. Most object oriented programming languages provide a default implementation. What makes Python special is that it is possible to create custom metaclasses. Most users never need this tool, but when the need arises, metaclasses can provide powerful, elegant solutions. They have been used for logging attribute access, adding thread-safety, tracking object creation, implementing singletons, and many other tasks.

- **method** ???

- **module** ???

- **mutable** - Mutable objects can change their value but keep their `id()`{.backtick}. See also **immutable**.

## N-Z 

- **namespace** - The place where a variable is stored in a Python program\'s memory. Namespaces are implemented as a dictionary. There are the local, global and builtins namespaces and the nested namespaces in objects (in methods). Namespaces support modularity by preventing naming conflicts. For instance, `__builtins__.open()`{.backtick} and `os.open()`{.backtick} are distinguished by their namespaces. Namespaces also aid readability and maintainabilty by making it clear which modules implement a function. For instance, writing `random.seed()`{.backtick} and `itertools.izip()`{.backtick} will make it clear that those functions are implemented by the `random`{.backtick} and `itertools`{.backtick} modules respectively.

- **nested scope** - The ability to refer to a variable in an enclosing definition. For instance, a function defined inside another function can refer to variables in the outer function. Note that nested scopes work only for reference and not for assignment which will always write to the innermost scope. In contrast, local variables both read and write in the innermost scope. Likewise, global variables read and write to the global namespace.

- **object** - Any data with state (attributes or value) and defined behavior (methods).

- **object oriented** - Programming typified by a data-centered (as opposed to a function-centered) approach to program design.

- **pie syntax** - A syntax using \'@\' for decorators that was committed to an alpha version of Python 2.4. So called because the \'@\' vaguely resembles a pie and the commital came on the heels of the Pie-thon at an open source conference in 2004.

- **property** - a built-in data type, used to implement managed (computed) attributes. You assign the property object created by the call **property**( *optional-args* **)** to a class attribute. When the attribute is accessed through an *instance* of the class, it dispatches functions that implement the managed-attribute operations, such as get-the-value and set-the-value.

- **Python 3000** - older name for [Python 3](https://www.python.org/dev/peps/pep-3000/). An update to the language that allowed breaking changes to be made in order to add features and improve various functionality.

- **regular expression** - A formula for matching strings that follow some pattern. Regular expressions are made up of normal characters and *metacharacters*. In the simplest case, a regular expression looks like a standard search string. For example, the regular expression \"testing\" contains no metacharacters. It will match \"testing\" and \"123testing\" but it will not match \"Testing\". Metacharacters match some expressions like \'.\' metacharacter match any single character in a search string.

- **reiterable** - An iterable object which can be iterated over multiple times. Reiterables must not return themselves when used as an argument to iter().

- **sequence** - An **iterable** that also supports random access using `__getitem__`{.backtick} and `len`{.backtick}. Some builtin sequence types are `list`{.backtick}, `str`{.backtick}, `tuple`{.backtick}, and `unicode`{.backtick}. Note that `dict`{.backtick} also supports these two operations but is considered a **mapping** rather than a sequence because the lookups use arbitrary keys rather than consecutive numbers and it should be considered unsorted.

- **`__slots__`** - A declaration inside a class that saves memory by pre-declaring space for instance attributes and eliminating instance dictionaries. Though popular, the technique is somewhat tricky to get right and is best reserved for rare cases where there are large numbers of instances in a memory critical application.

- **static typing** - A style of typing of variables common to many programming languages (such as C) where a variable, having been assigned an object of a given type, cannot be assigned objects of different types subsequently.

- **string** - One of the basic types in Python that store text. In Python 3, stores text as a sequence of Unicode code points.

- **triple-quoted string** - A string that is bounded by three instances of either the double quote mark (\") or the single quote mark (\'). For instance:

      '''This is such a string'''

  They are useful for multiple reasons: they allow you to include both single and double quotes within a string quite easily, and they can span multiple lines without the use of line-continuation characters (very useful in [docstrings](PythonGlossary#docstring)).

- **tuple** - (pronounced TUH-pul or TOO-pul) A built-in Python datatype, which is an **immutable** ordered **sequence** of values. Note that only the sequence itself is immutable. If it contains a **mutable** value such as a **dictionary**, that value\'s content may be changed (e.g. adding new key/value pair). Any Python **first-class object** can be placed in a tuple as a *value*.

- **type** - A \"sort\" or \"category\" of data that can be represented by a programming language. Types differ in their properties (such as mutability and immutability), the methods and functions applicable to them, and in their representations. Python includes, among others, the string, bytes, integer, long, floating point, list, tuple, and dictionary types.

- **whitespace** - The unconventional use of space characters (\' \') to control the flow of a program. Instead of a loosely-enforced ideal, this is an integral part of Python syntax. It\'s a tradeoff between readability and flexibility in favor of the former.

- **Zen of Python** - listing of Python design principles and philosophies that are helpful in understanding and using the language effectively. The listing can be found by typing \"import this\" at the interactive prompt.

## misc

- **\>\>\>** - The typical Python prompt of the interactive shell. Often seen for code examples that can be tried right away in the interpreter. Not to be confused with \"\>\" symbols used for the indentation of cited material on email lists.

# Historical information 

Previous versions of this page were mostly written before Python 3 was commonly used. For historical interest or Python 2-specific definitions, please see [previous page revisions](https://wiki.python.org/moin/PythonGlossary?action=recall&rev=36).

------------------------------------------------------------------------

[CategoryDocumentation](CategoryDocumentation)
