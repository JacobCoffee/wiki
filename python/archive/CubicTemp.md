# CubicTemp

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

A small, elegant templating engine.

### Masthead 

URL

:   [https://pypi.python.org/pypi/cubictemp](https://pypi.python.org/pypi/cubictemp)

version
:   2.0

licence
:   BSD

platforms
:   All

Python versions
:   2.4+

### Deployment Platforms 

- Any

### Sample 

            <select>
            <!--(for option in optionList)-->
                    <option @!if (option[1]) then "selected" else ""!@>
                    @!option[0]!@
                    </option>
            <!--(end)-->
            </select>

### Suitability 

CubicTemp should be used in association with a good web framework. It is small and simple enough to be modified on a per-project basis.

A back ported version of CubicTemp is available from my page [AshishShrestha](AshishShrestha). This works with Jython 2.1 This allows it to be used with servlet engines like Tomcat. I think the simplicity of CubicTemp and ease of Jython is a cool combination for web development.

### Development Interfaces 

### Environment Access 

### Session, Identification and Authentication 

### Persistence Support 

### Presentation Support 

### InTheirOwnWords 

CubicTemp is an attempt to make a Python templating system that is simple, powerful and well designed. Cubictemp also has built-in protection against cross-site-scripting attac, a very common class of web application vulnerability.

### Comments 

### Hosting 
