# Decorators

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

See also [PythonDecoratorLibrary](PythonDecoratorLibrary). And apart from decorators in the standard library, there are also lots of PyPI packages with convenient, interesting or novel use cases:

::: {}
  ------------------ -------------------------------------------------------------------------------------------------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------------------------
  **Category**       **Decorator**                                                                                                                                                        **Summary**
  builtin            [\@property](https://docs.python.org/3/library/functions.html?highlight=property#property)                                                                   Turn function into property accessor, also: `@property.setter`{.backtick}
  builtin            [\@classsmethod](https://docs.python.org/3/library/functions.html?highlight=property#classmethod)                                                            Use `cls`{.backtick} instead of `self`{.backtick}
  builtin            [\@staticmethod](https://docs.python.org/3/library/functions.html?highlight=property#staticmethod)                                                           Defines methods without self handle
  stdlib             [\@functools.wraps](https://docs.python.org/3/library/functools.html?highlight=functools#functools.wraps)                                                    Retain modicum of meta infos (`__doc__`{.backtick}) of wrapped function
  stdlib             [\@functools.singledispatch](https://docs.python.org/3/library/functools.html?highlight=functools#functools.singledispatch)                                  Allows for divergent implementations per \@f.register()
  stdlib/backports   [\@functools.lru_cache](https://stackoverflow.com/questions/815110/is-there-a-decorator-to-simply-cache-function-return-values)                              Wrap computationally expensive functions
  stdlib             [\@functools.cmp_to_key](https://docs.python.org/3/library/functools.html?highlight=functools#functools.cmp_to_key)                                          Transform an old-style comparison function to a key function.
  stdlib             [\@functools.total_ordering](https://docs.python.org/3/library/functools.html?highlight=functools#functools.total_ordering)                                  Adds any of the missing lt,le,eq,ge,gt comparison dunder methods
  stdlib             [\@functools.partial](https://docs.python.org/3/library/functools.html?highlight=functools#functools.partial)                                                Prepopulate a couple of function arguments
  stdlib             [\@typing.overload](https://python.readthedocs.io/en/stable/library/typing.html#typing.overload)                                                             Singledispatch based on function parameter or return types
  stdlib             [\@contextlib.contextmanager](https://docs.python.org/3/library/contextlib.html?highlight=decorator#contextlib.contextmanager)                               Uses generator protocol `yield`{.backtick} to turn function into `with`{.backtick}-able context mananger
  stdlib             [\@dataclasses.dataclass](https://docs.python.org/3/library/dataclasses.html?highlight=decorator#dataclasses.dataclass)                                      Adds various "dunder" methods to the class to streamline property access
  stdlib             [\@atexit.register](https://docs.python.org/3/library/atexit.html?highlight=decorator#atexit.register)                                                       Run as shutdown function
  stdlib             [\@abc.ABCMeta.register](https://docs.python.org/3/library/abc.html?highlight=decorator#abc.ABCMeta.register)                                                Turn into abstract base class
  stdlib             [\@enum.unique](https://docs.python.org/3/library/enum.html?highlight=decorator#enum.unique)                                                                 Guarantee unique members in enum class
  stdlib             [\@xmlrpc.register_function](https://docs.python.org/3a/library/xmlrpc.server.html?highlight=decorator#xmlrpc.server.SimpleXMLRPCServer.register_function)   \...
  stdlib             [\@sys.settrace](https://docs.python.org/3/library/sys.html#sys.settrace)                                                                                    Register function as debugger callback
  asyncio            [\@coroutine](https://docs.python.org/3/library/asyncio-task.html?highlight=asyncio%20coroutine#asyncio.coroutine)                                           Outdated scheme for `async def`{.backtick}, deprecated in 3.8
  asyncio            [\@throttle(2,1)](https://pypi.org/project/aiodecorator/)                                                                                                    Reduce invocations per timeframe
  asyncio            [\@exceptionCatcher...](https://hackernoon.com/python-async-decorator-to-reduce-debug-woes-nv2dg30q5)                                                        Log exceptions more instantly
  asyncio            [\@timeit](https://gist.github.com/Integralist/77d73b2380e4645b564c28c53fae71fb)                                                                             Basic benchmarking
  async              [\@async_process](https://pypi.org/project/process-decorator/)                                                                                               make func async and execute in other process
  threading          [\@threaded, \@debug, \@skip_if_env](https://gitlab.com/chadgh/ornamentation)                                                                                Convenient threading wrapper, and testing wrappers
  threading          [\@lock_or_wait](https://pypi.org/project/lockorator/)                                                                                                       Aquire and release locks for functions
  testing            [\@unittest.mock.patch](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.patch)                                                            Override function w/ signature
  testing            [\@wrapt.patch_function_wrapper](http://blog.dscpl.com.au/2015/03/using-wrapt-to-support-testing-of.html)                                                     Override function w/ signature
  debugging          [\@trycatch](https://pypi.org/project/handy-decorators/)                                                                                                     Capture exceptions to the log
  debugging          [\@log_calls](https://pythonhosted.org/log_calls/intro.html)                                                                                                 Record invocations with arguments
  decorator          [\@decorator](https://pypi.org/project/decorator/)                                                                                                           Assists declaring signature-preserving and single dispatch decorators
  decorator          [\@decorator_args](https://pypi.org/project/decorator-args/)                                                                                                 Ease parameterizing decorators themselvess
  decorator          [\@named_decorator](https://github.com/Yelp/named_decorator)                                                                                                 Retain callees\' function name to simplify tracebacks
  decorator          [\@dec.decorator(before=cb,after=cb)](https://pypi.org/project/Easy_Decorator/)                                                                              Craft trivial enter/exit decorator
  decorator          [\@log_call, \@intercept, \@instead, \@before](https://pypi.org/project/pydecor/)                                                                            Simplifies decorator construnction/interactions, parameter handling
  decorator          [undecorated(fn)](https://pypi.org/project/undecorated/)                                                                                                     reversible decoration
  collect            [\@click.option(\"-d\")](https://click.palletsprojects.com/en/7.x/commands/)                                                                                 Argparse alternative
  collect            [\@config_decorator.setting](https://pypi.org/project/config-decorator/)                                                                                     Declarative dict structure for application settings
  collect            [\@regex_decorator.listen](https://github.com/xtream1101/regex-decorator)                                                                                    Register function callbacks for pattern matching
  collect            [\@expose, \@register](https://pypi.org/project/pyplugs/)                                                                                                    Plugin interface/registration
  typing             [\@contract({\"param\":gt(3)})](https://pypi.org/project/contract-decorator/)                                                                                Exhaustive function parameter constraints
  typing             [\@pedantic, \@trace, \@dirty, ...](https://pypi.org/project/pedantic/)                                                                                      Encourages cleaner and better documented code
  typing             [\@Decorator](https://pypi.org/project/classy-decorators/)                                                                                                   OO-style class/method parameters
  typing             [\@mutable, \@final, \@auto_obj](https://pypi.org/project/decorateme/)                                                                                       decorators for str/repr, equality, immutability, and more
  typing             [\@to_string, \@data, \@repeat](https://pypi.org/project/paprika/)                                                                                           Reduces some common boilerplate for methods
  typing             [\@DataAtrribute(\"desc\")](https://pypi.org/project/pyAttributes/)                                                                                          .NET-like attributes
  parameter          [\@curried](https://pypi.org/project/simplecurry/)                                                                                                           Convenient decorator-alternative to partial()
  parameter          [\@attrs](https://www.attrs.org/en/stable/)                                                                                                                  object declarations
  parameter          [\@arg.validate](https://pypi.org/project/python-args/)                                                                                                      simplifies parameter handling/assertion
  flow handling      [\@\_\_main\_\_](Decorators#A__main__)                                                                                                                        Automatically run a function if invocation script
  flow handling      [\@retry(times=2)](http://www.praddy.in/retry-decorator-whitelisted-exceptions/)                                                                              Reinvokes function a few times when encountering (temporary) exceptions, alt: [pypi:retry-decorator](https://pypi.org/project/retry-decorator/)
  flow handling      [\@retry](https://pypi.org/project/retryz/)                                                                                                                  Rerun function in case of exceptions
  flow handling      [\@self](https://pypi.org/project/self/)                                                                                                                     method chaining (fluent interfaces)
  monkeypatching     [\@inject(modules...)](https://fossil.include-once.org/modseccfg/wiki/@inject)                                                                               Shorthand assignment to modules/objects
  monkeypatching     [\@monkeybiz.patch(fn)](https://github.com/theatlantic/python-monkey-business)                                                                               Swap out function in object, retain reference to original
  ------------------ -------------------------------------------------------------------------------------------------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------------------------
:::

(Note: Not sure this is going anywhere. Relisting builtins is somewhat redundant, but on topic here. The focus is novel/interesting decorators in the wild. The categorization probably won\'t hold up; and probably going to split this up into sections.)

### Other decorator links 

- [Awesome Python decorator collection (GitHub)](https://github.com/lord63/awesome-python-decorator)

- [PyPI decorator packages](https://pypi.org/search/?q=decorator) (gets interesting around page 10)

## \_\_main\_\_ 

This decorator does not alter a function, but causes it to be executed if `__name__ == '__main__'`{.backtick}. This provides an experimental cleaner syntax to the traditional way of bootstrapping a python script. This should not be used on class methods.

The function gets a copied list of sys.argv arguments.

:::: 
::: 
``` 
   1 def __main__(func):
   2 
   3     if __name__ == "__main__":
   4         import sys, os
   5         args = sys.argv[:]
   6         args[0] = os.path.abspath(args[0])
   7         func(args)
```
:::
::::
