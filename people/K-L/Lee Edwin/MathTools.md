# LeeEdwin/MathTools

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# Version 1.0 of Ceiling Calculator 

{{{from math import ceil

print \"Ceiling Calculator - Version 1.0\" print print \"What is the value of x?\" x = float(raw_input()) print print \"The ceiling of x is:\" print ceil(x) print print \"Press Enter to quit.\" raw_input()}}}

# Version 1.0 of Absolute Value Calculator 

{{{from math import fabs

print \"Absolute Value - Version 1.0\" print print \"What is the value of x?\" x = float(raw_input()) print print \"The absolute value of x is:\" print fabs(x) print print \"Press Enter to quit.\" raw_input()}}}

# Version 1.0 of Floor Calculator 

{{{from math import floor

print \"Floor Calculator - Version 1.0\" print print \"What is the value of x?\" x = float(raw_input()) print print \"The floor of x is:\" print floor(x) print print \"Press Enter to quit.\" raw_input()}}}

# Version 1.0 of fmod Calculator 

{{{from math import fmod

print \"fmod Calculator - Version 1.0\" print print \"What is the value of x?\" x = float(raw_input()) print print \"What is the value of y?\" y = float(raw_input()) print print \"The result of fmod(x, y) is:\" print fmod(x, y) print print \"Press Enter to quit.\" raw_input()}}}

# Version 1.0 of Mantissa and Exponent Calculator 

{{{from math import frexp

print \"Mantissa and Exponent Calculator - Version 1.0\" print print \"What is the value of x?\" x = float(raw_input()) y = frexp(x) print print \"The mantissa of x is:\" print y\[1\] print print \"The exponent of x is:\" print y\[2\] print print \"Press enter to quit.\" raw_input()}}}
