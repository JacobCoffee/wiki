# MultiLineLambda

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# Main idea 

Multi-statement anonymous functions

## Proposal details 

Various syntaxes have been proposed:

### Whitespace Delimited 

    this_one_takes_a_func_arg(
        "foo",
        42,
        def (*args, **kwargs):
            """Does useful and interesting things, I promise"""
            call_a_func()
            do_some_stuff()
            print("print")
            return "foo", # This is potentially ambiguous
        boop,
    )

### Brace Delimited 

    this_one_takes_a_func_arg(
        "foo",
        42,
        def (*args, **kwargs): {
            """Does useful and interesting things, I promise"""
            call_a_func()
            do_some_stuff()
            print("print")
            return "foo"
        },
        boop,
    )

### Keyword Delimited 

    this_one_takes_a_func_arg(
        "foo",
        42,
        def (*args, **kwargs):
            """Does useful and interesting things, I promise"""
            call_a_func()
            do_some_stuff()
            print("print")
            return "foo"
        undef, # potentially requires a new reserved word
        boop,
    )

### Arrow Function 

    this_one_takes_a_func_arg(
        "foo",
        42,
        (*args, **kwargs) => (
            """Does useful and interesting things, I promise"""
            call_a_func()
            do_some_stuff()
            print("print")
            return "hello"
        ),
        boop,
    )

# Main arguments 

## Supporting 

Many programming languages (e.g. C#, C++, Java, [JavaScript](./JavaScript.html), PHP, Ruby, Rust) support [Anonymous Functions](https://en.wikipedia.org/wiki/Anonymous_function). Programmers who work in other languages might reasonably expect to be able to use similar constructs in Python. However, the only way to implement anonymous functions in Python is using lambda, which is restricted to a body consisting of a single expression. This severely limits the expressiveness of anonymous functions and restricts the cases where it is applicable.

Anonymous functions are an important part of functional programming languages and other languages with first-class functions. Python provides many other functional constructs (e.g. list comprehensions, match) and the standard library provides many functions that support a functional paradigm (e.g. filter, map). However, there is no support for complex (multi-statement) anonymous functions.

## Against 

### Legibility 

When the function stands on its own, it can be indented like normal Python code. The code for both the function and the expression where the function is used will likely become clearer by being separated like this. It is for example much easier to see how many arguments are being passed in the function call.

In future if more code needs to be added to the body of the function then the expression with the inline function would become messier and harder to read. The restriction of lambda functions to a single expression helps to prevent this by drawing a clear line around when the inline function is becoming too complicated and should rather be factored out as an ordinary named function.

### Names are forced comments 

With an inline multi-line lambda, you probably need a comment summarizing what the function is doing. On the other hand, if you give the function a name, the name can stand in for the comment that you would otherwise be writing.

# Links and references 

## Discussion threads 

- [On the first\~classness of functions](https://discuss.python.org/t/on-the-first-classness-of-functions/12984)

- [Are better lambdas really impossible?](https://discuss.python.org/t/are-better-lambdas-really-impossible/2446)

- [Simple multi-line lambda syntax](https://discuss.python.org/t/simple-multi-line-lambda-syntax/27499)

- [Why not real anonymous functions?](https://discuss.python.org/t/why-not-real-anonymous-functions/44513)

## PEPs 

None.
