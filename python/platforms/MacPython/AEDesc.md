# MacPython/AEDesc

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

AEDesc (in the `Carbon.AE` extension) is a wrapper for the C type of the same name. An AEDesc is a (mostly) opaque data structure that represents an Apple Event Descriptor and encapsulates the related methods. Note that raw access to the [../FourCharacterCode](./MacPython(2f)FourCharacterCode.html) representing the AEDesc type is available through the `type` attribute, and the raw data stored by the AEDesc is available from the `data` attribute, but you should only use `data` for simple value types and use coercion and/or the accessor methods on anything else.

See also:

- [../AppleEvents](./MacPython(2f)AppleEvents.html)

- [../AppleScript](./MacPython(2f)AppleScript.html)
