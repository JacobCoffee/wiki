# Jython3000

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# Ideas for backwards incompatible changes in 3.x

It would be good if most of these can have warnings in 2.6

::: 
### Java

- In our core code kill methods that do not take a ThreadState when there is a method that does (mainly in PyObject)
- Kill all of Py.java (It\'s a giant global that we should be able to split up \-- maybe it will just become tiny)
:::

::: 
### Registry

- Kill respectJavaAccessibility
:::

::: 
### Package Cache

- Disable by default, add an easy flag to enable.
:::

::: 
### Proxy generation

- Remove event properties \-- they are arbitrary, hazardous and easy to go wrong with
:::
