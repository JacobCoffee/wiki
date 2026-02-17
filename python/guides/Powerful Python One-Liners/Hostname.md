# Powerful Python One-Liners/Hostname

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# Description 

This is a simple [Powerful Python One-Liners](). It prints the systems\'s hostname to the screen.

# Code 

`from socket import gethostname; print gethostname()`

# Download 

This program has been uploaded to the Wiki. You can download it as an attachment from this page.

Well, sometimes. A lighter-weight variant with desirable properties is

`import os; print os.uname()[1]`

[lwickjr](lwickjr): \--which doesn\`t seem to work on Windows. ![:(](/wiki/europython/img/sad.png ":(")

[snark](./snark.html): \-- use `import platform; print platform.uname()[1]`

[synthesis](./synthesis.html): \-- use `import platform; print platform.node()`
