# KeepingListsInDictionaries

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# Keeping Lists in Dictionaries 

Here\'s a cute technique I saw, for keeping lists inside dictionaries.

If you have a dictionary with list values, you can run into a problem when you need to add an item to a list value- *does the list already exist?*

Usually, we write it out like so:

:::: 
::: 
``` 
   1 def add_value_to_keys_list(dict_, key, value):
   2     if key not in dict_:
   3         dict_[key] = [value]  # Construct list
   4     else:
   5         dict_[key].append(value)  # Append to list
```
:::
::::

This is okay, but we can do even better!

:::: 
::: 
``` 
   1 def add_value_to_keys_list(dict_, key, value):
   2     dict_.setdefault(key, []).append(value)
```
:::
::::

How does it work?

`.setdefault` works like `.get`, except that when the item isn\'t found, the default isn\'t only *returned,* but they key is *set* to the default as well.

So, in effect, the line means, \"Look in the dictionary for the key. If it\'s *there,* return it\'s associate. If it\'s *not there,* set it\'s associate to `[]`, and *then* return it\'s new associate. The associate is (surprise, surprise) - a *list.* Now, append the value to the list.\"

Cute!
