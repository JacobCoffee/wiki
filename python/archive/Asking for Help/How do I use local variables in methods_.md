# Asking for Help/How do I use local variables in methods?

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# Local Variables in Functions 

\"How do I use local variables in a function within a class? (I do not want to use self.x, as this makes the instance have variables. I want variables local to my function, that get destroyed at the end of it.) I can only think of using del at the end of the function, is there a better way?\"

Local variables only ever define names within their scope, and these names do not appear in the surrounding class or module. Consider this function:

    def f(x, y, z):
        a = x + y + z
        print "Done!"
        return a

The names `x`{.backtick}, `y`{.backtick} and `z`{.backtick} come to life as the function `f`{.backtick} is called, pointing to the objects supplied as arguments to `f`{.backtick}. When `f`{.backtick} is finished executing, the names `x`{.backtick}, `y`{.backtick} and `z`{.backtick} are forgotten, but the objects they pointed to might still be around, of course. Here, we use a variable `a`{.backtick} in the function; this also gets forgotten at the end of the function, but the object `a`{.backtick} pointed to is returned to the caller.

In short, you always get local variables in Python unless you use the `global`{.backtick} keyword. You can always use `del`{.backtick} to make Python forget names, but this is done automatically at the end of function execution for all names in the local scope of that function.

------------------------------------------------------------------------

[CategoryAskingForHelp](CategoryAskingForHelp) [CategoryAskingForHelpAnswered](CategoryAskingForHelpAnswered)
