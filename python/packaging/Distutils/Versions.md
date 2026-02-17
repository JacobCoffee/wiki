# Distutils/Versions

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# Proposed Version Schemes 

## Numeric Portion 

Legal/Rational Versions can consist of any number of digits with dots as a field separator. The last field may have alphabetic characters. Proposals for those are explained below.

The sorting of the numeric digits is made by separating the numbers into fields and comparing each number separately. If a version does not have as many fields as the version being compared to, those fields sort before the version that contains a number (even if that number is 0).

Examples:

    1.1 > 1.0
    1.0.0 > 1.0
    1.0.1 > 1.0.0.1000

## Alphabetic Portion 

The last field may contain non numeric characters

### Proposal 1 

They sort in lexographic order. These are always post releases

Examples:

    1.1a > 1.1
    1.1zz > 1.1a

### Proposal 2 

They sort in lexographic order except for the following special names.

- alpha
- beta
- rc

The special names can have a trailing number.

Those are considered pre-releases and sort before the related numbers.

Examples:

    1.1alpha1
    1.1alpha2
    1.1beta
    1.1beta1
    1.1rc1
    1.1
    1.1a
    1.1b
    1.1c
