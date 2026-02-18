# KeyError

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

Python raises a **KeyError** whenever a dict() object is requested (using the format `a = adict[key]`) and the key is not in the dictionary.

If you don\'t want to have an exception but would rather a default value used instead, you can use the `get()`{.backtick} method:

:::: 
::: 
``` 
   1 default = 'Scruffy'
   2 a = adict.get('dogname', default)
```
:::
::::

Even more handy is somewhat controversially-named `setdefault(key, val)`{.backtick} which sets the value of the key only if it is not already in the dict, and returns that value in any case:

:::: 
::: 
``` 
   1 default = 'Scruffy'
   2 dog_owned_by = {'Peter': 'Furry', 'Sally': 'Fluffy'}
   3 
   4 dogs = []
   5 for owner in ('Peter', 'Sally', 'Tim'):
   6     dogs.append(dog_owned_by.setdefault(owner, default))
   7 
   8 # dogs == ['Furry', 'Fluffy', 'Scruffy']
   9 # dog_owned_by == {'Tim': 'Scruffy', 'Peter': 'Furry', 'Sally': 'Fluffy'}
```
:::
::::
