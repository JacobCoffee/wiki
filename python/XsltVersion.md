# XsltVersion

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

\<?xml version=\"1.0\" encoding=\"ISO-8859-1\"?\>

\<?xml-stylesheet href=\"XsltVersion\" type=\"text/xml\"?\>

\<xsl:stylesheet version=\"1.0\" xmlns:xsl=\"[http://www.w3.org/1999/XSL/Transform\"\>](http://www.w3.org/1999/XSL/Transform%22%3E)

- \<xsl:output method=\"html\" omit-xml-declaration=\"yes\" indent=\"no\"/\>

  \<xsl:template match=\"/\"\>

  - This Wiki is running an XSLT engine by

    \<xsl:value-of select=\"system-property(\'xsl:vendor\')\"/\> (\<a href=\"{system-property(\'xsl:vendor-url\')}\"\>\<xsl:value-of select=\"system-property(\'xsl:vendor-url\')\"/\>\</a\>) implementing XSLT v\<xsl:value-of select=\"system-property(\'xsl:version\')\"/\>

  \</xsl:template\>

\</xsl:stylesheet\>
