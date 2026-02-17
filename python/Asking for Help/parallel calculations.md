# Asking for Help/parallel calculations

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

Hi,

I was wondering which module I should use to parallelise my calculations. In fact I have two Monte Carlo models. Parameters for the models come from a python file but the models do not change the file. They just read some variables and a description of an object to create instances of the object. Each model takes a minimum of 5 minutes of calculation time. And I want to decrease the time and to launch the models in parallel. As far as I understand if I use threading module it will create two threads but because of GIL they will be executed consequently. Am I right? Could you please give me an advice on this?

Thank you! Maxim
