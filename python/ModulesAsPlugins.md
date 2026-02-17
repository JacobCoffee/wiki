# ModulesAsPlugins

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

Here\'s how to find all the modules in some directory, and import them.

## Finding Modules in a Directory 

Is there a better way than just listing the contents of the directory, and taking those tiles that end with \".pyc\" or \".py\"..?

But perhaps there isn\'t.

:::: 
::: 
``` 
   1 import os
   2 
   3 def find_modules(path="."):
   4     """Return names of modules in a directory.
   5 
   6     Returns module names in a list. Filenames that end in ".py" or
   7     ".pyc" are considered to be modules. The extension is not included
   8     in the returned list.
   9     """
  10     modules = set()
  11     for filename in os.listdir(path):
  12         module = None
  13         if filename.endswith(".py"):
  14             module = filename[:-3]
  15         elif filename.endswith(".pyc"):
  16             module = filename[:-4]
  17         if module is not None:
  18             s.add(module)
  19     return list(modules)
```
:::
::::

## Importing the Modules 

How do you import a module, once you have it\'s name?

With the [ImpModule](ImpModule)! It dynamically loads named modules.

:::: 
::: 
``` 
   1 import imp
   2 
   3 def load_module(name, path=["."]):
   4     """Return a named module found in a given path."""
   5     (file, pathname, description) = imp.find_module(name, path)
   6     return imp.load_module(name, file, pathname, description)
   7 
   8 modules = [load_module(name) for name in find_modules()]
```
:::
::::

## Finding the Things Inside a Module 

Once you have your module, you can look inside it, with `.__dict__`.

:::: 
::: 
``` 
   1 module.__dict__
```
:::
::::

## Finding Functions Within a Module 

We just look for dictionary values that are of type `types.FunctionType`.

:::: 
::: 
``` 
   1 def functions_in_module(module)
   2     functions = []
   3     for obj in module.__dict__.values():
   4         if isinstance(obj, types.FunctionType):
   5             functions.append(obj)
   6     return functions
```
:::
::::

## See Also 

The [DocXmlRpcServer](DocXmlRpcServer) page includes code demonstrating the use of these techniques.

# Discussion 

I got this error when executing find_modules() in a package directory. That is the directory contained an ` __init.py__` file:

      File "C:\Python254\lib\site-packages\joedorocak\find_modules.py", line 27, in find_modules
        s.add(module)
    NameError: global name 's' is not defined

It looks to me like s needs to be initialized (some place near \"modules = set()\"). I\'m not sure what the protocol is here, so I\'m just going to leave this comment in the discussion.

Here\'s what seems to work for me. I got rid of \'s\' altogether.

    def find_modules(path="."):
        """Return names of modules in a directory.

        Returns module names in a list. Filenames that end in ".py" or
        ".pyc" are considered to be modules. The extension is not included
        in the returned list.
        """
        modules = set()
        for filename in os.listdir(path):
            module = None
            if filename.endswith(".py"):
                module = filename[:-3]
            elif filename.endswith(".pyc"):
                module = filename[:-4]
            if module is not None:
                modules.add(module)
        return list(modules)

All the best,

[JoeDorocak](./JoeDorocak.html)
