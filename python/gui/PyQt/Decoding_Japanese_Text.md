# PyQt/Decoding_Japanese_Text

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# Decoding Japanese Text 

The following code was written in response to a [post on comp.lang.python](http://groups.google.com/group/comp.lang.python/msg/cbb6377999249b2c?dmode=source) to show how to obtain a unicode representation of text stored in the Shift-JIS encoding. The original text has also been Base64 encoded for delivery in an e-mail message:

:::: 
::: 
``` 
   1 import base64, sys
   2 from qt import *
   3 
   4 a = \
   5 """SW4gdGhpcyBzYW1wbGUsIGUtbWFpbCB0aXRsZSBhbmQgdGV4dCBhcmUgd3JpdHRlbiBpbiBKYXBh
   6 bmVzZS4gDQpPdXIgbGFuZ3VhZ2UgaGFzIHRocmVlIHR5cGVzIGNhbGxlZCCBZ0thdGFrYW5hgWgs
   7 IIFnSGlyYWdhbmGBaCBhbmQgDQqBZ0thbmppgWguIA0KVGhpcyBlLW1haWwgY29udGFpbnMgYWxs
   8 IHRoZSB0eXBlcy4gDQqDQ4NOg1aDQYLNgmiCd4Jrgm6CYIJjglKBRIJQgk+CyYLEg4GBW4OLi0CU
   9 XILwIA0Kk/qWe4zqkc6JnoKzgrmC6YLngrWCooLFgreC5oFCIA0KgqCCooKkgqaCqIFBg0GDQ4NF
  10 g0eDSSANCoKpgquCrYKvgrGBQYNKg0yDToNQg1IgDQqCs4K1greCuYK7gUGDVINWg1iDWoNcIA0K
  11 gr2Cv4LCgsSCxoFBg16DYINjg2WDZyANCoLIgsmCyoLLgsyBQYNpg2qDa4Nsg20gDQqCzYLQgtOC
  12 1oLZgUGDboNxg3SDd4N6IA0KgtyC3YLegt+C4IFBg32DfoOAg4GDgiANCoLiguSC5oFBg4aDhoOI
  13 IA0KgueC6ILpguqC64FBg4mDioOLg4yDjSANCoLtgvCC8YFBg4+DSYOTIA0KgmCCYYJigmOCZIJl
  14 gmaCZ4JogmmCaoJrgmyCbYJugm+CcIJxgnKCc4J0gnWCdoJ3gniCeSANCoKBgoKCg4KEgoWChoKH
  15 goiCiYKKgouCjIKNgo6Cj4KQgpGCkoKTgpSClYKWgpeCmIKZgpogDQqBQoFBgWmBaoGBgXuBW4GW
  16 gY+BdYF2gUmBlIGQgZOBlYFggYSBg4GbgX6BooGggZmB9CANCpOMi56Tc49hkkqL5pHjgViW2IJS
  17 gXyCUYJUgXyCUiANCoKggqKCqIKikbmV25BWj2iDcoOLglCCVYpLIA0Kg0ODToNWg0GKlI6uie+O
  18 0CANCg=="""
  19 
  20 if __name__ == "__main__":
  21 
  22     app = QApplication(sys.argv)
  23     s = base64.decodestring(a)
  24     qs = QTextCodec.codecForName("Shift-JIS").toUnicode(s)
  25     l = QLabel(qs, None)
  26     l.show()
  27     app.setMainWidget(l)
  28     sys.exit(app.exec_loop())
```
:::
::::

This script decodes the Base64 string, uses the appropriate codec to convert the contents into a unicode representation, and shows the result in a label.

Note that you will need suitable fonts installed on your system to see the result.
