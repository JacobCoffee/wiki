# SummerOfCode/WebIDE

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

There\'s no specific set of requirements or even a specific goal for a web-based Python IDE, but here are some thoughts you might find interesting in shaping a proposal:

- I think this is most interesting when targetting a relatively new Python programmer. Experienced programmers already have tools. If you can make the IDE useful for people using external editors, that might be a good idea, and will include the potential audience.

- The environment should be basically framework neutral. It might (and probably should) use some framework underneath, but it\'s primary UI doesn\'t need to integrate in any framework. Also, there\'s problems with a framework leaking into project. If you use

  version 2.0 of [FooFramework](./FooFramework.html), will a person developing a web application in 1.0 of [FooFramework](./FooFramework.html) be able to use your IDE?

- Developing web applications using a web-based IDE is probably the most obvious use for this, but there\'s no reason it can\'t be useful for any Python project.

- There are some significant limitations to what UI you can achieve in a web environment. If you don\'t have lots of Javascript experience, you should probably be pretty conservative in your proposal about what you can achieve in the UI.

- Some of the features are intended to encourage users to use good development methodology, especially when they themselves aren\'t familiar with that methodology. Version control and testing are very much part of that.

- There are existing tools that address many of those features. For instance, there are many testing tools available, and libraries for version control. An IDE is really about making a cohesive experience binding those tools.

- Describing your vision for what a cohesive experience would really look like would be a good strategy for a proposal.

- Repeating this bullet list in some form in your proposal is not a good strategy. This is more intended as a list of some of the challenging aspects of the topic, and some of the open questions. A proposal should respond to these issues.

\-- [Ian Bicking](mailto:ianb@colorstudy.com)
