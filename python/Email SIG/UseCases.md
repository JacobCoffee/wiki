# Email SIG/UseCases

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# Email Package Use Cases 

The following use cases for the email package API are gleaned from the email-sig mailing list and are collected here for reference. Note that \'strings\' are python3 unicode strings.

Debugging
:   The email module should not make it harder than necessary to debug programs that use it.

Testing
:   Complete messages may be input as strings (eg: from a doctest).

MUA #1
:   Composition. Input will be strings and multimedia file names, output will be bytes. Will attributes of message objects be manipulated? Not in a conventional MUA, but an email-based MUA might find uses for that.

MUA #2
:   Reading. Input will often be bytes (spool files, IMAP data). Could be strings, though, depending on the internal format of folders. Output will be strings and multimedia objects. Lots of string processing, especially generating folder directory displays from message headers.

Mailing list processor
:   Message input will be bytes. Configuration input, including heading and footer texts that may be added are likely to be strings. Header manipulation (adding topics, sequence numbers, RFC 2369 headers) most conveniently done with strings. Output will be bytes. A mailing list processor also needs to be able to add new headers, and add prefixes and suffixes to existing header bodies after checking that the prefix or suffix are not already present. It also needs to be able to add headers or footers to the message body, possibly inside mime subparts when possible, or as a separate mime part.

Mailing list archiver #1
:   Archive as web pages. Input will be bytes or message objects, output will be strings (typically HTML documents or XML fragments).

Mailing list archiver #2
:   Archive in wire-format. Input will be bytes or possibly message objects, output will be some strings (searchable headers, etc) and bytes.

Archiving
:   In general the archiver use case requires that serialization of a message or message part produces output without generating an exception. The wire-format archiver use case argues for it being possible to recover an exact copy of the input even when invalid; however, an API for producing an RFC compliant version by making adjustments in the case of Messages with defects would be useful for some archivers.

SpamBayes
:   input is very dirty raw data from the network, which is analyzed to the extent possible, and then a couple of headers are added. The most important characteristics for this application is that the message itself remain unchanged except for the header additions.

Spam/virus detection
:   Input may be bytes or message objects. Lots of internal string processing; in most cases the text/\* parts need to be converted to strings before grepping; in some cases even images or executables may be reconstituted to look for malware signatures. Output may be a flag or signal, or the message itself may be edited (typically to provide headers recording degree of spamminess, trace headers, maybe a body heading; in some cases, a new message may be generated with the suspected spam as a message/rfc822 MIME body part). This use case requires that feeding an input stream to the email package always produces a valid Message object, along with a defect report. The defect report and inspection of the valid parts of the message will be used in making decisions about the nature of message.

Handling large messages or subparts
:   Some applications may want to be able to handle large messages or attachments (eg: a message with a series of 10MB images). It must be possible to process these messages without holding all of the data in memory at one time. (Design note: it may be that all that we provide is hooks, but it must be possible to use these hooks to input a data stream, store messages/message parts on disk, and still have a fully consistent Message object that works with the normal API.)

Handling non-email data in RFC822-like format
:   A number of applications use RFC822-style headers (and sometimes bodies) to store non-email data. The email package should expose the parts of the API that deal with headers in a fashion that makes it reusable in such applications, as well as allowing such data to be input to the parser and produce valid Message objects. Input and output could be strings or bytes in any combination, depending on the application. This use case requires the ability within the API to optionally output lines that are longer than the maximum specified by the email RFCs (RFC 5322). This use case may also require acceptance of UTF-16 or UTF-32 (and -BE/-LE variants) charsets, even though CR LF are no longer bytes in those charsets.

Handling non-email data in MIME format
:   The MIME format is used in places other than email (http, for example). The email package MIME API should be usable in such applications.

Python standard library
:   The http package, the urllib package, the cgi module, and pytdoc are all clients of the current email package. (TODO: figure out exactly what they are using it for and add here as separate use cases.)

Handling HTTP data
:   It should be possible to feed an http stream containing headers and content to the parser and get back a valid Message object. One use case still in use in the field as of 2010-04-05 is parsing the \'mutlipart/byteranges\' content body returned as the payload of a \'206 Partial Content\' response (in response to a request with \'Range\' header(s). Zope currently uses \'multifile\' to do this parsing.

Netnews
:   Netnews articles are almost identical in format to email, but have a few additional quirks. The email package must be able to handle netnews articles, turn them into usable Message objects, and produce wire-format articles from modified or constructed Message objects.

NNTP
:   It should be possible to take the information that can be obtained from nttplib and use the email package to process it. In particular, this means that headers in wire format may be obtained and parsed separately from the message body.

Handling pathological data #1
:   Suppose an email-based MTA/LDA is handed a stream of random bytes. The \'correct\' response of the MTA/LDA (eg: if it is sendmail compatible) may well be to accept that data, prepend default From, Date, and Message-ID headers and send it on its way.

Handling pathological data #2
:   Suppose an incoming email has data that cannot be correctly parsed into MIME parts and/or decoded from wire format and/or decoded to Unicode. Salvage heuristics should be made available that can help determined clients to obtain as much data as they can from the message. Truncated MIME parts may still contain useful data in the part that exists; parts of the data may be able to be decoded, even if not all.

Multipart/report
:   An email-based MTA would want a way to take an existing Message object and generate new Message object that embodies a multipart/report per RFC 1892. (This may be out of scope for the email package.)

distutils
:   PEP 345 defines RFC822 compatible headers. The email package should be able to correctly parse these headers given that they are defined to be RFC2822 compliant.

issue 3609
:   the cgi package currently has parse_header and parse_multipart functions. It should be possible to replace these with simple wrappers around email package API calls.

reStructuredText
:   Docutils uses RFC 2822-like fields to parse reST files, e.g. PEPs. It could perhaps benefit from using email instead of regexes.
