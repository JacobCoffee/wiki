# YAML

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

YAML is a human-friendly format for structured data, that is both easy to write for humans and still parsable by computers.

### PyYAML parser 

[PyYAML](http://pyyaml.org/) is the most-used and go-to YAML package, which tries to be as compliant as possible with the YAML specs. It is, at its core, C-based. It can both read and write YAML. You can read the [official documentation](https://pyyaml.org/wiki/PyYAMLDocumentation), or try the condensed/simplified version of these docs, with usable example code on this [Python YAML tutorial](https://python.land/data-processing/python-yaml).

When using this package, be careful which function you use. The `load()`{.backtick} function is very powerful and allows arbitrary code execution, while the `safe_load()`{.backtick} function is enough for most use cases. It only allows a subset of the load function, making it a much safer choice. For more details, see also the [load deprecation notice](https://github.com/yaml/pyyaml/wiki/PyYAML-yaml.load(input)-Deprecation).

### YAML examples and usage in notable Python apps 

YAML is a feature-rich language. Some packages that heavily depend on YAML are:

- tmuxp - [http://tmuxp.readthedocs.org/en/latest/examples.html](http://tmuxp.readthedocs.org/en/latest/examples.html)

- ansible - [http://www.ansibleworks.com/docs/YAMLSyntax.html](http://www.ansibleworks.com/docs/YAMLSyntax.html) and [http://www.ansibleworks.com/docs/playbooks.html#id9](http://www.ansibleworks.com/docs/playbooks.html#id9)

- appengine - [https://developers.google.com/appengine/docs/python/config/appconfig](https://developers.google.com/appengine/docs/python/config/appconfig) and [https://github.com/rietveld-codereview/rietveld/blob/master/app.yaml](https://github.com/rietveld-codereview/rietveld/blob/master/app.yaml)

- salt - [http://docs.saltstack.com/topics/tutorials/starting_states.html#default-data-yaml](http://docs.saltstack.com/topics/tutorials/starting_states.html#default-data-yaml)
