# Asking for Help/how do I work through an array and change a particular element?

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# I want to change an element in an array during a loop: 

     lines=open("/etc/fstab","r").readlines()
     for line in lines:
        if line.split()[1]=="/": 
           line="# "+line

Now that does not change the contents of the array (commenting out a particular line in the file). I know you can easily make a loop counter, an d add i=i+1, but isn\'t there a better way?

== Answer== Try using the enumerate builtin.

     lines=open("/etc/fstab","r").readlines()
     for index,line in enumerate(lines):
        if line.split()[1]=="/": 
           lines[index] ="# "+line

::: note
When *answering* questions, add the [CategoryAskingForHelpAnswered](CategoryAskingForHelpAnswered) category when saving the page. This will move the link to this page from the questions section to the answers section on the [Asking for Help](./Asking(20)for(20)Help.html) page.
:::

------------------------------------------------------------------------

[CategoryAskingForHelp](CategoryAskingForHelp) [CategoryAskingForHelpAnswered](CategoryAskingForHelpAnswered)
