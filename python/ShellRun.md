# ShellRun

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

Page status - development of a library (public domain) to run commands through shell is moved to [https://bitbucket.org/techtonik/shellrun](https://bitbucket.org/techtonik/shellrun) along with detailed notes, because it is easier to sync notes with code in repository.

Libraries to run command through system shell, because subprocess suxx:

- [https://github.com/kennethreitz/envoy](https://github.com/kennethreitz/envoy)

- [http://shell-command.readthedocs.org/en/latest/](http://shell-command.readthedocs.org/en/latest/)

subprocess deadlock example:

- TODO

##### API Comparison 

Running:

    r = envoy.run('command')

    r = shell_command.shell_call('command')

Return code, [https://en.wikipedia.org/wiki/Exit_status](https://en.wikipedia.org/wiki/Exit_status)

    # subprocess
    p.returncode

    # envoy
    r.status_code

    # shell_command
    r
