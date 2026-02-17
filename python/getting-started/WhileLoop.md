# WhileLoop

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# While loops 

## Usage in Python 

- When do I use them?

*While* loops, like the [ForLoop](ForLoop), are used for repeating sections of code - but unlike a *for* loop, the *while* loop will not run *n* times, but until a defined condition is no longer met. If the condition is initially false, the loop body will not be executed at all.

As the *for* loop in Python is so powerful, *while* is rarely used, except in cases where a user\'s input is required\*, for example:

    n = raw_input("Please enter 'hello':")
    while n.strip() != 'hello':
        n = raw_input("Please enter 'hello':")

However, the problem with the above code is that it\'s wasteful. In fact, what you will see a lot of in Python is the following:

    while True:
        n = raw_input("Please enter 'hello':")
        if n.strip() == 'hello':
            break

As you can see, this compacts the whole thing into a piece of code managed entirely by the *while* loop. Having *True* as a condition ensures that the code runs until it\'s broken by `n.strip()` equaling `'hello'`.

- Another version you may see of this type of loop uses `while 1` instead of `while True`. In older Python versions *True* was not available, but nowadays is preferred for readability.

  - [Starting with Py2.3](https://docs.python.org/3.0/whatsnew/2.3.html#optimizations), the interpreter optimized `while 1` to just a single jump. Using *1* was minutely faster, since *True* was not a keyword and might have been given a different value, which the interpreter had to look up, as opposed to loading a constant. As a programmer, it is up to you which style to use - but always remember that readability is important, and that while speed is also important, readability trumps it except in cases where timings are significantly different.

  - [Starting in Python 3](https://docs.python.org/3.0/whatsnew/3.0.html#changed-syntax), `True`, `False`, and `None` are keywords, so using `while 1` no longer provides the tiny performance benefit used to justify it in earlier versions.

  - See also: [http://stackoverflow.com/questions/3815359/while-1-vs-for-whiletrue-why-is-there-a-difference](http://stackoverflow.com/questions/3815359/while-1-vs-for-whiletrue-why-is-there-a-difference)

\* If this were Wikipedia, the above statement would be followed by \"citation needed.\"
