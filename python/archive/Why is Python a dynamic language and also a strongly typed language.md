# Why is Python a dynamic language and also a strongly typed language

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

SEE: **[Ten things people want to know about Python](Ten things people want to know about Python)** for more details.

Answer

:   - People often use the term strongly-typed language to refer to a language that is both statically typed (types are associated with a variable declaration \-- or, more generally, the compiler can tell which type a variable refers to, for example through type inference, without executing the program) and strongly-typed (restrictive about how types can be intermingled). So, if you look at dynamic typing and strong-typing as orthogonal concepts, Python can be both dynamically and strongly typed.

Another answer:

- Python is strongly typed as the interpreter keeps track of all variables types. It\'s also very dynamic as it rarely uses what it knows to limit variable usage. In Python, it\'s the program\'s responsibility to use built-in functions like isinstance() and issubclass() to test variable types and correct usage. Python tries to stay out of your way while giving you all you need to implement strong type checking.

And another one:

- In a weakly typed language a compiler / interpreter will sometimes change the type of a variable. For example, in some languages (like [JavaScript](./JavaScript.html)) you can add strings to numbers `'x' + 3`{.backtick} becomes `'x3'`{.backtick}. This can be a problem because if you have made a mistake in your program, instead of raising an exception execution will continue but your variables now have wrong and unexpected values. In a strongly typed language (like Python) you can\'t perform operations inappropriate to the type of the object - attempting to add numbers to strings will fail. Problems like these are easier to diagnose because the exception is raised at the point where the error occurs rather than at some other, potentially far removed, place.

- In a statically typed language, the type of variables must be known (and usually declared) at the point at which it is used. Attempting to use it will be an error. In a dynamically typed language, objects still have a type, but it is determined at runtime. You are free to bind names (variables) to different objects with a different type. So long as you only perform operations valid for the type the interpreter doesn\'t care what type they actually are.

And another:

- In a strongly typed language, you are simply not allowed to do anything that\'s incompatible with the type of data you\'re working with. For example, in a weakly typed language you can typically do `3 + 5 + 7`{.backtick} and get the result `15`{.backtick}, because numbers can be added; similarly, you can often do `'Hello' + 'And' + 'Goodbye'`{.backtick} and get the result `"HelloAndGoodBye"`{.backtick}, because strings support concatenation. But in a strongly-typed language you **can\'t** do `'Hello' + 5 + 'Goodbye'`{.backtick}, because there\'s no defined way to \"add\" strings and numbers to each other. In a weakly typed language, the compiler or interpreter can perform behind-the-scenes conversions to make these types of operations work; for example, a weakly typed language might give you the string `"Hello5Goodbye"`{.backtick} as a result for `'Hello' + 5 + 'Goodbye'`{.backtick}. The advantage to a strongly typed language is that you can trust what\'s going on: if you do something wrong, your program will generate a type error telling you where you went wrong, and you don\'t have to memorize a lot of arcane type-conversion rules or try to debug a situation where your variables have been silently changed without your knowledge.

- In a dynamically typed language, a variable is simply a value bound to a name; the value has a type \-- like \"integer\" or \"string\" or \"list\" \-- but the variable itself doesn\'t. You could have a variable which, right now, holds a number, and later assign a string to it if you need it to change. In a statically typed language, the variable itself has a type; if you have a variable that\'s an integer, you won\'t be able to assign any other type of value to it later. Some statically typed languages require you to write out the types of all your variables, while others will deduce many of them for you automatically. A statically typed language can catch some errors in your program before it even runs, by analyzing the types of your variables and the ways they\'re being used. A dynamically language can\'t necessarily do this, but generally you\'ll be writing unit tests for your code either way (since type errors are a small fraction of all the things that might go wrong in a program); as a result, programmers in dynamic languages rely on their test suites to catch these and all other errors, rather than using a dedicated type-checking compiler.

Real Life Example:

This author ([SkipMontanaro](SkipMontanaro)) used to operate a now defunct concert calendar website. The backend was implemented in Python, but the front end was implemented in [Mason](http://www.masonhq.com), a Perl-based web application platform. One bug which took awhile to figure out was why entering concert dates for the band \"311\" failed. Python was seeing an int instead of a string. It turns out somewhere in the Perl or Mason frontend \"311\" was being converted into an integer.
