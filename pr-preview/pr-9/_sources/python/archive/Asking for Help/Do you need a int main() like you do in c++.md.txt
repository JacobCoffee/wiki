# Asking for Help/Do you need a int main() like you do in c++

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

## Do you need a int main() like you do in c++ here? 

**I am a Newbie to python and need to know if there is a int main that is the body of the program.**

There\'s no requirement to have a `main`{.backtick} function in Python, but there is the concept of a main module. But let us first consider what happens when you run a Python file.

Consider a Python file called `program.py`{.backtick}. If we run this file, the content of the file is executed. So you may have some functions and classes and perhaps some normal statements as follows:

:::: 
::: 
``` 
class C:
    def method(self, arg):
        ...

def func(x, y, z):
    ...

answer = func(1, 2, 3)
print "Answer is", answer
```
:::
::::

Here, the class `C`{.backtick} gets created, as does `method`{.backtick} inside the class, and the function `func`{.backtick} gets created. At this point, no code inside `method`{.backtick} or `func`{.backtick} is run, but these things are now defined in the module. Then, the statements at the end are run, and the first one does call `func`{.backtick}. Finally, a `print`{.backtick} statement is executed.

Now, if this file were to import other modules, the content of those modules would be executed in the same way. So if we add the following to `program.py`{.backtick}\...

:::: 
::: 
``` 
import mymodule
```
:::
::::

\...then that module, perhaps defined in `mymodule.py`{.backtick}, would be loaded and run in the same way. Let\'s say that the module is written as follows:

:::: 
::: 
``` 
def modfunc(a, b):
    ...

print test_the_function(123, 456)
```
:::
::::

Even if you import `mymodule`{.backtick}, with the code as it is, the `modfunc`{.backtick} function will be defined, but then the `print`{.backtick} statement will be run and you\'ll get something printed out, even though that probably isn\'t what you want.

So what people do in Python is this:

:::: 
::: 
``` 
def modfunc(a, b):
    ...

if __name__ == "__main__":
    print test_the_function(123, 456)
```
:::
::::

When `mymodule`{.backtick} is imported, the code is run as before, but when we get to the `if`{.backtick} statement, Python looks to see what name the module has. Since the module is imported, we know it by the name used when importing it, so `__name__`{.backtick} is `mymodule`{.backtick}. Thus, the `print`{.backtick} statement is never reached.

However, we might want to be able to run `mymodule.py`{.backtick} directly. If we do that, the code is run as before, but at the `if`{.backtick} statement when Python looks for the module name, since the code was not imported but actually run directly, the value of `__name__`{.backtick} will be `__main__`{.backtick}. Thus, the `print`{.backtick} statement will be reached and you\'ll be able to test the code.

So in summary, by testing the `__name__`{.backtick} in a Python file, you can find out whether the file is the one being run directly because it will have the value `__main__`{.backtick}. Otherwise, it will have another value. Some people tend to write code like the following to emulate a `main`{.backtick} function:

:::: 
::: 
``` 
def main():
    ...

if __name__ == "__main__":
    main()
```
:::
::::

But there\'s really no requirement to have such a function: it\'s just a convention.

------------------------------------------------------------------------

[CategoryAskingForHelp](CategoryAskingForHelp) [CategoryAskingForHelpAnswered](CategoryAskingForHelpAnswered)
