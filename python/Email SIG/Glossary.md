# Email SIG/Glossary

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# Glossary of Terms-of-Art for the Email Package

This page is an attempt to standardize on the language we use to describe concepts relevant to the email module. It also mentions some terms that are deprecated as incorrect or ambiguous, and why.

NOTE: this is a proposed draft, not a final document!

**charset**

:   The term used in the email RFCs for the identifier that specifies how to interpret a set of bytes so as to reconstruct the text characters of the original content. \'charset\' is also the keyword used in MIME headers when specifying a charset. What the RFCs refer to as a charset is more generally called a [character encoding](http://en.wikipedia.org/wiki/Character_encoding). Python documentation generally shortens this to simply \"encoding\". This unfortunately conflicts with the email RFCs use of the term \"encoding\"; see the \"encoding\" entry for more.

    The charset identifiers used in (among other things) MIME are listed in a [special document](http://www.iana.org/assignments/character-sets) on the IANA web site.

**conformant**
:   Conforming to a particular specification or standard. The Internet RFCs use this term to refer to implementations and data that conform to the requirements of the RFC.

**encoding**
:   In Python documentation, this is short for [character encoding](http://en.wikipedia.org/wiki/Character_encoding). In the email RFCs, encoding is short for \"transfer encoding\", and refers to the way in which arbitrary bytes are encoded into US-ASCII so as to produce an RFC conformant byte stream. The RFC defined encodings are \"quoted printable\" and \"base64\".

**idempotent**

:   A property of certain operations in computer science and mathematics. An operation is idempotent if multiple applications of the operation do not change the result. Formally, given an operation \'g\', \'g\' is idempontent if and only if:

    > g(g(x)) = g(x)

    For example, the \'lowercase\' operation is idempotent. There are operations provided by the email package where it makes sense to require either strict idempotence, or idempotence when possible.

**invertible**
:   The email package attempts to maintain *invertibility*. By this we mean that if you feed an input into the package, and later ask for that data to be serialized back out, you should get out the data you put in. For well-formed input, this is an absolute requirement, and any deviation is a bug. For other input, we may find it necessary to break invertibility. Note that invertibility is a stronger requirement on an operation than idempotence, but it applies only when an inverse operation exists.

**raw data**

:   Data in the form it enters the email module parser, or exits the email module generator (primarily the former). [\[\*\]](#id2) A related term is \'wire-format\', the difference being that wire-format data is understood to be RFC conformant. Raw data may or may not be RFC conformant, and may or may not be bytes (if, for example, it comes from a doctest or other text input source).

      ----------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
      [\[\*\]](#id1)   Note that in the past this term has been used ambiguously to also refer to the original source data that was transfer-encoded into the form that is the actual raw data that the email module deals with.
      ----------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

**string**
:   python3 unicode string

**text**
:   unicode text (stored in a python3 string)

**transfer-decoded**
:   Data that has been decoded from wire-format into 8 bit bytes.

**transfer-encoded**
:   Bytes that have been validly encoded per the RFCs for transmission \"over the wire\", ie: to wire-format. Mostly used in the verb form (ex: \"after the data has been transfer-encoded\") in discussing operations involving the RFC defined transfer encodings Quoted Printable and BASE64.

**wire-format**
:   The format that data is in when transmitted \"over the wire\"; which is to say in a binary format rather than unicode, said binary format containing the data of the message transfer-encoded according to the RFCs.
