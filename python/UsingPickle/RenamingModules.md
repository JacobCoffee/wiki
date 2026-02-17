# UsingPickle/RenamingModules

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

If you are using pickle to store your data and decide to rename some of the modules in your project, you will have troubles loading old saved pickles. However, this can be solved overloading the load_global method in the default pickle implementation like this:

    import pickle

    try:
        from cStringIO import StringIO
    except ImportError:
        from StringIO import StringIO

    renametable = {
        'old.module': 'new.module',
        'old_name': 'new_name',
        }

    def mapname(name):
        if name in renametable:
            return renametable[name]
        return name

    def mapped_load_global(self):
        module = mapname(self.readline()[:-1])
        name = mapname(self.readline()[:-1])
        klass = self.find_class(module, name)
        self.append(klass)

    def loads(str):
        file = StringIO(str)
        unpickler = pickle.Unpickler(file)
        unpickler.dispatch[pickle.GLOBAL] = mapped_load_global
        return unpickler.load()
