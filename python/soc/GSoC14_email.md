# GSoC14_email

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# Ideas for a RFC 6532 API 

## Policy 

- \- the internal charset has to be changeable (or at least a USASCII/UTF8 switch is needed)

## Header 

### \_header_value_parser 

- \- use settings from policy in \_fold

## Steps 

1.  change the Header class in header.py to make the default charset changeable (add \'\_internal_charset\' property)

2.  NOT SURE ABOUT THIS: create new classes in the headerregistry.py (e.g. [UnicodeAddressHeader](./UnicodeAddressHeader.html) as inheritor of [AddressHeader](./AddressHeader.html)

3.  provide an alternative header map (e.g. \_unicode_header_map) using the new classes

4.  [HeaderRegistry](./HeaderRegistry.html): create an inherited class with the \_unicode_header_map as default.

\...

1.  create a policy making use of the above
