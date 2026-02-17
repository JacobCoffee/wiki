# primer_arch_patterns

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

## Introduction 

Often a task's complexity is daunting. Often aspects of a task can be used to guide design decisions in a direction which leads to elegance, robustness, and flexibility. This can lead to more readable code and easier maintenance.

This primer is meant to inspire better design, not to guide it. Please explore patterns of interest to consider implementation. Any feedback or suggestions are welcomed.

## Some Architectural Patterns 

### Singleton and Registry 

If an object needs only one instance, it's a Singleton. Restrict to one instance if you need to coordinate actions or keep track of other classes. For Registry, use a singleton base class to keep a reference to all items.

### Loose Coupling and Chain of Responsibility 

Keep the steps of the process loosely coupled to keep the codebase modular. Call the next function until the process is done.

### Proxy 

Much like proxies in other cases, use an object to interface to another. This can be used to simplify usage of remote resources, to simplify a resource intensive object or process, or to control access to something.

### Observer and Publish-subscribe 

To pass information, either have a subject notify dependents upon state change directly, or use another service, like a Message Service.

### Blackboard 

If you have a data-heavy problem, like object or sound identification, focus on the data. When designing, consider all memory as a blackboard which reads a control component, which uses knowledge sources to operate on the blackboard memory.

### Stateful 

Consider the application as a relation of states, and think about how every action can be made to be a change of state. Essentially, implement a finite state machine.

## Other Design Considerations 

### Async 

If a method does not need to be done in order, try to separate the steps so that the kernel can perform the task, along with others, without keeping similarly-parallel tasks waiting.

### Mapreduce 
