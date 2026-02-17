# Email SIG/RelevantRFCs

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# RFCs of Relevance to the Email Package Implementation

::: 
### Base Email RFCs

- [rfc0733](http://tools.ietf.org/html/rfc0733) Standard for the Format of ARPA Network Text Messages
- [rfc0822](http://tools.ietf.org/html/rfc0822) Standard for the Format of ARPA Internet Text Messages
- [rfc2822](http://tools.ietf.org/html/rfc2822) Internet Message Format
- [rfc5322](http://tools.ietf.org/html/rfc5322) Internet Message Format

Each of these RFC\'s obsoletes the one that came before [\[1\]](#id3), but often reference the earlier RFC. We must also pay attention to the obsolete formats because of the [Postel principle](http://en.wikipedia.org/wiki/Robustness_principle)

The parser should have two modes (or there should be two parsers): strict and lax. The lax parser (probably with optional logging) would be for everyday use in handling email received from other sources, the strict parser would be for validation and/or data produced by an application itself.

The email package should produce output that strictly conforms to RFC 5322.
:::

::: 
### MIME

- [rfc2045](http://tools.ietf.org/html/rfc2045) MIME Part One: Format of Internet Message Bodies
- [rfc2046](http://tools.ietf.org/html/rfc2046) MIME Part Two: Media Types
- [rfc2047](http://tools.ietf.org/html/rfc2047) MIME Part Three: Message Header Extensions for Non-ASCII Text
- [rfc2048](http://tools.ietf.org/html/rfc2048) MIME Part Four: Registration Procedures
- [rfc2049](http://tools.ietf.org/html/rfc2049) MIME Part Five: Conformance Criteria and Examples
- [rfc2231](http://tools.ietf.org/html/rfc2231) MIME Parameter Value and Encoded Word Extensions: Character Sets, Languages, and Continuations
:::

::: 
### Specific MIME Content Types

- [rfc1847](http://tools.ietf.org/html/rfc1847) Security Multiparts for MIME: Multipart/Signed and Multipart/Encrypted
- [rfc1894](http://tools.ietf.org/html/rfc1894) An Extensible Message Format for Delivery of Status Notifications
:::

::: 
### Mailing List Headers

- [rfc2369](http://tools.ietf.org/html/rfc2369) The Use of URLs as Meta-Syntax for Core Mail List Commands and their Transport through Message Header Fields
- [rfc2919](http://tools.ietf.org/html/rfc2919) A Structured Field and Namespace for the Identification of Mailing Lists
:::

::: 
### Other

- [rfc4648](http://tools.ietf.org/html/rfc4648) The Base16, Base32, and Base64 Data Encodings
:::

::::: 
### Additional Considerations

An auxiliary module should provide access to the registered IANA data specified by the RFCs. We make use of the data from the mimetimes module, which overlaps with this requirement, so we need to coordinate with the maintainers of that module [\[2\]](#id4).

One of the sets of IANA data we need to pay attention to is the [list of charset identifiers](http://www.iana.org/assignments/character-sets).

We also make use of URLs ([rfc3986](http://tools.ietf.org/html/rfc3986)), and will need to coordinate with the maintainers of urllib for that support.

We also need to be aware of the RFCs that are relevant to the modules that share concerns with the email package and/or are consumers of email package services:

::: 
#### HTTP

- [RFC2616](http://tools.ietf.org/html/rfc2616) Hypertext Transfer Protocol \-- HTTP/1.1
:::

::: 
#### Netnews

- [RFC1036](http://tools.ietf.org/html/rfc1036) Standard for Interchange of USENET Messages
- [RFC3977](http://tools.ietf.org/html/rfc3977) Network News Transfer Protocol (NNTP)
:::
:::::

::: 
### Extensions

There are also email extensions that we may want to support. This list is not complete.

- [RFC2111](http://tools.ietf.org/html/rfc2111) Content-ID and Message-ID Uniform Resource Locators
- [RFC2112](http://tools.ietf.org/html/rfc2112) The MIME Multipart/Related Content-type

  ---------------------------- ---------------------------------------------------
  [\[1\]](#id1)   In fact, rfc0733 obsoletes several previous RFCs.
  ---------------------------- ---------------------------------------------------

  ---------------------------- -----------------------------------------------------------------------------------------------------------------------
  [\[2\]](#id2)   mimetypes does not currently have a maintainer listed in maintainers.rst, which may mean we get to tackle it as well.
  ---------------------------- -----------------------------------------------------------------------------------------------------------------------
:::
