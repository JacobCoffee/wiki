# Email SIG/DesignThoughts

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# Design Thoughts

::: 
### Guiding Thoughts

- To decide what to do with broken email we need to decide:

  > - To what level does the email module promise to parse conforming wire-format into useful objects?
  > - For non-conforming input, when is it OK to raise an error and return to the calling client rather than handle it? (The answer to this is probably \'never\').
  > - What is the API for accessing and/or mutating unparsable data, and requesting a reparse?

- We should treat backward compatibility the way Python3 did: as something desirable, but not something that prevents us from fixing the warts in the current API. We can worry about a migration strategy later.

- A more property based API would be nice.
:::

::: 
### Required Elements

- The code and documentation should state clearly what RFCs are implemented.

- There are two parallel APIs at the outer level: a bytes API and a string API. We expect that all user facing APIs will have both a string and a bytes version, except in cases where there is no sensible string version of the data (eg: binary attachments).

- Only developers working on the internals of the email package should need to worry about how the data is actually represented in the model.

- When raw data is fed in to the system, serializing the resulting object back to the same data-type as the input data should result in the exact same data whenever possible. (\"Invertability\")

- Once a model has been serialized, serializing it again in the absence of model mutations should produce the same result (\"Idempotence\")

- All headers are represented internally as Header objects. As with all user facing APIs, the Header object must have both a bytes and a string API.

- Ideally, accessing data from the model should never raise an exception.

- Mutating the model should raise exceptions as early as possible.

- As in the current email package, the fundamental model is the Message object. Message objects are recursively defined, and consist of the following parts:

  > - headers: an ordered list of Header objects (in RFC 5322 terms, this is the model of the \'header section\').
  >   - Duplicate headers must be supported
  >   - Header order must be preserved
  >   - As in the current package, a dictionary-like interface will probably also be provided.
  > - body/payload: the data encapsulated by the Message (the model of the RFC 5322 \'body\')
  >   - A Message can be either a terminal node, in which case an object corresponding to its MIME type can be retrieved, or an instance of one of the multipart MIME types, in which case a list of sub-Messages can be retrieved.
  >   - Access to the raw data of the body must be available

- A Message object should provide access to the following for *any* MIME type if the input is parsable:

  > - the raw data that was parsed to create the Message
  > - the Headers built from the header section
  > - the transfer-decoded bytes
  > - if the body is not a MIME multipart, the body instantiated into an object of some sort. The system should provide a way for application programs to determine how payloads of specific MIME types are instantiated into objects. This will presumably be a registration system with a series of default handlers registered by the email package itself for common and useful types, and a generic MIME object for types for which there is no specific handler. All registrations, even the one for the default \'fallback\' object, should be overridable by the application.

- The mainline APIs should emit only RFC compliant data. Access to malformed data (for, eg, error recovery attempts) should be via alternate APIs.

- When parsing raw data, the email package should do the right thing wherever possible (respecting the Postel Principle). When it cannot, it should

  > - construct a defect list that is exposed through the appropriate API (the defect list should include anything not RFC compliant, even if parsable following the Postel Principle).
  > - return an object that is as close as possible to the object that would have been returned if the raw data had been fully parsable, but whose attributes will raise errors if an attempt is made to access an API that would rely on data that was not in fact valid. (ex: suppose the text body cannot be decoded to Unicode via the declared charset. An object would be returned where accessing the string API would raise an error, while the alternate APIs would still provide access to the transfer-decoded data).
  > - the raw data that was parsed to build the object should always be accessible, whether the parse succeeded or failed.

- The API needs to at a minimum have hooks available for an application to store data on disk rather than holding everything in memory. This API should provide the ability to trigger disk storage based on

  > - an aggregate message size threshold
  > - a message part size threshold
  > - both

  The email package should provide a demonstration implementation of these hooks in the spirit of wsgiref.

- Different use cases require different levels of RFC conformance. The API should provide both a relaxed and strict API for modifying the model. (ex: an application might want to use the email module to manipulate email-like messages but without the 998 character line length limit). The parser can use the non-strict API when building the model-plus-defect-list for a non-conformant data stream. (It may also need additional non-API model methods).

- A registration system should also be provided for transfer-encodings, with the RFC standard encodings provided by default. This provides a way to handle new RFC defined encodings and for applications to implement X- encodings.

- It should be possible for third party extensions to add converters to the MIME part registration system (see timezones in the datetime module for a model).
:::

::: 
### Interesting Ideas

- An API for telling the system to store the decoded content of a MIME part in the filename specified in the MIME headers. (If the part is already stored on disk by the disk storage hooks, this might be a simple rename, thus avoiding the data transfer required if this API is not provided).
- The parsing could be lazy, only parsing the MIME sub-parts on request. If so, there should be an API available that requests \"full parsing\" of a Message be done immediately.
- Parsing of the header section and body section could also possibly be done lazily (though parsing the body requires that at least a certain minimum set of headers be parsed).
- After the API is fleshed out (and *only* after) we can map \_\_string\_\_ and \_\_bytes\_\_ to appropriate elements of that API.
- It might be useful for the email package to be able to parse the non-RFC but common \'+\' mailbox extension notation. If so this should be clearly documented as an extension.
- Even the fully-decoded content of a Message could be a Property, if we also expose a decode method that allows the application to do the decoding itself (for example to handle weird cases such as Shift JIS data being labeled as ISO-2022-JP). (This may simply be a specific case of using the alternate \"dirty data\" interface.)
- Instead of trying to pass things like header lengths up and down the call stack, let\'s support a \"formatting policy\" object that can be attached to message objects or the generator that encapsulate things like header wrapping rules, EOL-settings, etc. The generator would then apply the formatting policy to that message object and any other object below it in the MIME hierarchy. Headers might also inherit this policy and be able to override it on a per-header basis. This might also work well for supporting different wrapping policies based on the destination of the message (e.g. messages being spewed out a mail server have different requirements than messages being spewed out of a web server).
:::

::: 
### Issues

- How does the desire for not-quite-ducklike objects for badly formed input data mesh with the desire for a plugin system for instantiating the objects that represent the payloads?
- How does the registration system interact with threading? Can different threads have different registrations?
- We believe that there are no cross-part context items that would prevent the lazy decoding of MIME parts, but this has not been confirmed. It is the case that when parsing an inner MIME part, access to the boundary delimiter for the outer parts is required. There may also be some issues for semantic parsing with Content-ID references.
- Multipart/report could be both a Message-with-sub-Messages *and* a single specialized object type; this possibility should be considered in the API design.
:::
